#!/usr/bin/env python3
"""12-page portrait carousel for LinkedIn: the exit deck's ARCHITECTURE, typeset
for the feed. The full 47-slide file stays in the first comment.

Copy is lifted verbatim from the template's own section dividers.
"""
import os, textwrap
from PIL import Image, ImageDraw, ImageFont

GRAPHITE=(33,36,37); OFFWHITE=(245,243,240); SAND=(194,167,119); MIDGRAY=(146,148,148)
MONO="/System/Library/Fonts/Menlo.ttc"
W,H=1080,1350
here=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(here,"exit-deck-carousel-sections.pdf")

SECTIONS=[
 ("01","Executive Summary","The whole business in 8 slides. A buyer should be 70% convinced before page 12."),
 ("02","Industry","Third-party sources only. Your credibility on every later slide borrows from this one."),
 ("03","Solutions & Technology","What the product does, shown as jobs done for the customer. Real screenshots only."),
 ("04","Architecture","One look that says this scales. Volume numbers are receipts; claims are cheap."),
 ("05","Competitive Landscape","Name real competitors. An honest matrix survives diligence; an inflated one dies there."),
 ("06","Customers & Marketing","The growth engine, then the unit economics. This is where good deals become great ones."),
 ("07","Future Growth Drivers","This section is what the buyer's money buys. Write it as their plan, not yours."),
 ("08","Operations & Transaction","The company behind the product. Boring is the goal, every detail here is one less diligence question."),
 ("09","Financials","By now every number was earned by an earlier slide. This is just the scoreboard."),
]

def f(s,b=False): return ImageFont.truetype(MONO,s,index=1 if b else 0)
def base():
    im=Image.new("RGB",(W,H),GRAPHITE); return im, ImageDraw.Draw(im)
def tracked(d,xy,t,ft,fill,tr=0,left=True):
    x,y=xy
    if not left: x-=sum(d.textlength(c,font=ft)+tr for c in t)-tr
    for c in t: d.text((x,y),c,font=ft,fill=fill); x+=d.textlength(c,font=ft)+tr
def block(d,x,y,text,ft,fill,width,lead):
    for line in textwrap.wrap(text,width=width):
        d.text((x,y),line,font=ft,fill=fill); y+=lead
    return y
def foot(d,right):
    tracked(d,(80,H-110),"THE EXIT DECK",f(26),MIDGRAY,tr=4)
    tracked(d,(W-80,H-110),right,f(26,True),SAND,tr=3,left=False)

pages=[]

# 1 — hook
im,d=base()
d.rectangle([80,150,148,218],outline=SAND,width=3)
tracked(d,(80,300),"THE EXIT DECK",f(34,True),SAND,tr=8)
y=440
d.text((80,y),"47 SLIDES",font=f(120,True),fill=OFFWHITE); y+=150
d.text((80,y),"ONE $92M",font=f(120,True),fill=SAND); y+=150
d.text((80,y),"EXIT",font=f(120,True),fill=SAND); y+=200
block(d,80,y,"The 9 sections that sold AutoDS to Fiverr, and what each one has to do.",f(34),MIDGRAY,44,52)
tracked(d,(80,H-110),"[ life is beta ]",f(30),SAND,tr=4)
tracked(d,(W-80,H-110),"SWIPE",f(30,True),OFFWHITE,tr=6,left=False)
pages.append(im)

# 2 — the spine
im,d=base()
tracked(d,(80,150),"THE ARCHITECTURE",f(30,True),SAND,tr=8)
d.text((80,240),"The 9-section spine",font=f(64,True),fill=OFFWHITE)
y=380
for i,(num,name,_) in enumerate(SECTIONS):
    tracked(d,(80,y),num,f(40,True),SAND,tr=2)
    d.text((190,y),name,font=f(40),fill=OFFWHITE); y+=76
block(d,80,y+40,"Financials come last on purpose.",f(32),SAND,50,46)
foot(d,"[ SPINE ]")
pages.append(im)

# 3-11 — one page per section
for i,(num,name,rule) in enumerate(SECTIONS):
    im,d=base()
    tracked(d,(80,330),f"[ {num} ]",f(40,True),SAND,tr=4)
    y=430
    for line in textwrap.wrap(name,width=17):
        d.text((80,y),line,font=f(78,True),fill=OFFWHITE); y+=100
    block(d,80,y+60,rule,f(36),MIDGRAY,42,56)
    foot(d,f"[ {i+1} / 9 ]")
    pages.append(im)

# 12 — close
im,d=base()
y=380
for line in ["Take the structure.","Fill in your numbers.","Send it."]:
    d.text((80,y),line,font=f(76,True),fill=OFFWHITE); y+=100
y+=70
block(d,80,y,"The full 47-slide template is in the comments.",f(34),MIDGRAY,46,52)
block(d,80,y+110,"I'll take this deck apart section by section here over the next few weeks.",
      f(34),MIDGRAY,46,52)
tracked(d,(80,H-110),"[ life is beta ]",f(30),SAND,tr=4)
tracked(d,(W-80,H-110),"Lior Pozin",f(30),MIDGRAY,tr=2,left=False)
pages.append(im)

pages[0].save(OUT,save_all=True,append_images=pages[1:],resolution=150.0)
pages[0].save(os.path.join(here,"carousel-sections-p1.png"))
print(OUT,len(pages),"pages")
