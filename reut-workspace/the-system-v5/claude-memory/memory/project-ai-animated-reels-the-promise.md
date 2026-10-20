---
name: project-ai-animated-reels-the-promise
description: "In-house AI animated reels for Lior (Higgsfield CLI + Nano Banana 2 + Seedance 2.5); episode 1 \"The Promise\" (Lior + Galit) delivered 2026-10-13 as v12, pipeline lessons inside"
metadata:
  node_type: memory
  type: project
  originSessionId: f5e7d479-8ec5-44e8-96ca-a6deaa95d073
  modified: 2026-10-14T14:00:39.412Z
---

Since 2026-10-12 Reut makes Lior's Pixar-style "Based on our own story" reels in-house instead of hiring a creator.
Folder: `reut-workspace/the-system-v5/O-output/ai-animated-reels/the-promise/` (script, approved Lior + Galit sheets, locations, clips, voice refs).

Episode 1 "The Promise": café date → moldy 40 sqm apartment → graduation + Fiverr $92M → tarmac "1.8 million, and we're not stopping here" → real B-roll (jet, champagne, Ferrari). Final = `clips/the-promise-v12.mp4`, 33s, 9:16, NO baked music or captions (Reut adds both in TikTok). Hook still open: flash-forward + "From a moldy 40m² apartment to this" proposed as an IG Trial Reel A/B test.

Feedback that set the cut: Galit (top priority, she appears) = keep animation, real ending fast, champagne short. Alex = "animated reels usually run 1 min+" (answer with retention data, not padding). Shaked = improve the hook.

**Why:** pipeline knowledge cost ~10 hours and ~1,930 Higgsfield credits to learn; next episode estimated 3-4 hours.

**How to apply (hard-won):**
- Higgsfield CLI at `~/.local/bin/higgsfield`, needs `dangerouslyDisableSandbox` for network; zsh does not word-split `$VAR` (use `${=VAR}`), and `$R[v1]` is read as an array index (use `${R}`).
- Seedance "ip_detected" = auto-refunded. Triggers seen: generated music in the prompt, long multi-scene montages. Fix: say "No music", split into 4-6s clips, minimum duration 4s.
- Voices drift per clip: give `--audio-references` from the first approved clip from the START; loudness-match every clip (loudnorm -16) and gate quiet clips, or a faint Seedance music bed gets amplified.
- Write numbers as words in dialogue ("one point eight million"), never digits.
- CUT DENSITY drives virality (George, 2026-10-14): target an average shot of ~1.2s / ~8 cuts per 10s. Measured: Lior's best animated reel (49K likes) 1.2s, TJR fan reference 1.1s, our v12 animated part 2.8s. Ask Seedance for a cut every 1-1.5s in every prompt; in the edit, add 20% punch-ins on any shot held over 1.6s (v13).
- Reut's taste: fast speech (+15% speed in edit), 9:16, Lior always calm and confident (never wide-eyed), no masks, characters face each other not the camera, real B-roll muted and ~0.8s per shot, couple shots over Lior-alone.
Related: [[lior-ig-content-engines]], [[project-lior-ai-clone-videos-nicola]], [[reference-watch-video-skill]]
