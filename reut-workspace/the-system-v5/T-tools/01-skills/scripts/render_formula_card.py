#!/usr/bin/env python3
"""
render_formula_card.py — ONE formula, big, in Lior's VI. No photo needed.

The LinkedIn visual rule is "one artifact or one number, never the post as a
diagram". This card is the artifact: the formula the post is about, stacked one
term per line, the key number highlighted in warm sand, [ life is beta ] lockup
with hairlines at the bottom. Same palette, fonts and lockup as
render_photo_card.py, rendered with PIL at 3x.

Usage:
    python3 render_formula_card.py spec.json

Spec (one object or a list):
{
  "kicker": "FOUNDER SALARY · THE MATH",     # small label, top-left
  "lines":  ["CASH IN THE BANK",
             "{{÷ 18}}",                        # {{...}} = warm sand highlight
             "− MONTHLY TEAM COST",
             "= YOUR SALARY CEILING"],
  "variant": "dark",                          # dark (graphite) | light (off-white)
  "size":    "portrait",                      # portrait 1080x1350 | square 1080x1080
  "out":     "O-output/.../card.png"
}
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FONT_DIR = os.path.join(ROOT, "T-tools", "assets", "fonts")

SS = 3
SIZES = {"portrait": (1080, 1350), "square": (1080, 1080)}

GRAPHITE = (28, 28, 26)
OFF_WHITE = (242, 240, 236)
MED_GRAY = (138, 138, 133)
WARM_SAND = (214, 178, 124)

JB_XB = "JetBrainsMono-ExtraBold.ttf"
JB_B = "JetBrainsMono-Bold.ttf"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def tracked_width(draw, text, fnt, tracking):
    if not text:
        return 0
    return sum(draw.textlength(c, font=fnt) for c in text) + tracking * (len(text) - 1)


def draw_tracked(draw, x, y, text, fnt, fill, tracking):
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + tracking
    return x


def split_highlight(line):
    if "{{" in line and "}}" in line:
        before, rest = line.split("{{", 1)
        hi, after = rest.split("}}", 1)
        return [(before, 0), (hi, 1), (after, 0)]
    return [(line, 0)]


def render(spec, out_path):
    w, h = SIZES.get(spec.get("size", "portrait"), SIZES["portrait"])
    w, h = w * SS, h * SS
    dark = spec.get("variant", "dark") == "dark"
    bg = GRAPHITE if dark else OFF_WHITE
    fg = OFF_WHITE if dark else GRAPHITE
    pad = 72 * SS

    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    # kicker, top-left
    kicker = spec.get("kicker", "")
    if kicker:
        kf = font(JB_B, 24 * SS)
        draw_tracked(draw, pad, pad, kicker.upper(), kf, MED_GRAY, 0.14 * 24 * SS)

    # formula lines, fit to width
    lines = [l.upper() for l in spec["lines"]]
    plain = [l.replace("{{", "").replace("}}", "") for l in lines]
    size = 112 * SS
    while size > 30 * SS:
        hf = font(JB_XB, size)
        tr = 0.02 * size
        if max(tracked_width(draw, l, hf, tr) for l in plain) <= w - 2 * pad:
            break
        size -= 2 * SS
    hf = font(JB_XB, size)
    tr = 0.02 * size
    line_h = size * 1.28
    # highlighted line gets a larger size
    big = font(JB_XB, int(size * 1.6))
    big_tr = 0.02 * size * 1.6

    heights = []
    for l in lines:
        segs = split_highlight(l)
        heights.append(line_h * (1.8 if (len(segs) == 3 and segs[0][0].strip() == "" and segs[2][0].strip() == "") else 1))
    block_h = sum(heights)
    y = (h - block_h) / 2 + 20 * SS

    for l, lh in zip(lines, heights):
        segs = split_highlight(l)
        solo_hi = len(segs) == 3 and segs[0][0].strip() == "" and segs[2][0].strip() == ""
        x = pad
        for seg, is_hi in segs:
            if not seg:
                continue
            f = big if (is_hi and solo_hi) else hf
            t = big_tr if (is_hi and solo_hi) else tr
            col = WARM_SAND if is_hi else fg
            x = draw_tracked(draw, x, y, seg, f, col, t)
        y += lh

    # [ life is beta ] lockup with hairlines, bottom
    tag = "[ life is beta ]"
    tf = font(JB_B, 26 * SS)
    ttr = 0.10 * 26 * SS
    tw = tracked_width(draw, tag, tf, ttr)
    ty = h - pad - 26 * SS
    tb = tf.getbbox(tag)
    cy = ty + (tb[1] + tb[3]) / 2
    tx = (w - tw) / 2
    gap = 26 * SS
    rule = 2
    draw.rectangle([pad, cy - rule, tx - gap, cy + rule], fill=fg)
    draw.rectangle([tx + tw + gap, cy - rule, w - pad, cy + rule], fill=fg)
    draw_tracked(draw, tx, ty, tag, tf, fg, ttr)

    out = img.resize((w // SS, h // SS), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    out.save(out_path, "PNG")
    print(out_path)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: render_formula_card.py spec.json")
    with open(sys.argv[1]) as f:
        spec = json.load(f)
    specs = spec if isinstance(spec, list) else [spec]
    for s in specs:
        render(s, os.path.join(ROOT, s["out"]) if not os.path.isabs(s["out"]) else s["out"])


if __name__ == "__main__":
    main()
