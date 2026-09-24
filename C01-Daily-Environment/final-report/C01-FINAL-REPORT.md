# C01 — Rapport final d'exécution
24 septembre 2026.

## A. Exécution
Dépôt : Touuns/rushpivisualuplift, cloné dans `I:/ProjetDEv/rushpivisualuplift`. Branche `main`, HEAD `d0353f8759cfa92fc4c568c54e675f39ba8a8edd`.
Package utilisé : `I:/ProjetDEv/rushpivisualuplift/C01-Daily-Environment/`.
Le dossier de session initial était le dépôt de production RushPi : seules des lectures y ont été effectuées avant et après le travail. Tous les résultats sont dans le dépôt visuel séparé.

Quatre images initiales générées avec l'outil intégré image_gen, une par direction A/B/C/D. **Aucune régénération**. Aucun candidat fabriqué par filtres ou dessin procédural. Les quatre sorties originales sont copiées sans recompression dans les dossiers candidates ; leurs copies de génération restent dans le stockage local par défaut de l'outil.

Prompts source : [05-GENERATION-PROMPTS.md](../05-GENERATION-PROMPTS.md). Texte exact réellement envoyé, y compris les précisions géométriques : [C01-PROMPTS-USED.md](C01-PROMPTS-USED.md).
Le skill imagegen a guidé les quatre appels distincts, l'inspection des références et la conservation locale des résultats. L'ancienne consigne de préparation manuelle est remplacée, pour cette exécution, par la mission explicite de générer les quatre images ; l'infrastructure historique reste intacte.

Références réellement fournies à chaque génération :
1. [Daily gameplay](../references/01-daily-gameplay-414x736.png), 414×736 PNG : composition et lisibilité.
2. [Daily actuel](../references/02-current-daily-background-828w.webp), 828×1472 WebP : contrôle architectural.
3. [Chain Block](../references/03-current-chain-block-128w.png), 128×128 PNG : matériaux uniquement.
4. [Home](../references/04-home-background-828w.webp), 828×1472 WebP : cohérence du monde.
5. [Guided gameplay](../references/05-guided-gameplay-414x736.png), 414×736 PNG : silhouettes et exclusions.

Leurs cinq SHA-256 correspondent à [02-REFERENCE-MAP.md](../02-REFERENCE-MAP.md).
Le guide existant, le polygone routier et la zone HUD ont servi à l'inspection et au complément des prompts. Horizon demandé (50 %,16 %) ; HUD supérieur 20,4 % ; polygone calme (34 %,16 %),(66 %,16 %),(100 %,100 %),(0 %,100 %). Aucun masque d'inpainting n'a été appliqué.

## B. Sorties
Chemins relatifs au package C01 :

| Direction | Candidat original | Preview gameplay |
|---|---|---|
| A | [candidates/A/C01-A-v1.png](../candidates/A/C01-A-v1.png) | [review/C01-A-gameplay-preview.png](../review/C01-A-gameplay-preview.png) |
| B | [candidates/B/C01-B-v1.png](../candidates/B/C01-B-v1.png) | [review/C01-B-gameplay-preview.png](../review/C01-B-gameplay-preview.png) |
| C | [candidates/C/C01-C-v1.png](../candidates/C/C01-C-v1.png) | [review/C01-C-gameplay-preview.png](../review/C01-C-gameplay-preview.png) |
| D | [candidates/D/C01-D-v1.png](../candidates/D/C01-D-v1.png) | [review/C01-D-gameplay-preview.png](../review/C01-D-gameplay-preview.png) |

Revue complète, synthèse par candidat et notes /50 : [review/C01-REVIEW-SUMMARY.md](../review/C01-REVIEW-SUMMARY.md).
Une note courte est également disponible dans chaque dossier candidat sous `C01-X-NOTE.md`.
Ce rapport : `final-report/C01-FINAL-REPORT.md`.

| Candidat | Dimensions | Format / alpha | Octets | SHA-256 |
|---|---|---|---:|---|
| A | 941×1672 | PNG RGB, opaque | 1494244 | `d296f571945af2cf8b10ec4127d324a61fbff621e931d4fdd286338d7b5226b5` |
| B | 941×1672 | PNG RGB, opaque | 1468713 | `60c2a171baf10bfe8373bec74fda6edc112c40cab3b1b8edafe05ce1cbc4e6e7` |
| C | 941×1672 | PNG RGB, opaque | 1536967 | `e6595fcd29d84eed9d8464ac8687c627c8016b6c22ae16bbe4d77fd30614e1ac` |
| D | 941×1672 | PNG RGB, opaque | 1428605 | `84baa4263148b9008934867f3da78f110ad1abb7a7e608b502a5a4c545dd4a4f` |

Le moteur a produit 941×1672, un portrait proche du 9:16, conservé tel quel. Aucun redimensionnement n'est appliqué aux candidats originaux ; aucune livraison runtime 828×1472 n'est revendiquée.
Toutes les previews font 940×1620 ; leur zone d'image est 828×1472. Le helper existant conserve les proportions via ImageOps.contain, sans étirer ni découper le candidat.

Commande effectivement exécutée pour chaque lettre A/B/C/D, depuis le dépôt visuel :
```powershell
python C01-Daily-Environment/tools/build_c01_assets.py preview C01-Daily-Environment/candidates/A/C01-A-v1.png C01-Daily-Environment/review/C01-A-gameplay-preview.png
```

Les candidats et les quatre previews ont été ouverts et inspectés. Le helper n'a pas été modifié. Il recouvre le HUD et la piste avec la capture actuelle : le raccord horizontal à 150px logiques est un artefact de montage. Le centre, l'horizon et la lisibilité derrière le HUD sont donc aussi évalués sur les images originales ; les previews seules ne les valident pas.

## C. Évaluation
- **Meilleur candidat : B — Cinematic Architecture, 42/50, KEEP.** Meilleure profondeur et horizon le plus proche du contrat.
- **Runner-up : D — Premium Hybrid, 41/50, KEEP.** Composition équilibrée et centre calme.
- **Plus risqué : A — Refined Current, 37/50, NEEDS SECOND ROUND.** Reflets pouvant évoquer un second sol.
- **Plus original : C — Prismatic Identity, 37/50, NEEDS SECOND ROUND.** Facettes et conduits plus expressifs, mais émissions plus concurrentes.
- **Plus plausible pour une future production : B**, sous réserve de validation humaine et de tests réels ultérieurs.

Aucun faux pickup, hazard, logo, texte ou UI manifeste dans les images seules. Les quatre centres restent exploitables pour l'étude. Des réserves de convergence et de concurrence lumineuse sont détaillées dans la revue. Les quatre directions ont une différenciation modérée ; aucune promesse de gain produit ni de résultat prêt à intégrer n'est faite.
Un éventuel round 2 devrait pousser B avec la sobriété de D, calmer les émissions proches du HUD/rails et conserver l'horizon à 16 %. Aucun round 2 lancé.

## D. Intégrité
- Aucun fichier de production RushPi modifié ; lectures seules du dépôt `I:/ProjetDEv/RushPi`.
- Aucune logique gameplay touchée.
- Aucun commit, push, merge ou déploiement.
- Travail limité au laboratoire visuel pour les résultats ; seuls les fichiers natifs de sortie de l'outil restent aussi dans son stockage local.
- Références, prompts sources, masques, guides, helper et dossier Phase-A conservés sans changement.
- Les nouveaux résultats sont non suivis. Les anciens README et le rapport de préparation restent des archives de l'état avant génération ; ce rapport décrit l'exécution actuelle.

