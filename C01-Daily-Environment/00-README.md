# C01 — Daily Distant Side Architecture / Environment Plate

**Status:** prepared manual-generation and review package; no candidate is selected or integrated.

C01 is a deliberately narrow, offline visual-art experiment. It asks whether one generated **decorative Daily environment plate** can make the existing procedural track feel part of a more premium, coherent world. It is not gameplay redesign, production integration, or a replacement for Phaser geometry.

Start here:

1. Read [01 — context and goal](01-CONTEXT-AND-GOAL.md), [02 — reference map](02-REFERENCE-MAP.md), and [03 — composition and safe zones](03-COMPOSITION-AND-SAFE-ZONES.md).
2. In ChatGPT Web Image Creation, upload the five files in `references/` in the documented order.
3. Run exactly one of the four self-contained prompts in [05 — generation prompts](05-GENERATION-PROMPTS.md), one generation at a time, following [06 — generation instructions](06-GENERATION-INSTRUCTIONS.md).
4. Save the untouched output under its matching `candidates/A` through `candidates/D` folder and complete [09 — candidate intake](09-CANDIDATE-INTAKE.md).
5. Create a local comparison preview with `tools/build_c01_assets.py` and judge it with [07 — review scorecard](07-REVIEW-SCORECARD.md).

The immutable implementation boundary is in [08 — integration constraints](08-INTEGRATION-CONSTRAINTS.md). The concise completion record is [FINAL-REPORT](FINAL-REPORT.md).

## Package contents

- `references/` — exact, checksum-verified copies of the five uploaded product references.
- `masks/` and `overlays/` — technical composition guides only; never production art.
- `contact-sheets/C01-reference-board.png` — human review board.
- `candidates/A` … `D` — manual-generation intake only; no fabricated candidate art.
- `review/` — current control and later local comparison previews.
- `tools/build_c01_assets.py` — dependency-free-from-the-repository local helper (uses the already available Pillow Python package).

All paths are relative to this C01 folder unless stated otherwise. This entire directory is untracked review material and must stay outside runtime `public/` assets.
