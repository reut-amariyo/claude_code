#!/usr/bin/env python3
"""Cover-led variant of the deck wall: the real cover slide at full width,
then the remaining slides as a thumbnail grid underneath."""
import io, math, os, sys
import fitz
from PIL import Image, ImageDraw, ImageFont

GRAPHITE=(33,36,37); OFFWHITE=(245,243,240); SAND=(194,167,119); MIDGRAY=(138,140,140)
MONO="/System/Library/Fonts/Menlo.ttc"
here=os.path.dirname(os.path.abspath(__file__))
PDF=os.path.join(here,"exit-deck-template-v2.pdf")
OUT=os.path.join(here,"deck-wall-cover-1200.png")

def f(size,bold=False): return ImageFont.truetype(MONO,size,index=1 if bold else 0)
def tracked(d,xy,t,ft,fill,tr=0,left=True):
    x,y=xy
    if not left:
        w=sum(d.textlength(c,font=ft)+tr for c in t)-tr; x-=w
    for c in t:
        d.text((x,y),c,font=ft,fill=fill); x+=d.textlength(c,font=ft)+tr

doc=fitz.open(PDF); n=doc.page_count
W=1200; margin=64; gap=10; cols=7
cover_w=W-2*margin
cover_h=int(cover_w*doc[0].rect.height/doc[0].rect.width)
cell_w=(W-2*margin-(cols-1)*gap)//cols
cell_h=int(cell_w*doc[0].rect.height/doc[0].rect.width)
rows=math.ceil((n-1)/cols)
top_pad=56; label_h=86; foot_h=64
H=top_pad+cover_h+label_h+rows*cell_h+(rows-1)*gap+foot_h

canvas=Image.new("RGB",(W,H),GRAPHITE); d=ImageDraw.Draw(canvas)
px=doc[0].get_pixmap(dpi=150)
cov=Image.open(io.BytesIO(px.tobytes("png"))).convert("RGB").resize((cover_w,cover_h),Image.LANCZOS)
canvas.paste(cov,(margin,top_pad))
d.rectangle([margin,top_pad,margin+cover_w-1,top_pad+cover_h-1],outline=(70,72,72))

y=top_pad+cover_h+30
tracked(d,(margin,y),"+ 46 MORE SLIDES",f(24,True),SAND,tr=4)
tracked(d,(W-margin,y),"9 SECTIONS  /  FILL IN YOUR NUMBERS",f(22),MIDGRAY,tr=2,left=False)

top=top_pad+cover_h+label_h
for i in range(1,n):
    r,c=divmod(i-1,cols)
    x=margin+c*(cell_w+gap); yy=top+r*(cell_h+gap)
    p=doc[i].get_pixmap(dpi=90)
    th=Image.open(io.BytesIO(p.tobytes("png"))).convert("RGB").resize((cell_w,cell_h),Image.LANCZOS)
    canvas.paste(th,(x,yy))
    d.rectangle([x,yy,x+cell_w-1,yy+cell_h-1],outline=(70,72,72))

# no footer here: the cover slide already carries the lockup and the byline
canvas.save(OUT); print(OUT,canvas.size)
