#!/usr/bin/env python3
"""Carousel: the 8 slides that decide a deck. Brand-book design, one idea per card."""
import os, textwrap
from PIL import Image, ImageDraw, ImageFont

GRAPHITE=(33,36,37); OFFWHITE=(245,243,240); SAND=(194,167,119); MIDGRAY=(146,148,148)
MONO="/System/Library/Fonts/Menlo.ttc"
W,H=1080,1350
here=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(here,"carousel-8-slides.pdf")

CARDS=[
 ("01","The founder story",
  "Investors and buyers decide on the person first. Open with where you came from, not what you built."),
 ("02","The macro trend",
  "A shift that is true whether you build this or not. It answers why now, before anyone asks."),
 ("03","Problem and solution",
  "Third, not first. After the story and the trend, the problem reads as inevitable."),
 ("04","Traction",
  "Users and revenue. Strong numbers go early, thin ones go later. A waitlist is not traction."),
 ("05","Distribution",
  "Anyone can build now. Show what already works, then what the money unlocks."),
 ("06","Financials",
  "Nobody believes year five. They are checking whether you know what to do with the money."),
 ("07","The case study",
  "One customer saying it better than you can. If you don't have one, go get one."),
 ("08","The demo",
  "Show the product, late. Most of them never log in. The story is what they remember."),
]

def f(s,b=False): return ImageFont.truetype(MONO,s,index=1 if b else 0)
def base(): im=Image.new("RGB",(W,H),GRAPHITE); return im, ImageDraw.Draw(im)
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

im,d=base()
d.rectangle([80,150,148,218],outline=SAND,width=3)
tracked(d,(80,300),"THE EXIT DECK",f(34,True),SAND,tr=8)
y=430
d.text((80,y),"8 SLIDES",font=f(122,True),fill=OFFWHITE); y+=155
d.text((80,y),"DECIDE",font=f(122,True),fill=SAND); y+=155
d.text((80,y),"THE DEAL",font=f(122,True),fill=SAND); y+=205
block(d,80,y,"What every deck has to do to survive the room. Buyers and investors both.",
      f(34),MIDGRAY,44,52)
tracked(d,(80,H-110),"[ life is beta ]",f(30),SAND,tr=4)
tracked(d,(W-80,H-110),"SWIPE",f(30,True),OFFWHITE,tr=6,left=False)
pages.append(im)

for i,(num,title,rule) in enumerate(CARDS):
    im,d=base()
    tracked(d,(80,320),f"[ {num} ]",f(40,True),SAND,tr=4)
    y=420
    for line in textwrap.wrap(title,width=17):
        d.text((80,y),line,font=f(78,True),fill=OFFWHITE); y+=100
    block(d,80,y+60,rule,f(36),MIDGRAY,42,56)
    foot(d,f"[ {i+1} / 8 ]")
    pages.append(im)

im,d=base()
y=360
for line in ["Order is leverage."]:
    d.text((80,y),line,font=f(76,True),fill=OFFWHITE); y+=120
block(d,80,y+20,"Financials come last on purpose. The first 60 pages earn the right to show them.",
      f(38),SAND,40,58)
block(d,80,y+230,"The full 47-slide template that sold AutoDS is linked in the first comment. No need to comment for it.",
      f(32),MIDGRAY,48,48)
tracked(d,(80,H-110),"[ life is beta ]",f(30),SAND,tr=4)
tracked(d,(W-80,H-110),"Lior Pozin",f(30),MIDGRAY,tr=2,left=False)
pages.append(im)

pages[0].save(OUT,save_all=True,append_images=pages[1:],resolution=150.0)
print(OUT,len(pages),"pages")
