# C03 + C04 — Rapport final

25 septembre 2026.

## Exécution et sorties

Production lue : `I:/ProjetDEv/RushPi`.
Écritures de travail limitées à :

- `I:/ProjetDEv/rushpivisualuplift/C04-Chain-Block`
- `I:/ProjetDEv/rushpivisualuplift/C03-Player-Orb`
- `I:/ProjetDEv/rushpivisualuplift/C03-C04-Gameplay-Object-Review`

Ordre : inspection code/C01, C04, proofs et choix de référence matérielle C04-C, C03, review commune. **Sept images générées via image_gen : six propositions initiales et une correction C04-C. Six masters finaux1254×1254 RGBA conservés. Aucune régénération C03.** Les masters natifs sont copiés sans modification ; le C04-C initial non retenu demeure uniquement dans le stockage de génération.

Livraison : six masters, neuf normalisés C04(128/64/32), six normalisés C03(128/64), six vues C03 corps44/32, six previews individuelles, deux planches taille/alpha, une planche C04 corps exacts, deux planches communes, un pi authored séparé de review, références/crop, notes, prompts, scorecards, rapports, deux helpers locaux et inventaires. [Liste exhaustive des fichiers](FILE-INVENTORY.md). [51 PNG : dimensions, alpha, poids et SHA-256](IMAGE-INVENTORY.json).

- [Rapport C04 et hashes](../C04-Chain-Block/final-report/C04-FINAL-REPORT.md)
- [Rapport C03 et hashes](../C03-Player-Orb/final-report/C03-FINAL-REPORT.md)
- [Review commune](C03-C04-REVIEW-SUMMARY.md)
- [Comparaison six candidats](C03-C04-COMPARISON.png)
- [Proof commun à taille gameplay](C03-C04-GAMEPLAY-SCALE-PROOF.png)
- [Implémentation réelle](CURRENT-IMPLEMENTATION.md)
- [Méthode / limites / commandes reproductibles](NORMALIZATION-AND-PROOFS.md)

## Résultat

| Famille | A | B | C | Contrôle | Décision |
|---|---:|---:|---:|---:|---|
| C04 |40|40|43|44|KEEP CURRENT ; C leader de recherche, NEEDS SECOND ROUND |
| C03 |45|39|43|44|A leader proposé, KEEP pour review humaine |

C04-C est le plus natif de B2 en matière mais moins immédiat à32px que l'existant. C03-A équilibre simplicité, volume et visibilité ; son avantage sur le contrôle est faible et qualitatif. Cercle joueur/pi authored et bloc facetté/or restent distincts. Corps normaux non agrandis : Orb44px, Chain Block environ34px dans une boîte45. Pas de nouveau hitbox suggéré dans ces conditions. Aucun changement aux rayons22/18 ni à la collision. Les views C04 corps45 sont des stress tests clairement séparés.

Tous les candidats restent lisibles, avec réserves de contraste/petites tailles détaillées ; les scores ne constituent pas une validation en mouvement. Les deux familles sont prêtes à être examinées humainement, pas à être intégrées automatiquement.

## Vérification et intégrité

Copie des références vérifiée par SHA-256 ; dimensions réelles32/64/128 des assets Chain Block de production vérifiées. PNG normalisés RGBA, bords transparents, centrage et absence de clipping contrôlés. C03 cercle fixé par une normalisation alpha explicite ; les masters ont leur alpha natif. Pi absent des sprites, présent uniquement dans ses calques et montages de review. Proofs ouverts à taille logique et inspectés sur fonds sombres/clairs.

RushPi : aucun fichier modifié par cette mission, aucun diff suivi ni indexé. C01 : tous les54 fichiers préexistants conservent leur hash, sans modification du package ou de B2. Le dépôt visuel garde ses fichiers non suivis préexistants ; seuls les trois nouveaux dossiers sont ajoutés. Aucun changement de code, logique, assets publics, CSS, Phaser ou dépendances.

Aucun commit, push, merge ou déploiement. Aucune intégration production et aucune Visual Phase B. Les seules copies supplémentaires hors laboratoire sont les sorties natives automatiques d'image_gen dans son stockage habituel.

VERDICT: READY FOR C03 + C04 HUMAN PRODUCT REVIEW

