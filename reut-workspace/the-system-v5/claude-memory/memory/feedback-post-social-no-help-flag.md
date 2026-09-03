---
name: feedback-post-social-no-help-flag
description: "post_social.py has NO --help flag; any arg1 becomes live post text. Never run it to \"check usage\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e86b3836-bc91-4d96-8d23-108d75f1ac40
---

`T-tools/01-skills/scripts/post_social.py` takes `argv[1]` as the post text verbatim — there is NO `--help`/`-h` handling. Running `post_social.py --help` schedules a post whose text is literally "--help".

**Why:** On 2026-05-31 I ran `post_social.py --help` to inspect usage and it scheduled a "--help" post to X + Bluesky via Metricool. (It did not publish — Metricool dropped it from the queue — but that was luck, not a safeguard.)

**How to apply:** To understand the script, READ the file, don't run it. To schedule, call it only with real post text as arg1 and a time as arg2 (`"HH:MM"` for today or full ISO for another day). When scheduling multiple posts with quotes/newlines, import `post_to_metricool` in a Python heredoc instead of shell-quoting. Related: [[project-x-reply-pipeline-whitelist-collapse]].
