#!/usr/bin/env python3
"""ACTION PATTERN graph, faithful rebuild of Lior's original asset.

Renders at 2x and downsamples with Lanczos, so edges are genuinely sharp
rather than upscaled. Default output: LinkedIn portrait 1200x1500.
Usage: render_action_pattern_card.py OUT.png [W] [H]
"""
import sys, math
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else "action-pattern.png"
FW  = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
FH  = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
S   = 2                                   # supersample factor

W, H  = FW * S, FH * S
BG    = (19, 19, 19)
WHITE = (245, 245, 243)
TITLE = (138, 138, 133)
GRAY  = (150, 150, 145)
LINE  = (154, 154, 149)
DOTTD = (110, 110, 105)
TAN   = (199, 154, 107)
TANRG = (107, 79, 51)
DOTRG = (90, 90, 88)
BOXBG = (154, 154, 149)

MONO = "/System/Library/Fonts/Menlo.ttc"
def fnt(size, bold=False):
    return ImageFont.truetype(MONO, int(size * S), index=1 if bold else 0)

f_title = fnt(58)
f_hdr   = fnt(19, bold=True)
f_lbl   = fnt(20, bold=True)
f_sub   = fnt(19)
f_box   = fnt(19)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def P(x, y):  return (x * S, y * S)

def track(x, y, text, font, fill, sp=3, align="left"):
    sp *= S
    wsum = sum(d.textlength(c, font=font) + sp for c in text) - sp
    x *= S; y *= S
    if align == "right":  x -= wsum
    if align == "center": x -= wsum / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + sp
    return wsum / S

def arrow(p1, p2, color=LINE, w=2, head=10):
    p1, p2 = P(*p1), P(*p2)
    w, head = w * S, head * S
    d.line([p1, p2], fill=color, width=w)
    a = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    for s in (0.5, -0.5):
        d.line([p2, (p2[0]-head*math.cos(a+s), p2[1]-head*math.sin(a+s))], fill=color, width=w)

def dashed_climb(p1, p2, n=4, gap=0.30):
    """Run of small arrows along a segment - the original's climb style."""
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    L = math.hypot(dx, dy); ux, uy = dx/L, dy/L
    step = L / n
    for i in range(n):
        s0 = i*step + step*gap*0.5
        s1 = (i+1)*step - step*gap
        arrow((p1[0]+ux*s0, p1[1]+uy*s0), (p1[0]+ux*s1, p1[1]+uy*s1), LINE, 2, 8)

def dotted_v(x, y0, y1, color=DOTTD):
    y = y0
    while y < y1:
        d.line([P(x, y), P(x, min(y+4, y1))], fill=color, width=1*S)
        y += 9

def dotted_h(y, x0, x1, color=DOTTD):
    x = x0
    while x < x1:
        d.line([P(x, y), P(min(x+4, x1), y)], fill=color, width=1*S)
        x += 9

def node(p, tan=False, r=10):
    cx, cy = P(*p); r *= S
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=TANRG if tan else DOTRG)
    ir = r * 0.45
    d.ellipse([cx-ir, cy-ir, cx+ir, cy+ir], fill=TAN if tan else WHITE)

# ---------- header
track(60, 44, "STRATEGY", f_hdr, TITLE, sp=4)
track(FW-60, 44, "LIOR POZIN", f_hdr, TITLE, sp=4, align="right")

# ---------- title
track(58, 128, "ACTION",  f_title, TITLE, sp=8)
track(58, 200, "PATTERN", f_title, TITLE, sp=8)

# ---------- geometry
RUN0  = (215, 960)
RUN1  = (380, 960)
NO1   = (430, 1090)
BRK   = (560, 830)
PEAK  = (700, 600)
NO2   = (770, 900)
SCALE = (880, 480)
ENDA  = (1000, 440)

# path
for i in range(3):
    x0 = RUN0[0] + i * 58
    arrow((x0, 960), (x0 + 40, 960), LINE, 2, 8)
arrow(RUN1, (NO1[0]-8, NO1[1]-14))
arrow((NO1[0]+10, NO1[1]-16), (BRK[0]-8, BRK[1]+14))
dashed_climb(BRK, PEAK, n=3)
arrow((PEAK[0]+10, PEAK[1]+12), (NO2[0]-8, NO2[1]-16))
dashed_climb(NO2, SCALE, n=4)
arrow((SCALE[0]+18, SCALE[1]-6), ENDA)

# nodes
node(NO1, tan=True); node(BRK); node(PEAK); node(NO2, tan=True); node(SCALE)

# ---------- labels with dotted leaders
track(60, 922,  "JUST",  f_lbl, WHITE, sp=3)
track(60, 954,  "START", f_lbl, WHITE, sp=3)
for i, t in enumerate(["IDEA", "BUILD", "SELL"]):
    track(60, 994 + i*28, t, f_sub, GRAY, sp=3)

dotted_v(NO1[0], NO1[1]+16, 1147, TANRG)
track(NO1[0], 1155, "THE NO!", f_lbl, TAN, sp=3, align="center")

dotted_v(BRK[0], 722, BRK[1]-14)
track(505, 684, "BREAK THROUGH", f_lbl, WHITE, sp=3, align="center")

dotted_v(NO2[0], NO2[1]+16, 956, TANRG)
track(NO2[0], 964, "THE NO!", f_lbl, TAN, sp=3, align="center")

dotted_v(SCALE[0], 420, SCALE[1]-14)
track(960, 384, "AGGRESSIVE SCALE", f_lbl, WHITE, sp=3, align="right")

track(FW-60, 410, "WHAT'S", f_lbl, WHITE, sp=3, align="right")
track(FW-60, 442, "NEXT",   f_lbl, WHITE, sp=3, align="right")
track(FW-60, 486, "NEW GAME",  f_sub, GRAY, sp=3, align="right")
track(FW-60, 514, "NEXT PEAK", f_sub, GRAY, sp=3, align="right")

# ---------- baseline + box
BY = 1268
dotted_h(BY, 62, FW-62)
d.ellipse([P(60, BY)[0]-3*S, P(60, BY)[1]-3*S, P(60, BY)[0]+3*S, P(60, BY)[1]+3*S], fill=DOTTD)
arrow((FW-78, BY), (FW-60, BY), DOTTD, 1, 7)

box_t = "THE UNKNOWN TERRITORY"
bw = sum(d.textlength(c, font=f_box) + 3*S for c in box_t) - 3*S
bw /= S
bx0, by0 = FW/2 - bw/2 - 24, BY + 34
d.rectangle([P(bx0, by0), P(bx0 + bw + 48, by0 + 44)], fill=BOXBG)
track(FW/2, by0 + 12, box_t, f_box, (26, 26, 26), sp=3, align="center")

img.resize((FW, FH), Image.LANCZOS).save(OUT, "PNG")
print(OUT, f"{FW}x{FH}")
