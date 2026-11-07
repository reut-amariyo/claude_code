"""Record Lior's call lines with his ElevenLabs PVC voice. Usage: ELEVENLABS_API_KEY=sk_... python3 gen_voice.py"""
import json, os, urllib.request
VOICE = 'qAPjJ0gODMxl3kFXrSy6'  # "liors voice" PVC
key = os.environ['ELEVENLABS_API_KEY']
os.makedirs('voice', exist_ok=True)
for k, t in json.load(open('voice-lines.json')).items():
    if os.path.exists(f'voice/{k}.mp3'): continue
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_64',
        data=json.dumps({"text": t, "model_id": "eleven_multilingual_v2",
                         "voice_settings": {"stability": 0.5, "similarity_boost": 0.85, "style": 0.15, "use_speaker_boost": True}}).encode(),
        headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        a = urllib.request.urlopen(req, timeout=90).read(); open(f'voice/{k}.mp3', 'wb').write(a); print(k, 'ok', len(a))
    except Exception as e:
        print(k, 'ERR', getattr(e, 'code', ''), e.read()[:160] if hasattr(e, 'read') else e)
