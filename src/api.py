"""
BACKEND FASTAPI - API d'audit de configuration reseau
=====================================================
Endpoints :
  POST /audit                  : depose un XML, lance l'audit en arriere-plan,
                                 renvoie un job_id
  GET  /audit/{job_id}/status  : statut du traitement
  GET  /audit/{job_id}/report  : rapport complet (JSON) quand pret
  GET  /health                 : verifie que l'API et Ollama repondent

Lancement :
  uv run uvicorn src.api:app --reload --port 8000
"""

import uuid
import tempfile
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline import auditer_xml

app = FastAPI(title="Auditeur de configuration reseau Ericsson", version="1.0")

# CORS : autorise le frontend (React) a appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # en prod : restreindre a l'URL du front
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stockage en memoire des jobs (pour un prototype ; en prod : Redis/DB)
JOBS = {}


def _traiter(job_id, xml_path, workdir):
    """Tache d'arriere-plan : lance le pipeline complet."""
    try:
        JOBS[job_id]["status"] = "en_cours"
        resultats = auditer_xml(xml_path, workdir, avec_rag=True)
        JOBS[job_id]["status"] = "termine"
        JOBS[job_id]["resultats"] = resultats
    except Exception as e:
        JOBS[job_id]["status"] = "erreur"
        JOBS[job_id]["erreur"] = str(e)
    finally:
        # nettoie le dossier de travail (garde les resultats en memoire)
        shutil.rmtree(workdir, ignore_errors=True)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/audit")
async def lancer_audit(background_tasks: BackgroundTasks, fichier: UploadFile = File(...)):
    if not fichier.filename.lower().endswith(".xml"):
        raise HTTPException(400, "Le fichier doit etre un .xml")

    job_id = str(uuid.uuid4())
    workdir = Path(tempfile.mkdtemp(prefix=f"audit_{job_id}_"))
    xml_path = workdir / fichier.filename

    # sauvegarde le fichier uploade
    with open(xml_path, "wb") as f:
        shutil.copyfileobj(fichier.file, f)

    JOBS[job_id] = {"status": "en_attente", "nom_fichier": fichier.filename}
    background_tasks.add_task(_traiter, job_id, str(xml_path), str(workdir))

    return {"job_id": job_id, "status": "en_attente"}


@app.get("/audit/{job_id}/status")
def statut(job_id: str):
    if job_id not in JOBS:
        raise HTTPException(404, "job_id inconnu")
    job = JOBS[job_id]
    reponse = {"job_id": job_id, "status": job["status"]}
    if job["status"] == "erreur":
        reponse["erreur"] = job.get("erreur", "")
    return reponse


@app.get("/audit/{job_id}/report")
def rapport(job_id: str):
    if job_id not in JOBS:
        raise HTTPException(404, "job_id inconnu")
    job = JOBS[job_id]
    if job["status"] != "termine":
        raise HTTPException(409, f"Audit non termine (statut: {job['status']})")
    return {
        "job_id": job_id,
        "nom_fichier": job["nom_fichier"],
        "resultats": job["resultats"],
    }
