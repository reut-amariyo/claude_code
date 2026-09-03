#!/usr/bin/env python3
"""Render an X-post-style quote card for LinkedIn (1200x1500, 4:5).

Avatar and verified badge are lifted from the existing card art so every card in
the series stays visually identical. Body text comes from a file or stdin: blank
lines become paragraph gaps, a leading '**' marks a bold line.

    python3 render_tweet_card.py body.txt out.png
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SOURCE_CARD = os.path.join(ROOT, "O-output", "lior-linkedin-ai-timeline-tweet-card-2026-08-10.png")
AVATAR_BOX = (80, 129, 248, 297)
BADGE_BOX = (535, 159, 578, 203)

W, H, SS = 1200, 1500, 2
MARGIN = 100
INK = (15, 20, 25)
GRAY = (110, 118, 125)

HELV = "/System/Library/Fonts/Helvetica.ttc"


def font(size, bold=False):
    return ImageFont.truetype(HELV, size, index=1 if bold else 0)


def lift(box, size):
    """Crop a circular/loose asset from the source card and scale it."""
    im = Image.open(SOURCE_CARD).convert("RGBA").crop(box)
    return im.resize((size, size), Image.LANCZOS)


def circle_avatar(size):
    av = lift(AVATAR_BOX, size)
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    av.putalpha(mask.resize((size, size), Image.LANCZOS))
    return av


def parse(raw):
    out = []
    for line in raw.rstrip("\n").split("\n"):
        s = line.strip()
        if not s:
            out.append(("", False))
        elif s.startswith("**"):
            out.append((s[2:].strip(), True))
        else:
            out.append((s, False))
    return out


def fit_size(lines, width, ceiling=62):
    for size in range(ceiling, 20, -1):
        f, fb = font(size * SS), font(size * SS, True)
        if all((fb if b else f).getlength(t) <= width * SS for t, b in lines if t):
            return size
    return 20


def render(lines, path):
    img = Image.new("RGB", (W * SS, H * SS), "white")
    d = ImageDraw.Draw(img)

    av = 168 * SS
    img.paste(circle_avatar(av), (MARGIN * SS, 138 * SS), circle_avatar(av))

    name_x = (MARGIN + 168 + 40) * SS
    fname = font(56 * SS, True)
    d.text((name_x, 158 * SS), "Lior Pozin", font=fname, fill=INK)

    badge = lift(BADGE_BOX, 46 * SS)
    bx = name_x + int(fname.getlength("Lior Pozin")) + 18 * SS
    img.paste(badge, (bx, 166 * SS), badge)

    d.text((name_x, 236 * SS), "@lior_pozin", font=font(50 * SS), fill=GRAY)

    size = fit_size(lines, W - MARGIN * 2)
    step, gap = int(size * 1.5), int(size * 0.75)

    # Centre the body block in the space under the header so short cards don't
    # sit high with a dead bottom third.
    block = sum(gap if not t else step for t, _ in lines) - (step - size)
    top, bottom = 430, H - 120
    y = max(top, top + (bottom - top - block) // 2) * SS
    for text, bold in lines:
        if not text:
            y += gap * SS
            continue
        d.text((MARGIN * SS, y), text, font=font(size * SS, bold), fill=INK)
        y += step * SS

    img.resize((W, H), Image.LANCZOS).save(path)
    print(f"{path}  body {size}px")


if __name__ == "__main__":
    src = sys.argv[1]
    raw = sys.stdin.read() if src == "-" else open(src).read()
    render(parse(raw), sys.argv[2])
