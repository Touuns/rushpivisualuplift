# C03 — Rapport final de laboratoire

25 septembre 2026.

## Exécution

Dossier : `I:/ProjetDEv/rushpivisualuplift/C03-Player-Orb`. Production inspectée uniquement en lecture. Ordre respecté : C04, review intermédiaire C04, C03, review commune.

Trois appels image_gen, aucune régénération. Trois masters finaux sans pi. Référence matériau C04-C choisie après sa review ; pas de transfert de sa silhouette à l'Orb.

[Références exactes](../references/REFERENCE-MAP.md) · [prompts exacts](../notes/C03-PROMPTS-USED.md).
Les concepts sont générés, non fabriqués par Pillow. La compétence imagegen a encadré les références, appels séparés et sauvegarde non destructive.

## Implémentation réelle et contraintes

Orb actuel procédural dans MainScene.makeOrb/createPlayer : corps radius22, fill violet, stroke blanc2, halo séparé radius41.8. Pi runtime Georgia Bold25px séparé, origine.5, y−1. Pulse1.06 existant. Aucun raster Orb actif à remplacer directement.

[Constat source complet : dimensions, scaling, origin, collision et glyphes](../../C03-C04-Gameplay-Object-Review/CURRENT-IMPLEMENTATION.md). Les collisions se fondent sur les positions/seuils fixes, pas sur les pixels ; aucune autorité gameplay modifiée.

## Masters, dérivés et hashes

| Master | Dimensions / alpha | Octets | SHA-256 |
|---|---|---:|---|
| [C03-A-v1-master.png](../candidates/A/C03-A-v1-master.png) | 1254 × 1254 RGBA | 777832 | `91dff0df1df73af0d50626a4bdced9e911d9ccb49ba38eb88b0634c6c1af3246` |
| [C03-B-v1-master.png](../candidates/B/C03-B-v1-master.png) | 1254 × 1254 RGBA | 997795 | `d3824420999330a500d12249c074b2355fa91b47ce4d1b7db71308e55bb6c7f3` |
| [C03-C-v1-master.png](../candidates/C/C03-C-v1-master.png) | 1254 × 1254 RGBA | 904266 | `cc87b8b361a32e93a1018e4f979845d6a51bef1c1674987b1080585f9ddb98d4` |

Six dérivés PNG alpha128/64, corps112/56, plus six vues de proof corps44/32. Masque circulaire technique mineur, explicite ; masters préservés.
Dimensions, bboxes, décalage de centre, alpha et SHA-256 de chaque dérivé : [IMAGE-METADATA.json](../review/IMAGE-METADATA.json). Tous les PNG du laboratoire et références : [inventaire commun](../../C03-C04-Gameplay-Object-Review/IMAGE-INVENTORY.json).

## Proofs et évaluation

- [Planche tailles/alpha, jeu en premier](../proofs/C03-SCALE-ALPHA-PROOF.png)
- [Preview A](../proofs/C03-A-gameplay-preview.png), [B](../proofs/C03-B-gameplay-preview.png), [C](../proofs/C03-C-gameplay-preview.png)
- [Scorecard complet, notes et drapeaux de rejet](../review/C03-REVIEW-SUMMARY.md)
- [Comparaison commune](../../C03-C04-Gameplay-Object-Review/C03-C04-COMPARISON.png)

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


**C03-A (45/50), KEEP pour validation humaine.**

A apporte du volume avec la meilleure simplicité des nouvelles propositions. B est trop travaillé intérieurement ; C se fond davantage dans la piste. A ne prouve pas une meilleure performance de jeu que le contrôle : son avantage45/44 est une préférence visuelle faible.

Les preuves sont statiques, pas une simulation parfaite de Phaser. [Limites détaillées](../../C03-C04-Gameplay-Object-Review/NORMALIZATION-AND-PROOFS.md) : fond B2 latéral seulement, montage local, contrôle à une phase de pulse, traitements runtime additionnels approximés. Aucune validation en mouvement ou de states power-up.

## Intégrité

Aucune intégration production, aucun fichier RushPi écrit, aucun gameplay, asset public, Phaser, CSS, logique ou dépendance modifié. C01 inchangé. Aucun commit/push/merge/déploiement. Résultats uniquement dans les trois nouveaux dossiers autorisés ; copies natives image_gen dans son stockage habituel. [Rapport commun](../../C03-C04-Gameplay-Object-Review/FINAL-REPORT.md).

