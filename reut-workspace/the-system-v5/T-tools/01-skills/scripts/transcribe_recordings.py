#!/usr/bin/env python3
"""
transcribe_recordings.py — Transcribe Lior's audio/video recordings to Markdown.

Handles Hebrew, English, or mixed-language recordings (Whisper auto-detects).
Self-contained: bundles its own ffmpeg via the imageio-ffmpeg pip package, so
no Homebrew / system ffmpeg is required.

USAGE
-----
  # Transcribe every new file in O-output/lior-recordings/
  python3 transcribe_recordings.py

  # Transcribe one specific file
  python3 transcribe_recordings.py "/path/to/voice note.m4a"

  # Choose a model (default: medium — best Hebrew/quality balance)
  python3 transcribe_recordings.py --model large-v3      # best quality, slow
  python3 transcribe_recordings.py --model small         # faster, rougher

  # Force the language instead of auto-detecting
  python3 transcribe_recordings.py --language he
  python3 transcribe_recordings.py --language en

WORKFLOW
--------
1. Drop a recording into  O-output/lior-recordings/
   (m4a, mp3, wav, mp4, mov, ogg, opus, aac, webm, flac — incl. WhatsApp notes)
2. Run:  python3 transcribe_recordings.py
3. A clean .md transcript appears in  O-output/lior-transcripts/
4. Ask Claude to turn it into posts (/x, /ig, /scout, etc.)

Already-transcribed files are skipped automatically.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import sys
from pathlib import Path

# --- Locate the vault / output folders relative to this script -------------
SCRIPT_DIR = Path(__file__).resolve().parent
# scripts/ -> 01-skills/ -> T-tools/ -> the-system-v5/
PROJECT_ROOT = SCRIPT_DIR.parents[2]
RECORDINGS_DIR = PROJECT_ROOT / "O-output" / "lior-recordings"
TRANSCRIPTS_DIR = PROJECT_ROOT / "O-output" / "lior-transcripts"

AUDIO_EXTS = {
    ".m4a", ".mp3", ".wav", ".mp4", ".mov", ".ogg",
    ".opus", ".aac", ".webm", ".flac", ".mkv", ".m4v",
    ".aiff", ".aif",
}


def _setup_ffmpeg() -> None:
    """Put the bundled ffmpeg binary on PATH under the name 'ffmpeg'."""
    try:
        import imageio_ffmpeg
    except ImportError:
        sys.exit("Missing dependency: run  pip3 install imageio-ffmpeg")

    exe = Path(imageio_ffmpeg.get_ffmpeg_exe())
    bin_dir = SCRIPT_DIR / ".ffmpeg-bin"
    bin_dir.mkdir(exist_ok=True)
    link = bin_dir / "ffmpeg"
    if not link.exists():
        try:
            link.symlink_to(exe)
        except OSError:
            # Fall back to a copy if symlinks aren't allowed
            import shutil
            shutil.copy2(exe, link)
            link.chmod(0o755)
    os.environ["PATH"] = f"{bin_dir}{os.pathsep}" + os.environ.get("PATH", "")


def _fmt_duration(seconds: float) -> str:
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{sec:02d}" if h else f"{m:d}:{sec:02d}"


def _gather_targets(arg_path: str | None) -> list[Path]:
    if arg_path:
        p = Path(arg_path).expanduser()
        if not p.exists():
            sys.exit(f"File not found: {p}")
        if p.is_dir():
            return sorted(f for f in p.iterdir() if f.suffix.lower() in AUDIO_EXTS)
        return [p]
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)
    return sorted(f for f in RECORDINGS_DIR.iterdir() if f.suffix.lower() in AUDIO_EXTS)


def _transcript_path(audio: Path) -> Path:
    return TRANSCRIPTS_DIR / f"{audio.stem}.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe recordings to Markdown.")
    parser.add_argument("path", nargs="?", help="Audio file or folder (default: lior-recordings/)")
    parser.add_argument("--model", default=os.environ.get("WHISPER_MODEL", "medium"),
                        help="Whisper model: tiny|base|small|medium|large-v3 (default: medium)")
    parser.add_argument("--language", default=None,
                        help="Force language, e.g. 'he' or 'en' (default: auto-detect)")
    parser.add_argument("--force", action="store_true",
                        help="Re-transcribe even if a transcript already exists")
    args = parser.parse_args()

    targets = _gather_targets(args.path)
    if not targets:
        print(f"No audio files found.\nDrop recordings into:\n  {RECORDINGS_DIR}")
        return

    pending = [t for t in targets if args.force or not _transcript_path(t).exists()]
    skipped = len(targets) - len(pending)
    if skipped:
        print(f"Skipping {skipped} already-transcribed file(s). Use --force to redo.")
    if not pending:
        print("Nothing new to transcribe.")
        return

    _setup_ffmpeg()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading Whisper model '{args.model}' (first run downloads it once)...")
    import whisper
    model = whisper.load_model(args.model)

    for i, audio in enumerate(pending, 1):
        print(f"\n[{i}/{len(pending)}] Transcribing: {audio.name}")
        try:
            result = model.transcribe(
                str(audio),
                language=args.language,   # None => auto-detect
                fp16=False,               # CPU-safe
                verbose=False,
            )
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR: {e}")
            continue

        text = result.get("text", "").strip()
        lang = result.get("language", "?")
        duration = result["segments"][-1]["end"] if result.get("segments") else 0
        today = _dt.date.today().isoformat()

        out = _transcript_path(audio)
        out.write_text(
            f"---\n"
            f"source: {audio.name}\n"
            f"transcribed: {today}\n"
            f"language: {lang}\n"
            f"duration: {_fmt_duration(duration)}\n"
            f"model: {args.model}\n"
            f"speaker: Lior Pozin\n"
            f"status: raw\n"
            f"---\n\n"
            f"# Transcript — {audio.stem}\n\n"
            f"{text}\n",
            encoding="utf-8",
        )
        print(f"  -> {out.relative_to(PROJECT_ROOT)}  ({lang}, {_fmt_duration(duration)})")

    print(f"\nDone. Transcripts are in:\n  {TRANSCRIPTS_DIR}")


if __name__ == "__main__":
    main()
