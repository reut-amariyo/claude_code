#!/usr/bin/env python3
"""
render_photo_card.py — Lior photo + headline cards.

The "Simon Squibb" layout rebuilt inside Lior's Visual Identity: one real photo
on top, one short uppercase headline below, one number or phrase carrying the
payoff. JetBrains Mono, graphite / off-white, the container block as the
highlight device, the [ life is beta ] lockup across the photo.

Usage:
    python3 render_photo_card.py spec.json
    python3 render_photo_card.py spec.json --out /path/to/card.png

Spec (one object, or a list of them):
{
  "photo":   "O-output/photo-cards/some-photo.jpg",   # required, a REAL photo
  "line1":   "WE STARTED WITH ZERO FUNDING",          # required, setup line
  "line2":   "IT ENDED IN A {{$92M}} EXIT",           # required, payoff line
                                                      # {{...}} marks the highlight
  "variant": "block",          # block | sand | plain   see VARIANTS
  "kicker":  "AUTODS · 2017",  # optional small label, top-left over the photo
  "byline":  "Lior Pozin",     # optional small line under the headline
  "size":    "portrait",       # portrait 1080x1350 | square 1080x1080
  "focus":   "50% 30%",        # where to anchor the photo crop, CSS-style
  "out":     "O-output/photo-cards/my-card.png"
}

VARIANTS
  block  off-white band, graphite headline, highlight sits inside an inverted
         graphite container block. Most on-brand: in the VI the container's job
         is exactly "highlight / focal point".
  sand   graphite band, off-white headline, highlight in warm sand. Highest
         contrast in a LinkedIn feed, closest in punch to the reference card.
  plain  off-white band, graphite headline, highlight in warm sand text only.

Rendered with PIL at 3x and downsampled, so edges stay clean. No browser.
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FONT_DIR = os.path.join(ROOT, "T-tools", "assets", "fonts")

SS = 3  # supersampling factor

SIZES = {"portrait": (1080, 1350), "square": (1080, 1080)}

# VI palette
GRAPHITE = (28, 28, 26)
OFF_WHITE = (242, 240, 236)
MED_GRAY = (138, 138, 133)
WARM_SAND = (214, 178, 124)
WHITE = (255, 255, 255)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


JB_XB = "JetBrainsMono-ExtraBold.ttf"
JB_B = "JetBrainsMono-Bold.ttf"
IN_SB = "Inter-SemiBold.ttf"


# ---------- text helpers (PIL has no letter-spacing, so we do it by hand) ----


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
    """'IT ENDED IN A {{$92M}} EXIT' -> [('IT ENDED IN A ', 0), ('$92M', 1), (' EXIT', 0)]"""
    if "{{" in line and "}}" in line:
        before, rest = line.split("{{", 1)
        hi, after = rest.split("}}", 1)
        return [(before, 0), (hi, 1), (after, 0)]
    return [(line, 0)]


def parse_focus(focus, default=(0.5, 0.4)):
    try:
        fx, fy = focus.replace("%", "").split()
        return float(fx) / 100.0, float(fy) / 100.0
    except Exception:
        return default


# ---------- photo ----------


def cover_crop(path, box_w, box_h, focus):
    if not os.path.isabs(path):
        path = os.path.join(ROOT, path)
    if not os.path.exists(path):
        sys.exit(f"photo not found: {path}")
    im = Image.open(path).convert("RGB")
    src_ratio = im.width / im.height
    box_ratio = box_w / box_h
    if src_ratio > box_ratio:  # source too wide, crop sides
        new_w = int(im.height * box_ratio)
        x = int((im.width - new_w) * focus[0])
        im = im.crop((x, 0, x + new_w, im.height))
    else:  # source too tall, crop top/bottom
        new_h = int(im.width / box_ratio)
        y = int((im.height - new_h) * focus[1])
        im = im.crop((0, y, im.width, y + new_h))
    return im.resize((box_w, box_h), Image.LANCZOS)


def bottom_scrim(img, height, strength=0.58):
    """Darken the bottom of the photo so the lockup stays readable."""
    w, h = img.size
    grad = Image.new("L", (1, height))
    for i in range(height):
        grad.putpixel((0, i), int(255 * strength * (i / (height - 1)) ** 1.6))
    grad = grad.resize((w, height), Image.BILINEAR)
    black = Image.new("RGB", (w, height), (0, 0, 0))
    region = img.crop((0, h - height, w, h))
    img.paste(Image.composite(black, region, grad), (0, h - height))
    return img


# ---------- headline block ----------


def fit_headline(draw, lines, max_w, max_h, start_size, min_size=26):
    """Shrink until both lines fit the band. Long headlines are the caller's
    problem to shorten, this only stops them overflowing."""
    size = start_size
    while size > min_size:
        fnt = font(JB_XB, size)
        tracking = -0.02 * size
        widest = 0
        for line in lines:
            w = sum(
                tracked_width(draw, seg, fnt, tracking) for seg, _ in split_highlight(line)
            )
            # highlight block padding
            if any(f for _, f in split_highlight(line)):
                w += 2 * 0.18 * size
            widest = max(widest, w)
        total_h = len(lines) * size * 1.16
        if widest <= max_w and total_h <= max_h:
            return size, fnt, tracking
        size -= 1
    fnt = font(JB_XB, min_size)
    return min_size, fnt, -0.02 * min_size


def render(spec, out_path):
    w1, h1 = SIZES[spec.get("size", "portrait")]
    w, h = w1 * SS, h1 * SS
    variant = spec.get("variant", "block")
    band_h = int(h * 0.29)
    photo_h = h - band_h
    pad = 56 * SS

    dark_band = variant == "sand"
    band_bg = GRAPHITE if dark_band else OFF_WHITE
    text_col = OFF_WHITE if dark_band else GRAPHITE

    card = Image.new("RGB", (w, h), band_bg)

    # --- photo ---
    photo = cover_crop(spec["photo"], w, photo_h, parse_focus(spec.get("focus", "50% 40%")))
    photo = bottom_scrim(photo, int(photo_h * 0.34))
    card.paste(photo, (0, 0))

    draw = ImageDraw.Draw(card)

    # --- kicker block, top left ---
    kicker = spec.get("kicker", "")
    if kicker:
        kf = font(JB_B, 20 * SS)
        ktr = 0.16 * 20 * SS
        kw = tracked_width(draw, kicker, kf, ktr)
        box_w = int(kw + 2 * 22 * SS)
        box_h = int(20 * SS + 2 * 14 * SS)
        draw.rectangle([0, 0, box_w, box_h], fill=GRAPHITE)
        bbox = kf.getbbox(kicker)
        ky = (box_h - (bbox[3] - bbox[1])) / 2 - bbox[1]
        draw_tracked(draw, 22 * SS, ky, kicker, kf, OFF_WHITE, ktr)

    # --- [ life is beta ] lockup across the photo bottom ---
    tag = "[ life is beta ]"
    tf = font(JB_B, 26 * SS)
    ttr = 0.10 * 26 * SS
    tw = tracked_width(draw, tag, tf, ttr)
    ty = photo_h - 44 * SS - 26 * SS
    tbbox = tf.getbbox(tag)
    center_y = ty + (tbbox[1] + tbbox[3]) / 2
    tx = (w - tw) / 2
    gap = 26 * SS
    rule = max(2 * SS // 2, 2)
    draw.rectangle(
        [pad, center_y - rule / 2, tx - gap, center_y + rule / 2], fill=(255, 255, 255, 255)
    )
    draw.rectangle(
        [tx + tw + gap, center_y - rule / 2, w - pad, center_y + rule / 2], fill=WHITE
    )
    draw_tracked(draw, tx, ty, tag, tf, WHITE, ttr)

    # --- headline band ---
    lines = [spec["line1"].upper(), spec["line2"].upper()]
    byline = spec.get("byline", "")
    byline_room = (21 * SS + 20 * SS) if byline else 0
    room_h = band_h - 2 * 46 * SS - byline_room
    size, hf, tr = fit_headline(draw, lines, w - 2 * pad, room_h, 58 * SS)

    line_h = size * 1.16
    block_h = len(lines) * line_h
    y = photo_h + (band_h - block_h - byline_room) / 2

    cap = hf.getbbox("AZ$0")  # cap-height reference for the highlight block

    for line in lines:
        x = pad
        segs = split_highlight(line)
        for seg, is_hi in segs:
            if not seg:
                continue
            if is_hi and variant == "block":
                sw = tracked_width(draw, seg, hf, tr)
                bx = 0.18 * size
                draw.rectangle(
                    [
                        x,
                        y + cap[1] - 0.13 * size,
                        x + sw + 2 * bx,
                        y + cap[3] + 0.13 * size,
                    ],
                    fill=GRAPHITE,
                )
                draw_tracked(draw, x + bx, y, seg, hf, OFF_WHITE, tr)
                x += sw + 2 * bx
            else:
                col = WARM_SAND if is_hi else text_col
                x = draw_tracked(draw, x, y, seg, hf, col, tr) - tr
        y += line_h

    if byline:
        bf = font(IN_SB, 21 * SS)
        draw.text(
            (pad, y + 14 * SS),
            byline,
            font=bf,
            fill=MED_GRAY if not dark_band else (150, 150, 145),
        )

    card = card.resize((w1, h1), Image.LANCZOS)
    if not os.path.isabs(out_path):
        out_path = os.path.join(ROOT, out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    card.save(out_path, quality=95)
    return out_path


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1]) as f:
        data = json.load(f)
    specs = data if isinstance(data, list) else [data]

    out_override = None
    if "--out" in sys.argv:
        out_override = sys.argv[sys.argv.index("--out") + 1]

    for i, spec in enumerate(specs):
        out = out_override or spec.get("out", f"O-output/photo-cards/card-{i + 1}.png")
        print(render(spec, out))


if __name__ == "__main__":
    main()
