---
name: ig-reel-audio-transcription-pipeline
description: "Working pipeline to transcribe any IG reel's audio — yt-dlp with Chrome cookies + Whisper with the vault's bundled ffmpeg"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 10284552-7464-430c-a514-35daf8a7657f
---

Proven 2026-07-14. To get the spoken script of an Instagram reel, transcribe the audio; do not screen-scrape captions.

1. Anonymous yt-dlp fails ("empty media response"). Use Reut's logged-in Chrome session:
   `yt-dlp --cookies-from-browser chrome -x -o "reel_<id>.%(ext)s" "<reel URL>"`
   yt-dlp lives at `/Users/reutamariyo/Library/Python/3.9/bin/yt-dlp`.
2. No system ffmpeg, so the mp3 postprocess step fails but the raw `.m4a` downloads fine — that's all Whisper needs.
3. Transcribe with the vault's bundled ffmpeg on PATH:
   `export PATH="<vault>/reut-workspace/the-system-v5/T-tools/01-skills/scripts/.ffmpeg-bin:$PATH"`
   then `/Users/reutamariyo/Library/Python/3.9/bin/whisper <file> --model small --language en --output_format txt`.
   A ~1 min reel takes under a minute on the small model.

Complements [[transcribe-ig-reel-native-screenshot]], which covers reading on-screen visuals (Chrome MCP renders video black). For Lior's own recordings use `transcribe_recordings.py` instead.
