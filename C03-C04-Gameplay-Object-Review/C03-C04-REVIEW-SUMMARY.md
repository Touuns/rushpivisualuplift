# C03 + C04 — Review commune

25 septembre 2026. B2 est la référence de laboratoire approuvée humainement par le propriétaire produit ; aucune intégration C01 ni objets n'est autorisée par cette mission.

## Décision proposée

| Famille | Contrôle actuel | A | B | C | Proposition |
|---|---:|---:|---:|---:|---|
| C04 Chain Block |44/50|40/50|40/50|43/50|**KEEP CURRENT**. C est l'unique leader de recherche, **NEEDS SECOND ROUND** |
| C03 Player Orb |44/50|45/50|39/50|43/50|**A — KEEP**, faible préférence visuelle à soumettre humainement |

Ces scores sont qualitatifs ; aucune mesure de temps de reconnaissance. Les colonnes C03/C04 utilisent des critères différents et ne s'additionnent pas. Aucun rejet critique ne peut être compensé par un score total.

## Lecture à taille réelle

Ouvrir à100 % : [six previews individuelles réunies](C03-C04-COMPARISON.png), [contrôle actuel / B2 / couple étudié](C03-C04-GAMEPLAY-SCALE-PROOF.png), [C04 tailles et alpha](../C04-Chain-Block/proofs/C04-SCALE-ALPHA-PROOF.png), [C04 corps32/45 exacts](../C04-Chain-Block/proofs/C04-EXACT-BODY-STRESS.png), [C03 corps44/32 avec pi séparé](../C03-Player-Orb/proofs/C03-SCALE-ALPHA-PROOF.png).

La planche commune montre **C04-C + C03-A comme étude de cohérence**, pas deux vainqueurs autorisés pour production. Les autres Chain Blocks de la capture restent visibles. C04-C est un ajout de review à(207,510) ; C03-A est au centre joueur(207,589). Le choix de montrer C n'annule pas KEEP CURRENT.

## Cohésion avec B2

**C04-C paraît-il natif de B2 ?** Oui pour les grandes facettes, le violet sombre et le noyau or unique. C'est le meilleur rapprochement matière de ce lot. Non pour une adoption immédiate : en boîte32 son noyau et ses volumes ont moins de saillance que l'actuel. La suppression des connexions dorées coûte une part de reconnaissance.

**C03-A paraît-il natif de B2 ?** Suffisamment pour un héros : matière violette plus volumétrique, reflet large, bord contrôlé. Il reste volontairement plus clair que le décor. C03-C était plus sombre et plus intégré à B2, mais moins séparé de la piste ; il ne gagne pas pour cette seule cohésion.

## Différenciation gameplay

**C03 et C04 restent-ils immédiatement distincts ?** Oui dans les proofs : silhouette circulaire simple à identité pi blanche séparée contre bloc angulaire à petit noyau or. Aucun cercle doré/token, aucune forme cyan Shield, pas de rouge hazard, pas de pi ou de logo dans les nouveaux sprites. Sans overlay pi, l'Orb reste une sphère générique ; la référence de héros inclut nécessairement l'identité authored du jeu.

**Suggèrent-ils une autre hitbox ?** Pas dans les dérivés normalisés et à la taille de proof prescrite : Orb corps44 soit rayon22, Chain Block corps≈34 dans boîte45, rayon opaque mesuré≤17.03. La boîte et les halos runtime ne sont pas des hitboxes. Les tests de corps C04 exact45 sont volontairement plus grands et ne doivent pas être utilisés comme consigne de sizing runtime. La collision réelle est un test de positions sur deux axes, pas une collision circulaire pixel-perfect.

**Survivent-ils à la taille réelle ?** C03-A oui à44 et32, avec une réserve de moindre uniformité que le contrôle. C04-C reste identifiable mais moins immédiat à32, et ne bat donc pas l'existant. A/B C04 sont plus proches de l'ancien mais trop lumineux pour apporter un bénéfice convaincant. Aucun nouveau gagnant C04 forcé.

**Prêts pour human/product review ?** Oui : six masters, dérivés propres, contrôles, scorecards, provenance et limites explicites. Non pour une intégration automatique.

## Limites à conserver dans la décision

Les composites héritent du helper C01 : HUD et piste de l'ancienne capture, B2 seulement sur les côtés. Le pi ajouté est un rendu authored local selon Georgia Bold, non une extraction de texture Phaser. L'effacement du joueur initial est une réparation de montage. Le contrôle est capturé pendant un pulse ; le candidat est montré au corps nominal44. Les proofs ne simulent pas mouvement, transparence complète de piste, Shield/Magnet, charge ou animations. La validation mobile réelle reste une étape distincte, non exécutée.

Les masters presque circulaires C03 ont reçu une normalisation alpha circulaire mineure ; ne pas attribuer la perfection géométrique des dérivés à la génération brute. [Méthode complète](NORMALIZATION-AND-PROOFS.md).

[Review C04](../C04-Chain-Block/review/C04-REVIEW-SUMMARY.md) · [Review C03](../C03-Player-Orb/review/C03-REVIEW-SUMMARY.md) · [Implémentation source](CURRENT-IMPLEMENTATION.md).

