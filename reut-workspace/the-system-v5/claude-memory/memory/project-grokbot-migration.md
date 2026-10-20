---
name: project-grokbot-migration
description: "2026-09-13 Grok Bot migration of the-system-v5; which bots exist there, which schedules Reut retired, and where bluesky-mirror lives"
metadata: 
  node_type: memory
  type: project
  originSessionId: 912912c3-20df-4ca8-9e96-07c51659d81d
  modified: 2026-09-13T20:09:34.141Z
---

On 2026-09-13 Reut migrated the-system-v5 to Grok Bot (SuperGrok $30 plan). Guide:
the-system-v5/O-output/grokbot-migration/GROKBOT-MIGRATION-GUIDE.md. A `tom-guide` bot
read it from the GitHub repo (read-only fine-grained PAT) and created 13 bots + 3 rooms.
The vault-root CLAUDE.md had to be force-added to git for the bots to read it.

Retired by Reut the same day, "I no longer use them": `daily-pm`, `x-daily-reply-posts`,
`x-analyst-weekly`. Do not draft for them, do not re-enable them, do not treat the
Sunday X analyst hypothesis as a live input anymore.

LinkedIn bots that need a browser logged in as Lior (comment-drafts, daily-scan, weekly-digest)
stay on the Mac. `bluesky-mirror` placement was still undecided at the end of the session;
it must run in exactly one place or Bluesky/Threads get double posts.

**Why:** Reut wants the cloud-native parts (mirror) off the sleeping laptop and the
lightly-used X analytics gone, not moved.

**How to apply:** before touching any scheduled task, check this file and
[[project-agency-produces-content-i-learn]]. Secrets are per bot in Grok Bot and Reut enters
them herself via the secure secret card; Claude never handles the values.
