---
name: project-reddit-scout-pipeline
description: "/demand-radar — multi-source virality scanner (HN free + Reddit via Apify) telling Reut what Lior's audience cares about + why, for viral LinkedIn ideas"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4f9b708b-75ad-4fef-9a2f-233ececb6de9
---

Virality idea-engine for Lior, built 2026-06-27 (Reut wants to "go viral" — find what the audience cares about + WHY there's demand). e-commerce de-prioritized per Reut.

**Skill:** `/demand-radar` (`.claude/commands/demand-radar.md`). Multi-source: scans Hacker News + (Reddit via Apify if token) + X/Grok, clusters into demand THEMES, scores by cross-source recurrence + debate + recency, outputs ranked viral ideas each with "why there's demand" + archetype + hook + "vs." + the Lior proof to attach. Proposes only, never posts.

**Script:** `the-system-v5/T-tools/01-skills/scripts/demand_radar.py` — pulls HN (Algolia API, FREE, no auth, verified working 2026-06-27) + Reddit via Apify (optional, needs APIFY_TOKEN). Word-boundary keyword match, comments weighted (debate). `--json` for machine output.

**Why NOT Reddit directly (verified 2026-06-27 — do not re-attempt):** Reddit is fully walled off here. curl/scrape → 403; WebFetch → blocked; Reddit OAuth self-service → closed by Responsible Builder Policy (2026-06-05, manual approval only); WebSearch → Anthropic crawler blocked from reddit.com; Chrome MCP → reddit "not allowed". **Paying Reddit does NOT unlock it** (Premium ≠ API; official paid API is enterprise-tier). The practical paid unlock is a 3rd-party data provider — **Apify** (pay-as-you-go, ~cents/run): sign up at apify.com → API token → `export APIFY_TOKEN="..."` in ~/.zshrc. Apify actor/input may need a one-time tweak on first run.

**Cadence:** manual skill, run each morning. Not scheduled (cron unreliable — see [[project-scheduled-tasks-need-mac-awake]]). Complements `/scout` (X/Grok+RSS+HN for X posts) — demand-radar is the LinkedIn-virality lens. Related: the Top-12 playbook is the archetype target.

**First live run (2026-06-27)** surfaced the dominant demand theme: AI cost/efficiency + bubble anxiety (CNBC tokenmaxxing→efficiency + Lindy→DeepSeek; HN DSpark inference 683pts; "AI super bubble"; "AI burnout"). Validated the Hermes 10-min-swap post angle.
