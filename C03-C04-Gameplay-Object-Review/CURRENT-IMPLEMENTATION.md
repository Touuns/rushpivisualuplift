# Implémentation actuelle — constat en lecture seule

25 septembre 2026. Racine source : `I:/ProjetDEv/RushPi`. Aucun code importé/exécuté pour modifier le jeu. Les commentaires historiques « lane + y » ont été confrontés au code de collision actuel, qui utilise la position x autoritaire pendant les transitions.

| Sujet | Source réelle | Constat |
|---|---|---|
| Canvas / rayons | `src/game/gameConfig.ts:9`, `:23`, `:41` | 414 × 736 ; joueur radius 22 ; objets radius 18 ; trois voies ; tween 110 ms ; joueur y=0.8×736=588.8 |
| Orb | `src/game/scenes/MainScene.ts:522`, `:558` | Procédural Phaser, pas un raster chargé. Arc centré (0,0) : corps violet radius 22, stroke blanc 2px alpha .85 ; container placé sur le joueur, depth 10 |
| Palette / halo | `src/game/theme.ts:14`, `:40` | Player #8b5cf6 ; halo radius 22×1.9=41.8, alpha .18 ; halo décoratif, pas corps ni collision |
| π | `src/game/scenes/MainScene.ts:571` | Text séparé, Georgia / Times New Roman / serif, bold, round(22×1.15)=25px, blanc alpha .95, origin .5, position (0,-1) |
| Orb mouvement visuel | `src/game/scenes/MainScene.ts:599` | Idle tween scale 1.06, 720ms, yoyo. Corps nominal 44px ; pulsation jusqu'à 46.64px avant stroke. Le rayon logique reste 22 |
| Décors joueur additionnels | `src/game/scenes/MainScene.ts:584` | Shield radius31 stroke3 ; magnet radius28 stroke2 ; charge radius27 stroke3. Masqués hors activation ; π pulse/FX et traînée sont indépendants |
| Chain Block chargé | `src/game/productionAssets.ts:46`, `:68`, `:219` | Clé prod:chain-block ; PNG 32/64/128 choisi selon DPR et heuristique appareil, préchargé avant Daily, enregistré en TextureManager |
| Raster effectif | `public/assets/rushpi/production/collectibles/chain-block-production-{32,64,128}w.png` | Famille raster actuelle ; référence copiée depuis la variante 128. Les anciens SVG du manifeste ne sont pas le rendu Daily raster actif |
| Chain Block rendu | `src/game/dailyTokens.ts:289` | Image origin .5, setDisplaySize(18×2.5)=45×45, container centré. Sans texte/glyphe. Glow blanc radius30.6 alpha .1 blend ADD, backing #0c0717 radius23.4 alpha .5 séparés |
| Chain Block fallback | `src/game/dailyTokens.ts:313` | Si texture absente : corps carré or 28.8px, contour violet, deux petits carrés liés et halo. Aucun changement apporté |
| Spawn / rôle | `src/game/scenes/MainScene.ts:747`, `:1559` | Daily energy -> makeChainBlock ; reste type energy, combo/magnet inchangés ; depth5, sous joueur |
| Perspective | `src/game/track.ts:254`, `src/game/theme.ts:63` | p=clamp((y−117.76)/(588.8−117.76),0,1) ; scale=.5+.6p ; boîte Chain Block 22.5px au loin à 49.5px près du joueur. Origin central conservé |
| Collision effective | `src/game/scenes/MainScene.ts:846`, `:895`, `src/game/laneTransition.ts:132` | Hors règles Magnet : abs(playerX−centreVoieObjet)≤40 ET abs(objectY−playerY)≤40, somme22+18. Pas de collision circulaire au pixel, ni de hitbox tirée de l'alpha, de la taille du sprite ou de sa projection |
| Exceptions gameplay | `src/game/scenes/MainScene.ts:907` | Magnet a son reach existant pour energy, invulnérabilité et effets restent autoritaires ; aucune modification |

Le corps opaque de la référence Chain Block 128 mesure environ 88×96px au seuil alpha128 ; la boîte de fichier n'est pas sa silhouette. Dans une boîte d'affichage 45px, ce corps occupe environ 31×34px. Normaliser un nouveau corps à 45px **tout en l'appelant équivalent au runtime** le grossirait. Les dérivés C04 conservent donc 75 % d'occupation maximale du fichier, et les proofs de corps 45px sont explicitement des stress tests.

**Visuel uniquement :** textures, facettes, alpha, couleur, reflets, halo/backing, pi, stroke, perspective et pulses. **Autorité gameplay :** rayons logiques, positions de transition, seuils de collision, voies, règles Magnet, spawns/RNG/scoring. Les nouveaux PNG sont des études, pas des remplacements prêts à charger.

