#!/usr/bin/env python3
"""
render_note_card.py — a real Lior photo with a phone-note pasted on top.

Reference: the "Reminder to self:" Notes-app card over a photo. Rebuilt in the
VI: off-white note, warm sand title and highlight, Inter for the note body so
it reads as a real note, [ life is beta ] lockup with hairlines at the bottom
of the photo. Personal-artifact family, so the photo must be a candid Lior
moment, never a studio portrait.

Usage:
    python3 render_note_card.py spec.json

Spec (one object or a list):
{
  "photo":  "O-output/.../lior-laptop.jpg",      # required, a REAL photo
  "title":  "Founder salary, the math:",          # note title, warm sand
  "lines":  ["Cash in the bank ÷ 18",
             "minus monthly team cost",
             "= your salary ceiling"],            # note body, highlighted
  "focus":  "50% 40%",                            # photo crop anchor
  "size":   "portrait",                           # portrait 1080x1350 | square 1080x1080
  "note_y": 56,                                   # note top margin, px at 1x
  "out":    "O-output/.../card.png"
}
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_photo_card import (  # noqa: E402
    ROOT, FONT_DIR, SS, SIZES, GRAPHITE, OFF_WHITE, MED_GRAY, WARM_SAND, WHITE,
    JB_B, font, tracked_width, draw_tracked, parse_focus, cover_crop, bottom_scrim,
)

IN_R = "Inter-Regular.ttf"
IN_SB = "Inter-SemiBold.ttf"
IN_B = "Inter-Bold.ttf"
NOTE_BG = (247, 245, 241)
HILITE = (214, 178, 124, 92)  # warm sand at ~36%


def render(spec, out_path):
    w, h = SIZES.get(spec.get("size", "portrait"), SIZES["portrait"])
    w, h = w * SS, h * SS

    img = cover_crop(spec["photo"], w, h, parse_focus(spec.get("focus", "50% 40%")))
    img = bottom_scrim(img, int(h * 0.22), 0.62).convert("RGBA")

    # ---------- the note ----------
    margin = 40 * SS
    note_x0 = margin
    note_w = w - 2 * margin
    note_y0 = int(spec.get("note_y", 56)) * SS
    pad = 34 * SS

    title = spec.get("title", "")
    lines = spec["lines"]
    tf = font(IN_B, 36 * SS)
    bf = font(IN_R, 42 * SS)
    body_lh = int(42 * SS * 1.42)

    # shrink body if a line is too wide
    while max(bf.getlength(l) for l in lines) > note_w - 2 * pad - 12 * SS and bf.size > 22 * SS:
        bf = font(IN_R, bf.size - SS)
        body_lh = int(bf.size * 1.42)

    header_h = 34 * SS + 30 * SS
    note_h = pad + header_h + len(lines) * body_lh + pad - 6 * SS

    # shadow
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(
        [note_x0, note_y0 + 10 * SS, note_x0 + note_w, note_y0 + note_h + 10 * SS],
        radius=22 * SS, fill=(0, 0, 0, 110),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(24 * SS))
    img = Image.alpha_composite(img, shadow)

    note = Image.new("RGBA", img.size, (0, 0, 0, 0))
    nd = ImageDraw.Draw(note)
    nd.rounded_rectangle(
        [note_x0, note_y0, note_x0 + note_w, note_y0 + note_h], radius=22 * SS, fill=NOTE_BG + (255,)
    )

    # header: chevron + title + share / more glyphs
    hx = note_x0 + pad
    hy = note_y0 + pad
    chev = font(IN_R, 36 * SS)
    nd.text((hx, hy - 4 * SS), "‹", font=chev, fill=WARM_SAND)
    nd.text((hx + 30 * SS, hy), title, font=tf, fill=WARM_SAND)
    # "more" glyph: three dots in a ring
    r = 17 * SS
    cx = note_x0 + note_w - pad - r
    cy = hy + 17 * SS
    nd.ellipse([cx - r, cy - r, cx + r, cy + r], outline=WARM_SAND, width=2 * SS)
    for dx in (-8, 0, 8):
        nd.ellipse([cx + dx * SS - 2 * SS, cy - 2 * SS, cx + dx * SS + 2 * SS, cy + 2 * SS], fill=WARM_SAND)
    # "share" glyph: box with an arrow
    sx = cx - r - 34 * SS - 14 * SS
    nd.rectangle([sx - 12 * SS, cy - 6 * SS, sx + 12 * SS, cy + 15 * SS], outline=WARM_SAND, width=2 * SS)
    nd.line([sx, cy - 16 * SS, sx, cy + 4 * SS], fill=WARM_SAND, width=2 * SS)
    nd.line([sx - 7 * SS, cy - 9 * SS, sx, cy - 16 * SS, sx + 7 * SS, cy - 9 * SS], fill=WARM_SAND, width=2 * SS)

    # body with highlight
    by = note_y0 + pad + header_h
    hl = Image.new("RGBA", img.size, (0, 0, 0, 0))
    hd = ImageDraw.Draw(hl)
    for i, l in enumerate(lines):
        y = by + i * body_lh
        tw = bf.getlength(l)
        hd.rectangle([hx - 6 * SS, y - 2 * SS, hx + tw + 6 * SS, y + bf.size + 8 * SS], fill=HILITE)
    # selection handles, first and last line
    handle_col = WARM_SAND + (255,)
    y0 = by - 2 * SS
    y1 = by + (len(lines) - 1) * body_lh + bf.size + 8 * SS
    hd.line([hx - 7 * SS, y0, hx - 7 * SS, y0 + bf.size + 10 * SS], fill=handle_col, width=3 * SS)
    hd.ellipse([hx - 7 * SS - 7 * SS, y0 - 14 * SS, hx - 7 * SS + 7 * SS, y0], fill=handle_col)
    xr = hx + bf.getlength(lines[-1]) + 7 * SS
    hd.line([xr, y1 - bf.size - 10 * SS, xr, y1], fill=handle_col, width=3 * SS)
    hd.ellipse([xr - 7 * SS, y1, xr + 7 * SS, y1 + 14 * SS], fill=handle_col)
    note = Image.alpha_composite(note, hl)
    nd = ImageDraw.Draw(note)
    for i, l in enumerate(lines):
        nd.text((hx, by + i * body_lh), l, font=bf, fill=GRAPHITE)

    img = Image.alpha_composite(img, note)

    # ---------- lockup ----------
    draw = ImageDraw.Draw(img)
    tag = "[ life is beta ]"
    lf = font(JB_B, 26 * SS)
    ttr = 0.10 * 26 * SS
    tw = tracked_width(draw, tag, lf, ttr)
    ty = h - 44 * SS - 26 * SS
    tb = lf.getbbox(tag)
    cy = ty + (tb[1] + tb[3]) / 2
    tx = (w - tw) / 2
    gap = 26 * SS
    draw.rectangle([margin, cy - 1, tx - gap, cy + 1], fill=WHITE)
    draw.rectangle([tx + tw + gap, cy - 1, w - margin, cy + 1], fill=WHITE)
    draw_tracked(draw, tx, ty, tag, lf, WHITE, ttr)

    out = img.convert("RGB").resize((w // SS, h // SS), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    out.save(out_path, "PNG")
    print(out_path)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: render_note_card.py spec.json")
    with open(sys.argv[1]) as f:
        spec = json.load(f)
    for s in (spec if isinstance(spec, list) else [spec]):
        out = s["out"] if os.path.isabs(s["out"]) else os.path.join(ROOT, s["out"])
        render(s, out)


if __name__ == "__main__":
    main()
