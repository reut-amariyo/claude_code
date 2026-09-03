---
name: podcast-audio-transcription-pipeline
description: "Proven pipeline to transcribe any podcast episode locally — curl mp3 from page, vault ffmpeg on PATH, Whisper small"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d7cec0df-7dab-4b1c-ad4c-516ad2f6f7c8
  modified: 2026-08-03T13:39:32.478Z
---

Proven 2026-08-02 on Real Life Superpowers E97 (Lior, 50 min).

Pipeline:
1. `curl` the episode page, grep for `.mp3` URLs. WordPress podcast sites embed the file directly.
2. Put the vault ffmpeg on PATH: `the-system-v5/T-tools/01-skills/scripts/.ffmpeg-bin` — it is a SYMLINK to the imageio_ffmpeg full build, so `find -type f -name ffmpeg` misses it. Do not conclude "no ffmpeg" from that; check this dir first.
3. `~/Library/Python/3.9/bin/whisper file.mp3 --model small --language en` — small model does ~50 min of audio in ~3.5 min on this Mac.
4. Whisper mishears brand names: "AutoDS" → "Autodesk", "Pozin" → "Pozen". Always grep and fix before delivering.
5. HEBREW audio: the small model produces garbage Hebrew (confirmed 2026-08-03). Use `--model large-v3 --language he` — large-v3 is already cached in ~/.cache/whisper. Pass ALL files in one whisper invocation so the 3GB model loads once. Even large-v3 mishears Hebrew names ("טוני רובינס" → "רובינסון"); translate meaning, flag uncertain lines.
6. REPETITION LOOPS ("אה אה אה", "ו... ו... ו...", rows of ".") are a decoder failure, not silence. Fix: re-slice just those windows with ffmpeg and re-run with `--condition_on_previous_text False`. Recovered four whole topics on the 2026-08-20 Tony Robbins tape that the first pass had swallowed. Detect them from the JSON: `compression_ratio > 2.4` flags the loop. Loops also cost real time — a 20-min tape ran 5.6x realtime with loops, ~2x without.
7. Consistent Hebrew mishears to fix on sight: AutoDS → "אותו דיאס"/"אוטודסק", LTV → "MTV", וילה → "מילה", UFC → "CFC", Burning Man → "גרונינג מן".

Avoid the remotion ffmpeg at `T-tools/remotion-videos/node_modules/@remotion/compositor-darwin-arm64/` — it needs `DYLD_LIBRARY_PATH` set to its own dir and its `s16le` pipe muxer is stripped, so Whisper's internal ffmpeg call fails with it. Workaround if ever needed: convert to 16 kHz mono WAV, load with `wave`+numpy, pass the float32 array to `model.transcribe()` directly.

Related: [[reference-ig-reel-audio-transcription-pipeline]]. Output convention: `O-output/podcast-transcripts/` with ~45-second timestamp paragraphs.
