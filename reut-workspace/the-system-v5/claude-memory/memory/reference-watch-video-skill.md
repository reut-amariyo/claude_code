---
name: reference-watch-video-skill
description: "/watch skill lets Claude watch videos (frames + transcript); installed 2026-08-11, IG needs browser cookies"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 34833b2d-ed12-4fbf-b3e1-4eebd11150fa
  modified: 2026-08-11T10:18:07.640Z
---

The `/watch` skill (bradautomates/claude-video, MIT) is installed at `~/.claude/skills/watch`. Give it a video URL or local file + a question; it pulls captions (or Whisper with a GROQ_API_KEY/OPENAI_API_KEY in `~/.config/watch/.env` — none set, keyless mode), extracts frames via ffmpeg, and Claude reads them. Detail levels: transcript / efficient / balanced / token-burner.

Environment facts (2026-08-11, do not relearn):
- No Homebrew and only Python 3.9 on the Mac. ffmpeg = symlink in `~/.local/bin` to the imageio-ffmpeg static binary; ffprobe = wrapper script in `~/.local/bin` using dylibs copied to `~/.local/lib/watch-ffmpeg` (sourced from Remotion's compositor package).
- yt-dlp is the official standalone binary at `~/.local/bin/yt-dlp` (pip version removed — py3.9 caps it at an old release YouTube blocks). Update with `yt-dlp -U`.
- Instagram URLs fail anonymous download ("empty media response") — needs `--cookies-from-browser chrome` (triggers a keychain prompt) or a cookies file. Verified working on YouTube.
