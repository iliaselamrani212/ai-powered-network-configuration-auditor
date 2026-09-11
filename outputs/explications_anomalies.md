# Rapport - Explications des anomalies (couche 2)

## Cas 1 : hoSuccLevel

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 4G | score -0.151
- **Valeur trouvee** : 3.0
- **Reference** : majorite des voisins = 1.0

**Explication :**

Le paramètre hoSuccLevel représente le niveau de succès des handovers vers une cellule voisine dans un réseau mobile. Il prend trois niveaux : HIGH, MEDIUM et LOW, selon le taux de réussite des handovers observés vers ce voisin.

Cette valeur pose problème lorsque son niveau est différent de la majorité des voisins (MEDIUM ou LOW), ce qui signifie que les handovers échouent plus souvent pour cette cellule voisine. Cela peut entraîner des appels coupés, une mauvaise mobilité et une degradation de la qualité de service vers ce voisin.

En résumé, un hoSuccLevel différent de la majorité des voisins est un candidat "cellule problematique" au sens de l'ANR (Automatic Neighbor Relation), ce qui peut avoir des impacts négatifs sur le réseau.

---

## Cas 2 : mobilityStatus.available

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 4G | score -0.151
- **Valeur trouvee** : 0.0
- **Reference** : majorite des voisins = 1.0

**Explication :**

Ce paramètre "mobilityStatus.available" décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) dans un réseau 4G/LTE. La valeur normale est "true", indiquant que le voisin est disponible pour le handover.

Cette valeur de 0,0 est anormale car elle indique que le voisin est indisponible pour le handover, ce qui peut entraîner des problèmes de continuité de service en bordure de cellule. En effet, les handovers vers cette cellule ne peuvent pas se faire, ce qui peut causer des coupures d'appel ou des perturbations du service.

L'impact possible sur le réseau est une dégradation de la qualité du service et un risque accru de coupure d'appel, en particulier dans les zones où les handovers sont fréquents. Il est donc important de surveiller ce paramètre pour détecter tout écart par rapport à la référence normale.

---

## Cas 3 : hoSuccLevel

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 4G | score -0.151
- **Valeur trouvee** : 3.0
- **Reference** : majorite des voisins = 1.0

**Explication :**

Le paramètre hoSuccLevel est utilisé pour définir le niveau de succès des handovers vers une cellule voisine dans un réseau mobile 4G/LTE. Cette valeur change automatiquement en fonction de seuils contrôlés par la fonction ANR (Automatic Neighbour Relation) et peut prendre les niveaux HIGH, MEDIUM ou LOW.

Cette valeur est anormale car elle se situe à 3.0, ce qui indique que les handovers vers cette cellule voisine échouent plus souvent que la majorité des voisins, ce qui peut entraîner des problèmes de qualité de service et d'appels coupés.

L'impact possible sur le réseau est une dégradation de la qualité de service et un risque accru d'appels coupés vers cette cellule voisine.

---

## Cas 4 : mobilityStatus.available

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 4G | score -0.151
- **Valeur trouvee** : 0.0
- **Reference** : majorite des voisins = 1.0

**Explication :**

Ce paramètre "mobilityStatus.available" décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) dans un réseau 4G/LTE. La valeur normale est "true", indiquant que le voisin est disponible pour le handover.

Cette valeur inférieure à la référence (0,0) signifie que la majorité des voisins sont disponibles, mais qu'un seul voisin est indisponible pour le handover. Cela peut entraîner des problèmes de continuité de service en bordure de cellule, car les handovers vers cette cellule ne peuvent pas se faire.

En conséquence, ce paramètre peut être considéré comme une anomalie statistique, car il est loin de la valeur attendue (1,0). Cela nécessite une investigation et une analyse pour déterminer la cause sous-jacente et prendre des mesures correctives pour améliorer la continuité de service dans le réseau.

---

## Cas 5 : coverageIndicator

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-4301`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 2G | score -0.045
- **Valeur trouvee** : 1.0
- **Reference** : majorite des voisins = 0.0

**Explication :**

Le paramètre coverageIndicator est un indicateur de couverture de la relation de voisinage dans les réseaux mobiles. Il marque si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité.

Cette valeur pose problème car elle est différente de la majorité des voisins, qui est attendue à 0. Cela peut indiquer qu'une cellule voisine traite différemment pour la couverture, ce qui pourrait être volontaire ou une incohérence de configuration. L'impact possible sur le réseau est que cela pourrait affecter la qualité de service et la stabilité du réseau.

En résumé, cette valeur anormale peut indiquer un problème de configuration ou une différence dans les comportements des cellules voisines, ce qui nécessite une investigation plus approfondie pour déterminer la cause et trouver une solution.

---

## Cas 6 : coverageIndicator

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-14301`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 2G | score -0.045
- **Valeur trouvee** : 1.0
- **Reference** : majorite des voisins = 0.0

**Explication :**

Le paramètre coverageIndicator est un indicateur de couverture de la relation de voisinage dans les réseaux mobiles. Il marque si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité.

Cette valeur pose problème car elle est différente de la majorité des voisins, qui est attendue à 0. Cela peut indiquer qu'une cellule est traitée différemment pour la couverture, ce qui pourrait être volontaire ou une incohérence de configuration.

L'impact possible sur le réseau est que cette anomalie peut affecter la qualité de service et la stabilité du réseau mobile. Il est important de vérifier la documentation et confirmer avec l'ingénieur réseau pour déterminer si cela constitue une erreur de configuration ou un problème réel.

---

## Cas 7 : coverageIndicator

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-3,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-24301`
- **Nature** : anomalie statistique (couche 2)
- **Contexte** : Technologie : 2G | score -0.045
- **Valeur trouvee** : 1.0
- **Reference** : majorite des voisins = 0.0

**Explication :**

Le paramètre coverageIndicator est un indicateur de couverture de la relation de voisinage dans les réseaux mobiles. Il marque si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité.

Cette valeur pose problème car elle est différente de la majorité des voisins, qui est attendue à 0. Cela peut indiquer qu'une cellule voisine traite différemment pour la couverture, ce qui pourrait être volontaire ou une incohérence de configuration.

L'impact possible sur le réseau est que cette anomalie peut affecter la qualité de service et la stabilité du réseau, car les décisions de mobilité sont basées sur les informations de couverture des cellules voisines. Il est important de vérifier la documentation ou de confirmer avec l'ingénieur réseau pour déterminer la cause de cette anomalie et prendre les mesures nécessaires pour la résoudre.

---
