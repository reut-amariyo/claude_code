#!/usr/bin/env python3
"""Hand-drawn founder-journey graph card for Lior's LinkedIn.

Marker-on-paper aesthetic on purpose: visual family = personal artifact /
signed illustration, never a marketing-team graphic. Red hand-circle marks
the detail the post hinges on (playbook Rule C).
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont

random.seed(11)

W, H = 1200, 1500
PAPER = (250, 248, 243)
INK = (26, 26, 26)
GHOST = (176, 172, 164)
RED = (204, 41, 41)

SUP = "/System/Library/Fonts/Supplemental/"
def font(name, size, idx=0):
    return ImageFont.truetype(SUP + name, size, index=idx)

f_title = font("Bradley Hand Bold.ttf", 74)
f_sub   = font("MarkerFelt.ttc", 34)
f_lbl   = font("MarkerFelt.ttc", 31)
f_num   = font("Bradley Hand Bold.ttf", 44)
f_note  = font("MarkerFelt.ttc", 30)
f_tag   = font("MarkerFelt.ttc", 27)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# paper grain
for _ in range(5200):
    x, y = random.randrange(W), random.randrange(H)
    v = random.randint(0, 14)
    d.point((x, y), fill=(PAPER[0]-v, PAPER[1]-v, PAPER[2]-v))

# plot frame
PX0, PY0, PX1, PY1 = 150, 470, 1060, 1210

def to_px(p):
    x, y = p
    return (PX0 + x * (PX1 - PX0), PY1 - y * (PY1 - PY0))

def jitter_line(pts, width, color, amp=2.2, passes=2):
    """Draw a polyline with a hand-drawn wobble, a couple of passes for marker feel."""
    for p in range(passes):
        off, prev = 0.0, None
        for (x, y) in pts:
            off += random.uniform(-amp, amp)
            off = max(-amp * 2.4, min(amp * 2.4, off)) * 0.86
            cur = (x + off + p * 0.7, y + off * 0.55 + p * 0.7)
            if prev:
                d.line([prev, cur], fill=color, width=width, joint="curve")
            prev = cur

def catmull(points, steps=26):
    pts = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(len(pts) - 3):
        p0, p1, p2, p3 = pts[i], pts[i+1], pts[i+2], pts[i+3]
        for s in range(steps):
            t = s / steps
            t2, t3 = t*t, t*t*t
            x = 0.5*((2*p1[0]) + (-p0[0]+p2[0])*t + (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2 + (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y = 0.5*((2*p1[1]) + (-p0[1]+p2[1])*t + (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2 + (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            out.append((x, y))
    out.append(points[-1])
    return out

# ---- title block
d.text((150, 150), "THE FOUNDER GRAPH", font=f_title, fill=INK)
d.text((152, 252), "what the deck promises  vs.  what actually happens", font=f_sub, fill=(90, 88, 84))
jitter_line([(150, 232), (150 + 640, 232)], 4, INK, amp=1.4, passes=1)

# ---- axes
jitter_line([(PX0, PY0 - 40), (PX0, PY1)], 5, INK, amp=1.3, passes=2)
jitter_line([(PX0, PY1), (PX1 + 40, PY1)], 5, INK, amp=1.3, passes=2)
d.text((PX0 - 118, PY0 - 40), "UP", font=f_lbl, fill=INK)
d.text((PX1 - 20, PY1 + 26), "TIME", font=f_lbl, fill=INK)

# ---- the pitch-deck line (dashed, ghost)
ghost = catmull([to_px(p) for p in [(0.03, 0.22), (0.5, 0.55), (0.97, 0.93)]], steps=18)
for i in range(0, len(ghost) - 6, 12):
    jitter_line(ghost[i:i+7], 4, GHOST, amp=1.0, passes=1)
d.text((PX0 + 470, PY0 + 92), "the pitch deck", font=f_note, fill=GHOST)

# ---- the real line
nodes = [(0.03, 0.26), (0.135, 0.34), (0.20, 0.10), (0.28, 0.20),
         (0.38, 0.56), (0.45, 0.44), (0.53, 0.04), (0.62, 0.26),
         (0.74, 0.80), (0.82, 0.64), (0.90, 0.86), (0.97, 0.99)]
curve = catmull([to_px(p) for p in nodes], steps=24)
jitter_line(curve, 8, INK, amp=2.0, passes=2)

# ---- numbered beats
beats = [
    (1, (0.03, 0.26), "START",            (16, -74)),
    (2, (0.20, 0.10), "NO",               (-18, 44)),
    (3, (0.38, 0.56), "BREAK THROUGH",    (-40, -84)),
    (4, (0.53, 0.04), "NO. AGAIN.\nBIGGER.", (30, 34)),
    (5, (0.74, 0.80), "SCALE",            (-30, -84)),
    (6, (0.97, 0.99), "NEXT PEAK",        (-150, -78)),
]
for n, p, label, off in beats:
    cx, cy = to_px(p)
    d.ellipse([cx-11, cy-11, cx+11, cy+11], fill=INK)
    tx, ty = cx + off[0], cy + off[1]
    d.text((tx, ty), f"{n}", font=f_num, fill=INK)
    d.text((tx + 34, ty + 9), label, font=f_lbl, fill=INK)

# ---- red hand-drawn circle on the lowest point (Rule C)
lx, ly = to_px((0.53, 0.04))
for pas in range(2):
    ring = []
    for a in range(0, 372, 6):
        r = math.radians(a + pas * 9)
        rx = 96 + random.uniform(-5, 5)
        ry = 68 + random.uniform(-5, 5)
        ring.append((lx + rx * math.cos(r), ly + ry * math.sin(r) - 4))
    jitter_line(ring, 6, RED, amp=1.4, passes=1)

note = "the lowest point decides"
note2 = "the next peak"
d.text((lx - 300, ly - 210), note, font=f_note, fill=RED)
d.text((lx - 300, ly - 172), note2, font=f_note, fill=RED)
jitter_line([(lx - 120, ly - 140), (lx - 66, ly - 82)], 4, RED, amp=1.2, passes=1)

# ---- footer lockup
jitter_line([(150, 1322), (1050, 1322)], 3, (196, 192, 184), amp=1.0, passes=1)
d.text((150, 1352), "[ life is beta ]", font=f_tag, fill=(120, 118, 112))

out = sys.argv[1] if len(sys.argv) > 1 else "founder-graph.png"
img.save(out, "PNG")
print(out)
