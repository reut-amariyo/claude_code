---
name: project-scheduled-tasks-need-mac-awake
description: Why scheduled tasks (bluesky-mirror etc.) silently miss runs — Mac must be awake + Claude Desktop open; no real cron
metadata: 
  node_type: memory
  type: project
  originSessionId: 4f9b708b-75ad-4fef-9a2f-233ececb6de9
---

All scheduled tasks (`bluesky-mirror`, scout-replies, analysts, etc.) run **inside the Claude for Desktop app**, NOT via macOS `launchd`/`cron`. There is no system cron job. A task fires only if, at its scheduled minute, (1) the Mac is awake AND (2) the Claude Desktop app is open. The app config shows `"wakeScheduler":{"status":"unavailable"}` — it cannot wake the Mac. The machine sleeps frequently (thousands of sleep/wake cycles), so most 2-hourly slots are silently missed.

**Symptom:** "I don't see posts on Threads/Bluesky today." `list_scheduled_tasks` shows the task `enabled` but `lastRunAt` days old, even though `nextRunAt` looks fine. This is NOT a code/config bug — the task is healthy.

**Why:** confirmed 2026-06-24 — `bluesky-mirror` (cron `0 8-22/2 * * *`) had lastRun stuck at Jun 14 while enabled. Only tasks whose slot landed while the Mac was awake ran.

**How to apply:** when a scheduled social task "didn't post," first check if it's a missed-slot issue (run it manually) before debugging scripts. Reut's chosen workaround (2026-06-24) is to **run `/bluesky-mirror` manually**, not change Mac sleep settings. The standalone-cron route is blocked because mirror DETECTION needs the Chrome MCP via the agent, not just the python script. Related: [[project-bluesky-mirror-pipeline]]
