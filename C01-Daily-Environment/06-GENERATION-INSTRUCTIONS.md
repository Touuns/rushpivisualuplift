# Manual generation instructions

## One candidate direction at a time

1. Open **ChatGPT Web Image Creation**.
2. Upload all five files from `references/` in the exact order given in [02 — reference map](02-REFERENCE-MAP.md): Daily gameplay, current Daily environment, Chain Block, Home environment, Guided gameplay.
3. Open [05 — generation prompts](05-GENERATION-PROMPTS.md), copy **one** complete prompt, and generate it separately.
4. Start with C01-A, then repeat independently for C01-B, C01-C, and C01-D. Do not ask the tool to blend all four directions at once.
5. Request one candidate per generation initially. The preferred master is 828×1472, or the nearest supported vertical 9:16 equivalent.
6. Save untouched outputs in the matching directory:

   ```text
   candidates/A/C01-A-v1.png
   candidates/B/C01-B-v1.png
   candidates/C/C01-C-v1.png
   candidates/D/C01-D-v1.png
   ```

7. If the tool returns multiple variants, preserve every useful original in the matching direction folder, with unambiguous names such as `C01-B-v1a.png`, `C01-B-v1b.png`; do not overwrite one silently.
8. Fill a row in [09 — candidate intake](09-CANDIDATE-INTAKE.md) for each file. Record the actual tool/date and any deviations such as size or format.
9. Build a fast local review preview before judging it. See below.

Do not request automatic production integration. Do not upload an art candidate into `public/`, alter application code, or replace a production asset. A visual win is a review result, not release approval.

## Local preview helper

The helper is local-only and uses the package references. It intentionally makes an approximate review composite, not a Phaser simulation. It places the candidate behind a masked current gameplay road/HUD sample so a reviewer can quickly judge corridor compatibility.

From repository root:

```powershell
python docs/Brainstorm/Visual-Uplift/C01-Daily-Environment/tools/build_c01_assets.py preview docs/Brainstorm/Visual-Uplift/C01-Daily-Environment/candidates/A/C01-A-v1.png docs/Brainstorm/Visual-Uplift/C01-Daily-Environment/review/C01-A-gameplay-preview.png
```

Use the analogous B/C/D paths. It accepts PNG, WebP, or any Pillow-readable image. It letterboxes/crops candidates to the 828×1472 review area without stretching and adds a review-only title above the image. The road/HUD mask comes from the current Daily runtime screenshot, so it is deliberately not pixel-perfect runtime compositing.

To rebuild technical overlays, reference board and current control only:

```powershell
python docs/Brainstorm/Visual-Uplift/C01-Daily-Environment/tools/build_c01_assets.py build
```

No dependencies are added to the application or `package.json`.
