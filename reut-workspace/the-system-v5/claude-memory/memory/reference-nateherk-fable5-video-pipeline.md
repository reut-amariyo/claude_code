---
name: nateherk-fable5-video-pipeline
description: "Nate Herk's end-to-end AI video production pipeline with Claude Fable 5 — workflow steps, costs, and prerequisites. Reference for Lior's ONE DECISION video series."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 15f874d3-f1ca-4518-bd60-9de43deaa66a
---

Source: https://www.wisdomai.com/insights/nateherk/claude-fable-5-ai-video-production-long-horizon-ai-3f34db39 (shared by Reut 2026-07-02, "learn from this")

Nate Herk had Claude Fable 5 autonomously produce a complete YouTube video from a single prompt in ~1 hour: script in the creator's voice → chunked audio via ElevenLabs voice clone → avatar rendering → ffmpeg stitching → motion graphics generated as code → rendered frames visually verified scene by scene.

Key numbers: ~380K tokens, ~1 hour, $10/M input + $50/M output token pricing — meaningful paid-plan consumption per video.

Critical caveat: it only worked because infrastructure pre-existed — working voice clone, avatar rendering engine, integrated stitching tools, saved templates. Same prompt without those assets ≠ same result.

Practical lessons (relevant to [[lior-video-series-one-decision]]):
- Automate ONE repeatable step at a time, not the whole pipeline at once
- Preserve templates per episode for consistency; don't expect identical output from identical prompts
- Measure token cost per video before scaling
- Keep a human/visual verification step on every rendered scene — the model iterated on visual output, it didn't skip QA
