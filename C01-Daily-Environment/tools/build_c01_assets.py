#!/usr/bin/env python3
"""Build C01 technical guides and local-only review composites.

This tool does not generate or alter artistic candidates. It only builds masks,
a human reference board, a framed current-production control, and approximate
candidate + gameplay review composites from files already in this C01 package.
Requires Pillow, available in the local Python environment; no project dependency.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
MASKS = ROOT / "masks"
OVERLAYS = ROOT / "overlays"
CONTACT_SHEETS = ROOT / "contact-sheets"
REVIEW = ROOT / "review"
ROAD_LOGICAL = [(140.76, 117.76), (273.24, 117.76), (414, 736), (0, 736)]
HUD_LOGICAL_HEIGHT = 150
HORIZON_LOGICAL = (207, 117.76)


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def scaled_polygon(scale: int) -> list[tuple[float, float]]:
    return [(x * scale, y * scale) for x, y in ROAD_LOGICAL]


def label(draw: ImageDraw.ImageDraw, pos: tuple[int, int], text: str, size: int = 18) -> None:
    draw.text(pos, text, font=font(size, True), fill=(255, 255, 255, 255), stroke_width=2, stroke_fill=(9, 7, 20, 220))


def make_road_exclusion(scale: int) -> None:
    size = (414 * scale, 736 * scale)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    road = scaled_polygon(scale)
    draw.polygon(road, fill=(229, 72, 83, 92))
    draw.line(road + [road[0]], fill=(255, 93, 104, 235), width=3 * scale, joint="curve")
    hx, hy = HORIZON_LOGICAL[0] * scale, HORIZON_LOGICAL[1] * scale
    draw.ellipse((hx - 4 * scale, hy - 4 * scale, hx + 4 * scale, hy + 4 * scale), fill=(255, 248, 240, 240))
    if scale == 1:
        label(draw, (10, 705), "RED = PROTECTED ROAD / NO GENERATED DETAIL", 11)
    image.save(MASKS / f"c01-road-exclusion-{size[0]}x{size[1]}.png")


def make_hud_safe_zone(scale: int) -> None:
    size = (414 * scale, 736 * scale)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    hud_h = HUD_LOGICAL_HEIGHT * scale
    draw.rectangle((0, 0, size[0], hud_h), fill=(229, 72, 83, 82), outline=(255, 93, 104, 235), width=3 * scale)
    if scale == 1:
        label(draw, (10, 12), "HUD SAFE / LOW FREQUENCY", 13)
    image.save(MASKS / f"c01-hud-safe-zone-{size[0]}x{size[1]}.png")


def make_generation_guide(scale: int) -> None:
    size = (414 * scale, 736 * scale)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    road = scaled_polygon(scale)
    # Lateral world: detail allowed, intentionally outside the authoritative road.
    draw.rectangle((0, 0, size[0], size[1]), fill=(38, 173, 145, 40))
    # Center corridor: quiet, low contrast; red boundary identifies prohibited generated detail.
    draw.polygon(road, fill=(13, 17, 31, 132))
    draw.line(road + [road[0]], fill=(255, 93, 104, 245), width=3 * scale, joint="curve")
    # HUD zone on top of the side-detail color.
    draw.rectangle((0, 0, size[0], HUD_LOGICAL_HEIGHT * scale), fill=(229, 72, 83, 72), outline=(255, 93, 104, 215), width=2 * scale)
    hx, hy = HORIZON_LOGICAL[0] * scale, HORIZON_LOGICAL[1] * scale
    draw.line((hx - 13 * scale, hy, hx + 13 * scale, hy), fill=(255, 248, 240, 235), width=2 * scale)
    draw.line((hx, hy - 13 * scale, hx, hy + 13 * scale), fill=(255, 248, 240, 235), width=2 * scale)
    if scale == 1:
        label(draw, (10, 12), "RED: HUD SAFE", 12)
        label(draw, (9, 195), "GREEN: SIDE DETAIL ALLOWED", 11)
        label(draw, (111, 428), "QUIET GAMEPLAY CORRIDOR", 11)
        label(draw, (155, 132), "HORIZON", 10)
    image.save(OVERLAYS / f"c01-generation-guide-{size[0]}x{size[1]}.png")


def contain(image: Image.Image, box: tuple[int, int], background=(20, 15, 35, 255)) -> Image.Image:
    result = Image.new("RGBA", box, background)
    fitted = ImageOps.contain(image.convert("RGBA"), box, Image.Resampling.LANCZOS)
    result.alpha_composite(fitted, ((box[0] - fitted.width) // 2, (box[1] - fitted.height) // 2))
    return result


def make_reference_board() -> None:
    assets = [
        ("01  DAILY GAMEPLAY\nRUNTIME COMPOSITION", REFERENCES / "01-daily-gameplay-414x736.png"),
        ("02  CURRENT DAILY ENVIRONMENT\nPRODUCTION CONTROL", REFERENCES / "02-current-daily-background-828w.webp"),
        ("03  CHAIN BLOCK\nMATERIAL VOCABULARY", REFERENCES / "03-current-chain-block-128w.png"),
        ("04  HOME ENVIRONMENT\nWORLD IDENTITY", REFERENCES / "04-home-background-828w.webp"),
        ("05  GUIDED GAMEPLAY\nREADABILITY BASELINE", REFERENCES / "05-guided-gameplay-414x736.png"),
    ]
    canvas = Image.new("RGBA", (1900, 1280), (12, 8, 25, 255))
    draw = ImageDraw.Draw(canvas)
    draw.text((50, 35), "C01 — REFERENCE BOARD", font=font(38, True), fill=(255, 211, 110, 255))
    draw.text((50, 86), "Human review only · references define composition, material and readability", font=font(20), fill=(197, 190, 220, 255))
    cells = [(50, 145), (415, 145), (780, 145), (1145, 145), (1510, 145)]
    for (title, path), (x, y) in zip(assets, cells):
        image = Image.open(path).convert("RGBA")
        card = contain(image, (320, 880), (25, 19, 42, 255))
        canvas.alpha_composite(card, (x, y + 45))
        draw.rounded_rectangle((x - 2, y + 43, x + 322, y + 927), radius=8, outline=(121, 91, 212, 255), width=2)
        draw.multiline_text((x, y), title, font=font(15, True), fill=(255, 255, 255, 255), spacing=3)
    draw.text((50, 1110), "Central gameplay corridor remains quiet. Generated details belong primarily in lateral architecture and far depth.", font=font(20), fill=(170, 220, 210, 255))
    draw.text((50, 1150), "No image on this board is a production replacement or a prompt to reproduce UI, objects, logos or text.", font=font(20), fill=(197, 190, 220, 255))
    canvas.convert("RGB").save(CONTACT_SHEETS / "C01-reference-board.png")


def frame_preview(image: Image.Image, heading: str, subheading: str) -> Image.Image:
    game = contain(image, (828, 1472))
    frame = Image.new("RGBA", (940, 1620), (9, 6, 18, 255))
    draw = ImageDraw.Draw(frame)
    draw.text((56, 28), heading, font=font(29, True), fill=(255, 211, 110, 255))
    draw.text((56, 69), subheading, font=font(16), fill=(203, 196, 224, 255))
    frame.alpha_composite(game, (56, 116))
    draw.rectangle((55, 115, 884, 1588), outline=(130, 94, 220, 255), width=2)
    return frame


def make_current_control() -> None:
    runtime = Image.open(REFERENCES / "01-daily-gameplay-414x736.png")
    control = frame_preview(runtime, "CURRENT PRODUCTION CONTROL", "Actual Daily midrun capture: current production environment + current gameplay composition")
    control.convert("RGB").save(REVIEW / "C01-CURRENT-CONTROL.png")


def candidate_preview(candidate: Path, output: Path) -> None:
    if not candidate.exists():
        raise FileNotFoundError(f"Candidate not found: {candidate}")
    background = contain(Image.open(candidate), (828, 1472))
    runtime = Image.open(REFERENCES / "01-daily-gameplay-414x736.png").convert("RGBA").resize((828, 1472), Image.Resampling.LANCZOS)
    mask = Image.new("L", (828, 1472), 0)
    mask_draw = ImageDraw.Draw(mask)
    # Preserve current HUD sample and the actual road/object corridor as a fast review overlay.
    mask_draw.rectangle((0, 0, 828, 300), fill=255)
    mask_draw.polygon(scaled_polygon(2), fill=255)
    gameplay_overlay = Image.new("RGBA", (828, 1472), (0, 0, 0, 0))
    gameplay_overlay.paste(runtime, (0, 0), mask)
    background.alpha_composite(gameplay_overlay)
    composed = frame_preview(background, f"C01 REVIEW PREVIEW — {candidate.stem}", "Approximate local composite: candidate environment behind current HUD/road gameplay sample")
    output.parent.mkdir(parents=True, exist_ok=True)
    composed.convert("RGB").save(output)


def build() -> None:
    for folder in (MASKS, OVERLAYS, CONTACT_SHEETS, REVIEW):
        folder.mkdir(parents=True, exist_ok=True)
    for scale in (1, 2):
        make_road_exclusion(scale)
        make_hud_safe_zone(scale)
        make_generation_guide(scale)
    make_reference_board()
    make_current_control()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="build guides, reference board and current control")
    preview = sub.add_parser("preview", help="create a local candidate + gameplay review composite")
    preview.add_argument("candidate", type=Path)
    preview.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.command == "build":
        build()
    else:
        candidate_preview(args.candidate, args.output)


if __name__ == "__main__":
    main()
