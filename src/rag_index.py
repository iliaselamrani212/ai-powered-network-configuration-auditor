"""
COUCHE 3 - RAG : INDEXATION (Phase 1) - version amelioree
=========================================================
Construit la base vectorielle a partir de DEUX sources :
  1. docs/parametres_ericsson.txt : fiches VERIFIEES (une par parametre),
     decoupees par fiche (delimiteur "### PARAMETRE"). Prioritaires.
  2. Les PDF Ericsson, extraits proprement avec pdfplumber (lignes
     reconstituees par position), filtres pour retirer le bruit.

Embeddings via Ollama (nomic-embed-text), stockage ChromaDB.
    python src/rag_index.py
"""

from pathlib import Path
from collections import defaultdict
import pdfplumber
import chromadb
import ollama

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
CHROMA_DIR = BASE_DIR / "outputs" / "chroma"

FICHES_TXT = "parametres_ericsson.txt"
PDFS = ["ericsson_gold.pdf", "ericsson_reco.pdf"]

EMBED_MODEL = "nomic-embed-text"
COLLECTION = "ericsson_params"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


def charger_fiches(chemin):
    """Decoupe le fichier de fiches par '### PARAMETRE'. Un chunk = une fiche."""
    texte = Path(chemin).read_text(encoding="utf-8")
    blocs = texte.split("### PARAMETRE")
    fiches = []
    for b in blocs[1:]:                       # [0] = en-tete, on saute
        fiche = "### PARAMETRE" + b.strip()
        fiches.append(fiche)
    return fiches


def extraire_pdf_propre(chemin):
    """Extrait le texte d'un PDF en reconstituant les lignes par position (pdfplumber)."""
    texte = []
    pdf = pdfplumber.open(str(chemin))
    for page in pdf.pages:
        words = page.extract_words()
        lignes = defaultdict(list)
        for w in words:
            lignes[round(w["top"])].append((w["x0"], w["text"]))
        for top in sorted(lignes):
            mots = [t for _, t in sorted(lignes[top])]
            texte.append(" ".join(mots))
    pdf.close()
    return "\n".join(texte)


def est_bruit(ligne):
    """Vrai si la ligne est du bruit (liste de noms, titre deforme, trop courte)."""
    mots = ligne.split()
    if len(mots) < 6:
        return True
    # titres deformes : beaucoup de mots d'une seule lettre
    isoles = sum(1 for m in mots if len(m) <= 1)
    if isoles > len(mots) * 0.3:
        return True
    return False


def nettoyer(texte):
    """Retire les lignes de bruit, garde les lignes descriptives."""
    lignes = [l.strip() for l in texte.splitlines() if l.strip()]
    lignes = [l for l in lignes if not est_bruit(l)]
    return "\n".join(lignes)


def chunker(texte, taille=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    debut = 0
    while debut < len(texte):
        m = texte[debut:debut + taille].strip()
        if m:
            chunks.append(m)
        debut += taille - overlap
    return chunks


def embed(textes):
    return [ollama.embeddings(model=EMBED_MODEL, prompt=t)["embedding"] for t in textes]


def indexer():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass
    collection = client.create_collection(COLLECTION)

    tous_chunks, tous_ids, tous_metas = [], [], []

    # --- Source 1 : fiches verifiees (prioritaires) ---
    chemin_fiches = DOCS_DIR / FICHES_TXT
    if chemin_fiches.exists():
        fiches = charger_fiches(chemin_fiches)
        print(f"Fiches verifiees : {len(fiches)} fiches")
        for i, f in enumerate(fiches):
            tous_chunks.append(f)
            tous_ids.append(f"fiche_{i}")
            tous_metas.append({"source": "fiches_verifiees", "type": "fiche"})

    # --- Source 2 : PDF extraits proprement ---
    for nom_pdf in PDFS:
        chemin = DOCS_DIR / nom_pdf
        if not chemin.exists():
            print(f"  (absent) {nom_pdf}")
            continue
        print(f"Traitement PDF {nom_pdf} ...")
        texte = nettoyer(extraire_pdf_propre(chemin))
        chunks = chunker(texte)
        print(f"  {len(chunks)} chunks (apres filtrage du bruit)")
        for i, c in enumerate(chunks):
            tous_chunks.append(c)
            tous_ids.append(f"{nom_pdf}_{i}")
            tous_metas.append({"source": nom_pdf, "type": "pdf"})

    # --- Embeddings + stockage (par lots) ---
    print(f"\nCalcul des embeddings pour {len(tous_chunks)} chunks ...")
    LOT = 100
    for debut in range(0, len(tous_chunks), LOT):
        fin = debut + LOT
        vecteurs = embed(tous_chunks[debut:fin])
        collection.add(
            ids=tous_ids[debut:fin],
            documents=tous_chunks[debut:fin],
            embeddings=vecteurs,
            metadatas=tous_metas[debut:fin],
        )
        print(f"  {min(fin, len(tous_chunks))}/{len(tous_chunks)}")

    print(f"\nIndexation terminee : {len(tous_chunks)} chunks dans ChromaDB.")


if __name__ == "__main__":
    indexer()
