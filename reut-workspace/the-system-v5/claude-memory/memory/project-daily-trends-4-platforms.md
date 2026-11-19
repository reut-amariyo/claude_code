---
name: project-daily-trends-4-platforms
description: "Daily 08:00 trends report across TikTok, IG, X, LinkedIn in Lior's niche; Volume (tryvolume.app) for TikTok+IG, Grok x_search for X, swipe engine for LinkedIn"
metadata:
  node_type: memory
  type: project
  originSessionId: b5849d32-f219-4c7a-ab15-54e3661fd8ef
  modified: 2026-11-11T15:45:50.248Z
---

Set up 2026-11-11 at Reut's request: every morning at 08:00 she wants the most trending posts in Lior's niche, one per platform audience.

- **Audiences:** TikTok = US builders; IG = builders, US; LinkedIn = entrepreneurs, builders, investors; X = buyers for AvatarFactory (AI influencers / UGC / avatars). Ownership stays private per [[project-lior-avatar-factory-side-project]].
- **Scheduled task** `daily-trends-4-platforms`, cron `0 8 * * *` (dispatches ~08:11). Report: `the-system-v5/O-output/daily-trends/YYYY-MM-DD.md`, Hebrew top-3 in chat.
- **Volume** (app.tryvolume.app, Reut signed up 2026-11-11, trial ended ~2026-11-14). MCP URL `https://app.tryvolume.app/api/mcp`, added by Reut as a custom connector in the Claude app. Its Library covers ONLY TikTok, Instagram and Meta ads. No LinkedIn organic posts and no X discovery. Its "Tech and AI" niche is consumer phone tips; builders must be found by keyword search. Trial = 50 social-tool calls total; Core = 1,000 library searches/day + 1,000 social calls/month.
- **X:** `T-tools/01-skills/scripts/x_trends.py` (Grok x_search, XAI_API_KEY). Grok may invent posts, so the report keeps only real status URLs.
- **LinkedIn:** reads today's report from [[project-linkedin-swipe-engine]]; never triggers Bright Data again.
