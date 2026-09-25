"""Local review evidence only; never changes candidate art or the existing helper."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROUND = Path(__file__).resolve().parents[1]
C01 = ROUND.parent
ITEMS = [
    ("B | round 1", C01 / "candidates/B/C01-B-v1.png", C01 / "review/C01-B-gameplay-preview.png"),
    ("B2 | round 2", ROUND / "generated/C01-B2-v1.png", ROUND / "preview/C01-B2-gameplay-preview.png"),
    ("D | round 1", C01 / "candidates/D/C01-D-v1.png", C01 / "review/C01-D-gameplay-preview.png"),
]
board = Image.new("RGB", (1282, 1570), "#090612")
draw = ImageDraw.Draw(board)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
for i, (title, raw, preview) in enumerate(ITEMS):
    x = 10 + i * 424
    draw.text((x, 12), title + " - RAW / 414 x 736", font=font, fill="white")
    fitted = ImageOps.contain(Image.open(raw).convert("RGB"), (414, 736), Image.Resampling.LANCZOS)
    board.paste(fitted, (x + (414 - fitted.width) // 2, 42))
    draw.text((x, 800), title + " - EXISTING COMPOSITE", font=font, fill="white")
    # Exact game viewport from the existing 940x1620 helper output.
    game = Image.open(preview).convert("RGB").crop((56, 116, 884, 1588))
    board.paste(game.resize((414, 736), Image.Resampling.LANCZOS), (x, 830))
board.save(ROUND / "review/C01-B-B2-D-comparison.png")
print("Saved", ROUND / "review/C01-B-B2-D-comparison.png")

