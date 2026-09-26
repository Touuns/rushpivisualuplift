# Normalisation et limites des proofs

Les six concepts retenus proviennent de l'outil intégré image_gen. Pillow n'a créé aucun concept : il effectue uniquement crop de référence, normalisation alpha, réduction, typographie de review et montage. La compétence imagegen a guidé les générations séparées, les références et la conservation des masters.

## Masters et alpha

Tous les masters finaux sont des PNG RGBA 1254×1254, avec transparence véritable. Ils sont conservés octet pour octet. Les générations contiennent quelques pixels parasites alpha1–3, jusque sur les bords du fichier ; ce n'est pas un fond opaque. Les dérivés retirent uniquement ces pixels quasi invisibles. Le resize se fait en alpha prémultiplié, puis retour RGBA, afin d'éviter une frange sombre.

C04 : crop du support alpha, mise à l'échelle uniforme selon bbox alpha≥8, occupation corporelle maximale 75 % du fichier, recentrage. Sorties128/64/32. À alpha128, corps max96/48/24px respectivement, conforme à l'occupation de l'ancien128. Aucun renforcement de glow, aucun pi, aucune recoloration. En boîte45, rayon opaque maximal mesuré : A17.03px, B16.40px, C17.03px, inférieur à18 ; cela ne remplace pas le calcul de collision réel.

C03 : masters presque circulaires, mais alpha imparfait et petite ovalisation A/B. Normalisation technique explicite : recherche du cercle inscrit au seuil alpha128 sur360 directions, marge interne1px, crop carré uniforme puis masque alpha circulaire anticrénelé. Refus automatique si min/max des rayons<.95. Aucun étirement, ajout de matière ou recoloration. Cette opération rogne très légèrement le bord et n'est pas présentée comme une propriété parfaite du master brut. Dérivés128 avec corps112 ; dérivés64 avec corps56 ; centres exacts(.5,.5), transparence sur tous les bords. Les vues corps44 et32 sont des proofs sans marge externe ; leur cercle touche normalement les tangentes du cadre. Les vrais sprites normalisés gardent leur marge.

Pour afficher un corps44 à partir du normalisé C03, la boîte théorique est44/.875≈50.29px ; le montage emploie directement le crop corporel44. Ne pas confondre cette boîte avec le diamètre gameplay. Aucune intégration de cette convention n'a été faite.

## Contrôle à taille réelle

Les planches doivent être vues à100 % : 1pixel image=1pixel logique. C04 présente128/64/45/32 en boîte fichier et une autre planche montre des corps exacts45/32 sur violet, blanc et noir. Les corps32 sont plus grands que ceux d'un fichier32 runtime : les deux tests sont identifiés. C03 présente les corps44/32 en premier, sans puis avec pi, ainsi que des agrandissements pour inspection. Le contrôle actuel est un crop de capture, donc rasterisé et pris à une phase de pulse ; son corps peut être légèrement supérieur au nominal44. Ce biais ne doit pas être interprété comme un gain du nouveau sprite.

## Composites

La base reprend le viewport de la preview B2 existante, sans modifier C01. Comme le helper C01, elle conserve l'ancien haut y0–150 et toute la piste ; seuls les côtés montrent B2. Cela ne prouve pas un vrai rendu du nouveau fond sous la piste.

C04 : un candidat est **ajouté** dans la voie centrale à(207,510), boîte45px, pendant que les anciens objets restent visibles pour comparaison. À cet y la projection normale serait≈1 ; le test utilise exactement1 pour comparer les familles. Backing et faible lueur sont deux calques de review séparés ; le mélange Pillow n'est pas une simulation exacte du blend ADD de Phaser. Le chevron sous-jacent et les autres objets de la capture sont conservés. Aucun spawn réel n'a été produit.

C03 : position joueur(207,589), corps44. L'ancien corps et son pi sont retirés dans une petite région par interpolation horizontale du fond de la même ligne ; le halo externe de la capture est conservé. C'est une réparation de montage local, pas une reconstruction exacte du runtime. Les proofs isolés permettent de vérifier la séparation sans halo.

Le **pi est un PNG séparé de review**, dessiné d'après Georgia Bold25px, blanc alpha.95, offsety−1. Son anticrénelage/alignement peuvent différer de Phaser. Aucun pi n'est présent dans les masters, normalisés ou vues corps seuls. Il n'est ajouté qu'aux planches et composites.

## Reproduction

Depuis `I:/ProjetDEv/rushpivisualuplift`, Pillow déjà installé, aucun package projet ajouté :

```powershell
python C03-C04-Gameplay-Object-Review/tools/build_object_proofs.py controls
python C03-C04-Gameplay-Object-Review/tools/build_object_proofs.py C04
python C03-C04-Gameplay-Object-Review/tools/build_object_proofs.py C03
python C03-C04-Gameplay-Object-Review/tools/build_object_proofs.py common
python C03-C04-Gameplay-Object-Review/tools/build_scale_checks.py
```

Les scripts écrivent uniquement dans les trois nouveaux dossiers. Arial et Georgia Bold sont lus depuis Windows. Pas de runtime, navigateur, serveur, RNG gameplay ni réseau. Les scripts régénèrent les dérivés/proofs, jamais les masters.

[Inventaire PNG avec dimensions, alpha, octets et SHA-256](IMAGE-INVENTORY.json).

