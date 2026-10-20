#!/usr/bin/env python3
"""Render the 'The 50 people who taught me' 4:5 card with real headshots. 2x = 2160x2700."""
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os
V="/Users/reutamariyo/Documents/Obsidian Vault/reut-workspace/the-system-v5"
F=V+"/T-tools/assets/fonts/"; AV=V+"/O-output/linkedin-swipe-engine/data/raw/avatars/"
HIRES=os.path.dirname(os.path.abspath(__file__))+"/avatars-hires/"  # verified 400px, takes priority
S=int(os.environ.get("CARD_SCALE","2"))  # scale, override with CARD_SCALE=3
W,H=1080*S,1350*S
BG=(233,231,227); TILE=(255,255,255); INK=(31,31,31); INK2=(92,90,86); SAND=(201,169,122); CIRC=(224,222,218)
def font(name,size): return ImageFont.truetype(F+name,int(size*S))
mono_b=lambda s: font("JetBrainsMono-Bold.ttf",s); mono=lambda s: font("JetBrainsMono-Regular.ttf",s)
inter_b=lambda s: font("Inter-Bold.ttf",s); inter=lambda s: font("Inter-Regular.ttf",s)

rows=[
 ("01","MINDSET",["For the days","you want to quit"],[("Arianna Huffington","9.6M","ariannahuffington"),("Tony Robbins","7.5M","officialtonyrobbins"),("Sahil Bloom","723K","sahilbloom"),("Dan Ariely","452K","danariely")]),
 ("02","LEADERSHIP",["For when the","team gets bigger","than you"],[("Satya Nadella","12.2M","satyanadella"),("Simon Sinek","9.1M","simonsinek"),("Adam Grant","5.6M","adammgrant"),("Brigette Hyacinth","4.2M","brigettehyacinth")]),
 ("03","AI",["For what","actually works","inside a company"],[("Lex Fridman","1.77M","lexfridman"),("Jensen Huang","1.74M","jenhsunhuang"),("Allie K. Miller","1.67M","alliekmiller"),("Pascal Bornet","1.55M","pascalbornet")]),
 ("04","BUSINESS",["For the numbers","behind the","growth"],[("Richard Branson","18.6M","rbranson"),("Gary Vaynerchuk","6.0M","garyvaynerchuk"),("Sara Blakely","2.3M","sarablakely27"),("Alex Hormozi","1.05M","alexhormozi")]),
 ("05","FOUNDERS &\nINVESTORS",["For the people","in the arena"],[("Steven Bartlett","3.2M","stevenbartlett-123"),("Garry Tan","346K","garrytan"),("Harry Stebbings","281K","harrystebbings"),("Greg Isenberg","256K","gisenberg")]),
]

im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
M=40*S  # margin
# header
y=52*S
f1=mono_b(36); f2=mono(25)
d.text((M,y),"The top 1% of creators to follow on LinkedIn",font=f1,fill=INK)
y2=y+54*S
pre="who taught me how to build a "; hi="$50M ARR"; post=" company."
x=M
d.text((x,y2),pre,font=f2,fill=INK2); x+=d.textlength(pre,font=f2)
hw=d.textlength(hi,font=f2); d.rectangle([x-5*S,y2+3*S,x+hw+5*S,y2+33*S],fill=SAND)
d.text((x,y2),hi,font=mono_b(25),fill=INK); x+=hw
d.text((x,y2),post,font=f2,fill=INK2)

# grid
top=186*S; gap=18*S; label_w=165*S; rowh=192*S
tile_w=(W-2*M-label_w)/4
for i,(num,name,desc,people) in enumerate(rows):
    ry=top+i*(rowh+gap)
    # label block
    d.rectangle([M+label_w,ry,W-M,ry+rowh],fill=(224,222,218))
    d.rectangle([M,ry,M+label_w,ry+rowh],fill=SAND)
    d.text((M+14*S,ry+14*S),num,font=mono(15),fill=INK)
    d.multiline_text((M+14*S,ry+40*S),name,font=mono_b(21),fill=INK,spacing=4*S)
    dy=ry+40*S+(26*S if "\n" not in name else 54*S)+16*S
    for line in desc:
        d.text((M+14*S,dy),line,font=inter(13.5),fill=INK); dy+=17*S
    # tiles
    for j,(pname,fol,slug) in enumerate(people):
        tx=M+label_w+j*tile_w; tx2=tx+tile_w
        pad=5*S
        d.rectangle([tx+pad,ry+pad,tx2-pad,ry+rowh-pad],fill=TILE)
        cx=(tx+tx2)/2; r=38*S; cy=ry+16*S+r
        p=HIRES+slug+".jpg"
        if not os.path.exists(p): p=AV+slug+".jpg"
        if os.path.exists(p):
            ph=ImageOps.fit(Image.open(p).convert("RGB"),(2*r,2*r),Image.LANCZOS)
            ph=ph.filter(ImageFilter.UnsharpMask(radius=1.1*S,percent=95,threshold=2))
            mask=Image.new("L",(2*r*2,2*r*2),0); ImageDraw.Draw(mask).ellipse([0,0,4*r-1,4*r-1],fill=255); mask=mask.resize((2*r,2*r),Image.LANCZOS)
            im.paste(ph,(int(cx-r),int(cy-r)),mask)
            d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(210,208,204),width=S)
        else:
            d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=CIRC,outline=INK2,width=S)
        # name, up to 2 lines
        fn=inter_b(16.5); words=pname.split(); lines=[pname]
        if d.textlength(pname,font=fn)>tile_w-24*S and len(words)>1:
            lines=[" ".join(words[:-1]),words[-1]] if len(words)>2 else words
        lh=20*S; fol_y=ry+rowh-30*S; ntop=cy+r
        ny=ntop+(fol_y-ntop-len(lines)*lh)/2
        for ln in lines:
            d.text((cx,ny),ln,font=fn,fill=INK,anchor="ma"); ny+=lh
        d.text((cx,fol_y),fol,font=mono(14.5),fill=INK,anchor="ma")

# footer
fy=H-104*S
d.line([M,fy,W-M,fy],fill=INK,width=S)
pr=26*S; pcx=M+pr; pcy=fy+46*S
lp=AV+"liorpozin.jpg"
if os.path.exists(lp):
    ph=ImageOps.fit(Image.open(lp).convert("RGB"),(2*pr,2*pr),Image.LANCZOS)
    mask=Image.new("L",(4*pr,4*pr),0); ImageDraw.Draw(mask).ellipse([0,0,4*pr-1,4*pr-1],fill=255); mask=mask.resize((2*pr,2*pr),Image.LANCZOS)
    im.paste(ph,(int(pcx-pr),int(pcy-pr)),mask)
d.text((pcx+pr+14*S,pcy-10*S),"Lior Pozin",font=inter_b(18),fill=INK)
d.text((W-M,pcy-9*S),"follow.liorpozin.com",font=mono(17),fill=INK,anchor="ra")
im.save(f"lior-50-card-{W}x{H}.png")
im.resize((1080,1350),Image.LANCZOS).save("lior-50-card-1080x1350.png")
print(f"saved {W}x{H} + 1080x1350")
