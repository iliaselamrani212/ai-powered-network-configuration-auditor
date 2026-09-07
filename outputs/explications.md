# Rapport d'audit - Explications des anomalies

## Anomalie 1 : hoSuccLevel (4G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Valeur trouvee** : 3.0 (majorite : 1.0)
- **Score** : -0.151

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations concernant le paramètre "hoSuccLevel" et son impact potentiel sur le réseau.

1. A quoi sert ce paramètre ?

Le paramètre "hoSuccLevel" représente le niveau de succès des handovers vers une cellule voisine dans un réseau 4G/LTE. Il indique la probabilité que les handovers réussissent entre deux cellules voisines.
2. Pourquoi cette valeur devrait-elle être différente de la majorité ?

Une valeur de "hoSuccLevel" différente de la majorité des voisins (1,0) signifie qu'il y a une cellule voisine vers laquelle les handovers échouent plus souvent. Cela peut indiquer une "cellule problematique" au sens de l'ANR (Automatic Neighbor Relation), ce qui pourrait entraîner des problèmes de qualité de service, d'appels coupés et de dégradation de la mobilité.
3. L'impact possible sur le réseau ?

Une valeur anormale de "hoSuccLevel" peut avoir un impact négatif sur le réseau, notamment en termes de qualité de service et de stabilité des communications. Il est donc important de surveiller cette valeur pour identifier les problèmes potentiels et prendre des mesures correctives si nécessaire.

---

## Anomalie 2 : mobilityStatus.available (4G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Valeur trouvee** : 0.0 (majorite : 1.0)
- **Score** : -0.151

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations disponibles sur le paramètre "mobilityStatus.available".

1. A quoi sert ce paramètre ?
Le paramètre "mobilityStatus.available" décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) dans un réseau 4G.

2. Pourquoi cette valeur devrait-elle être inférieure à la majorité des voisins ?
Une valeur de "0,0" indique que la cellule voisine est marquée comme indisponible pour le handover, ce qui signifie qu'elle ne peut pas être utilisée pour effectuer un handover. Cela pourrait être dû à une erreur ou à une configuration incorrecte.

3. L'impact possible sur le réseau ?
Cette valeur inférieure à la majorité des voisins peut entraîner des problèmes de continuité de service en bordure de cellule, car les handovers vers cette cellule ne peuvent pas se faire. Cela pourrait entraîner des coupures d'appel ou des perturbations du service.

---

## Anomalie 3 : hoSuccLevel (4G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Valeur trouvee** : 3.0 (majorite : 1.0)
- **Score** : -0.151

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations relatives au paramètre "hoSuccLevel".

1. A quoi sert ce paramètre ?

Le paramètre "hoSuccLevel" représente le niveau de succès des handovers vers une cellule voisine dans un réseau 4G/LTE. Il indique la probabilité que les handovers réussissent entre deux cellules voisines.

2. Pourquoi cette valeur devrait-elle être différente de la majorité ?

Une valeur de "hoSuccLevel" différente de la majorité des voisins (1,0) signifie qu'il y a une cellule voisine vers laquelle les handovers échouent plus souvent. C'est un candidat "cellule problematique" au sens de l'ANR (Automatic Neighbor Relation).

3. L'impact possible sur le réseau ?

Une valeur anormale de "hoSuccLevel" peut entraîner des problèmes de qualité de service, tels que des appels coupés ou une mauvaise mobilité, car les handovers vers cette cellule voisine ne réussissent pas correctement.

---

## Anomalie 4 : mobilityStatus.available (4G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Valeur trouvee** : 0.0 (majorite : 1.0)
- **Score** : -0.151

**Explication :**

Je vais vous expliquer les informations disponibles sur le paramètre "mobilityStatus.available" :

**1. A quoi sert ce paramètre ?**
Le paramètre "mobilityStatus.available" décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) entre deux cellules 4G/LTE.

**2. Pourquoi cette valeur devrait-elle être inférieure à la majorité des voisins ?**
Une valeur de "0,0" indique que le voisin est marqué comme indisponible pour le handover, ce qui signifie qu'il n'est pas possible de passer d'une cellule à une autre sans interruption. Cela peut entraîner des problèmes de continuité de service et de risque de coupure d'appel.

**3. L'impact possible sur le réseau ?**
Cette anomalie peut entraîner des problèmes de continuité de service et de risque de coupure d'appel, ce qui peut affecter la qualité du service pour les utilisateurs. Il est important de vérifier et de résoudre ce problème pour maintenir une bonne disponibilité du réseau.

---

## Anomalie 5 : coverageIndicator (2G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-4301`
- **Valeur trouvee** : 1.0 (majorite : 0.0)
- **Score** : -0.045

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations fournies.

**1. A quoi sert ce paramètre ?**

Le paramètre `coverageIndicator` indique si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité. Il marque si la cellule assurant une couverture étendue est traitée différemment par rapport aux autres voisins.

**2. Pourquoi cette valeur devrait-elle être différente de la majorité ?**

La valeur normale de `coverageIndicator` est 0, ce qui signifie que la plupart des voisins sont traités de manière standard. Cependant, si la valeur est différente (par exemple, 1), cela indique qu'une cellule voisine joue un rôle de couverture particulier et doit être traitée différemment.

**3. L'impact possible sur le réseau**

Cette anomalie peut avoir des impacts sur le fonctionnement du réseau, notamment en termes de performance et de qualité de service. Si une cellule voisine est traitée différemment sans justification, cela pourrait entraîner des problèmes de connectivité ou de qualité de signal. Il est donc important de vérifier la configuration et de corriger cette anomalie pour garantir un fonctionnement optimal du réseau.

---

## Anomalie 6 : coverageIndicator (2G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-14301`
- **Valeur trouvee** : 1.0 (majorite : 0.0)
- **Score** : -0.045

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations fournies.

**1. A quoi sert ce paramètre ?**

Le paramètre `coverageIndicator` indique si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité. Il marque si la cellule assurant une couverture étendue est traitée différemment par rapport aux autres voisins.

**2. Pourquoi cette valeur devrait-elle être différente de la majorité ?**

La valeur normale de `coverageIndicator` est 0, ce qui signifie que la plupart des voisins sont traités de manière égale. Cependant, si la valeur est différente (par exemple, 1), cela indique qu'une cellule voisine est traitée différemment pour la couverture. Il s'agit peut-être d'une cellule dédiée à la couverture ou d'une incohérence de configuration.

**3. L'impact possible sur le réseau**

Cette anomalie peut avoir un impact sur la stabilité et la performance du réseau, car elle peut entraîner des décisions de mobilité incorrectes ou des erreurs dans les traitements de signal. Il est important de vérifier la configuration de la cellule voisine et de confirmer si cette valeur est intentionnelle ou non.

---

## Anomalie 7 : coverageIndicator (2G)

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-3,vsDataGeranFreqGroupRelation=1,vsDataGeranCellRelation=6042-42-24301`
- **Valeur trouvee** : 1.0 (majorite : 0.0)
- **Score** : -0.045

**Explication :**

Bonjour ! En tant qu'expert en configuration de réseaux mobiles Ericsson, je vais vous expliquer les informations disponibles sur le paramètre "coverageIndicator".

1. A quoi sert ce paramètre ?
Le paramètre coverageIndicator est un indicateur de couverture de la relation de voisinage dans le réseau. Il permet de déterminer si une cellule voisine joue un rôle de couverture particulier dans les décisions de mobilité.

2. Pourquoi cette valeur devrait-elle être différente de la majorité ?
Une valeur differente de la majorite (par exemple 1 au lieu de 0) indique que la cellule voisine traite différemment pour la couverture, ce qui peut être volontaire ou une incohérence de configuration. Il est important de vérifier avec la documentation ou l'ingénieur réseau pour confirmer.

3. L'impact possible sur le réseau ?
Une valeur differente de la majorité peut avoir un impact sur le fonctionnement du réseau, car cela peut indiquer une erreur de configuration ou une incohérence entre les cellules voisines. Il est important de vérifier et de corriger cette valeur pour éviter tout problème de service.

---
