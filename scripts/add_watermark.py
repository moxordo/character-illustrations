#!/usr/bin/env python3
"""Add an exact-text watermark to a PNG/JPEG/WebP illustration (bottom-right quiet margin).

The watermark text comes from the active character profile's `watermark` frontmatter.
Requires Pillow. Adapted from aishwaryaashok14/peanut-illustrations (MIT).
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf",
        "/System/Library/Fonts/MarkerFelt.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def load_symbol_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """A clean font for the © glyph (hand fonts render it as a tiny superscript)."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser(description="Add an exact-text watermark to an image.")
    parser.add_argument("--input", required=True, help="Source image path")
    parser.add_argument("--out", required=True, help="Output image path")
    parser.add_argument("--text", required=True, help="Exact watermark text")
    parser.add_argument(
        "--scale",
        type=float,
        default=0.016,
        help="Font size as a fraction of image width (default: 0.016)",
    )
    parser.add_argument(
        "--opacity",
        type=int,
        default=210,
        help="Watermark opacity, 0-255 (default: 210)",
    )
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGBA")
    width, height = image.size

    font_size = max(28, round(width * args.scale))
    text_font = load_font(font_size)
    symbol_font = load_symbol_font(font_size)
    draw = ImageDraw.Draw(image)

    # Hand fonts render "©" as a tiny superscript, so draw a leading symbol in a
    # clean font and the rest in the hand font, sharing one baseline.
    if " " in args.text:
        symbol, rest = args.text.split(" ", 1)
    else:
        symbol, rest = args.text, ""
    gap = round(font_size * 0.2) if rest else 0
    symbol_w = draw.textlength(symbol, font=symbol_font)
    rest_w = draw.textlength(rest, font=text_font) if rest else 0
    total_w = symbol_w + gap + rest_w

    margin_x = round(width * 0.035)
    margin_y = round(height * 0.05)
    x = width - margin_x - total_w
    baseline_y = height - margin_y

    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    fill = (0, 0, 0, args.opacity)
    overlay_draw.text((x, baseline_y), symbol, font=symbol_font, fill=fill, anchor="ls")
    if rest:
        overlay_draw.text(
            (x + symbol_w + gap, baseline_y), rest, font=text_font, fill=fill, anchor="ls"
        )

    result = Image.alpha_composite(image, overlay)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    result.save(out)


if __name__ == "__main__":
    main()
