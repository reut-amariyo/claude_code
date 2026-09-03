---
name: feedback-ai-prompts-in-code-blocks
description: Deliver every AI-tool prompt (image, video, lipsync) inside a fenced code block so Reut gets a one-click copy button
metadata:
  type: feedback
---

When Reut asks for a prompt to paste into an AI tool (Seedream, HiggsField, Kling, Veo,
NanoBanana, ElevenLabs, sync.so, etc.), always deliver it inside a fenced code block.

**Why:** Reut asked on 2026-08-31. Prompts delivered as plain paragraphs have to be
selected by hand, which is slow and error-prone with long multi-paragraph prompts. A
fenced block gives her a copy button.

**How to apply:** wrap the prompt text in triple backticks. Use a plain fence with no
language tag for prompts. Keep the fence around the prompt ONLY, so the copy grabs exactly
what goes into the tool and nothing else. Explanation, settings and flags go outside the
fence. If there is a separate negative prompt, give it its own fence.

Note this is the opposite of the drafts rule in [[feedback-reply-formatting]] and
[[feedback-post-draft-delimiters]]: social posts and replies stay plain text with
--- POST STARTS/ENDS --- markers, because she edits those before publishing. Only
machine-input prompts go in code blocks.
