# C01-B2 — Review ciblée

25 septembre 2026. Review interne qualitative ; les notes sont un jugement visuel, pas une mesure de performance joueur.

## Contexte et décisions conservées

Le [premier round](../../review/C01-REVIEW-SUMMARY.md) donnait A 37/50, B 42/50, C 37/50, D 41/50. B est la base principale, D le runner-up, C une banque d'identité ; A n'est pas repris comme base.

B gagnait par la profondeur, le grand centre calme et la convergence proche de la cible. Ses longues émissions violettes et sa symétrie restaient perfectibles. D proposait des surfaces propres, mais un horizon légèrement plus bas et des accents chauds hauts. C apportait des facettes intéressantes, avec trop de concurrence lumineuse. Les reflets de A risquaient d'évoquer un second sol : ils ne doivent pas revenir.

Objectif B2 : garder la géométrie et la profondeur de B ; modérer la lumière dans l'esprit de D ; ajouter très peu de facettes de C. Un seul nouveau candidat, aucun nouveau batch.

## Références et méthode

Lectures : les quatre notes individuelles, le review summary initial, le rapport final d'exécution, les prompts initiaux, les contrats de composition/DA/intégration, la carte des références et le scorecard. Inspection des quatre candidats, de leurs quatre composites, de la planche des cinq références et du guide de génération.

Entrées réellement envoyées à image_gen : [B](../../candidates/B/C01-B-v1.png), [D](../../candidates/D/C01-D-v1.png), [C](../../candidates/C/C01-C-v1.png), [capture Daily](../../references/01-daily-gameplay-414x736.png), [Chain Block](../../references/03-current-chain-block-128w.png), dans cet ordre. La capture et le Chain Block n'autorisent pas leur reproduction dans le décor. [Prompt exact](../notes/C01-B2-PROMPT-USED.md).

Un appel à l'outil intégré ; aucune régénération. Le PNG natif est conservé sans retouche ni recompression. Le helper existant produit la preview sans modification. La comparaison présente chaque image et chaque viewport gameplay à 414 × 736 ; elle a été ouverte et inspectée ainsi que le rendu brut et la preview pleine taille.

## Livrables visuels

- [C01-B2-v1.png](../generated/C01-B2-v1.png) : 941 × 1672, PNG RGB opaque, proche 9:16 ; pas encore un asset runtime normalisé.
- [C01-B2-gameplay-preview.png](../preview/C01-B2-gameplay-preview.png) : 940 × 1620, cadre du helper, viewport 828 × 1472.
- [B / B2 / D](C01-B-B2-D-comparison.png) : 1282 × 1570, trois colonnes, brut puis composite. Ce fichier est une planche de review, pas un autre candidat.

## Analyse du rendu brut

Le point de fuite paraît conservé près de x=50 %, y=16 %, estimé visuellement. Les mêmes grandes parois et leur succession vers l'horizon maintiennent la profondeur de B. Le bas central demeure sombre et sans surface de chaussée, reflet de sol ou objet.

Le changement visible porte sur les longs rubans violets et les inserts dorés : leur cœur lumineux et leur halo sont moins dominants. Les facettes et arêtes restent lisibles. Les traits cyan conservent leur rôle architectural et secondaire.

Les défauts de B ne sont pas tous résolus : répétition bilatérale et symétrie restent très marquées. L'apport identitaire de C est discret au point de ne pas constituer un gain net à taille mobile. Les accents cyan et certains biseaux chauds attirent encore l'œil sur les bords. La brume violette de l'horizon reste visible ; elle ne devient pas un portail ni un objet détaché.

## Analyse de la preview composite

Les côtés de B2 rivalisent moins avec les rails dorés et les Chain Blocks que ceux de B. Ce gain apparaît notamment sur les longues coutures violettes latérales dans la moitié haute du décor visible. Les volumes ne disparaissent pas dans le noir et la continuité violet/indigo reste cohérente.

La piste procédurale conserve une lecture plate face aux parois volumétriques. B2 atténue la concurrence lumineuse, mais ne démontre pas la résolution du décalage entre piste et décor identifié dans l'audit.

**Limite déterminante :** le helper recouvre intégralement le polygone de piste ET le haut y=0–150 logique avec la capture actuelle. Le centre du candidat, son horizon et son vrai fond sous le HUD ne sont donc pas visibles dans le composite. Les objets, la piste et le HUD y sont identiques par construction. Leur lisibilité inchangée n'est pas une preuve d'amélioration de B2. Le raccord horizontal à y=150 est un artefact commun aux previews. Pas de test de mouvement, de transparence réelle de piste, ni de validation sur appareil.

## Comparaison directe avec B

| Aspect | B | B2 | Conclusion |
|---|---|---|---|
| Centre et espace disponible | Très calme | Très calme | Équivalent |
| Géométrie et profondeur | Meilleures du round 1 | Très fidèlement conservées | Équivalent |
| Émissions latérales | Longues bandes violettes/or dominantes | Bandes atténuées, volumes encore lisibles | Gain visible B2 |
| Identité prismatic | Cohérente, répétitive | Cohérente, apport C discret | Pas de progrès net |
| Impression premium | Forte | Forte, plus retenue | Préférence légère B2 |
| Composite | Décor parfois concurrent des objets | Côtés moins concurrentiels | Gain limité aux zones visibles |

B2 améliore le compromis de B plutôt que de proposer une architecture nouvelle. La préférence repose sur la retenue lumineuse sans perte visible de profondeur, pas sur le fait qu'il s'agit du round 2.

## Comparaison secondaire avec D

D reste convaincant par ses surfaces et son centre propre. B2 conserve cependant l'horizon plus haut et l'échelonnement des masses de B. Dans la comparaison, les larges accents chauds de D et sa brume latérale sont plus présents. B2 réalise mieux la sobriété recherchée, mais ne dépasse pas clairement D en originalité.

## Scorecard /50

Les scores B et D sont repris sans réécriture de la review initiale. 1 = insuffisant ; 5 = très fort pour ce laboratoire. La plausibilité production reste provisoire.

| Critère | B | D | B2 |
|---|---:|---:|---:|
| 1. Lisibilité du centre | 5 | 5 | 5 |
| 2. Compatibilité piste | 4 | 4 | 4 |
| 3. Profondeur | 5 | 4 | 5 |
| 4. Qualité des matériaux | 4 | 4 | 4 |
| 5. Identité Rush Pi | 4 | 4 | 4 |
| 6. Cohérence lumineuse | 4 | 4 | 5 |
| 7. Maîtrise du bruit visuel | 4 | 4 | 5 |
| 8. Séparation objets / décor | 4 | 4 | 4 |
| 9. Impression premium | 4 | 4 | 4 |
| 10. Plausibilité production | 4 | 4 | 4 |
| **Total** | **42** | **41** | **44** |

Les deux points supplémentaires concernent la lumière et le bruit. La note de séparation objets/décor n'est pas augmentée : la preview ne permet pas d'en faire une validation réelle.

## Drapeaux de rejet

Aucun faux pickup, pièce/orbe dorée, forme Shield cyan, objet rouge de type hazard, texte, logo, HUD peint, personnage, portail, voie, rail factice ou occlusion centrale majeure manifeste sur le rendu brut. Pas de nouvelle rupture de perspective constatée. Les traits lumineux restent attachés aux parois.

La concurrence effective avec le HUD et les objets en mouvement reste non vérifiée. La symétrie donne encore un aspect conceptuel répétitif, mais pas au point de déclencher ici le rejet pour rendu générique. Toute confusion détectée en validation ultérieure devra primer sur le total.

## Verdict

**KEEP — 44/50. B2 surpasses B.**

Avantage modeste et circonscrit à la review statique : émissions moins agressives avec géométrie et centre préservés. B2 devient la proposition prioritaire à soumettre au propriétaire produit. Ce n'est ni une supériorité objectivement démontrée en jeu ni une autorisation d'intégration. B reste la référence forte ; D reste utile. Aucun autre finaliste généré.

