---
name: reference-transcribe-ig-reel-native-screenshot
description: "How to read an Instagram reel's burned-in captions when Chrome MCP screenshots render the video black"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5b40193f-a7d7-4ea2-a771-75d4fa0d4b2b
---

To capture/transcribe an Instagram reel's spoken content, read its burned-in captions frame by frame. Chrome MCP's own screenshots render hardware-accelerated video as a BLACK frame — useless for this.

Working method:
1. Grant Chrome to computer-use via `request_access` (comes back tier "read" — fine, we only need to SEE it).
2. Open the reel and make its tab the visually-foreground tab (navigate the already-front tab to the reel URL; MCP-navigating a background tab does NOT bring it forward).
3. Click play via Chrome MCP `computer` left_click on the video center.
4. Take NATIVE screenshots with `mcp__computer-use__screenshot` (captures the composited display, so the real video frame + captions show). Batch `wait 1.5-2s + screenshot` x6 in one `computer_batch` to sweep a loop and read each caption segment.
5. Also pull `get_page_text` — for caption-style creators (e.g. thevibefounder) the full post caption often IS the script/structure.

Used for Lior content research when Reut sends a reel link to "catch the script". Related: [[project-lior-video-series-one-decision]]
