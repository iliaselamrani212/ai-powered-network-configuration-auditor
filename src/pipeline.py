"""
PIPELINE UNIFIE - orchestration pour l'API
==========================================
Une fonction unique auditer_xml(chemin_xml, workdir) qui enchaine :
  1. parser         : XML -> CSV (dans workdir/tables)
  2. detection_ml   : voisins -> anomalies
  3. conformite     : tous les objets -> non-conformites
  4. rag_explain    : explications metier (si Ollama dispo)

Chaque audit travaille dans son propre 'workdir' isole (multi-utilisateurs).
Renvoie un dict de resultats en memoire (pas seulement des fichiers).

L'index ChromaDB (les PDF/fiches) reste PARTAGE et construit une seule fois.
"""

from pathlib import Path
import pandas as pd

# On importe les briques existantes
from parser import parse, exporter
import detection_ml
import conformite


def _detecter_anomalies(tables_dir):
    """Detection statistique (couche 2) sur un dossier de tables donne."""
    anomalies = []
    for techno, nom in detection_ml.FICHIERS.items():
        chemin = tables_dir / nom
        if chemin.exists():
            anomalies.extend(detection_ml.auditer_fichier(chemin, techno))
    return pd.DataFrame(anomalies)


def _detecter_conformite(tables_dir):
    """Audit de conformite (mission 2) sur un dossier de tables donne."""
    non_conf = []
    for f in sorted(tables_dir.glob("*.csv")):
        type_objet = f.name.replace("vsData", "").replace(".csv", "")
        try:
            df = pd.read_csv(f)
        except Exception:
            continue
        if "DN" not in df.columns:
            continue
        non_conf.extend(conformite.volet_a(df, type_objet))
        if f.name not in conformite.FICHIERS_VOISINS:
            non_conf.extend(conformite.volet_b(df, type_objet))
    return pd.DataFrame(non_conf)


def auditer_xml(chemin_xml, workdir, avec_rag=True):
    """
    Pipeline complet sur un fichier XML.
    - chemin_xml : le fichier a auditer
    - workdir    : dossier de travail isole pour cet audit
    - avec_rag   : si True, genere les explications (necessite Ollama)
    Retourne un dict de resultats.
    """
    workdir = Path(workdir)
    tables_dir = workdir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    # --- 1. PARSER : XML -> CSV ---
    objets = parse(Path(chemin_xml))
    exporter(objets, tables_dir)

    stats = {
        "nb_objets": sum(len(v) for v in objets.values()),
        "nb_types": len(objets),
        "nb_voisins_4g": len(objets.get("vsDataEUtranCellRelation", [])),
        "nb_voisins_3g": len(objets.get("vsDataUtranCellRelation", [])),
        "nb_voisins_2g": len(objets.get("vsDataGeranCellRelation", [])),
    }

    # --- 2. DETECTION (couche 2) ---
    df_anomalies = _detecter_anomalies(tables_dir)

    # --- 3. CONFORMITE (mission 2) ---
    df_conformite = _detecter_conformite(tables_dir)

    resultats = {
        "stats": stats,
        "anomalies": df_anomalies.to_dict(orient="records"),
        "non_conformites": df_conformite.to_dict(orient="records"),
        "explications_anomalies": [],
        "explications_non_conformites": [],
    }

    # --- 4. RAG (explications) - optionnel ---
    if avec_rag:
        try:
            import rag_explain
            resultats["explications_anomalies"] = _expliquer(df_anomalies, rag_explain, "anomalie")
            resultats["explications_non_conformites"] = _expliquer(df_conformite, rag_explain, "conformite")
        except Exception as e:
            resultats["rag_erreur"] = f"RAG indisponible : {e}"

    return resultats


def _expliquer(df, rag_explain, genre):
    """Genere les explications pour chaque ligne d'un DataFrame."""
    if df.empty:
        return []
    import chromadb
    client = chromadb.PersistentClient(path=str(rag_explain.CHROMA_DIR))
    collection = client.get_collection(rag_explain.COLLECTION)
    fiches = rag_explain.charger_fiches(rag_explain.FICHES_TXT)

    normaliser = (rag_explain.cas_depuis_anomalie if genre == "anomalie"
                  else rag_explain.cas_depuis_conformite)

    sorties = []
    for _, ligne in df.iterrows():
        cas = normaliser(ligne)
        explication, avec_fiche = rag_explain.expliquer_cas(collection, fiches, cas)
        sorties.append({**cas, "explication": explication, "source_fiche": avec_fiche})
    return sorties
