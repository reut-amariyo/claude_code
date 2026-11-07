from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
W,H=1080,1350
ph=Image.open('clean.jpg').convert('RGB')
# 4:5 crop 1500x1875, keep from top
ph=ph.crop((0,60,1500,1935)).resize((W,H),Image.LANCZOS)
# top gradient for text
g=np.zeros((H,W),dtype=np.uint8)
for y in range(H):
    t=y/H
    a = 235 if t<0.30 else max(0,int(235*(1-(t-0.30)/0.16)))
    g[y,:]=a
grad=Image.fromarray(g,'L')
dark=Image.new('RGB',(W,H),(14,14,16))
img=Image.composite(dark,ph,grad)
d=ImageDraw.Draw(img)
HN='/System/Library/Fonts/HelveticaNeue.ttc'
fq=ImageFont.truetype(HN,58,index=4)   # bold
fs=ImageFont.truetype(HN,30,index=0)
fn=ImageFont.truetype(HN,34,index=4)
# logo: key out dark bg
lg=Image.open('investing-logo.png').convert('RGBA'); a=np.asarray(lg).copy()
lum=a[:,:,:3].astype(int).max(axis=2)
a[:,:,3]=np.clip((lum-40)*255//(200-40),0,255).astype(np.uint8)
lg=Image.fromarray(a); lg=lg.resize((int(lg.width*0.62),int(lg.height*0.62)),Image.LANCZOS)
M=72; y=70
img.paste(lg,(M-6,y),lg); y+=lg.height+46
quote='“AutoDS and the team that joined Fiverr a couple of years ago are killing it.”'
words=quote.split(); lines=[]; cur=''
for w_ in words:
    t=(cur+' '+w_).strip()
    if d.textlength(t,font=fq)>W-2*M: lines.append(cur); cur=w_
    else: cur=t
lines.append(cur)
for ln in lines:
    d.text((M,y),ln,font=fq,fill=(255,255,255)); y+=72
y+=22
d.rectangle((M,y+6,M+48,y+10),fill=(240,120,30))
d.text((M+66,y-6),'Micha Kaufman',font=fn,fill=(255,255,255)); y+=44
d.text((M+66,y-6),'Founder & CEO, Fiverr  |  NYSE: FVRR',font=fs,fill=(205,205,210))
img.save('lior-micha-quote-card.png'); img.save('lior-micha-quote-card.jpg',quality=93)
print(y)
