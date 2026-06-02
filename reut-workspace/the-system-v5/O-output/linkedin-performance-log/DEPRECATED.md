# ⚠️ DEPRECATED — 2026-06-01

This directory (`posts.jsonl`) was a **second, redundant** LinkedIn performance
tracker fed by Metricool via `T-tools/01-skills/scripts/fetch_linkedin_performance.py`.

**It is retired.** It went stale (frozen 2026-05-03) because its advertised
`linkedin-analyst-daily` scheduled task was never created — it was an orphan.

## Canonical LinkedIn performance log
The live, authoritative log is the Markdown file, maintained daily by the
`lior-linkedin-daily-scan` scheduled task (Chrome scrape of Creator Analytics):

    ~/.claude/projects/-Users-reutamariyo-Documents-Obsidian-Vault/memory/lior-performance-log.md

`posts.jsonl` is kept here read-only for historical data only. Do not wire it
back into any automation without a deliberate decision to consolidate the two
systems.
