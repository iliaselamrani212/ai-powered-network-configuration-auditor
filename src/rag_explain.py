"""
COUCHE 3 - RAG : INTERROGATION (Phase 2) - Mission 1
====================================================
Pour chaque anomalie de outputs/anomalies.csv :
  1. RETRIEVE : recupere la fiche verifiee du parametre DIRECTEMENT (par nom),
     puis complete avec la recherche semantique dans les PDF.
  2. AUGMENT  : prompt = fiche verifiee (prioritaire) + chunks PDF + anomalie
  3. GENERATE : Ollama redige l'explication, sans inventer.

Produit outputs/explications.md
    python src/rag_explain.py
"""

from pathlib import Path
import pandas as pd
import chromadb
import ollama

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "outputs" / "chroma"
FICHES_TXT = BASE_DIR / "docs" / "parametres_ericsson.txt"
ANOMALIES_CSV = BASE_DIR / "outputs" / "anomalies.csv"
OUT_MD = BASE_DIR / "outputs" / "explications.md"

EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2"
COLLECTION = "ericsson_params"
TOP_K = 4


def charger_fiches(chemin):
    """Retourne un dict {nom_parametre_minuscule: texte_fiche}."""
    texte = Path(chemin).read_text(encoding="utf-8")
    blocs = texte.split("### PARAMETRE")
    fiches = {}
    for b in blocs[1:]:
        contenu = "### PARAMETRE" + b.strip()
        # le titre est sur la 1re ligne : "### PARAMETRE hoSuccLevel ###"
        titre = b.strip().split("\n")[0].replace("#", "").strip().lower()
        fiches[titre] = contenu
    return fiches


def fiche_pour(param, fiches):
    """Cherche une fiche dont le titre contient le nom du parametre."""
    p = param.lower()
    # 1) correspondance directe sur le debut du nom (ex: mobilityStatus.available -> mobilityStatus)
    base = p.split(".")[0]
    for titre, contenu in fiches.items():
        if base in titre:
            return contenu
    return None


def embed_requete(texte):
    return ollama.embeddings(model=EMBED_MODEL, prompt=texte)["embedding"]


def retrieve_pdf(collection, param, k=TOP_K):
    """Chunks PDF pertinents (contexte complementaire)."""
    vecteur = embed_requete(param)
    res = collection.query(query_embeddings=[vecteur], n_results=k)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    return [d for d, m in zip(docs, metas) if m.get("type") != "fiche"]


def construire_prompt(anomalie, fiche, chunks_pdf):
    param = anomalie["colonne_deviante"]
    parties = []
    if fiche:
        parties.append(f"[FICHE VERIFIEE - source prioritaire]\n{fiche}")
    for i, c in enumerate(chunks_pdf):
        parties.append(f"[Extrait PDF {i+1}]\n{c}")
    contexte = "\n\n".join(parties)

    return f"""Tu es un expert en configuration de reseaux mobiles Ericsson.

Voici la documentation disponible (la FICHE VERIFIEE est la source la plus
fiable, utilise-la en priorite) :

{contexte}

REGLE ABSOLUE :
- Utilise UNIQUEMENT les informations ci-dessus.
- Base-toi en priorite sur la FICHE VERIFIEE si elle est presente.
- Si rien ne decrit le parametre "{param}", reponds EXACTEMENT :
  "La documentation indexee ne contient pas d'information exploitable sur ce parametre."
- N'invente RIEN.

Anomalie detectee :
  - Technologie : {anomalie['technologie']}
  - Parametre : {param}
  - Valeur trouvee : {anomalie['valeur_trouvee']}
  - Valeur de la majorite des voisins : {anomalie['valeur_majoritaire']}

Explique en francais, de facon concise (4 a 6 phrases) :
  1. A quoi sert ce parametre.
  2. Pourquoi cette valeur devie de la majorite.
  3. L'impact possible sur le reseau."""


def generer(prompt):
    rep = ollama.chat(
        model=GEN_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.1},
    )
    return rep["message"]["content"].strip()


def expliquer_anomalies():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_collection(COLLECTION)
    fiches = charger_fiches(FICHES_TXT)

    df = pd.read_csv(ANOMALIES_CSV)
    print(f"{len(df)} anomalies a expliquer.\n")

    lignes_md = ["# Rapport d'audit - Explications des anomalies\n"]

    for i, anomalie in df.iterrows():
        param = anomalie["colonne_deviante"]
        fiche = fiche_pour(param, fiches)            # recuperation DIRECTE
        chunks_pdf = retrieve_pdf(collection, param) # contexte semantique
        prompt = construire_prompt(anomalie, fiche, chunks_pdf)
        explication = generer(prompt)

        etat = "fiche+pdf" if fiche else "pdf seul"
        print(f"[{i+1}/{len(df)}] {param} ({anomalie['technologie']}) [{etat}] OK")

        lignes_md.append(f"## Anomalie {i+1} : {param} ({anomalie['technologie']})\n")
        lignes_md.append(f"- **DN** : `{anomalie['DN']}`")
        lignes_md.append(f"- **Valeur trouvee** : {anomalie['valeur_trouvee']} "
                         f"(majorite : {anomalie['valeur_majoritaire']})")
        lignes_md.append(f"- **Score** : {anomalie['score']}\n")
        lignes_md.append(f"**Explication :**\n\n{explication}\n")
        lignes_md.append("---\n")

    OUT_MD.write_text("\n".join(lignes_md), encoding="utf-8")
    print(f"\nRapport ecrit : {OUT_MD}")


if __name__ == "__main__":
    expliquer_anomalies()
