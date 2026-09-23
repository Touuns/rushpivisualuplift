# Reference map

Upload these exact copies to ChatGPT Web Image Creation **in this order**. They are evidence and art-direction constraints, not instructions to copy text, logos, gameplay objects, or UI into the generated plate.

| # | Package file | Verified source path | Use | Dimensions / format / bytes | SHA-256 |
|---:|---|---|---|---|---|
| 01 | `references/01-daily-gameplay-414x736.png` | `docs/Brainstorm/Visual-Audit/10-REFERENCE-SCREENSHOTS/daily-midrun-414x736.png` | Runtime composition, HUD safe area, road projection, object density, player area and readability | 414×736 PNG; 162,371 bytes | `d03d19e956ea46aae4bb8e114b708a0263a6dbe2cf5a7e08ac0ca5a00b1a4c38` |
| 02 | `references/02-current-daily-background-828w.webp` | `public/assets/rushpi/production/backgrounds/daily-market-tunnel-production-828w.webp` | Current Daily control, palette, material language and architecture | 828×1472 WebP; 36,800 bytes | `ed8c001d800fad29f23d8353e62368717f10a32b90beb59aff46db1f7a076289` |
| 03 | `references/03-current-chain-block-128w.png` | `public/assets/rushpi/production/collectibles/chain-block-production-128w.png` | Violet/gold material vocabulary and energy-object finish only | 128×128 PNG with alpha; 18,085 bytes | `9794b9718b39ecf129688b68cdae15078fe595a6c250f05ceeb56306ce94175b` |
| 04 | `references/04-home-background-828w.webp` | `public/assets/rushpi/production/backgrounds/home-background-production-828w.webp` | Broader Rush Pi architectural/material identity and cross-screen consistency | 828×1472 WebP; 46,298 bytes | `f9b04176e5af900695eaa572223cd2c7ce95fdfd66fdd4e9bd26261ea0fa68d0` |
| 05 | `references/05-guided-gameplay-414x736.png` | `docs/Brainstorm/Visual-Audit/10-REFERENCE-SCREENSHOTS/guided-gameplay-414x736.png` | Clean player/hazard/track silhouette and readability baseline | 414×736 PNG; 29,945 bytes | `610b2d015fdfd6a1f62acdcad299652698a2753b8de936112b3604aa0d313537` |

## Copy integrity

The package-copy SHA-256 hashes equal their respective source hashes above. Copies preserve original encoding; no source has been recompressed or altered.

## Supporting technical references

- [C01 reference board](contact-sheets/C01-reference-board.png) presents all five assets with labels for human review.
- `masks/c01-road-exclusion-*` and `masks/c01-hud-safe-zone-*` explain where generated detail must not compete.
- `overlays/c01-generation-guide-*` combines the guide regions. Do not upload an overlay as a creative reference unless deliberately using it as a composition constraint.
