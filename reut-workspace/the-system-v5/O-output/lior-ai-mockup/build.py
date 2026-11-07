import base64, json, os, re
s=open('app-src.html').read()
b64=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
norm=lambda t:re.sub(r'[^a-z0-9]','',t.lower())
lines=json.load(open('voice-lines.json'))
vm={norm(t):f'voice/{k}.mp3' for k,t in lines.items() if os.path.exists(f'voice/{k}.mp3')}
s=s.replace('__HERO__',b64('lior-hero.jpg')).replace('__AVA__',b64('lior-avatar.jpg')).replace('__VOICE_MAP__',json.dumps(vm))
open('lior-store-builder-ai.html','w').write(s)
print('voice clips mapped:',len(vm))
