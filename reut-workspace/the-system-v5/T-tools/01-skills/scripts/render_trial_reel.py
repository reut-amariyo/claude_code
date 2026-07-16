#!/usr/bin/env python3
"""Render a listicle trial reel: vertical crop of b-roll + text-list card overlay.

Usage: render_trial_reel.py spec.json output.mp4

spec.json:
{
  "source": "/path/to/broll.mp4",     // horizontal or vertical source video
  "start": "00:03:20",                 // segment start in source
  "duration": 13,                      // reel length in seconds
  "crop_x_frac": 0.5,                  // horizontal center of the vertical crop, 0..1
  "hook": ["10 AI businesses", "you can start with $0", "in 2026"],
  "items": ["AI receptionist for clinics", "..."],
  "footer": "Comment \"BUILD\"",
  "scrim": 0.5                         // darkness of the overlay behind text, 0..1
}

Output: 1080x1920 MP4, no audio (music gets added in the IG app on upload).
Never posts anywhere - it only writes the file.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FFMPEG = str(Path(__file__).parent / ".ffmpeg-bin" / "ffmpeg")
W, H = 1080, 1920

HOOK_FONT = ("/System/Library/Fonts/Menlo.ttc", 1)  # Menlo Bold
ITEM_FONT = ("/System/Library/Fonts/HelveticaNeue.ttc", 0)
NUM_FONT = ("/System/Library/Fonts/Menlo.ttc", 1)
SAND = (226, 211, 184, 255)  # VI Sand accent
WHITE = (255, 255, 255, 255)


def load_font(spec, size):
    path, index = spec
    return ImageFont.truetype(path, size=size, index=index)


def build_card(spec, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 250
    hook_font = load_font(HOOK_FONT, 72)
    for line in spec["hook"]:
        w = draw.textlength(line, font=hook_font)
        draw.text(((W - w) / 2, y), line, font=hook_font, fill=WHITE)
        y += 92

    y += 55
    items = spec["items"]
    item_font = load_font(ITEM_FONT, 46)
    num_font = load_font(NUM_FONT, 42)
    line_h = 92
    x_num, x_text = 120, 210
    for i, item in enumerate(items, 1):
        draw.text((x_num, y + 4), f"{i:>2}", font=num_font, fill=SAND)
        draw.text((x_text, y), item, font=item_font, fill=WHITE)
        y += line_h

    footer = spec.get("footer")
    if footer:
        footer_font = load_font(HOOK_FONT, 52)
        w = draw.textlength(footer, font=footer_font)
        draw.text(((W - w) / 2, H - 260), footer, font=footer_font, fill=SAND)

    img.save(path)


def render(spec, out_path):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        card_path = tmp.name
    build_card(spec, card_path)

    crop_x = max(0.0, min(1.0, spec.get("crop_x_frac", 0.5)))
    scrim = spec.get("scrim", 0.5)
    # vertical 9:16 slice of the source, positioned by crop_x_frac
    vf = (
        f"crop=ih*{W}/{H}:ih:(iw-ih*{W}/{H})*{crop_x}:0,"
        f"scale={W}:{H},"
        f"drawbox=color=black@{scrim}:t=fill[bg];"
        f"[1:v]format=rgba,fade=t=in:st=0.3:d=0.6:alpha=1[card];"
        f"[bg][card]overlay=0:0"
    )
    cmd = [
        FFMPEG, "-hide_banner", "-loglevel", "error",
        "-ss", str(spec["start"]), "-t", str(spec["duration"]),
        "-i", spec["source"],
        "-loop", "1", "-t", str(spec["duration"]), "-i", card_path,
        "-filter_complex", vf,
        "-an", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-t", str(spec["duration"]), "-y", str(out_path),
    ]
    subprocess.run(cmd, check=True)
    Path(card_path).unlink(missing_ok=True)
    print(f"Rendered: {out_path}")


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    spec = json.loads(Path(sys.argv[1]).read_text())
    render(spec, sys.argv[2])


if __name__ == "__main__":
    main()
