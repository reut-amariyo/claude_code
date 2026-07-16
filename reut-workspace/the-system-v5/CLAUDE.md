# CLAUDE.md — the-system-v5 (ABC-TOM)

Written by Claude Fable 5 on 2026-07-07. Project-level rules only; vault-wide rules
live in the vault-root CLAUDE.md and are not repeated here.

## What this project is

Content operating system for Lior Pozin's personal brand. Reut learns, drafts,
measures, and iterates here. Git-backed: every file survives any platform switch.

## Map

- A-agents/ — role definitions (analyst, copywriter, scout, gatekeeper, TOM)
- B-brain/ — raw source material: Lior-Prompt.md, communication + content samples
- C-core/ — icp-profile.md, voice-dna.md, project-brief.md, api-keys-registry.md
- M-memory/ — decisions.md, feedback.md, learning-log.md (2,000+ lines of post analysis)
- O-output/ — every deliverable, organized by workstream
- T-tools/01-skills/ — skills + scripts/ (posting, mirroring, trial reels, transcription)

## Operating reality (as of July 2026)

- An external agency produces Lior's content (X confirmed). This system is the
  LEARNING layer: study what works so creation can resume if the agency ends.
  Do not proactively draft X posts unless Reut asks.
- Q3 2026 targets: 7M+ views/mo total, 190K+ followers. X and LinkedIn are the
  under-target platforms; prefer moves that help them.
- Platform priority: IG > LinkedIn > X > conferences.

## Lior brand — the non-negotiables

Archetype: Architect of Growth, never Motivator. Tagline: [ life is beta ].
Three pillars, every post hits at least one: (1) "I live on 200" as joy never
superiority, (2) loves 0→1, (3) focus.

- Personal founder journey, NEVER AutoDS product marketing. Vary the proof;
  don't name AutoDS in every reply.
- Team size is "250 employees", used only when central. NEVER "100 engineers" —
  the number is unverified.
- Lior is dyslexic. Never "I read / just finished a book". Podcasts, audiobooks, team summaries.
- No imposter syndrome, no disbelief lines, no fear confessions. Wins are earned
  outcomes; vulnerability means real past failures only.
- Never criticize Shopify. Never name Shopify as a potential AutoDS acquirer.
- His AI stack is Hermes Agent + OpenAI Codex since June 2026. Any workflow
  content must match it. Claude may appear only for direct terminal/desktop use.
- CEO relevance filter: would a SaaS CEO with 250 employees credibly say this?
  Kill CMO/creator/productivity-tip topics. Exception: a how-to framed as insider
  intel + operator confession + strategic close (the 93K MD→HTML post pattern).
- Every reply/comment needs a real Lior story with a specific number — unless the
  post asks a direct question; then just answer it genuinely.

## LinkedIn — leading reference

The Top 12 / 10K+ playbook wins over all older rules: 9 confirmed archetypes,
hooks under 10 words with a concrete anchor, always a "vs." in one sentence,
visuals only from the 4 families (third-party authority / personal artifact /
cultural meme / signed illustration) — never marketing-team graphics.
Mechanics: 750–1,200 chars, no arrow lists (→ killed three posts at ~800 imp),
no "Read that again" template phrases, leave an engagement gap open at the end.

### Pre-publish gate (mandatory before any go/no-go)

April 2026 shipped 10 failures out of 12 by skipping this. Audit every final
draft against: the non-negotiables above, the anti-AI rules in the vault-root
CLAUDE.md, archetype match, hook discipline, visual family, and the "vs." test.
Output a visible ✅/❌ table with a 🟢/🟡/🔴 verdict. Any hard-rule ❌ = do not
publish, no overrides.

## X

Operator archetype 70/20/10 (Operator/Builder/Contrarian), zero Educator lane.
Weekly mix: 2 story, 1 vulnerability, 1 midas, 1 conviction. Bookmarks ×3,
replies/reposts ×2, likes ×1. Reply targets: 200+ likes or 10K+ views,
SaaS/AI/startup only, never hardware/robotics/crypto. Prefix named companies
with @ and the exact handle.

## Pipelines & gotchas (hard-won, do not relearn)

- Performance data: O-output/x-performance-log/posts.jsonl. LinkedIn perf is logged
  daily via Chrome → Creator Analytics (the old Metricool JSONL was retired 2026-06-01).
- post_social.py has NO --help; arg1 is always live post text. Read the script, never
  run it to check usage.
- Bluesky auto-replies DISABLED 2026-07-09 (scout-reply-01..10 all off) — Reut wants
  only the X-post mirror on Bluesky. If replies ever resume: run find FIRST, copy
  uri/cid verbatim, never parallelize find+reply; the dedup log at
  ~/.scout-replies-bluesky-log.json silently drops entries — pull the full candidate
  pool and exclude ALL seen URIs.
- Metricool doesn't log X replies; missing entries ≠ broken pipeline.
- The 403 auto-blocker cannibalizes the X reply whitelist (12 of 18 blocked) — root
  cause of the reply drought.
- Scheduled tasks only run when the Mac is awake with the app open. "Didn't post
  today" = missed slot, not a bug; run /bluesky-mirror manually.
- Trial reels: /trial-reels renders 7 MP4s + captions; NEVER auto-post, Reut uploads
  manually. Stay out of TikFusion usage.
