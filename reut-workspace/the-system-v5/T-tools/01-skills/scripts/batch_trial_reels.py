#!/usr/bin/env python3
"""Render a full day-batch of trial reels from one batch JSON.

Usage: batch_trial_reels.py batch.json output_dir/

batch.json:
{
  "defaults": {"source": "...", "crop_x_frac": 0.62, "scrim": 0.55,
               "duration": 13, "footer": "Comment \"BUILD\""},
  "reels": [
    {"slug": "ai-businesses", "start": "00:09:55",
     "hook": ["...", "...", "..."], "items": ["...", ...],
     "keyword": "BUILD", "caption": "full caption text"},
    ...
  ]
}

Writes NN-slug.mp4 + NN-slug-caption.txt per reel and UPLOAD-CHECKLIST.md.
Renders files only - posting is always manual.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_trial_reel import render

SLOT_TIMES = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00"]


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    batch = json.loads(Path(sys.argv[1]).read_text())
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    defaults = batch.get("defaults", {})
    lines = [
        "# Upload checklist",
        "",
        "For each reel, in the Instagram app or Metricool:",
        '1. Upload the MP4, toggle **Trial** ON, paste the caption.',
        "2. Add a trending audio in the app.",
        "3. Make sure the comment keyword automation is live for the keyword.",
        "",
        "| # | File | Keyword | Suggested slot |",
        "|---|------|---------|----------------|",
    ]
    for i, reel in enumerate(batch["reels"], 1):
        spec = {**defaults, **reel}
        name = f"{i:02d}-{reel['slug']}"
        mp4 = out_dir / f"{name}.mp4"
        render(spec, mp4)
        (out_dir / f"{name}-caption.txt").write_text(reel["caption"])
        slot = SLOT_TIMES[(i - 1) % len(SLOT_TIMES)]
        lines.append(f"| {i} | {name}.mp4 | {reel.get('keyword', '?')} | {slot} |")

    (out_dir / "UPLOAD-CHECKLIST.md").write_text("\n".join(lines) + "\n")
    print(f"Batch done: {len(batch['reels'])} reels in {out_dir}")


if __name__ == "__main__":
    main()
