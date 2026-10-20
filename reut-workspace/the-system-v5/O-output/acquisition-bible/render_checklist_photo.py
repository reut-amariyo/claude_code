#!/usr/bin/env python3
"""Acquisition checklist over a real Lior photo, 1080x1350 for the LinkedIn image slot.
Photo: ~/Desktop/brand/liors pic/0G1A0162 G.jpg (boardroom table, signing). Pure PIL, 3x supersampled."""
import os
from PIL import Image, ImageOps, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "../../T-tools/assets/fonts")
PHOTO = os.path.expanduser("~/Desktop/brand/liors pic/0G1A0162 G.jpg")
OUT = os.path.join(HERE, "acquisition-checklist-photo-1080x1350.png")

S = 3
W, H = 1080 * S, 1350 * S
GRAPHITE = (33, 36, 37); SAND = (194, 167, 119); MID = (120, 122, 122)
PANEL = (245, 243, 240, 236); WHITE = (255, 255, 255)

def font(name, px): return ImageFont.truetype(os.path.join(FONTS, name), px * S)
MONO_B = lambda p: font("JetBrainsMono-Bold.ttf", p)
MONO = lambda p: font("JetBrainsMono-Regular.ttf", p)
INTER = lambda p: font("Inter-Regular.ttf", p)
INTER_SB = lambda p: font("Inter-SemiBold.ttf", p)

RULES = [
    ("01", "People I trust", "Would we hire the founders?"),
    ("02", "Value we can add", "Can we name the fixes on day one?"),
    ("03", "A gap in our ecosystem", "Does it close a hole our customers feel?"),
    ("04", "Payback in 12 months", "Price ÷ monthly profit after fixes = 12 or less?"),
    ("05", "A product we know", "Was it on our roadmap anyway?"),
]

# photo: fill width, keep the top of the frame
ph = ImageOps.exif_transpose(Image.open(PHOTO)).convert("RGB")
scale = W / ph.width
ph = ph.resize((W, int(ph.height * scale)), Image.LANCZOS)
top = int(40 * S)
canvas = ph.crop((0, top, W, top + H)).convert("RGBA")

over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(over)

# title in the white haze above his head
x0 = 64 * S
d.text((x0, 58 * S), "THE ACQUISITION CHECKLIST", font=MONO_B(42), fill=GRAPHITE)
d.text((x0, 116 * S), "5 rules I run before buying a company", font=INTER(24), fill=(70, 72, 73))

# checklist panel on the table
px0, py0, px1, py1 = 48 * S, 640 * S, (1080 - 48) * S, 1268 * S
d.rectangle((px0, py0, px1, py1), fill=PANEL, outline=GRAPHITE, width=2 * S)
row_h = 100 * S
y = py0 + 24 * S
for i, (n, title, q) in enumerate(RULES):
    hi = n == "04"
    ry0, ry1 = y, y + row_h - 12 * S
    if hi:
        d.rectangle((px0 + 18 * S, ry0, px1 - 18 * S, ry1), fill=GRAPHITE)
    fg = WHITE if hi else GRAPHITE
    sub = (217, 214, 209) if hi else (74, 77, 78)
    d.text((px0 + 40 * S, ry0 + 18 * S), n, font=MONO_B(22), fill=SAND)
    d.text((px0 + 100 * S, ry0 + 14 * S), title, font=MONO_B(26), fill=fg)
    d.text((px0 + 100 * S, ry0 + 52 * S), q, font=INTER(21), fill=sub)
    bx = px1 - 72 * S; by = ry0 + 26 * S; b = 30 * S
    d.rectangle((bx, by, bx + b, by + b), outline=(WHITE if hi else GRAPHITE), width=3 * S)
    if not hi and i < len(RULES) - 1 and RULES[i + 1][0] != "04":
        d.line((px0 + 40 * S, ry1 + 6 * S, px1 - 40 * S, ry1 + 6 * S), fill=(214, 210, 203), width=S)
    y += row_h

# verdict line
d.text((px0 + 40 * S, py1 - 70 * S), "5 OF 5 · MAKE THE OFFER", font=MONO_B(22), fill=GRAPHITE)
vt = "ANY NO · WALK"
d.text((px1 - 40 * S - d.textlength(vt, font=MONO_B(22)), py1 - 70 * S), vt, font=MONO_B(22), fill=MID)

# footer
d.text((x0, 1296 * S), "[ life is beta ]", font=MONO(19), fill=GRAPHITE)
ft = "Lior Pozin"
d.text((W - x0 - d.textlength(ft, font=INTER_SB(20)), 1295 * S), ft, font=INTER_SB(20), fill=GRAPHITE)

out = Image.alpha_composite(canvas, over).convert("RGB").resize((1080, 1350), Image.LANCZOS)
out.save(OUT, optimize=True)
print(OUT)
