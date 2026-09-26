# C03 — Review gameplay d'abord

25 septembre2026. Évaluation sur dérivés normalisés, corps44/32 sans puis avec pi authored séparé, avant examen des masters. [Proof taille/alpha](../proofs/C03-SCALE-ALPHA-PROOF.png).

| Critère | Actuel | A | B | C |
|---|---:|---:|---:|---:|
| 1. Reconnaissance joueur | 5 | 5 | 4 | 5 |
| 2. Silhouette circulaire parfaite | 5 | 5 | 5 | 5 |
| 3. Lisibilité à 44 px | 5 | 5 | 4 | 4 |
| 4. Lisibilité à 32 px | 5 | 4 | 3 | 4 |
| 5. Matériaux | 2 | 4 | 4 | 5 |
| 6. Séparation piste violette | 5 | 4 | 3 | 3 |
| 7. Séparation Chain Block | 5 | 5 | 5 | 5 |
| 8. Glow contrôlé | 4 | 5 | 4 | 5 |
| 9. Impression premium | 3 | 4 | 4 | 4 |
| 10. Plausibilité production | 5 | 4 | 3 | 3 |
| **Total /50** | 44 | 45 | 39 | 43 |


**Leader proposé : C03-A — KEEP,45/50**, avantage faible et qualitatif sur le contrôle44/50. Le progrès concerne le volume et la matière ; l'existant garde la meilleure uniformité de contraste. Aucun droit d'intégration.

## A — Refined Current — 45/50

Le plus simple et le plus clair des nouveaux Orbs. Le reflet large et la transition douce apportent du volume sans détourner l'attention du pi. Cercle lisible à44 et32, séparation nette du bloc angulaire ; la moitié inférieure est moins lumineuse que celle de l'actuel, réserve réelle sur piste sombre. KEEP pour review humaine, pas victoire de gameplay démontrée.
[Master](../candidates/A/C03-A-v1-master.png) · [Preview](../proofs/C03-A-gameplay-preview.png).

## B — Prismatic Core — 39/50

Les grandes courbes internes traversent davantage le visage de l'Orb et ressemblent à une bille décorative. Le pi reste lisible, mais la matière n'apporte pas assez à32 et complexifie le héros. NEEDS SECOND ROUND ; simplifier plutôt qu'ajouter du glow.
[Master](../candidates/B/C03-B-v1-master.png) · [Preview](../proofs/C03-B-gameplay-preview.png).

## C — Premium Hybrid — 43/50

Belle matière sombre, fine influence indigo de B2, forme simple. Le bas et une partie de la face sont plus sombres que A : plus cohérent au décor, moins saillant contre la piste. NEEDS SECOND ROUND ; ne pas confondre cohésion et perte de hiérarchie joueur/décor.
[Master](../candidates/C/C03-C-v1-master.png) · [Preview](../proofs/C03-C-gameplay-preview.png).

## Cercle, pi, rejet et limites

Les masters sont presque circulaires, pas mathématiquement parfaits. Une normalisation alpha explicite, uniforme et sans recoloration établit le cercle des dérivés. Corps112×112 centré dans128 ;56×56 dans64. Les vues44/32 sont effectivement44×44 et32×32 de corps. Pas de corps supérieur au rayon22 nominal ni de satellites, de spikes ou de halo externe intégré.

Aucun pi, texte ou logo généré. Le calque pi de review reprend la police et les paramètres observés, avec un rasterizer différent de Phaser. Sans pi, les Orbs sont des sphères génériques ; avec l'identité authored et leur position joueur ils restent reconnaissables. Aucun anneau crypto ni bloc facetté rond. Pas d'effondrement constaté à32 ou de dépendance à un énorme halo ; B/C ont toutefois moins de contraste sur la piste.

Le contrôle screenshot inclut une phase du pulse existant jusqu'à1.06 : il n'est pas strictement au repos44. Le nouveau proof44 n'implique ni la suppression ni l'augmentation de ce pulse. L'image plate actuelle conserve sa force iconique ; le léger avantage de A doit être confirmé humainement. Ni mouvement, ni states Shield/Magnet/charge n'ont été simulés.

