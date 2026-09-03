#!/usr/bin/env python3
"""Turn the 16:9 exit-deck template into a 4:5 portrait LinkedIn document post.

Portrait pages take roughly twice the feed height of a 16:9 document, and page 1
becomes a hook page instead of the quiet cover. Output: a PDF ready to upload as
a LinkedIn document.
"""
import io, os
import fitz
from PIL import Image, ImageDraw, ImageFont

GRAPHITE=(33,36,37); OFFWHITE=(245,243,240); SAND=(194,167,119); MIDGRAY=(140,142,142)
MONO="/System/Library/Fonts/Menlo.ttc"
W,H = 1080,1350
here=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(here,"exit-deck-template-v2.pdf")
import sys
SHORT = "--short" in sys.argv
OUT=os.path.join(here,"exit-deck-carousel-short.pdf" if SHORT else "exit-deck-linkedin-carousel.pdf")
PREVIEW=os.path.join(here,"carousel-page1.png")
# spine slide + the 9 section dividers + the closing slide
SHORT_PAGES=[2,4,12,16,23,26,29,35,38,41,46]

def f(s,b=False): return ImageFont.truetype(MONO,s,index=1 if b else 0)

def tracked(d,xy,t,ft,fill,tr=0,left=True):
    x,y=xy
    if not left:
        x-=sum(d.textlength(c,font=ft)+tr for c in t)-tr
    for c in t:
        d.text((x,y),c,font=ft,fill=fill); x+=d.textlength(c,font=ft)+tr

def base():
    im=Image.new("RGB",(W,H),GRAPHITE)
    return im, ImageDraw.Draw(im)

def hook_page():
    im,d=base()
    d.rectangle([80,150,148,218],outline=SAND,width=3)          # the container motif
    y=300
    tracked(d,(80,y),"THE EXIT DECK",f(34,True),SAND,tr=8)
    y+=140
    d.text((80,y),"47 SLIDES",font=f(120,True),fill=OFFWHITE); y+=150
    d.text((80,y),"ONE $92M",font=f(120,True),fill=SAND);       y+=150
    d.text((80,y),"EXIT",font=f(120,True),fill=SAND);           y+=210
    for line in ["The presentation structure that",
                 "sold AutoDS to Fiverr.",
                 "",
                 "Fill in your numbers. Get buyer-ready."]:
        d.text((80,y),line,font=f(34),fill=MIDGRAY); y+=52
    tracked(d,(80,H-120),"[ life is beta ]",f(30),SAND,tr=4)
    tracked(d,(W-80,H-120),"SWIPE",f(30,True),OFFWHITE,tr=6,left=False)
    return im

def slide_page(doc,i,n):
    im,d=base()
    px=doc[i].get_pixmap(dpi=200)
    s=Image.open(io.BytesIO(px.tobytes("png"))).convert("RGB")
    sw=W-100; sh=int(sw*s.height/s.width)
    s=s.resize((sw,sh),Image.LANCZOS)
    im.paste(s,(50,(H-sh)//2))
    tracked(d,(50,H-110),"THE EXIT DECK",f(26),MIDGRAY,tr=4)
    tracked(d,(W-50,H-110),n,f(26,True),SAND,tr=3,left=False)
    return im

def outro():
    im,d=base()
    y=380
    for line in ["Take the structure.","Fill in your numbers.","Send it."]:
        d.text((80,y),line,font=f(76,True),fill=OFFWHITE); y+=100
    y+=70
    for line in ["The full 47-slide template is in the comments.",
                 "",
                 "I'll take this deck apart section by",
                 "section here over the next few weeks."]:
        d.text((80,y),line,font=f(34),fill=MIDGRAY); y+=52
    tracked(d,(80,H-120),"[ life is beta ]",f(30),SAND,tr=4)
    tracked(d,(W-80,H-120),"Lior Pozin",f(30),MIDGRAY,tr=2,left=False)
    return im

doc=fitz.open(SRC); n=doc.page_count
if SHORT:
    idx=SHORT_PAGES
    pages=[hook_page()]+[slide_page(doc,p,f"[ {k+1} / {len(idx)} ]") for k,p in enumerate(idx)]+[outro()]
else:
    pages=[hook_page()]+[slide_page(doc,i,f"[ {i+1} / {n} ]") for i in range(n)]+[outro()]
pages[0].save(PREVIEW)
pages[0].save(OUT,save_all=True,append_images=pages[1:],resolution=150.0)
print(OUT, len(pages), "pages", W, "x", H)
