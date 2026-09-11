"""
COUCHE 3 - MISSION 2 : AUDIT DE CONFORMITE (document entier)
============================================================
Audite TOUS les types d'objets (68 CSV), avec deux volets complementaires :

  VOLET A - Regles de bonnes pratiques :
    compare certains parametres a une valeur de reference SURE
    (ex: isHoAllowed doit etre true). Detecte meme les defauts generalises.
    S'applique a tout objet portant ces parametres.

  VOLET B - Coherence interne :
    pour chaque type d'objet (SAUF les voisins, deja traites par la couche 2),
    detecte les objets qui devient de la majorite de leur propre type.
    Ne necessite aucun document de reference.

Produit outputs/non_conformites.csv
    python src/conformite.py
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
TABLES_DIR = BASE_DIR / "outputs" / "tables"
OUT_CSV = BASE_DIR / "outputs" / "non_conformites.csv"

# Colonnes qui ne sont jamais des reglages a auditer (identite, dates, pointeurs, temporaires)
COLONNES_IGNORE = {
    "DN", "id", "vsDataType", "adjacentCell", "extGeranCellRef",
    "timeOfCreation", "timeOfLastModification", "lastModification", "createdBy",
    "userLabel",
}

# Les 3 fichiers de voisins : exclus du volet B (couverts par la couche 2)
FICHIERS_VOISINS = {
    "vsDataEUtranCellRelation.csv",
    "vsDataUtranCellRelation.csv",
    "vsDataGeranCellRelation.csv",
}

# --- VOLET A : table de references SURE -----------------------------------
# Valeur attendue pour des parametres dont la "bonne" valeur est connue avec
# une confiance raisonnable (bonnes pratiques / defaut ANR / bon sens metier).
# On compare en minuscules pour les booleens.
REGLES_BONNES_PRATIQUES = {
    "isHoAllowed": "true",                 # le handover doit etre autorise
    "isRemoveAllowed": "true",             # defaut ANR
    "mobilityStatus.available": "true",    # le voisin doit etre disponible
}


def est_temporaire(colonne):
    """Ecarte les parametres reserves/temporaires (zzzTemporaryN)."""
    return colonne.lower().startswith("zzztemporary")


def colonnes_auditables(df):
    """Colonnes candidates : ni identite, ni temporaire."""
    return [c for c in df.columns
            if c not in COLONNES_IGNORE and not est_temporaire(c)]


def volet_a(df, type_objet):
    """Compare les parametres de la table de references a leur valeur attendue."""
    resultats = []
    for param, attendu in REGLES_BONNES_PRATIQUES.items():
        if param not in df.columns:
            continue
        for _, ligne in df.iterrows():
            valeur = str(ligne[param]).strip().lower()
            if valeur in ("", "nan"):
                continue
            if valeur != attendu.lower():
                resultats.append({
                    "DN": ligne["DN"],
                    "type_objet": type_objet,
                    "parametre": param,
                    "valeur_trouvee": ligne[param],
                    "reference": attendu,
                    "volet": "A - bonne pratique",
                })
    return resultats


def volet_b(df, type_objet):
    """Detecte les objets qui devient de la majorite de leur type, colonne par colonne."""
    resultats = []
    if len(df) < 3:
        # trop peu d'objets pour parler de "majorite" -> on ne juge pas
        return resultats

    cols = colonnes_auditables(df)
    for col in cols:
        serie = df[col].dropna()
        if serie.nunique() <= 1:
            continue  # colonne constante : rien a signaler
        majoritaire = serie.mode().iloc[0]
        # part de la valeur majoritaire : on ne signale que si elle domine nettement
        part = (serie == majoritaire).mean()
        if part < 0.6:
            continue  # pas de vraie majorite -> parametre trop varie, on n'audite pas
        for idx, valeur in serie.items():
            if valeur != majoritaire:
                resultats.append({
                    "DN": df.loc[idx, "DN"],
                    "type_objet": type_objet,
                    "parametre": col,
                    "valeur_trouvee": valeur,
                    "reference": f"majorite={majoritaire}",
                    "volet": "B - coherence interne",
                })
    return resultats


def auditer_conformite():
    fichiers = sorted(TABLES_DIR.glob("*.csv"))
    non_conformites = []

    for f in fichiers:
        type_objet = f.name.replace("vsData", "").replace(".csv", "")
        try:
            df = pd.read_csv(f)
        except Exception:
            continue
        if "DN" not in df.columns:
            continue

        # VOLET A : sur TOUS les objets (voisins inclus - c'est une regle absolue)
        non_conformites.extend(volet_a(df, type_objet))

        # VOLET B : sur tous les objets SAUF les voisins (couches 2 les couvre deja)
        if f.name not in FICHIERS_VOISINS:
            non_conformites.extend(volet_b(df, type_objet))

    df_out = pd.DataFrame(non_conformites)
    df_out.to_csv(OUT_CSV, index=False, encoding="utf-8")

    print(f"non_conformites.csv cree avec {len(df_out)} lignes.")
    if len(df_out):
        print()
        print("Repartition par volet :")
        print(df_out["volet"].value_counts().to_string())
        print()
        print("Repartition par type d'objet (top 10) :")
        print(df_out["type_objet"].value_counts().head(10).to_string())
    return df_out


if __name__ == "__main__":
    auditer_conformite()
