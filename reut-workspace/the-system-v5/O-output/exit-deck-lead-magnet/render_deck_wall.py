#!/usr/bin/env python3
"""Render a 'deck wall' promo graphic: every slide of a PDF as a thumbnail grid,
under a headline. Built for the exit-deck lead magnet, reusable for any deck.

Usage:
  python3 render_deck_wall.py                      # default: exit-deck-template-v2.pdf
  python3 render_deck_wall.py --pdf other.pdf --out wall.png --cols 6

Colors and type are sampled from the deck itself so the promo matches the asset.
"""
import argparse, io, math, os
import fitz
from PIL import Image, ImageDraw, ImageFont

GRAPHITE = (33, 36, 37)
OFFWHITE = (245, 243, 240)
SAND     = (194, 167, 119)
MIDGRAY  = (138, 140, 140)

MONO_BOLD = "/System/Library/Fonts/Menlo.ttc"      # index 1 = Bold
MONO_REG  = "/System/Library/Fonts/Menlo.ttc"      # index 0 = Regular


def font(size, bold=False):
    return ImageFont.truetype(MONO_BOLD, size, index=1 if bold else 0)


def tracked(draw, xy, text, f, fill, tracking=0, anchor_left=True):
    """Draw text with letter spacing. Returns total width."""
    x, y = xy
    if not anchor_left:
        w = sum(draw.textlength(c, font=f) + tracking for c in text) - tracking
        x -= w
    for c in text:
        draw.text((x, y), c, font=f, fill=fill)
        x += draw.textlength(c, font=f) + tracking
    return x - xy[0]


def build(pdf, out, cols, width, headline_a, headline_b, eyebrow, sub, footer_l, footer_r):
    doc = fitz.open(pdf)
    n = doc.page_count

    margin, gap = 64, 12
    cell_w = (width - 2 * margin - (cols - 1) * gap) // cols
    page_ratio = doc[0].rect.height / doc[0].rect.width
    cell_h = int(cell_w * page_ratio)
    rows = math.ceil(n / cols)

    head_h = 500
    foot_h = 130
    height = head_h + rows * cell_h + (rows - 1) * gap + foot_h

    canvas = Image.new("RGB", (width, height), GRAPHITE)
    d = ImageDraw.Draw(canvas)

    # ---- header
    y = 78
    tracked(d, (margin, y), eyebrow, font(20, True), SAND, tracking=6)
    y += 62
    f_h1 = font(104, True)
    d.text((margin, y), headline_a, font=f_h1, fill=OFFWHITE)
    y += 118
    d.text((margin, y), headline_b, font=f_h1, fill=SAND)
    y += 138
    f_sub = font(25)
    for line in sub:
        d.text((margin, y), line, font=f_sub, fill=MIDGRAY)
        y += 36

    # ---- grid
    top = head_h
    for i in range(n):
        r, c = divmod(i, cols)
        x = margin + c * (cell_w + gap)
        yy = top + r * (cell_h + gap)
        px = doc[i].get_pixmap(dpi=110)
        thumb = Image.open(io.BytesIO(px.tobytes("png"))).convert("RGB")
        thumb = thumb.resize((cell_w, cell_h), Image.LANCZOS)
        canvas.paste(thumb, (x, yy))
        d.rectangle([x, yy, x + cell_w - 1, yy + cell_h - 1], outline=(70, 72, 72))

    # ---- footer
    fy = height - foot_h + 42
    tracked(d, (margin, fy), footer_l, font(22), SAND, tracking=3)
    tracked(d, (width - margin, fy), footer_r, font(22), MIDGRAY, tracking=1,
            anchor_left=False)

    canvas.save(out)
    print(f"{out}  {canvas.size[0]}x{canvas.size[1]}  {n} slides")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=os.path.join(here, "exit-deck-template-v2.pdf"))
    ap.add_argument("--out", default=os.path.join(here, "deck-wall-1200.png"))
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--width", type=int, default=1200)
    ap.add_argument("--a", default="47 SLIDES")
    ap.add_argument("--b", default="ONE $92M EXIT")
    ap.add_argument("--eyebrow", default="THE EXIT DECK")
    ap.add_argument("--footer-left", default="[ life is beta ]")
    ap.add_argument("--footer-right", default="Lior Pozin  /  CEO & Co-Founder of AutoDS")
    args = ap.parse_args()

    build(args.pdf, args.out, args.cols, args.width, args.a, args.b, args.eyebrow,
          ["The presentation structure that sold AutoDS to Fiverr.",
           "9 sections. Fill in your numbers. Get buyer-ready."],
          args.footer_left, args.footer_right)
