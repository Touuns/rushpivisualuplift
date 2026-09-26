# C04 — Rapport final de laboratoire

25 septembre 2026.

## Exécution

Dossier : `I:/ProjetDEv/rushpivisualuplift/C04-Chain-Block`. Production inspectée uniquement en lecture. Ordre respecté : C04, review intermédiaire C04, C03, review commune.

Quatre appels image_gen : A, B, C initial, une correction C. Trois masters finaux conservés ; C initial non retenu reste seulement dans le stockage natif de génération.

[Références exactes](../references/REFERENCE-MAP.md) · [prompts exacts](../notes/C04-PROMPTS-USED.md).
Les concepts sont générés, non fabriqués par Pillow. La compétence imagegen a encadré les références, appels séparés et sauvegarde non destructive.

## Implémentation réelle et contraintes

Raster actif32/64/128 via productionAssets.ts, rendu makeChainBlock dans dailyTokens.ts. Origin.5, boîte45 avant perspective, rayon logique18. Backing et glow runtime séparés ; fallback procédural conservé.

[Constat source complet : dimensions, scaling, origin, collision et glyphes](../../C03-C04-Gameplay-Object-Review/CURRENT-IMPLEMENTATION.md). Les collisions se fondent sur les positions/seuils fixes, pas sur les pixels ; aucune autorité gameplay modifiée.

## Masters, dérivés et hashes

| Master | Dimensions / alpha | Octets | SHA-256 |
|---|---|---:|---|
| [C04-A-v1-master.png](../candidates/A/C04-A-v1-master.png) | 1254 × 1254 RGBA | 1192378 | `d28246f31f8d52784e4cd3b9d7e45ecfd3aa699c4c4796ee0a9017b24277dded` |
| [C04-B-v1-master.png](../candidates/B/C04-B-v1-master.png) | 1254 × 1254 RGBA | 1346156 | `bbc84cdea6d5f9e8836b3ce66c33c98425bfedb454bf8d2d69f26ce0eef2b082` |
| [C04-C-v1-master.png](../candidates/C/C04-C-v1-master.png) | 1254 × 1254 RGBA | 1357658 | `6220509d5e310c89585ac28110025870d62d31640011dfd77335302f4ea40067` |

Neuf dérivés PNG alpha128/64/32, corps maximal96/48/24.
Dimensions, bboxes, décalage de centre, alpha et SHA-256 de chaque dérivé : [IMAGE-METADATA.json](../review/IMAGE-METADATA.json). Tous les PNG du laboratoire et références : [inventaire commun](../../C03-C04-Gameplay-Object-Review/IMAGE-INVENTORY.json).

## Proofs et évaluation

- [Planche tailles/alpha, jeu en premier](../proofs/C04-SCALE-ALPHA-PROOF.png)
- [Corps exacts45/32 sur fond violet/blanc/noir](../proofs/C04-EXACT-BODY-STRESS.png)
- [Preview A](../proofs/C04-A-gameplay-preview.png), [B](../proofs/C04-B-gameplay-preview.png), [C](../proofs/C04-C-gameplay-preview.png)
- [Scorecard complet, notes et drapeaux de rejet](../review/C04-REVIEW-SUMMARY.md)
- [Comparaison commune](../../C03-C04-Gameplay-Object-Review/C03-C04-COMPARISON.png)

| Critère | Actuel | A | B | C |
|---|---:|---:|---:|---:|
| 1. Reconnaissance Chain Block | 5 | 5 | 4 | 4 |
| 2. Silhouette à 32 px | 5 | 4 | 4 | 3 |
| 3. Lisibilité à 45 px | 5 | 4 | 4 | 4 |
| 4. Matériaux | 3 | 4 | 4 | 5 |
| 5. Cohésion B2 / Rush Pi | 3 | 3 | 4 | 5 |
| 6. Continuité violet/or | 5 | 5 | 5 | 4 |
| 7. Glow contrôlé | 4 | 3 | 3 | 5 |
| 8. Distinction token/power-up | 5 | 4 | 4 | 5 |
| 9. Impression premium | 4 | 4 | 4 | 5 |
| 10. Plausibilité production | 5 | 4 | 4 | 3 |
| **Total /50** | 44 | 40 | 40 | 43 |


**KEEP CURRENT ; leader de recherche C04-C (43/50), NEEDS SECOND ROUND.**

A/B restent proches et trop brillants. C rapproche le matériau de B2 mais sacrifie une partie de la reconnaissance à très petite taille. L'existant gagne encore sur le critère prioritaire. Pas de remplacement proposé.

Les preuves sont statiques, pas une simulation parfaite de Phaser. [Limites détaillées](../../C03-C04-Gameplay-Object-Review/NORMALIZATION-AND-PROOFS.md) : fond B2 latéral seulement, montage local, contrôle à une phase de pulse, traitements runtime additionnels approximés. Aucune validation en mouvement ou de states power-up.

## Intégrité

Aucune intégration production, aucun fichier RushPi écrit, aucun gameplay, asset public, Phaser, CSS, logique ou dépendance modifié. C01 inchangé. Aucun commit/push/merge/déploiement. Résultats uniquement dans les trois nouveaux dossiers autorisés ; copies natives image_gen dans son stockage habituel. [Rapport commun](../../C03-C04-Gameplay-Object-Review/FINAL-REPORT.md).

