# Rapport - Explications des non-conformites (mission 2)

## Cas 1 : onDurationTimer

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : DrxProfile | B - coherence interne
- **Valeur trouvee** : 3
- **Reference** : majorite=7

**Explication :**

Ce paramètre "onDurationTimer" est utilisé pour définir la durée pendant laquelle un timer est activé après une interruption de service. 

Cette valeur trouvée (3) est inférieure à la référence attendue (majorité = 7), ce qui peut entraîner des problèmes de synchronisation et de cohérence dans le réseau.

L'impact possible sur le réseau est que les timers ne seront pas suffisamment longs pour garantir une reprise rapide et précise du service, ce qui pourrait entraîner des erreurs de communication et des pertes de connexion.

---

## Cas 2 : onDurationTimer

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : DrxProfile | B - coherence interne
- **Valeur trouvee** : 4
- **Reference** : majorite=7

**Explication :**

Ce paramètre "onDurationTimer" est lié à la gestion du temps de connexion pour les profiles Drx. Il définit la durée pendant laquelle un appareil reste connecté au réseau après avoir été désactivé.

La valeur trouvée (4) est inférieure à la référence attendue (7), ce qui peut entraîner des problèmes de cohérence interne dans le réseau, car les appareils pourraient ne pas respecter les normes de connexion prévues. Cela pourrait potentiellement affecter la stabilité et la sécurité du réseau.

En résumé, cette valeur non conforme peut entraîner des problèmes de cohérence interne et de stabilité dans le réseau, il est donc recommandé de corriger cette valeur pour garantir une fonctionnalité correcte.

---

## Cas 3 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-2`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Alert Neighbour Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage. Cependant, dans ce cas, la valeur est fixée à "false", ce qui pourrait indiquer qu'une relation critique a été protégée manuellement ou que le paramètre n'a pas été correctement configuré.

Cela pourrait entraîner des problèmes de fonctionnement du réseau, car l'ANR ne pourra pas supprimer automatiquement les relations de voisinage qui pourraient être en conflit avec d'autres configurations. Il est donc important de vérifier la configuration de ce paramètre pour garantir que le réseau fonctionne correctement.

---

## Cas 4 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-3`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Alert Neighbour Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage. Cependant, dans ce cas, la valeur est fixée à "false", ce qui pourrait indiquer qu'une relation critique a été protégée manuellement ou qu'un paramètre a été oublié.

Cela pourrait avoir un impact sur le réseau, car l'ANR ne pourra pas supprimer automatiquement les relations de voisinage, ce qui pourrait entraîner des problèmes de performance ou de stabilité. Il est donc important de vérifier la raison de cette valeur et de prendre les mesures nécessaires pour éviter tout problème.

---

## Cas 5 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-1`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Alert Neighbor Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage. Cependant, dans ce cas, la valeur est fixée à "false", ce qui pourrait indiquer qu'une relation critique a été protégée manuellement ou qu'un reglage a été oublié.

Cela pourrait entraîner des problèmes de stabilité et de fonctionnement du réseau, car l'ANR ne peut pas supprimer automatiquement les relations de voisinage qui pourraient être critiques. Il est donc important de vérifier la raison de cette valeur fixée à "false" et de prendre les mesures nécessaires pour éviter tout impact négatif sur le réseau.

---

## Cas 6 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-3`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Automatic Neighbor Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage. Cependant, dans ce cas, la valeur est fixée à "false", ce qui pourrait indiquer qu'une relation critique a été protégée manuellement ou qu'un reglage a été oublié.

Cela pourrait entraîner des problèmes de stabilité et de fonctionnement du réseau, car l'ANR ne peut pas supprimer automatiquement les relations de voisinage qui pourraient être critiques. Il est donc important de vérifier la raison de cette valeur et de prendre les mesures nécessaires pour garantir la stabilité du réseau.

---

## Cas 7 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-3,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-1`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Alert Neighbor Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage et les supprimer automatiquement. Cependant, si cette valeur est fixée à "false", cela peut indiquer qu'une relation critique a été protégée manuellement ou qu'un reglage a été oublié.

Cela peut entraîner des problèmes dans le réseau, car l'ANR ne pourra pas supprimer les relations de voisinage qui sont critiques et qui peuvent affecter la qualité du service. Il est donc important de vérifier cette valeur et de la mettre à jour si nécessaire pour éviter les problèmes de réseau.

---

## Cas 8 : isRemoveAllowed

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-3,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126001-2`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre "isRemoveAllowed" permet de définir si la fonction ANR (Alert Neighbour Relation) peut supprimer automatiquement une relation de voisinage sans intervention humaine.

Cette valeur est normalement fixée à "true", ce qui signifie que l'ANR peut gérer les relations de voisinage. Cependant, dans ce cas, la valeur est fixée à "false", ce qui pourrait indiquer qu'une relation de voisinage est protégée manuellement ou que le paramètre a été oublié.

Cela pourrait entraîner des problèmes de fonctionnement du réseau, car l'ANR ne pourra pas supprimer automatiquement les relations de voisinage qui sont potentiellement inutiles ou qui créent des conflits. Il est donc recommandé de vérifier la raison de cette valeur et de la corriger si nécessaire pour éviter tout impact négatif sur le réseau.

---

## Cas 9 : mobilityStatus.available

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) entre deux cellules 4G/LTE. La valeur normale est "true", indiquant que le voisin est disponible pour un handover.

Cette valeur false pose problème car elle signale une cellule voisine marquée INDISPONIBLE pour le handover, ce qui peut dégrader la continuité de service en bordure de cellule et entraîner des risques de coupure d'appel. Cela peut avoir un impact sur la qualité du service mobile.

---

## Cas 10 : mobilityStatus.available

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650,vsDataEUtranCellRelation=6042-126004-1`
- **Nature** : non-conformite (A - bonne pratique)
- **Contexte** : Type d'objet : EUtranCellRelation | A - bonne pratique
- **Valeur trouvee** : False
- **Reference** : true

**Explication :**

Ce paramètre décrit le statut de disponibilité d'une relation de voisinage pour la mobilité (handover) entre deux cellules 4G/LTE. La valeur normale est "true", indiquant que la cellule voisine est disponible pour un handover.

Cette valeur fausse signale une cellule voisine marquée INDISPONIBLE pour le handover, ce qui peut dégrader la continuité de service en bordure de cellule et entraîner des risques de coupure d'appel. Cela peut avoir un impact sur la qualité du service et la fiabilité du réseau.

---

## Cas 11 : candNeighborRel.physicalLayerCellIdGroup

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : EUtranFreqRelation | B - coherence interne
- **Valeur trouvee** : 35.0
- **Reference** : majorite=36.0

**Explication :**

Ce paramètre "candNeighborRel.physicalLayerCellIdGroup" désigne le groupe d'ID de cellule physique associé à un voisin de réseaux (candNeighborRel). Cette valeur est utilisée pour définir les relations entre les cellules physiques dans le réseau.

La valeur trouvée, 35.0, est inférieure à la référence attendue, 36.0, ce qui indique une incohérence interne dans le réseau. Cela peut entraîner des problèmes de communication et de coordination entre les cellules physiques, affectant potentiellement la qualité du service et la stabilité du réseau.

En résumé, cette valeur anormale peut provoquer des erreurs de synchronisation et de communication entre les cellules physiques, ce qui pourrait avoir un impact négatif sur le fonctionnement du réseau.

---

## Cas 12 : candNeighborRel.cellId

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-3,vsDataEUtranFreqRelation=1650`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : EUtranFreqRelation | B - coherence interne
- **Valeur trouvee** : 3.0
- **Reference** : majorite=1.0

**Explication :**

Ce paramètre "candNeighborRel.cellId" est utilisé pour définir l'identifiant cellulaire d'un voisin potentiel dans un réseau EUtran. La valeur trouvée, 3.0, est inférieure à la référence attendue de 1.0.

Cette valeur pose problème car elle indique qu'il y a au moins une cellule avec un identifiant cellulaire supérieur à 2 (puisque les identifiants cellulaires sont généralement numériques et non décimales). Cela peut entraîner des problèmes de cohérence interne dans le réseau, car les cellules ne peuvent pas être correctement mappées et gérées.

L'impact possible sur le réseau est une dégradation de la qualité du service, des erreurs de connexion et des problèmes de synchronisation entre les cellules. Il est donc important de corriger cette valeur pour garantir la cohérence interne du réseau et assurer un bon fonctionnement.

---

## Cas 13 : candNeighborRel.enbId

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : EUtranFreqRelation | B - coherence interne
- **Valeur trouvee** : 168011.0
- **Reference** : majorite=126032.0

**Explication :**

Ce paramètre "candNeighborRel.enbId" est utilisé pour spécifier l'ID de l'antenne relais associée à un émetteur fréquentiel (EUtranFreqRelation). 

Cette valeur est supérieure à la référence attendue (126032.0) et pose problème car elle indique que l'antenne relais associée à cet émetteur n'est pas correctement configurée ou identifiée.

En cas de non-conformité, cela peut entraîner des problèmes de communication entre les antennes et des erreurs dans la gestion du trafic fréquentiel, ce qui pourrait affecter la qualité et la fiabilité du réseau.

---

## Cas 14 : candNeighborRel.tac

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-1,vsDataEUtranFreqRelation=1650`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : EUtranFreqRelation | B - coherence interne
- **Valeur trouvee** : 1146.0
- **Reference** : majorite=1042.0

**Explication :**

Ce paramètre "candNeighborRel.tac" indique la valeur attendue pour le TAC (Time Advance Counter) d'un voisin de réseau (candNeighborRel). La valeur trouvée est de 1146,0 dBm, tandis que la valeur attendue est de 1042,0 dBm.

Ce paramètre sert à déterminer si un UE peut relier à un voisin de réseau. Si la valeur trouvée est supérieure à la valeur attendue, cela indique une non-conformité interne du réseau, car le TAC d'un voisin de réseau devrait être inférieur à celui de l'UE.

L'impact possible sur le réseau est que les UEs peuvent avoir des difficultés à relier à un voisin de réseau, ce qui peut entraîner des problèmes de connexion et de qualité de service. Il est donc important de vérifier cette valeur pour garantir la cohérence interne du réseau et assurer une bonne fonctionnement des services mobiles.

---

## Cas 15 : candNeighborRel.mobilityStatusReason

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataEUtranCellFDD=AHO-1001_L-2,vsDataEUtranFreqRelation=1650`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : EUtranFreqRelation | B - coherence interne
- **Valeur trouvee** : 1.0
- **Reference** : majorite=0.0

**Explication :**

Ce paramètre "candNeighborRel.mobilityStatusReason" indique le statut de mobilité d'un voisin de réseau. Une valeur de 1,0 indique une mobilité actuelle, tandis qu'une valeur de 0,0 est attendue pour une mobilité non active.

Cette valeur anormale peut poser problème car elle suggère que le voisin de réseau est en mouvement, ce qui pourrait entraîner des erreurs de synchronisation et d'authentification dans le réseau. Cela pourrait également affecter la qualité de service et la stabilité du réseau.

En résumé, cette valeur anormale peut avoir un impact négatif sur la fonctionnalité du réseau en raison de la mobilité non attendue du voisin de réseau.

---

## Cas 16 : absPrioOverride

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci5`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "absPrioOverride" est utilisé pour définir si un profil de QCI (Quality of Experience Class Identifier) doit être override par une priorité absolue. 

Cette valeur de 1 indique que la priorité absolue est activée, ce qui peut entraîner des problèmes de cohérence interne dans le réseau.

L'impact possible sur le réseau est qu'une priorité absolue peut perturber l'équilibre entre les différents flux de trafic, potentiellement affectant la qualité de service et la performance globale du réseau.

---

## Cas 17 : resourceAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci6`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceAllocationStrategy" définit la stratégie d'allocation des ressources dans le réseau. 

Cette valeur trouvée (1) est en dehors de la plage attendue (majorité = 0), ce qui indique une non-conformité interne. 

L'impact possible sur le réseau est qu'une allocation erronée des ressources pourrait entraîner des problèmes de performance, de qualité du service ou même de disponibilité du réseau.

---

## Cas 18 : resourceAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci7`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceAllocationStrategy" définit la stratégie d'allocation des ressources dans le réseau. 

Cette valeur trouvée (1) est en désaccord avec la référence attendue (majorité=0), ce qui indique que la stratégie d'allocation n'est pas configurée pour utiliser une majorité, mais plutôt une valeur fixe.

Cela pourrait entraîner des problèmes de performance et de stabilité dans le réseau, car les ressources ne seraient pas réparties de manière optimale.

---

## Cas 19 : resourceAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci8`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceAllocationStrategy" définit la stratégie d'allocation des ressources dans le réseau. 

Cette valeur trouvée (1) est en contradiction avec la référence attendue (majorité=0), ce qui indique que la documentation n'a pas fourni d'information sur cette stratégie.

L'impact possible sur le réseau est qu'une allocation inadéquate des ressources pourrait entraîner des problèmes de performance, de qualité du service ou même de disponibilité.

---

## Cas 20 : resourceAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci9`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceAllocationStrategy" définit la stratégie d'allocation des ressources dans le réseau. 

Cette valeur trouvée (1) est en dehors de la plage attendue (majorité = 0), ce qui indique une non-conformité interne. 

L'impact possible sur le réseau est qu'il pourrait y avoir des problèmes d'allocation efficace des ressources, ce qui pourrait affecter la qualité et la stabilité du service.

---

## Cas 21 : measReportConfigParams.a1ThresholdRsrpPrimOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 2
- **Reference** : majorite=0

**Explication :**

Ce paramètre, `measReportConfigParams.a1ThresholdRsrpPrimOffset`, est lié à la configuration des rapports de mesures pour les signaux RSRP (Received Signal Strength Indicator) primaires dans un réseau mobile.

Cette valeur de 2 pose problème car elle indique que le seuil de détection du signal RSRP primaire est supérieur à la référence attendue, qui est de 0. Cela peut entraîner des erreurs de détection et d'analyse des signaux, ce qui peut affecter la qualité globale du réseau.

En termes d'impact sur le réseau, cette non-conformité peut entraîner des problèmes tels que :

* Des erreurs de connexion ou de communication entre les appareils et le réseau.
* Une diminution de la qualité des signaux RSRP primaires, ce qui peut affecter la performance du réseau.
* Des difficultés pour les opérateurs à optimiser leur réseau et améliorer la couverture.

---

## Cas 22 : measReportConfigParams.a2ThresholdRsrpPrimOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 8
- **Reference** : majorite=0

**Explication :**

Ce paramètre "measReportConfigParams.a2ThresholdRsrpPrimOffset" définit l'écart entre les valeurs de RSRP (Signal-to-Noise Ratio) primaires et secondaires pour les mesures de reportage.

Cette valeur est trouvée à 8, mais la référence attendue est majorité=0, ce qui signifie que le paramètre doit être égal à 0. Cette différence pose problème car elle peut entraîner des erreurs dans les mesures de reportage et affecter ainsi la qualité du réseau.

L'impact possible sur le réseau est une diminution de la précision des mesures de reportage, ce qui peut entraîner des problèmes de connectivité et de qualité de service pour les utilisateurs.

---

## Cas 23 : measReportConfigParams.b2Threshold1RsrpGeranOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 8
- **Reference** : majorite=0

**Explication :**

Ce paramètre "measReportConfigParams.b2Threshold1RsrpGeranOffset" définit la limite de tolérance pour les reports de mesures RSRP (Received Signal Strength Indicator) en GAN (Global Area Network). 

Cette valeur trouvée est de 8, ce qui est supérieur à la référence attendue de 0. Cela indique une incohérence interne dans le paramètre.

L'impact possible sur le réseau est que les reports de mesures RSRP ne seront pas correctement pris en compte, ce qui pourrait entraîner des erreurs de gestion du trafic et des performances réduites.

---

## Cas 24 : measReportConfigParams.b2Threshold2GeranOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 4
- **Reference** : majorite=0

**Explication :**

Ce paramètre "measReportConfigParams.b2Threshold2GeranOffset" définit la limite de déviation pour les mesures de reportage des signaux B2Gérans. Une valeur supérieure à la référence (majorité = 0) indique que le réseau est moins précis dans ses mesures, ce qui peut entraîner des erreurs de configuration ou de gestion.

Cette valeur non conforme peut entraîner des problèmes de cohérence interne du réseau, notamment en termes de qualité des signaux et de stabilité de la connexion. Il est donc important de corriger cette valeur pour garantir une configuration précise et fiable du réseau.

---

## Cas 25 : measReportConfigParams.b2Threshold1RsrpUtraOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 8
- **Reference** : majorite=0

**Explication :**

Ce paramètre, `measReportConfigParams.b2Threshold1RsrpUtraOffset`, définit la limite d'écart entre les valeurs de RSRP (Signal-to-Noise Ratio en Pointe) et UTRA Offset pour les rapports de mesures B2.

Cette valeur est problématique car elle est fixée à 8, ce qui est supérieur à la référence attendue de 0. Cela peut entraîner des erreurs dans les calculs de mesures et potentiellement affecter la qualité du réseau.

L'impact possible sur le réseau est que les erreurs de mesures peuvent se propager et affecter la performance globale du réseau, notamment en termes de qualité des signaux et de précision des mesures. Cela peut entraîner des problèmes de connectivité et de communication pour les utilisateurs.

---

## Cas 26 : measReportConfigParams.b2Threshold2RscpUtraOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 5
- **Reference** : majorite=0

**Explication :**

Ce paramètre, `measReportConfigParams.b2Threshold2RscpUtraOffset`, définit la limite de tolérance pour les reports de mesures de signal en RSCP (Received Signal Code Power) et UTRA (Universal Terrestrial Radio Access). 

Cette valeur est supérieure à la référence attendue, qui est 0. Cela signifie que le réseau peut tolérer une certaine variation dans la qualité du signal avant de déclencher un événement ou une action spécifique.

L'impact possible sur le réseau est qu'une tolérance trop élevée peut entraîner des erreurs de détection et d'intervention, ce qui peut affecter la qualité globale du service. Il est donc important de trouver un équilibre entre la tolérance et l'exactitude pour garantir une fonctionnalité stable et fiable.

---

## Cas 27 : drxProfileRef

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=1
- **Reference** : majorite=SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=0

**Explication :**

Ce paramètre "drxProfileRef" fait référence à un profil de drx (dropping power) spécifique pour une sous-réseau. La valeur trouvée est incorrecte car elle indique que le profil actuel est "vsDataDrxProfile=1", mais la reference attendue est "vsDataDrxProfile=0". Cela signifie que le profil de drx actuellement en usage n'est pas celui prévu.

L'impact possible sur le réseau est qu'il peut y avoir des problèmes de performance ou de qualité de service, car les paramètres de drx sont cruciaux pour la gestion efficace du trafic et de l'espace de fréquence. Une valeur incorrecte pour ce paramètre peut entraîner des erreurs de synchronisation entre les éléments du réseau, ce qui pourrait affecter la stabilité globale du réseau.

---

## Cas 28 : drxProfileRef

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=2
- **Reference** : majorite=SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataDrxProfile=0

**Explication :**

Ce paramètre "drxProfileRef" fait référence à un profil de drx (dropping power) spécifique pour une sous-réseau. La valeur trouvée est incorrecte car elle pointe vers un profil de drx avec la valeur 2, alors que la valeur attendue est 0.

Cette erreur peut entraîner des problèmes de connectivité et de qualité de service dans le réseau, car les paramètres de drx sont cruciaux pour la communication entre les appareils mobiles et l'antenne base. Une valeur incorrecte de drx peut entraîner une perte de signal ou une diminution de la qualité du signal.

Il est recommandé de corriger cette erreur en ajustant la valeur de "drxProfileRef" à la valeur attendue, qui est 0 dans ce cas.

---

## Cas 29 : rlcSNLength

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 5
- **Reference** : majorite=10

**Explication :**

Ce paramètre "rlcSNLength" définit la longueur du SN (Sequence Number) utilisé pour les contrôles de qualité des données dans un réseau LTE.

Cette valeur est trouvée à 5, mais la référence attendue est une majorité de 10. Cela signifie que le paramètre "rlcSNLength" doit être configuré pour une longueur qui permet une cohérence interne et une efficacité optimale des contrôles de qualité.

Si cette valeur n'est pas correcte, cela pourrait entraîner des problèmes de cohérence dans les données transmises au sein du réseau, ce qui pourrait affecter la qualité globale de l'expérience utilisateur.

---

## Cas 30 : counterActiveMode

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : True
- **Reference** : majorite=False

**Explication :**

Ce paramètre "counterActiveMode" est utilisé pour définir le mode d'activation des compteurs de réactivité dans le réseau. 

Cette valeur "True" indique que le compteur de réactivité est activé, ce qui peut entraîner une augmentation du trafic et des coûts de fonctionnement.

En effet, lorsque le compteur de réactivité est activé, il s'agit d'un mécanisme pour contrôler la réactivité excessive des appareils mobiles. Cependant, si cette valeur est "True", cela peut entraîner une augmentation du trafic et des coûts de fonctionnement, car les compteurs de réactivité sont activés pour plus de situations que prévu.

Cela peut également avoir un impact sur la performance du réseau, car les appareils mobiles peuvent être plus réactifs et générer plus de trafic.

---

## Cas 31 : counterActiveMode

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci5`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : True
- **Reference** : majorite=False

**Explication :**

Ce paramètre "counterActiveMode" est utilisé pour activer ou désactiver le mode de comptage des événements dans le réseau. La valeur attendue est "majorite=False", ce qui signifie que le mode de comptage doit être désactivé.

Cette valeur pose problème car elle indique qu'un événement a été détecté, mais la documentation n'apporte aucune explication sur ce paramètre. Cela peut entraîner des erreurs ou des comportements non prévus dans le réseau.

L'impact possible est que le réseau ne fonctionne pas correctement, car les événements sont comptés incorrectement. Cela peut entraîner des problèmes de connectivité, de qualité de service et d'autres problèmes de performance.

---

## Cas 32 : srsAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci6`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre srsAllocationStrategy est utilisé pour définir la stratégie d'allocation des fréquences SRS (Spectral Reuse) dans un réseau LTE.

Cette valeur trouvée (1) est en dehors de la plage attendue (majorité = 0), ce qui indique une non-conformité interne. En effet, la valeur 1 ne correspond pas à aucune des stratégies d'allocation SRS standardises.

L'impact possible sur le réseau est que les fréquences SRS ne seront pas attribuées de manière optimale, ce qui peut entraîner une réduction de la qualité du signal et de la capacité du réseau.

---

## Cas 33 : srsAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci7`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre srsAllocationStrategy est utilisé pour définir la stratégie d'allocation des fréquences SRS (Small Cell Radio) dans un réseau LTE.

Cette valeur trouvée, 1, indique que la stratégie d'allocation par défaut est activée. Cependant, selon la documentation, cette valeur devrait être 0 pour une majorité de cas, car elle permet une allocation plus efficace des fréquences SRS.

L'impact possible sur le réseau est que les fréquences SRS ne seront pas attribuées de manière optimale, ce qui peut entraîner des problèmes de qualité de service et de performance du réseau.

---

## Cas 34 : srsAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci8`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre srsAllocationStrategy est utilisé pour définir la stratégie d'allocation des fréquences SRS (Small Resource Block) dans un réseau LTE.

Cette valeur trouvée, 1, indique que la stratégie par défaut est utilisée, ce qui peut être considéré comme non optimisé car la majorité des réseaux utilise une stratégie plus avancée pour améliorer les performances. 

L'impact possible sur le réseau est que les performances de transmission peuvent être affectées, entraînant des retards ou des pertes de signal. Cependant, il convient de noter que cette valeur n'est pas nécessairement une erreur grave et qu'une analyse plus approfondie est nécessaire pour déterminer l'impact réel sur le réseau.

---

## Cas 35 : srsAllocationStrategy

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci9`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre srsAllocationStrategy est utilisé pour définir la stratégie d'allocation des fréquences SRS (Small Cell Radio) dans un réseau LTE.

Cette valeur trouvée, 1, indique que la stratégie d'allocation par défaut est utilisée, ce qui peut être considéré comme non optimisé car il n'y a pas de majorité (0) pour définir une stratégie plus avancée. Cela pourrait entraîner des problèmes de performance et de qualité du service dans le réseau.

L'impact possible sur le réseau est que les fréquences SRS ne sont pas optimisées, ce qui peut entraîner des pertes de qualité de signal, des retards et des problèmes de connectivité pour les utilisateurs.

---

## Cas 36 : qciSubscriptionQuanta

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci8`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 2600
- **Reference** : majorite=1

**Explication :**

Ce paramètre "qciSubscriptionQuanta" définit la quantité de QCI (Quality of Experience Class) que peut utiliser un abonné à un réseau mobile. La valeur attendue est 1, ce qui signifie qu'un seul abonné peut utiliser une seule QCI.

La valeur trouvée est 2600, ce qui indique que plusieurs abonnés peuvent utiliser la même QCI, ce qui est non conforme à la référence. Cela pourrait entraîner des problèmes de qualité de service et de priorisation des trafics sur le réseau.

En termes d'impact sur le réseau, cette non-conformité pourrait entraîner des problèmes tels que :

* Des retards ou des pertes de trafic pour les abonnés qui utilisent la même QCI
* Des difficultés à prioriser les trafics et à assurer une qualité de service équitable pour tous les abonnés
* Des problèmes de gestion du réseau, car le système ne peut pas déterminer avec précision la quantité de trafic à gérer pour chaque QCI.

---

## Cas 37 : ulMinBitRate

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 384
- **Reference** : majorite=0

**Explication :**

Ce paramètre "ulMinBitRate" définit la limite minimale du taux de transmission en bits par seconde pour les communications UMTS.

Cette valeur trouvée est de 384, ce qui est supérieur à la référence attendue de 0. Cela indique une non-conformité car le réseau n'atteint pas la limite minimale prévue.

L'impact possible sur le réseau est que cette valeur élevée peut entraîner des problèmes de performance et de qualité des communications, car les appareils ne peuvent pas transmettre à un taux inférieur quels que soient les besoins du réseau. Cela pourrait entraîner des retards ou des pertes de données.

---

## Cas 38 : serviceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "serviceType" est utilisé pour définir le type de service à fournir par le réseau mobile. Dans ce cas, la valeur trouvée est 1, qui correspond à un service de majorité.

Cette valeur pose problème car elle ne correspond pas à la référence attendue, qui est majorité=0. Cela signifie que le réseau mobile doit fournir un service de majorité, mais la valeur actuelle indique qu'il fournit un service de non-majorité.

L'impact possible sur le réseau est que les communications entre les appareils et le réseau peuvent être perturbées ou interrompues, ce qui peut entraîner des problèmes de connectivité et de qualité de service. Il est donc important de corriger cette valeur pour garantir la cohérence interne du système.

---

## Cas 39 : serviceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci5`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 2
- **Reference** : majorite=0

**Explication :**

Ce paramètre "serviceType" est utilisé pour définir le type de service à fournir par le réseau mobile. Dans ce cas, la valeur trouvée est 2, qui n'est pas conforme à la référence attendue (majorité = 0).

Cette valeur pose problème car elle indique que le réseau mobile fournit un service de majorité, ce qui n'est pas la norme pour les réseaux mobiles. En effet, les réseaux mobiles sont conçus pour fournir des services de majorité, où une décision est prise en fonction de la majorité des votes.

L'impact possible sur le réseau est que cette configuration pourrait entraîner des problèmes de cohérence et de stabilité dans l'exécution des opérations du réseau. En effet, si un service de majorité est configuré, cela pourrait conduire à des décisions erronées ou incomplètes, ce qui pourrait avoir des conséquences sur la qualité des services offerts au public.

---

## Cas 40 : rlcMode

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "rlcMode" est lié à la gestion de la qualité du service radio (QoS) dans les réseaux mobiles. Il spécifie la mode d'operation de la fonctionnalité RLC (Radio Link Control), qui est responsable de la gestion des connexions radio et de la transmission de données.

La valeur trouvée "1" indique que le paramètre "rlcMode" est configuré en mode "majorité", ce qui signifie que les décisions prises par la fonctionnalité RLC sont basées sur une majorité des votes. Cependant, selon la documentation, la valeur attendue pour ce paramètre est "0", ce qui indique que le mode d'operation est "non-majoritaire".

Cette valeur non conforme peut entraîner des problèmes de cohérence interne dans le réseau, car les décisions prises par la fonctionnalité RLC peuvent ne pas être cohérentes avec les autres composants du réseau. Cela pourrait potentiellement affecter la qualité du service radio et la stabilité du réseau.

En résumé, la valeur "1" pour le paramètre "rlcMode" est non conforme à la documentation attendue, ce qui peut entraîner des problèmes de cohérence interne dans le réseau. Il est recommandé de corriger cette valeur pour garantir la cohérence et la stabilité du réseau.

---

## Cas 41 : rlcMode

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "rlcMode" est lié à la gestion de la qualité du service radio (QoS) dans les réseaux mobiles. Il spécifie le mode d'operation de la fonctionnalité RLC (Radio Link Control), qui est responsable de la gestion des connexions radio et de la transmission de données.

La valeur trouvée "1" indique que le paramètre "rlcMode" est configuré sur "majorité", ce qui signifie que les décisions prises par la fonction RLC sont basées sur une majorité des votes. Cependant, selon la documentation, la valeur attendue est "0", ce qui indiquerait qu'il n'y a pas de vote majoritaire.

Cette valeur inattendue peut poser problème car elle peut entraîner des décisions erronées ou des conflits entre les différents composants du réseau. En effet, si le mode "majorité" est activé, les décisions prises par la fonction RLC peuvent être influencées par les votes de certains composants, ce qui peut perturber l'ensemble du réseau.

L'impact possible sur le réseau est que des erreurs ou des perturbations peuvent se produire, entraînant des problèmes de connexion, de qualité de service ou même d'interruption du service. Il est donc important de vérifier et de corriger cette valeur pour garantir la cohérence interne du réseau et assurer sa stabilité.

---

## Cas 42 : schedulingAlgorithm

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=default`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 0
- **Reference** : majorite=3

**Explication :**

Ce paramètre "schedulingAlgorithm" est utilisé pour définir l'algorithme d'assignation des fréquences dans un réseau mobile. Il permet de gérer efficacement les ressources de fréquence et de réduire les interférences entre les appareils.

La valeur trouvée, 0, est inférieure à la référence attendue, 3, ce qui indique une configuration non optimale pour l'assignation des fréquences. Cela pourrait entraîner des problèmes de performance du réseau, tels que des interférences entre les appareils et une réduction de la qualité des signaux.

En effet, un algorithme d'assignation des fréquences efficace est crucial pour garantir une bonne couverture et une qualité des signaux dans le réseau. Une configuration non optimale pourrait entraîner des problèmes de cohabitation entre les appareils et réduire la capacité du réseau à gérer les flux de données.

---

## Cas 43 : schedulingAlgorithm

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 6
- **Reference** : majorite=3

**Explication :**

Ce paramètre "schedulingAlgorithm" est utilisé pour définir l'algorithme d'assignation des fréquences dans un réseau mobile.

Cette valeur de 6 est en dessous de la référence attendue de 3, ce qui indique une non-conformité interne. Cela signifie que le réseau utilise un algorithme d'assignation des fréquences moins efficace que celui prévu.

Ceci pourrait entraîner des problèmes de performance et de qualité du service dans le réseau, car les fréquences ne seront pas attribuées de manière optimale.

---

## Cas 44 : schedulingAlgorithm

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci5`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 0
- **Reference** : majorite=3

**Explication :**

Ce paramètre "schedulingAlgorithm" est utilisé pour définir l'algorithme de gestion du temps des signaux dans un réseau mobile. La valeur attendue est "majorite=3", ce qui signifie que la plupart des signaux doivent être traités en priorité.

Cette valeur pose problème car elle indique une valeur de 0, ce qui n'est pas conforme à la référence. En effet, une valeur de 0 ne permettrait pas de définir un algorithme de gestion du temps valide.

L'impact possible sur le réseau est que les signaux ne seraient pas traités correctement, ce qui pourrait entraîner des problèmes de connexion et de qualité de service pour les utilisateurs. Il est donc important de corriger cette valeur pour garantir la cohérence interne du système.

---

## Cas 45 : resourceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceType" est utilisé pour définir le type de ressource dans un réseau mobile. 

Cette valeur trouvée (1) est en désaccord avec la référence attendue (majorité = 0), ce qui indique que le type de ressource n'est pas correctement défini.

Cela pourrait entraîner des problèmes de cohérence interne dans le réseau, notamment lors de la gestion des ressources et des paramètres de configuration. Il est donc important de corriger cette valeur pour garantir une bonne fonctionnement du réseau.

---

## Cas 46 : resourceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceType" est utilisé pour définir le type de ressource dans un réseau mobile. Il permet de préciser si une ressource est un équipement, un service ou autre chose.

Cette valeur "1" est en conflit avec la référence attendue "majorité=0", ce qui signifie que la documentation n'a pas fourni d'information exploitable sur le paramètre "resourceType". Cela peut entraîner des problèmes de cohérence interne dans les configurations réseau.

En termes d'impact, cette non-conformité peut entraîner des erreurs ou des comportements inattendus dans la gestion du réseau mobile, ce qui pourrait affecter la qualité et la fiabilité des services offerts aux utilisateurs.

---

## Cas 47 : resourceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci3`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceType" est utilisé pour définir le type de ressource dans un réseau mobile. La valeur attendue est "majorite=0", ce qui signifie que le paramètre ne doit pas être défini.

Cette valeur pose problème car elle indique que la valeur trouvée (1) n'est pas conforme à la référence. Cela peut entraîner des problèmes de cohérence interne dans le réseau, car les ressources ne seront pas correctement gérées.

L'impact possible sur le réseau est qu'il peut entraîner des erreurs de fonctionnement, des pertes de connexion ou des problèmes de performance. Il est donc important de vérifier et de corriger cette valeur pour assurer la cohérence interne du réseau.

---

## Cas 48 : resourceType

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci4`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "resourceType" est utilisé pour définir le type de ressource dans un réseau mobile. 

Cette valeur trouvée (1) est en contradiction avec la référence attendue (majorité = 0), ce qui indique que la documentation n'a pas d'information exploitable sur ce paramètre.

L'impact possible sur le réseau est qu'il pourrait y avoir une erreur de configuration, ce qui pourrait entraîner des problèmes de fonctionnement ou de stabilité du réseau.

---

## Cas 49 : drxPriority

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 98
- **Reference** : majorite=0

**Explication :**

Ce paramètre "drxPriority" est utilisé pour définir la priorité de la réduction du drx (dwell time) dans les réseaux mobiles Ericsson.

Cette valeur trouvée (98) est supérieure à la référence attendue (majorité = 0), ce qui indique une non-conformité en termes de cohérence interne. En effet, une priorité élevée pour la réduction du drx peut entraîner des problèmes de stabilité et de performance dans le réseau.

L'impact possible sur le réseau est que les réductions de drx peuvent être trop fréquentes, ce qui peut entraîner des perturbations dans la communication entre les appareils mobiles et l'antenne base. Cela pourrait entraîner des problèmes de connectivité, de qualité de service et de performance globale du réseau.

---

## Cas 50 : drxPriority

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 100
- **Reference** : majorite=0

**Explication :**

Ce paramètre "drxPriority" est utilisé pour définir la priorité de l'allocation des fréquences DRX (Discontinuous Reception) dans un réseau LTE.

Cette valeur trouvée, 100, est supérieure à la référence attendue, qui est majorité = 0. Cela signifie que le paramètre "drxPriority" n'est pas configuré correctement, ce qui peut entraîner des problèmes de fonctionnement du réseau.

L'impact possible sur le réseau est qu'il peut y avoir des retards ou des pertes de signal en cas d'allocation insuffisante de fréquences DRX, ce qui peut affecter la qualité de service et la performance globale du réseau.

---

## Cas 51 : drxPriority

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci5`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 1
- **Reference** : majorite=0

**Explication :**

Ce paramètre "drxPriority" est utilisé pour définir l'ordre de priorité des fréquences DRX (Discontinuous Reception) dans un réseau mobile.

Cette valeur trouvée (1) est en dessous de la référence attendue (majorité = 0), ce qui indique une non-conformité interne. En effet, une valeur de 1 signifie que les fréquences DRX sont traitées avec une priorité faible, ce qui peut entraîner des problèmes de réception et de qualité du signal.

L'impact possible sur le réseau est qu'il pourrait entraîner des pertes de connexion ou des dégradations de la qualité du signal pour les utilisateurs. Il est donc important de corriger cette valeur pour garantir une cohérence interne et un bon fonctionnement du réseau.

---

## Cas 52 : dlMinBitRate

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci2`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 384
- **Reference** : majorite=0

**Explication :**

Ce paramètre "dlMinBitRate" définit la limite minimale du taux de transmission en bits par seconde pour les connexions réseau. 

Cette valeur trouvée est de 384, ce qui est supérieur à la référence attendue de 0, indiquant une non-conformité interne. 

L'impact possible sur le réseau est que cette valeur peut entraîner des problèmes de performance et de qualité des connexions, car les taux de transmission excessifs peuvent saturer les canaux de transmission et affecter la qualité globale du service.

---

## Cas 53 : rohcEnabled

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : True
- **Reference** : majorite=False

**Explication :**

Ce paramètre "rohcEnabled" est utilisé pour activer ou désactiver l'activation automatique des relations de voisinage (ANR) dans les réseaux mobiles Ericsson.

La valeur trouvée "True" indique que l'ANR est activé, ce qui peut poser problème car la référence attendue est "majorite=False", ce qui signifie que l'ANR ne doit pas être activé pour garantir la cohérence interne du réseau. L'activation de l'ANR sans autorisation appropriée peut entraîner des problèmes de coherance et d'intégrité du réseau, notamment en termes de gestion des relations de voisinage entre les cellules.

L'impact possible sur le réseau est une perturbation potentielle dans la fonctionnalité de l'ANR, ce qui pourrait entraîner des erreurs de connexion, des problèmes de qualité de service et des difficultés à maintenir la cohérence interne du réseau. Il est donc important de vérifier et d'actualiser cette valeur pour garantir que le réseau fonctionne correctement et sans risques.

---

## Cas 54 : pdbOffset

- **DN** : `SubNetwork=ONRM_ROOT_MO_R,SubNetwork=RadioNodes,MeContext=AHO-1001_BB_L,ManagedElement=AHO-1001_BB_L,vsDataENodeBFunction=1,vsDataQciTable=default,vsDataQciProfilePredefined=qci1`
- **Nature** : non-conformite (B - coherence interne)
- **Contexte** : Type d'objet : QciProfilePredefined | B - coherence interne
- **Valeur trouvee** : 50
- **Reference** : majorite=0

**Explication :**

Ce paramètre "pdbOffset" est utilisé pour définir l'offset du point de base des données (PDB) dans le système. 

Cette valeur trouvée (50) est supérieure à la référence attendue (majorité = 0), ce qui indique une non-conformité interne. 

En effet, un offset supérieur à zéro peut entraîner des problèmes de cohérence et d'exactitude dans les données stockées dans le système, ce qui pourrait avoir un impact sur la stabilité et la performance du réseau.

---
