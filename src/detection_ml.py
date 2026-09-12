from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest

BASE_DIR = Path(__file__).resolve().parent.parent
TABLES_DIR = BASE_DIR / "outputs" / "tables"
OUT_CSV = BASE_DIR / "outputs" / "anomalies.csv"

COLONNES_A_RETIRER = [
    'id', 'vsDataType', 'adjacentCell', 'extGeranCellRef',
    'timeOfCreation', 'timeOfLastModification',
    'lastModification', 'createdBy', 'mobilityStatus.reason',
]

FICHIERS = {
    '4G': 'vsDataEUtranCellRelation.csv',
    '3G': 'vsDataUtranCellRelation.csv',
    '2G': 'vsDataGeranCellRelation.csv',
}


def auditer_fichier(chemin_csv, technologie, contamination=0.1):
    dataset = pd.read_csv(chemin_csv)
    X = dataset.set_index('DN').drop(columns=COLONNES_A_RETIRER, errors='ignore').astype(float)

    model = IsolationForest(contamination=contamination, random_state=42)
    predictions = model.fit_predict(X)
    scores = model.decision_function(X)
    X['anomalie'] = predictions
    X['score'] = scores

    colonnes_reglages = X.columns.drop(['anomalie', 'score'])
    normaux = X[X['anomalie'] == 1]
    anormaux = X[X['anomalie'] == -1]

    resultats = []
    if len(anormaux) == 0:
        return resultats

    valeurs_normales = normaux[colonnes_reglages].mode().iloc[0]

    for dn, ligne in anormaux.iterrows():
        for col in colonnes_reglages:
            if ligne[col] != valeurs_normales[col]:
                resultats.append({
                    'DN': dn,
                    'technologie': technologie,
                    'colonne_deviante': col,
                    'valeur_trouvee': ligne[col],
                    'valeur_majoritaire': valeurs_normales[col],
                    'score': round(ligne['score'], 3),
                })
    return resultats


def detecter_toutes_anomalies(tables_dir=TABLES_DIR, out_csv=OUT_CSV, contamination=0.1):
    anomalies = []
    for techno, nom_fichier in FICHIERS.items():
        chemin = Path(tables_dir) / nom_fichier
        anomalies.extend(auditer_fichier(chemin, techno, contamination))

    df_anomalies = pd.DataFrame(anomalies)
    df_anomalies.to_csv(out_csv, index=False, encoding='utf-8')
    print(f"anomalies.csv cree avec {len(df_anomalies)} lignes.")
    return df_anomalies


if __name__ == "__main__":
    detecter_toutes_anomalies()