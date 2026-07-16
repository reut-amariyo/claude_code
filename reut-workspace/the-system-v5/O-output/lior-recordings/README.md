# 🎙️ Lior Recordings → Transcripts

Drop Lior's recordings **here**, then transcribe them to Markdown for content work.

## How to use

1. **Drop a recording into this folder.**
   Works with: m4a, mp3, wav, mp4, mov, ogg, **opus** (WhatsApp voice notes), aac, aiff, flac…
   Hebrew, English, or mixed — Whisper auto-detects the language.

2. **Run the transcriber** (from the `the-system-v5` folder):
   ```
   python3 T-tools/01-skills/scripts/transcribe_recordings.py
   ```

3. **Find the transcript** in `../lior-transcripts/` as a clean `.md` file.

4. **Ask Claude** to turn it into content — e.g. "turn the latest transcript into an X post" (`/x`, `/ig`, `/scout`…).

## Options

| Want | Command |
|------|---------|
| Best quality (slower) | `... transcribe_recordings.py --model large-v3` |
| Default balance       | `... transcribe_recordings.py`  (model = medium) |
| Faster, rougher       | `... transcribe_recordings.py --model small` |
| One specific file     | `... transcribe_recordings.py "/path/to/file.m4a"` |
| Force Hebrew / English | `... --language he`  /  `... --language en` |
| Re-do an existing one | `... --force` |

Already-transcribed files are skipped automatically, so you can re-run it any time.
