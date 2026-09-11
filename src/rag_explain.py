"""
COUCHE 3 - RAG : EXPLICATION (Mission 1 + Mission 2)
====================================================
Explique en langage metier :
  - les ANOMALIES statistiques   (outputs/anomalies.csv, couche 2)
  - les NON-CONFORMITES          (outputs/non_conformites.csv, mission 2)

Meme mecanisme RAG pour les deux :
  RETRIEVE : fiche verifiee du parametre (par nom) + chunks PDF (semantique)
  AUGMENT  : prompt = fiche prioritaire + PDF + details du cas
  GENERATE : llama3.2, sans inventer

Produit :
  outputs/explications_anomalies.md
  outputs/explications_non_conformites.md

    python src/rag_explain.py                 # explique les deux
    python src/rag_explain.py anomalies       # seulement les anomalies
    python src/rag_explain.py conformite      # seulement les non-conformites
"""

import sys
from pathlib import Path
import pandas as pd
import chromadb
import ollama

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "outputs" / "chroma"
FICHES_TXT = BASE_DIR / "docs" / "parametres_ericsson.txt"

ANOMALIES_CSV = BASE_DIR / "outputs" / "anomalies.csv"
CONFORMITE_CSV = BASE_DIR / "outputs" / "non_conformites.csv"
OUT_ANOMALIES = BASE_DIR / "outputs" / "explications_anomalies.md"
OUT_CONFORMITE = BASE_DIR / "outputs" / "explications_non_conformites.md"

EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2"
COLLECTION = "ericsson_params"
TOP_K = 4


# --------------------------------------------------------------------------
# Chargement des fiches verifiees (recuperation directe par nom)
# --------------------------------------------------------------------------
def charger_fiches(chemin):
    texte = Path(chemin).read_text(encoding="utf-8")
    blocs = texte.split("### PARAMETRE")
    fiches = {}
    for b in blocs[1:]:
        contenu = "### PARAMETRE" + b.strip()
        titre = b.strip().split("\n")[0].replace("#", "").strip().lower()
        fiches[titre] = contenu
    return fiches


def fiche_pour(param, fiches):
    base = param.lower().split(".")[0]
    for titre, contenu in fiches.items():
        if base in titre:
            return contenu
    return None


# --------------------------------------------------------------------------
# RAG : recuperation + generation
# --------------------------------------------------------------------------
def embed_requete(texte):
    return ollama.embeddings(model=EMBED_MODEL, prompt=texte)["embedding"]


def retrieve_pdf(collection, param, k=TOP_K):
    vecteur = embed_requete(param)
    res = collection.query(query_embeddings=[vecteur], n_results=k)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    return [d for d, m in zip(docs, metas) if m.get("type") != "fiche"]


def construire_prompt(cas, fiche, chunks_pdf):
    """cas est un dict normalise : parametre, valeur_trouvee, reference, contexte, nature."""
    param = cas["parametre"]
    parties = []
    if fiche:
        parties.append(f"[FICHE VERIFIEE - source prioritaire]\n{fiche}")
    for i, c in enumerate(chunks_pdf):
        parties.append(f"[Extrait PDF {i+1}]\n{c}")
    contexte_doc = "\n\n".join(parties)

    return f"""Tu es un expert en configuration de reseaux mobiles Ericsson.
Ne commence pas par une salutation, va droit au fait.

Voici la documentation disponible (la FICHE VERIFIEE est la source la plus fiable) :

{contexte_doc}

REGLE ABSOLUE :
- Utilise UNIQUEMENT les informations ci-dessus.
- Priorise la FICHE VERIFIEE si presente.
- Si rien ne decrit le parametre "{param}", reponds EXACTEMENT :
  "La documentation indexee ne contient pas d'information exploitable sur ce parametre."
- N'invente RIEN.

Cas detecte ({cas['nature']}) :
  - {cas['contexte']}
  - Parametre : {param}
  - Valeur trouvee : {cas['valeur_trouvee']}
  - Reference / attendu : {cas['reference']}

Explique en francais, de facon concise (4 a 6 phrases) :
  1. A quoi sert ce parametre.
  2. Pourquoi cette valeur pose probleme (ecart a la reference).
  3. L'impact possible sur le reseau."""


def generer(prompt):
    rep = ollama.chat(
        model=GEN_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.1},
    )
    return rep["message"]["content"].strip()


def expliquer_cas(collection, fiches, cas):
    fiche = fiche_pour(cas["parametre"], fiches)
    chunks = retrieve_pdf(collection, cas["parametre"])
    prompt = construire_prompt(cas, fiche, chunks)
    return generer(prompt), (fiche is not None)


# --------------------------------------------------------------------------
# Normalisation des deux formats de CSV vers un "cas" commun
# --------------------------------------------------------------------------
def cas_depuis_anomalie(ligne):
    return {
        "DN": ligne["DN"],
        "parametre": ligne["colonne_deviante"],
        "valeur_trouvee": ligne["valeur_trouvee"],
        "reference": f"majorite des voisins = {ligne['valeur_majoritaire']}",
        "contexte": f"Technologie : {ligne['technologie']} | score {ligne['score']}",
        "nature": "anomalie statistique (couche 2)",
    }


def cas_depuis_conformite(ligne):
    return {
        "DN": ligne["DN"],
        "parametre": ligne["parametre"],
        "valeur_trouvee": ligne["valeur_trouvee"],
        "reference": ligne["reference"],
        "contexte": f"Type d'objet : {ligne['type_objet']} | {ligne['volet']}",
        "nature": f"non-conformite ({ligne['volet']})",
    }


# --------------------------------------------------------------------------
# Boucle principale (generique)
# --------------------------------------------------------------------------
def expliquer_fichier(csv_path, out_md, normaliser, titre):
    if not Path(csv_path).exists():
        print(f"(absent) {csv_path}")
        return
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_collection(COLLECTION)
    fiches = charger_fiches(FICHES_TXT)

    df = pd.read_csv(csv_path)
    print(f"{titre} : {len(df)} cas a expliquer.")

    lignes_md = [f"# {titre}\n"]
    for i, ligne in df.iterrows():
        cas = normaliser(ligne)
        explication, avec_fiche = expliquer_cas(collection, fiches, cas)
        etat = "fiche+pdf" if avec_fiche else "pdf seul"
        print(f"  [{i+1}/{len(df)}] {cas['parametre']} [{etat}]")

        lignes_md.append(f"## Cas {i+1} : {cas['parametre']}\n")
        lignes_md.append(f"- **DN** : `{cas['DN']}`")
        lignes_md.append(f"- **Nature** : {cas['nature']}")
        lignes_md.append(f"- **Contexte** : {cas['contexte']}")
        lignes_md.append(f"- **Valeur trouvee** : {cas['valeur_trouvee']}")
        lignes_md.append(f"- **Reference** : {cas['reference']}\n")
        lignes_md.append(f"**Explication :**\n\n{explication}\n")
        lignes_md.append("---\n")

    Path(out_md).write_text("\n".join(lignes_md), encoding="utf-8")
    print(f"  -> ecrit : {out_md}\n")


def main():
    quoi = sys.argv[1] if len(sys.argv) > 1 else "tout"

    if quoi in ("tout", "anomalies"):
        expliquer_fichier(ANOMALIES_CSV, OUT_ANOMALIES,
                          cas_depuis_anomalie,
                          "Rapport - Explications des anomalies (couche 2)")

    if quoi in ("tout", "conformite"):
        expliquer_fichier(CONFORMITE_CSV, OUT_CONFORMITE,
                          cas_depuis_conformite,
                          "Rapport - Explications des non-conformites (mission 2)")


if __name__ == "__main__":
    main()
