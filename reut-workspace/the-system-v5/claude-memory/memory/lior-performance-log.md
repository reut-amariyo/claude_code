---
name: Lior LinkedIn Performance Log
description: Chronological log of every LinkedIn post Lior publishes, with metrics + post-hoc analysis. THE most important file for learning what actually works for Lior's audience.
type: project
originSessionId: 11cc6c8f-354d-4bc2-8669-8d3411421269
modified: 2026-08-09T07:58:03.862Z
---
# Lior LinkedIn Performance Log

**Purpose:** The patterns from other creators are hypotheses. Lior's own performance is the ground truth. Every post Lior publishes gets logged here, with metrics tracked at 24h, 72h, and 7d checkpoints.

**How to add:**
- **Automatic:** A daily scheduled task scans Lior's LinkedIn at 10:13 local, logs new posts, and updates metrics on existing posts.
- **Manual trigger:** `/lior-posted [URL]` when Lior publishes and we want an immediate lock-in.
- **One-off:** `/linkedin-learn` with a Lior post URL.

**How to use:** Before drafting a new post, scan Lior's top 5 and bottom 5 posts from this log. Our own data beats generic best practices.

### 2026-08-25 — Exit deck lead magnet (document carousel) — 23,111 imp ⭐

Hook: "Sold my business to Fiverr for $92M with this 47-slide deck. / (Now I'm open-sourcing it.)"
Format: native LinkedIn document, portrait 1080x1350, hook card + 9 section cards + close.
CTA: none. Link to the full 47-slide template in the first comment, "no need to comment for it".

**23,111 impressions, ~159 reactions, 17 comments, ~80 connection requests.**

**A/B against the killed version.** The identical copy ran 2026-08-24 with a comment-gate CTA
("Leave any comment & like the post / Add me in connections / I will send you the link in the
DM") and a single grid image: **55 impressions at 1h, 15 members reached, 78% in-network**, all 17
comments solicited directly by Reut. Deleted the same evening. One variable changed between them:
the gate. Full analysis: memory file lior-post-exit-deck-lead-magnet.md.

Read: the gate was the suppressor, not the topic, not the account. ~80 connection requests with no
ask is the follower-KPI headline, since a connection auto-follows.

## Benchmarks (defined 2026-04-18)

**The primary success metric is impressions.** Engagement (likes, comments, shares) is secondary but tracked.

| Impressions | Verdict |
|---|---|
| 5,000+ | ✅ Post worked |
| 2,500-5,000 | 🟡 Middling — diagnose what was off |
| Under 2,500 | 🔴 Didn't resonate — deep learning opportunity |

**Engagement standards (tracked alongside impressions):**
- Likes
- Comments
- Reshares
- Comments-to-likes ratio (high ratio = deep engagement, often predicts second-wave impressions)

**Rolling benchmarks** (auto-updated monthly by the daily scan):
- Lior's median impressions: TBD
- Lior's median engagement rate: TBD
- Lior's top 10% threshold: TBD

Until we have 10+ posts logged, we use absolute benchmarks above. After that, we shift to relative benchmarks (e.g., "top 20% of Lior's own posts").

---

## Log Format

```
### {YYYY-MM-DD} — {short title}
**Post URL:** {url}
**Topic tag:** #{tag}
**Hook type:** {category from hooks library}
**Structure:** {category from structures library}
**Visual:** {type from visuals library}
**Length:** {word count}
**CTA:** {type or "none"}

**Full post text:**
> {verbatim post}

**Metrics (at 24h):**
- Impressions: {N}
- Likes: {N}
- Comments: {N}
- Reshares: {N}
- Comments/likes ratio: {%}

**Metrics (at 72h):**
- Impressions: {N}
- Likes: {N}
- Comments: {N}
- Reshares: {N}

**Metrics (at 7 days — FINAL):**
- Impressions: {N} → **verdict: ✅ / 🟡 / 🔴** (5000+ = worked)
- Likes: {N}
- Comments: {N}
- Reshares: {N}
- Engagement rate: {%}

**Analysis:**
- What worked: {1-3 bullets}
- What didn't: {1-3 bullets}
- vs. Lior's baseline: {above/below average, by X%}
- vs. top-creator patterns: {did it match a known winning pattern? which?}

**Learnings applied going forward:** {1-2 sentences — what do we change based on this?}
```

---

## Scan Issues

| Date | Issue | Action |
|------|-------|--------|
| 2026-04-21 21:47 | Claude in Chrome not connected — Chrome extension unreachable. Could not navigate to LinkedIn profile or read posts. | Skipped scan. Will retry on next scheduled run. |
| 2026-04-23 10:13 | Claude in Chrome not connected — Chrome extension unreachable. Could not navigate to LinkedIn profile or read posts. | Skipped scan. Will retry on next scheduled run. |
| 2026-04-24 10:13 | Claude in Chrome not connected — Chrome extension unreachable. Could not navigate to LinkedIn profile or read posts. | Skipped scan. Will retry on next scheduled run. |
| 2026-04-25 10:13 | Claude in Chrome not connected — Chrome extension unreachable. Could not navigate to LinkedIn profile or read posts. | Skipped scan. Will retry on next scheduled run. |
| 2026-04-26 10:13 | Claude in Chrome not connected — Chrome extension unreachable. Could not navigate to LinkedIn profile or read posts. | Skipped scan. Will retry on next scheduled run. |
| 2026-04-27 (weekly digest) | Chrome extension not connected — 7th consecutive day. Weekly digest ran on web search only. Two Lior posts found via web search (Jensen Huang takeaways, 10-80-10 rule) but dates/metrics unconfirmed. Full digest at linkedin-digests/digest-2026-04-27.md | Chrome fix required. Notified Reut in Hebrew. |
| 2026-04-27 10:13 | Chrome reconnected — first successful scan after 7-day outage. Backfilled 5 most recent posts. Post URLs captured by date + first line (LinkedIn three-dot copy-link not batched in this run; will add in next scan via read_page data-urn). | Logged 5 posts. 30K-impression post (Paperclip AI agents) flagged exceptional. |
| 2026-04-28 10:13 | Chrome extension connected (browser listed) but `navigate` to LinkedIn timed out after 300s — twice. Underlying Chrome/CDP unresponsive. Could not load profile or read posts. | Skipped scan. Modball post (2026-04-24) is now ~4 days old; 7d checkpoint due 2026-05-01 — must capture in next successful scan. |
| 2026-04-30 10:13 | Chrome extension connected; LinkedIn tab loaded (title "Activity \| Lior Pozin"); but `get_page_text` failed mid-operation ("Chrome extension disconnected"). Retry tab was closed by user (active browser session). Could not read posts. | Skipped scan. Pending checkpoints: Modball 7d (2026-05-01), "I got rejected" 72h (2026-05-01) and 7d (2026-05-05), Wim Hof sequel 72h (2026-05-01) and 7d (2026-05-05). |
| 2026-05-01 10:13 | Successful scan. Read 5 posts from activity page. New post (find-skills, 2026-04-30) logged. 3 checkpoints locked: Modball 7d FINAL (🔴 2,070), "I got rejected" 72h (1,660), Wim Hof sequel 72h (1,795). Cold feet refresh captured. Post URLs still TBD (didn't extract individual permalinks this run). | All checkpoints captured. No exceptional/bombed posts triggering notification. |
| 2026-05-02 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty. Could not navigate to LinkedIn or read posts. | Skipped scan. Pending: find-skills 72h checkpoint (due 2026-05-03), find-skills 7d FINAL (due 2026-05-07), "I got rejected" 7d FINAL (due 2026-05-05), Wim Hof sequel 7d FINAL (due 2026-05-05). |
| 2026-05-03 10:13 | Successful scan after multiple Chrome reconnect retries (extension dropped twice during the run, recovered). Activity page read; 5 most recent posts re-checked. find-skills 72h LOCKED (639 imp, projects 🔴 at 7d). "I got rejected" and Wim Hof sequel intermediate refreshes captured (both 5-day mark, 7d FINAL due 2026-05-05). Modball post still slowly accruing past 7d lock. No new posts since 2026-04-30 — Lior hasn't published in 3 days. | All pending checkpoints either locked or progressing to schedule. No notification triggers met. |
| 2026-05-04 (weekly digest run) | Successful Lior scan + 4 of 11 inspiration creators (Hormozi, Welsh, Martell, Bartlett) before Chrome timed out on Matt Gray + remaining creators. Got 25+ posts at 1000+ reactions for analysis. New Lior post detected and logged: PocketOS / Jeremy Crane / "How does the worst mistake of your career become a personal brand win?" (2026-05-04, 16h post). Refresh metrics on find-skills (714 imp), Wim Hof sequel (1,892 imp at ~7d → 🔴 final), "I got rejected" (1,925 imp at ~7d → 🔴 final). Full digest at linkedin-digests/digest-2026-05-04.md | 2 posts hit 7d FINAL: Wim Hof sequel 🔴 (1,892), I got rejected 🔴 (1,925). New post logged. Notified Reut. Chrome failure on 7 creators noted in Gaps. |
| 2026-05-04 daily scan (later run, ~10:13) | Successful scan. Activity page read; 5 posts visible. No new posts since 2026-05-04 morning run. Refreshed metrics: PocketOS at 18h (721→769 imp, 9→10 likes, 2 comments, 1 self-repost). find-skills at ~4d (714→722 imp, 9 likes, 1 comment — basically stalled). "I got rejected" post-FINAL refresh (1,925→1,941 imp, 55→56 likes, 1 comment, 4 reposts). Wim Hof sequel post-FINAL refresh (1,892→1,899 imp, 43 likes, 0 comments). | All metrics updated. No checkpoints crossed today. No notification triggers met (nothing exceptional, nothing under 1,500 newly). |
| 2026-05-05 10:13 | Successful scan after Chrome reconnect retry (extension dropped twice during early steps, recovered). Activity page read; 5 posts visible. **NEW post detected and logged: 2026-05-05 "Coffee in Manhattan / 100 videos in 100 days" / YouTube origin story (17h post, 1,062 imp / 19 likes / 2 comments / 1 self-repost already deployed).** PocketOS 24h LOCKED (1,029 imp, 11 likes, 2 comments, self-repost no longer visible in feed view). find-skills at ~5d (722→746 imp, 9 likes, 1 comment — fully stalled, projecting 🔴 at 7d). "I got rejected" TRUE 7d at 2,066 imp (post had been pre-locked at 1,925 on 2026-05-04 6d, today is the actual 7d mark — ticked up to 2,066, still 🔴). | New post logged. 1 checkpoint at TRUE 7d. No exceptional/bombed verdicts to notify on. Silent completion. |
| 2026-05-06 10:13 | Chrome extension listed as connected but BOTH `get_page_text` and `navigate` timed out after 300s each (mid-operation extension drop, then post-reconnect navigate stuck on CDP). Tab title showed "Activity \| Lior Pozin" so the page had at least partially loaded earlier in the session — but no readable text retrieved. Could not refresh metrics or detect new posts. | Skipped scan. Pending checkpoints: Coffee/100-videos 24h (due 2026-05-06 — TODAY, missed), PocketOS 72h (due 2026-05-07), find-skills 7d FINAL (due 2026-05-07), Coffee/100-videos 72h (due 2026-05-08), PocketOS 7d FINAL (due 2026-05-11), Coffee/100-videos 7d FINAL (due 2026-05-12). Will retry on next scheduled run. |
| 2026-05-07 10:13 | Successful scan after one `get_page_text` timeout retry. Activity page read; 9 posts visible. **2 NEW posts detected and logged: 2026-05-06 "Founder salary trap / Pay yourself enough to think straight" (17h, 1,861 imp / 19 likes / 0 comments / 1 self-repost — strong early velocity) and 2026-05-06 "LangTalks AI Engineering Conference recap" (~1d, 486 imp / 7 likes / 1 comment).** find-skills 7d FINAL LOCKED at 792 imp → 🔴 BOMBED (<1,500 → Hebrew notification triggered). PocketOS 72h LOCKED (1,166 imp / 14 likes / 2 comments). Coffee/100-videos 48h refresh (1,954 imp / 29 likes / 7 comments — picking up speed). Post-FINAL refreshes captured for "I got rejected" (2,264), Wim Hof sequel (2,006), Modball (2,277). | All checkpoints captured. find-skills bomb notification sent in Hebrew. New posts logged. |
| 2026-05-08 10:13 | Chrome extension was listed as connected at scan start (Browser 1, macOS, isLocal=true), tab created. First `navigate` call to LinkedIn dropped the extension mid-operation. `list_connected_browsers` returned empty across multiple retries (8s, then attempted longer wait — blocked by sleep guard). Could not load profile, read posts, or refresh metrics. | Skipped scan. Pending checkpoints missed today: Coffee/100-videos 72h (due 2026-05-08) and Founder salary trap 24h (due 2026-05-08). Will retry next scheduled run. PocketOS 7d FINAL still due 2026-05-11; Coffee 7d FINAL due 2026-05-12; Founder salary 7d FINAL due 2026-05-13; LangTalks 7d FINAL due 2026-05-13. |
| 2026-05-10 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. Pending checkpoints missed: Coffee/100-videos 72h (overdue from 2026-05-08), Founder salary trap 24h (overdue from 2026-05-08), LangTalks 72h (due 2026-05-09 — missed). Upcoming: PocketOS 7d FINAL (due 2026-05-11), Coffee 7d FINAL (due 2026-05-12), Founder salary 7d FINAL (due 2026-05-13), LangTalks 7d FINAL (due 2026-05-13). 3rd consecutive scan failure (2026-05-08, 2026-05-09 not run, 2026-05-10). Will retry next scheduled run. |
| 2026-05-11 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **PocketOS 7d FINAL was due TODAY and was missed** — currently held at 24h LOCK (1,029 imp from 2026-05-05); the true 7d value will have to be back-captured on next successful scan and flagged as post-window lock. Still-pending: Coffee/100-videos 72h (overdue since 2026-05-08), Founder salary trap 24h (overdue since 2026-05-08), LangTalks 72h (overdue since 2026-05-09). Upcoming: Coffee 7d FINAL (due 2026-05-12), Founder salary 7d FINAL (due 2026-05-13), LangTalks 7d FINAL (due 2026-05-13). 4th consecutive scan failure (2026-05-08, 2026-05-10, 2026-05-11 — 2026-05-09 not run). Chrome reconnect required before next scheduled run. |
| 2026-05-12 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **Coffee/100-videos 7d FINAL was due TODAY and was missed** — currently held at 48h refresh (1,954 imp from 2026-05-07); the true 7d value will have to be back-captured on next successful scan and flagged as post-window lock. Still-pending: PocketOS 7d FINAL (overdue from 2026-05-11, still at 24h LOCK 1,029), Coffee/100-videos 72h (overdue since 2026-05-08), Founder salary trap 24h (overdue since 2026-05-08), LangTalks 72h (overdue since 2026-05-09). Upcoming: Founder salary 7d FINAL (due 2026-05-13), LangTalks 7d FINAL (due 2026-05-13). 5th consecutive scan failure (2026-05-08, 2026-05-10, 2026-05-11, 2026-05-12 — 2026-05-09 not run). Chrome reconnect required before next scheduled run. |
| 2026-05-13 10:13 | Chrome extension not reachable — `tabs_context_mcp` returned "Claude in Chrome is not connected" at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **TWO 7d FINALs due TODAY and missed: Founder salary trap (held at 17h, 1,861 imp from 2026-05-07) and LangTalks recap (held at ~1d, 486 imp from 2026-05-07)** — both will need post-window back-capture on next successful scan. Still-pending: PocketOS 7d FINAL (overdue from 2026-05-11, still at 24h LOCK 1,029), Coffee/100-videos 7d FINAL (overdue from 2026-05-12, held at 48h 1,954), Coffee 72h (overdue since 2026-05-08), Founder salary 24h (overdue since 2026-05-08), LangTalks 72h (overdue since 2026-05-09). 6th consecutive scan failure (2026-05-08, 2026-05-10, 2026-05-11, 2026-05-12, 2026-05-13 — 2026-05-09 not run). Chrome reconnect required before next scheduled run. |
| 2026-05-14 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **All 4 pending 7d FINALs remain back-capture targets** (PocketOS overdue from 2026-05-11 at 1,029 imp; Coffee/100-videos overdue from 2026-05-12 at 1,954 imp; Founder salary trap overdue from 2026-05-13 at 1,861 imp; LangTalks recap overdue from 2026-05-13 at 486 imp). Still-pending intermediate checkpoints: Coffee 72h (overdue since 2026-05-08), Founder salary 24h (overdue since 2026-05-08), LangTalks 72h (overdue since 2026-05-09). 7th consecutive scan failure (2026-05-08, 2026-05-10, 2026-05-11, 2026-05-12, 2026-05-13, 2026-05-14 — 2026-05-09 not run). **One week of Chrome outage — Reut needs to reconnect Chrome extension manually before any further scans can run.** |
| 2026-05-15 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **All 4 pending 7d FINALs remain back-capture targets** (PocketOS overdue from 2026-05-11 at 1,029 imp; Coffee/100-videos overdue from 2026-05-12 at 1,954 imp; Founder salary trap overdue from 2026-05-13 at 1,861 imp; LangTalks recap overdue from 2026-05-13 at 486 imp — all now well past 7d, will be post-window back-captures only). Still-pending intermediate checkpoints (all stale): Coffee 72h (overdue since 2026-05-08), Founder salary 24h (overdue since 2026-05-08), LangTalks 72h (overdue since 2026-05-09). 8th consecutive scan failure (2026-05-08, 2026-05-10, 2026-05-11, 2026-05-12, 2026-05-13, 2026-05-14, 2026-05-15 — 2026-05-09 not run). **8 days of Chrome outage. Also: no scan since 2026-05-07 means any new posts published 2026-05-08 through 2026-05-15 are not yet logged.** Chrome reconnect required before any further scans can run. |
| 2026-05-17 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **All 4 pending 7d FINALs remain back-capture targets only** (PocketOS at 1,029 imp from 2026-05-05; Coffee/100-videos at 1,954 imp from 2026-05-07; Founder salary trap at 1,861 imp from 2026-05-07; LangTalks recap at 486 imp from 2026-05-07). 9th consecutive scan failure (2026-05-08, 2026-05-10 through 2026-05-15, 2026-05-17 — 2026-05-09 and 2026-05-16 not run). **10 days since last successful scan (2026-05-07). All new posts published 2026-05-08 onward are unlogged.** Chrome reconnect required before any further scans can run. |
| 2026-05-18 10:13 | Chrome extension not connected — `list_connected_browsers` returned empty at scan start. Could not navigate to LinkedIn or read posts. | Skipped scan. **All 4 pending 7d FINALs still back-capture targets only** (PocketOS at 1,029 imp from 2026-05-05; Coffee/100-videos at 1,954 imp from 2026-05-07; Founder salary trap at 1,861 imp from 2026-05-07; LangTalks recap at 486 imp from 2026-05-07). 10th consecutive scan failure (2026-05-08, 2026-05-10 through 2026-05-15, 2026-05-17, 2026-05-18 — 2026-05-09 and 2026-05-16 not run). **11 days since last successful scan (2026-05-07). All new posts published 2026-05-08 onward remain unlogged.** Chrome reconnect required before any further scans can run. |
| 2026-05-18 weekly digest | Chrome down 11d. WebFetch attempted on all 11 creators + Lior — only Justin Welsh leaked through (7 posts at 1000+ reactions, exceptional weekly throughput). All other creators returned HTTP 999. Lior's activity page returned login wall via WebFetch — no fresh metrics. Digest written at linkedin-digests/digest-2026-05-18.md with degraded-data flag. 1 new style guide proposal (aphorism-only experimental lane) added on top of 2 pending from prior digest. | Notified Reut in Hebrew. **Chrome reconnect remains the single blocking issue.** |
| 2026-05-19 weekly digest (Chrome RECONNECTED) | Reut reconnected Chrome mid-conversation. Full scan completed. **5 new Lior posts logged (2026-05-10 Anthropic 92,869 imp ⭐⭐ NEW ALL-TIME RECORD; 2026-05-12 Master Prompt 516 imp 🔴; 2026-05-14 Treat-yourself 403 imp 🔴; 2026-05-18 Funnel 1,728 imp @ 7h).** Founder Salary trap back-captured at 7d-post-window: 4,614 imp 🟡. **PocketOS/Coffee/LangTalks 7d FINALs still unavailable** (LinkedIn analytics page returns "Trouble Loading" for those 13-14d old URNs). All 11 creators successfully scanned via JS extraction on activity pages. Top creator post: Will Ahmed WHOOP x Red Sox at 6,414 reactions. Digest rewritten at linkedin-digests/digest-2026-05-19.md (replaces digest-2026-05-18.md as the canonical week-of file). | Lior's Anthropic post is the headline finding — 92K imp is 3x Paperclip's prior ceiling. Lane (contrarian-AI-trending-tool) now confirmed n=2 repeatable winning pattern. |
| 2026-05-20 10:13 | Successful scan (Chrome stable, 2nd good run since reconnect). Activity feed read top-down. **No new posts since 2026-05-18 Funnel — Funnel remains the newest post, so nothing new to log.** Refreshes captured: Funnel ~42h (2,793 imp / 65 react / 11 comm / 9 reposts), Treat-yourself ~6d (472 imp / 11 react / 1 comm — 7d FINAL due 2026-05-21, verdict locked-in 🔴), Anthropic ~10d (92,898 imp, record stable). Followers now 9,432. **Back-capture targets (PocketOS / Coffee/100-videos / LangTalks 7d FINALs) still unreachable** — the activity-feed lazy-load stalls into blank space just past the Anthropic post, so the 14-16d-old posts won't render inline (inline impressions would have bypassed the analytics-page "Trouble Loading" issue, but the posts never load). Holding last-known values as de-facto finals: PocketOS 1,029, Coffee 1,954, LangTalks 486. | No 7d crossings today (Treat-yourself 7d is tomorrow). No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. |
| 2026-05-25 weekly digest | Chrome connected — full scan completed. **NEW Lior post logged: 2026-05-24 "Sold AutoDS to Fiverr at 28 / Turning 31 today / 10 lessons" milestone — 8,858 imp @ 16h / 102 react / 4 comm / 1 repost → tracking ✅ WINNER (first ✅-trajectory non-AI post; credential-flex + listicle lane).** Funnel-conversion-40% 7d FINAL LOCKED at 3,352 imp → 🟡 (74 react / 11 comm / 9 reposts). CEO-job-3-rules ~4d refresh (1,925 imp / 8 react / 3 comm — tracking 🔴). Treat-yourself long-tail 554, Master Prompt long-tail 567 (both 🔴 FINAL, unchanged). All 11 inspiration creators scanned via JS extraction. 6 creators had ZERO 1000+ posts this week (Dan Martell, Gary V, Matt Gray, Dan Koe, Guillermo Rauch, Tyler Denk). Top creator post: Steven Bartlett "I'M HIRING ANYONE" at 21,355 react. Digest at linkedin-digests/digest-2026-05-25.md. | Birthday post is the headline finding — strong ✅ candidate, NON-AI lane. Notified Reut in Hebrew. |
| 2026-05-25 10:13 daily scan | Successful scan (Chrome stable, ran ~1h after today's weekly digest). Activity feed read; impressions captured inline via `find` (no per-post analytics navigation needed). **No new posts since 2026-05-24 birthday/milestone — it remains the newest, nothing new to log.** Refreshes: Birthday "31/10 lessons" ~17h (9,621 imp / 112 react / 4 comm / 2 reposts — self-repost now deployed; tracking ✅ WINNER strongly, ~2x the 5K floor pre-24h); CEO-job-3-rules ~4d (1,937 imp / 8 react / 3 comm — stalled, holds 🔴); Funnel-conversion post-FINAL long-tail (3,368, +16, 🟡 unchanged); Treat-yourself long-tail (558, +4, 🔴 unchanged). Followers 9,501. | No 7d crossings today (Birthday 24h is 2026-05-26; CEO 7d is 2026-05-28). No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. |
| 2026-05-19 10:13 daily scan | Successful scan after weekly digest backfill yesterday. Activity page read; 5 most recent posts visible. **No new posts since 2026-05-18 Funnel — Lior hasn't published since yesterday afternoon.** Refreshed metrics on all 5 visible posts: Funnel at ~18h (2,182 imp / 56 reactions / 9 comments / 9 reposts — strong velocity past first day, projects 🟡 floor); Treat-yourself at ~5d (425 imp / 10 reactions / 0 comments — basically dead, holds 🔴); **Master Prompt at TRUE 7d FINAL today (520 imp / 9 reactions / 0 comments / 0 reposts → 🔴 BOMBED locked, +4 imp since yesterday's pre-7d snapshot);** Anthropic at ~9d (92,874 imp / 56 reactions / 24 comments — basically locked, +5 imp); Founder Salary trap at ~13d (4,634 imp / 31 reactions / 4 comments / 1 repost — marginal +20 imp accrual past 7d window). Follower count: 9,408. | Master Prompt TRUE 7d FINAL locked at 520 — Hebrew bombed notification already sent in yesterday's weekly digest run (post was diagnosed at 516 imp), so today's re-lock is a silent re-confirmation only. No new notification triggers met. |
| 2026-05-26 10:13 daily scan | Successful scan (Chrome stable). Activity feed read; 5 most recent posts visible with inline impressions. **No new posts since 2026-05-24 birthday/milestone — it remains the newest, nothing new to log.** **Birthday "31 / 10 lessons" 24h LOCKED at 15,366 imp / 167 react / 7 comm / 1 repost → tracking ⭐ EXCEPTIONAL pre-7d (already past >15K trigger AT 24H — first non-AI-lane post to cross this threshold in any window).** Velocity ACCELERATED into 24h (+5,745 imp / +55 react in the 7h between yesterday's 17h read and today's 24h lock). Refreshes: CEO-job-3-rules ~5d (2,009 imp / 8 react / 3 comm — engagement frozen for 2 days, holds 🔴 trajectory, 7d FINAL due 2026-05-28); Funnel long-tail ~8d (3,467 imp / 74 react / 11 comm / 9 reposts — +99 since 2026-05-25, 🟡 unchanged); Treat-yourself long-tail ~12d (572 imp / 13 react / 2 comm — +14, 🔴 unchanged, still log's worst); Master Prompt long-tail ~14d (602 imp / 9 react / 0 comm — +56, 🔴 unchanged). | Birthday post is the headline finding — but per task rules notifications fire only on 7d EXCEPTIONAL/BOMBED crossings. Birthday is at 24h, not 7d → silent completion. Flag for Monday digest as strong ⭐ candidate + potential first non-AI repeatable winning lane (credential-anchored milestone reflection). |
| 2026-05-27 10:13 daily scan | Successful scan (Chrome stable). Activity feed read top-down; 5 most recent posts visible with inline impressions (post #1 in feed is Lior's self-repost of post #2 — same content). **NEW post detected and logged: 2026-05-26 ~17h "Microsoft + Anthropic AI agents workshop / MCP / Foundry" (435 imp @ 17h / 8 react / 1 comm / 1 self-repost) — contrarian-AI lane (same DNA as Paperclip/Anthropic mega-winners) but tactical-prescription body, soft velocity start; tracking 🔴/🟡 borderline.** Birthday "31 / 10 lessons" 72h LOCKED at 16,686 imp / 187 react / 8 comm / 1 repost → still tracking ⭐ EXCEPTIONAL (well past >15K trigger; velocity flattened hard after 24h: only +1,320 imp in the 48h between 24h LOCK and 72h LOCK — the post is reach-capped). Refreshes: CEO-job-3-rules ~6d (2,058 imp / 9 react / 3 comm — +49 imp / +1 react in 24h, holds 🔴 trajectory; 7d FINAL due TOMORROW 2026-05-28); Funnel-conversion long-tail ~9d (3,528 imp / 75 react / 11 comm / 9 reposts — +61, 🟡 unchanged). Treat-yourself and Master Prompt aged off the activity-feed top-5 window (no fresh long-tail this run). | New post logged. 72h Birthday LOCK captured. No 7d FINAL crossings today (CEO 7d is tomorrow). No notification triggers met → silent completion. |
| 2026-05-28 10:13 daily scan | Successful scan (Chrome stable). Activity feed read top-down; 5 most recent posts visible inline (post #1 is Lior's self-repost of post #2 — same content). **NEW post detected and logged: 2026-05-27 ~17h "Google just dropped a Base44 killer / AI Studio for Android / narrow your niche" — 22,646 imp @ 17h / 66 react / 8 comm / 1 self-repost → tracking ⭐⭐ EXCEPTIONAL pre-24h, well past the >15K trigger AT 17H (2nd-fastest 17h read in the log behind Anthropic 92K).** CEO-job-3-rules 7d FINAL LOCKED at 2,083 imp / 9 react / 3 comm / 0 reshares → 🔴 verdict (under 2,500 floor, but above 1,500 → no bomb notification triggered). Birthday "31 / 10 lessons" ~3.5d refresh (17,298 imp / 192 react / 8 comm / 1 repost — +612 imp / +5 react / 0 comm since 72h LOCK; engagement curve flattened but reach still creeping up, tracking ⭐ EXCEPTIONAL toward 7d FINAL due 2026-05-31). Microsoft+Anthropic agents workshop 24h refresh (887 imp / 10 react / 1 comm / 0 reshares visible — +452 imp / +2 react / 0 comm in 24h; tracking 🔴 trajectory, 7d FINAL due 2026-06-02). Funnel-conversion and Treat-yourself/Master Prompt aged off the top-5 view this run. | New ⭐⭐ candidate logged. CEO 3-rules 7d FINAL locked 🔴 (no bomb threshold met). No 7d EXCEPTIONAL/BOMBED crossings today → silent completion. **Flag for Monday digest: Google/Base44-killer is the strongest 17h velocity since Anthropic 92K, ⭐⭐ candidate; first AI-lane post pairing trending-tool news anchor with personal founder-fear framing ("giants ship your roadmap").** |
| 2026-05-29 10:13 daily scan | Successful scan (Chrome stable). Activity feed read top-down; 5 most recent posts visible inline with impressions. **NEW post detected and logged: 2026-05-28 ~18h "Tough days for Israeli tech / Wix Meta Oracle Cisco / DMs are open" — 10,969 imp @ 18h / 195 react / 14 comm / 14 reposts → tracking ⭐ EXCEPTIONAL pre-24h (already 2x the 5K ✅ floor; the 14-repost count at 18h is the highest reshare velocity in the log). Hybrid lane: market-empathy hook + hiring CTA, but cleanly separated (not bait-and-switch like "I got rejected").** **Google/Base44-killer 24h LOCKED at 113,821 imp / 167 react / 35 comm / 1 repost → ⭐⭐⭐ NEW ALL-TIME RECORD, surpassing Anthropic (92,959) by ~21K. +91,175 imp in the 7h between 17h reading (22,646) and 24h lock — fastest acceleration in log history.** Microsoft+Anthropic agents workshop ~48h refresh (1,003 imp / 11 react / 1 comm — +116 imp / +1 react in 24h, fully stalled, locks 🔴 trajectory for 7d FINAL). Birthday "31 / 10 lessons" ~4d refresh (17,653 imp / 197 react / 9 comm / 1 repost — +355 imp / +5 react / +1 comm in 24h, slow reach creep, tracking ⭐ EXCEPTIONAL for 7d FINAL due 2026-05-31). CEO-job-3-rules long-tail (2,099 imp / 9 react / 3 comm — +16 imp post-7d-FINAL, residual only, 🔴 unchanged). | **Two notification-worthy events: (1) Google/Base44-killer is a NEW ALL-TIME RECORD at 24h LOCK. (2) Tough-days-Israeli-tech is tracking ⭐ EXCEPTIONAL at 18h. Both pre-7d, but record-breaker warrants Hebrew notification per spirit of task rules.** |
| 2026-05-31 10:13 daily scan | Successful scan after a rocky start (Chrome listed as connected but the prior session's tab group was lost; first JS-extraction attempts threw "Maximum call stack size exceeded" via the extension's MutationObserver — recovered by creating a fresh tab group and switching from `.innerText` to `.textContent` reads, which don't force reflow). Activity feed read top-down; 12 posts loaded. Post #1 = Lior's self-repost of the Tough-days post (1,653 imp on the repost object, ~1d old). **NO new original posts since 2026-05-28 Tough-days — it remains the newest.** **Birthday "31 / 10 lessons" 7d FINAL LOCKED at 18,009 imp / 199 react / 10 comm / 1 repost → ⭐ EXCEPTIONAL (>15K trigger met; FIRST non-AI-lane post to reach 7d EXCEPTIONAL in the log). Reach-capped hard after 24h — only +2,643 imp across days 1→7.** (All values from content-matched DOM reads — earlier index-based reads in this same run were unreliable due to feed re-indexing between calls; matched-by-post-text reads are authoritative.) Refreshes: Google/Base44-killer ~4d (**144,070 imp** / 188 react / 39 comm / 1 repost — +30,249 imp since 24h LOCK, still climbing hard, engagement flat = classic mega-reach shape; ⭐⭐⭐ all-time record extends, 7d FINAL due 2026-06-03); Tough-days-Israeli-tech ~2.5d (**13,400 imp** / 231 react / 21 comm / **15 reposts** — +2,431 imp / +36 react / +1 repost since 18h; 15 reposts is the highest reshare count in the log; tracking strong ✅/⭐, just under the 15K EXCEPTIONAL line, 7d FINAL due 2026-06-04); Microsoft+Anthropic agents workshop ~4.5d (1,112 imp — +109 since 48h, still 🔴, 7d FINAL due 2026-06-02); CEO-job-3-rules ~1w long-tail (2,119 imp / 9 react / 3 comm, +20 residual, 🔴 unchanged). | **Birthday 7d FINAL crossed at ⭐ EXCEPTIONAL (18,009 imp) → Hebrew notification sent.** Two more big posts in flight (Google/Base44 144K @ ~4d ⭐⭐⭐, Tough-days 13.4K @ ~2.5d tracking ⭐) — both pre-7d, no new notification. Next 7d FINALs: MS+Anthropic 2026-06-02 (🔴), Google/Base44 2026-06-03, Tough-days 2026-06-04. |
| 2026-06-01 10:13 daily scan | Successful scan (Chrome stable, ran shortly after today's weekly digest). Activity feed read top-down via `textContent` JS extraction; impressions captured inline (no per-post analytics navigation). **No new posts since 2026-05-28 Tough-days — it remains the newest ("3 days ago"), nothing new to log.** Refreshes: **Google/Base44-killer ~4.5d (145,479 imp / 192 react / 39 comm / 1 repost — +1,409 imp since 144,070 on 2026-05-31, still climbing, ⭐⭐⭐ all-time record holds, 7d FINAL due 2026-06-03);** Tough-days-Israeli-tech ~3.5d (13,975 imp / 234 react / 21 comm / **15 reposts** — +575 imp / +3 react since 2026-05-31; 15 reposts remains highest reshare count in log; tracking ⭐/✅, still under the 15K EXCEPTIONAL line, 7d FINAL due 2026-06-04); Birthday "31/10 lessons" post-FINAL long-tail (18,171 imp / 198 react / 10 comm / 1 repost — +162 imp residual past 7d FINAL lock of 18,009 ⭐); MS+Anthropic agents workshop ~5.5d (1,164 imp / 11 react / 1 comm — +52 imp since 2026-05-31, fully stalled, 🔴, 7d FINAL due TOMORROW 2026-06-02); CEO-job-3-rules ~1w long-tail (2,132 imp / 9 react / 3 comm — +13 residual, 🔴 FINAL unchanged). | No 7d FINAL crossings today (MS+Anthropic 7d is 2026-06-02; Google 2026-06-03; Tough-days 2026-06-04). No new posts. No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. |
| 2026-06-01 weekly digest | **Full scan — Chrome stable, all 11 inspiration creators read via JS extraction (first clean full-creator run since 2026-05-25).** 15 qualifying posts (1000+ react, ≤7d) across 7 creators; 4 creators ZERO (Dan Martell [activity hidden], Simon Beard, Dan Koe, Guillermo Rauch). Top creator post: Steven Bartlett bunkbed-childhood-origin 11,960 react / 799 reposts. Justin Welsh 5 posts, Hormozi 4, Bartlett 2. **No new Lior posts since 2026-05-28 Tough-days** — digest covers the 3 in-flight posts (Google/Base44 144K ⭐⭐⭐, Tough-days 13.4K ⭐, MS+Anthropic 1,112 🔴) + Birthday 7d FINAL (18,009 ⭐, locked 2026-05-31). Digest at linkedin-digests/digest-2026-06-01.md. Libraries (hooks/structures/visuals) updated with week-of observations. Date-filter false positive corrected (Bartlett "2mo" → excluded). | Best week in log history (record + most-reshared post both this window). 2 style-guide proposals pending Reut's Hebrew approval (contrarian-AI lane rule + hiring-as-gift rule). Notified Reut in Hebrew. |
| 2026-06-02 10:13 daily scan | Successful scan (Chrome stable, `textContent` JS extraction; impressions read inline from each post's "N impressions View analytics" element). Activity feed read top-down; 5 posts visible (post #1 = Lior's self-repost of post #2 = the new YouTube post). **NEW post detected and logged: 2026-06-01 ~17h "We just hit 400K subscribers on YouTube / 100 videos in 100 days / 70% rule + hardest hire (Liran Zablo)" — 1,109 imp @ 17h / 33 react / 7 comm / 1 self-repost. Credential-milestone + delegation-story lane; soft 17h velocity (well below Birthday 9,621 / Tough-days 10,969 at equivalent checkpoint), tracking 🔴/🟡 borderline.** **Microsoft+Anthropic agents workshop 7d FINAL LOCKED at 1,175 imp / 11 react / 1 comm / 0 reshares → 🔴 BOMBED (<1,500 → Hebrew notification triggered). Confirms: AI-trending topic with tactical-prescription body bombs even when the hook names Microsoft + Anthropic.** Refreshes: Google/Base44-killer ~5.5d (**146,096 imp** / 195 react / 39 comm / 1 repost — +2,026 since 145,479 on 2026-06-01, still creeping up, ⭐⭐⭐ all-time record holds, 7d FINAL due TOMORROW 2026-06-03); Tough-days-Israeli-tech ~4.5d (**14,341 imp** / 238 react / 22 comm / **15 reposts** — +366 since 13,975 on 2026-06-01, tracking ⭐/✅ just under the 15K EXCEPTIONAL line, 7d FINAL due 2026-06-04). Birthday/CEO-3-rules/Funnel aged off the top-5 view this run (no fresh long-tail). | **MS+Anthropic 7d FINAL crossed at 🔴 BOMBED (1,175 imp) → Hebrew notification sent.** New YouTube-400K post logged. Two big posts still in flight (Google/Base44 146K @ ~5.5d ⭐⭐⭐, Tough-days 14.3K @ ~4.5d ⭐/✅) — both pre-7d. Next 7d FINALs: Google/Base44 2026-06-03, Tough-days 2026-06-04. |
| 2026-06-03 10:13 daily scan | Successful scan (Chrome stable, `textContent` JS extraction; impressions + social counts read inline; **post URLs captured this run via `data-urn`**). Activity feed read top-down; 5 posts visible (post #1 = Lior's self-repost of post #2 = the new layoffs post). **NEW post detected and logged: 2026-06-02 ~17h "34,454 tech workers laid off to AI / 8 things I'd tell a friend who got laid off" — 1,537 imp @ 17h / 13 react / 10 comm / 1 self-repost. Layoff/market-empathy lane (same topic as Tough-days ⭐) but recast as a generic advice-listicle with NO named companies and NO hiring offer; soft 17h velocity (Tough-days was 10,969 @ 18h on the same theme), but exceptional comments-to-reactions ratio (10:13 ≈ 77%). Tracking 🔴/🟡 borderline.** Refreshes: **Google/Base44-killer ~6.7d (146,385 imp / 196 react / 39 comm / 1 repost — +289 since 146,096 on 2026-06-02, reach fully plateaued; ⭐⭐⭐ all-time record holds; true 7d crosses this evening ~17h so 7d FINAL locks on tomorrow's run; record already notified 2026-05-29). URL: urn:li:activity:7465400833464000512;** Tough-days-Israeli-tech ~5.7d (**14,511 imp** / 240 react / 22 comm / **15 reposts** — +170 since 14,341; tracking ⭐/✅ just under the 15K EXCEPTIONAL line; 7d FINAL due TOMORROW 2026-06-04. URL: urn:li:activity:7465756982331891713); YouTube-400K milestone ~1.5d / **24h LOCK** (1,394 imp / 44 react / 7 comm / 1 self-repost — +285 imp / +11 react since 17h; reactions healthy but reach soft, tracking 🔴/🟡; 72h due 2026-06-04, 7d FINAL 2026-06-08. URL: urn:li:activity:7467205850911305728). | New post logged with URL. YouTube-400K 24h LOCK captured. No 7d FINAL crossings today (Google's true 7d is this evening → lock tomorrow). No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. |
| 2026-06-04 10:13 daily scan | Successful scan (Chrome stable, `textContent` JS extraction; impressions read inline via `/([\d,]+)\s+impressions/` regex on each post's textContent; URLs from `data-urn`). Activity feed read top-down; 5 distinct posts (post #1 = Lior's self-repost of the layoffs post). **NEW post detected and logged: 2026-06-04 ~1-2h "Let me just try one more prompt / 900 prompts later" — 363 imp / 6 react / 0 comm. Vibe-coding/AI-build humor; caption-only-hook with the payoff carried in the attached visual (a new format for the log). URL: urn:li:activity:7468172552377503744.** **Google/Base44-killer 7d FINAL LOCKED at 146,506 imp / 196 react / 39 comm / 1 repost → ⭐⭐⭐ ALL-TIME RECORD (true 7d crossed last evening; +121 since 2026-06-03, fully plateaued; surpasses Anthropic 92,959 by ~58%).** Refreshes: Tough-days-Israeli-tech ~6.7d (14,601 imp / 241 react / 22 comm / 15 reposts — +90, plateaued just under 15K, locks ✅/⭐ tomorrow; true 7d this evening); YouTube-400K ~2.7d (1,492 imp / 48 react / 7 comm — +98 since 24h LOCK, tracking 🔴/🟡, 72h locks next run); 34,454-layoffs ~41h / 24h back-capture (2,665 imp / 21 react / 10 comm — +1,128 since 17h, recovered overnight into 🟡 territory past the 2,500 line). | **Google/Base44-killer 7d FINAL crossed at ⭐⭐⭐ ALL-TIME RECORD (146,506 imp) → Hebrew notification sent (official 7d lock at a new log record; record first flagged 2026-05-29 at 24h).** New "900 prompts" post logged. Tough-days locks tomorrow (✅/⭐). |
| 2026-06-07 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex; reactions via `reactions-count`/social-counts). Activity feed read top-down; 5 distinct posts visible. **No new posts since 2026-06-04 "900 prompts" — it remains the newest ("3d"), nothing new to log.** **"900 prompts" vibe-coding 72h LOCK at 3,678 imp / 39 react / 1 comm / 0 reposts → tracking 🟡 (+366 since 3,312 @ ~48h on 2026-06-06; the caption-only-hook + payoff-in-visual format holds above the median, reach now crawling). 7d FINAL due 2026-06-11.** Refreshes: 34,454-layoffs advice-listicle ~5d (4,190 imp / 24 react / 10 comm / 0 reposts — +88 since 4,102 on 2026-06-06, plateauing just under the 5K ✅ floor, holds 🟡; 7d FINAL due 2026-06-09); YouTube-400K milestone ~6d (1,672 imp / 52 react / 7 comm / 0 reposts — +35 since 1,637, reach fully capped near channel-marketing band, tracking 🔴; 7d FINAL due TOMORROW 2026-06-08); Tough-days-Israeli-tech post-FINAL long-tail (14,809 imp / 242 react / 22 comm / 15 reposts — +11 residual past the 14,798 ✅⭐ 7d lock, 15 reposts still log-record); Google/Base44-killer post-FINAL long-tail (146,614 imp / 197 react / 39 comm / 1 repost — +108 residual past the 146,506 ⭐⭐⭐ 7d lock, all-time record holds). | "900 prompts" 72h LOCK captured. No new posts. No 7d FINAL crossings today (YouTube-400K 7d is tomorrow). No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. Next 7d FINALs: YouTube-400K 2026-06-08 (🔴), 34,454-layoffs 2026-06-09 (🟡), "900 prompts" 2026-06-11 (🟡). |
| 2026-06-08 weekly digest | **Full scan — Chrome stable, all 11 inspiration creators read via JS extraction (recent-activity pages).** ~16 qualifying posts (1000+ react, ≤7d) across 8 creators. Top-10 led by Hormozi "Agree?" quote-cards (4,753 & 2,971) and **Steven Bartlett "laid off? we are hiring" (4,202 / 259 reposts) — same market-empathy + hiring-as-gift lane as Lior's Tough-days ✅⭐ (n=2 cross-creator this week).** Justin Welsh 3 posts (740/714-comment question hooks); Dan Koe "Just one hour. Please." (2,541, visual-carried). ZERO: Dan Martell (activity hidden, 3rd+ wk), Simon Beard, Tyler Denk. **Lior's week (3 tracked + 1 new, cooldown after 3 mega-posts):** "900 prompts" crossed the 5K ✅ floor (5,008 @ ~4d, first ✅ for caption-only-hook + payoff-in-visual format); 34,454-layoffs 4,593 🟡 (same topic as Tough-days but stripped of named-companies + hiring-offer → no reshare); YouTube-400K 7d FINAL 🔴 (1,784, channel-marketing cap); new accent/rejection post logged (early). Digest at linkedin-digests/digest-2026-06-08.md. Libraries (hooks/structures/visuals) updated with week-of observations. | Mid-tier consolidation week for Lior — no breakout, no bomb; headline is "900 prompts" winning a brand-new format. 2 style-guide proposals for Reut's Hebrew approval (elevate market-empathy+hiring-as-gift to confirmed lane; add caption-only+payoff-in-visual experimental lane) — on top of 2 still pending from the 2026-06-01 digest. Notified Reut in Hebrew. |
| 2026-06-09 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex; reactions/comments/reposts from `social-details-social-counts`). Activity feed read top-down; 5 distinct posts visible (post #1 = Lior's self-repost of post #2 = the new accent post). **NEW post detected and logged: 2026-06-08 ~17h "your accent was the dealbreaker / You are (:" — 905 imp @ 17h / 16 react / 4 comm / 1 self-repost. Vulnerability/self-acceptance lane (Wim Hof cold-feet 2,662 🟡, "I got rejected" 2,066 🔴); quoted-rejection hook with a self-implicating undercut ("Said by me. Never once by an investor") + on-stage photo as proof; NOT bait-and-switch (delivers a real lesson, no CTA payload). Soft 17h velocity, tracking 🟡/🔴 borderline ~2.5K. URL: urn:li:activity:7469746042029215745.** Refreshes: **"900 prompts" vibe-coding ~5d (5,150 imp / 49 react / 3 comm / 0 reposts — +187 since 4,963 @ ~4d on 2026-06-08; CROSSED the 5,000 ✅ floor — first ✅-trajectory post with no news anchor / no contrarian thesis, pure AI-builder humor; 7d FINAL due 2026-06-11. URL: urn:li:activity:7468172552377503744);** 34,454-layoffs advice-listicle ~6.7d (4,644 imp / 25 react / 10 comm / 0 reposts — +55 since 4,589, plateaued; true 7d crosses this evening → FINAL locks next run at ~4,650-4,750 → 🟡. URL: urn:li:activity:7467568112138272768); YouTube-400K milestone post-FINAL long-tail (1,802 imp / 53 react / 7 comm — +23 residual past the 1,779 🔴 7d FINAL locked 2026-06-08. URL: urn:li:activity:7467205850911305728). | New post logged with URL. No 7d FINAL crossings today (YouTube already locked 2026-06-08 🔴; 34,454-layoffs true 7d is this evening → next run; 900-prompts 7d is 2026-06-11). 900-prompts crossing the 5K ✅ floor at 5d is notable but not a 7d EXCEPTIONAL (>15K) or BOMBED crossing → silent completion, no notification. Flag for Monday digest: first ✅ in the comedic caption-only + payoff-in-visual lane. |
| 2026-06-10 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex; reactions/comments/reposts from `social-details-social-counts`). Activity feed read top-down; 5 distinct posts visible (post #1 = Lior's self-repost of post #2 = the new Founder's-Guide post). **NEW post detected and logged: 2026-06-09 ~17h "The Founder's Guide: 7 things about building an AI startup in 2026" — 1,091 imp @ 17h / 28 react / 6 comm / 1 self-repost. Event-recap / secondhand-wisdom listicle (23 exited founders in a room, Team8/PEF event); soft 17h velocity (well below the credential-milestone ⭐ lane — Birthday 9,621 @ 17h — because the wisdom is secondhand, not Lior's own first-person proof); tracking 🔴/🟡 borderline. URL: urn:li:activity:7470103427205828608.** **34,454-layoffs advice-listicle 7d FINAL LOCKED (back-capture, true 7d was 2026-06-09 evening) at 4,686 imp / 26 react / 10 comm / 0 reposts → 🟡 (landed just under the 5K ✅ floor exactly as projected). A/B with same-topic Tough-days (14,798 ✅⭐, 15 reposts) CLOSED: ~3.2x reach gap = the named-anchors + hiring-offer reshare engine, not the empathy theme.** Refreshes: "900 prompts" vibe-coding ~6d (**5,543 imp** / 49 react / 3 comm / 0 reposts — +393 since 5,150 @ ~5d, still climbing, 7d FINAL due TOMORROW 2026-06-11 → solid ✅ locked-in; URL urn:li:activity:7468172552377503744); accent-dealbreaker vulnerability ~41h / 24h back-capture (1,409 imp / 26 react / 4 comm — +504 since 905 @ ~17h, tracking 🟡/🔴 borderline in the Wim-Hof band; URL urn:li:activity:7469746042029215745). | New post logged with URL. 34,454-layoffs 7d FINAL locked 🟡 (4,686 — above 1,500, no bomb notification). No 7d EXCEPTIONAL/BOMBED crossing → silent completion, no notification. Next 7d FINALs: "900 prompts" 2026-06-11 (✅), accent 2026-06-15 (🟡/🔴), Founder's-Guide 2026-06-16. |
| 2026-06-11 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex; reactions/comments/reposts from `social-details-social-counts`). Activity feed read top-down; 5 distinct posts visible (post #1 = Lior's self-repost of post #2 = the new AutoDS-Claude post). **NEW post detected and logged: 2026-06-10 ~17h "AutoDS now talks to Claude" product-launch — 1,132 imp @ 17h / 28 react / 0 comm / 3 organic reposts. Product-announcement lane (names Claude/Anthropic in the hook — same trending-tool anchor as the mega-winners — but to ANNOUNCE a feature, not make a contrarian argument; soft 17h velocity, same setup that bombed MS+Anthropic workshop 1,175 🔴). Off the personal-journey brand per [feedback-lior-personal-brand-not-autods]. Tracking 🔴/🟡 borderline. URL: urn:li:activity:7470467368805117952.** **"900 prompts" vibe-coding 7d FINAL LOCKED at 5,825 imp / 51 react / 3 comm / 0 reposts → ✅ (cleared the 5,000 floor and kept climbing through the full window; first ✅ in the log on pure relatability — no news anchor / no thesis / no credential; reach-led, thin engagement ~0.93%). New repeatable reach format confirmed.** Refreshes: Founder's-Guide secondhand-listicle ~41h / 24h LOCK (1,467 imp / 34 react / 7 comm / 1 self-repost — +376 since 1,091 @ 17h; high comment-ratio but NO reach wave, same first-degree cap as 34,454-layoffs; confirms secondhand credential-listicle caps low vs first-person Birthday 18,009 ⭐; tracking 🔴/🟡, 7d FINAL 2026-06-16); accent-dealbreaker vulnerability ~65h (1,557 imp / 28 react / 4 comm — +148 since 1,409 @ ~41h; vulnerability lane's low-reach signature holds, comments frozen at 4; tracking 🔴/🟡, 72h locks tomorrow, 7d FINAL 2026-06-15). | "900 prompts" 7d FINAL locked ✅ (5,825 — above the 5K floor, but not EXCEPTIONAL >15K and not BOMBED <1,500). New AutoDS-Claude post logged. No 7d EXCEPTIONAL/BOMBED crossing → silent completion, no notification. **Flag for Monday digest: first ✅ in the comedic caption-only-hook + payoff-in-visual lane (n=1 confirmed); secondhand vs first-person credential-listicle A/B (Founder's-Guide low-cap vs Birthday ⭐) closing; product-launch AI post tracking soft (AI-name without contrarian frame).** Next 7d FINALs: accent 2026-06-15 (🔴/🟡), Founder's-Guide 2026-06-16, AutoDS-Claude 2026-06-17. |
| 2026-06-14 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex; reactions/comments/reposts from `social-details-social-counts`). **No scans ran 2026-06-12 or 2026-06-13 — this run back-captures.** Activity feed read top-down; 5 distinct posts visible (post #1 = the new Anthropic-repricing post). **NEW post detected and logged: 2026-06-12 ~48h "Anthropic is quietly repricing Claude on June 15 / here's how to prepare" — 2,124 imp / 15 react / 3 comm / 0 reposts. Contrarian-AI news anchor (names Anthropic + Claude in first 5 words — same DNA as the 30K/92K/146K mega-winners) bolted to a 3-step tactical-prescription body (Codex, Hermes, file-based setup) + vendor-lock-in meta-principle close; mirrors his real stack per [project-lior-agent-stack-hermes-codex]. 24h LOCK (2026-06-13) MISSED. Soft-middling velocity, tracking 🟡/🔴. URL: urn:li:activity:7470830643392770049.** Refreshes: AutoDS-Claude product-launch ~3-4d (1,633 imp / 38 react / 0 comm / 4 reposts — +501 imp / +10 react / +1 repost since 1,132 @ 17h on 2026-06-11; reshares creeping but reach still soft, tracking 🔴/🟡, 7d FINAL due 2026-06-17. URL urn:li:activity:7470467368805117952); Founder's-Guide secondhand-listicle ~5d (1,799 imp / 44 react / 9 comm — +332 imp / +10 react / +2 comm since 1,467 @ 24h; high comment-ratio, still no reach wave [first-degree cap], tracking 🔴/🟡, 7d FINAL due 2026-06-16. URL urn:li:activity:7470103427205828608); accent-dealbreaker vulnerability ~6d (1,738 imp / 30 react / 4 comm — +181 since 1,557 @ ~65h, comments frozen at 4, Wim-Hof low-reach band holds, tracking 🔴/🟡, 7d FINAL due TOMORROW 2026-06-15. URL urn:li:activity:7469746042029215745); "900 prompts" vibe-coding post-FINAL long-tail (6,595 imp / 56 react / 3 comm / 0 reposts — +770 residual past the 5,825 ✅ 7d FINAL locked 2026-06-11; ✅ holds, reach still creeping. URL urn:li:activity:7468172552377503744). Followers ~9,5xx. | New post logged with URL. No 7d FINAL crossings today (accent 7d is tomorrow). No EXCEPTIONAL/BOMBED 7d-FINAL crossing → silent completion, no notification. Next 7d FINALs: accent 2026-06-15 (🔴/🟡), Founder's-Guide 2026-06-16, AutoDS-Claude 2026-06-17, Anthropic-repricing 2026-06-19 (🟡/🔴). |
| 2026-06-27 10:13 daily scan | **PARTIAL scan — impressions captured for all 5 visible posts, then Chrome navigation locked out mid-run.** No scans ran 2026-06-15 → 2026-06-26 (12-day gap), so this run is a bulk back-capture. Initial `navigate` to the activity feed succeeded and two `data-urn` + inline `/([\d,]+)\s+impressions/` JS reads returned all 5 top-feed posts before the user took over the active tab (moved it to Instagram); every subsequent `navigate` to linkedin.com returned "Navigation to this domain is not allowed" (8 retries across 2 tabs + a fresh tab, all blocked — domain permission appears scoped out once the user reclaimed the browser). **Could not retrieve full post bodies, reactions, or run per-post analytics — only the inline impressions + partial comment/repost counts below were captured.** **5 NEW posts detected (all published in the 2026-06-15→25 window, none previously logged; last logged post was Anthropic-repricing 2026-06-12):** (1) urn:li:activity:7475903179285499904 ~2d (~2026-06-25) — **865 imp** / ~17 comm? [comment count low-confidence, implausibly high vs reach — likely regex noise] — body opens "There are two ways to build a SaaS. I learned which one…" (SaaS-building-philosophy lane); tracking 🔴. (2) urn:li:activity:7475563306238332928 ~3d (~2026-06-24) — **1,797 imp** — body opens "Anthropic just turned Claude into a…" (AI-name anchor — same hook DNA as the 30K/92K/146K mega-winners, but soft 1,797 @ 3d velocity = consistent with the recurring finding that an Anthropic/Claude name WITHOUT a contrarian thesis underperforms, cf. AutoDS-Claude 🔴 / MS+Anthropic 🔴); tracking 🔴/🟡. (3) urn:li:activity:7474816396057833473 ~5d (~2026-06-22) — **4,099 imp** / ~7 comm — body unread; tracking 🟡. (4) urn:li:activity:7474453586266038272 ~6d (~2026-06-21) — **3,893 imp** / ~7 comm / 1 rep — body unread; tracking 🟡. (5) urn:li:activity:7473242312660230144 ~1w (~2026-06-20) — **850 imp** — body unread; at/near 7d this is a 🔴 BOMB candidate (<1,500) but exact age + content unconfirmed → NOT notifying until back-captured. **All checkpoints from the 12-day outage (accent 7d 2026-06-15, Founder's-Guide 7d 2026-06-16, AutoDS-Claude 7d 2026-06-17, Anthropic-repricing 7d 2026-06-19) were MISSED and have aged off the top-5 feed — they are now post-window back-capture targets only, last-known values: accent 1,738 (🔴/🟡), Founder's-Guide 1,799 (🔴/🟡), AutoDS-Claude 1,633 (🔴/🟡), Anthropic-repricing 2,124 (🟡/🔴).** | Impressions (primary metric) captured for all 5 new posts despite the lockout. **NEXT CLEAN SCAN MUST: (a) pull full bodies + reactions for the 5 new posts and properly categorize hook/structure/visual; (b) confirm post #5's age + content and lock its 7d FINAL (likely 🔴 BOMB → Hebrew notification if confirmed <1,500 at 7d); (c) lock 7d FINALs for the 4 missed posts from last-known values.** No notification fired this run — the only bomb candidate (post #5) is unconfirmed on age + content. Navigation lockout is the blocking issue; cleanest fix is to run the scan when the browser is idle (no active user tab). |
| 2026-06-27 weekly digest (Chrome RECONNECTED, clean) | Full digest run; Chrome navigation worked (the 2026-06-27 daily partial had been locked out). **Back-captured full bodies + metrics for the 5 new posts the partial scan flagged** (per-creator creator feed still caps at top-5 via the blank-skeleton "Show more" bug). **Lior's week = COOLDOWN: zero ✅, two 🟡, three 🔴 (one bomb-in-progress):** (1) **World Cup/Levi's guerrilla-marketing case-study** urn:7474816396057833473 — 4,099 imp / 23 react / 7 comm @5d → 🟡 (best of week; named-brand case-study = reliable mid-reach floor); (2) **"If you have a dream… don't listen" / AutoDS turns 10** urn:7474453586266038272 — 3,893 imp / 88 react / 7 comm / 1 rep @6d → 🟡 (highest reactions of week; first-person founder-conviction + milestone, reach-capped by generic motivational opener); (3) **"Anthropic just turned Claude into a teammate in Slack" + how-to body** urn:7475563306238332928 — 1,798 imp / 11 react @3d → 🔴 (**AI-name WITHOUT contrarian thesis — n=4 confirmed dead-end**, joins AutoDS-Claude, MS+Anthropic 1,175, Anthropic-repricing 2,124); (4) **"There are two ways to build a SaaS" (Path A/B, $1 trial) + "what would you choose?"** urn:7475903179285499904 — 865 imp / 42 react / **17 comm (40% comment ratio — sharpest discussion-driver of the week; the partial-scan "regex noise" flag was wrong, the 17 is real)** @2d → 🔴 reach / strong comments; (5) **"Business is the ultimate team game"** urn:7473242312660230144 — 850 imp / 7 react @1w → 🔴 **BOMB-in-progress** (flat aphorism, no scene/number; 7d FINAL locks next run, likely <1,500 → Hebrew notification then). **Creators:** 7 qualifiers — Welsh 3 (7,854/6,264/4,255 conviction-aphorisms), Bartlett 2 (15,868 broad-invitation hiring / 3,189 Grantham AI-investing), Will Ahmed 2 (2,295 FDA-milestone / 1,109 founder-vision); Hormozi near-miss 992; GaryV/Matt Gray/Dan Koe/Rauch ZERO (GaryV+Hormozi windows under-sampled); Simon Beard + Tyler Denk profiles unresolved (wrong/404 handles — need correct vanity URLs from Reut). 4 back-window 7d FINALs locked from last-known (accent 1,738, Founder's-Guide 1,799, AutoDS-Claude 1,633, Anthropic-repricing 2,124 — all low-band, none recovered). Digest at linkedin-digests/digest-2026-06-27.md; hooks/structures/visuals libraries updated. | First digest since 2026-06-08 (06-15 & 06-22 Mondays missed). 2 new style-guide proposals pending Reut's Hebrew approval (AI-name-needs-thesis hard rule; aphorism-needs-edge rule) on top of those from prior digests. No notification-worthy 7d crossing this run (Team-game bomb locks next run). Notified Reut in Hebrew. |
| 2026-06-28 10:13 daily scan | Successful scan (Chrome stable, `data-urn` query + inline `/([\d,]+)\s+impressions/` regex). Activity feed read top-down but **capped at 5 posts** (the recurring lazy-load / "Show more" skeleton bug) — the team-game bomb candidate had aged off the top-5, so it was back-captured by navigating directly to its post URL. **No new posts since 2026-06-25 SaaS-two-ways — it remains the newest ("3d"), nothing new to log.** **TWO 7d FINALs locked this run:** (1) **"Business is the ultimate team game" 7d FINAL LOCKED (back-capture, true 7d was 2026-06-27) at 850 imp / 7 react → 🔴 BOMBED (<1,500 → Hebrew notification triggered). Confirms: flat aphorism with no scene / no number / no first-person story does not travel — joins the dead aphorism lane; the digest's bomb-in-progress call was correct, value held flat at 850 from 1w→8d. URL: urn:li:activity:7473242312660230144.** (2) **"If you have a dream… don't listen" / AutoDS turns 10 7d FINAL LOCKED at 3,895 imp / 88 react / 7 comm / 1 rep → 🟡 (above 1,500 → no bomb notification; highest reactions of the week but first-person founder-conviction + milestone reach-capped by the generic motivational opener — confirms motivational-opener tax even on first-person credential content). URL: urn:li:activity:7474453586266038272.** Refreshes (in-flight, post-window approaching): World Cup/Levi's guerrilla-marketing ~6d (4,099 imp / 23 react / 7 comm — flat since 2026-06-27, 🟡 holds, true 7d this evening → FINAL locks next run; named-brand case-study mid-reach floor. URL: urn:li:activity:7474816396057833473); Anthropic-Claude-Slack ~4d (1,804 imp / 11 react — +6 since 1,798 on 2026-06-27, tracking 🔴, the n=4-confirmed AI-name-without-thesis dead-end, 7d FINAL due 2026-07-01. URL: urn:li:activity:7475563306238332928); SaaS-two-ways ~3d (865 imp / 42 react / 17 comm — flat reach but 40% comment ratio holds [sharpest discussion-driver of the week], tracking 🔴 reach / strong comments, 7d FINAL due 2026-07-02. URL: urn:li:activity:7475903179285499904). | **Team-game 7d FINAL crossed at 🔴 BOMBED (850 imp) → Hebrew notification sent.** dream/AutoDS-10 locked 🟡 (3,895, no bomb threshold met). No new posts. Next 7d FINALs: World Cup/Levi's 2026-06-29 (🟡), Anthropic-Claude-Slack 2026-07-01 (🔴), SaaS-two-ways 2026-07-02 (🔴/comments-strong). |
| 2026-06-06 10:13 daily scan | Successful scan (Chrome stable, `textContent` JS extraction; impressions + social counts read inline; URLs from `data-urn`). **No scan ran 2026-06-05 — this run back-captures the checkpoints that were due then.** Activity feed read top-down; 5 distinct posts visible. **No new posts since 2026-06-04 "900 prompts" — it remains the newest, nothing new to log.** **Tough-days-Israeli-tech 7d FINAL LOCKED (back-capture, true 7d was 2026-06-04 ~18h) at 14,798 imp / 242 react / 22 comm / 15 reposts → ✅⭐ EXCEPTIONAL (under the 15K absolute line but top-10% of all Lior posts ever — 5th-highest of n=18 finals; the most-reshared post in the log; first EXCEPTIONAL in the market-empathy + value-first-hiring lane).** Refreshes: **Google/Base44-killer ~9.7d post-FINAL long-tail (146,595 imp / 196 react / 39 comm / 1 repost — +89 residual past the 146,506 7d FINAL lock; ⭐⭐⭐ all-time record holds);** "900 prompts" vibe-coding ~48h (3,312 imp / 35 react / 1 comm / 0 reposts — **huge recovery from 363 @ 1-2h on 2026-06-04**; +2,949 imp, the caption-only-hook + payoff-in-visual format found reach overnight; tracking 🟡 toward 7d FINAL due 2026-06-11); 34,454-layoffs advice-listicle ~4d / **72h back-capture (due 2026-06-05)** (4,102 imp / 23 react / 10 comm / 0 organic reposts — +1,437 since 24h 2,665; recovered into solid 🟡 but ~3.6x softer than same-topic Tough-days, no reshare engine; 7d FINAL due 2026-06-09); YouTube-400K milestone ~5d / **72h back-capture (due 2026-06-04)** (1,637 imp / 51 react / 7 comm / 0 reposts — +145 since 24h LOCK 1,492; reactions healthy but reach soft, tracking 🔴/🟡, 7d FINAL due 2026-06-08). | **Tough-days 7d FINAL crossed at ✅⭐ EXCEPTIONAL (14,798 imp, top-10% of Lior's posts) → Hebrew notification sent.** No new posts. Next 7d FINALs: YouTube-400K 2026-06-08 (🔴/🟡), 34,454-layoffs 2026-06-09 (🟡), "900 prompts" 2026-06-11 (🟡). |
| 2026-07-12 10:13 daily scan | Successful scan (Chrome logged in as Lior; `data-urn` + inline `/([\d,]+)\s+impressions/` regex; social counts from `.social-details-social-counts`; full bodies from `.update-components-text`). **No scan ran 2026-06-29 → 2026-07-11 (14-day gap; last successful run 2026-06-28) — this run bulk back-captures.** Activity feed read top-down; **8 distinct posts visible, ALL NEW (last logged post-entry was Anthropic-repricing 2026-06-12; the 5 late-June posts from the 06-27/28 runs live only in Scan Issues rows).** All 8 logged fresh below with URLs. **Batch verdict = soft/middling fortnight — zero ✅ (none cleared 5,000), five 🟡, three 🔴.** Ranked by impressions: I'm-31/co-founder **3,909 🟡** (7479889605165694979, 5d); Ofir-Bokobza/macro-manager **3,404 🟡** (7480614165741486080, 3d); 250-people/autonomy **3,374 🟡** (7477356579235979264, ~1w, 109 react/2 rep — highest reactions of batch); Forbes-30u30/"same room" **3,224 🟡** (7478083961689235456, ~1w); WhatsApp-Meta-username **3,032 🟡** (7477715303322435585, ~1w); Fable5/"Claude is a team of four" **3,027 🟡** (7480252170936782848, 4d); Fable5-back/"go to the beach" **1,222 🔴** (7478319331647516672, ~7d — BOMB, <1,500 → Hebrew notification); Grok-4.5/"insane month for programming" **1,141 🔴** (7480977724845654017, 2d, in-flight but low velocity). **Cross-cut pattern (reinforces existing rule): 4 of 8 were AI-model-news; the two weakest were both AI posts without a contrarian thesis (Grok 1,141, Fable5-beach 1,222) — n=6 now on the "AI-name-without-thesis dead-end." Personal founder-story + macro-manager-autonomy posts carried the batch (3.0–3.9K band).** Abandoned (aged off feed, never locked, too old to matter): World Cup/Levi's 7d (2026-06-29), Anthropic-Claude-Slack 7d (2026-07-01), SaaS-two-ways 7d (2026-07-02) — held at last-known 4,099/1,804/865. | 8 new posts logged with URLs after a 14-day outage. **Fable5-beach 7d BOMB (1,222 🔴, <1,500) → Hebrew notification sent** (folded into a recovery + pattern note). No EXCEPTIONAL crossings. In-flight 7d FINALs to lock next runs: Grok 2026-07-17, Ofir 2026-07-16, Fable5-team 2026-07-15, I'm-31 2026-07-14 (all currently 🟡 except Grok 🔴). |
| 2026-08-02 10:13 daily scan | Successful scan (Chrome logged in as Lior; activity feed read top-down via `get_page_text`, per-post `View analytics` hrefs read from the a11y tree for URNs, per-post analytics pages for saves / network split). **No scans ran 2026-07-27 → 2026-08-01 (6-day outage, Mac asleep) — this run back-captures.** 8 posts visible; **5 NEW, all logged with URLs:** 07-28 AI-moat thesis **2,207 @5d 🔴** (7487499827619143681), 07-29 profitable-company shutdown **3,350 @4d 🟡** (7487861977659133952, best of batch), 07-30 "At 21 / Me at 31" **2,223 @3d 🔴** (7488224531732393984), **07-31 Fiverr-anniversary REPUBLISH 693 @2d 🔴 BOMB** (7488585446252445696 — near-verbatim reuse of the 200K+ 1-year post; 7.9% ER, the log's highest, on the log's 3rd-lowest reach = duplicate-content suppression), 08-01 accidental-founder origin **1,213 @1d 🔴** (7488949326258307072). **4 back-captured 7d FINALs locked past their slots:** Messi **10,771 ⭐** (07-27 slot), AutoDS-connectors **2,811 🟡** (07-28 slot), DotDev-learnings **3,777 🟡** (07-29 slot), coffee-truck **2,562 🟡** (07-30 slot); plus Ronen reshare **1,208** (unscored) and trainer post-FINAL drift 3,286 → 3,361. Followers **11,570**. LinkedIn 7-day rollup: 11,680 imp, +48% vs prior 7 days. Baseline recount to **n=36**, median 3,255, top-10% threshold moves 30,009 → 18,009. | No 7d FINAL crossed into EXCEPTIONAL (Messi 10,771 sits below both the >15,000 line and the new 18,009 top-10% threshold) and no *authored* 7d FINAL bombed (lowest was coffee-truck 2,562). **Notified Reut in Hebrew anyway on two counts the silent-completion rule does not cover: the 6-day scan outage, and the 07-31 anniversary republish collapsing to 693 (~300x below the 200K+ original it copies) — a standing instruction in memory says to reuse that post for the 2-year anniversary, so the finding is time-sensitive.** Next 7d FINALs: AI-moat 2026-08-04, shutdown 2026-08-05, then-vs-now 2026-08-06, anniversary-republish 2026-08-07, accidental-founder 2026-08-08. |
| 2026-08-04 10:13 daily scan | **Clean scan — Chrome signed back in as Lior, Creator Analytics restored** after the 2026-08-03 outage. Impressions were readable **inline on the activity feed** (`N impressions / View analytics` under each post), so no per-post analytics navigation was needed; URNs confirmed via DOM `data-urn` and all six matched the log. Followers **11,600** (+30 since 08-02). **1 NEW post logged:** 2026-08-03 "Don't take advice from me" podcast-promo, **1,099 @ 17h** (7490036287115005952), already self-reposted (7490273961277317120). **1 7d FINAL locked on the day:** 07-28 AI-moat thesis **2,402 🔴**. **1 checkpoint locked:** 08-01 accidental-founder **1,522 🔴 @ 72h**. Refreshes: 07-29 shutdown **3,464 @6d 🟡**, 07-30 then-vs-now **2,324 @5d 🔴** (engagement fully frozen), 07-31 republish **778 @4d 🔴 BOMB** (+85 imp in 2 days, ER 7.6%). Baseline recount to **n=37**, median **3,224** (first median decline since n=15); thresholds unchanged. Corrected an arithmetic error in the 2026-08-02 band counts (n=36 was 13 🔴 / 14 🟡 / 9 ✅, not 14/13/9). | **Silent completion — no notification trigger met.** The only 7d FINAL (2,402) is neither exceptional (>15,000 / top-10% ≥18,009) nor a bomb (<1,500 / bottom-10% ≤1,175), and nothing went wrong with access. Three locks land in the next four days: shutdown 08-05, then-vs-now 08-06, **anniversary-republish 08-07 — projected ~820–860, which enters the bottom-10% band and WILL trigger a Hebrew notification on lock.** Digest items carried forward: topic concentration on the exit/origin story capping the whole 07-28→08-03 block; the 08-03 post's off-platform "link in first comment" CTA; and the contrast-template drift streak breaking at n=4. |
| 2026-08-03 10:13 daily scan | **PARTIAL scan — Chrome NOT logged in as Lior.** `linkedin.com/in/liorpozin/recent-activity/all/` rendered the logged-OUT public view ("Join to view profile", experience redacted, follower count shown as the public 12K), and `linkedin.com/feed/` redirected to `/login`. **Creator Analytics unreachable → impressions UNAVAILABLE for every post this run** (per the task rules, marked unavailable rather than estimated; logging in is out of scope for this task — read-only, and credentials are never entered). Public reaction/comment counts WERE readable from the guest profile view and are logged as deltas. **No new posts** — newest item is still 08-01 accidental-founder ("2d"), so nothing to add to the Posts Log. **No 7d FINAL crossed today** (next is AI-moat, due 2026-08-04). **72h checkpoint for the 07-31 anniversary republish falls today and is locked on public engagement only, impressions unavailable.** Engagement deltas vs the 2026-08-02 capture: 07-28 AI-moat 37 react / 19 comm (+1 comm); 07-29 shutdown 28 / 14 (+1 react); 07-30 then-vs-now 54 / 17 (+1 react, +1 comm); 07-31 republish 45 / 12 (+4 react); 08-01 origin 43 / 12 (+3 react). Reposts not exposed in the guest view. **Signal despite the missing impressions: all five in-flight posts added between 0 and 4 reactions in 24h — the whole batch has gone flat on engagement, and the 07-31 republish adding the most (+4) while carrying the log's lowest reach reinforces the first-degree-only / duplicate-suppression reading rather than weakening it.** | Impressions marked unavailable for the 2026-08-03 checkpoints; flag in the next Monday digest per the task rules. **Blocking issue: the Chrome profile driving the extension is signed out of LinkedIn — Reut needs to sign back in as Lior before the next run, otherwise 2026-08-04 (AI-moat 7d FINAL) and every subsequent 7d lock will also land without the primary metric.** No EXCEPTIONAL/BOMBED 7d crossing today, but notified Reut in Hebrew because the scan could not complete and a 7d FINAL is due tomorrow. Rolling Benchmarks unchanged (no new final-locked posts; baseline holds at n=36, median 3,255). |
| 2026-08-05 10:13 daily scan | **Clean scan — Chrome logged in as Lior, Creator Analytics readable.** Impressions read inline on the activity feed (`data-urn` + `/([\d,]+)\s+impressions/`), social counts from `.social-details-social-counts`, bodies from `.update-components-text`; the two posts that had aged off the recurring top-5 feed cap were back-captured by direct post URL. Followers **11,611** (+11 since 08-04). **1 NEW post logged: 08-04 "wealthy friend / the founder who froze 3 products" (focus parable) — 821 imp @ 18h, the softest opening in the log and the first post to be weak on reach AND on reactions at the same time.** **7d FINAL locked: the shutdown post at 3,494 🟡.** ⚠️ **Data-integrity finding: the publish dates on the four entries headed 07-29 → 08-01 are each one day late.** Decoding the activity URN (`id >> 22` = epoch ms) gives the true publish times — shutdown **07-28** 13:30 UTC, "At 21" **07-29** 13:30, republish **07-30** 13:25, origin **07-31** 13:30 — and all four match LinkedIn's own relative age labels this run (1w / 6d / 5d / 4d). The 08-03 and 08-04 entries are correct. Entry headings left unchanged so URL/permalink matching keeps working; checkpoint due-dates corrected in-line. **Method note for future scans: URN-decoding is exact and should be preferred over the relative age label.** | Log updated. No notification sent — the only 7d crossing (3,494 🟡) is neither top-10% nor bottom-10%. |
| 2026-08-09 10:13 daily scan | **Clean scan — Chrome logged in as Lior, Creator Analytics fully readable.** Activity feed read via `get_page_text` (impressions render inline under each post), then per-post analytics pages pulled directly at `/analytics/post-summary/urn:li:activity:{id}/` for saves / sends / profile viewers / followers-gained. **No scan ran 2026-08-08, so every reading below is a two-day delta and the 08-06 Shopify post's 24h checkpoint was missed** (first read after the mark is this one at 2.7d). One transient Chrome-extension disconnect mid-run, recovered on retry after ~20s. **NO NEW POSTS — nothing published since 2026-08-06 14:14 UTC, a ~2.8-day gap against the agency's previously daily cadence.** Four in-flight posts refreshed, none crossed 7d: **08-05 give-back listicle 8,864 @3.7d ✅** (96 react / 18 comm / 166 profile viewers / 5 followers — **+1,382 in two days, the only post in the block still compounding**; projects ~9.5–10.3K at the 08-12 lock, which would be 5th-highest final-locked in the log); **08-06 Shopify newsjack 3,832 @2.7d 🟡** (54 / 24 / 22 / 1 — the 48h doubling test called on 08-07 comes back negative at 1.36x, so the 5–7K ✅ projection is revised down to **~4,200–4,800 🟡**; carries the block's sharpest comment rate at 0.63%); **08-03 podcast promo 1,529 @5.7d 🔴** (+104 in two days, engagement frozen at 38/15 for a fourth reading, locks ~1,570–1,610 tomorrow); **08-04 borrowed-story parable 1,039 @4.7d 🔴** (+57 in two days, every counter frozen, locks ~1,090–1,120 on 08-11). Post-FINAL drift: 08-01 origin post 1,695 → **1,788**. **Three findings this run:** (1) **slow-burn vs fast-burst** — the give-back listicle is still climbing on day four while the newsjack flattened after day one, so evergreen reference material and news-anchored commentary decay on completely different curves and should not share a target; (2) **save/send/repost counts are unusable at any age** — this post's saves have been revised 8 → 3 → 1 across three readings while impressions, reactions and comments have never revised downward, which retires the "saves are the tell" read from 08-06; (3) **profile conversion separates the lanes harder than reach does** — 1.87% of impressions for the give-back post vs 0.57% for the newsjack and 0.03% for the off-platform-CTA podcast post. | **Silent completion — no notification trigger met.** No post crossed 7d this run, so neither the EXCEPTIONAL (>15,000 / top-10% ≥18,009) nor the BOMBED (<1,500 / bottom-10% ≤1,175) condition could fire, and Chrome access was clean. Rolling Benchmarks unchanged (no new final-locked posts; baseline holds at n=37, median 3,224). **Next 7d FINALs: podcast promo 2026-08-10 (🔴 ~1,590), parable 2026-08-11 (🔴 ~1,100, just outside the bottom-10% band so no notification expected), give-back listicle 2026-08-12 (✅ ~9.5–10.3K — lands below the 18,009 top-10% threshold so it will not trigger a notification, but it is the strongest ✅ in 22 posts and belongs at the top of the digest), Shopify newsjack 2026-08-13 (🟡 ~4,500).** Digest items carried forward: the ~2.8-day publishing gap immediately after the account's best post in three weeks; slow-burn vs fast-burst lane separation; and the give-back structure now confirmed at a third reading as the only thing converting reach into profile traffic. |
| 2026-08-29 10:13 daily scan | **20-DAY SCAN OUTAGE CLOSED (last successful run 2026-08-09).** No scan executed 2026-08-10 → 2026-08-28; the scheduled task only fires with the Mac awake and the app open, so this is 19 missed slots, not a pipeline fault. Consequence: **every 24h and 72h checkpoint for the eleven posts published 08-10 → 08-27 was missed**, and the eight that are past 7d are locked here from lifetime values rather than clean 7d marks (they had all plateaued, so drift is small but each may run marginally high). Chrome logged in as Lior, Creator Analytics fully readable. Method: post list + lifetime impressions from `/analytics/creator/top-posts/?timeRange=past_28_days`; publish times by URN decoding; per-post saves/sends/profile-viewers/**followers gained** from `/analytics/post-summary/urn:li:activity:{id}/`. **Two transient Chrome-extension disconnects** (recovered on retry) and **one stale-render fault** — the analytics SPA returned the *previous* post's metrics when read 3s after navigation, which briefly mis-attributed the 08-12 and 08-13 posts; fixed by echoing `location.pathname` with every reading, raising the wait to 5s, and cross-checking every number against the top-posts list. **Method note for future scans: always echo the URL alongside the metrics on the post-summary SPA.** **12 FINALS locked, 3 in-flight, baseline n=40 → n=52, followers 12,698 (+1,036 since 08-06).** | Log updated. **Hebrew notification SENT** — the 08-25 exit-deck post is at 66,524 impressions / 86 followers, the 3rd-highest post in the log, and two posts crossed 7d in the bottom-10% band (Jim Rohn 687, founder-stations 1,084). |

---

## Posts Log

### 2026-04-13 — 70% rule for delegation (carousel)
**Post URL:** TBD (next scan)
**Topic tag:** #delegation #scaling #framework
**Hook type:** Time-contrast personal stat ("I spent the first 5 years... Today I barely touch a task list")
**Structure:** Hook → Personal context → Rule statement → Application examples → Outcome → Carousel CTA
**Visual:** Carousel/document
**Length:** ~95 words
**CTA:** Implicit — "I broke the full framework down slide by slide" → carousel

**Full post text:**
> I spent the first 5 years at AutoDS doing almost everything myself.
> Today I barely touch a task list.
> Here's the one rule that freed 80% of my time.
> The 70% rule: if someone can do the task at least 70% as well as you, they're doing it.
> Not 100%.
> Not 90%.
> 70%.
> Sounds risky.
> But here's what happened when I applied it:
> First hire took YouTube off my plate.
> Then finance.
> Then product ops.
> One by one, every task that passed the 70% test became someone else's job.
> The result?
> Scaled to 1M+ paying users and sold AutoDS to Fiverr.
> I broke the full framework down slide by slide.
> The 70% rule that changed everything 👇
> AutoDS - Automatic Dropshipping Tools

**Metrics (at 7 days — FINAL, locked retroactively):**
- Impressions: 1,783 → **verdict: 🔴** (under 2,500)
- Likes: 32
- Comments: 1
- Reshares: 0
- Engagement rate: ~1.85%

**Analysis:**
- What worked: Specific framework name + specific number (70%); trust signal (1M+ users, Fiverr exit)
- What didn't: Carousel CTA may have suppressed dwell time vs native text; comments-to-likes ratio extremely low (1:32) suggests no debate trigger; the 80% time-saved claim is a closed loop that doesn't invite opinion
- vs. Lior's baseline: TBD (insufficient data — 5 posts logged)
- vs. top-creator patterns: Matches "named-rule + personal proof" structure (Justin Welsh territory). Failed here likely because the close was a CTA-to-asset, not an open question

**Learnings applied going forward:** When the post is a framework-style breakdown, end with a question that invites the reader to share their own version of the rule. Don't close with "swipe to see more" — that exports engagement off-feed.

---

### 2026-04-13 — 10-80-10 rule for AI marketing
**Post URL:** TBD (next scan)
**Topic tag:** #ai #marketing #framework
**Hook type:** Outcome stat + comparison ("We went from one brand to five. Same marketing team")
**Structure:** Hook → Social proof list → Framework name → Breakdown → Closing question
**Visual:** Image (likely 10-80-10 graphic)
**Length:** ~115 words
**CTA:** Open question — "What's the one task AI cut from hours to minutes for you?"

**Full post text:**
> We went from one brand to five.
> Same marketing team. Not a single hire added.
> And we're not the only ones:
> → Anthropic built a $60B company with one person (!) running growth marketing.
> → Cursor scaled to $2B in revenue. Zero traditional marketing spend.
> → Notion hit 20M+ users. Nearly all organic.
> Here's how we do it.
> I call it the 10-80-10 rule:
> 10% - we ideate. Brand voice, audience, strategy.
> 80% - AI executes. Content, funnels, designs, campaigns.
> 10% - we review, sniff test, ship.
> The human brings taste and vision.
> AI does the heavy lifting you shouldn't be doing twice.
> This is what marketing in 2026 actually looks like. Not "AI is coming for your job" think pieces.
> Just a team that quietly scaled 5x.
> What's the one task AI cut from hours to minutes for you?

**Metrics (at 7 days — FINAL, locked retroactively):**
- Impressions: 1,701 → **verdict: 🔴** (under 2,500)
- Likes: 15
- Comments: 4
- Reshares: 0
- Engagement rate: ~1.12%

**Analysis:**
- What worked: Comments-to-likes ratio (4:15 = 26%) is high — the closing question DID earn dialogue. Named framework (10-80-10) is sticky.
- What didn't: Hook is a brag-stat that doesn't pull skeptics; Anthropic/Cursor/Notion name-drop is generic SaaS-Twitter wallpaper; "marketing in 2026" framing is overused. Impressions floor (1,701) suggests algorithm didn't push past first-degree network.
- vs. Lior's baseline: Below average so far (lowest of 5 logged).
- vs. top-creator patterns: Matches Justin Welsh "named framework" pattern. The closing question style matches the LinkedIn engagement-gap rule from memory. So why did it flop? Hypothesis: the framework name (10-80-10) lands as forgettable percentages, and the proof points are abstract (other companies, not Lior's own daily reality).

**Learnings applied going forward:** When using a numbered framework, anchor it to a SPECIFIC moment from Lior's week — not abstract company examples. "Last Tuesday I watched our AI agent write the email I would've spent 90 minutes on" beats "Notion hit 20M users."

---

### 2026-04-20 — Paperclip / zero-human-company experiment ⭐ EXCEPTIONAL
**Post URL:** TBD (next scan)
**Topic tag:** #ai #building #judgment
**Hook type:** Provocative confession ("I set up AI agents to replace my entire team. Including me.")
**Structure:** Hook → Setup (tool + premise) → Day-1 enthusiasm → Reality check → Diagnosis (telephone game) → Insight (judgment can't be delegated) → Closing question
**Visual:** Carousel/image
**Length:** ~210 words
**CTA:** Open question — "Is this not the greatest time in history to be building?"

**Full post text:**
> I set up AI agents to replace my entire team.
> Including me.
> And let them run.
> For 2 weeks, I've been using one of the most viral AI tools.
> Paperclip.
> An open-source tool that lets you hire AI agents.
> You sit on the board.
> They run the company.
> Day one, I was hooked.
> I set a goal for my CEO agent.
> He broke it into tasks, hired a CTO, CTO hired engineers.
> They started building.
> The dashboard tracked every agent, every dollar, every task.
> It looked like a real company.
> Until I checked the output.
> What came back was a blurry copy of a blurry copy of what I originally asked for.
> Same as the telephone game.
> I told the CEO what I wanted.
> CEO told CTO.
> CTO told the engineer.
> Every handoff dropped context.
> Real people push back.
> Agents don't. They just execute the drift.
> AI can do everything except apply your judgment.
> You still have to encode that yourself.
> Paperclip is a great tool for managing AI agents.
> But the "zero human company" story? Marketing.
> Humans aren't going anywhere.
> Is this not the greatest time in history to be building?

**Metrics (at 7 days — FINAL):**
- Impressions: 30,009 → **verdict: ✅ EXCEPTIONAL** (top 10% threshold; >15K trigger met)
- Likes: 23
- Comments: 3
- Reshares: 0
- Engagement rate: ~0.09% (engagement low DESPITE huge reach — see analysis)

**Analysis:**
- What worked: Hook is a contrarian confession with stakes ("replace my entire team. Including me."). The "telephone game" metaphor is concrete, visual, instantly understandable. The post takes a hot AI tool (Paperclip) and adds an honest contrarian conclusion — that pattern travels because it's rare.
- What didn't: Engagement rate is suspiciously low for 30K impressions. Hypothesis: post got pushed into the broader feed (algorithm saw it as a hot-take on a trending tool) but the audience was second/third-degree, not Lior's core network. Also, the closing rhetorical question ("greatest time to be building?") is a closed enthusiasm cap, not a real prompt.
- vs. Lior's baseline: 17x median (rough estimate based on 5 posts). Far and away the top performer.
- vs. top-creator patterns: Matches the "I tried the viral tool, here's the truth" pattern (Greg Isenberg, Sahil Bloom territory). Reinforces that contrarian-conclusion-on-trending-topic is high-leverage for Lior.

**Learnings applied going forward:** This is a TEMPLATE — try it again on the next viral AI tool. Pattern: (1) name the tool, (2) confess you went all-in, (3) report the unexpected failure mode with a concrete metaphor, (4) extract a principle about judgment/humans/taste. Also: when reach is huge but engagement is flat, swap the closing rhetorical question for something the lurker can actually answer in one line.

---

### 2026-04-20 — Wim Hof Winter Expedition / cold feet
**Post URL:** TBD (next scan)
**Topic tag:** #personal #fear #growth
**Hook type:** Vulnerable confession ("I'm about to get cold feet. Literally.")
**Structure:** Hook → Setup (where + why) → Specific fears (bulleted) → Resolution → Mantra → Closing wish
**Visual:** Image (likely Wim Hof / cold-water imagery)
**Length:** ~110 words
**CTA:** Soft — "Wish me luck ❄️"

**Full post text:**
> I'm about to get cold feet. Literally.
> The more I want to cancel this trip, the more I know I have to go.
> I'm heading to Sweden for the Wim Hof Winter Expedition -
> the guy who ran a half-marathon barefoot in the snow and climbed Kilimanjaro in shorts. I'll be honest, I've been terrified of this journey.
> • Plunging into glacial waters
> • Snow hikes at -10°C
> • Standing under frozen waterfalls
> The fear is real.
> But I'm still getting on the plane.
> I'm doing this to remind myself that I can stretch my boundaries to the absolute edge.
> You can call me crazy - but for me, the comfort zone is the most dangerous place a person can live.
> So I'm jumping into the (frozen) water.
> I'll report back. Wish me luck ❄️

**Metrics (at 7 days — FINAL):**
- Impressions: 2,530 → **verdict: 🟡** (middling, just above 2,500 floor)
- Likes: 57
- Comments: 11
- Reshares: 1
- Engagement rate: ~2.73%

**Metrics (refresh 2026-04-29, ~9 days post):**
- Impressions: 2,594 (+64 since 7d lock)
- Likes: 57 (no change)
- Comments: 11 (no change)
- Reshares: 1 (no change)

**Metrics (refresh 2026-05-01, ~11 days post):**
- Impressions: 2,662 (+68 since 2026-04-29)
- Likes: 60 (+3)
- Comments: 12 (+1)
- Reshares: 1 (no change)
- Note: still slowly accruing — long-tail engagement on personal-journey post.

**Metrics (refresh 2026-05-03, ~13 days post — Modball / Wim Hof entries below kept current; this entry not re-fetched in 2026-05-03 scan, still trusts 2026-05-01 numbers):**
- (No fresh data this run — only 5 most recent posts surfaced on activity page; this post sits past the visible window. Holds at 2,662 imp / 60 likes / 12 comments.)

**Analysis:**
- What worked: Highest like count + comment count of the 5 posts. Personal, vulnerable hook ("cold feet. Literally."). The bulleted fear list (glacial waters / -10°C / frozen waterfalls) gives readers concrete imagery to react to. Comments-to-likes ratio (11:57 = 19%) shows real dialogue.
- What didn't: Impressions cap at 2,530 suggests algorithm read this as a personal/lifestyle post and limited it to first-degree network. Compare to Paperclip (broader topic, 30K impressions).
- vs. Lior's baseline: Highest engagement RATE of the 5 logged, lowest absolute reach among the AI/business posts but high for personal-narrative posts.
- vs. top-creator patterns: Matches "real person on a real path" principle from memory — Lior as a human, not a marketing channel. This is the category we want MORE of.

**Learnings applied going forward:** Personal-journey posts will cap at ~3K reach but generate the highest engagement rate AND build long-term audience loyalty. Don't judge them on impressions. Run the follow-up post ("I survived Wim Hof, here's what changed") — it's the natural sequel and will earn second-wave reach. **CONFIRMED 2026-04-28:** the sequel ("5 days with Wim Hof taught me…") posted — track it as the natural A/B for this hypothesis.

---

### 2026-04-24 — Modball × AutoDS partnership announcement
**Post URL:** TBD (next scan)
**Topic tag:** #partnership #brand #event
**Hook type:** Announcement / brand reveal ("Modball × AutoDS 🏁")
**Structure:** Hook → Announcement → Route map → Stakes → Tagline → CTA
**Visual:** Video
**Length:** ~85 words
**CTA:** Soft — "See you on the road 🏎️"

**Full post text:**
> Modball × AutoDS 🏁
> I've been waiting to share this one-
> Proud to continue our partnership with Modball - this year as the Official Title Sponsor!
> In 39 days, the journey begins:
> 🇬🇷 Thessaloniki → 🇦🇱 Tirana → 🇭🇷 Dubrovnik → 🇭🇷 Split → 🇮🇹 Trieste → 🇮🇹 Milan → 🇲🇨 Monaco
> 7 days.
> 1 finish line - the Monaco F1 Grand Prix. 🏁
> Modball, powered by AutoDS - Automatic Dropshipping Tools, brings together drivers, founders, builders, and operators who move fast - our kind of crowd.
> See you on the road 🏎️

**Metrics (at ~3 days):**
- Impressions: 1,752 (still mid-window)
- Likes: 33
- Comments: 3
- Reshares: 5
- Comments/likes ratio: ~9%

**Metrics (at ~5 days, snapshot 2026-04-29):**
- Impressions: 1,980
- Likes: 36
- Comments: 3
- Reshares: 5
- Comments/likes ratio: ~8%

**Metrics (at 7 days — FINAL, locked 2026-05-01):**
- Impressions: 2,070 → **verdict: 🔴** (under 2,500)
- Likes: 37
- Comments: 3
- Reshares: 5
- Engagement rate: ~2.17%

**Metrics (post-FINAL refresh 2026-05-03, ~9 days post):**
- Impressions: 2,095 (+25 since 7d lock — slow long tail, partnership posts don't accrue much)
- Likes: 37 (no change)
- Comments: 3 (no change)
- Reshares: 5 (no change)

**Metrics (post-FINAL refresh 2026-05-07, ~13 days post):**
- Impressions: 2,277 (+182 since 2026-05-03 — partnership posts apparently DO keep accruing slowly via reshares; 5 reposts each kept seeding new audiences)
- Likes: 37 (no change)
- Comments: 3 (no change)
- Reshares: 5 (no change)
- Note: 13 days out, post crossed the original Wim Hof / cold feet 7d FINAL impression mark (2,530). 7d verdict unchanged at 🔴. Confirms reshare-heavy partnership posts keep a longer tail than personal-vulnerability posts (cold-feet was 2,662 at 11d; Modball at 2,277 / 13d still trailing).

**Analysis:**
- What worked: Reshare count (5 = highest in current log set) — partnership/brand announcements travel via repost more than via reaction. Comments-to-likes ratio (3:37 = 8%) modest but positive.
- What didn't: Impressions ceiling at 2,070 confirms the brand-announcement lane is the weakest performer on Lior's profile. Algorithm reads "powered by AutoDS" as channel marketing and limits reach beyond first-degree network.
- vs. Lior's baseline: Below median (1,783 prior median). Not the bottom but in the 🔴 band.
- vs. top-creator patterns: Doesn't match a winning pattern. This is brand-channel content, not personal-founder content. Expected outcome.

**Learnings applied going forward:** Brand-partnership announcement posts will cap ~2K impressions on Lior's profile. Either (1) accept this as a brand-awareness post (not engagement), or (2) reframe future partnership posts as Lior's personal stake/story ("Why I personally signed off on title-sponsoring this") to enter the personal-journey lane. Logs as third confirmation that AutoDS-branded posts underperform on Lior's profile.

---

### 2026-04-28 — Wim Hof Sweden, 5-day takeaways (sequel to "cold feet")
**Post URL:** TBD (next scan)
**Topic tag:** #personal #wellness #growth
**Hook type:** Vivid extreme-action stat ("I hiked a mountain in shorts at -15°C. Then I sat in a frozen lake for 7 minutes.")
**Structure:** Hook → Numbered takeaways (1. The first step is the hardest 2. Body knows things mind doesn't 3. If it scares me, that's the sign) → Personal anecdote per takeaway → Closing imperative
**Visual:** Image (Wim Hof / cold-water imagery, carousel likely)
**Length:** ~250 words
**CTA:** Imperative — "Don't think about it. Just go."

**Full post text:**
> I hiked a mountain in shorts at -15°C. Then I sat in a frozen lake for 7 minutes.
> Here's what 5 days with Wim Hof taught me:
> 1. The first step is the hardest.
> The hard part of the mountain wasn't the top - it was the bottom.
> Taking the first step into the snow.
> The first dip in the frozen lake.
> The beginning is where the resistance lives.
> 2. Our body knows things the mind doesn't.
> After every session, I was frozen solid.
> I couldn't move my fingers.
> I couldn't move my toes.
> At the top of the mountain, I ordered a hot chocolate and couldn't even hold the cup.
> Then I started breathing the way they taught us.
> Slow. Deep. Deliberate.
> I sent warm thoughts to my hands and feet.
> My fingers were working again within a minute.
> 3. If it scares me, that's the sign to do it.
> Amit Giladi told me over coffee that it was the best wellness event he'd ever joined.
> I didn't know where I was going.
> I didn't know the plan.
> It scared me.
> So I booked the ticket.
> Now I'm passing it on.
> Don't think about it. Just go.

**Metrics (at ~24h, snapshot 2026-04-29):**
- Impressions: 1,352
- Likes: 40
- Comments: 0 visible (none surfaced in feed view; verify in next scan)
- Reshares: 1 (Lior reposted himself — matches the linkedin-posting-rules.md self-repost tactic)
- Comments/likes ratio: ~0% (verify)

**Metrics (at 72h, locked 2026-05-01):**
- Impressions: 1,795 (+443 since 24h)
- Likes: 43 (+3)
- Comments: 0 visible
- Reshares: 1 (no change)
- Comments/likes ratio: 0%

**Metrics (refresh 2026-05-03, ~5 days post):**
- Impressions: 1,867 (+72 since 72h lock — decelerating, as predicted)
- Likes: 43 (no change since 72h)
- Comments: 0 visible
- Reshares: 0 visible (the prior "1 repost" reading may have been the self-repost; no new reposts captured)
- Comments/likes ratio: 0%
- Trajectory: holds the "sequel decays faster than setup" hypothesis. At 5d the post is at 1,867 vs. the original "cold feet" which hit 2,530 by 7d. Projected 7d landing: ~1,950-2,100 → 🔴 verdict.

**Metrics (at 7 days — FINAL, locked 2026-05-04):**
- Impressions: 1,892 → **verdict: 🔴** (under 2,500)
- Likes: 43
- Comments: 0 visible
- Reshares: 0 visible
- Engagement rate: ~2.27% (likes-only; no comments dropped this below the cold-feet engagement rate of 2.73%)

**Metrics (post-FINAL refresh 2026-05-04 evening, ~6d):**
- Impressions: 1,899 (+7 since 7d lock — basically done)
- Likes: 43 (no change)
- Comments: 0 (no change)
- Reshares: 0 (no change)

**Metrics (post-FINAL refresh 2026-05-07, ~9d):**
- Impressions: 2,006 (+107 since 6d refresh — slow steady accrual past 7d)
- Likes: 43 (no change)
- Comments: 0 (no change)
- Reshares: 0 visible
- Note: Post crossed the 2,000 threshold post-7d. Verdict unchanged at 🔴 (the 7d FINAL is the lock).

**Notes:**
- This is the sequel post to the 2026-04-22 "cold feet" entry — direct A/B test of the "personal-journey post will cap ~3K but earn deepest engagement" hypothesis.
- **A/B result locked:** sequel post hit 1,892 imp at 7d vs. cold feet's 2,530 at 7d (and 2,662 at 11d). Sequel is 25% below setup. The decay-faster hypothesis holds.
- Comment count (0) is striking vs. cold feet (12 comments) — the reveal/takeaway format closes the dialogue gap. Numbered-list takeaway format = closed loop = no comments.
- Self-repost tactic deployed (one of Lior's posting rules).

**Learnings applied going forward:** When running a sequel to a personal-journey post, do NOT default to "X lessons learned" numbered list. The setup post invited dialogue (bulleted fears + "wish me luck"); the sequel closed it (numbered takeaways + "Don't think about it. Just go."). Sequel structure should keep the same dialogue invitation: leave one thing unresolved that readers can react to.

---

### 2026-04-28 — "I got rejected" / Director of Partnerships hiring post 🔴 FAILED
**Post URL:** https://www.linkedin.com/posts/liorpozin_i-got-rejected-over-and-over-and-over-share-7454884828262338560-Ca0E
**Topic tag:** #hiring #partnerships #founder-story
**Hook type:** Vulnerable confession ("I got rejected. Over and over and over.")
**Structure:** Hook → Personal-low setup → Stubbornness moment → Reversal proof → Department-importance pivot → Job-listing CTA (BAIT & SWITCH)
**Visual:** Image (Lior + creator photo, party setting)
**Length:** ~230 words
**CTA:** Hard — "Link is in the comments." (job listing for Director of Partnerships & Affiliations)

**Full post text:**
> I got rejected.
> Over and over and over.
> That feeling slowly creeps in - the one where you stop blaming the pitch, and start wondering if something is wrong with you.
> For the first 2 years of building AutoDS, almost no influencer would work with us.
> Cold DMs went unread.
> The ones that got a reply got "no thanks."
> We kept going.
> That stubbornness - refusing to accept no - is the reason this company exists.
> Today, type "dropshipping" into YouTube.
> The first result. The second. Third. Fourth. Fifth.
> All AutoDS partners. 200+ creators.
> The DMs go the other way now.
> Partnerships became one of the most important departments in the company.
> Which is why we're hiring the person who'll shape what's next.
> Director of Partnerships & Affiliations.
> Works directly with me and our CMO, Ofir Bokobza.
> The person taking this seat owns the channel that drives the company.
> - They treat creators as long-term partners, not vendors.
> - They decide who we work with, how the deals look, and what the program will be like three years from now.
> If you've spent your career running partnerships inside a company and you're ready to make this channel the main engine - that's the seat.
> Link is in the comments.
> AutoDS - Automatic Dropshipping Tools

**Metrics (at ~17h, snapshot 2026-04-29 morning):**
- Impressions: 860
- Likes: 34
- Comments: 1
- Reshares: 4
- Comments/likes ratio: ~3%

**Metrics (at ~18h, WebFetch 2026-04-29):**
- Likes: 35
- Comments: 1
- Reshares: not visible
- (impressions not exposed in public WebFetch view)

**Metrics (at 72h, locked 2026-05-01):**
- Impressions: 1,660 (+800 since 17h)
- Likes: 55 (+20)
- Comments: 1 (no change)
- Reshares: 4 (no change)
- Comments/likes ratio: ~2%
- Note: Likes nearly doubled overnight — likely from network reaction to recruiting CTA. But comments stayed flat at 1 → confirms the "closed CTA = no dialogue" diagnosis.

**Metrics (refresh 2026-05-03, ~5 days post):**
- Impressions: 1,811 (+151 since 72h lock — slow accrual, decelerating)
- Likes: 55 (no change since 72h)
- Comments: 1 (no change)
- Reshares: 4 (no change)
- Comments/likes ratio: ~2%
- Trajectory: Projects to ~1,900-2,100 at 7d → confirms 🔴 verdict pre-locked. The bait-and-switch diagnosis holds: post stalled completely between 72h and 5d (no new likes, no new comments).

**Metrics (at 7 days — FINAL, locked 2026-05-04):**
- Impressions: 1,925 → **verdict: 🔴** (under 2,500)
- Likes: 55
- Comments: 1
- Reshares: 4
- Engagement rate: ~3.12%
- Final note: Post landed exactly where the bait-and-switch diagnosis predicted. Likes nearly doubled in early window (network reaction to job CTA) but stalled completely after 72h. Comments stayed at 1 the whole way — no dialogue ever triggered. Locks in `feedback-no-hiring-ads-as-story-posts.md` as a confirmed third-time pattern.

**Metrics (post-FINAL refresh 2026-05-04 evening, ~5d):**
- Impressions: 1,941 (+16 since 7d lock — minimal long tail)
- Likes: 56 (+1)
- Comments: 1 (no change)
- Reshares: 4 (no change)
- Note: Marginal accrual past 7d lock. Post is effectively done.

**Metrics (TRUE 7d snapshot 2026-05-05, post originally published 2026-04-28):**
- Impressions: 2,066 (+125 since 2026-05-04 evening — slightly more late accrual than expected)
- Likes: 57 (+1)
- Comments: 1 (no change)
- Reshares: 4 (no change)
- Verdict unchanged: 🔴 (under 2,500). Locked 7d FINAL was prematurely set yesterday at 1,925 / 6d; the actual 7d mark holds at 2,066 — still in the 🔴 band. No analysis change.

**Metrics (post-FINAL refresh 2026-05-07, ~9d):**
- Impressions: 2,264 (+198 since 7d TRUE lock — surprising late accrual, likely from self-repost spinning around)
- Likes: 60 (+3)
- Comments: 1 (no change)
- Reshares: 4 (no change)
- Note: Post is still gaining slowly two weeks out. No change to 7d verdict. Comment count flat at 1 the entire run reinforces the bait-and-switch dialogue-killer diagnosis.

**Analysis (post-hoc, declared a failure by Reut at 18h):**
- **Why it failed: BAIT & SWITCH.** Hook promised a personal/founder vulnerability story ("I got rejected. Over and over and over."). 80% of the post delivered on that promise — strong stubbornness arc, concrete reversal proof (200+ creators, top 5 YouTube results). Then it hard-pivoted into a job listing for Director of Partnerships. Readers came for a story, got a recruiting ad. The trust break is the engagement killer.
- **What worked:** The first 80% of the post is gold — vulnerability hook, specific time anchor (2 years), concrete reversal numbers (200+ creators / top 5 YouTube). This story arc, ON ITS OWN, would have been a winner.
- **What didn't:**
  1. Pivot from founder-journey to "we're hiring [Role]" violates THE REAL PERSON PRINCIPLE (Lior content must not be AutoDS channel marketing).
  2. Closed CTA ("If you've spent your career running partnerships... that's the seat. Link is in the comments.") removed the engagement gap — only candidates have anything to react to. Per `feedback-linkedin-engagement-gap.md`, closed endings = no comments = algorithm flatlines.
  3. "Link in the comments" is a known recruiting-post signature → algorithm down-ranks vs. organic content.
  4. Comments-to-likes ratio at 18h (1:35 = ~3%) confirms zero dialogue triggered. Compare to "Wim Hof / cold feet" (11:57 = 19%) which was pure personal-journey, no CTA contamination.
- **vs. Lior's baseline:** Below median impressions (860 < median 1,783) AND below median likes (35 vs 32 — basically tied) AT 18h with no signs of acceleration. Trajectory points to 🔴 (under 2,500) at 7d.
- **vs. top-creator patterns:** Doesn't match any winner. The closest analog is the "Wim Hof / cold feet" personal-journey winner — but THAT post stayed in lane (no AutoDS pivot, no CTA). This post broke from the lane mid-flight.

**Learnings applied going forward:**
- New iron-clad rule: **Never blend a founder vulnerability story with a hiring CTA.** Filed as `feedback-no-hiring-ads-as-story-posts.md`.
- The story half is salvageable — repackage rejection → 200 creators arc as a standalone founder post with an open ending ("What's the 'no' that built your business?"). The hiring post can run separately the same week as a clearly-framed recruiting post (different expectations, different lane).
- Add this post to the failure pattern set in `lior-linkedin-data-rules.md` as a confirmed third-time pattern: "Story-to-CTA pivot kills the post."

**Next checkpoint:** 2026-05-01 (72h) → 2026-05-05 (7d FINAL).

---

### 2026-04-30 — find-skills / "AI finds skills for me"
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #ai #claude #tooling
**Hook type:** Behavior-shift confession ("I stopped searching for AI tools. Now AI finds them for me.")
**Structure:** Hook → Tool reveal (find-skills) → Numbered usage flow → Concrete example → Unexpected twist (Claude asked questions back) → Insight (sharper questions before code) → Punchline ("Wrong forum. Just ask Claude.") → Soft CTA to repo
**Visual:** Image (likely screenshot of find-skills in action)
**Length:** ~175 words
**CTA:** Soft — "Link to the find-skills repo in the first comment."

**Full post text:**
> I stopped searching for AI tools.
> Now AI finds them for me.
> For the past few weeks, I've been using something that changed how I work with Claude-
> It's called find-skills.
> A skill that finds other skills.
> 1. You describe your problem.
> 2. It scans the open-source skill libraries.
> 3. Pulls the ones that fit.
> 4. Then you tell Claude to plug them into your workflow.
> The first time I used it, I asked for something simple:
> "I need an agent that does QA on my code."
> It found four different skills for that job.
> I told Claude to learn from all of them.
> Built me one super agent.
> But here's what I didn't expect.
> Claude didn't just give me answers.
> It asked me the right questions about my code before I shipped it.
> The questions sharpened what I was trying to build before I wrote a single line.
> That's the part most people miss.
> Every AI group I'm in, someone is asking, "How do I do X with Claude?"
> Wrong forum.
> Just ask Claude.
> Link to the find-skills repo in the first comment.

**Metrics (at ~24h, snapshot 2026-05-01):**
- Impressions: 481
- Likes: 4
- Comments: 1
- Reshares: 0 visible
- Comments/likes ratio: 25% (only 1 comment though — small sample)

**Metrics (at 72h — LOCKED 2026-05-03):**
- Impressions: 639 (+158 since 24h — decelerating)
- Likes: 7 (+3)
- Comments: 1 (no change)
- Reshares: 1 (the self-repost — Lior reposted himself, surfaced on the activity feed as "Lior Pozin reposted this")
- Comments/likes ratio: ~14%
- Note: 72h velocity (158 impressions in 48h = ~3.3/hour) much weaker than 24h velocity (~20/hour). Algorithm gave up on this post fast. Self-repost tactic deployed.

**Metrics (refresh 2026-05-04, ~4 days post):**
- Impressions: 714 (+75 since 72h — almost stalled completely)
- Likes: 9 (+2)
- Comments: 1 (no change)
- Reshares: 1 (the self-repost still showing)
- Comments/likes ratio: ~11%
- Trajectory: Projects to ~800-900 at 7d → confirms 🔴 verdict, will be one of the lowest-performing posts logged.

**Metrics (refresh 2026-05-04 evening scan, ~4d):**
- Impressions: 722 (+8 since morning — fully stalled)
- Likes: 9 (no change)
- Comments: 1 (no change)
- Reshares: 1 (no change)
- Trajectory unchanged: projects to ~800 at 7d → 🔴 locked-in.

**Metrics (refresh 2026-05-05, ~5d):**
- Impressions: 746 (+24 since 2026-05-04 evening — ~5/day, basically dead)
- Likes: 9 (no change)
- Comments: 1 (no change)
- Reshares: 0 visible (self-repost no longer surfaces in feed view — same pattern as PocketOS)
- Trajectory: projects to ~770-800 at 7d → 🔴 confirmed.

**Metrics (at 7 days — FINAL, locked 2026-05-07):**
- Impressions: 792 → **verdict: 🔴 BOMBED** (well under 1,500 — bottom 10% of logged posts)
- Likes: 10
- Comments: 1
- Reshares: 0 visible (self-repost aged off the activity feed view, same as PocketOS)
- Engagement rate: ~1.39%
- Final note: Lowest 7d impression count of any logged post except the 70% rule baseline. Came in 35% below pre-projection range (770-800) — actually landed slightly above the floor of that range. Self-repost did not generate enough secondary lift to break out of the first-degree cap. Confirms three failure patterns: (1) positive AI-tool endorsement underperforms vs. contrarian conclusion; (2) "link in first comment" CTA is a known down-rank signal; (3) the "I stopped X. Now Y." time-contrast hook may be overused on Lior's profile.

**Analysis:**
- What worked: Topic is squarely in Lior's AI-tooling lane. Hook is concise. The "Claude asked me the right questions" insight is a real, specific moment — that's the kind of detail that usually travels.
- What didn't: Three compounding signals dragged it down: (1) endorsement framing (no contrarian edge — Paperclip's win was the contrarian flip "the zero human company story is marketing"), (2) "Link in first comment" pattern matches recruiting-post signatures the algorithm down-ranks, (3) time-contrast hook reused too soon after 70% rule (also a 🔴 at 1,783).
- vs. Lior's baseline: 38% of median (792 vs. 2,066 median pre-this-lock). Worst 7d FINAL of any logged post.
- vs. top-creator patterns: Doesn't match a winning Lior pattern. Endorsement-style AI-tool posts haven't won yet; only contrarian-conclusion AI takes (Paperclip 30K) have broken through.

**Learnings applied going forward:**
- AI-tool posts MUST carry a contrarian conclusion. Positive endorsement = algorithm reads as marketing → first-degree cap → 🔴.
- Avoid "Link in first comment" — known down-rank signature when paired with founder vulnerability or product-style hook.
- Park the "I stopped X. Now Y." hook for 90+ days — it's been used twice in 30 days and both flopped.
- Filed as fourth confirmed failure for the under-2,500 cap pattern in [lior-linkedin-data-rules.md](lior-linkedin-data-rules.md).

---

### 2026-05-04 — PocketOS / "How does the worst mistake of your career become a personal brand win?"
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #ai #failure #brand #building-in-public
**Hook type:** Question hook ("How does the worst mistake of your career become a personal brand win?")
**Structure:** Hook (question) → Story setup (Jeremy Crane / PocketOS) → Failure detail (9 seconds, prod DB deleted, backups too) → Reframe ("Was it the team's fault? Absolutely. But...") → Counter-move (Crane went viral with public breakdown) → 3-bullet lesson list (min permissions, off-service backups, post failures) → Personal anchor (AutoDS hack story / Facebook Live) → Close ("Real brands aren't built when everything works. They're built on what breaks.")
**Visual:** Image (Jeremy Crane / Lior; Activate to view larger image)
**Length:** ~210 words
**CTA:** None (open close — closing line is a quotable principle)

**Full post text:**
> How does the worst mistake of your career become a personal brand win?
> Jeremy Crane, The CEO of PocketOS, just gave a masterclass in building in public when it breaks.
> Here's the story:
> An AI agent at PocketOS did something no one asked it to do.
> In 9 seconds, the production database was deleted. Backups too.
> 3 months of customer data vanished.
> The rules were in the system prompt.
> It violated every one.
> Was it the team's fault? Absolutely.
> But...
> Most founders in this situation would have hidden in their Slack DMs and quietly rebuilt the company.
> Crane did the opposite.
> He posted a long, public breakdown on X that went viral.
> His authority only grew from there.
> Here's what everyone running AI can learn from this:
> 1. Minimum permissions only.
> Separate tokens for staging and production.
> 2. Backups off-service.
> If your AI can delete the data, it shouldn't be able to delete the backup.
> 3. Post your failures. Take ownership.
> They can build more brand than any win.
> Years ago, hackers broke into AutoDS and changed every customer's username overnight.
> I went live on Facebook the same day.
> Walked everyone through what happened, why, and what we were doing to prevent it.
> Zero customers left.
> Real brands aren't built when everything works.
> They're built on what breaks.

**Metrics (at ~16h, snapshot 2026-05-04):**
- Impressions: 721
- Likes: 9
- Comments: 2
- Reshares: 1 (the self-repost — visible on activity page as "Lior Pozin reposted this")
- Comments/likes ratio: ~22%

**Metrics (at ~18h, snapshot 2026-05-04 evening):**
- Impressions: 769 (+48 in ~2h — still accruing)
- Likes: 10 (+1)
- Comments: 2 (no change)
- Reshares: 1 (the self-repost still showing)
- Comments/likes ratio: 20%
- 24h checkpoint due tomorrow morning (2026-05-05).

**Metrics (at 24h — LOCKED 2026-05-05):**
- Impressions: 1,029 (+260 since 18h — decent overnight pickup)
- Likes: 11 (+1)
- Comments: 2 (no change)
- Reshares: 0 visible (the self-repost no longer surfaces in the activity feed view at 1d window — appears to have aged off or got deduped behind the latest post)
- Comments/likes ratio: ~18%
- Velocity check: 1,029 imp at 24h is roughly 2x find-skills 24h pace (481) and ~70% of "I got rejected" 24h trajectory. Tracking middle-of-pack — not the Paperclip lane (would need ~3-4K at 24h to project into the 🟡/✅ band).

**Metrics (at 72h — LOCKED 2026-05-07):**
- Impressions: 1,166 (+137 since 24h — big slowdown after first day)
- Likes: 14 (+3)
- Comments: 2 (no change)
- Reshares: 0 visible (self-repost still aged off feed view)
- Comments/likes ratio: ~14%
- Velocity check: 137 imp gain over 48h = ~2.85 imp/hour, vs. the first 24h pace of ~43/hour. Algorithm gave up after day 1. Projects to ~1,400-1,600 at 7d → 🔴 verdict likely. Doesn't break the under-2,500 cap.

**Next checkpoint:** 2026-05-11 (7d FINAL).

**Notes:**
- Topic is AI/contrarian-conclusion — same lane as Paperclip (30K imp ⭐). The hook is a question instead of a confession this time, but the pattern (commentary-on-trending-AI-failure with personal anchor) matches the Paperclip template.
- Personal anchor: dollar-bug / hack story (the AutoDS Facebook Live moment) — see [lior-story-dollar-bug.md](lior-story-dollar-bug.md) for canonical version. Pattern reuse working as intended.
- 16h impressions (721) tracking ahead of find-skills (481 at 24h) but well below Paperclip pace. Hard to project — may go either way.
- Self-repost deployed within first day.
- Closing line ("Real brands aren't built when everything works. They're built on what breaks.") is a quote-card moment — high save/share potential if it gets reach.

**Next checkpoints:** 2026-05-05 (24h), 2026-05-07 (72h), 2026-05-11 (7d FINAL).

---

### 2026-05-05 — Coffee in Manhattan / "100 videos in 100 days" YouTube origin story
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #founder-story #content #youtube #channel-building
**Hook type:** Setup-twist confession ("We built a software that actually worked. The only problem? Nobody gave a damn.")
**Structure:** Hook (setup-twist) → Action (flew to NYC for influencer coffee) → Specific scene (1hr in coffee shop, 40 phone checks) → Stood-up beat → Flight-home reframe → Decision moment ("never let one stranger be the bottleneck") → Pivot ("we'd build our own channel") → Action arc ("100 videos in 100 days") → Crickets beat → Outcome (397K subs) → Quotable closer ("The coffee is much better in Tel Aviv anyway")
**Visual:** Document/carousel ("Your document is loading" surfaced in feed — likely a slide deck or PDF carousel)
**Length:** ~225 words
**CTA:** None (open close — quotable line, no question, no link)

**Full post text:**
> We built a software that actually worked.
> The only problem?
> Nobody gave a damn.
> So I did the logical thing: I flew across the world to buy a 20-year-old influencer a coffee.
> We set the meeting in a coffee shop in Manhattan.
> I sat there for an hour.
> Checking my phone 40 times.
> He didn't show up.
> I wanted to flip a table, but settled for aggressively refreshing my Gmail instead.
> I walked back to the hotel, feeling like an absolute idiot.
> On the flight back to Tel Aviv, I was just pissed off.
> I decided right there: I'd never let one stranger be the bottleneck between our customers and us again.
> We'd build our own channel.
> So we went all in.
> 100 videos in 100 days.
> At first? Crickets.
> It felt like shouting into a completely empty room.
> But then the algorithm caught up.
> Today, the AutoDS - Automatic Dropshipping Tools YouTube channel has 397K subscribers.
> I still don't know what that influencer is doing today.
> But if I had just flown home and accepted defeat, we'd still be at the mercy of someone else's calendar.
> The coffee is much better in Tel Aviv anyway.

**Metrics (at ~17h, snapshot 2026-05-05 morning):**
- Impressions: 1,062
- Likes: 19
- Comments: 2
- Reshares: 1 (self-repost already deployed within first day — surfaced as "Lior Pozin reposted this" duplicate at top of activity feed)
- Comments/likes ratio: ~11%

**Notes:**
- Pure founder-journey post in the "real person on a real path" lane — vulnerability-first hook, specific scene details (NYC coffee shop, 40 phone checks, flight home), and a quotable closer with no CTA. Matches the Wim Hof / cold feet template that earned the deepest engagement rate of any logged post.
- DOES include AutoDS YouTube channel mention (397K subs) — but as a story payoff, not a marketing channel. Different from the bait-and-switch failure of "I got rejected": there's no hiring CTA, no "link in comments," the AutoDS reference is the punchline of Lior's own story arc.
- Self-repost tactic deployed within first day (per linkedin-posting-rules.md).
- 17h impressions (1,062) tracking ahead of PocketOS 18h pace (769) and find-skills 24h (481). On rough trajectory, projects somewhere in 2,000-3,500 range at 7d if velocity holds — would make it the first 🟡 (middling band) post since Paperclip if it lands above 2,500.
- Hook structure ("We built X that worked. The only problem? Nobody gave a damn.") is the first time we've seen this exact setup-twist on Lior's profile. Worth tracking — could be a new winning template.

**Next checkpoints:** 2026-05-06 (24h — MISSED, Chrome down), 2026-05-08 (72h), 2026-05-12 (7d FINAL).

**Metrics (at ~48h, snapshot 2026-05-07 — 24h checkpoint missed yesterday due to Chrome outage):**
- Impressions: 1,954 (+892 since 17h, +925 since 18h on day-of)
- Likes: 29 (+10)
- Comments: 7 (+5)
- Reshares: 1 (the self-repost)
- Comments/likes ratio: ~24%
- Velocity check: 892 imp gain over ~31h is roughly 28 imp/hour — actually *accelerating* into day 2, opposite of the typical decay curve. 7 comments at 48h is the highest dialogue rate of any logged post except cold-feet (12 at 7d). Strong A/B signal that the founder-journey lane (vulnerability hook + scene detail + open close) is repeatable.
- Trajectory: at 1,954 by 48h with comments still rolling, projects 2,500-3,500 at 7d → first 🟡 (or even ✅) verdict since Paperclip if velocity holds. Worth flagging as the standout post of this scan.

---

### 2026-05-06 — LangTalks AI Engineering Conference recap
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #ai #agents #conference-recap
**Hook type:** Time-anchor + listicle promise ("If you're building with agents in 2026... here are the shifts I walked away with")
**Structure:** Hook → Setup (LangTalks AI Engineering Conference, yesterday) → Numbered shifts (1. Prompts stopped being the focus 2. The bugs got much harder to find 3. Gamification for agents is the next big hit) → Per-shift commentary → Specific tool callout (AgentCraft / Ido Salomon) → Personal frame ("This is exactly how I think about work. Business is a game.") → Closer ("The field grew up.") → Open question + thanks
**Visual:** Image (carousel, "Activate to view larger image" surfaced)
**Length:** ~225 words
**CTA:** Open question — "Which shift hits you hardest?"

**Full post text:**
> If you're building with agents in 2026, you know how fast things are going.
> I spent yesterday at LangTalks AI Engineering Conference, and here are the shifts I walked away with:
> 1. Prompts stopped being the focus.
> We are in a new era.
> Nobody on stage talked about prompting. They talked about the system around the agent: tracing, wiring, feedback loops. Writing a prompt is the easy part.
> The actual job is to ensure the prompt works the same way on day 30 as on day 1.
> 2. The bugs got much harder to find.
> The output looks fine in every spot check.
> Then you open the dashboard and realize something has been off for a month.
> No crash, no error, just a quiet decline.
> Monitoring AI stopped being debugging. It became observation.
> 3. Gamification for agents is the next big hit.
> Not every builder wants to live inside a black terminal.
> Different people, different work styles, and tools should reflect that.
> The standout demo was AgentCraft by Ido Salomon. A Warcraft-style platform that turns AI agents into units on a map, making human-AI collaboration something you can actually see.
> This is exactly how I think about work. Business is a game.
> The field grew up. Less hype, more execution.
> Which shift hits you hardest?
> Thanks to Gal Peretz and Lee Twito for the production, and to all the AI agents in the audience, who probably implemented the talks before I left the building (:

**Metrics (at ~24h, snapshot 2026-05-07):**
- Impressions: 486
- Likes: 7
- Comments: 1
- Reshares: 0 visible
- Comments/likes ratio: ~14%

**Notes:**
- Conference-recap post in the AI-tooling lane. Recap-format flag: per [feedback-conference-recap-posts-flatline.md](feedback-conference-recap-posts-flatline.md), conference recap posts flatline at ~400 impressions without an AutoDS-Operator stake. This post stays at stage-observation level (3 shifts from talks + AgentCraft demo + thanks-to-organizers) without naming a specific AutoDS production moment that ties the lessons back to Lior's daily reality.
- 486 imp at 24h tracks worse than find-skills (481 at 24h, ended at 792 7d FINAL 🔴). Projects to ~700-900 at 7d → 🔴 lock-in likely.
- Open question CTA ("Which shift hits you hardest?") is the right shape, but the recap framing already suppressed reach below the threshold where the question can earn dialogue.
- Hook ("If you're building with agents in 2026, you know how fast things are going") is generic AI-Twitter wallpaper; doesn't carry Lior-specific stake or contrarian edge.
- Confirms third instance of conference-recap posts underperforming; locks the [feedback-conference-recap-posts-flatline.md](feedback-conference-recap-posts-flatline.md) rule.

**Next checkpoints:** 2026-05-09 (72h), 2026-05-13 (7d FINAL).

---

### 2026-05-06 — Founder salary trap / "Pay yourself enough to think straight"
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #founder-story #money #leadership
**Hook type:** Setup-twist confession ("My company was making millions, but I had zero in my bank account.")
**Structure:** Hook (setup-twist) → Personal admission ("For the first 5 years of AutoDS, I didn't take a salary") → Self-correction ("I was wrong") → Two-sided trap framing (take too much / take too little) → Year-anchored rule ("9 years in, here's my rule") → Quotable principle ("Pay yourself enough to think straight") → Mechanism explainer (survival mode → judgment → desperate decisions) → Open question close
**Visual:** Image (carousel, "Activate to view larger image" surfaced — 2 images)
**Length:** ~150 words
**CTA:** Open question — "Founders, how did you find your sweet spot number?"

**Full post text:**
> My company was making millions, but I had zero in my bank account.
> For the first 5 years of AutoDS, I didn't take a salary.
> Every dollar went back into the business.
> "This is what it takes," I told myself.
> I was wrong.
> Setting your own salary is a founder's mental trap:
> - Take too much: You look like a lifestyle founder.
> - Take too little: You work your ass off, but can't cover rent. It's hard to keep up in the long run.
> 9 years in, here's my rule for every first-time founder: Pay yourself enough to think straight.
> Enough to move money stress into the background.
> When you're in survival mode, your judgment is the first thing to go.
> If you're worried about your personal bank account, you'll make desperate decisions for your company's bank account.
> Founders, how did you find your sweet spot number?

**Metrics (at ~17h, snapshot 2026-05-07):**
- Impressions: 1,861
- Likes: 19
- Comments: 0 visible
- Reshares: 1 (self-repost already deployed — surfaced as "Lior Pozin reposted this" at top of feed)
- Comments/likes ratio: 0% (early)

**Notes:**
- Pure founder-journey post in the "real person on a real path" lane. Strong opening velocity: 1,861 imp at 17h is the second-highest 17-18h read of any post except Paperclip — tracking faster than Coffee/100-videos (1,062 at 17h, currently breakout at 1,954 by 48h).
- Setup-twist hook ("making millions, but I had zero in my bank account") matches the Coffee post's winning structure ("software that worked. The only problem? Nobody gave a damn"). This is the second confirmed use of setup-twist; both early-tracking strong.
- Vulnerability + concrete number anchor + open dialogue question = textbook personal-journey winner format.
- Self-repost deployed within first day (per linkedin-posting-rules.md).
- Open question ("how did you find your sweet spot number?") is specific and answerable in one line — the kind of close that earns comments. 0 comments at 17h is early — the post just dropped.
- Quotable principle ("Pay yourself enough to think straight") is a save-card moment.
- Topic — founder finances/salary — is unprecedented in this log. If it lands strong, that's a new winning lane to test.
- **Trajectory if velocity holds:** 1,861 at 17h, with self-repost deployed and dialogue not yet triggered, projects 3,500-5,500 at 7d → first 🟡 / 🟡-bridge-✅ verdict since Paperclip. Strong candidate for next-window standout post.

**Next checkpoints:** 2026-05-08 (24h), 2026-05-09 (72h), 2026-05-13 (7d FINAL).

**Metrics (at post-window back-capture 2026-05-19, ~13 days post-publish):**
- Impressions: **4,614** → **verdict: 🟡 (middling band, just above the 2,500 floor)**
- Likes/Reactions: 31
- Comments: 4
- Reshares: 1
- Engagement rate: ~0.78%

**Metrics (refresh 2026-05-19 10:13 daily scan, ~13 days):**
- Impressions: 4,634 (+20 since weekly digest snapshot — slow long-tail accrual continues)
- Likes/Reactions: 31 (no change)
- Comments: 4 (no change)
- Reshares: 1 (no change)
- Note: 🟡 verdict locked. Long-tail accrual (+20 imp in 17h) is unusual for posts past 7d — suggests the reshare is still seeding new audiences. Hold at 🟡.

**Final analysis:**
- ✅ Setup-twist hook lane confirmed working — second 🟡 verdict in Lior's log (after Wim Hof cold-feet at 2,662).
- 🟡 verdict puts founder salary trap as Lior's second-best logged post on raw impressions, but engagement (31 reactions on 4,614 imp = ~0.67%) is weaker than Wim Hof (60 reactions on 2,662 = 2.25%).
- Topic novelty (founder finances/salary, unprecedented in log) gave the algorithmic boost. Setup-twist hook closed the deal.
- Confirms hypothesis from 2026-05-11 digest: setup-twist + concrete number + open question = repeatable.

---

### 2026-05-10 — Anthropic / MD→HTML workflow trick → ⭐ MEGA-WINNER (BACK-CAPTURED 2026-05-19)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7459595864215511042/
**Topic tag:** #ai #claude #anthropic #workflow #building-in-public
**Hook type:** Trending-tool callout + insider workflow promise ("Anthropic's team just dropped the workflow trick they use internally")
**Structure:** Hook (insider scoop) → Tribe-callout ("approve all without reading gang") → The shift in one phrase (MD files → HTML) → Personal proof ("45 design screens reviewed in one afternoon") → 3-step how-to (Make it HTML / Approve+Changes buttons + comment fields / "Fix the notes" agent loop) → Meta-principle ("human brain isn't built to process walls of plain text") → Quotable closer ("reviewing at the speed at which the brain runs. And it is much more fun.")
**Visual:** Image (Anthropic + Claude branding, probable carousel preview)
**Length:** ~210 words
**CTA:** None (open close — quotable principle, no question, no link)

**Full post text:**
> Anthropic's team just dropped the workflow trick they use internally.
> If you're in the "approve all without reading" gang, here's the shift you need to take-
>
> MD files → HTML.
>
> Tested it last week.
> 45 design screens reviewed in one afternoon.
>
> How to start:
> 1. Tell Claude: "Make it an HTML file."
> That's it.
>
> And if you want to level up:
>
> 2. Add comment fields right on the page, so you can approve and request changes directly on what you see.
>
> "Build me an HTML page for [your content], with Approve/Changes buttons and comment fields on each item. Save notes to a local file."
>
> 3. When done leaving notes, write: "Fix the notes." The agent reads every comment, applies the fixes, and ships the next version.
>
> The human brain isn't built to process walls of plain text. We need color, layout, and visual hierarchy that we can scan at a glance.
>
> A visual surface means reviewing at the speed at which the brain runs. And it is much more fun.

**Metrics (post-window back-capture 2026-05-19, ~9 days post-publish — true 7d FINAL was 2026-05-17):**
- Impressions: **92,869** → **verdict: ⭐ EXCEPTIONAL** (new all-time record, 3x the previous Paperclip ceiling of 30,009)
- Likes/Reactions: 56
- Comments: 24
- Reshares: 9
- Engagement rate: ~0.10% (low ratio, but absolute reach is the headline)

**Metrics (refresh 2026-05-19 10:13 daily scan, ~9 days):**
- Impressions: 92,874 (+5 since weekly digest snapshot — essentially locked)
- Likes/Reactions: 56 (no change)
- Comments: 24 (no change)
- Reshares: 9 (no change — not visible in feed view today; counted from yesterday's digest)
- Note: Post is past its growth window. Locks the ⭐⭐ NEW ALL-TIME RECORD at ~92.9K imp.

**Metrics (refresh 2026-05-20 10:13 daily scan, ~10 days):**
- Impressions: 92,898 (+24 since 2026-05-19 — fully locked, residual long-tail only)
- Likes/Reactions: 56 / Comments: 24 / Reshares: 9 — unchanged. ⭐⭐ ALL-TIME RECORD confirmed stable.

**Metrics (long-tail refresh 2026-05-23 10:13 daily scan, ~13 days):**
- Impressions: **92,959** (+61 since 2026-05-20 — pure long-tail, post fully done). Likes/Reactions: 56 / Comments: 24 / Reshares: 9 — all unchanged. ⭐⭐ ALL-TIME RECORD stable at ~93K.

**Analysis:**
- What worked:
  - Topic = Anthropic (massive AI-Twitter/LinkedIn surface area + Claude tribal pull). Same Paperclip-lane principle: contrarian-take + trending-tool = first-degree-network-busting reach.
  - Hook ("Anthropic's team just dropped the workflow trick they use internally") combines insider-access framing + "trick" promise + specific company name. This is a stronger hook than Paperclip's question hook.
  - Tribe-callout ("approve all without reading gang") creates an identity trigger — readers immediately self-sort.
  - Three concrete prompts copy-pasteable. Save-card material.
  - Meta-principle in close ("human brain isn't built for plain text") is a quotable aphorism that lifts the post above tactical "how-to" content.
  - No CTA, no link, no question. The post earns dwell on its own.
- What didn't:
  - Engagement rate (~0.10%) is low. Reach blew past first-degree network into cold AI-audience territory — many viewers landed but didn't engage.
  - 9 reposts is modest given 92K imp (vs. Bartlett Henry Ford post 352 reposts for ~3K reactions — different metric, but signals lower share-worthiness).
- vs. Lior's baseline: **TOP 1 OF ALL TIME** — replaces Paperclip as the #1 post in the log (was 30,009).
- vs. top-creator patterns: This is the same DNA as the 2026-04-20 Paperclip post: trending AI tool + contrarian/insider framing + concrete how-to + open close. Lior has now produced TWO mega-winners in the contrarian-AI-take lane. **This is the only repeatable winning pattern on Lior's profile.**

**Learnings applied going forward:**
1. Contrarian-AI-take lane is now confirmed-repeatable (n=2: Paperclip 30K → Anthropic 92K).
2. Trending-tool callout in the FIRST 7 WORDS (Anthropic) + tribe-callout in next sentence ("approve all without reading gang") drives the algorithm + identity pull.
3. The "no CTA" close still works at scale — Anthropic post broke records without a question, link, or hashtags.

**Rolling Benchmark Impact:**
- New top 10% floor: should reset, but Anthropic at 92K is a 3x outlier — treat as a new ceiling, not a baseline.
- Median impressions will NOT shift on this post alone (medians are robust to outliers). But the mean impressions metric jumps significantly.

---

### 2026-05-12 — Master Prompt / "AI wrote exactly like you" (5-step playbook)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7459958268761821184/
**Topic tag:** #ai #branding #playbook #prompt-engineering
**Hook type:** Question hook + problem statement ("Tired of re-explaining who you are to every new AI chat? Here's the one problem with AI: People can smell it.")
**Structure:** Question hook → Problem statement (AI-generated content is detectable) → Promise reframe ("what if your AI wrote exactly like you?") → Solution name (Master Prompt) → Mechanism (one doc → every chat → ChatGPT/Claude/Gemini/Grok) → 5-step playbook (IDENTITY, MINDSET, VOICE, GUARDRAILS, TEST+PORT) with ☑ checkmark sub-bullets → [truncated remaining steps]
**Visual:** Image
**Length:** ~280+ words (truncated by LinkedIn display)
**CTA:** Implicit playbook-followthrough

**Metrics (at ~6.5 days post-publish, snapshot 2026-05-19 weekly digest):**
- Impressions: **516** → **verdict: 🔴 BOMBED** (challenges find-skills 792 for new floor)
- Likes/Reactions: 9
- Comments: 0
- Reshares: 0

**Metrics (at TRUE 7d FINAL, locked 2026-05-19 10:13 daily scan):**
- Impressions: **520** → **verdict: 🔴 BOMBED FINAL** (under 1,500, bottom-decile of log)
- Likes/Reactions: 9 (no change)
- Comments: 0 (no change)
- Reshares: 0 (no change)
- Engagement rate: ~1.73%
- Note: +4 imp in the 17h between weekly digest snapshot and 7d TRUE lock. Post is fully stalled. Verdict unchanged from yesterday's pre-7d lock.
- Long-tail refresh 2026-05-23: **546** imp (+26 since FINAL), 9 reactions, 0 comments — residual accrual only, verdict 🔴 unchanged.
- Long-tail refresh 2026-05-26 10:13 daily scan (~14d): **602 imp** (+56 since 2026-05-23 546), 9 react, 0 comm, 0 reshares — slow residual, verdict 🔴 BOMBED FINAL unchanged.

**Analysis:**
- What worked: Topic stays in AI tooling lane that has produced winners (Paperclip, Anthropic). Question hook + problem statement is a standard playbook opening.
- What didn't:
  - **Hyper-tactical "5-step playbook with ☑ checklist sub-bullets" format closed the post off to reader projection.** Unlike Anthropic (which had 3 concrete prompts but framed by a meta-principle), Master Prompt is all tactics with no story arc, no scene, no personal stake.
  - 0 comments. The post invites copy-paste, not dialogue.
  - "People can smell it" hook is fine but the body doesn't earn the contrarian edge the hook promised.
  - Same lane as Paperclip/Anthropic but different DNA: this is a "how to use AI better" post (creator-lane productivity tip), not a "look at this AI failure / breakthrough" commentary on a specific trending tool. **The lane works only when there's a topical news anchor.**
- vs. Lior's baseline: 516 imp = lower-quartile of the log. Sits with find-skills 792 and LangTalks ~700 in the under-1K BOMBED bracket.
- Confirms feedback rule [feedback-no-productivity-tool-tips.md](feedback-no-productivity-tool-tips.md): AI workflow tips / "how to use [tool]" posts don't perform for Lior. Creator lane, not CEO lane.

**Learnings applied going forward:**
- **NEVER post a "playbook" / "how to use AI" tactical breakdown without a specific news anchor or production failure as the frame.** The AI lane works on commentary, not tactical instruction.

---

### 2026-05-14 — "Treat yourself like a product" / Personal OKRs
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7460693568081289216/
**Topic tag:** #founder-story #wellness #personal-okrs #leadership
**Hook type:** Time-contrast claim ("One idea completely changed the way I run my company-")
**Structure:** Hook → Idea name ("Treat yourself like a product") → Contrast frame ("weeks on product roadmap, but your own growth? Bottom of list") → Vulnerability ("Pushing at 200% to win a market is one thing. The real challenge is building a life that doesn't collapse while you do it.") → 3-point system (Personal OKRs / Prioritize / Buying Shortcuts — coach) → Quotable closer ("You'd never ship a product without a roadmap, testing, and iteration. Why run yourself without one?")
**Visual:** Image
**Length:** ~165 words
**CTA:** None (rhetorical question close)

**Full post text:**
> One idea completely changed the way I run my company-
> Treat yourself like a product.
> You spend weeks on your product roadmap, but when it comes to your own growth?
> Bottom of the list.
> The truth? It isn't simple.
> Pushing at 200% to win a market is one thing.
> The real challenge is building a life that doesn't collapse while you do it.
> Three things that help me stay on the list:
> 1. Personal OKRs: I roadmap my health and growth exactly like a new feature.
> Exercises and learning time are defined and scheduled.
> 2. Prioritize: No matter what's on my desk, I'm home for dinner with my wife.
> 3. Buying Shortcuts: Just as I hire experts in business to move faster, I hired a personal coach to shorten my learning curve and fix my own bugs.
> You'd never ship a product without a roadmap, testing, and iteration.
> Why run yourself without one?

**Metrics (at ~5 days post-publish, snapshot 2026-05-19 weekly digest):**
- Impressions: **403** → **verdict: 🔴 BOMBED** (lowest of any logged post)
- Likes/Reactions: 10
- Comments: 0
- Reshares: 0

**Metrics (refresh 2026-05-19 10:13 daily scan, ~5 days):**
- Impressions: 425 (+22 since weekly digest snapshot — minimal accrual)
- Likes/Reactions: 10 (no change)
- Comments: 0 (no change)
- Reshares: 0 (no change)
- Note: Post effectively done. Will hit TRUE 7d FINAL on 2026-05-21. Trajectory holds 🔴 BOMBED (well under 1,500).

**Metrics (refresh 2026-05-20 10:13 daily scan, ~6 days):**
- Impressions: **472** (+47 since 2026-05-19 — minimal accrual)
- Likes/Reactions: 11 (+1)
- Comments: 1 (+1)
- Reshares: 0 (no change)
- Note: TRUE 7d FINAL due tomorrow (2026-05-21). At 472 imp the verdict is locked-in 🔴 BOMBED regardless — remains the worst-performing post in the log. One comment finally appeared at ~6d but dialogue never formed. (Visual: post carries a "put it in the backlog / but never do" meme image — a self-deprecating product-backlog meme that doesn't reinforce the "treat yourself like a product" thesis; post shows "Edited", so media may have been swapped post-publish.)

**Metrics (7d FINAL locked 2026-05-23 10:13 daily scan, ~9 days — scans on 05-21/05-22 did not run):**
- Impressions: **518** → **verdict: 🔴 BOMBED FINAL** (under 1,500; remains the worst-performing post in the log)
- Likes/Reactions: 13 (+2 since 2026-05-20)
- Comments: 2 (+1)
- Reshares: 0 (no change)
- Engagement rate: ~2.9%
- Note: TRUE 7d checkpoint (2026-05-21) was missed (daily scan did not run 05-21 or 05-22). Captured at ~9d. Post fully stalled at 518 imp; verdict 🔴 BOMBED was already locked-in at the 05-20 reading. **NEW WORST in the log confirmed** (518 < find-skills 792).
- Long-tail refresh 2026-05-25 10:13 daily scan (~11d): 558 imp (+4 since digest's 554), residual only — verdict 🔴 BOMBED unchanged, remains the worst-performing post in the log.
- Long-tail refresh 2026-05-26 10:13 daily scan (~12d): **572 imp** (+14 since 2026-05-25 558), 13 react (+0 net since 11 visible 05-25; reads as "Sharon Gidron Peskin and 12 others"), 2 comm, 0 reshares — residual only. Verdict 🔴 BOMBED unchanged, still the worst-performing post in the log.

**Analysis:**
- What worked: "I'm home for dinner with my wife" is genuine vulnerability + concrete priority. Closing rhetorical question is on-brand. "200% to win a market" hits Pillar #1 (lives on 200).
- What didn't:
  - Wellness/personal post WITHOUT the founder-bridge to a friction or open ending — exactly the pattern flagged in [feedback-linkedin-wellness-personal-needs-founder-bridge.md](feedback-linkedin-wellness-personal-needs-founder-bridge.md).
  - No specific story moment, no scene, no number anchor.
  - "Personal coach" sub-bullet is generic wellness content; doesn't carry the operator-CEO stake.
  - Hook "One idea completely changed..." is generic LinkedIn-bait; doesn't promise specificity.
  - 0 comments at 5d = dialogue never started.
- vs. Lior's baseline: **NEW WORST** in the log (403 < find-skills 792).
- Rule applied: wellness/personal content needs concrete friction + production-tie to land. Confirmed 3rd time.

**Learnings applied going forward:**
- **Wellness / personal-OKR posts MUST include a specific operator scene** (e.g., a specific board meeting where lack of sleep cost a decision; a specific production crisis that taught the priority). Without it, this lane is a guaranteed BOMB on Lior's profile.

---

### 2026-05-18 — Funnel conversion 40% / Build Your Store AI / Shopify
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7462130051736563712/
**Topic tag:** #product #funnel #partnership #conversion
**Hook type:** Outcome-stat claim ("We just lifted our funnel conversion rate by over 40% with one test.")
**Structure:** Hook (40% claim) → "Here's what we actually did" → 5-step process (drop identification / customer interviews / pre-tests / 2-year focus / iteration) → Outcome stat (hit annual BYS AI target in single quarter) → Meta-principle ("The headline is the one that worked. The real story is the 30 that almost didn't.") → Partner thank-you list (8 internal + 3 Shopify)
**Visual:** Image
**Length:** ~180 words
**CTA:** None (thank-you close)

**Full post text:**
> We just lifted our funnel conversion rate by over 40% with one test.
> Here's what we actually did:
> 1. Found the biggest drop in the funnel.
> 2. Talked to customers until we understood why they dropped.
> 3. Ran pre-tests to see which angles moved the needle for those customers.
> 4. We pushed for 2 years to fix this specific main funnel drop, without jumping between different small opportunities; we focused on the main big one.
> 5. We set this as the main goal, and we kept iterating until it worked.
> Then this month, we just hit our annual Build Your Store AI target in a single quarter.
> The headline is the one that worked.
> The real story is the 30 that almost didn't.
> Huge thanks to Yuval Wilf, Viacheslav Hryhorash, Natalia Soshko, Max Kardanets, Aliaksandr Baryhin, Mykhailo L., Valeriia Pukhir, and to Christiana Gianzanti, Shayna Massey, Michelle Pushefski from Shopify for being true partners.

**Metrics (at ~7h post-publish, snapshot 2026-05-19 weekly digest):**
- Impressions: **1,728** at 7h
- Likes/Reactions: 47
- Comments: 9
- Reshares: 9
- Comments/likes ratio: ~19%

**Metrics (at ~18h post-publish, snapshot 2026-05-19 10:13 daily scan):**
- Impressions: **2,182** (+454 in 11h — sustained velocity past first day, ~41 imp/hour)
- Likes/Reactions: 56 (+9)
- Comments: 9 (no change)
- Reshares: 9 (no change)
- Comments/likes ratio: ~16%
- Note: Reactions accelerated (47→56) while comments held flat at 9. Sustained 41 imp/hour rate past the typical 12-18h decay point is a positive signal. 24h checkpoint due tomorrow morning.

**Metrics (at ~42h post-publish / ~2 days, snapshot 2026-05-20 10:13 daily scan):**
- Impressions: **2,793** (+611 in ~24h — velocity holding, ~25 imp/hour)
- Likes/Reactions: 65 (+9)
- Comments: 11 (+2)
- Reshares: 9 (no change)
- Comments/likes ratio: ~17%
- Note: 24h checkpoint was not separately captured (no dedicated scan inside the 24h window; nearest pre-24h reading is 2,182 @ 18h on 2026-05-19). Steady accrual past 24h. Projecting ~4,000-5,000 at 7d → 🟡 likely, outside chance of ✅.

**Analysis (early):**
- What worked: 9 reshares at 7h is unusually high (Anthropic had 9 at full 7d). Comments-to-likes ratio (19%) suggests dialogue forming.
- Caveats:
  - Outcome-stat hook with no personal stake — standard product-marketing opener.
  - "The headline is the one that worked. The real story is the 30 that almost didn't." is a quotable line and a save-card moment.
  - Long thank-you list (11 named people) bloats the close and may suppress dwell past line ~140.
  - Topic = product partnership + Shopify proximity. Shopify mention is on-brand (key partner per [feedback-never-criticize-shopify.md](feedback-never-criticize-shopify.md)).
- Trajectory: 1,728 at 7h is on par with PocketOS pace (1,029 at 24h). Projects 2,500-4,500 at 7d → likely 🟡.
- vs. Lior's baseline: Tracking middle of pack, not in the contrarian-AI lane that produces ⭐ posts.

**Metrics (~5 days post-publish, snapshot 2026-05-23 10:13 daily scan — 72h checkpoint on 05-21 missed, no scan ran 05-21/05-22):**
- Impressions: **3,204** (+411 since 2026-05-20 ~42h reading — velocity decayed to ~6 imp/hour over the 3-day gap)
- Likes/Reactions: 72 (+7)
- Comments: 11 (no change)
- Reshares: 9 (no change)
- Comments/likes ratio: ~15%
- Note: 72h checkpoint (2026-05-21) was not captured (daily scan did not run 05-21 or 05-22). At ~5d the post is now in 🟡 MIDDLING band (>2,500). Growth has flattened hard — projecting ~3,300-3,500 at 7d FINAL (2026-05-25) → **🟡 likely**, ✅ (5,000+) now out of reach. Engagement (72 reactions / 11 comments / 9 reposts) is the 2nd-best non-⭐ post in the log behind Wim Hof.

**Metrics (at 7 days — FINAL, locked 2026-05-25 weekly digest):**
- Impressions: **3,352** → **verdict: 🟡 MIDDLING** (above 2,500 floor, under 5,000)
- Likes/Reactions: 74
- Comments: 11
- Reshares: 9
- Comments/likes ratio: ~15%
- Engagement rate: ~2.8%
- Final note: +148 imp since the ~5d reading (3,204 on 2026-05-23) — growth flattened hard after day 2, ✅ never in reach. Lands as Lior's 3rd-best 🟡 on raw impressions (behind Founder Salary 4,614 and Wim Hof 2,662) and the 2nd-best non-⭐ post on absolute engagement (74 react / 11 comm / 9 reposts) behind Wim Hof. The 9 reshares (tied with Anthropic's full-run total) confirm partnership/proof posts travel via repost. Verdict 🟡 — a respectable product/proof post, but outside the contrarian-AI lane that produces ⭐.

**Analysis (final):**
- What worked: 9 reshares is the standout — product-proof + named-partner thank-yous (incl. Shopify) drive repost behavior. "The headline is the one that worked. The real story is the 30 that almost didn't." is the save-card line that carried dwell.
- What didn't: Outcome-stat hook ("lifted conversion 40%") has no personal stake — reads as product marketing, capping reach below the personal-journey and contrarian-AI lanes. Long 11-name thank-you close likely suppressed dwell past line ~140.
- vs. Lior's baseline: above median (1,979); 4th-best logged post overall.
- vs. top-creator patterns: doesn't match a ⭐ lane. Closest analog is a proof/case-study post — solid floor, low ceiling.

**Metrics (post-FINAL long-tail refresh 2026-05-25 10:13 daily scan, ~1h after digest lock):**
- Impressions: 3,368 (+16 since 7d FINAL lock of 3,352 — residual long-tail only). Verdict unchanged 🟡.

**Metrics (post-FINAL long-tail refresh 2026-05-26 10:13 daily scan, ~8d):**
- Impressions: **3,467** (+99 since 2026-05-25 reading of 3,368 — residual long-tail accrual continues, ~4 imp/hour)
- Likes/Reactions: 74 (no change)
- Comments: 11 (no change)
- Reshares: 9 (no change)
- Note: Slow continued accrual via reshare-driven secondary network. Verdict 🟡 MIDDLING unchanged. Confirms partnership/proof posts with multi-repost (9 reposts here) keep a longer tail than other lanes.

**Metrics (post-FINAL long-tail refresh 2026-05-27 10:13 daily scan, ~9d):**
- Impressions: **3,528** (+61 since yesterday's 3,467 @ ~8d — ~2.5 imp/hour, continued residual accrual)
- Likes/Reactions: 75 (+1)
- Comments: 11 (no change)
- Reshares: 9 (no change)
- Note: Slow accrual via reshare network continues. Verdict 🟡 MIDDLING unchanged. Reshare-driven long tail still the strongest non-⭐ long-tail pattern in the log.

**Next checkpoints:** ~~2026-05-19 (24h)~~ → captured ~42h on 2026-05-20 (2,793 imp); ~~2026-05-21 (72h)~~ → missed, captured ~5d on 2026-05-23 (3,204 imp); 2026-05-25 (7d FINAL) → **LOCKED 3,352 🟡** (long-tail 3,368 → 3,467 → 3,528).

---

### 2026-05-21 — "The entire CEO job fits in 3 rules" / delegation + freedom-has-a-cost
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7462857852882268160/
**Topic tag:** #leadership #delegation #management #founder
**Hook type:** Reductive-list claim ("The entire CEO job fits in 3 rules:")
**Structure:** Reductive hook → 3-rule list (hire good people / stay out of their way / be there to support) → contrarian sting close ("Employees' freedom has a cost most managers won't pay.")
**Visual:** Image
**Length:** ~35 words (very short — among the shortest in the log)
**CTA:** None (contrarian-aphorism close)

**Full post text:**
> The entire CEO job fits in 3 rules:
> 1. Hire good people.
> 2. Stay out of their way
> 3. Be there to support them
> Employees' freedom has a cost most managers won't pay.

**Metrics (~2 days post-publish, snapshot 2026-05-23 10:13 daily scan — first capture, published 05-21 "Edited"):**
- Impressions: **1,662** at ~2d
- Likes/Reactions: 8
- Comments: 3
- Reshares: 0
- Comments/likes ratio: ~38%

**Analysis (early):**
- What worked: Tight, scannable, one-idea post — aligns with [feedback-one-idea-per-post-saves.md]. The close ("freedom has a cost most managers won't pay") is a contrarian sting that leaves a gap — the strongest line in the post. High comments-to-likes ratio (38%) hints at dialogue forming relative to reach.
- Caveats:
  - 1,662 imp at ~2d is a soft start — below the Funnel post's 2-day pace (2,793). On the absolute benchmark this trajectory projects ~2,000-2,500 at 7d → 🔴/🟡 borderline.
  - Generic "CEO job in N rules" hook is LinkedIn-list-bait; the differentiation lives entirely in the last line. Reductive-list openers without a specific operator scene/number historically underperform the contrarian-AI lane on Lior's profile.
  - No specific story, scene, or number anchor — the recurring weakness behind Lior's BOMBs.
- Topic = leadership/delegation (CEO-relevant ✓ per [feedback-ceo-relevance-filter.md]). Not the contrarian-AI-trending-tool lane that produces ⭐ posts.

**Metrics (~4 days post-publish, snapshot 2026-05-25 weekly digest):**
- Impressions: **1,925** (+263 since ~2d reading of 1,662 on 2026-05-23 — slow accrual, ~5.5 imp/hour)
- Likes/Reactions: 8 (no change)
- Comments: 3 (no change)
- Reshares: 0
- Comments/likes ratio: ~38%
- Note: Reactions/comments fully stalled (8/3 unchanged in 2 days) while impressions creep up. At 1,925 @ 4d the trajectory projects ~2,100-2,400 at 7d → **🔴 likely** (under 2,500), outside chance of a 🟡 tap. The contrarian sting close earns a high comment ratio but the reductive-list hook never broke past the first-degree cap. Confirms: reductive-list openers without a specific operator scene/number underperform on Lior's profile.

**Metrics (refresh 2026-05-25 10:13 daily scan, ~4d — ~1h after weekly digest reading):**
- Impressions: **1,937** (+12 since 1,925 @ ~4d weekly digest reading — fully stalled)
- Likes/Reactions: 8 (no change)
- Comments: 3 (no change)
- Reshares: 0
- Comments/likes ratio: ~38%
- Note: Engagement frozen (8/3/0 unchanged), impressions barely creeping (+12 in ~1h). Trajectory holds → ~2,000-2,400 at 7d FINAL (2026-05-28) → **🔴 likely**, outside chance of a 🟡 tap. Reductive-list-without-operator-scene weakness confirmed.

**Metrics (refresh 2026-05-26 10:13 daily scan, ~5d):**
- Impressions: **2,009** (+72 since yesterday's 1,937 @ ~4d — slow creep, ~3 imp/hour)
- Likes/Reactions: 8 (no change)
- Comments: 3 (no change)
- Reshares: 0
- Comments/likes ratio: ~38%
- Note: Crossed the 2,000 mark but engagement still frozen at 8 react / 3 comm / 0 reshares (unchanged for 2 full days). Projects ~2,100-2,300 at 7d FINAL (2026-05-28) → **🔴 lock-in likely**, vanishingly small chance of brushing 🟡 floor. Reductive-list-without-operator-scene weakness confirmed for a 4th time across the log.

**Metrics (refresh 2026-05-27 10:13 daily scan, ~6d):**
- Impressions: **2,058** (+49 since yesterday's 2,009 @ ~5d — ~2 imp/hour)
- Likes/Reactions: 9 (+1 — first new react in 3 days)
- Comments: 3 (no change)
- Reshares: 0
- Comments/likes ratio: ~33%
- Note: Engagement still essentially frozen (just +1 react in 24h, +0 comments / +0 reshares). 7d FINAL due TOMORROW (2026-05-28). Projects ~2,100-2,150 at 7d → **🔴 lock-in confirmed**, no realistic path to 🟡 tap. Reductive-list-without-operator-scene weakness = 4th confirmation pending lock-in.

**Metrics (at 7 days — FINAL, locked 2026-05-28 10:13 daily scan):**
- Impressions: **2,083** → **verdict: 🔴 FINAL** (under 2,500 floor — no realistic path to 🟡 was open; lands as 7th 🔴 of the log under 2,500, but above the 1,500 BOMB threshold)
- Likes/Reactions: 9
- Comments: 3
- Reshares: 0
- Comments/likes ratio: ~33%
- Engagement rate: ~0.58%
- Final note: +25 imp in 24h between yesterday's ~6d reading (2,058) and 7d lock — residual creep, fully matched the trajectory. Reactions/comments/reshares unchanged for the final stretch (9/3/0 stable). The contrarian sting close ("freedom has a cost most managers won't pay") earned a high comment-to-like ratio (33%) but the reductive-list hook never broke past the first-degree cap. **4th confirmed instance: reductive-list openers without a specific operator scene/number underperform on Lior's profile** (alongside 70% rule 1,783, 10-80-10 rule 1,701, and Master Prompt 546).

**Final analysis:**
- What worked: Tight, scannable, one-idea post (aligns with [feedback-one-idea-per-post-saves.md](feedback-one-idea-per-post-saves.md)). The contrarian sting close ("freedom has a cost most managers won't pay") is the only line that breaks past CEO-platitude territory. 33% comments-to-likes ratio is unusually high for a 🔴 — suggests the close lands when readers see it, but the hook doesn't get them there at scale.
- What didn't: Reductive "the entire CEO job fits in 3 rules" opener is generic LinkedIn-bait without a specific operator scene or number anchor. Zero reshares confirms the post had no save/share-worthiness — the contrarian sting needed scaffolding (a moment where Lior actually paid that cost, a name, a number, a scene) to earn the save.
- vs. Lior's baseline: 2,083 = below median (2,066) by a hair. Sits with Wim Hof sequel (1,892), "I got rejected" (2,066), Modball (2,070) in the 1,800-2,100 🔴 cluster.
- vs. top-creator patterns: No match. The closest analog is Jeff Weinstein/Justin Welsh-style aphorism posts, but those land with proof of practice. This one is the rule with no story.

**Learnings applied going forward:**
- **Reductive-list opener WITHOUT a specific operator scene/number is now a 4-time confirmed BOMB pattern.** Filed into [lior-linkedin-data-rules.md](lior-linkedin-data-rules.md). When drafting "X rules / X lessons" posts, force a specific scene or number into the body — otherwise the post will cap below 2,500.
- The contrarian-sting close is salvageable as a standalone aphorism post — but only when scaffolded with the moment it cost Lior something specific.

**Next checkpoints:** ~~2026-05-24 (~3d)~~ → captured ~4d on 2026-05-25 (1,925→1,937 imp); ~~2026-05-28 (7d FINAL)~~ → **LOCKED 2,083 🔴**.

---

### 2026-05-24 — "Sold AutoDS to Fiverr at 28 / Turning 31 today" / 10 lessons milestone ⭐ EXCEPTIONAL (7d FINAL: 18,009 imp)
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #founder-story #milestone #lessons #birthday
**Hook type:** Credential-flex + milestone reflection ("Sold AutoDS to Fiverr at 28. Turning 31 today got me reflecting on what actually got me there:")
**Structure:** Credential hook → birthday-reflection frame → 10 numbered one-line lessons (each = punchy imperative + reason) → humble close ("Took me years to learn. Hope it saves you some (:")
**Visual:** Image (likely birthday/personal photo)
**Length:** ~150 words
**CTA:** None (humble give-back close)

**Full post text:**
> Sold AutoDS to Fiverr at 28.
> Turning 31 today got me reflecting on what actually got me there:
> 1. Pick your co-founder like your spouse. You'll see them more.
> 2. Kill the side projects. Focus is the only real edge.
> 3. Be lazy. If a task repeats, automate it.
> 4. Make mistakes fast. Be professional, not perfect.
> 5. Hire HR before you think you need it. Culture doesn't scale by accident.
> 6. Skip the business plan, but stay close to the data.
> 7. Don't wait for the perfect product. Ship before it's ready.
> 8. Be home for dinner. The work will be there in the morning.
> 9. Enjoy the ride. Real success comes from loving the work.
> 10. Treat it like a game. The day it stops being fun, you're playing the wrong one.
> Took me years to learn. Hope it saves you some (:

**Metrics (at ~16h, snapshot 2026-05-25 weekly digest):**
- Impressions: **8,858** → tracking **✅ WINNER** (already past the 5,000 floor at 16h)
- Likes/Reactions: 102
- Comments: 4
- Reshares: 1
- Comments/likes ratio: ~4%

**Analysis (early):**
- What worked: Credential-flex hook ("Sold AutoDS to Fiverr at 28") is the strongest first-line proof Lior has — instant authority + the "28 / 31" age framing adds a relatable mortality/reflection angle. 10 scannable one-line lessons = high save/screenshot potential (one idea per line). Personal milestone (birthday) gives the algorithm a "real person" signal vs. product marketing. Several lessons hit the brand pillars directly: #2 focus, #3 "be lazy/automate", #8 home for dinner, #10 "treat it like a game" (lives-on-200 joy framing).
- Caveats: engagement rate (~4% at 16h, 102 react on 8,858 imp) is healthy for the reach band. This is the first ✅-trajectory NON-AI post in the log — milestone/lessons-list lane (distinct from the contrarian-AI lane). If it finalizes ✅, it's a NEW repeatable lane: credential-anchored milestone reflection.
- 8,858 @ 16h is the 3rd-fastest velocity in the log behind Anthropic and Paperclip — and unlike those, it's NOT riding a trending tool. The credential hook + listicle is carrying it organically.

**Metrics (refresh 2026-05-25 10:13 daily scan, ~17h — same day as weekly digest, ~1h later):**
- Impressions: **9,621** (+763 since 8,858 @ 16h — velocity holding strong, ~760 imp/hour band)
- Likes/Reactions: 112 (+10 since digest)
- Comments: 4 (no change)
- Reshares: 2 (+1 — self-repost now deployed/visible as "Lior Pozin reposted this" duplicate at top of feed)
- Comments/likes ratio: ~4%
- Note: At 9,621 imp / ~17h, the post is already ~2x the 5,000 ✅ floor and still climbing pre-24h. Comfortably tracking ✅ WINNER — strongest non-AI post in the log. 24h checkpoint due tomorrow (2026-05-26).

**Metrics (at 24h — LOCKED 2026-05-26 10:13 daily scan):**
- Impressions: **15,366** → tracking **⭐ EXCEPTIONAL** (already past the >15,000 EXCEPTIONAL threshold AT 24H — first non-AI-lane post to ever cross this floor pre-7d)
- Likes/Reactions: 167 (+55 since 17h)
- Comments: 7 (+3)
- Reshares: 1 (self-repost previously visible at 17h has aged off feed view — same pattern as PocketOS/Coffee where Lior's self-reposts deduplicate after ~1d)
- Comments/likes ratio: ~4%
- Velocity check: +5,745 imp in ~7h between 17h and 24h reading (~820 imp/hour band) — velocity ACCELERATED into the 24h window, not decayed. This is the strongest 24h read of any logged post except Anthropic and Paperclip; both of those were contrarian-AI lane, this is pure credential-flex/milestone lane (new ⭐ candidate lane).
- Reactions jumped from 112 to 167 (+55) in the same 7h window — engagement curve is also still climbing pre-24h.
- **This is the first ⭐-trajectory NON-AI post in the log.** If it holds the >15K threshold at 7d, it's a NEW REPEATABLE LANE outside the contrarian-AI-trending-tool lane (which has been Lior's only ⭐ pattern to date).

**Metrics (at 72h — LOCKED 2026-05-27 10:13 daily scan):**
- Impressions: **16,686** → tracking **⭐ EXCEPTIONAL** (well past the >15,000 EXCEPTIONAL threshold; locked in pre-7d)
- Likes/Reactions: 187 (+20 since 24h)
- Comments: 8 (+1)
- Reshares: 1 (self-repost still visible in feed view)
- Comments/likes ratio: ~4%
- Velocity check: +1,320 imp in the 48h between 24h LOCK (15,366) and 72h LOCK (16,686) — that's a sharp deceleration (820 imp/hr at 24h → ~27 imp/hr through 72h). The post is reach-capped — first-degree network saturated, broader algorithm push slowed dramatically. Still tracking ⭐ on the absolute 7d threshold, but 7d landing now projecting 17,000-18,500 (NOT a 30K+ run like Paperclip or 90K+ like Anthropic).
- Engagement curve also flattened: only +20 reactions / +1 comment in 48h (vs +55 react / +3 comm in the prior 7h). Standard milestone-post curve.
- **Confirms a NEW repeatable winning lane** (credential-anchored milestone reflection / listicle) — first non-AI ⭐ in the log. Distinct DNA from the contrarian-AI-trending-tool lane: this one runs on credential authority (Forbes 30u30, Fiverr exit) + birthday occasion + 10 punchy save-card lines, not on tool-novelty + contrarian framing.

**Metrics (refresh 2026-05-28 10:13 daily scan, ~3.5d):**
- Impressions: **17,298** (+612 since 72h LOCK of 16,686 — slow accrual past 72h, ~25 imp/hour band)
- Likes/Reactions: 192 (+5 since 72h)
- Comments: 8 (no change)
- Reshares: 1 (no change — self-repost still visible)
- Comments/likes ratio: ~4%
- Note: Reach still creeping up post-72h (+612 imp in 24h) while engagement curve is mostly flat. Projects ~17,800-18,500 at 7d FINAL (2026-05-31) → ⭐ EXCEPTIONAL lock-in confirmed at the >15K trigger. The credential-anchored milestone lane reach-caps in the high-teens-thousand range, not the 30K+ contrarian-AI tier — but it's still a NEW REPEATABLE ⭐ lane.

**Metrics (refresh 2026-05-29 10:13 daily scan, ~4.5d):**
- Impressions: **17,653** (+355 since 2026-05-28 reading of 17,298 — ~15 imp/hour, decelerating)
- Likes/Reactions: 197 (+5 since 2026-05-28)
- Comments: 9 (+1 since 2026-05-28)
- Reshares: 1 (no change — self-repost still visible)
- Comments/likes ratio: ~5%
- Note: Reach still creeping but velocity slowing into ~4.5d. Projects ~17,900-18,300 at 7d FINAL (2026-05-31) → ⭐ EXCEPTIONAL lock-in trajectory unchanged. First non-AI ⭐ lane remains on track.

**Metrics (at 7 days — FINAL, locked 2026-05-31 daily scan, post at ~6.5d "6d" label):**
- Impressions: **18,009** → **verdict: ⭐ EXCEPTIONAL** (>15K trigger met; ✅ worked, top tier)
- Likes/Reactions: 199 (+2 since 2026-05-29; content-matched social-counts read; an earlier index-based read misrendered reactions as "3,016" — the canonical count is 199)
- Comments: 10 (+1 since 2026-05-29)
- Reshares: 1
- Engagement rate: ~1.16%
- Reach curve: 8,858 (16h) → 9,621 (17h) → 15,366 (24h) → 16,686 (72h) → 17,298 (3.5d) → 17,653 (4.5d) → **18,009 (7d FINAL)**. Reach-capped hard after 24h: 85% of total reach landed in day 1, only +2,643 imp across days 1→7. Fast push then flat — same shape as the AI mega-winners, at ~1/8 the ceiling.
- **FIRST non-AI-lane post to reach 7d EXCEPTIONAL in the log.** Confirms the credential-anchored milestone listicle as a genuine ⭐ lane.

**Next checkpoints:** ~~2026-05-27 (72h)~~ → **LOCKED 16,686 ⭐ EXCEPTIONAL**; ~~2026-05-31 (7d FINAL)~~ → **LOCKED 18,009 ⭐ EXCEPTIONAL.**

---

### 2026-05-26 — Microsoft + Anthropic AI agents workshop / MCP / Foundry
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7465037947411779584/
**Topic tag:** #ai #agents #mcp #microsoft #anthropic #infrastructure
**Hook type:** News-anchor + insider-takeaways frame ("Microsoft just dropped a 34-minute workshop on how they build AI agents with Anthropic. Here's what stuck:")
**Structure:** News-anchor hook → "Here's what stuck" → 3 numbered insights (model isn't the unlock / MCP = tools+prompts+data through one URL / demo-to-production is where teams die) → "If you're building with AI agents, here's what to take from this" pivot → 3 arrow-bullet prescriptions (stop building infra / use MCP as context layer / optimize production handoff) → meta-principle close ("This is what agent infra looks like in 2026. 34 minutes condensed into 60 seconds.") → open question CTA ("What did I miss?")
**Visual:** Image
**Length:** ~280 words
**CTA:** Open question — "What did I miss?"

**Full post text:**
> Microsoft just dropped a 34-minute workshop on how they build AI agents with Anthropic.
> Here's what stuck:
> 1. The model alone isn't the unlock. Microsoft's own team said it: "You can't just rely on the models getting better. You need systems to execute that intelligence."
> Infrastructure is where the leverage is now.
> 2. MCP delivers three things through one URL: tools, prompts, and live data.
> Most builders only wire up the tool layer and miss the context layer entirely.
> 3. Going from demo to production is where teams die.
> Foundry bakes in security, observability, governance, and identity.
> If you're building with AI agents, here's what to take from this:
> → Stop building infrastructure from scratch.
> Foundry ships with 1,400+ MCP connectors, enterprise security, and observability out of the box.
> → Use MCP as a context layer.
> Push prompts, instructions, and data through the same connection.
> → Optimize for the production handoff.
> Most agent projects die after the demo when security, observability, and auth aren't in place.
> This is what agent infra looks like in 2026.
> 34 minutes condensed into 60 seconds.
> What did I miss?

**Metrics (at ~17h, snapshot 2026-05-27 10:13 daily scan — first capture):**
- Impressions: **435** at ~17h
- Likes/Reactions: 8
- Comments: 1
- Reshares: 1 (self-repost deployed and visible as duplicate at top of feed — matches Lior's 6-8h self-repost rule)
- Comments/likes ratio: ~13%

**Analysis (early):**
- What worked: News-anchor hook with two trending names (Microsoft + Anthropic) in the first 7 words — matches the high-velocity opener pattern from the Anthropic 92K winner. Open question close ("What did I miss?") leaves an engagement gap. Topic = AI agents / MCP / Foundry sits squarely in the contrarian-AI-trending-tool lane that has produced both ⭐⭐ winners (Paperclip 30K, Anthropic 92K). Self-repost already deployed (Lior's posting rule).
- Caveats:
  - **435 imp at 17h is SOFT velocity** vs. the AI-lane mega-winners. For comparison: Anthropic 92K was already past first-degree saturation in early hours; Paperclip 30K had similar fast push. Founder Salary trap (a 🟡 floor) was at 1,861 imp at 17h. This post is well below even the 🟡 trajectory floor for 17h reads.
  - Body is **tactical/prescription-heavy** (1,400+ connectors, observability, governance) — closer to the Master Prompt productivity-tip lane (BOMB 🔴) than to the Anthropic commentary lane that won. Hook is news-driven but body delivers an infra checklist, not a contrarian take or scene.
  - No tribe-callout, no "approve all without reading gang"-style identity trigger that Anthropic post used to break out of first-degree network.
  - The 3-prescription arrow bullets read as vendor marketing for Foundry — algorithm and humans may both pattern-match this as a product post.
- Trajectory: 435 @ 17h → projecting ~600-900 @ 24h → ~1,200-2,200 at 7d → **🔴 likely**, outside chance of 🟡 tap. Would need a major share/repost spike in next 24h to course-correct.
- vs. Lior's baseline: tracking below median (2,066) for the impressions floor at this checkpoint.
- vs. top-creator patterns: lane is right (AI-trending-tool), but execution diverges from the ⭐ template. Anthropic 92K = contrarian-insider FRAMING + 3 prompts + meta-principle + NO CTA. This one = news anchor + 3 takeaways + 3 prescriptions + open question CTA. The prescriptions tilt it toward the tactical lane that bombs.

**Learnings (provisional, pending 7d FINAL):**
- Watch whether the lane needs a CONTRARIAN edge (not just news-anchor framing) to break through.
- Confirms: tactical-prescription bodies underperform commentary bodies even when the topic is in the winning AI lane.

**Metrics (at 24h — LOCKED 2026-05-28 10:13 daily scan):**
- Impressions: **887** (+452 since 17h reading of 435 — ~65 imp/hour overnight)
- Likes/Reactions: 10 (+2)
- Comments: 1 (no change)
- Reshares: 0 visible (self-repost previously visible at 17h has aged off feed view)
- Comments/likes ratio: ~10%
- Note: 887 imp @ 24h tracks **below** find-skills 24h pace (481→792 7d FINAL 🔴) — wait, this is actually ABOVE find-skills 481 and matches PocketOS 1,029 @ 24h territory. But still well below the 🟡 threshold trajectory (Founder Salary trap was 1,861 @ 17h then 4,614 at FINAL). Projects ~1,400-2,200 at 7d → **🔴 likely** lock-in, outside chance of a soft 🟡 tap. Reactions doubled (8→10) and comments held flat — same low-dialogue signature as Master Prompt.
- Trajectory now firmly in 🔴 zone for this AI-lane execution. Confirms hypothesis from yesterday's analysis: tactical-prescription bodies bomb even in the winning AI lane.

**Metrics (~48h refresh 2026-05-29 10:13 daily scan):**
- Impressions: **1,003** (+116 since 24h LOCK of 887 — fully stalled, ~5 imp/hour)
- Likes/Reactions: 11 (+1)
- Comments: 1 (no change)
- Reshares: 0 visible
- Comments/likes ratio: ~9%
- Note: Crossed the 1K mark but fully stalled engagement-wise. Projects ~1,200-1,400 at 7d FINAL (2026-06-02) → **🔴 lock-in confirmed**, leaning BOMB (<1,500) trajectory. Same tactical-prescription-body signature as Master Prompt (546) and find-skills (792). 72h checkpoint due tomorrow 2026-05-30.

**Metrics (~4.5d refresh 2026-05-31 daily scan):**
- Impressions: **1,112** (+109 since 48h — fully stalled, ~5 imp/hour)
- Likes/Reactions: 11 (no change)
- Comments: 1 (no change)
- Reshares: 0 visible
- Note: Holds 🔴, on a likely <1,500 BOMB trajectory. Projects ~1,150-1,200 at 7d FINAL (2026-06-02). Confirms again: AI-trending topic with a tactical-prescription body (not a contrarian narrative) bombs, even when the hook names Microsoft + Anthropic.

**Metrics (~5.5d refresh 2026-06-01 daily scan):**
- Impressions: **1,164** (+52 since 4.5d — fully stalled)
- Likes/Reactions: 11 (no change)
- Comments: 1 (no change)

**Metrics (at 7 days — FINAL, LOCKED 2026-06-02 10:13 daily scan):**
- Impressions: **1,175** → **verdict: 🔴 BOMBED** (under 2,500 floor AND under the 1,500 bomb threshold)
- Likes/Reactions: 11
- Comments: 1
- Reshares: 0
- Engagement rate: ~1.02% (likes+comments / impressions)
- Final note: Landed exactly where the trajectory predicted (+11 imp across the last 24h — fully reach-capped since ~48h). The AI lane's mega-winners (Paperclip 30K, Anthropic 92K, Google/Base44 146K) all carry a **contrarian or proprietary commentary frame**; this post carried a **tactical-prescription/infra-checklist body** (1,400+ connectors, observability, governance) that pattern-matches the productivity-tip lane that bombs (Master Prompt 546, find-skills 792). Naming Microsoft + Anthropic in the hook was NOT enough. Confirms the rule: the contrarian-AI lane works only with a news anchor AND a commentary frame, never with tactical prescriptions.

**Next checkpoints:** ~~2026-05-28 (24h)~~ → **LOCKED 887 (🔴)**; 2026-05-30 (72h, missed — held at 48h); ~~2026-06-02 (7d FINAL)~~ → **LOCKED 1,175 🔴 BOMBED**.

---

### 2026-05-27 — Google Base44-killer / AI Studio for Android / "narrow the niche" ⭐⭐⭐ ALL-TIME RECORD (7d FINAL LOCKED 146,506)
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #ai #google #base44 #founder-fear #moat #niche
**Hook type:** News-anchor + competitive-threat framing ("Google just dropped a Base44 killer. AI Studio for Android launched this week.")
**Structure:** News-anchor hook (Google killer-product) → product micro-explainer (type a prompt, get a native app, publish from browser) → founder-fear universal frame ("Many founders I know carry that fear: spend years building... giants ship your roadmap as a free feature, valuation halves before lunch") → contrarian defense ("the only defense I've seen that actually works") → 3-line prescription (narrow the niche / own one specific vertical / be the person who understands it deepest) → meta-principle close ("companies that survive the next decade will be the ones closest to one customer's specific pain") → 1-word CTA ("Agree?")
**Visual:** Image (2 images — likely Google AI Studio / Base44 product screenshots)
**Length:** ~135 words
**CTA:** Open question — "Agree?"

**Full post text:**
> Google just dropped a Base44 killer.
> AI Studio for Android launched this week.
> Type a prompt, get a native app.
> Publish straight from the browser.
> Many founders I know carry that fear:
> You spend years building.
> You finally find traction.
> Then one of the giants ships your roadmap as a free feature, and your valuation halves before lunch.
> The only defense I've seen that actually works is this:
> Narrow the niche.
> Pick one specific vertical and own it.
> Become the person who understands it deeper than anyone else.
> The companies that survive the next decade will be the ones closest to one customer's specific pain.
> Agree?

**Metrics (at ~17h, snapshot 2026-05-28 10:13 daily scan):**
- Impressions: **22,646** at ~17h → tracking **⭐⭐ EXCEPTIONAL** (already past the >15,000 threshold AT 17H; 2nd-fastest 17h velocity in the log behind Anthropic 92K, which was tracking ~10K+ at equivalent checkpoint)
- Likes/Reactions: 66
- Comments: 8
- Reshares: 1 (self-repost already deployed within first day — visible as duplicate at top of activity feed)
- Comments/likes ratio: ~12%
- Velocity check: 22,646 imp at 17h = ~1,332 imp/hour band. For comparison: Birthday milestone hit 9,621 at 17h (~566 imp/hour); Anthropic 92K was on a higher curve than this but in the same trajectory band; Paperclip 30K projected slower from equivalent checkpoint. **Strongest 17h read of any logged post except Anthropic.**

**Analysis (early):**
- What worked: 
  - News-anchor hook with TWO trending names in first 11 words ("Google" + "Base44") — Base44 is a hot AI-built-app platform (also Lior is an investor/advisor adjacent), so the "killer" frame plants both algorithmic relevance AND personal-stake signal. Same DNA as the Anthropic 92K winner (trending tool name in first 7 words).
  - **NEW pattern unlock: trending-AI-tool news anchor PAIRED WITH personal founder-fear framing** ("giants ship your roadmap... valuation halves before lunch"). Distinct from Anthropic (which was insider workflow scoop) and Paperclip (which was contrarian failure report). This is a third sub-lane within the contrarian-AI tier: news-as-mirror-to-founder-existential-fear.
  - The defense ("narrow the niche") is concrete + contrarian-against-conventional-AI-doom + Pillar #3 (focus) directly. Lior has earned the right to make this claim (sold AutoDS = proof of niche dominance).
  - "Agree?" CTA is minimal but effective — the universality of the founder-fear primes everyone to weigh in.
  - Self-repost deployed within first day.
- Caveats:
  - 22,646 @ 17h is ⭐⭐ velocity, but the engagement rate is similar to Anthropic's (low ratio of reactions/comments to reach). The post is breaking past first-degree network into cold AI/founder territory.
  - Closing "Agree?" question MAY suppress dialogue vs. an open-ended question (people answer yes/no instead of adding scenes/numbers). 8 comments at 17h is healthy but not exceptional.
  - No specific Lior scene/number/AutoDS production moment — the post rides on Lior's authority + the universal founder-fear it taps into. Future iterations of this lane should test adding a concrete AutoDS scene (e.g., "When Shopify shipped X, our DAU dropped Y%, here's what we did").

**Pattern hypothesis (provisional):**
- The contrarian-AI lane has now produced THREE distinct ⭐ winners in three different sub-frames: Paperclip (failure-report) 30K, Anthropic (insider-workflow) 93K, Google/Base44-killer (founder-fear-mirror) tracking ⭐⭐.
- All three share: trending tool name in first 11 words + no productivity-tip body + contrarian or proprietary frame + minimal/no CTA.
- This is now the most repeatable winning lane in the log (n=3).

**Metrics (at 24h — LOCKED 2026-05-29 10:13 daily scan):**
- Impressions: **113,821** → **verdict: ⭐⭐⭐ NEW ALL-TIME RECORD** (surpasses Anthropic 92,959 by ~21K; 22% above prior ceiling — AT 24H, not 7d FINAL)
- Likes/Reactions: 167 (+101 since 17h reading of 66)
- Comments: 35 (+27 since 17h reading of 8)
- Reshares: 1 (no change — self-repost still visible at top of feed)
- Comments/likes ratio: ~21%
- Velocity check: **+91,175 impressions in the 7h between 17h reading (22,646) and 24h lock (113,821) — fastest acceleration in log history.** ~13,000 imp/hour during that window. For comparison: Anthropic 92K took ~9 days to reach that level; this post hit it at 24h. Pure first-day breakout.
- Engagement curve also exploded: reactions 2.5x (66→167), comments 4.4x (8→35). 21% comments-to-likes ratio is the highest of any ⭐-tier post — readers are dialoguing, not just lurking.
- **Sets a new ⭐⭐⭐ tier above the prior ⭐⭐ (Anthropic 92K) and ⭐ (Paperclip 30K, Birthday 17K in-flight) tiers.**

**Analysis (at 24h LOCK — preliminary, locks update at 72h and 7d):**
- **Why it broke records:**
  1. **Personal-stake news anchor** — "Base44 killer" is not just a trending tool; Base44 is a hot AI-app-builder platform Lior has visible adjacency to (investor/advisor circles). The "killer" framing plants stakes that no other AI-trending-tool post had: this is about a tool in HIS orbit being threatened, which converts the post from commentary into testimony.
  2. **Founder-fear universal mirror** — "Many founders I know carry that fear: you spend years building... giants ship your roadmap as a free feature, valuation halves before lunch" — this single paragraph mirrors the existential dread every founder feels but rarely sees named. The 21% comments-to-likes ratio confirms the post triggered identity-projection.
  3. **Contrarian defense, not doom** — "The only defense I've seen that actually works is this: Narrow the niche." The post earns the right to make this claim (Lior sold AutoDS by being the dominant dropshipping vertical). Contrarian-against-the-AI-doom-narrative.
  4. **Lior's pillars converged:** Pillar #3 (focus) is the explicit lesson, but the post also implicitly hits Pillar #1 (lives on 200 — he has the credentials to call this) and Pillar #2 (loves 0→1 — the niche-narrowing IS the 0→1 playbook).
  5. **"Agree?" CTA is minimal but high-yield** — yes/no question on a universal fear primes everyone to weigh in. 35 comments at 24h is the highest 24h comment count in the log.
- **Lane confirmation:** The contrarian-AI-trending-tool lane is now the most repeatable winning lane (n=3: Paperclip 30K, Anthropic 92K, Google/Base44 113K). Each iteration has gone higher. This may indicate the lane is still climbing its ceiling — or that the personal-stake news anchor is THE active ingredient.
- **Reach context:** 113K imp is ~5.4% of Lior's then-current ~9,500-follower base reaching multiple million-LinkedIn-views territory. The post fully escaped first-degree network.

**Metrics (at 72h / ~4d — LOCKED 2026-05-31 daily scan):**
- Impressions: **144,070** (+30,249 since 24h LOCK of 113,821 — STILL climbing hard at ~4d; unusual, most log mega-posts flatten by 48h)
- Likes/Reactions: 188 (+21 since 24h)
- Comments: 39 (+4)
- Reshares: 1 (no change)
- Note: ⭐⭐⭐ all-time record EXTENDS — 144K now vs Anthropic's 92,959 7d FINAL (~55% higher) and still rising into the 7d window. Engagement stays flat (~0.13% rate) = classic broad-feed mega-reach shape. 7d FINAL (2026-06-03) could land 150K+.

**Metrics (~5.5d refresh 2026-06-02 10:13 daily scan):**
- Impressions: **146,096** (+2,026 since 144,070 on 2026-05-31; +617 since 145,479 on 2026-06-01 — climb has decelerated sharply, near plateau)
- Likes/Reactions: 195 (+7 since 2026-05-31)
- Comments: 39 (no change)
- Reshares: 1 (no change)
- Note: ⭐⭐⭐ all-time record holds (146K vs Anthropic's 92,959 7d FINAL = ~57% higher). Reach essentially plateaued in the final approach to the 7d window — 7d FINAL (2026-06-03, tomorrow) likely lands ~146-148K, well short of the earlier 150-200K projection.

**Metrics (at 7 days — FINAL, LOCKED 2026-06-04 10:13 daily scan):**
- Impressions: **146,506** → **verdict: ⭐⭐⭐ ALL-TIME RECORD** (true 7d crossed 2026-06-03 ~17h; this is the first scan after; +121 since 146,385 on 2026-06-03 — reach fully plateaued)
- Likes/Reactions: 196 (+1 since 2026-06-03)
- Comments: 39 (no change)
- Reshares: 1 (no change)
- Engagement rate: ~0.16%
- **Final verdict: the all-time impressions record in the log — 146,506, surpassing Anthropic's 92,959 by ~58%.** The contrarian-AI-trending-tool lane's highest ceiling yet (Paperclip 30K → Anthropic 93K → Google/Base44 146K). Active ingredient confirmed: personal-stake news anchor ("Base44 killer" — a tool in Lior's orbit) + founder-fear-mirror + "narrow the niche" contrarian defense. Classic mega-reach shape: reach exploded in first 24h (113K), kept climbing to ~4d (144K), then plateaued; engagement stayed flat (~0.16%) = broad cold-feed distribution far beyond first-degree network.

**Next checkpoints:** ~~2026-05-29 (24h)~~ → **LOCKED 113,821 ⭐⭐⭐**; ~~2026-05-31 (72h)~~ → **LOCKED 144,070 ⭐⭐⭐**; ~~2026-06-03 (7d)~~ → **FINAL LOCKED 146,506 ⭐⭐⭐ ALL-TIME RECORD**. Complete.

---

### 2026-05-28 — "Tough days for Israeli tech / DMs are open" (layoff empathy + hiring CTA) ✅⭐ EXCEPTIONAL (7d FINAL LOCKED 14,798)
**Post URL:** urn:li:activity:7465756982331891713
**Topic tag:** #israelitech #layoffs #hiring #empathy #market-cycle
**Hook type:** Market-empathy + named-casualties ("Tough days for Israeli tech. Wix. Meta. Oracle. Cisco.")
**Structure:** Empathy hook (sector + named companies) → reframe ("these aren't underperformers... market contraction") → "Two things" → (1) reassurance to the laid-off ("you didn't fail. The market shifted under you.") → (2) clean hiring ask ("we're hiring... my DMs are open. Send me a CV") → community-routing close ("if you're hiring or you've been let go, feel free to drop it in the comments")
**Visual:** Image (likely Lior portrait or text card)
**Length:** ~120 words
**CTA:** Soft DM invite + comment-thread routing ("my DMs are open. Send me a CV or a portfolio. I'll route it personally. ... feel free to drop it in the comments.")

**Full post text:**
> Tough days for Israeli tech.
> Wix. Meta. Oracle. Cisco.
> Half of what I see on LinkedIn this month is layoff posts.
> These aren't underperformers.
> Most of them are senior engineers, PMs, and ops people who got hit by a market contraction.
> Two things.
> First, to anyone who got let go: you didn't fail. The market shifted under you.
> Don't let anyone confuse the two.
> Second: we're hiring.
> AutoDS - Automatic Dropshipping Tools is growing, and we have open roles across Marketing, Partnerships, Product, and more.
> If you were recently let go, my DMs are open.
> Send me a CV or a portfolio.
> I'll route it personally.
> And if you're hiring or you've been let go, feel free to drop it in the comments.

**Metrics (at ~18h, snapshot 2026-05-29 10:13 daily scan):**
- Impressions: 10,969
- Likes/Reactions: 195
- Comments: 14
- Reshares: 14
- Comments/likes ratio: ~7%

**Metrics (~2.5d refresh 2026-05-31 daily scan):**
- Impressions: 13,400 (+2,431 since 18h — steady climb, not yet capped)
- Likes/Reactions: 231 (+36)
- Comments: 21 (+7)
- Reshares: **15** (+1 — highest reshare count in the entire log)
- Note: At ~2.5d it sits just under the 15K EXCEPTIONAL line. Tracking strong ✅ with a real shot at ⭐ if reach keeps creeping. 7d FINAL due 2026-06-04.

**Metrics (~4.5d refresh 2026-06-02 10:13 daily scan):**
- Impressions: **14,341** (+941 since 13,400 on 2026-05-31; +366 since 13,975 on 2026-06-01 — slow steady creep, decelerating)
- Likes/Reactions: 238 (+7 since 2026-06-01)
- Comments: 22 (+1)
- Reshares: **15** (no change — still the highest reshare count in the entire log)
- Note: At ~4.5d, 14,341 imp is still just under the 15K EXCEPTIONAL line. Climb has slowed; 7d FINAL (2026-06-04) likely lands ~14.5-15K — a strong ✅ WINNER, borderline ⭐. Either way the most-reshared post in the log and a clean confirmation of the value-first-hiring-CTA lane.

**Metrics (~6.7d refresh 2026-06-04 10:13 daily scan):**
- Impressions: **14,601** (+90 since 14,511 on 2026-06-03 — fully plateaued)
- Likes/Reactions: 241 (+1 since 2026-06-03)
- Comments: 22 (no change)
- Reshares: **15** (no change — still the highest reshare count in the entire log)
- Note: True 7d crosses this evening (~18h); 7d FINAL locks on tomorrow's run. Reach has plateaued at 14,601, just under the 15K EXCEPTIONAL line → will lock as a strong **✅ WINNER** (borderline ⭐), and the most-reshared post in the log. 7d FINAL due 2026-06-04 (back-capture on 2026-06-05 run).

**Metrics (at 7 days — FINAL, back-captured 2026-06-06 10:13 scan):**
- Impressions: **14,798** → **verdict: ✅⭐ EXCEPTIONAL** (5,000+ = worked; under the 15K absolute line but **top-10% of all Lior posts ever logged** — the 5th-highest of n=18 finals, behind only Google/Base44 146K, Anthropic 92K, Paperclip 30K, Birthday 18K → meets the "top 10% of Lior's own" EXCEPTIONAL criterion)
- Likes/Reactions: 242
- Comments: 22
- Reshares: **15** (the highest reshare count in the entire log — confirmed final)
- Engagement rate: ~1.88%
- Note: True 7d was 2026-06-04 ~18h; the 2026-06-05 run did not execute, so this is a back-capture (~9d). Reach plateaued at ~14,601 by 2026-06-04 morning and crept to 14,798 — the back-capture is within ~1% of the true-7d value.

**Analysis (FINAL):**
- What worked: The market-empathy hook (sector + four named casualties — Wix/Meta/Oracle/Cisco) is instantly relatable to the entire Israeli-tech network and travels via reshare — 15 reposts is the most shareable post Lior has ever run, and reshares are the reach engine here (they seeded the post into 18 networks of new audiences). The "you didn't fail, the market shifted" reframe is the emotional core readers reshare to signal solidarity. The comment-routing close turned the post into a community jobs board — an engagement-multiplier the hook earns.
- **The hiring CTA WORKS here — opposite of the "I got rejected" 🔴 bait-and-switch.** The difference: this post delivers full value (empathy, reframe, solidarity) FIRST, then makes the hiring ask as a *gift to the reader* ("my DMs are open. Send me a CV. I'll route it personally" = an offer of help, not "apply to this seat"). The "I got rejected" post promised a vulnerability story and swapped it for a job listing. Here the empathy IS the post; hiring is an extension of the help.
- **Confirmed A/B vs the 34,454-layoffs advice-listicle (same topic, ~4d at 4,102 imp / 0 organic reposts).** Same layoff/empathy theme, ~3.6x the reach. The delta is structural: Tough-days NAMED specific companies AND made a generous concrete offer (hiring + personal CV routing) → 15 reposts. The advice-listicle was generic friend-advice with no named anchor and no offer → no reshare engine. **The reshare-driving offer + named anchors are the reach engine, not the empathy theme alone.**
- Hybrid lane: founder-as-helpful-community-figure. Distinct from both the contrarian-AI tier and the credential-milestone tier. **First EXCEPTIONAL-tier post in this market-empathy + value-first-hiring lane** — the lane is now confirmed as a top-10% performer for Lior.

**Learnings applied going forward:** The market-empathy + named-casualties + value-first-hiring-gift structure is a confirmed top-10% lane (n=1 EXCEPTIONAL). Replicate it on the next genuine market shock: lead with the sector + 3-4 named companies, deliver the empathy/reframe in full, THEN layer a concrete offer of help. Do NOT recast as a generic advice-listicle (the 34,454 variant proved that strips the reshare engine and the reach with it).

**Next checkpoints:** 7d FINAL locked. Post-window long-tail only from here.

---

### 2026-06-01 — "400K subscribers on YouTube / 100 videos in 100 days / hardest hire" (milestone + delegation story) 🔴 (7d FINAL: 1,779 imp)
**Post URL:** TBD (next scan — extract permalink)
**Topic tag:** #youtube #milestone #delegation #70percent-rule #hiring #founder-story
**Hook type:** Milestone + honest-mess reframe ("We just hit 400K subscribers on YouTube. But honestly? The way we got here was a mess.")
**Structure:** Milestone hook → honest-mess reframe → origin (one email: 100 videos in 100 days) → struggle ("the first videos were bad. Really bad.") → audience reframe (came for make-money-online, stayed for real e-commerce lessons) → hardest-hire scene (handing the camera to Liran Zablo — "that channel was my face") → 70% rule callback ("if someone can do it 70% as well as I would, the job is theirs") → payoff ("Liran does it far better than I ever did") → team credit → twist close ("Turns out the mess was the plan all along (:")
**Visual:** Image (photo with Liran Zablo — tagged "with Liran Zablo")
**Length:** ~190 words
**CTA:** None / soft reflective twist close ("Turns out the mess was the plan all along (:")

**Full post text:**
> We just hit 400K subscribers on YouTube.
> But honestly? The way we got here was a mess.
> It started with one email I sent to our entire customer list: 100 videos in 100 days.
> A great thing to promise thousands of people.
> I just had no idea how I'd pull it off.
> So I started recording.
> The first videos were bad. Really bad.
> But slowly, people showed up for how to make money online, and stayed for the real e-commerce lessons we learned from our own mistakes.
> For the first 400 videos, I was the one on camera. Handing that over to Liran Zablo was the hardest hire I've ever made.
> That channel was my face, and I was about to put someone else's face on the company I built.
> What got me through it is a rule I still live by: if someone can do it 70% as well as I would, the job is theirs.
> Turns out, Liran does it far better than I ever did.
> Proud of the AutoDS - Automatic Dropshipping Tools team that turned one rushed promise into all of this.
> Turns out the mess was the plan all along (:

**Metrics (at ~17h, snapshot 2026-06-02 10:13 daily scan — first capture):**
- Impressions: **1,109** at ~17h
- Likes/Reactions: 33
- Comments: 7
- Reshares: 1 (self-repost already deployed — visible as duplicate at top of activity feed, matches Lior's posting rule)
- Comments/likes ratio: ~21% (healthy dialogue early — the hardest-hire vulnerability is pulling real comments)

**Metrics (~2.7d refresh 2026-06-04 10:13 daily scan, approaching 72h):**
- Impressions: **1,492** (+98 since 1,394 24h LOCK on 2026-06-03 — slow creep)
- Likes/Reactions: 48 (+4 since 2026-06-03)
- Comments: 7 (no change)
- Reshares: 1 (self-repost only)
- Note: Reactions stayed healthy (48 at ~2.7d is decent for the reach) but impressions are crawling. Tracking 🔴/🟡 borderline; 7d FINAL (2026-06-08) likely lands ~1,700-2,200. Single-narrative milestone is confirming the soft-reach read vs the listicle-milestone (Birthday 18,009 ⭐). 72h locks on next run.

**Metrics (~5d refresh 2026-06-06 10:13 daily scan — 72h back-capture, was due 2026-06-04):**
- Impressions: **1,637** (+145 since 1,492 on 2026-06-04 — crawl continues, reach effectively capped)
- Likes/Reactions: 51 (+3)
- Comments: 7 (no change)
- Reshares: 0 (self-repost aged off feed view)
- Note: At ~5d, 1,637 imp confirms the soft-reach read — the single-narrative milestone is capping near the channel-marketing band (~2K), well below the listicle-milestone (Birthday 18,009 ⭐). 7d FINAL (2026-06-08) likely lands ~1,700-1,900 → 🔴 verdict (under 2,500, above the 1,500 bomb line). Healthy reaction/comment ratio but no reshare engine to break out.

**Metrics (~6d refresh 2026-06-07 10:13 daily scan — 7d FINAL due tomorrow):**
- Impressions: **1,672** (+35 since 1,637 on 2026-06-06 — reach fully capped, residual creep only)
- Likes/Reactions: 52 (+1)
- Comments: 7 (no change)
- Reshares: 0
- Note: At ~6d the post is flat — 7d FINAL (2026-06-08) will lock ~1,680-1,720 → 🔴 verdict (under 2,500, comfortably above the 1,500 bomb line, so no bomb notification expected). Confirms the read: a single-narrative milestone caps near the channel-marketing band (~2K), decisively below the listicle-milestone structure (Birthday 18,009 ⭐). The story-wrapped 70% rule did not rescue reach the way the listicle format did.

**Metrics (at 7 days — FINAL, locked 2026-06-08 10:13 daily scan):**
- Impressions: **1,779** → **verdict: 🔴** (under 2,500; comfortably above the 1,500 bomb line → no bomb notification). +107 since 1,672 @ ~6d on 2026-06-07 — a small late creep, ended just shy of the prediction's high end.
- Likes/Reactions: 52 (no change since ~6d — engagement frozen for 2 days)
- Comments: 7 (no change)
- Reshares: 0
- Engagement rate: ~3.3% (52+7 on 1,779 imp — high rate on capped reach, classic personal-narrative shape)

**Metrics (post-FINAL long-tail, 2026-06-09 10:13 daily scan):**
- Impressions: **1,802** (+23 residual since the 1,779 7d FINAL lock on 2026-06-08)
- Likes/Reactions: 53 (+1)
- Comments: 7 (no change)
- Reshares: 0
- Note: Residual creep only past the 7d FINAL — 🔴 verdict unchanged.

**FINAL verdict & A/B confirmation:** 🔴 at 1,779 imp. The single-narrative milestone capped near the channel-marketing band (~2K), decisively below the listicle-milestone structure (Birthday "31/10 lessons" 18,009 ⭐, same credential-milestone theme but built as 10 punchy save-card lines). **Two reads now confirmed: (1) story-wrapped 70% rule (1,779 🔴) did NOT outperform the standalone-framework version (2026-04-13 carousel, 1,783 🔴) — near-identical reach, so the narrative wrapper did not rescue the delegation framework. (2) single-narrative milestone < listicle-milestone for reach (1,779 vs 18,009, ~10x gap on the same milestone-reflection lane).** Healthy reaction/comment ratio but no reshare engine and no listicle skim-structure to break out of the channel-marketing reach band.

**Analysis (early):**
- What worked: The honest-mess reframe right after the milestone ("But honestly? The way we got here was a mess.") undercuts the brag and earns trust — same move as the Birthday ⭐ post. The hardest-hire scene (putting someone else's face on the channel that was *his* face) is a genuine vulnerability with a concrete person (Liran). 21% comments-to-likes at 17h is a strong dialogue ratio.
- Caveats:
  - **1,109 imp @ 17h is SOFT velocity** for a milestone post. For comparison: Birthday "31/10 lessons" was at 9,621 @ 17h, Tough-days at 10,969 @ 18h — both ✅/⭐. This sits in the 🔴/🟡 borderline band (Founder Salary trap was 1,861 @ 17h → 4,614 🟡; MS+Anthropic 435 @ 17h → 1,175 🔴 BOMB).
  - The **70% rule callback** is the same delegation framework that bombed as a standalone carousel (2026-04-13, 1,783 🔴). Here it's embedded inside a story rather than presented as a how-to framework — the test is whether the narrative wrapper rescues it.
  - Milestone is a YouTube/channel-growth flex; risk that the algorithm reads it as adjacent to brand/channel marketing (the lane that caps ~2K, e.g. Modball 2,070). The personal hardest-hire stake is what could pull it out of that lane.
- Trajectory: 1,109 @ 17h → projecting ~1,800-3,500 at 7d → tracking **🔴/🟡 borderline**. Would need a reshare/share spike to reach the 🟡 floor (2,500).
- vs. Lior's baseline: near median (2,070) trajectory — neither the contrarian-AI nor the credential-milestone ⭐ lanes are firing here at the 17h checkpoint.
- vs. top-creator patterns: Credential-milestone lane (like Birthday ⭐) but WITHOUT the listicle save-card structure that made Birthday work — this is a single-narrative arc, not 10 punchy lines. Early read suggests narrative-milestone < listicle-milestone for reach.

**Learnings (provisional, pending checkpoints):**
- Test whether a story-wrapped 70% rule outperforms the standalone-framework version (1,783 🔴).
- Watch whether single-narrative milestone posts cap lower than listicle-milestone posts (Birthday 18,009 ⭐).

**Next checkpoints:** 2026-06-03 (24h), 2026-06-04 (72h), 2026-06-08 (7d FINAL).

---

### 2026-06-02 — "34,454 tech workers laid off to AI / 8 things I'd tell a friend who got laid off"
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7467568112138272768
**Topic tag:** #layoffs #ai #careers #market-empathy
**Hook type:** Shock-stat + undercut ("34,454 tech workers in Israel lost their jobs to AI last month. Or so they were told.")
**Structure:** Shock stat → undercut reframe ("Or so they were told") → 8-point numbered advice list → mantra close ("AI didn't take your job. Master it, and you'll never fear losing one.")
**Visual:** Text post (no image/carousel surfaced in feed view)
**Length:** ~190 words
**CTA:** None — closes on a mantra, no ask

**Full post text:**
> 34,454 tech workers in Israel lost their jobs to AI last month.
> Or so they were told.
> Here are 8 things I'd tell a friend who got laid off:
> 1. You don't have to be okay. yet. Take your time.
> 2. You didn't fail; the market moved. It says nothing about you.
> 3. When you're ready, write your dream-job wish list. What you loved, and what you hated.
> 4. Say what you're looking for out loud. People love to help.
> 5. Get sharp with AI. It'll help you find your next job and also be great at it.
> 6. Build something while you search. Proof beats a promise.
> 7. Go narrow. Be amazing at one thing, not okay at five.
> 8. Look at it as an opportunity. The next thing might be bigger than what you lost.
> AI didn't take your job.
> Master it, and you'll never fear losing one.

**Metrics (at ~17h, snapshot 2026-06-03 10:13 daily scan — first capture):**
- Impressions: **1,537** at ~17h
- Likes/Reactions: 13
- Comments: 10
- Reshares: 1 (self-repost already deployed — visible as duplicate at top of activity feed)
- Comments/reactions ratio: ~77% (10:13 — exceptionally high dialogue ratio; the advice format is pulling genuine replies)

**Metrics (~41h refresh 2026-06-04 10:13 daily scan — 24h checkpoint fell between scans, back-captured here):**
- Impressions: **2,665** (+1,128 since 1,537 @ 17h on 2026-06-03 — solid recovery, the post found a second-degree push overnight)
- Likes/Reactions: 21 (+8 since 2026-06-03)
- Comments: 10 (no change — comment velocity stalled while reach grew)
- Reshares: 1 (self-repost only)
- Note: The overnight jump (+1,128 imp) lifts this off the 🔴 floor into 🟡 territory — already past the 2,500 middling line at ~41h, a much better trajectory than the 17h read suggested. Still ~6x softer than the same-topic Tough-days (10,969 @ 18h) — the absence of named anchors + a generous offer keeps it out of the reshare-driven ⭐ band, but the advice-listicle is at least clearing the median (2,070). 72h due 2026-06-05; 7d FINAL 2026-06-09.

**Metrics (~4d refresh 2026-06-06 10:13 daily scan — 72h back-capture, was due 2026-06-05):**
- Impressions: **4,102** (+1,437 since 2,665 on 2026-06-04 — kept climbing past 72h, solid 🟡 and approaching the 5K ✅ floor)
- Likes/Reactions: 23 (+2 since 2026-06-04)
- Comments: 10 (no change — comment velocity fully stalled; the 77% ratio was a first-day phenomenon)
- Reshares: 0 organic (self-repost aged off feed view)
- Note: At ~4d, 4,102 imp is a much healthier 🟡 than the 17h read suggested — the advice-listicle clears the median comfortably and may touch the 5K ✅ floor by 7d (2026-06-09). But it's still ~3.6x softer than the same-topic Tough-days (14,798 ✅⭐) — A/B confirmed: the reshare engine (named anchors + concrete offer) is what separates a 🟡 advice-listicle from a top-10% market-empathy post. Comment dialogue did NOT convert into a sustained second reach wave.

**Metrics (~5d refresh 2026-06-07 10:13 daily scan):**
- Impressions: **4,190** (+88 since 4,102 on 2026-06-06 — plateauing just under the 5K ✅ floor)
- Likes/Reactions: 24 (+1)
- Comments: 10 (no change — comment velocity remains fully stalled)
- Reshares: 0 organic
- Note: Growth has all but stopped — the +88 over a day suggests the 7d FINAL (2026-06-09) will likely land ~4,200-4,400 and miss the 5K ✅ floor → 🟡 verdict. Confirms the A/B read: a generic advice-listicle on the layoff theme caps in the low-🟡 band, ~3.5x below the named-anchor + hiring-gift variant (Tough-days 14,798 ✅⭐).

**Metrics (~6d refresh 2026-06-08 10:13 daily scan — 7d FINAL due tomorrow):**
- Impressions: **4,589** (+399 since 4,190 on 2026-06-07 — picked back up after the plateau, now within striking distance of the 5K ✅ floor)
- Likes/Reactions: 24 (no change)
- Comments: 10 (no change — comment velocity remains fully stalled since day 1)
- Reshares: 0 organic
- Note: The +399 day-over-day revives the question of whether the 7d FINAL (2026-06-09) clears 5,000 → ✅ or lands just under → 🟡. Either way it stays ~3x below the same-topic Tough-days (14,798 ✅⭐), confirming the A/B: the reshare engine (named anchors + concrete hiring offer) is the reach multiplier, not the empathy theme alone.

**Metrics (~6.7d refresh 2026-06-09 10:13 daily scan — true 7d crosses this evening ~17h, FINAL locks next run):**
- Impressions: **4,644** (+55 since 4,589 @ ~6d on 2026-06-08 — plateaued; the +399 day-2-prior was the last meaningful push)
- Likes/Reactions: 25 (+1)
- Comments: 10 (no change — comment velocity dead since day 1)
- Reshares: 0 organic
- Note: At ~6.7d the post is flat at 4,644 — the true 7d FINAL (locks 2026-06-09 evening / next run) will land ~4,650-4,750, **just under the 5K ✅ floor → 🟡 verdict**. Confirms the A/B with same-topic Tough-days (14,798 ✅⭐, 15 reposts): the generic advice-listicle caps in the high-🟡 band, ~3x below the named-anchor + hiring-gift variant. The reshare engine, not the empathy theme, is the reach multiplier.

**Metrics (~7.7d, 7d FINAL — LOCKED, back-captured 2026-06-10 10:13 daily scan; true 7d crossed 2026-06-09 evening):**
- Impressions: **4,686** → **verdict: 🟡** (between 2,500-5,000 — landed just under the 5K ✅ floor exactly as projected)
- Likes/Reactions: 26 (+1 since 4,644 @ ~6.7d)
- Comments: 10 (no change — comment velocity dead since day 1; the 77% first-day ratio never produced a second wave)
- Reshares: 0 organic
- Engagement rate: ~0.77% (36 total engagements / 4,686 imp)
- **FINAL verdict: 🟡 (4,686 imp).** A/B with same-topic Tough-days (14,798 ✅⭐, 15 reposts) now CLOSED and confirmed: identical layoff/market-empathy theme, but the generic advice-listicle (no named companies, no hiring offer) caps at ~4.7K — **~3.2x below** the news-anchored + hiring-gift variant. The reshare engine (named anchors + a concrete generous offer), not the empathy theme alone, is what separates a mid-🟡 from a top-10% ✅⭐ market-empathy post.

**Analysis (FINAL):**
- What worked: The "34,454" hyper-specific stat + the "Or so they were told" undercut is a strong contrarian hook — it questions the AI-layoff panic narrative rather than amplifying it. The 8-point advice list is genuinely useful and empathetic. Comments-to-reactions at ~77% is one of the highest dialogue ratios in the log.
- Caveats:
  - **1,537 imp @ 17h is SOFT velocity for a market-empathy post.** Direct comparison: the **same-topic** Tough-days-Israeli-tech post hit **10,969 @ 18h** (✅/⭐, 14,511 @ ~5.7d). This post is ~7x softer at the equivalent checkpoint despite the identical layoff/empathy theme.
  - The difference appears structural: Tough-days named specific companies (Wix/Meta/Oracle/Cisco) AND offered a generous concrete action ("we're hiring, my DMs are open, I'll route your CV personally") that drove **15 reposts** — the log's most-reshared post. This post is generic friend-advice with no named anchor and no offer → only 1 (self) repost, so it isn't seeding new audiences.
  - "8 things I'd tell a friend" is a save-bait listicle; like other reductive-list openers it risks closing the dialogue loop — though the unusually high comment ratio suggests the empathy angle partially overrides that here.
- Trajectory: 1,537 @ 17h → projecting ~2,200-3,500 at 7d → tracking **🔴/🟡 borderline**.
- vs. Lior's baseline: near/just-above median (2,070) trajectory.
- vs. top-creator patterns: Market-empathy lane, but the advice-listicle variant rather than the news-anchored-empathy + hiring-gift variant that made Tough-days fly.

**Learnings (provisional, pending checkpoints):**
- Direct A/B forming: **same empathy topic, two structures.** News-anchored (named companies) + generous hiring offer (Tough-days, 14K+/15 reposts) vs. generic advice-listicle, no offer (this post, ~1.5K). Early read: the reshare-driving *offer* and *named anchors* are the reach engine, not the empathy theme alone.
- Watch whether the 77% comment ratio converts into a second reach wave or stays first-degree.

**Next checkpoints:** 2026-06-03 17h (24h), 2026-06-05 (72h), 2026-06-09 (7d FINAL).

---

### 2026-06-04 — "Let me just try one more prompt / 900 prompts later" (vibe-coding / AI-build grind) ✅
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7468172552377503744
**Topic tag:** #ai #vibecoding #building #prompting #founder
**Hook type:** Relatable inner-monologue + escalation ("'Let me just try one more prompt.' 900 prompts later:")
**Structure:** Quoted self-talk hook → comedic escalation reveal ("900 prompts later:") → body carried in the attached visual (image/carousel — caption is the hook only)
**Visual:** Image/carousel (the body/payoff lives in the visual; feed caption is just the two-line hook)
**Length:** ~10 words (caption); body in visual
**CTA:** TBD (not surfaced in caption — likely in the visual)

**Full post text (caption):**
> "Let me just try one more prompt."
> 900 prompts later:

**Metrics (at ~1-2h, first capture 2026-06-04 10:13 daily scan):**
- Impressions: **363** (was 312 at the first read ~30 min earlier — fresh, climbing)
- Likes/Reactions: 6
- Comments: 0
- Reshares: 0 (no self-repost yet)
- Note: Far too early to read trajectory (post is ~1-2h old). Caption-only-hook + payoff-in-visual is a new format for the log — most Lior winners carry the full argument in the text body. Watch whether burying the payload in the image suppresses dwell/reach. The "one more prompt → 900 later" vibe-coding joke is relatable AI-builder humor (adjacent to the contrarian-AI lane but lighter/comedic, not a news anchor or contrarian thesis).

**Metrics (~48h refresh 2026-06-06 10:13 daily scan — covers the missed 24h checkpoint):**
- Impressions: **3,312** (+2,949 since 363 @ ~1-2h — large overnight recovery; the caption-only-hook + payoff-in-visual format found reach despite the buried payload)
- Likes/Reactions: 35 (+29)
- Comments: 1 (+1)
- Reshares: 0
- Note: The 2026-06-05 run did not execute so the 24h checkpoint is unlocked; this 48h read shows the format is NOT suppressed — already in solid 🟡 territory (past 2,500) and climbing. The relatable AI-builder humor traveled. Tracking 🟡 toward 7d FINAL. First evidence in the log that a caption-only + payoff-in-visual format can clear the median.

**Metrics (~72h LOCK, snapshot 2026-06-07 10:13 daily scan):**
- Impressions: **3,678** (+366 since 3,312 @ ~48h on 2026-06-06 — reach now crawling after the overnight surge)
- Likes/Reactions: 39 (+4)
- Comments: 1 (no change)
- Reshares: 0
- Note: At 72h the caption-only-hook + payoff-in-visual format is confirmed holding above the median (2,070) in solid 🟡 territory — the buried-payload format did NOT suppress reach. Velocity has flattened (most of the lift came in the first 48h); 7d FINAL (2026-06-11) likely lands ~3,800-4,200 → 🟡 verdict. First log evidence that a comedic caption-only AI-builder post can clear the median without a news anchor or contrarian thesis.

**Metrics (~4d refresh 2026-06-08 10:13 daily scan):**
- Impressions: **4,963** (+1,285 since 3,678 @ 72h on 2026-06-07 — velocity REACCELERATED after the flatten, a second reach wave landed; now knocking on the 5K ✅ floor)
- Likes/Reactions: 48 (+9 since 2026-06-07)
- Comments: 3 (+2)
- Reshares: 0
- Note: The +1,285 day-over-day jump revises the trajectory upward — the post is now ~4,963 at ~4d, materially above the 72h-flatten projection, and may clear the 5,000 ✅ floor by the 7d FINAL (2026-06-11). The comedic caption-only + payoff-in-visual format is not just clearing the median — it found a genuine second wave. Strongest evidence yet that the buried-payload comedic format can reach ✅ territory without a news anchor or contrarian thesis.

**Metrics (~5d refresh 2026-06-09 10:13 daily scan):**
- Impressions: **5,150** (+187 since 4,963 @ ~4d on 2026-06-08 — **crossed the 5,000 ✅ floor**; the second wave that landed at ~4d carried it over the line)
- Likes/Reactions: 49 (+1 since 2026-06-08)
- Comments: 3 (no change)
- Reshares: 0
- Note: At ~5d the comedic caption-only-hook + payoff-in-visual post has cleared the **5K ✅ floor** — the first ✅-trajectory post in the log to do so WITHOUT a news anchor or contrarian thesis (pure relatable AI-builder humor). Reaction velocity has flattened (engagement frozen for 2 days) but reach keeps creeping; 7d FINAL (2026-06-11) now likely lands ~5,200-5,500 → ✅ verdict. Confirms the new format read: a buried-payload comedic AI-build post can reach ✅ on relatability alone.

**Metrics (~6d refresh 2026-06-10 10:13 daily scan — 7d FINAL due TOMORROW):**
- Impressions: **5,543** (+393 since 5,150 @ ~5d on 2026-06-09 — still climbing past the 5K floor, the second wave has real legs)
- Likes/Reactions: 49 (no change since 2026-06-09 — engagement fully frozen, reach-only growth)
- Comments: 3 (no change)
- Reshares: 0
- Note: At ~6d the post is at 5,543 and still adding ~390/day — the 7d FINAL (2026-06-11) now projects ~5,700-6,000 → **solid ✅ verdict locked-in**. Confirms decisively: a comedic caption-only-hook + payoff-in-visual AI-build post reaches ✅ territory on pure relatability, no news anchor / no contrarian thesis / no credential. New repeatable format for the log.

**Metrics (at 7 days — FINAL, locked 2026-06-11 10:13 daily scan):**
- Impressions: **5,825** → **verdict: ✅** (+282 since 5,543 @ ~6d on 2026-06-10 — cleared the 5,000 floor and kept climbing through the full 7-day window)
- Likes/Reactions: 51 (+2 since 2026-06-10 — engagement was frozen for days, then ticked up slightly into the close; reach-led growth throughout)
- Comments: 3 (no change)
- Reshares: 0
- Engagement rate: ~0.93% (54 total engagements / 5,825 imp — low ratio, classic reach-led-not-engagement-led shape)

**Analysis:**
- What worked: The comedic caption-only-hook + payoff-in-visual format reached ✅ on **pure relatability** — no news anchor, no contrarian thesis, no credential flex. The "'one more prompt' → 900 prompts later" inner-monologue is instantly recognizable to every builder using AI tools; the joke traveled on identification alone. Reach built in two waves (overnight surge to 3,312 by 48h, then a second wave at ~4d that carried it over 5K) rather than a single first-day spike.
- What didn't: Engagement is thin (0.93% rate, 51 react / 3 comm / 0 reshares) — the format earns reach but not dialogue or saves. Burying the payoff in the visual means no quotable principle in the feed text, so nothing to debate or reshare. This is a reach-only win, not a save/authority win.
- vs. Lior's baseline: ✅ (above the 5,000 floor), comfortably above the ~2,070 median. Mid-pack among Lior's ✅ posts — well below the AI-mega-winners (Google 146K, Anthropic 92K) and the credential-milestone ⭐ posts, but a clean win for a low-effort comedic format.
- vs. top-creator patterns: Matches the **visual-carried / payoff-in-the-image** lane seen in Dan Koe's "Just one hour. Please." (2,541) and Hormozi's quote-cards — the feed text is bait, the image is the substance. First confirmed ✅ for this lane in Lior's log.

**Learnings applied going forward:** Caption-only-hook + payoff-in-visual comedic AI-builder posts are a **confirmed ✅ reach format** — repeatable for low-stakes relatable humor (n=1 strong). Use it when the goal is reach/top-of-funnel, NOT saves or authority. Don't over-deploy: the thin engagement means it won't build the credential/depth signal that the milestone and contrarian-AI lanes do. Best as an occasional palate-cleanser between heavier first-person-proof posts.

**Next checkpoints:** FINAL locked. Long-tail only.

---

### 2026-06-08 — "your accent was the dealbreaker" (vulnerability / self-acceptance) (in-flight)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7469746042029215745
**Topic tag:** #personal #vulnerability #founder #confidence #self-acceptance
**Hook type:** Quoted-rejection + self-implicating undercut ("'We loved everything about you, but your accent was the dealbreaker.' I heard that sentence too many times. Said by me. Never once by an investor.")
**Structure:** Quoted-rejection hook → undercut twist (the critic was himself, not any investor) → 20-year backstory (shame, hundreds of hours of recorded English, coaching, every accent hack) → the flaw stayed → resolution (stopped waiting, built AutoDS / put out content / spoke on stages anyway) → universal reframe ("we all have that one flaw we're sure everyone notices first") → principle ("whatever you're putting off until you fix yourself, it's rarely the thing in your way") → twist close ("You are (:")
**Visual:** Image — Lior speaking on stage, headset mic + presentation clicker (visually proves the "spoke on stages with it anyway" line; alt text confirms conference-stage photo)
**Length:** ~165 words
**CTA:** None / soft reflective twist close ("You are (:")

**Full post text:**
> "We loved everything about you, but your accent was the dealbreaker."
> I heard that sentence too many times.
> Said by me. Never once by an investor.
> For 20 years, I've been ashamed of my accent.
> Hundreds of hours of recorded English content.
> Coaching. Every accent hack on the internet.
> The Russian accent stayed.
> So I stopped waiting for it to leave.
> I built AutoDS - Automatic Dropshipping Tools, put out content to thousands, and spoke on stages with it anyway.
> We all have that one flaw we're sure everyone notices first.
> And we tell ourselves that's the reason it's worth waiting.
> Whatever you're putting off until you fix yourself, it's rarely the thing in your way.
> You are (:

**Metrics (at ~17h, first capture 2026-06-09 10:13 daily scan):**
- Impressions: **905** at ~17h
- Likes/Reactions: 16
- Comments: 4
- Reshares: 1 (self-repost already deployed — visible as the duplicate at the top of the activity feed, matches Lior's posting rule)
- Comments/reactions ratio: ~25% (4:16 — healthy early dialogue, consistent with the vulnerability lane)

**Analysis (early):**
- What worked: The hook is a quoted rejection with a **self-implicating undercut** ("Said by me. Never once by an investor.") — the same own-the-flaw honesty that made the Birthday and YouTube-milestone reframes land. The on-stage photo is a smart proof device: it shows him doing the exact thing the accent supposedly disqualified him from. Crucially this is NOT a bait-and-switch — it delivers a genuine self-acceptance lesson with no CTA payload, unlike "I got rejected" 🔴 (which baited a story and delivered a job listing).
- Caveats:
  - **905 imp @ 17h is soft velocity**, consistent with the personal-vulnerability lane, which caps ~2-3K (Wim Hof cold-feet 2,662, "I got rejected" 2,066). No news anchor, not the contrarian-AI or credential-milestone ⭐ lanes.
  - The vulnerability lane reliably earns the **highest engagement rate** but the **lowest absolute reach** — the algorithm tends to read these as personal/lifestyle and hold them to first-degree network.
- Trajectory: 905 @ 17h → projecting ~1,800-2,800 at 7d → tracking **🟡/🔴 borderline** (likely just around the 2,500 line, same band as Wim Hof cold-feet 2,662 🟡).
- vs. Lior's baseline: near/just-below median (2,070) trajectory.
- vs. top-creator patterns: "Real person on a real path" vulnerability lane — best engagement-rate category, build-audience-loyalty play rather than a reach play. Don't judge on impressions alone.

**Learnings (provisional, pending checkpoints):**
- A/B against "I got rejected" 🔴: same rejection-hook DNA, but this one pays off the hook with a real lesson (no hiring bait) — test whether the honest payoff lifts it above the bait-and-switch version.
- Confirm the vulnerability-lane reach cap (~2-3K) and high engagement-rate signature.

**Metrics (~41h refresh 2026-06-10 10:13 daily scan — 24h checkpoint fell between scans, back-captured here):**
- Impressions: **1,409** (+504 since 905 @ ~17h on 2026-06-09 — modest overnight accrual, consistent with the vulnerability lane's low-reach signature)
- Likes/Reactions: 26 (+10 since 2026-06-09)
- Comments: 4 (no change)
- Reshares: 0 organic (self-repost aged off the top-feed view)
- Note: At ~41h the post sits at 1,409 imp — tracking right on the 🟡/🔴 borderline, projecting ~2,000-2,600 at 7d (Wim Hof cold-feet band). Reactions kept climbing (+10) while comments froze — the highest-engagement-rate / lowest-reach vulnerability signature holds. 72h due 2026-06-12; 7d FINAL 2026-06-15.

**Metrics (~65h refresh 2026-06-11 10:13 daily scan):**
- Impressions: **1,557** (+148 since 1,409 @ ~41h on 2026-06-10 — slow steady accrual, the vulnerability lane's low-reach signature holds firmly)
- Likes/Reactions: 28 (+2 since 2026-06-10)
- Comments: 4 (no change)
- Reshares: 0 organic
- Note: At ~65h the post is at 1,557, adding ~+74/day — projecting ~1,800-2,100 at 7d → tracking **🔴/🟡 borderline**, likely landing just under or near the 🟡 floor (Wim Hof cold-feet 2,530 band but softer). Comments fully frozen at 4 since ~17h; reactions creep slowly — the highest-engagement-rate-but-lowest-reach vulnerability signature is textbook here. 72h locks tomorrow (2026-06-12); 7d FINAL 2026-06-15.

**Next checkpoints:** 2026-06-12 (72h), 2026-06-15 (7d FINAL).

---

### 2026-06-09 — "The Founder's Guide: 7 things about building an AI startup in 2026" (event-recap / secondhand-wisdom listicle) (in-flight)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7470103427205828608
**Topic tag:** #startups #ai #founders #building #vc
**Hook type:** Insider-room credential + promise ("I sat in a room with 23 founders who've already sold companies in multi-million dollar deals. Here's what they'd tell you before you build anything")
**Structure:** Title label ("The Founder's Guide: 7 things…") → insider-room setup (23 exited founders) → 7-point numbered list (tech doesn't impress / go vertical / stay small / speed / love the problem / commitment / see what customers can't ask for) → synthesis line (building today is about leveraging AI, not tech stack) → event thanks + name-tags → closing question
**Visual:** Text post (no image/carousel surfaced in feed view; long-form text)
**Length:** ~290 words
**CTA:** Open question — "Which point resonated with you most? I'd love to hear your thoughts in the comments."

**Full post text:**
> The Founder's Guide: 7 things about building an AI startup in 2026
> I sat in a room with 23 founders who've already sold companies in multi-million dollar deals.
> Here's what they'd tell you before you build anything:
> 1. Technology no longer impresses investors.
> What they're really betting on is the team and how it executes.
> 2. Go vertical, not horizontal.
> The real opportunities lie in the narrow, complex niches that require strong branding and a deep understanding of your audience.
> 3. Stay small on purpose.
> Almost every company in that room had ten people or fewer. Lean to a point that's honestly a little scary.
> 4. Speed beats everything.
> The market shifts quickly, and the advantage goes to whoever sees where it's heading first.
> 5. Fall in love with the problem, not the solution.
> Solutions get replaced overnight. A real problem stays exactly where it is.
> 6. Commitment is what actually carries you.
> To an investor, a partner, or a customer. It's what keeps you moving through the unglamorous, unexciting days that make up most of building a company.
> 7. See what customers can't ask for yet.
> Henry Ford said it best: "If I had asked people what they wanted, they would have said faster horses."
> Building a startup today is less about your tech stack and more about how well you leverage AI to run the company.
> Thanks to Alon Huri, Ronen Assia, Yuval Tal, the PEF Community, and Team8 for organizing a great event.
> Great to share the room with [13 named founders].
> Which point resonated with you most? I'd love to hear your thoughts in the comments.

**Metrics (at ~17h, first capture 2026-06-10 10:13 daily scan):**
- Impressions: **1,091** at ~17h
- Likes/Reactions: 28
- Comments: 6
- Reshares: 1 (self-repost already deployed — visible as the duplicate at the top of the activity feed, matches Lior's posting rule)
- Comments/reactions ratio: ~21% (6:28 — healthy early dialogue, the "which point resonated?" question is pulling replies)

**Analysis (early):**
- What worked: The insider-room credential hook ("23 founders who've already sold companies") borrows the same authority-anchor that powers the credential-milestone ⭐ lane (Birthday). The 7-point list is tight and quotable, and the closing question is a clean dialogue invite (already converting at ~21% comment ratio).
- Caveats:
  - **1,091 imp @ 17h is SOFT velocity** — well below the credential-milestone ⭐ posts at equivalent checkpoints (Birthday 9,621 @ 17h, Tough-days 10,969 @ 18h). The difference: this is *secondhand* wisdom (what 23 OTHER founders would tell you), not Lior's own first-person milestone or contrarian thesis. The save-bait listicle format also risks closing the dialogue loop.
  - Closest comparison is the 70% / 10-80-10 framework-listicle posts (1,783 / 1,701 🔴) and the CEO-3-rules listicle (2,083 🔴) — generic-advice numbered lists cap in the low band even with a credential hook. The Birthday listicle flew because it was *Lior's own* 10 lessons from *his own* exit, not a room of other people's.
  - The "see what customers can't ask for" Henry Ford quote is recognizable SaaS-Twitter wallpaper.
- Trajectory: 1,091 @ 17h → projecting ~1,800-2,600 at 7d → tracking **🔴/🟡 borderline**.
- vs. Lior's baseline: near/just-below median (2,070) trajectory.
- vs. top-creator patterns: Event-recap + numbered-advice listicle. Memory rule [feedback-conference-recap-posts-flatline] confirmed: recap posts flatline without a concrete first-person AutoDS-production stake — this one stays at the observer's altitude (what others said), which is exactly the flatline pattern.

**Learnings (provisional, pending checkpoints):**
- A/B forming: *first-person* credential-listicle (Birthday "my 10 lessons" 18,009 ⭐) vs. *secondhand* credential-listicle (this post, "7 things 23 founders would tell you"). Early read: the reach engine is Lior's OWN lived proof, not borrowed room-authority.
- Watch whether the ~21% comment ratio converts to a second reach wave or stays first-degree (same question that 34,454-layoffs failed).

**Metrics (~41h / 24h LOCK 2026-06-11 10:13 daily scan):**
- Impressions: **1,467** (+376 since 1,091 @ ~17h on 2026-06-10 — modest overnight accrual; the secondhand-listicle reach cap is asserting itself early)
- Likes/Reactions: 34 (+6 since 2026-06-10)
- Comments: 7 (+1 since 2026-06-10)
- Reshares: 1 (self-repost; no organic reshares)
- Comments/reactions ratio: ~21% (7:34 — dialogue holding, the "which point resonated?" question keeps pulling replies, but it is NOT converting to a reach wave)
- Note: At 24h the post is at 1,467 — the ~21% comment ratio earns dialogue but the reach stays first-degree (same failure mode as 34,454-layoffs, which also had high comment-ratio + no second wave). Tracking **🔴/🟡 borderline**, projecting ~1,900-2,400 at 7d. Confirms the early A/B read: *secondhand* credential-listicle ("7 things 23 founders would tell you") caps in the low band, unlike *first-person* credential-listicle (Birthday "my 10 lessons" 18,009 ⭐). The reach engine is Lior's OWN lived proof, not borrowed room-authority. 72h due 2026-06-13; 7d FINAL 2026-06-16.

**Next checkpoints:** 2026-06-13 (72h), 2026-06-16 (7d FINAL).

---

### 2026-06-10 — "AutoDS now talks to Claude" (product-launch / founder-pride) (in-flight)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7470467368805117952
**Topic tag:** #ai #autods #anthropic #claude #building #product
**Hook type:** Announcement reveal ("I can finally share: AutoDS now talks to Claude")
**Structure:** Reveal hook → what-it-does feature list (find/research products, build dashboard, audit/fix/publish) → market-trend thesis ("users are moving their workday into AI assistants; products that don't meet them there will quietly fall out of the workflow") → team credit (5 named engineers) → "0 to 1" pillar close
**Visual:** Image/graphic (product/connector announcement visual; not surfaced as text)
**Length:** ~110 words
**CTA:** None explicit (founder-pride close, no question or link)

**Full post text:**
> I can finally share: AutoDS - Automatic Dropshipping Tools now talks to Claude.
> We just launched a connector that lets Claude work directly inside our stores.
> What it can do:
> • Find and research winning products
> • Build a full store dashboard
> • Audit, fix, and publish straight to your store and much more
> Anthropic became part of everyone's workday this year, ours included. This is where the market is heading: users are moving their workday into AI assistants, and products that don't meet them there will quietly fall out of the workflow.
> Proud of the people who took it from idea to production: Tomer Rubinstein, Sergey Shubin, Demian Vyrozub, Anton Timofeev, Yuriy Poltorak. Watching a small team move that fast is why I still love the 0 to 1 stage more than anything else (:

**Metrics (at ~17h, first capture 2026-06-11 10:13 daily scan):**
- Impressions: **1,132** at ~17h
- Likes/Reactions: 28
- Comments: 0 (none surfaced in social-counts)
- Reshares: 3 (organic — notable; the product-launch announcement is being shared by team/network)
- Note: Self-repost already deployed (duplicate at top of feed, matches Lior's posting rule).

**Analysis (early):**
- What worked: Names Claude/Anthropic in the hook — the same trending-tool anchor that powers the contrarian-AI mega-winners (Google 146K, Anthropic 92K). The "0 to 1" pillar close + team credit is on-brand founder-pride. 3 organic reshares at 17h is healthy for a product post (the announcement has built-in share value for the team).
- Caveats:
  - **This is a PRODUCT-LAUNCH post, not Lior's personal founder-journey lane** — memory rule [feedback-lior-personal-brand-not-autods] flags AutoDS product marketing as off the personal brand. It reads as a company announcement with a founder-pride wrapper, not a first-person story or contrarian thesis.
  - **1,132 imp @ 17h is soft velocity** — far below the contrarian-AI lane's mega-winners at equivalent checkpoints (those named a trending tool to make a *contrarian argument*; this one names Claude to *announce a feature*). The AI anchor without a contrarian/personal frame is the same setup that bombed the Microsoft+Anthropic workshop post (1,175 🔴).
  - The feature-list body (bullet points of what it does) is product-page copy, not a story — no dwell-driving narrative.
- Trajectory: 1,132 @ 17h → projecting ~1,800-2,800 at 7d → tracking **🔴/🟡 borderline**. Watch whether the 3 reshares seed a second wave (team networks) or it caps first-degree like the MS+Anthropic post.
- vs. Lior's baseline: near/just-below median (2,070) trajectory.
- vs. top-creator patterns: Product-announcement lane — distinct from the contrarian-AI commentary lane that wins big. The AI-tool NAME is not the multiplier; the contrarian/personal FRAME is. This post has the name without the frame.

**Learnings (provisional, pending checkpoints):**
- A/B forming: contrarian-AI-commentary (Google/Anthropic mega-winners) vs. AI-product-announcement (this post + MS+Anthropic 1,175 🔴). Early read: naming a trending AI tool only wins when paired with a contrarian thesis or first-person fear/story — a feature announcement caps in the low band.
- Confirms memory rule [feedback-lior-personal-brand-not-autods]: AutoDS product content underperforms Lior's personal-journey lanes; if it must run, a story frame ("why we built this / what it cost us") would likely outreach a feature list.

**Next checkpoints:** 2026-06-12 (24h), 2026-06-14 (72h), 2026-06-17 (7d FINAL).

---

### 2026-06-12 — "Anthropic is quietly repricing Claude on June 15 / here's how to prepare" (contrarian-AI news anchor + tactical prescription + vendor-lock-in thesis) (in-flight)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7470830643392770049
**Topic tag:** #ai #anthropic #claude #agents #building
**Hook type:** Trending-tool news scoop + urgency ("Anthropic is quietly repricing Claude on June 15. Here's how to prepare.")
**Structure:** News-scoop hook → what's changing (subscription → metered credits for outside agents) → stakes ("your bill is about to multiply") → 3-step tactical prescription (1. get a Codex sub, 2. swap OpenClaw → Hermes, 3. point Hermes at your setup file) → personal-proof reveal (his whole system lives in Obsidian plain files on his own machine, backed up on GitHub) → meta-principle close ("A reprice only hurts when your setup lives inside the vendor") → open question CTA
**Visual:** Image/graphic (not surfaced as text)
**Length:** ~270 words
**CTA:** Open question — "How are you preparing for the change?"

**Full post text:**
> Anthropic is quietly repricing Claude on June 15.
> Here's how to prepare:
> Until now, you could wire external agents and tools like OpenClaw directly into your Claude subscription.
> They ran on the flat monthly fee, which was a steal. Anthropic was losing money on every power user.
> That deal is over.
> From next Monday, the subscription only covers Claude itself: the chat and Claude Code. Every agent wired in from outside moves to metered credits at full API rates.
> If your stack runs on third-party agents, your bill is about to multiply.
> 3 steps to get ahead of it:
> 1. Get a Codex subscription from OpenAI. Flat monthly fee. This becomes the engine for your outside agents.
> 2. Install Hermes instead of OpenClaw. It runs on that Codex subscription instead of burning credits, and is also lighter and less buggy.
> 3. Point Hermes at the one file that documents your setup. It learns everything and picks up where the old agent left off.
> Claude stays your main tool.
> You keep chatting and coding with it directly, still on the subscription. Only the outside agents move off the metered credits.
> The whole switch takes minutes, but only because of how the setup is built.
> The entire system lives in Obsidian: plain files, sitting on my own machine.
> Every prompt sits in a single folder, backed up on GitHub. The model only reads from it. So moving an agent to a new engine means pointing it at that same folder and letting it learn. That's it.
> Even if OpenAI eventually makes the same move Anthropic just did, switching again will take minutes.
> A reprice only hurts when your setup lives inside the vendor.
> How are you preparing for the change?

**Metrics (at ~48h, first capture 2026-06-14 10:13 daily scan — 24h LOCK on 2026-06-13 was MISSED, no scan ran):**
- Impressions: **2,124** at ~48h
- Likes/Reactions: 15
- Comments: 3
- Reshares: 0
- Comments/likes ratio: ~20%
- Note: Self-repost deployed; post was edited after publishing.

**Analysis (early):**
- What worked: **Names Anthropic + Claude in the first 5 words** — the exact trending-tool news anchor that powers the contrarian-AI mega-winners (Google 146K, Anthropic 92K, Paperclip 30K). The vendor-lock-in meta-principle close ("A reprice only hurts when your setup lives inside the vendor") is a genuine, quotable thesis — the same insider-workflow + meta-principle shape as the Anthropic 92K post. The personal-proof reveal (Obsidian plain files on his own machine, GitHub-backed) is real first-person operator detail, not abstract advice. Mirrors his actual stack per [project-lior-agent-stack-hermes-codex]. Open-question close leaves an engagement gap.
- Caveats:
  - **The body is a 3-step tactical prescription** (get Codex, install Hermes, point at the file) — the same tactical-prescription structure that bombed Master Prompt (546 🔴), find-skills (792 🔴), and Microsoft+Anthropic workshop (1,175 🔴). This post is the cleanest test case in the log for whether a strong news anchor + meta-principle can *rescue* a tactical body.
  - **2,124 imp @ ~48h is soft-middling** — far below the contrarian-AI lane's mega-winners at equivalent checkpoints (those used the tool name to make a *contrarian argument*, not to deliver a *how-to*). It IS outpacing the pure tactical bombs (Master Prompt 546, MS+Anthropic 1,175), so the news anchor + meta-principle is lifting it above the tactical floor — but the prescription body looks to be capping the ceiling.
  - Names a competing vendor's tool (Codex/OpenAI) and a third-party agent (Hermes) as the recommended fix — unusually prescriptive/operational for the personal-brand lane.
- Trajectory: 2,124 @ ~48h → projecting ~2,500–3,500 at 7d → tracking **🟡/🔴 borderline**.
- vs. Lior's baseline: at/just-above median (2,070) trajectory.
- vs. top-creator patterns: contrarian-AI news anchor (strong) bolted to a tactical-prescription body (weak). Early read reinforces the lane rule: the trending-tool NAME plus a contrarian/meta FRAME beats the tactical floor, but a how-to body still caps reach well below the commentary mega-winners.

**Learnings (provisional, pending checkpoints):**
- Sharpens the AI-lane A/B: news anchor + meta-principle + first-person proof (this post) sits ABOVE the pure tactical bombs but BELOW the contrarian-commentary mega-winners — the body type, not just the anchor, governs the ceiling.
- A reprice/news post that ends as a how-to ("3 steps to get ahead of it") trades reach for utility; a contrarian *argument* about the same news would likely outreach the prescription.

**Next checkpoints:** 2026-06-13 (24h — MISSED), 2026-06-15 (72h), 2026-06-19 (7d FINAL).

---

<!-- ===== 2026-07-12 back-capture: 8 posts published during the 06-29→07-11 scan outage. All first-logged here. Dates for "1w" posts are approximate (LinkedIn shows "1w" for 7–13 days). ===== -->

### 2026-07-03 (approx, "1w") — "250 people on my team, I don't track hours" (macro-manager / autonomy manifesto) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7477356579235979264
**Topic tag:** #leadership #management #autonomy #scaling
**Hook type:** Credential + contrarian-confession ("250 people are on my team, and I don't track how many hours they work - I don't care.")
**Structure:** Contrarian confession → "instead of X, here's what I do" → 4-step numbered principle (hire self-runners / laser goals / milestones+OKRs / let them fail) → one-line thesis ("They need autonomy, not a babysitter") → 1-word CTA
**Visual:** Not captured this run (aged low in feed)
**Length:** ~70 words
**CTA:** "Agree?"
**Full post text:**
> 250 people are on my team, and I don't track how many hours they work - I don't care.
> Instead of tracking tasks, hours, or where they work from
> Here's what I do:
> 1. Hire people who can run on their own.
> 2. Give them laser-focused goals.
> 3. Track milestones and OKRs.
> 4. Let them fail and learn.
> Your team doesn't need a babysitter. They need autonomy.
> Agree?

**Metrics (first capture 2026-07-12, ~1w / effectively 7d FINAL):**
- Impressions: **3,374** → **verdict: 🟡**
- Reactions: 109 (highest of the 8-post batch); Comments: 15; Reposts: 2
**Analysis:** Same macro-manager/autonomy thesis as the Ofir post (3,404 🟡) two days later — the theme is a reliable mid-3K performer with strong reactions. Short, punchy, save-card numbered list + 1-word CTA. Reach-capped ~3.4K like the rest of the batch. Uses "250 people" as the central credential (on-rule per [feedback-stop-overusing-250-employees] — team size IS the subject here).

---

### 2026-07-04 (approx, "1w") — "Open your WhatsApp / Meta username + Meta AI" (trending-product news + builder takeaway) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7477715303322435585
**Topic tag:** #meta #whatsapp #ai #product #building
**Hook type:** Direct-question news scoop ("Open your WhatsApp. Are you part of the A/B test?")
**Structure:** Question hook → 2 Meta features (username reservation, in-chat Meta AI) with a how-to line → "both point the same direction" synthesis → builder meta-lesson ("walk into the workflow people already use") → 1-word CTA
**Visual:** Not captured this run
**Length:** ~190 words
**CTA:** "Agree?"
**Full post text:**
> Open your WhatsApp. Are you part of the A/B test?
> Meta just rolling out two features worth paying attention to:
> 1. Reserve your WhatsApp username
> WhatsApp is killing the need to share your phone number.
> Soon, people will reach you by a username instead, the same way they already do on Instagram.
> Grab yours before someone else takes it.
> To do it: update WhatsApp ⭢ Settings ⭢ Username ⭢ reserve one.
> 2. Meta AI inside your chats
> Meta is testing an AI you can talk to in any conversation, so you never have to open a separate app to use it.
> Both moves point in the exact same direction-
> Meta isn't sending you somewhere new. It's pulling more of your day into the one app already open on your phone.
> Here's what I take from it as a builder:
> Meta walked into the workflow people already use.
> Now reaching new people and getting answers from AI is possible without ever leaving the app.
> Think about where your users already spend their day, and be there.
> It's far easier than teaching them to leave their routine for something new.
> Agree?

**Metrics (first capture 2026-07-12, ~1w / effectively 7d FINAL):**
- Impressions: **3,032** → **verdict: 🟡**
- Reactions: 39; Comments: 11; Reposts: 0
**Analysis:** Trending-product news anchor (Meta/WhatsApp) that DOES land a builder meta-principle ("be where users already are") rather than a bare how-to — so it clears the ~3K mid-band, unlike the bare-AI-tool posts. Not a breakout: the news is adjacent to Lior's operator lane, not a personal-stake story. Confirms news + genuine meta-lesson > news + tactical checklist.

---

### 2026-07-04 (approx, "1w") — "A year ago Forbes added me to 30 under 30 / back in the room" (credential-milestone reflection) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7478083961689235456
**Topic tag:** #forbes30under30 #mindset #founders #reflection
**Hook type:** Credential anchor + scene ("A year ago, Forbes added me to their 30 under 30 list. Yesterday I was back in a room full of them")
**Structure:** Credential+scene hook → question ("what do they have in common?") → 3 numbered observations (they fail a lot / invest in themselves / still feel like impostors) → reframe for the reader ("if it feels heavy, you're in the right room") → open-question CTA
**Visual:** Image collage with partner/brand logos (GLIDAI, Wolt Benefits, ExpressVPN visible)
**Length:** ~135 words
**CTA:** "What's the one thing you've learned from people you look up to?"
**Full post text:**
> A year ago, Forbes added me to their 30 under 30 list.
> Yesterday I was back in a room full of them, and I spent most of it asking myself one question:
> What do all these people actually have in common?
> Founders. Scientists. Athletes. Completely different worlds.
> But sit with them long enough, and the same three things show up:
> 1. They failed. A lot. The wins get posted. The falls never do.
> 2. They invest in themselves. Sleep, health, focus.
> 3. They still feel like impostors. Even at the very top, the self-doubt never fully goes away.
> If what you are building feels heavy right now, that is not a sign you are failing.
> It might be the clearest sign you are in the right room.
> What's the one thing you've learned from people you look up to?

**Metrics (first capture 2026-07-12, ~1w / effectively 7d FINAL):**
- Impressions: **3,224** → **verdict: 🟡**
- Reactions: 117; Comments: 15; Reposts: 0
**Analysis:** Credential-milestone lane (Forbes 30u30 anchor) — but landed 🟡 (~3.2K), far below the Birthday "31/10 lessons" ⭐ (18,009) in the same lane. Difference: Birthday was Lior's own first-person lessons; this reflects on OTHERS in the room (secondhand wisdom), the same first-degree cap that held Founder's-Guide low. **⚠️ Brand-guardrail flag:** point 3 ("they still feel like impostors… self-doubt never fully goes away") brushes [feedback-lior-no-imposter-syndrome] — softened by being an observation about the group, not Lior's own confession, but on-brand it should be steered away from impostor framing.

---

### 2026-07-05 (approx, "1w") — "Finally I can go back to the beach / Fable 5 is back" (AI-model news + Opus vs Fable comparison) 🔴 BOMB
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7478319331647516672
**Topic tag:** #anthropic #claude #fable5 #opus #ai
**Hook type:** Playful confession + AI-model news ("Finally, I can go back to the beach. Anthropic just brought Claude Fable 5 back.")
**Structure:** Confession hook → "Claude is your smartest colleague now" → personal test anecdote (it fixed bugs unasked) → Opus 4.8 vs Fable 5 feature comparison (✅ bullet lists) → pricing note → meta-thesis ("the future goes to whoever balances capability/cost/reliability") → either/or CTA
**Visual:** Video (subway scene, person in a yellow vest)
**Length:** ~200 words
**CTA:** "So which one are you running, Fable 5 for maximum capability, or Opus 4.8 for maximum ROI?"
**Full post text:**
> Finally, I can go back to the beach.
> Anthropic just brought Claude Fable 5 back. The most powerful public model, live again.
> If you're in the "can't think without Claude" gang, here's what you need to know:
> Claude is shifting from your best worker → to your smartest colleague.
> Tested it last time it was live. I asked it to build a feature. Then, without me asking, it went back through the code, found bugs I hadn't even noticed, and fixed them on its own.
> So what actually changed?
> Opus 4.8: ✅ Strong coding, reasoning, and agentic workflows ✅ Better self-checking and error detection ✅ Far more cost-effective at scale
> Fable 5: ✅ Superior on the hardest coding and autonomous agent jobs ✅ Handles massive codebases and long-horizon planning ✅ Higher ceiling, at a significantly higher price
> Think of Opus 4.8 as your best full-time employee. Shows up every day, handles almost everything you throw at it, and never blows the budget.
> Fable 5 is the specialist consultant you call when nobody else can crack the problem. Brilliant, and priced like it- It's free only up to 50% of your weekly limit through July 7, then it moves to pay-per-use.
> The future of AI won't go to whoever builds the smartest model. It'll go to whoever balances capability, cost, and reliability into real business value.
> So which one are you running, Fable 5 for maximum capability, or Opus 4.8 for maximum ROI?

**Metrics (first capture 2026-07-12, ~7d FINAL):**
- Impressions: **1,222** → **verdict: 🔴 BOMBED (<1,500)**
- Reactions: 16; Comments: 5; Reposts: 0
**Analysis:** AI-model news anchor bolted to a spec-comparison/how-to body — the exact n=6-confirmed "AI-name-without-a-contrarian-thesis" dead-end (joins AutoDS-Claude 🔴, MS+Anthropic 1,175 🔴, Anthropic-Slack 1,798 🔴, Anthropic-repricing 2,124 🔴/🟡, Grok below). The "go to the beach" personal hook doesn't rescue a body that reads as a model-picker guide. Lowest reach + lowest engagement of the batch. **Learning: naming Anthropic/Claude/Fable/Opus and then explaining which model to use = reliably capped under ~2K.** Compare the same-week "Claude is a team of four" (3,027 🟡) — a cleaner original metaphor + signed illustration doubled the reach of this one, but even that stayed sub-3.1K.

---

### 2026-07-07 ("5d") — "I'm 31, bootstrapped to a multi-million exit / scaling a SaaS is lonely" (founder-journey / co-founder lesson) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7479889605165694979
**Topic tag:** #founders #saas #cofounder #scaling #exit
**Hook type:** Credential + curiosity-gap ("I'm 31. Bootstrapped my company to a Multi-million dollar exit. Here's what nobody tells you about scaling a SaaS past 8-figures")
**Structure:** Credential hook → curiosity promise → first-person loneliness story → advisor quote ("the CEO role is a lonely one") → resolution (brought in a partner, split tech/business) → either/or CTA
**Visual:** Illustration "The Journey of a Founder (probably)" — expectation-vs-reality squiggle chart
**Length:** ~200 words
**CTA:** "So what's your take: solo founder or building with a co-founder?"
**Full post text:**
> I'm 31. Bootstrapped my company to a Multi-million dollar exit.
> Here's what nobody tells you about scaling a SaaS past 8-figures:
> In my first year, it was all on me. Legal, product, customer support.
> At some point, I got to a place where I felt really lonely.
> I knew a CEO advisor back then. Since I couldn't afford to pay him, I gave him free access to my system in exchange for his advice.
> I was 21, and he looked at me and said, "Lior, the CEO role is a lonely one. That's what's waiting for you on the other side."
> It took me years to realize how right he was.
> Mentally, it burns you out, and practically, it's just too much for one person.
> Sooner or later, you have to bring in a partner.
> After a year, that's what I did. He took the tech, I took business, and the company started moving faster than one person ever could.
> So what's your take: solo founder or building with a co-founder?

**Metrics (first capture 2026-07-12, 5d — in-flight):**
- Impressions: **3,909** → **verdict: 🟡 (best reach of the 8-post batch, 7d FINAL due 2026-07-14)**
- Reactions: 56; Comments: 13; Reposts: 0
**Metrics (7d FINAL, back-capture 2026-07-15, ~8d):**
- Impressions: **4,175** → **verdict: 🟡 (best final of the batch; still under the 5K ✅ floor)**
- Reactions: 57; Comments: 17; Reposts: 0
**Analysis:** Best performer of the fortnight. First-person founder-journey with a concrete scene (the 21-year-old / unpaid advisor), a genuine credential hook, and a real vulnerability (loneliness = past hardship, on-rule per [feedback-lior-no-fear-confessions]). This is the lane that consistently beats the AI-model posts. Still capped under 5K — consistent with the month-long soft-reach band. Watch for a 7d lift.

---

### 2026-07-08 ("4d") — "Fable 5 cost me 3 nights of sleep / Claude is a team of four" (AI-model explainer + original metaphor) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7480252170936782848
**Topic tag:** #anthropic #claude #ai #models #workflow
**Hook type:** Confession + contrarian claim ("Fable 5 cost me three nights of sleep this week. And it made me realize most people use Claude wrong.")
**Structure:** Confession hook → news peg (subscription → pay-per-token) → original metaphor "Claude is a team of four" (Haiku/Sonnet/Opus/Fable each a role) → thesis ("matching model to task is the whole skill, same as matching people to roles") → either/or CTA
**Visual:** Signed illustration "Claude is a team of four" (Haiku the Sprinter / Sonnet the Workhorse / Opus the Heavy Lifter / Fable the Superhuman)
**Length:** ~135 words
**CTA:** "Do you switch models per task, or run everything through one?"
**Full post text:**
> Fable 5 cost me three nights of sleep this week.
> And it made me realize most people use Claude wrong.
> Starting today, Anthropic's smartest model is changing from: Subscription → pay per token.
> Which makes today the right day to learn who does what.
> Claude is a team of four:
> 1. Haiku takes the repetitive work. Tagging, filtering, first-line customer answers. Instant.
> 2. Sonnet is the daily workhorse. Emails, summaries, first drafts. The default.
> 3. Opus handles the heavy lifting. Complex code, deep analysis. Slower, but it never quits halfway.
> 4. Fable is the one you trust with the monsters. The projects you'd normally clear a week for. That's what kept me up.
> Matching the model to the task is the whole skill now. Same as matching people to roles.
> Do you switch models per task, or run everything through one?

**Metrics (first capture 2026-07-12, 4d — in-flight):**
- Impressions: **3,027** → **verdict: 🟡 (7d FINAL due 2026-07-15)**
- Reactions: 34; Comments: 16 (highest comment count of the batch)
**Metrics (7d FINAL, 2026-07-15):**
- Impressions: **3,459** → **verdict: 🟡 (middling; +14% over the 4d capture)**
- Reactions: 35; Comments: 18; Reposts: 0
**Metrics (post-final refresh, 2026-07-16, ~8d):**
- Impressions: **3,564** (long-tail drift past the 7d lock; verdict stays 🟡)
- Reactions: 35; Comments: 18; Reposts: 0
**Analysis:** The strongest of the four AI-model posts — an ORIGINAL metaphor ("team of four" tying models to team roles, echoing Lior's own management thesis) + a signed illustration, not a spec sheet. ~2.5x the reach of the same-week Fable5-beach spec-comparison (1,222 🔴). Still capped ~3K: even a good AI-explainer sits below the founder-story and contrarian-AI lanes. Highest comments-to-reach ratio of the batch = the "switch per task?" question drove discussion.

---

### 2026-07-09 ("3d") — "When Ofir Bokobza joined AutoDS / I don't have tasks for you" (macro-manager hiring philosophy) 🟡
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7480614165741486080
**Topic tag:** #hiring #management #autonomy #culture
**Hook type:** Scene + say-the-quiet-part ("When Ofir Bokobza joined AutoDS, I told him something most founders would never say out loud: 'I actually don't have tasks for you.'")
**Structure:** Named scene hook → the confession → parallel PA anecdote → principle ("I'm a super macro manager, I don't track time/place/tasks") → payoff ("I hand a goal, not a list; the ones who make an undefined role their own carry the company")
**Visual:** Photo — Times Square AutoDS billboard ("Best Dropshipping Software 2025")
**Length:** ~230 words
**CTA:** None (closes on principle) + "AutoDS - Automatic Dropshipping Tools" tag
**Full post text:**
> When Ofir Bokobza joined AutoDS, I told him something most founders would never say out loud:
> "I actually don't have tasks for you."
> I only knew that someone needed to take marketing, and that there were enough things there that needed to be done. I just didn't know what they were, so we started working it out together.
> It was the same when I brought in my first personal assistant.
> I told her I didn't know how to work with a personal assistant, and that we'd have to figure it out together. I wasn't going to be there to teach her each thing the role needed because she had to resolve that herself.
> That's how I set up the expectations from the very first interview.
> I do this because I'm a super macro manager.
> I don't track time, I don't track where people work from, and I don't track tasks at all.
> I'd rather give people the room to try and to fail than guide them and make sure they never do, because that freedom is what motivates them, and it's the only way I know how to manage.
> So I don't hand people a list, I hand them a goal.
> The ones who take a role I couldn't even define for them and make it completely their own are the ones who end up carrying the company.
> That's what I'm looking for in every single person I bring in.
> AutoDS - Automatic Dropshipping Tools

**Metrics (first capture 2026-07-12, 3d — in-flight):**
- Impressions: **3,404** → **verdict: 🟡 (7d FINAL due 2026-07-16)**
- Reactions: 89; Comments: 14; Reposts: 0
**Metrics (6d refresh, 2026-07-15):**
- Impressions: **3,619** → **verdict: 🟡 (tracking; 7d FINAL due 2026-07-16)**
- Reactions: 92; Comments: 14; Reposts: 0
**Metrics (7d FINAL, 2026-07-16):**
- Impressions: **3,659** → **verdict: 🟡 (middling; +1% over the 6d capture — reach fully plateaued)**
- Reactions: 92; Comments: 14; Reposts: 0
**Analysis:** Named-person scene + a genuinely contrarian confession ("I don't have tasks for you") = the macro-manager/autonomy thesis again, and again a reliable ~3.4K 🟡 (see the 250-people post, 3,374). Strong reactions. Closed ending (no open question) — consistent with the log's note that closed endings cap engagement, though the reactions held up here. Billboard visual = personal-artifact/brand-milestone family.

---

### 2026-07-10 ("2d") — "This month is insane for programming / Grok 4.5" (AI-model roundup + Grok review) 🔴
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7480977724845654017
**Topic tag:** #grok #xai #ai #models #coding
**Hook type:** Trend observation + list ("This month is insane for programming it's hard to keep up:")
**Structure:** "Insane month" hook → model roundup (Fable 5 / GPT 5.6 / Gemini 3.5 Pro / Grok 4.5) → Grok 4.5 launch note → honest first-impression bullets → when-to / when-not-to-use → pivot to "the real headline" (Musk's monthly-model claim) → either/or CTA
**Visual:** Shared third-party article — "Grok 4.5 Beats Fable 5 And Opus 4.8 In Agent AI Test With 51.4% Score" (with Grok UI screenshot)
**Length:** ~230 words
**CTA:** "Think Elon's models will overtake Anthropic?"
**Full post text:**
> This month is insane for programming it's hard to keep up:
> - Fable 5
> - GPT 5.6
> - Gemini 3.5 Pro
> - And today Grok 4.5
> SpaceX & Cursor launched Grok 4.5, xAI's smartest model yet, built for coding and agentic work.
> I gave it a serious run this morning.
> Honest first impression:
> - Fast
> - Fun to build with
> - Smart enough for most of the tasks I threw at it
> - Ridiculously cheap
> When to use it:
> - Everyday coding, debugging, and agent work: it handles them beautifully.
> - Anything that needs real-time data: it's the only model plugged straight into X.
> When not to use it:
> - The hardest problems, where one wrong decision costs weeks of work. Those still belong to the smartest models.
> But that's not the headline.
> In his X post, Musk promised a new model trained from scratch every month until the end of the year.
> Even OpenAI and Anthropic manage that only a few times a year.
> Think Elon's models will overtake Anthropic?
**Metrics (first capture 2026-07-12, 2d — in-flight):**
- Impressions: **1,141** → **verdict: 🔴 (2d, low velocity; 7d FINAL due 2026-07-17)**
- Reactions: 34; Comments: 13; Reposts: 0
**Metrics (5d refresh, 2026-07-15):**
- Impressions: **1,302** → **verdict: 🔴 (still tracking well below the 🟡 floor; 7d FINAL due 2026-07-17)**
- Reactions: 35; Comments: 14; Reposts: 0
**Metrics (6d refresh, 2026-07-16):**
- Impressions: **1,320** → **verdict: 🔴 (essentially frozen at ~1.3K; 7d FINAL due 2026-07-17 — will lock 🔴)**
- Reactions: 35; Comments: 14; Reposts: 0
**Metrics (9d — 7d FINAL, locked 2026-07-19; scan missed the 07-17/18 slots, Mac asleep):**
- Impressions: **1,347** → **verdict: 🔴 FINAL (BOMB, under 1,500; +27 over the 6d capture — dead-frozen)**
- Reactions: 35; Comments: 14; Reposts: 0
- Engagement rate: ~3.6% (high rate on tiny reach = first-degree audience only, no reach wave)
**Analysis:** Another AI-model post (Grok review) — soft 1,141 @ 2d, the weakest early velocity of the batch, tracking with the AI-name-without-thesis dead-end. The closing question ("will Elon overtake Anthropic?") is a genuine contrarian hook, so the 7d could recover above the Fable5-beach floor — but the body is a first-impression review, not a personal-stake argument. Shared-article visual (third-party authority family). **7d LOCKED 1,347 🔴** — the contrarian *question* at the end was not enough; a spec-sheet/first-impression body with the thesis bolted on as a closing line still bombs. This extends the AI-model-news-without-a-real-contrarian-thesis dead-end (Fable5-beach 1,222, Microsoft+Anthropic 1,175, Master Prompt 546, find-skills 792, and now Grok 1,347). The lane needs the thesis to BE the body, not the CTA.

---

### 2026-07-14 — "For two months, I had no idea one of our people had a disability / Paul's promotion" (culture / inspiring-teammate story) ✅ (7d FINAL: 5,721 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7482790928798093312 ✅ CORRECTED 2026-07-20 (was mis-logged as 7483024680992440320, which does not exist in the feed)
**Topic tag:** #culture #remote #disability #promotion #team #inspiration
**Hook type:** Confession/reveal ("For two months, I had no idea one of our people had a disability.") — under 10 words, provocative anchor, no "I"-as-ego opener
**Structure:** Reveal hook → remote-work context ("only knew him by his results") → the reveal (video call, Paul has cerebral palsy, crawls / types one-handed) → achievement stack (promoted to AI QA Specialist, 6 yrs support→Team Leader, starting over) → external proof (71K-follower Facebook gaming page) → admiration line → named congratulations (Paul John Redondo)
**Visual:** Photo (teammate)
**Length:** ~180 words
**CTA:** None (congratulatory close, names + tags the teammate)
**Full post text:**
> For two months, I had no idea one of our people had a disability.
> We're a fully remote company, so before our first call, I only knew him by his results.
> In those two months, I never once heard "I don't know how" or "it's impossible."
> When we finally jumped on a video call, I realized Paul has cerebral palsy.
> He moves by crawling with his arms, and he types everything with just one hand.
> Recently, he got promoted to a brand new role: AI QA Specialist.
> Six years at AutoDS, from customer support specialist to Team Leader, and now starting over in something completely unfamiliar.
> And he doesn't stop there.
> Outside of work, he runs a Facebook gaming page with 71,000 followers.
> One of the most inspiring people I've ever hired, and there's a lot to learn from him.
> Congratulations on the promotion, Paul John Redondo!

**Metrics (24h checkpoint, 2026-07-14→15, ~19h):**
- Impressions: **3,433** → **verdict: 🟡 (in-flight; strongest early velocity of the July batch)**
- Reactions: 76; Comments: 20; Reposts: 2
- Comments/reactions ratio: ~26% (deepest discussion of the batch)
**Metrics (~2d refresh, 2026-07-16, ~43h):**
- Impressions: **4,326** → **verdict: 🟡 (+26% over the 19h capture — steady climb, best-tracking post of the batch)**
- Reactions: 96; Comments: 24; Reposts: 1
- Comments/reactions ratio: ~25% (still the deepest discussion in-flight)
**Metrics (~5d refresh, 2026-07-19):**
- Impressions: **5,072** → **verdict: ✅ (CLEARED the 5K floor — first ✅-band July post; +17% over the ~2d capture)**
- Reactions: 111; Comments: 24; Reposts: 2
- Comments/reactions ratio: ~22% (still the batch's deepest discussion)
- ⚠️ Data-integrity: live feed maps this post's body to **urn:li:activity:7482790928798093312** (the URN the log had recorded for the DotDev post); the originally-logged Paul URN 7483024680992440320 no longer appears in the feed. Matched by content this run. Flag for Monday digest — likely a mis-recorded/self-repost URN swap between the two 07-14 posts; verify canonical permalinks.
**Metrics (~6d refresh, 2026-07-20):**
- Impressions: **5,248** → **verdict: ✅ (holding above the 5K floor; +3.5% over the ~5d capture — reach decelerating into the 7d lock)**
- Reactions: 115; Comments: 24; Reposts: 2
- Comments/reactions ratio: ~21%
- ✅ URN mismatch RESOLVED 2026-07-20 via DOM `data-urn` extraction: canonical Paul URN is **7482790928798093312**, canonical DotDev URN is **7482426311492190210**. The two 07-14 entries had swapped/mis-recorded URNs; both corrected in-place. No digest action needed.
**Metrics (8d — 7d FINAL, locked 2026-07-22; the 07-21 slot was missed, Mac asleep):**
- Impressions: **5,721** → **verdict: ✅ FINAL (cleared the 5K floor and held; +9% over the ~6d capture — still creeping at lock time)**
- Reactions: 120; Comments: 25; Reposts: 2
- Engagement rate: ~2.6%
**Analysis:** Human/culture-story lane with a named teammate and a genuine reveal — a different lane from the AI-model and macro-manager posts, and off to the best 24h start of the July batch (3,433 @ 19h with 76 reactions + 20 comments already). Confession-reveal hook does the work; on-brand as admiration for others, no self-flex, no impostor framing. This is the "journey/real-person" content the style rules say compounds. Watch for a reshare wave — 2 reposts + high comment ratio at 19h could pull the 7d well above the 🟡 band. **7d FINAL LOCKED 5,721 ✅** — the reshare wave never came (2 reposts at lock, same as day 1), so the ✅ was carried entirely by sustained first-degree reach plus the log's deepest comment ratio. Confirms **human/culture-reveal with a named, real teammate as a repeatable non-AI ✅ lane** — the second ✅ of the week alongside the Shopify-#1-affiliate proof post, breaking the ~7-week ✅ drought.

---

### 2026-07-14 — "Excited to see everyone at Shopify DotDev in Toronto / 20,000 cups" (conference-presence / brand-activation announcement) 🔴 (7d FINAL: 1,784 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7482426311492190210 ✅ CORRECTED 2026-07-20 (was mis-logged as 7482790928798093312, which is the Paul post)
**Topic tag:** #dotdev #shopify #toronto #conference #autods #brand
**Hook type:** Event announcement ("Excited to see everyone at Shopify DotDev in Toronto!") — opens on excitement, no number/confession anchor (weakest hook family)
**Structure:** Event announcement → last-year recap (2 branded coffee stations, 20,000+ cups poured, "every attendee walking around with our brand in hand") → connect CTA
**Visual:** Branded event graphic ("See you at DotDev / LIOR POZIN — CEO @ AUTODS", July 21-22 Toronto) — marketing-team graphic, the visual family the playbook flags as underperforming
**Length:** ~55 words
**CTA:** "If you're attending, I'd love to connect."
**Full post text:**
> Excited to see everyone at Shopify DotDev in Toronto!
> Last year was an absolute blast.
> We ran 2 branded coffee stations right outside the venue.
> Poured over 20,000 cups -
> meaning almost every single attendee was walking around with our brand in hand.
> If you're attending, I'd love to connect.
> See you in Toronto

**Metrics (24h checkpoint, 2026-07-14→15, ~1d):**
- Impressions: **1,424** → **verdict: 🔴/🟡 (reach-capped; high reactions relative to reach)**
- Reactions: 65; Comments: 13; Reposts: 1
**Metrics (~2d refresh, 2026-07-16):**
- Impressions: **1,498** → **verdict: 🔴 (only +5% in a day — reach cap holding just under 1.5K, exactly as the conference lane predicts)**
- Reactions: 66; Comments: 14; Reposts: 1
**Metrics (~5-6d refresh, 2026-07-19):**
- Impressions: **1,691** → **verdict: 🔴 (+13% over 3 days — inched up but firmly reach-capped, will lock 🔴 on 07-21)**
- Reactions: 72; Comments: 14; Reposts: 1
- ⚠️ Data-integrity: live feed maps this post's body ("Excited to see everyone at Shopify DotDev") to **urn:li:activity:7482426311492190210**, not the logged 7482790928798093312 (which the feed now maps to the Paul post). Matched by content. Flag for Monday digest — canonical permalink for DotDev may be 7482426311492190210.
**Metrics (~6d refresh, 2026-07-20):**
- Impressions: **1,707** → **verdict: 🔴 (+1% over the ~5-6d capture — fully plateaued, locks 🔴 tomorrow)**
- Reactions: 72; Comments: 14; Reposts: 1
- ✅ URN mismatch RESOLVED 2026-07-20 via DOM `data-urn` extraction: canonical DotDev URN is **7482426311492190210**. Corrected above; no digest action needed.
**Metrics (8d — 7d FINAL, locked 2026-07-22; the 07-21 slot was missed, Mac asleep):**
- Impressions: **1,784** → **verdict: 🔴 FINAL (+4.5% over the ~6d capture; never escaped the conference-lane cap)**
- Reactions: 72; Comments: 14; Reposts: 1
- Engagement rate: ~4.9% (highest rate in the July batch on the lowest reach — pure first-degree warmth)
**Analysis:** Conference-presence announcement — the lane that consistently flatlines (see the LangTalks recap 486 🔴 and the conference-recap note: these need a concrete operator/AutoDS-production moment, not a "see you there"). The 20,000-cups brand-activation stat is the one operator anchor and it's the post's best asset, but the body is a promo, the hook opens on "Excited," and the visual is a marketing graphic. Reach capped at 1,424 @ 24h despite unusually strong reactions (65) — an audience-warmth signal, not a reach one. **7d FINAL LOCKED 1,784 🔴** — third confirmation of the conference lane (LangTalks recap 486 🔴, this 1,784 🔴). The 4.9% engagement rate on 1.8K reach is the signature: the announcement lands warmly with people who already follow him and reaches nobody else. **Rule stands: "see you there" announcements do not distribute. The lane only works as a post-event operator scene with a production number** — and the 2026-07-22 DotDev learnings post is the live test of exactly that.

---

### 2026-07-15 — "How does a small startup get Shopify's attention? / #1 affiliate partner" (proof / case-study founder-journey) ✅ (7d FINAL: 5,624 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7483153311907540992
**Topic tag:** #shopify #partnership #proof #founderjourney #autods
**Hook type:** Question hook with named entity ("How does a small startup get Shopify's attention?") — under 10 words, concrete anchor (Shopify), curiosity-gap
**Structure:** Question hook → "Here's the story" → 2024 context (Shopify dropshipping growing, "we weren't there") → mission framing → the move (emailed Shopify, put in writing "we will become your biggest partner in 2024") → build → payoff (Shopify >50% of business; hit #1 affiliate partner in 2024, repeated in 2025) → principle close ("that is how a small player earns the attention of someone much bigger")
**Visual:** Image (not inspected this run — "Activate to view larger image")
**Length:** ~180 words
**CTA:** None (closes on principle)
**Full post text:**
> How does a small startup get Shopify's attention?
> Here's the story:
> In 2024, Shopify dropshipping was alive, growing, and bigger than we had imagined.
> The problem? We weren't there.
> Our mission was to help as many people as possible make money online.
> If the market was moving to Shopify, we had to move too.
> We knew the rule giants play by: they start paying attention when you prove yourself in numbers.
> So here's what I did:
> I sent Shopify an email and put it in writing: we will become your biggest partner in 2024.
> Then we kept building.
> Shopify grew to more than 50% of our business.
> And in 2024, we hit exactly what I promised, and did it again in 2025- became Shopify's #1 affiliate partner.
> We aimed for it, kept building, and we hit it.
> That is how a small player earns the attention of someone much bigger.

**Metrics (first capture 2026-07-16, ~17h):**
- Impressions: **3,581** → **verdict: 🟡 (in-flight; solid early velocity, self-reposted within the first day)**
- Reactions: 63; Comments: 15; Reposts: 2
- Comments/reactions ratio: ~24%
**Metrics (~4d refresh, 2026-07-19):**
- Impressions: **5,249** → **verdict: ✅ (CLEARED the 5K floor — highest of the July batch; +47% over the 17h capture, best reach-climb of the batch)**
- Reactions: 86; Comments: 25; Reposts: 1
- Comments/reactions ratio: ~29% (deep discussion)
**Metrics (~5d refresh, 2026-07-20):**
- Impressions: **5,343** → **verdict: ✅ (holding above the 5K floor; +1.8% over the ~4d capture — climb has flattened, but the ✅ band looks safe for the 07-22 lock)**
- Reactions: 86; Comments: 25; Reposts: 1
- Comments/reactions ratio: ~29% (unchanged, still the batch's deepest)
**Metrics (7d FINAL, locked 2026-07-22):**
- Impressions: **5,624** → **verdict: ✅ FINAL (+5.3% over the ~5d capture — climbed through the lock, best final since "900 prompts" 5,825 on 2026-06-11)**
- Reactions: 88; Comments: 25; Reposts: 1
- Engagement rate: ~2.0%
**Analysis:** Proof / case-study founder-journey — same lane as the Funnel-conversion 40% "Shopify partner thanks" post (3,352 🟡, 9 reshares) and consistent with the month-long soft-reach band (this batch lives 1.2K–4.3K). Strong 17h start (3,581) with a healthy comment ratio; the named-goal-then-delivered arc (emailed Shopify → became #1 affiliate partner) is a concrete operator story, not a promo. On-brand: proof through a specific milestone, "the giant notices you when you prove yourself in numbers" reads as earned outcome, no flex, Shopify treated as partner (never criticized). Watch for a reshare wave on the 24h/72h checkpoints — this lane's ceiling is set by reposts. **7d FINAL LOCKED 5,624 ✅** — and the reshare wave never arrived (1 repost), which revises that hypothesis: this post cleared 5K on reach alone, exactly like Paul-disability. **Concrete-proof founder-journey is now a confirmed non-AI ✅ lane.** DNA: question hook naming a giant + a promise put in writing + the number that proves it was kept. Reusable.

---

### 2026-07-16 — "My trainer asked one question I couldn't answer / find the hour or find the story" (personal-discipline scene → business parallel) 🟡 (7d FINAL: 3,286 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7483513492973617152
**Topic tag:** #discipline #focus #mindset #excuses #founderlesson
**Hook type:** Confession/reveal ("My trainer asked one question I couldn't answer.") — under 10 words, curiosity-gap + confession anchor, no ego-"I"
**Structure:** Confession hook → personal scene (10 yrs of travel, fitness routine, every long trip cost 1-2 kg muscle) → the ready-made excuse ("that's just how travel works") → the trainer's sting question → admission → business-parallel triplet ("We can't grow without more funding" / "our market is slow" / "no time for that") → principle ("When something truly matters, you find the hour. When it doesn't, you find the story.") → forward commitment (a month of travel ahead, no lost muscle) → closing aphorism ("The truth is whatever we keep telling ourselves.")
**Visual:** Image (personal artifact family)
**Length:** ~200 words
**CTA:** None (open principle — leaves an engagement gap)
**Full post text:**
> My trainer asked one question I couldn't answer.
> For 10 years, I've been traveling a lot. Work and pleasure.
> Fitness comes first: gym 2-4 times a week, tennis twice.
> But every trip longer than a week broke it. 1-2 kg of muscle gone, months to earn it back.
> The explanation was always ready: "That's just how travel works."
> This time, my trainer heard it and asked, "If it really matters to you, can't you find one hour for a gym while traveling?"
> That stung. He was right. The excuse was never about time.
> I see the same pattern in business:
> "We can't grow without more funding."
> "Our market is just slow."
> "There's no time for that."
> When something truly matters, you find the hour. When it doesn't, you find the story.
> I have over a month of straight travel ahead. This time, no lost muscle. No lost momentum.
> The truth is whatever we keep telling ourselves.

**Metrics (~3d / 72h checkpoint, 2026-07-19):**
- Impressions: **2,952** → **verdict: 🟡 (in-flight; mid-band, tracking the founder-lesson lane)**
- Reactions: 39; Comments: 18; Reposts: 0
- Comments/reactions ratio: ~46% (unusually deep discussion for the reach — the question-and-parallel format pulls comments)
**Metrics (~4d refresh, 2026-07-20):**
- Impressions: **3,060** → **verdict: 🟡 (+3.7% in a day — mid-band and slowing; the ~46% comment ratio did NOT trigger a second reach wave)**
- Reactions: 39; Comments: 18; Reposts: 0
- Comments/reactions ratio: ~46% (engagement frozen exactly where it was at 3d — zero new reactions or comments in 24h)
**Metrics (~6d refresh, 2026-07-22):**
- Impressions: **3,272** → **verdict: 🟡 (+6.9% over the ~4d capture — mid-band, will lock 🟡 tomorrow)**
- Reactions: 39; Comments: 18; Reposts: 0
- Comments/reactions ratio: ~46% (engagement now frozen at 39/18 for **three straight days** while impressions kept creeping — decisive evidence that comment depth ≠ distribution)
**Metrics (7d FINAL, locked 2026-07-23):**
- Impressions: **3,286** → **verdict: 🟡 FINAL (+0.4% over the ~6d capture — reach fully plateaued; lands mid-🟡, just above the n=32 median of 3,255)**
- Reactions: 39; Comments: 18; Reposts: 0
- Engagement rate: ~1.7%
- Comments/reactions ratio: ~46% (frozen at 39/18 for **four straight days** — final confirmation)
**Analysis:** Wellness/discipline post that DOES carry the founder-bridge the rule requires — the gym-excuse scene resolves into a business-excuse triplet and a portable principle, so it avoids the "Treat yourself like a product" 518-bomb trap. On-brand for the focus pillar and the "discipline over story" mindset; confession hook is clean (under 10 words, no number but a real confession anchor), no forbidden templates, no self-flex. Reach is mid-band (2,952 @ 3d) but the comment ratio is the highest of any in-flight post (~46%), which sometimes precedes a second reach wave. Personal-scene-to-principle is a reliable 🟡 lane for Lior, not a ⭐ lane. **7d FINAL LOCKED 3,286 🟡** — and the ~46% comment ratio never converted into reach at any point across four days of frozen engagement, so the negative result is now closed and confirmed: **comment depth is an audience-warmth signal, not a distribution one.** The personal-scene→business-parallel lane is a dependable 3.0–3.5K 🟡 producer for Lior; it does not reach the ✅ floor and should not be scheduled when a 5K-band slot is needed.

**Post-FINAL long-tail (2026-08-02 scan, ~17d):** 3,361 imp (41 react / 18 comm / 0 reposts / 2 saves) — +2.3% residual past the 3,286 🟡 7d FINAL locked 2026-07-23. 🟡 holds; no change to the locked value.

---

### 2026-07-20 — "Messi walks 83% of the match / the lazy method" (sports-observation → founder-focus parallel) ⭐ (7d FINAL: 10,771 imp — BREAKOUT, 6th-highest in the log)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7484962760804483072
**Topic tag:** #focus #delegation #messi #worldcup #founderlesson #newsjack
**Hook type:** Cultural-moment observation with a named entity ("Watched the World Cup final live yesterday, and one thing kept me busy:") → the anchor lands in line 3 ("Messi was barely running.") — under 10 words, globally-topical entity, curiosity gap
**Structure:** Live cultural moment (World Cup final, watched in person) → the observation that nagged (Messi barely running) → humility disclaimer ("I'm not a football expert") → the researched stat (walks 83% of the match) → instant transfer ("Business feels exactly like this") → founder past (ran sprints, no sleep, chased everything) → the named principle ("the lazy method": pick where to attack, delegate, leave ego out) → aphorism pair ("Busy players run more. Great players run right.") → open question CTA ("Which balls are you still chasing?")
**Visual:** Image ×2 (personal artifact family — at the match)
**Length:** ~160 words
**CTA:** Open question ("Which balls are you still chasing?") — engagement gap left wide open
**Full post text:**
> Watched the World Cup final live yesterday, and one thing kept me busy:
> Messi was barely running.
> I'm not a football expert, but it bothered me enough to go digging after the game.
> Apparently, Messi walks 83% of the match.
> It clicked instantly.
> Business feels exactly like this.
> Early in my founder years, I ran sprints.
> No sleep, chasing everything at once.
> Until I developed the lazy method:
> Pick where to attack, delegate, and leave ego out of it.
> Success showed up when the effort relaxed.
> Not every ball deserves a chase.
> Busy players run more.
> Great players run right.
> Which balls are you still chasing?

**Metrics (first capture 2026-07-22, ~2d):**
- Impressions: **10,299** → **verdict: ⭐ (in-flight; ~3x the July batch ceiling and the highest reach since Tough-days 14,798 on 2026-05-28)**
- Reactions: 87; Comments: 27; Reposts: 0
- Engagement rate: ~1.1% (reach-led, exactly the ⭐-lane signature — distribution far outrunning first-degree engagement)
**Metrics (72h / 3d checkpoint, locked 2026-07-23):**
- Impressions: **10,395** → **verdict: ⭐ (in-flight; +0.9% over the 2d capture — the climb has essentially stopped, so this is a fast-burst breakout that front-loaded nearly all its reach in the first 48h, not a long-tail climber)**
- Reactions: 91; Comments: 27; Reposts: 0
- Engagement rate: ~1.1% (unchanged)
**Analysis:** First genuine breakout in ~8 weeks, and it arrives from a **new lane: cultural-moment newsjack with zero AI content**. The DNA rhymes with the confirmed ⭐ lane rather than the July 🟡 band — a globally-trending anchor (World Cup final, watched live) in the first 7 words, a counter-intuitive number (83%) doing the argument's work, and a contrarian thesis that IS the body rather than a bolted-on CTA. That is the exact structural inverse of the AI-model dead-end (Grok 1,347, Fable5-beach 1,222), and it confirms the anchor does not need to be AI: it needs to be trending, and the thesis needs to carry the body. Also fully on-brand for the focus pillar, and "the lazy method" is a genuine Lior coinage delivered as joy, not superiority. Reach-led with 0 reposts at 2d, so the ceiling is being set by algorithmic distribution, not sharing. Watch closely — if this holds its climb it is the first non-AI ⭐ since the Birthday post. **3d update: it did NOT keep climbing — 10,299 → 10,395 (+0.9%) in a full day.** The reach was delivered in one burst inside 48h and then cut off, which mirrors the Birthday post's "reach-caps after 24h" behavior rather than the Anthropic/Google long-tail. Practical read: the cultural-moment newsjack lane buys a large, fast, algorithmically-distributed audience, but the ceiling is set on day one — so the newsjack has to ship while the moment is still live, and nothing in the post's later life will rescue a slow start. Barring a surprise this locks around 10.5K, which would make it the **6th-highest final in the log (n=32)** and the highest since Tough-days. 7d FINAL due 2026-07-27.
⚠️ Style note for the digest: the aphorism pair "Busy players run more. Great players run right." is very close to the banned "not X, it's Y" contrast template. It worked here, but flag it — the agency is drifting toward the template the rules kill.

**Metrics (7d FINAL — LOCKED 2026-08-02 scan, post-window capture at ~13d; the 07-27 slot was missed during the 07-27→08-01 scan outage):**
- Impressions: **10,771** → **verdict: ⭐ (7d FINAL; +1.3% over the 10,632 @ 6d capture — the fast-burst read holds all the way out)**
- Reactions: 93; Comments: 27; Reposts: 0; Saves: 5; Sends: 1
- Members reached: 7,173 · **in-network 21% / out-of-network 79%** · 63 profile viewers · 3 followers gained
- Engagement rate: ~1.2% (reach-led ⭐ signature)
**FINAL analysis:** Locks as the **6th-highest final in the log** and the highest since Tough-days (14,798, 2026-05-28). Everything the 3d/4d/6d captures predicted held: ~96% of the reach landed inside the first 48h and the remaining 11 days added ~470 impressions. The out-of-network split (79%) is the mechanical proof of what makes this lane different — every 🔴/🟡 post in the July batch was first-degree-capped, this one was carried by strangers. **Confirmed rule for the cultural-moment newsjack lane:** a globally-trending anchor in the first 7 words + a counter-intuitive number carrying the argument + the thesis as the body buys algorithmic distribution *on day one only*. Ship while the moment is live; there is no recovery path afterwards. Note for the digest: at n=36 the top-10% threshold is now 18,009, so 10,771 is a strong ⭐ but no longer a top-10% post.

---

### 2026-07-21 — "AutoDS is on Anthropic's official connectors list" (product-launch / founder-origin callback) 🟡 (7d FINAL: 2,811 imp — highest product-launch post logged)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7485340364334063618
**Topic tag:** #anthropic #claude #autods #productlaunch #founderorigin #ai
**Hook type:** Announcement with a named entity ("I can finally share this: AutoDS is on Anthropic's official connectors list.") — named AI entity, but the payload is a product milestone, not a thesis
**Structure:** Announcement → 3-line capability list (find winning products / fix listing issues / go live) → origin-story callback (eBay blocked the main account 10 yrs ago, 100 accounts by hand) → "I had to build software" → that software became AutoDS → decade + 1.8M people scale line → "Now, it jumped a level" → close ("AutoDS is inside Claude.")
**Visual:** Image ×2
**Length:** ~110 words
**CTA:** None
**Full post text:**
> I can finally share this: AutoDS is on Anthropic's official connectors list.
> One click, and you run your store by chatting:
> - Find winning products.
> - Fix listing issues.
> - Go live.
> Ten years ago, eBay blocked my main account, and I was suddenly running 100 new ones by hand.
> I had to build software to automate the work.
> That software became AutoDS.
> We spent a decade automating the grind of e-commerce and helped 1.8 million people make money online.
> Now, it jumped a level.
> AutoDS is inside Claude.

**Metrics (24h checkpoint, 2026-07-22, ~1d):**
- Impressions: **2,008** → **verdict: 🔴/🟡 (in-flight; soft 24h start, tracking the product-launch lane)**
- Reactions: 68; Comments: 18; Reposts: 2
- Engagement rate: ~4.4% (high rate on low reach — the first-degree-only signature again)
**Metrics (~2d refresh, 2026-07-23):**
- Impressions: **2,279** → **verdict: 🔴/🟡 (in-flight; +13.5% over 24h — still climbing, but from a soft base and tracking straight at the ~2K product-launch cap)**
- Reactions: 73; Comments: 18; Reposts: 2
- Engagement rate: ~4.1% (reactions +5, comments and reposts frozen — the warmth is first-degree and already spent)
**Metrics (07-26 refresh, ~5d):**
- Impressions: **2,530** → **verdict: 🟡 (5d; +5.2% over the 3d capture, just cleared the 2,500 🟡 floor — the highest a pure product-launch post has reached in the log, edging past its ~2K cap)**
- Reactions: 76; Comments: 18; Reposts: 2; Saves: 3
- Engagement rate: ~3.8% (reactions +3 over 2 days, comments/reposts frozen — first-degree warmth long since spent, the small reach creep is slow algorithmic tail)
**Analysis:** Product-launch lane, which has a consistent record: "AutoDS now talks to Claude" (2026-06-10) opened at 1,633 and the launch frame reliably caps around 2K. This version is meaningfully better written — the eBay-ban origin callback gives it a real founder scene and keeps it from reading as pure product marketing — but the hook is still an announcement, and the named AI entity (Anthropic/Claude) is a badge rather than a thesis, which is precisely the pattern that bombs. High engagement rate with 2 reposts at 24h says his existing audience is genuinely happy for him; it does not predict reach. ⚠️ Brand-rule tension: this is the closest the feed comes to AutoDS product marketing, which the personal-brand rules push against — the origin story is what rescues it. 7d FINAL due 2026-07-28.

**Metrics (7d FINAL — LOCKED 2026-08-02 scan, post-window capture at ~12d; the 07-28 slot was missed during the scan outage):**
- Impressions: **2,811** → **verdict: 🟡 (7d FINAL; +11.1% over the 2,530 @ 5d capture — the tail kept creeping past the checkpoint)**
- Reactions: 77; Comments: 18; Reposts: 2; Saves: 3
- Engagement rate: ~3.6% (comments and reposts frozen since 24h; all late movement is reach, not warmth)
**FINAL analysis:** **The highest a pure product-launch post has ever reached in this log**, clearing the lane's ~2K ceiling ("AutoDS now talks to Claude" 1,633 🔴, 2026-06-10) by ~72%. The differentiator is the eBay-ban origin callback — the same announcement wrapped in a founder scene moves from 🔴 to the middle of the 🟡 band. It still never threatened the 5K ✅ floor, so the rule stands: **a product launch can be rescued into 🟡 by a real origin scene, but the launch frame itself caps the lane.** Do not spend a reach slot on it.

---

### 2026-07-22 — "Here's what I learned from the most senior people at Shopify / make other people rich" (conference-recap with operator numbers) 🟡 (7d FINAL: 3,777 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7485693548781162496
**Topic tag:** #shopify #dotdev #toronto #partnership #ecosystem #conferencerecap
**Hook type:** Insider-intel promise with a named entity ("Here's what I learned from the most senior people at Shopify:") — named giant, insider framing, under 10 words
**Structure:** Insider hook → thesis stated immediately ("Make other people rich") → authority stack from the stage (1.3B shared with partners, 100,000 new builders, 68 countries / 6.5-yr average tenure, 7:1 developer-to-Shopify dollar ratio) → "so what's their secret?" → operator standing declared (#1 affiliate and partner 2 years running) → the win-win mechanic → the ambassador flywheel → quotable principle ("Your best salespeople are the people you made rich") → AI-era durability line → warm close
**Visual:** Image (+1 — event/stage, personal artifact family)
**Length:** ~200 words
**CTA:** None (closes on a principle)
**Full post text:**
> Here's what I learned from the most senior people at Shopify:
> And that's the best business advice I can give in 2026.
> Make other people rich.
> It built Shopify into an empire.
> I'm at their developer conference in Toronto, and the numbers on stage are hard to process:
> - $1.3 billion shared with partners last year.
> - 100,000 new people building apps and themes.
> - Developers from 68 countries, staying 6.5 years on average.
> - For every dollar Shopify makes, its developers make 7.
> So what's their secret?
> We've been their #1 affiliate and partner for 2 years in a row, so I'll tell you this:
> Shopify found the win-win that most platforms never look for.
> Partners get total freedom to build real businesses, fast, and Shopify earns the trust of an entire industry.
> And the smartest part:
> Every developer who succeeds there becomes an ambassador, selling Shopify.
> That's what Shopify knows that others don't:
> Your best salespeople are the people you made rich.
> In an era where AI eats companies every week, Shopify is here to stay.
> And it feels so good to grow alongside a partner like that (:

**Metrics (first capture 2026-07-22, ~1h):**
- Impressions: **319** → (too early for a verdict; 24h checkpoint due 2026-07-23)
- Reactions: 22; Comments: 4; Reposts: 0
**Metrics (24h checkpoint, locked 2026-07-23):**
- Impressions: **2,488** → **verdict: 🔴/🟡 (24h; below the 2,500 🟡 floor at the checkpoint — a soft start for a post this well built)**
- Reactions: 68; Comments: 23; Reposts: 0
- Engagement rate: ~3.7% (comments/reactions ~34%, the deepest of the current in-flight set)
**Analysis:** This is the **post-event operator-scene version of the conference lane** that the DotDev-announcement failure (1,784 🔴) said was the only way the lane can work — the direct A/B test, same conference, same week. It brings what the announcement lacked: hard numbers from the stage, a stated thesis in line 3, real operator standing ("#1 affiliate and partner for 2 years"), and a quotable principle instead of a "come say hi." It also correctly uses "affiliate and partner" per the 2026-07-22 rule, and never criticizes Shopify. Structurally it is the closest post in weeks to the insider-intel + operator-confession + strategic-close pattern that produced the 93K MD→HTML winner. Risks: no engagement gap at the end (closes fully resolved, and the rules say a closed ending suppresses comments), and the opening two lines are inverted — "And that's the best business advice I can give in 2026" lands before the advice itself, which reads as a sequencing error. 24h checkpoint 2026-07-23; 7d FINAL due 2026-07-29.
**07-26 refresh (~4d):** **3,480 imp 🟡** (90 react / 23 comm / 0 reposts / 3 saves), +10.5% over the ~2d capture (3,150) — the healthiest reach-climb of the three DotDev posts and now clearly the best of the conference lane, but still capped in the 🟡 band exactly where the lane's topic-ceiling read predicts. Note the divergence from its lane-mates: this recap version keeps creeping (2,488 → 3,150 → 3,480) while the coffee-truck stalled, so the *execution* gap (stage numbers + stated thesis) buys a few hundred extra impressions inside the band — but not a band change. Consistent with "topic is the ceiling, craft moves you within the band, not out of it." 7d FINAL due 07-29.
**24h read (2026-07-23):** 2,488 at the checkpoint, which is **below** the 2,500 🟡 floor and slightly under the DotDev-announcement's own trajectory-adjusted pace. The A/B test is therefore leaning the wrong way so far: the far better-built conference post is not out-reaching the weak one by much, which suggests **the conference topic itself is the reach ceiling, not the execution** — Lior's audience does not travel with him to a partner's developer event, however good the operator numbers are. Engagement tells the opposite story (68 reactions / 23 comments in 24h is the warmest first-degree response of the current set, ~34% comment ratio), and by the now-confirmed rule that engagement depth is warmth rather than distribution, that warmth will not convert. Provisional call: this lane is capped in the 2–3.5K band regardless of craft, and conference content should be treated as relationship maintenance, not reach. Confirm or overturn at the 7d lock on 07-29.

**Metrics (7d FINAL — LOCKED 2026-08-02 scan, post-window capture at ~11d; the 07-29 slot was missed during the scan outage):**
- Impressions: **3,777** → **verdict: 🟡 (7d FINAL; +8.5% over the 3,480 @ 4d capture — best-reaching of the three DotDev posts, exactly as the craft-ordering predicted)**
- Reactions: 93; Comments: 30; Reposts: 0
- Engagement rate: ~3.3% (30 comments is the deepest comment count of the whole DotDev run)
**FINAL analysis:** Confirms the 07-26 finding in full. Within the conference topic the three posts ordered **by craft** — learnings-recap **3,777** > coffee-truck **2,562** > announcement **1,784** — and none of them came near the 5K ✅ floor. **Topic set the ceiling, execution set the rank underneath it.** This was the best-built conference post in the log (hard stage numbers, a stated thesis, real operator standing, the warmest engagement of the set) and it still finished mid-🟡. The digest recommendation stands: retire the conference lane as a reach slot and treat it as relationship maintenance.

---

### 2026-07-23 — "How do we sponsor the Shopify conference that sells no sponsorships? / guerrilla marketing coffee truck" (operator war-story / rule-bending scene) 🟡 (7d FINAL: 2,562 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7486059544305930240
**Topic tag:** #shopify #dotdev #toronto #guerrillamarketing #operatorstory #autods
**Hook type:** Question hook naming a giant with a built-in paradox ("How do we sponsor the Shopify conference that sells no sponsorships?") — 12 words, named entity in the first 6, and the paradox IS the curiosity gap
**Structure:** Paradox question hook → claim ("a masterclass in guerrilla marketing") → "Here's the story:" → the constraint (no sponsor packages, no logos but Shopify's) → the move (branded coffee truck outside the entrance) → escalating timestamps (9 AM line / 10 AM half the conference carrying AutoDS cups / noon security shuts it down) → sportsmanship beat ("We knew the rules. Fair play.") → the escalation (next morning, two stands in two spots + a photographer giving free LinkedIn headshots) → comedic button ("People loved it. Security… not so much.") → quotable principle ("You can rent a booth. You can't buy buzz.")
**Visual:** Image ×2 (personal artifact family — WhatsApp screenshot of the truck being shut down + event photo)
**Length:** ~170 words
**CTA:** None (closes on the principle)
**Full post text:**
> How do we sponsor the Shopify conference that sells no sponsorships?
> We just gave a masterclass in guerrilla marketing.
> Here's the story:
> Shopify's biggest annual event.
> No sponsor packages, no logos except Shopify's.
> So we parked an AutoDS-branded coffee truck right outside the entrance.
> By 9 AM there was a line.
> By 10 AM, half the conference was walking the halls with AutoDS printed on their coffee cups.
> By noon, security came over and shut us down.
> We knew the rules.
> Fair play, they were doing their job.
> So the next morning, we took it further-
> We came back with two coffee stands in two new spots, plus a photographer offering free LinkedIn headshots to everyone in line.
> People loved it.
> Security… not so much.
> You can rent a booth. You can't buy buzz.

**Metrics (first capture 2026-07-23, ~27m):**
- Impressions: **140** → (far too early for a verdict; 24h checkpoint due 2026-07-24)
- Reactions: 8; Comments: 2; Reposts: 0
**Metrics (24h checkpoint, locked 2026-07-24):**
- Impressions: **2,114** → **verdict: 🔴 (24h; below the 2,500 🟡 floor — and, decisively, BELOW the DotDev-learnings 24h of 2,488 and roughly at the announcement's own pace)**
- Reactions: 43; Comments: 11; Reposts: 0
**24h read (2026-07-24):** This is the clean answer to the test the 07-23 scan set up — *does format beat topic in the conference lane?* At the 24h checkpoint the answer is **no**: the best-built of the three DotDev posts (a real scene, escalation, a security antagonist, a quotable button) opened **lower** than the recap version (2,114 vs 2,488) and only marginally above the flat announcement. All three conference posts are now clustered in the same 1.7K–2.5K band at their equivalent checkpoints regardless of craft, which is strong evidence that **topic is the ceiling, not execution** — Lior's audience does not travel with him to a partner's developer event however good the operator story. Engagement is again the warm-but-non-converting signature of the lane (43 react / 11 comm in 24h). Provisional call stands: conference content is relationship maintenance, not reach, and should not occupy slots that need to clear 5K. Confirm at the 7d lock 2026-07-30. Format did not beat topic.
**Analysis:** Third Shopify-DotDev post in ten days, and structurally the strongest of the three. Unlike the announcement (1,784 🔴) and the learnings recap (2,488 @ 24h), this one is **a scene with escalating action and a protagonist taking risk** — timestamps do the pacing, security is a real antagonist, and the payoff is a genuinely quotable principle. It is the closest the feed has come to the operator war-story format, and it carries the CEO-relevance filter easily: a founder describing how his own team out-flanked a closed sponsorship model is exactly what a SaaS CEO can credibly tell. On-brand for the 0→1 pillar and delivered as joy rather than superiority; Shopify is never criticized, and the "we knew the rules, fair play" beat is what keeps a rule-bending story from reading as arrogance. ⚠️ Two watch items: (1) it is the third post in a row anchored on the same conference, and the lane's own 24h data says the topic caps reach around 2–3.5K no matter the craft, so this becomes the cleanest possible test of whether **format can beat topic** — if a true war-story clears 3.5K where the recap and the announcement did not, execution wins and the conference lane is salvageable; if it lands in the same band, topic is the ceiling and the digest should recommend ending the DotDev run; (2) the closing principle "You can rent a booth. You can't buy buzz." is again in the family of the banned "not X, it's Y" contrast template, the **second** instance in four days after the Messi post's "Busy players run more. Great players run right." — the agency's drift toward that template is now a pattern, not a one-off, and belongs in the Monday digest. 24h checkpoint due 2026-07-24; 7d FINAL due 2026-07-30.
**07-26 refresh (~3d):** **2,315 imp 🔴** (46 react / 23 comm / 0 reposts / 2 saves), +9.5% over the 24h capture (2,114) — still below the 2,500 🟡 floor at 3d, and below both lane-mates at equivalent ages. Comments doubled 11 → 23 (now tied with the recap for the set's deepest comment count) while reach stayed capped — another clean instance of the confirmed rule that comment depth is audience warmth, not distribution. The "format beats topic" test is now decisively answered NO at 3d: the best-built conference post is the lowest-reaching of the three. Barring a surprise this locks 🔴 in the low-2.4Ks. 7d FINAL due 07-30.

**Metrics (7d FINAL — LOCKED 2026-08-02 scan, post-window capture at ~10d; the 07-30 slot was missed during the scan outage):**
- Impressions: **2,562** → **verdict: 🟡 (7d FINAL; +10.7% over the 2,315 @ 3d capture — cleared the 2,500 🟡 floor at the tail, but only just)**
- Reactions: 49; Comments: 23; Reposts: 0
- Engagement rate: ~2.8%
**FINAL analysis:** The **"format beats topic" test is now settled: it does not.** This was the only DotDev post with a real scene, an escalation and an antagonist (security shutting the truck down twice), the exact ingredients that carry the ⭐ lanes, and it finished **1,215 impressions below** the flat learnings-recap and 3.5x below a cultural-moment post from the same week. Craft moved it from 🔴 to the bottom of 🟡 and no further. ⚠️ Its closing line "You can rent a booth. You can't buy buzz." is the second instance of the banned "not X, it's Y" contrast drift and it bought nothing — worth citing to the agency now that the number is in.

---

### 2026-07-24 — QUOTE-REPOST of Ronen Anaby's DotDev recap ("Proud of our amazing team … 10/10 goals achieved") (reshare-with-commentary — NEW post type) (final 1,208 imp, unscored)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7486446776070344706/
**Reshared source:** Ronen Anaby (Senior Marketing Operations Manager at AutoDS), urn:li:activity:7486260984425295872 — "What I learned from Shopify DotDev 2026 / I learned that I'm working in the right company"
**Topic tag:** #shopify #dotdev #team #reshare #autods
**Hook type:** N/A (reshare) — Lior's own commentary opens "Proud of our amazing team, who went to an event and came back with 10/10 goals achieved."
**Structure:** Quote-repost — short first-person team-pride commentary on top of a teammate's warm recap that name-checks the founders (CMO friendliness, CTO Shopify-ecosystem depth, CEO's measurable-goals leadership). This is the **first reshare/quote-repost in the entire log** — a distinct format from Lior's authored posts.
**Visual:** Inherited from the reshared post (Ronen's event image)
**Length:** ~30 words of own commentary
**CTA:** None
**Full commentary text (Lior's):**
> Proud of our amazing team, who went to an event and came back with 10/10 goals achieved.
>
> So happy to keep building, innovating, and always pushing forward.
> Love this life, love the building.

**Metrics (first capture 2026-07-24, ~5h):**
- Impressions: **500** → (far too early for a verdict; reshares typically under-reach authored posts)
- Reactions: 30; Comments: 4; Reposts: 0
**Analysis:** First quote-repost in the log, so no in-format benchmark exists yet — but the 5h pace (500 imp) is slow, consistent with LinkedIn suppressing reshare distribution vs original authorship. On brand it is clean: "Love this life, love the building" is a direct echo of the **[ life is beta ]** tagline and the 0→1/joy pillar, and the underlying recap positions the founders as respected operators without Lior having to say it himself (the teammate does the crediting) — a genuinely low-risk way to bank credibility. ⚠️ But it is the **4th straight DotDev/Shopify-anchored item in five days** (coffee-truck 07-23, learnings 07-22, this reshare 07-24, plus the 07-14 announcement), during the exact week the log's only breakout came from an *unrelated* cultural moment (Messi). The topic-concentration risk flagged on 07-23 has intensified, not eased. Because reshares don't fit the authored-post scoring model, treat this as a soft credibility/relationship post, not a reach slot; no 7d verdict scoring planned unless it behaves unusually. Track once more, then let it age off.
**07-26 refresh (~2d):** 872 imp (38 react / 5 comm / 0 reposts), up from 500 @ 5h — under-reaches every authored post in the window by 2.6x+ (vs the reshare's underlying source doing its own reach), confirming LinkedIn suppresses reshare distribution as expected. Nothing unusual; aging off, no further scoring.

**Final capture (2026-08-02 scan, ~9d — reshare, not scored against the authored baseline):** **1,208 imp** (44 react / 5 comm / 0 reposts). Aged off. For the record the quote-repost finished **2.2x below** the median authored post of the same week and below every authored post in the 07-20→08-01 window except the 07-31 anniversary republish. Reshare suppression confirmed at full term; the format is a credibility gesture, never a reach slot.

---

### 2026-07-28 — "In 2026, building a product has never been easier" (AI-era moat thesis / build-is-now-free) 🔴 (7d FINAL: 2,402 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7487499827619143681
**Topic tag:** #ai #moat #reviews #distribution #buildvsbrand #contrarian
**Hook type:** Trend-state opener ("In 2026, building a product has never been easier.") — a year anchor, but no named entity, no number, and no confession; the concrete anchor never arrives
**Structure:** Trend statement → the two-day AI build → "everyone is racing to build" → the thesis (AI cannot build the reason someone picks you, and cannot generate the reviews tens of thousands read) → "that asset takes years, none of it can be prompted" → closing inversion ("Building was the hard part. Now it's the free part.") → a warning close aimed at the reader
**Visual:** Image ×1
**Length:** ~130 words
**CTA:** None (closes on a warning, no question)
**Full post text:**
> In 2026, building a product has never been easier.
> An AI agent will build your app in two days, something that used to take years.
> Now everyone is racing to build, and most of them are missing the actual problem.
> AI can build the product.
> But it cannot build the reason anyone picks your product out of the thousand identical ones launching this weekend.
> And it does not generate the reviews that tens of thousands of people a month read before signing up.
> That asset takes years to build, and none of it can be prompted.
> Building was the hard part.
> Now it's the free part.
> If you're spending all your energy there, you're competing on the one thing that no longer separates anyone.

**Metrics (first capture 2026-08-02, ~5d):**
- Impressions: **2,207** → **verdict: 🔴 (5d; under the 2,500 🟡 floor with two days left and the AI-lane tail historically flat — will almost certainly lock 🔴)**
- Reactions: 37; Comments: 18; Reposts: 0
- Engagement rate: ~2.5% (18 comments on 2,207 impressions is a healthy comment ratio on thin reach — the first-degree signature again)
**Analysis:** This is the **closest the agency has come to a real contrarian-AI thesis since the mega-winners**, and it still under-reached, which is informative. The DNA that made Anthropic (92,959) and Google/Base44 (146,506) travel was a **named trending entity in the first 7 words**; here the argument is right but the anchor is a calendar year. No named tool, no number, no scene, and the proof point that would have carried it — AutoDS's own review moat, tens of thousands of readers a month — is stated abstractly instead of with the actual figure. **Refines the AI-lane rule rather than breaking it: a contrarian thesis is necessary but not sufficient; the lane needs a named, currently-trending anchor to get out of network.** 7d FINAL due 2026-08-04.
**08-03 refresh (~6d, impressions UNAVAILABLE — Chrome signed out, Creator Analytics unreachable):** public counts 37 react / 19 comm (+1 comment in 24h, reactions flat). Engagement has stopped moving one day before the 7d lock, which is the tail shape that keeps this under the 2,500 🟡 floor; 🔴 still the expected FINAL. 7d FINAL due TOMORROW 2026-08-04 — needs a logged-in Chrome to lock with a real impressions number.

**★ 7d FINAL LOCKED 2026-08-04: 2,402 impressions 🔴** (37 react / 19 comm / 0 reposts / engagement frozen — reactions have not moved in 48h, comments +0). Finished **98 impressions under the 2,500 🟡 floor** after a +8.8% tail off the 5d capture, so the 🔴 call made on 08-02 holds. Sits at position 14 of 37 in the final-locked array, **26% below the log median (3,224)**.
**FINAL analysis:** The most instructive 🔴 in the log, because the *thesis* was right and the *anchor* was not. Both mega-winners in this lane opened on a named, currently-trending entity inside the first 7 words (Anthropic → 92,959; Google/Base44 → 146,506); this one opened on a calendar year. Same lane, same contrarian frame, ~40x less reach. **Rule now confirmed at n=3 in both directions and promoted from hypothesis to hard rule: in the AI lane, a contrarian thesis is necessary but not sufficient — the post must name a trending entity in the hook or it caps in the low 2Ks.** Second confirmed miss: the strongest proof available was AutoDS's own review moat ("tens of thousands of people a month"), which the post states abstractly rather than as the actual figure. The lane's winners all carry one hard number in the body. ⚠️ Hard-rule violation logged at FINAL: "Building was the hard part. Now it's the free part." is the banned "not X, it's Y" contrast template in the closing slot (instance 4 of the drift documented across 07-20 → 07-29).

---

### 2026-07-29 — "We shut down one of our companies last month. And I'm happy about it." (kill-a-profitable-business / focus) 🟡 (7d FINAL: 3,494 imp — true publish 2026-07-28)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7487861977659133952
**Topic tag:** #focus #shutdown #hardcalls #operatordecision #founderlesson
**Hook type:** Confession + reversal in 13 words ("We shut down one of our companies last month. And I'm happy about it.") — concrete action, counter-intuitive emotion, no ego-"I" opener
**Structure:** Confession hook → the twist that raises the stakes (it was profitable) → the honest discomfort ("that's the part that feels strange") → the contrast that names the real test (losing money is easy math / still making money is the decision that tests you) → the mechanism (it quietly eats the focus your main bet needs) → the resolution (closed it, moved the energy back, slept fine) → the principle ("Focus is the only real edge") → open question CTA ("Have you ever killed something that was working?")
**Visual:** Image ×2 — **a redacted Israel Registrar of Companies dissolution letter dated 28/06/2026** (personal artifact family, the strongest visual of the batch: documentary proof rather than a stock graphic)
**Length:** ~120 words
**CTA:** Open question — engagement gap left open
**Full post text:**
> We shut down one of our companies last month.
> And I'm happy about it.
> This one was profitable.
> But it just never reached the scale we built it for.
> That's the part that feels strange.
> Closing a business that loses money is easy math.
> Closing one that still makes money is the decision that actually tests you-
> Every month you keep it, it quietly eats the focus your main bet needs.
> So we closed it, moved that energy back to the core, and slept fine.
> It doesn't shake me.
> Focus is the only real edge.
> Have you ever killed something that was working?

**Metrics (first capture 2026-08-02, ~4d):**
- Impressions: **3,350** → **verdict: 🟡 (4d; top of the batch, mid-🟡 band, still climbing)**
- Reactions: 27; Comments: 14; Reposts: 0; Saves: 3
- 22 profile viewers from this post; 0 followers gained
- Engagement rate: ~1.3% (**the lowest reaction count of the batch on the highest reach — the only post in the window whose distribution outran its first-degree warmth**)
**Analysis:** **The strongest post of the week on every craft axis and the only one behaving like a reach post rather than a friends-and-family post.** It hits the focus pillar dead-on, the vulnerability is a real past decision rather than anticipatory fear, the hook is a confession with a reversal inside 13 words, the visual is documentary proof, and the ending leaves the engagement gap open — the full Top-12 playbook, executed. Notably it has the *worst* reactions-per-impression of the batch, which by the rule this log confirmed on 07-22 is a good sign: warmth does not predict distribution, and this is the only post of the five that strangers saw. ⚠️ One hard-rule miss: "Closing a business that loses money is easy math. Closing one that still makes money is the decision that actually tests you" is a **third instance of the "not X, it's Y" contrast drift** in two weeks — the template keeps landing in the pivot slot. 7d FINAL due 2026-08-05; on this trajectory it should lock in the upper 🟡 band (~3.6–3.9K), and if it clears 5K it opens a genuine **hard-operator-decision** ✅ lane.
**08-03 refresh (~5d, impressions UNAVAILABLE — Chrome signed out):** public counts 28 react / 14 comm (+1 reaction, comments flat). Still the *lowest* reaction count of the five in-flight posts, which on this log's confirmed rule is the reach-post signature rather than a weakness. Upper-🟡 call unchanged; 7d FINAL due 2026-08-05.
**08-04 refresh (6d): 3,464 imp 🟡** (29 react / 14 comm / 0 reposts) — +3.4% over the 4d capture, climb flattening as expected. **Confirmed the best post of the 07-28→08-01 batch by a wide margin: 44% above the batch's second-best (07-30 at 2,324) and the only one of the six above the log median.** Reaction count is still the lowest of every post in the window on the highest reach, which is the reach-post signature this log confirmed on 07-22. Locks tomorrow (7d FINAL 2026-08-05) at ~3.5K — solid mid-🟡, short of the 5K ✅ floor that would have opened a hard-operator-decision ✅ lane. The lane is real but reach-limited; treat it as a reliable 🟡 producer, not a breakout slot.
**★ 7d FINAL LOCKED 2026-08-05: 3,494 impressions 🟡** (29 reactions / 14 comments / 0 reposts / engagement rate ~1.2%). ⚠️ Date correction: the URN decodes to **2026-07-28 13:30 UTC**, so this post turned 7d on 08-04 and locks here at 7.7d; the +30 impressions between the 08-04 refresh (3,464) and today confirm distribution is finished. **Final call: mid-🟡, 7% above the n=38 log median (3,255), and the best post of the 07-28 → 08-04 block by 47% over the second-best.** It is also the only post in that eight-day window above the median. What the lock settles: **the hard-operator-decision lane is a reliable 🟡 producer with a ceiling around 3.5K, not a ✅ lane.** Executing the full Top-12 playbook — 13-word confession hook with a reversal, documentary personal artifact (the dissolution letter), focus pillar, open-question close — bought a solid mid-🟡 and nothing more, which is the cleanest available evidence that on this account craft sets the floor and topic sets the ceiling. Reactions-per-impression stayed the lowest of every post in the window (1.2%), the reach-post signature this log confirmed on 07-22, so the distribution it did get came from strangers rather than from his own network. **Rule to carry forward: keep the shutdown/kill-a-profitable-business lane in the rotation as a dependable median-beater, but never schedule it into a slot that needs a breakout.**

---

### 2026-07-30 — "At 21 … Me at 31" (then-vs-now credential list) 🔴 (7d FINAL: 2,393 imp — true publish 2026-07-29 13:30 UTC)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7488224531732393984
**Topic tag:** #thenvsnow #milestone #credential #founderjourney #listicle
**Hook type:** Bare time-stamp label ("At 21:") — two words, but the anchor is a bullet list rather than a scene or a number
**Structure:** "At 21" four-bullet before-state (terrified of public speaking / parents' apartment / 100 eBay accounts by hand / reinvesting everything) → "Me at 31" seven-bullet after-state (Fiverr exit, 250+ employees from 30+ countries, 1.8M+ dropshippers, 4 competitors acquired, loves public speaking, three more 0→1 products, snowboarding/diving/travel) → no close, no principle, no question
**Visual:** Image ×1
**Length:** ~85 words
**CTA:** None
**Full post text:**
> At 21:
> - Terrified of public speaking
> - Worked out of my parents' apartment
> - Manually managed 100 eBay accounts
> - Reinvesting everything back into what I was building
> Me at 31:
> - Sold AutoDS to Fiverr for MILLIONS
> - 250+ employees from 30+ countries
> - 1.8 million+ dropshippers use AutoDS
> - Acquired 4 competitors
> - Love public speaking
> - Building three more products from zero
> - Snowboarding, scuba diving, and traveling all over the world

**Metrics (first capture 2026-08-02, ~3d):**
- Impressions: **2,223** → **verdict: 🔴 (3d; under the 2,500 🟡 floor)**
- Reactions: 53; Comments: 16; Reposts: 0
- Engagement rate: ~3.1% (**highest reaction count of the batch on the second-lowest reach — a textbook first-degree-only post**)
**Analysis:** The credential-milestone lane produced the log's first non-AI ⭐ (Birthday "31 / 10 lessons", 18,009), so the raw ingredients work — but that post carried **10 written lessons given back to the reader**, and this one carries only the scoreboard. Strip the give-back and the format reads as a highlight reel, which his existing audience applauds (53 reactions, the batch high) and strangers never see. **Rule sharpened: the credential-milestone lane travels on what the milestone teaches, not on the milestone.** ⚠️ Brand-rule tension: "Sold AutoDS to Fiverr for MILLIONS" in caps is the closest the feed has come to flexing, which cuts against the never-arrogant rule and the "I live on 200 reads as joy, not superiority" pillar. ⚠️ Also the second of **three straight origin/exit-anniversary posts** (07-30, 07-31, 08-01) — see the topic-concentration flag below. 7d FINAL due 2026-08-06.
**08-03 refresh (~4d, impressions UNAVAILABLE — Chrome signed out):** public counts 54 react / 17 comm (+1 react, +1 comm). Holds the highest reaction count of the batch on the second-lowest reach — the first-degree-only signature is stable, not a slow burn. 7d FINAL due 2026-08-06.
**08-04 refresh (5d): 2,324 imp 🔴** (54 react / 17 comm / 0 reposts) — +4.5% over the 3d capture, and **engagement is now completely frozen** (react and comment counts identical to yesterday's capture). Distribution is done; the remaining two days will add a few dozen impressions at most, so this locks 🔴, roughly 150–200 short of the 🟡 floor. Still carries the batch's highest reaction count on the second-lowest reach — the textbook first-degree-only post, exactly as called at first capture. 7d FINAL due 2026-08-06.
**08-05 refresh (6d): 2,378 imp 🔴** (54 react / 17 comm / 0 reposts) — +54 impressions in 24h and engagement **still completely frozen** for a second straight day (react and comment counts identical to the 08-04 capture). ⚠️ Date correction: the URN decodes to **2026-07-29 13:30 UTC**, so the true 7d lock is **2026-08-06** (unchanged) and the post is at 6.7d now. It will lock ~2,400, roughly 100 short of the 🟡 floor. The reading is settled: highest reaction count in the window on the second-lowest reach, i.e. his own network applauded the scoreboard and no stranger ever saw it. **Rule stands: the credential-milestone lane travels on what the milestone teaches, never on the milestone itself.**

**★ 7d FINAL LOCKED 2026-08-06 (captured at 7.75d — the 7d mark, 2026-08-05 13:30 UTC, fell after yesterday's scan): 2,393 impressions 🔴.** 54 reactions / 17 comments / 0 reposts / 2 saves / 0 sends. 11 profile viewers, **0 followers gained.** Engagement rate ~3.0%. Final climb from the 6d capture was **+15 impressions**, with reactions and comments frozen for a third straight day — distribution ended days ago. Lands 107 short of the 🟡 floor, at position 15 of 40 in the final-locked array.
**Analysis (final):** Called correctly at first capture and never wavered: **the highest reaction count in its publishing window on the second-lowest reach.** His own network applauded the scoreboard; no stranger was served it. 0 followers gained on 2,393 impressions is the cleanest statement of what a highlight-reel post buys — nothing. **The rule is now confirmed, not provisional: the credential-milestone lane travels on what the milestone teaches, never on the milestone itself.** ⚠️ Compare directly with the 2026-08-05 post below, which uses the *same* credential anchor plus 7 given-back lessons and did **5,412 impressions in 17 hours** — a controlled A/B on the same account, seven days apart, that isolates the give-back as the active ingredient. See that entry and the 08-06 rolling-benchmarks block.

---

### 2026-07-31 — "2 year ago, I sold that business to Fiverr" / Advisors, Networking, Partners (REPUBLISH of the 200K+ 1-year anniversary post) 🔴 BOMB (7d FINAL: 806 imp — true publish 2026-07-30 13:25 UTC; 4th-worst post in the log)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7488585446252445696
**Topic tag:** #fiverr #anniversary #advisors #networking #partners #republish
**Hook type:** Milestone announcement ("2 year ago, I sold that business to Fiverr.") — the proven hook, carried over verbatim apart from the year swap
**Structure:** Identical to the 1-year anniversary post: milestone hook → origin reminder (living with parents, an idea and a laptop) → 3 numbered choices, each with a short story (1. Advisors 2. Networking 3. Partners, naming Michael Royf and Ofir Bokobza) → roller-coaster line → "Advisors, Networking, Partners — those will make or break your business" → "These are the real keys to success."
**Visual:** Image ×2 (Times Square / Nasdaq billboard artifact)
**Length:** ~430 words (by far the longest post of the batch, ~3.5x the 750–1,200 char guideline at the top end)
**CTA:** None (closes fully resolved — no engagement gap)
**Diff vs the proven original:** "Last year" → "2 year ago"; "7 years ago" → "8 years ago"; the closing directive triple (Hire the right advisors / Network relentlessly / Find the right partners) dropped. Otherwise the body is the same text.

**Metrics (first capture 2026-08-02, ~2d):**
- Impressions: **693** → **verdict: 🔴 BOMB (2d; the third-lowest number in the entire log, behind only Treat-yourself 518 and Master Prompt 546, and comfortably inside the bottom-10% band ≤1,175)**
- Reactions: 41; Comments: 12; Reposts: 1; Saves: 1
- 10 profile viewers; 0 followers gained
- Engagement rate: **~7.9% — the highest in the log by a wide margin**, and on 693 impressions that is the pure first-degree signature: almost nobody outside his own network was served this post
**Analysis:** **The single most valuable data point of this scan, because it is a controlled experiment nobody meant to run.** The 1-year version of this exact text did **200K+ impressions**; the 2-year republish did **693** — a ~300x collapse with the copy, the structure, the author and the account held constant. The only variables that changed are (a) the text is a near-duplicate of content LinkedIn has already distributed, (b) the closing directive triple was removed so the post now ends fully resolved with no engagement gap, and (c) it ran at ~430 words with no visual payoff carrying the length. **(a) is almost certainly the dominant term** — the engagement rate proves the audience still loves the material (7.9%, the log's best) while distribution refused to serve it at all, which is the fingerprint of duplicate-content suppression, not of a weak post. **Operational rule to add to the playbook: a proven post is a proven *template*, never a proven *text*. Reuse the spine — milestone hook, origin reminder, three numbered choices, a give-back close — and rewrite every sentence, with this year's numbers and at least one story the original did not contain.** ⚠️ This matters directly to a standing instruction: the 1-year post is saved in memory as *the* template to reuse for the 2-year anniversary, and the reuse has now been run and failed as a copy-paste. The memory entry needs the "rewrite, don't republish" caveat attached. 7d FINAL due 2026-08-07; on a flat first-degree tail this locks somewhere around 750–900.
**08-03 / 72h CHECKPOINT LOCKED (impressions UNAVAILABLE — Chrome signed out, Creator Analytics unreachable):** public counts **45 react / 12 comm** (+4 reactions, comments flat). Impressions could not be read, so the 72h checkpoint locks on engagement only and the impressions cell stays unavailable permanently for this checkpoint. **What the engagement alone still shows: this post added the most reactions of any in-flight post in the last 24h (+4) while sitting on the log's third-lowest reach — more of his own network keeps finding it and liking it, and distribution still will not carry it outward. That is the duplicate-content-suppression fingerprint getting *stronger*, not a recovery.** No change to the 🔴 BOMB call or to the "a proven post is a proven template, never a proven text" rule. 7d FINAL due 2026-08-07.
**08-04 refresh (4d): 778 imp 🔴 BOMB** (47 react / 12 comm / 1 repost) — the first real impressions number since the 2d capture, and it is **+85 impressions in two days**. Engagement rate now **7.6%**, still the highest in the entire log by a wide margin, carried on what remains the third-lowest reach ever recorded. The duplicate-content-suppression reading is now unambiguous: his own network keeps finding and engaging the post while LinkedIn refuses to serve it outward at all. On this tail it locks **~820–860** on 2026-08-07, landing directly inside the bottom-10% band (≤1,175) as the **4th-worst post in a 37-post log**. No change to the "a proven post is a proven template, never a proven text" rule — this run only hardens it.
**08-05 refresh (5d): 794 imp 🔴 BOMB** (48 react / 12 comm / 1 repost) — **+16 impressions in 24 hours** while reactions added +1. Engagement rate **7.6%**, still the highest in the log by a wide margin, still carried on the log's third-lowest reach. The tail is now effectively flat, so the projected lock tightens from ~820–860 to **~805–815**. ⚠️ Date correction: the URN decodes to **2026-07-30 13:25 UTC**, so the 7d FINAL is due **2026-08-06**, a day earlier than previously recorded — it locks tomorrow, alongside the "At 21" post. It will enter the bottom-10% band (≤1,175) as the **4th-worst post in a 38-post log** and will trigger a bottom-10% notification on lock. Duplicate-content suppression remains the only reading the numbers support: his network keeps finding and liking it, LinkedIn keeps refusing to carry it outward.
**★ 7d FINAL LOCKED 2026-08-06: 806 impressions 🔴 BOMB.** 48 reactions / 12 comments / 1 repost / 1 save / 0 sends. 11 profile viewers, **0 followers gained.** Engagement rate **7.4%** — still the highest in the entire log by a wide margin. ⚠️ Locked at **6.7d**, roughly 6 hours before the true 7d mark (URN decodes to 2026-07-30 13:25 UTC, so 7d lands 2026-08-06 13:25 UTC, after this scan ran). The tail added **+12 impressions in the last 24h**, so the true 7d value is 806–812 and the locked figure is accurate to within ~1%. Locked now rather than deferred because the value is settled and the bottom-10% notification was due.
**Analysis (final):** The controlled experiment holds at lock. The 1-year version of this text did **200K+**; this near-verbatim 2-year republish finished at **806** — a **~250x collapse** with copy, structure, author and account held constant. Record-high engagement rate on record-low reach is the fingerprint of duplicate-content suppression, not of a weak post: the audience that saw it loved it, and distribution refused to serve it. Two clean controls confirm the collapse was about this specific recycled text and not an account-level throttle: the 07-31 origin post ran **2.0x** its reach at matched age in the same week, and the 2026-08-05 credential post did **5,412 in 17 hours** on the same account four days later. **Enters the bottom-10% band as the 4th-worst post in a 40-post log**, displacing MS+Anthropic (1,175) from the bottom four.
**Rule (now final, add to the playbook): a proven post is a proven TEMPLATE, never a proven TEXT.** Reuse the spine — milestone hook → origin reminder → three numbered choices → give-back close — and rewrite every sentence, with this year's numbers and at least one story the original did not contain. ⚠️ The saved memory template for the Fiverr-anniversary post carries this caveat as of 2026-08-06.

---

### 2026-08-01 — "I accidentally built a dropshipping software that turned into a company I ran for 10 years" (origin story) 🔴 (7d FINAL: 1,695 imp — true publish 2026-07-31 13:30 UTC)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7488949326258307072
**Topic tag:** #origin #accidentalfounder #ebay #autods #founderjourney
**Hook type:** Confession-flavoured origin claim with a curiosity gap ("…and most people still don't know the story") — 25 words, well over the under-10 guideline, and opens with "I" on a non-confession verb
**Structure:** Origin claim + curiosity gap → conference scene (people asking how he runs his own dropshipping business) → the reveal (software running 100 eBay accounts) → the ask and the deflection ("It's not open to the public, but let's stay in touch") → the concrete detail that sells it (**phone numbers saved in WhatsApp as "eBay 1, eBay 2, eBay 3"**) → built it for them → free for a few weeks, then charged → "that software became AutoDS"
**Visual:** Image ×2
**Length:** ~180 words
**CTA:** None
**Full post text:**
> I accidentally built a dropshipping software that turned into a company I ran for 10 years, and most people still don't know the story.
> A few years ago, at a conference, people asked me how I manage my own dropshipping business.
> I told them I have software that automatically runs 100 eBay accounts for me.
> They started to wonder and asked how they could use it for their own businesses, too. Initially, I said, "It's not open to the public, but let's stay in touch."
> I got their phone numbers, added them to my WhatsApp, and saved them as a list: eBay 1, eBay 2, eBay 3.
> I started to build the software for them.
> Asked whether I would release it and whether they would use it. They said yes.
> We went public with a better version for a few weeks for free, and then straight away started charging.
> Eventually, that software became AutoDS, the company I ran for the last 10 years.

**Metrics (first capture 2026-08-02, ~1d / 24h checkpoint):**
- Impressions: **1,213** → **verdict: 🔴 (24h; soft start, roughly the pace that locks in the 1.5–2K band)**
- Reactions: 40; Comments: 12; Reposts: 1
- Engagement rate: ~4.4% (first-degree signature again)
**Analysis:** The best-*written* of the three origin posts — the "eBay 1, eBay 2, eBay 3" WhatsApp detail is exactly the kind of specific, unglamorous artifact that makes a founder story land, and the accidental-founder frame is genuinely on-brand for the 0→1 pillar. Two mechanical problems: the hook runs 25 words when the confirmed rule is under 10, so the curiosity gap arrives after the reader has already scrolled; and it is the **third consecutive origin/exit post in three days**, published into an audience that has just been told the same story twice. The 24h number is soft but not catastrophic, and it sits ~75% above the 07-31 republish, which supports the duplicate-content reading of that post rather than a general account-level throttle. 24h checkpoint locked; 7d FINAL due 2026-08-08.
**08-03 refresh (~2d, impressions UNAVAILABLE — Chrome signed out):** public counts 43 react / 12 comm (+3 react, comments flat). 72h checkpoint falls 2026-08-04 and needs a logged-in Chrome to capture impressions. 7d FINAL due 2026-08-08.
**★ 72h CHECKPOINT LOCKED 2026-08-04: 1,522 impressions 🔴** (48 react / 14 comm / 1 repost / engagement rate ~4.1%). +25% over the 24h capture — a normal-shaped climb, but off a base so low that the trajectory points at a **1.7–1.9K lock**, which would put it in the 🔴 band alongside the other two origin posts. The 24h read holds up: the "eBay 1, eBay 2, eBay 3" WhatsApp detail is the best-written moment in the whole batch and it still could not lift the post, because the 25-word hook spends the reader's attention before the curiosity gap arrives and the audience had already been served the same origin story twice in three days. **Useful control: at equivalent age it sits ~2x above the 07-31 republish (778 @ 4d), which is the cleanest available evidence that the republish collapse was duplicate-content suppression on that specific text rather than an account-level throttle.** 7d FINAL due 2026-08-08.
**08-05 refresh (4d): 1,590 imp 🔴** (50 react / 14 comm / 1 repost / engagement rate ~4.1%) — **+68 impressions over the 72h lock**, a 4.5% climb that puts the projected final at **~1.7K**, inside the 🔴 band and a little below the 1.7–1.9K call made at 72h. ⚠️ Date correction: the URN decodes to **2026-07-31 13:30 UTC**, so the 7d FINAL is due **2026-08-07**, a day earlier than previously recorded. The control value holds and sharpens: at matched age (both ~4–5d) this post sits at 1,590 against the republish's 794, exactly **2.0x**, on the same account in the same week with the same audience — the republish collapse was about that specific recycled text, not about the account.
**08-06 refresh (5.7d): 1,631 imp 🔴** (50 react / 14 comm / 1 repost) — **+41 impressions in 24h**, engagement completely frozen. The tail is flat, so this locks **~1,650** tomorrow, inside the 🔴 band and slightly below the 1.7K call made at 4d. The control value against the republish closes at **2.0x** at matched age and holds as the cleanest evidence in the log that duplicate-content suppression, not an account throttle, killed the 07-30 republish. 7d FINAL due 2026-08-07.

**★★ 7d FINAL LOCKED 2026-08-07: 1,695 impressions 🔴** (captured at ~6.75d — the true 7d mark is 2026-08-07 13:30 UTC, ~6h after this scan; the observed tail is ~+60/24h so the true 7d value is **1,695–1,710** and the locked figure is a mild under-read). 50 reactions / 14 comments / 1 repost / 2 saves / 0 sends. **12 profile viewers from this post, 0 followers gained.** Engagement rate ~4.0%.
**Final read:** it finished +4% over the 5.7d capture and ~11% over the 72h checkpoint, i.e. a completely flat tail, and it lands in the 🔴 band exactly where the 4d call put it. Three things this post settles:
1. **The diagnosis made at 24h holds all the way to the lock.** The best-written moment in the whole origin block — the "eBay 1, eBay 2, eBay 3" WhatsApp list — could not lift the post, because the 25-word hook spent the reader's attention before the curiosity gap arrived and the audience had already been served the same origin story twice in three days. Craft inside a saturated topic buys rank, not band, which is the same finding the DotDev block produced in July.
2. **It closes the cleanest control in the log on the republish collapse.** At its 7d lock this post sits at 1,695 against the republish's 806 — **2.1x on the same account, the same week, the same audience, the same subject matter** — and its engagement rate (4.0%) is roughly half the republish's record 7.4%. Record warmth on record-low reach is the duplicate-content fingerprint; this post has ordinary warmth on ordinary-low reach. **The republish died of recycled text, not of an account-level throttle. That question is now closed.**
3. **It is the third and weakest of the three origin posts** and the middle of the eight-post concentration block. Nothing about the writing explains its position; the subject does.

---

### 2026-08-03 — "Don't take advice from me" (podcast-promo / advice-filter thesis) 🔴 (in-flight, 24h checkpoint locked: 1,304)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7490036287115005952
**Self-repost:** https://www.linkedin.com/feed/update/urn:li:activity:7490273961277317120 (already live at first capture)
**Topic tag:** #advice #filter #podcast #mentorship #contrarian #reallifesuperpowers
**Hook type:** Flat contrarian imperative ("Don't take advice from me.") — **5 words, no "I" opener, self-deprecating reversal.** The best-disciplined hook the agency has shipped since the 07-29 shutdown post, and a direct fix for the 25-word hook that hurt 08-01
**Structure:** Contrarian imperative → the filter stated ("If you don't want to be where I am, nothing I say should matter to you") → "it works in both directions" → 3-bullet list of well-meaning advisers (parents / friends / colleagues) → the concession ("They all mean well") → the one question to run → the "vs." line → podcast credit naming Noa Eshed and Ronen Menipaz → closing hook back to the theme ("49 minutes of advice from someone who ignored almost all of it") → "Link in the first comment"
**Visual:** Image ×2 (Real Life Superpowers podcast episode card, ep 97, third-party-authority family)
**Length:** ~180 words
**CTA:** Link in first comment (podcast episode) — no open question

**Metrics (first capture 2026-08-04, ~17h):**
- Impressions: **1,099** → tracking 🔴 (17h; below the pace that reaches the 🟡 floor, but pre-24h so not yet a checkpoint)
- Reactions: 31; Comments: 14; Reposts: 1
- Engagement rate: ~4.1%
**Analysis:** **Craft-wise this is the cleanest post of the last ten days and it is starting soft anyway, which points at the CTA rather than the writing.** The hook obeys every rule the log has confirmed (under 10 words, no "I" opener, a reversal that earns attention), the "Advice from people who love you vs. advice from people who did it" line is the mandated "vs." executed properly, the 3-bullet list is odd-numbered, and there are no parentheses, em dashes or "not X, it's Y" constructions — **the first post in five to break the contrast-template drift.** The visible drag is structural: this is an **off-platform-referral post** ("Link in the first comment"), a format LinkedIn consistently under-distributes, and it lands on an audience that has now absorbed six consecutive posts about Lior's own story. The podcast credit also arrives late, so the reader hits a promo turn after being sold a principle. **Test this post sets up: if a fully rule-compliant post still locks 🔴, the binding constraint on this account is topic and CTA selection, not craft — which is what the last three weeks of data already suggest.** 24h checkpoint due 2026-08-05; 7d FINAL due 2026-08-10.
**★ 24h CHECKPOINT LOCKED 2026-08-05 (captured at ~42h — the 24h mark fell between scan runs, so this is the first available read after it): 1,304 impressions 🔴** (38 reactions / 15 comments / 0 reposts / engagement rate ~4.1%). +19% over the 17h capture — a shallow climb for a post at this age. Two things moved: reactions jumped 31 → 38 and comments 14 → 15, while the single repost recorded at 17h is no longer showing. **On this trajectory it locks around 1.6–1.8K on 08-10, which would put the most rule-compliant post of the last three weeks into the 🔴 band.** That is the test called at first capture, and it is now most of the way to answering itself: craft compliance alone does not move this account. The two structural drags identified at 17h both look correct — the off-platform "link in the first comment" CTA, and an audience that had absorbed six consecutive posts about Lior's own story before this one arrived. 7d FINAL due 2026-08-10.
**08-06 refresh (2.7d): 1,357 imp 🔴** (38 react / 15 comm / 0 reposts) — **+53 impressions in 24h and engagement frozen exactly** at yesterday's reaction and comment counts. A post this young should still be climbing; it is not. Projected lock tightens to **~1,450–1,550** on 08-10. <!-- see 08-07 refresh below --> **The test called at first capture is now effectively answered: the most rule-compliant post the agency has shipped in three weeks — 5-word hook, no "I" opener, proper "vs." line, odd-numbered list, no contrast template — is going to finish 🔴. Craft compliance alone does not move this account.** The two structural drags stand: an off-platform "link in the first comment" CTA, and an audience saturated with Lior's own story. 7d FINAL due 2026-08-10.
**08-07 refresh (3.7d): 1,425 imp 🔴** (38 react / 15 comm / 0 reposts / **0 saves / 0 sends / 1 profile viewer / 0 followers gained**) — **+68 impressions in 24h; reactions and comments frozen at yesterday's exact counts for the second consecutive day.** Projected lock now **~1,550–1,650** on 08-10, a touch above yesterday's call. The new datum is the profile-activity line: **1 profile viewer and 0 followers across the post's whole life**, against 135 viewers / 5 followers for the 08-05 give-back post and 15 / 1 for the 08-06 Shopify post at only 17h. **An off-platform-referral post does not just under-distribute, it converts nothing back to the profile** — the reader who wants the episode leaves for the podcast and never returns. That is a second, independent argument against the "link in the first comment" format beyond the reach penalty. 7d FINAL due 2026-08-10.
**08-09 refresh (5.7d — no scan ran 2026-08-08, so this is a two-day delta): 1,529 imp 🔴** (38 react / 15 comm / 0 reposts / **0 saves / 0 sends / 1 profile viewer / 0 followers**) — **+104 impressions across two days, and reactions and comments are frozen at 38 / 15 for the fourth consecutive reading.** The post has been socially dead since 08-05 and is now accruing residual feed impressions at ~50/day. **7d FINAL locks tomorrow (08-10) at ~1,570–1,610 🔴**, in line with the projection called on 08-07. Nothing left to learn from further reads; the entry is ready to close. **The test set at first capture is answered: a fully rule-compliant post — 5-word hook, no "I" opener, a proper "vs." line, an odd-numbered list, no contrast template — finishes 🔴 when it carries an off-platform CTA.** Craft compliance sets the floor, not the ceiling. The second, sharper finding stands on its own: **1 profile viewer and 0 followers across the post's entire life, against 166 / 5 for the 08-05 give-back post — "link in the first comment" does not just under-distribute, it converts nothing back to the profile.**

---

---

### 2026-08-04 — "Had a wealthy friend tell me about this founder doing $5M/year" (focus parable / borrowed-story fable) 🔴 (in-flight, 18h) — NEW
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7490398749744218112
**Self-repost:** https://www.linkedin.com/feed/update/urn:li:activity:7490640659587067904 (published 2026-08-05 05:31 UTC, ~16h after the original — inside the 6-8h self-repost window? No: 16h, roughly double it)
**True publish time (URN-decoded):** 2026-08-04 13:30 UTC
**Topic tag:** #focus #8020 #productportfolio #operatordecision #parable
**Hook type:** Second-hand anecdote opener with an ellipsis ("Had a wealthy friend tell me about this founder doing $5M/year...") — 12 words, over the under-10 rule, and **the concrete anchor belongs to a stranger.** No named entity, no Lior stake, no confession verb
**Structure:** Borrowed anecdote → the problem stated in numbers (4 products, attention split 25% each, flat revenue for years) → the decision ("Then he froze 3 of them") → the mechanism (same scale, minimum maintenance, whole team on one problem) → the payoff ("Revenue more than doubled within a year") → 3-line negation triple (No map / No guidebook / No secrets) → the principle ("Just focus") → the 80/20 restatement. No close, no question, no CTA
**Visual:** Image ×1 — a **cartoon-illustration dialogue panel**: two men at a café table, speech bubbles reading "this founder is doing $5M a year" / "So what did he do?". Illustration family, but **generic AI-cartoon rendering, unsigned, no personal artifact and no third-party authority.** ⚠️ **No ALT text** (the DOM carries only the generic "View image" label), which breaks the mandated ALT-text posting rule
**Length:** ~105 words
**CTA:** None — closes fully resolved, no engagement gap

**Full post text:**
> Had a wealthy friend tell me about this founder doing $5M/year...
> He had 4 products, each one kind of average.
> Attention was split 25% per product, and the team split the same way.
> He sat at that revenue for years, barely growing.
> Then he froze 3 of them.
> Same scale, minimum maintenance, zero new bets.
> The entire team moved to one problem on one main product.
> Revenue more than doubled within a year.
> No map to the top.
> No guidebook.
> No secrets.
> Just focus.
> 80% of your energy on the thing that already brings 80% of the revenue.

**Metrics (first capture 2026-08-05, ~18h):**
- Impressions: **821** → tracking **🔴, and on the worst opening pace in the log**
- Reactions: 9; Comments: 2; Reposts: 1; Saves: 1; Sends: 0
- 1 profile viewer from this post; 0 followers gained
- Engagement rate: ~1.6% (13 social engagements / 821 impressions)

**Analysis:** **This is the first post in the log that is simultaneously weak on reach AND weak on network warmth, which makes it a different failure from everything in the preceding block.** Every 🔴 of the last two weeks carried a high reaction count on low reach — the first-degree-only signature, where his own network still showed up. Here the network did not show up either: **9 reactions at 18h against 31 for the 08-03 post at 17h and 40-53 for the origin/credential posts at comparable ages.** Reach is 25% below the 08-03 post at matched age and it is the softest 18h number the log has ever recorded.

Three probable causes, in order of confidence:
1. **The story is not his.** "Had a wealthy friend tell me about this founder" puts two degrees of separation between Lior and the only concrete numbers in the post. His two ⭐ lanes both run on first-hand stake — a trending entity he has an operator opinion about, or his own credential and its lesson. A parable about an anonymous third party has neither, and it reads as generic LinkedIn wisdom rather than as insider intel. The exact same idea, told about AutoDS, is the 07-28 shutdown post, which is the best-performing post of the last eight days.
2. **It repeats the focus thesis eight days after the shutdown post** — same pillar, same argument, weaker proof. Topic concentration has now capped three consecutive monthly blocks, and this is the fourth consecutive post that fails to introduce a new subject.
3. **The visual is the weakest of the four approved families** — a generic AI-cartoon with the hook re-lettered into the speech bubbles, so it repeats line 1 instead of paying anything off, and it ships without ALT text.

⚠️ Craft notes: the hook runs 12 words and the anchor is a stranger's revenue figure; the negation triple (No map / No guidebook / No secrets) is a rhythm device with no information in it; there is no "vs." line; and the post closes fully resolved with no question, so the engagement gap is shut. On the positive side there are no parentheses, no em dashes and no "not X, it's Y" construction — **the contrast-template drift stays broken at two posts running.**

**Self-repost note:** the repost went out at 05:31 UTC on 08-05, about 16h after the original, roughly double the 6-8h window the posting rules specify. At capture it carried the same 9 reactions / 2 comments and no separate impression count.

24h checkpoint due 2026-08-05 (evening) — will be captured at the 08-06 run; 7d FINAL due 2026-08-11.
**★ 24h CHECKPOINT LOCKED 2026-08-06 (captured at ~42h — the 24h mark, 2026-08-05 13:30 UTC, fell between scan runs): 939 impressions 🔴.** 12 reactions / 3 comments / 0 reposts / 0 saves / 0 sends. **2 profile viewers, 0 followers gained.** Engagement rate ~1.6%, unchanged from 18h. **This is the coldest post in the log at this age on every axis at once.** For scale: at 42h it sits below the 08-03 post's *17-hour* number (1,099), and its 12 reactions compare with 38-54 for every other post in the window. The 1 repost and 1 save logged at 18h are both gone. On this trajectory it locks **~1,050-1,150** on 08-11, which would put it inside or on the edge of the bottom-10% band.
**The 08-05 hypothesis is now strongly supported and close to a hard rule: second-hand parables underperform first-hand operator stories so badly that even his own network disengages.** Same thesis, same pillar, same week: the shutdown post told *his* focus story with *his* dissolution letter and did 3,494; this one told a stranger's focus story with a stock cartoon and is tracking ~1,100 — a **~3x gap on identical subject matter, separated only by whose story it is.** Confirm at the 08-11 lock, then promote to a hard rule: **every story needs Lior's own stake and Lior's own numbers.**
**08-07 refresh (2.7d): 982 imp 🔴** (12 react / 3 comm / 0 reposts / 0 saves / 0 sends / **2 profile viewers / 0 followers**) — **+43 impressions in 24h and every engagement counter frozen exactly.** Projected lock **~1,050–1,100** on 08-11, which puts it 5th-lowest in the log and just outside the ≤806 bottom-10% band. **The borrowed-story finding got its counter-proof today rather than at the lock:** the 08-06 Shopify post argues from the same distance — a company Lior does not run, numbers that are not his — but he buys the stake back explicitly ("I got to see the answer up close. AutoDS is a #1 Shopify partner for the last 2 years, so I know their people personally") and it opened at **2,824 @ 17h, ~3x this post's entire 2.7-day total.** So the rule is sharper than "the story must be his": **the story can be about anyone, but Lior's standing to tell it has to be stated in the post.** A wealthy friend's anecdote gives him none; a two-year partnership gives him all of it. Confirm at the 08-11 lock.
**08-09 refresh (4.7d — two-day delta, no 08-08 scan): 1,039 imp 🔴** (12 react / 3 comm / 0 reposts / 0 saves / 0 sends / **2 profile viewers / 0 followers**) — **+57 impressions across two days, and every engagement counter is still frozen at its 08-06 value.** It cleared 1,000, but the shape has not changed in four days: this remains the coldest post in the log on every axis at once. **7d FINAL due 08-11 projects ~1,090–1,120**, 5th-lowest in the log and just outside the ≤806 bottom-10% band, so it will not trigger a notification on lock. The borrowed-story finding holds against its own counter-proof: **the 08-06 Shopify post is also about a company Lior does not run, using numbers that are not his, and it is at 3,832 on a two-day-younger clock — ~3.7x this post.** The single variable remains whether Lior's standing to tell the story is stated in the post.

---

### 2026-08-05 — "At 28, I sold my business to Fiverr" / 7 things I wish someone had told me (credential-milestone + give-back listicle) ✅ (in-flight; 24h checkpoint LOCKED 7,482 — **the best 24h in the log outside the ⭐ tier**)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7490761025462591489
**Self-repost:** https://www.linkedin.com/feed/update/urn:li:activity:7491001351049486337 (published 2026-08-06 05:24 UTC, ~16h after the original — again roughly double the 6-8h window, second run in a row)
**True publish time (URN-decoded):** 2026-08-05 13:30 UTC
**Topic tag:** #credential #milestone #fiverr #lessons #listicle #giveback #founderjourney
**Hook type:** Credential milestone + give-back promise ("At 28, I sold my business to Fiverr. / Here's what I wish someone had told me when I started:") — **8 words in line 1**, concrete anchor is a number plus a named acquirer, and line 2 states the payoff. Two-beat hook, inside the rules
**Structure:** Credential hook → give-back promise → **7 numbered lessons, each a bolded claim plus one line of mechanism** (side-hustle start / build it better than the incumbent / business model beats product / pick one thing / goals and milestones not tasks / let your people fail / treat business like a game) → humility close ("Took me years and one company to learn these. Hope they save you some time")
**Visual:** Image ×2
**Length:** ~200 words
**CTA:** None — closes on a give-back line, no link, no question

**Full post text:**
> At 28, I sold my business to Fiverr.
> Here's what I wish someone had told me when I started:
> 1. You don't have to quit your job to start a business.
> Start it on the side and let it pull you out.
> 2. If someone else built it, you can build it better.
> Same starting point, same raw materials. Stay competitive to your core.
> 3. Your product matters less than you think.
> The business model is what wins. Product, marketing, and finance pulling as one is the real edge.
> 4. Pick one thing and go all in on it.
> Focus plus belief is the whole game.
> 5. Track goals and milestones, not tasks.
> Then hire people who run without you standing over them.
> 6. Let your people fail.
> Room to try and miss is what grows them.
> 7. Treat business like a game.
> Clear the map in front of you, beat that boss, and the next one opens.
> Took me years and one company to learn these.
> Hope they save you some time (:

**Metrics (first capture 2026-08-06, ~17h):**
- Impressions: **5,412** → **tracking ✅ — already above the 5,000 floor at 17 hours**
- Reactions: 78; Comments: 16; Reposts: 1; Saves: 8; Sends: 2
- **93 profile viewers from this post; 4 followers gained**
- Engagement rate: ~1.9% (105 social engagements / 5,412 impressions)

**Analysis:** **This breaks a nine-post 🔴/🟡 block and it is the cleanest natural experiment the log has produced since the republish.** Seven days ago the "At 21 … Me at 31" post used the identical credential anchor — same exit, same account, same audience — and locked at **2,393 🔴 with 0 followers gained.** This post is that post with the scoreboard replaced by **7 lessons handed to the reader**, and at 17 hours it is already at **5,412 with 4 followers gained and 93 profile viewers.** The two differ in one structural variable, and the give-back is that variable. **The rule the log has been circling since the Birthday post (18,009 ⭐, credential + 10 lessons) is now demonstrated twice with a matched control: the credential-milestone lane travels on what the milestone teaches, never on the milestone.**
Three further reads:
1. **Saves are the tell.** 8 saves at 17h against 2 for "At 21" over its whole life and 0-1 for everything else in the block. A save is the signature of a reference listicle, and it is the one engagement type in this log that has consistently accompanied reach rather than trailing it.
2. **It answers the craft-versus-topic question from the other side.** The last three weeks established that craft compliance does not rescue a saturated topic. This post is proof of the converse: **the right subject with a give-back clears 5K without a trending news anchor, without a contrarian thesis, and without an off-platform CTA.** Craft sets the floor; subject and structure set the ceiling.
3. **It is still exit-anniversary content**, the eleventh consecutive post drawn from Lior's own story, so the topic-concentration flag is not resolved by it — the finding is narrower and more useful: **within a saturated topic, the give-back structure is what buys reach back.**
⚠️ Craft notes: hook is compliant; no parentheses, no em dashes, no "not X, it's Y" — **the contrast-template drift stays broken at four posts running.** Weak points: lesson 3's "the real edge" and lesson 7's game metaphor both edge toward aphorism, "I/me/my" runs 6 times against the ~3 guideline, and the post closes fully resolved with no engagement gap, which the 08-04 audit rates as a ⚠️ note rather than a blocker.
24h checkpoint due 2026-08-06 (evening, captured at the 08-07 run); 7d FINAL due 2026-08-12. **If it holds its trajectory it will be the first ✅ since Shopify-#1-affiliate (5,624, 2026-07-15) and the first in 22 posts.**

**★ 24h CHECKPOINT LOCKED 2026-08-07 (captured at ~41.7h — the 24h mark, 2026-08-06 13:30 UTC, fell between scan runs): 7,482 impressions ✅.** 92 reactions / 18 comments / 0 reposts / 3 saves / 1 send. **135 profile viewers from this post, 5 followers gained, 7 visits to the profile link button.** Engagement rate ~1.5% (114 social engagements / 7,482).
**+38% over the 17h capture, and it has already cleared every 🟡 post in the log.** At 41.7h it stands as **the 10th-highest number in the log at any age** and the highest anything has reached since Messi (10,771, 2026-07-20). On the Messi fast-burst shape it locks ~8.0–8.5K on 08-12; on a slower founder-journey shape, ~8.5–9.5K. Either way it is a decisive ✅ and the first since Shopify-#1-affiliate (5,624, 2026-07-15), ending a 22-post drought.
**The give-back control from the 08-06 scan strengthens at the checkpoint.** Against "At 21 … Me at 31" — same credential, same account, same audience, seven days apart, locked **2,393 with 0 followers** — this post is at **7,482 with 5 followers and 135 profile viewers**. That is **3.1x the reach**, up from the 2.3x measured at 17h, with the give-back as the only structural difference. The rule promoted yesterday is confirmed at a second checkpoint: **the credential-milestone lane travels on what the milestone teaches, never on the milestone itself.**
⚠️ **Metric revision to note:** LinkedIn now reports **3 saves / 1 send / 0 reposts** where the 17h capture read 8 saves / 2 sends / 1 repost. Saves and sends are being revised *down* as the post ages, so the "saves are the tell" read from 08-06 needs handling with care — 3 saves is still the highest in the current block, but the 8 that carried that argument was a transient number. **Treat LinkedIn's save/send/repost counts as provisional for the first 24h; impressions, reactions and comments have never revised downward in this log.**
⚠️ **Profile-activity is the stronger signal and it is unambiguous:** 135 profile viewers and 5 followers here, against 12 viewers / 0 followers for the 08-01 origin post over its entire seven days, and 1 viewer / 0 followers for the 08-03 podcast post over three days. **Give-back structure is the only thing in this block converting reach into profile traffic.**
7d FINAL due 2026-08-12.

**08-09 refresh (3.7d / ~89h — two-day delta, no 08-08 scan): 8,864 imp ✅** (96 react / 18 comm / 2 reposts / 1 save / 0 sends / **166 profile viewers / 5 followers**) — **+1,382 impressions since the 24h lock, and it is the only post in the current block still compounding.** Everything else on the feed added between 43 and 104 impressions per 48h; this added 1,382. On a decaying curve it locks **~9.5–10.3K on 08-12**, which would make it the **5th-highest final-locked post in the log** and put it within reach of Messi (10,771) without a trending news anchor of any kind.
**The slow-burn shape is the new finding, and it separates this lane from the newsjack lane.** Both this post and the 08-06 Shopify post opened strong. Measured against its own first capture, this one has climbed 5,412 → 7,482 → 8,864 and is still moving on day four, while Shopify went 2,824 → 3,832 and flattened. **A give-back listicle keeps getting re-served because it is reference material; a newsjack decays with the news cycle.** That is the practical argument for building the evergreen lane rather than chasing earnings days.
Profile conversion widens the gap further: **166 viewers / 5 followers here (1.87% of impressions) against 22 / 1 for Shopify (0.57%) and 1 / 0 for the 08-03 podcast post.** The give-back structure is the only thing in this block turning reach into profile traffic, now confirmed at a third reading.
⚠️ **The save-count revision continues downward: 8 (17h) → 3 (41.7h) → 1 (89h).** Reposts moved the other way, 0 → 2. This is the third consecutive reading where saves/sends/reposts were revised while impressions, reactions and comments only ever climbed. **Treat save and send counts as unusable for analysis at any age, not only in the first 24h** — a tightening of the 08-07 note, and it retires the "saves are the tell" read entirely.
7d FINAL due 2026-08-12.

---

### 2026-08-06 — "Here's the secret behind Shopify's 18% jump" (trending-entity newsjack + insider-standing + culture thesis) 🟡/✅ (in-flight, 17h) — NEW
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7491134728067055616
**Self-repost:** https://www.linkedin.com/feed/update/urn:li:activity:7491363708628135936 (published 2026-08-07 05:24 UTC, **~15.2h after the original** — third consecutive run at roughly double the 6-8h window)
**True publish time (URN-decoded):** 2026-08-06 14:14 UTC
**Topic tag:** #shopify #earnings #aikillssaas #culture #partnerintel #newsjack
**Hook type:** Trending-entity news anchor with a number ("Here's the secret behind Shopify's 18% jump.") — **7 words, named entity in position 4, a hard number, no "I" opener.** Fully compliant, and the first hook in twelve posts anchored on something that is not Lior's own biography
**Structure:** News hook → the reversal setup (all year the story was "AI kills SaaS" with Shopify as the named victim, stock down 23%) → the turn (earnings: revenue +34%, AI orders tripled) → curiosity gap ("everyone is now hunting for the secret strategy") → **insider standing stated explicitly** ("I got to see the answer up close. AutoDS is a #1 Shopify partner for the last 2 years, so I know their people personally") → the deflating answer ("almost boring. Culture.") → 3-bullet mechanism (hackathons / trainings / daily AI expectation) → the CEO memo line ("Before you ask for headcount, prove AI can't do the job") → developer-community close → wink ("Someone forgot to tell Shopify that SaaS is dead (:")
**Visual:** Image ×2
**Length:** ~190 words
**CTA:** None — closes on a wink, fully resolved

**Full post text:**
> Here's the secret behind Shopify's 18% jump.
> All year, the story was the opposite: AI kills SaaS, and Shopify was the named victim.
> The stock dropped 23% on that fear.
> Then the earnings landed.
> Revenue up 34%.
> AI orders tripled.
> Everyone is now hunting for the secret strategy behind it.
> I got to see the answer up close.
> AutoDS is a #1 Shopify partner for the last 2 years, so I know their people personally.
> The answer is almost boring.
> Culture.
> - AI hackathons
> - Trainings
> - Every employee is expected to work with AI daily
> The CEO put it in a memo that the whole industry read:
> Before you ask for headcount, prove AI can't do the job.
> And around them, a developer community that believes in the platform and keeps shipping, fast.
> Someone forgot to tell Shopify that SaaS is dead (:

**Metrics (first capture 2026-08-07, ~17h):**
- Impressions: **2,824** → **tracking 🟡/✅ — the second-best 17h start in the log**, behind only the 08-05 give-back post (5,412)
- Reactions: 44; Comments: 16; Reposts: 2; Saves: 2; Sends: 0
- 15 profile viewers from this post; 1 follower gained
- Engagement rate: ~2.3% (64 social engagements / 2,824 impressions)

**Analysis: this is the first post in twelve to leave Lior's own biography, and it is built to the exact specification the 08-04 scan promoted to a hard rule.** That rule reads: *named trending entity + contrarian thesis = ⭐; thesis without an entity = low 2Ks; entity without a thesis = sub-1.5K.* This post has both halves — Shopify and its earnings in the first seven words, and a real counter-thesis (the AI-kills-SaaS narrative was wrong, and the reason is culture rather than product) carried by the body rather than parked in a CTA. **2,824 at 17h is roughly 2.5x the 17h pace of the origin/exit block it follows.**
Three reads:
1. **It answers the 08-04 borrowed-story problem from the other direction, and sharpens the rule.** The 08-04 parable was also about someone else's company and someone else's numbers, and it did 821 @ 18h. The difference is one sentence: this post **states Lior's standing to tell the story** ("#1 Shopify partner for the last 2 years, so I know their people personally"), where the parable offered "a wealthy friend told me." Same structural distance from the subject, opposite result. **The story does not have to be his; his standing to tell it has to be in the post.**
2. **The ceiling is set by how big the moment is, and this moment is mid-sized.** The two ⭐⭐ posts in this lane sat at ~22K by 17h (Google/Base44) because the anchor was a globally trending product launch. A quarterly earnings beat is real news with a much narrower audience, so the honest projection is **5–7K, i.e. ✅ but not ⭐**, on the Messi fast-burst shape where day one sets the ceiling. Watch the 48h number: if it is not roughly double this, it locks 🟡.
3. **It clears the CEO relevance filter on standing rather than on topic.** Shopify's culture memo is not Lior's story, but a two-year #1-partner relationship is exactly the credential that makes commentary on it insider intel rather than commentary. This is the reusable move for newsjacking a partner's news without slipping into product marketing.
⚠️ Craft notes: hook compliant (7 words, named entity, number); 3-bullet list is odd-numbered; **no parentheses, no em dashes, no "not X, it's Y" — the contrast-template drift stays broken at five posts running**; "I/me/my" runs 3 times, inside the guideline; Shopify is treated as a partner and praised throughout, so the never-criticize-Shopify rule holds and "#1 Shopify partner" uses the approved public wording rather than "affiliate." Weak points: **there is no single "vs." sentence** — the fear-narrative-versus-earnings contrast is carried across the whole post rather than landed in one line, which the Top-13 playbook asks for; and the post **closes fully resolved on a wink with no engagement gap**, rated ⚠️ note rather than blocker per the 08-04 audit.
24h checkpoint due 2026-08-07 (evening, captured at the 08-08 run); 7d FINAL due 2026-08-13.

**⚠️ 24h CHECKPOINT MISSED — no scan ran 2026-08-08. The first available read after the 24h mark is this one, at 2.7d.**
**08-09 capture (2.7d / ~65h): 3,832 imp 🟡** (54 react / **24 comm** / 2 reposts / 0 saves / 0 sends / **22 profile viewers / 1 follower**). Engagement rate ~2.1% (80 social engagements / 3,832). **+1,008 impressions over the ~48h since the 17h capture.**
**The 48h test called on 08-07 comes back negative, and the projection has to come down.** That test read: *if the 48h number is not roughly double the 17h number, it locks 🟡.* At 65h it is **1.36x** the 17h number, not 2x. Revised projection for the 08-13 lock: **~4,200–4,800 🟡, missing the 5,000 ✅ floor.** The 5–7K ✅ call made at first capture was too generous and the reason is the one flagged in read #2 of that entry: **a quarterly earnings beat is a mid-sized moment.** The ⭐⭐ posts in this lane (Google/Base44) were anchored to globally trending product launches and sat at ~22K by 17h. **The named-entity + contrarian-thesis rule still holds for whether a post travels; the size of the moment sets how far.**
**Two things this post does better than anything else in the block, and neither is reach.**
1. **It is the sharpest discussion-driver in the current window: 24 comments on 3,832 impressions = 0.63%, against 0.20% for the 08-05 give-back post.** Comments have climbed 16 → 24 while its reactions moved 44 → 54, a 0.44 comment-per-reaction ratio. A contrarian thesis about a company people have opinions about generates argument; a give-back listicle generates saves and profile visits. **These are two different products and they should be measured against different targets.**
2. **It is the only post in twelve to leave Lior's biography**, and it still cleared every 🔴 in the block by a wide margin. Topic rotation is worth roughly 2.5x against the exhausted exit/origin material even at the bottom of its own lane.
**Cadence flag: nothing has been published since this post went out 2026-08-06 14:14 UTC — a ~2.8-day gap against what had been a daily agency cadence.** Two of the three days with no publishing follow the account's best post in three weeks, so the momentum from the 08-05 give-back post is being spent rather than compounded. Worth raising in the Monday digest.
7d FINAL due 2026-08-13.


### 2026-08-10 — "The most successful people I've met all share one habit: They ask" (Jim Rohn borrowed-principle listicle) 🔴 BOMB (7d FINAL, back-captured 2026-08-29: 687 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7492586991721537536/
**Published (URN-decoded):** 2026-08-10 14:25 UTC
**Topic tag:** #mindset #borrowed-principle
**Hook type:** superlative-claim opener ("The most successful people I've met…")
**Structure:** 3-step numbered principle + attribution P.S.
**Visual:** none captured
**Length:** ~120 words
**CTA:** none

**Full post text:**
> The most successful people I've met all share one habit:
> They ask.
> (People rarely do it)
> I get it. Asking feels exposed. What will people think?
> Since the very beginning of my journey as an entrepreneur, one person has been on my side and taught me this:
> 1. Define what you want. Be clear. Be specific. How wide, how high, how soon, what size, how much.
> 2. Ask big. Success isn't in short supply; it's like an ocean, and there's plenty of it. So ask with intelligence and ask with faith.
> 3. That's it... That's the art of asking.
> The people who live by this don't wait to be picked. They define what they want. And ask for it.
> The ocean is full. Bring a bucket.
> P.S. Jim Rohn is the person I've learned this from.

**Metrics (7d FINAL — captured 2026-08-29 at ~19d, includes long tail):**
- Impressions: **687** → **verdict: 🔴 BOMB**
- Reactions: 41 · Comments: 12 · Reposts: 1 · Saves: 2 · Sends: 0
- Profile viewers from post: 1 · **Followers gained: 1**
- Engagement rate: 7.9% (high rate on tiny reach = first-degree-only distribution)

**Analysis:**
- What worked: nothing at the distribution layer. The 7.9% engagement rate on 687 impressions is the classic signature of a post that never left the first-degree network.
- What didn't: (1) **the story is Jim Rohn's, not Lior's** — this is the third confirmation of the borrowed-story failure after the 08-04 parable (1,174 🔴) and it is the same shape: cold on reach AND cold on network. (2) "The art of asking" is exactly the aphoristic concept-naming the vault rules ban. (3) Zero operator stake, zero numbers, no AutoDS scene — it fails the CEO relevance filter as pure motivational content, the Motivator archetype the brand explicitly is not.
- vs. Lior's baseline: **80% below the 3,255 median**; enters the bottom-five of all n=52 finals.
- vs. top-creator patterns: matches no winning pattern. Closest analogue is "Treat yourself like a product" (518 🔴) — self-help with no founder bridge.

**Learnings applied going forward:** Borrowed-principle posts are now 🔴 three-for-three (Jim Rohn 687, wealthy-friend parable 1,174, and the pattern behind Treat-yourself 518). **Promote to a hard rule: if the story's protagonist is not Lior and the numbers are not AutoDS's, do not draft it.**

---

### 2026-08-11 — "Anthropic just dropped invisible watermarks into Claude" (trending-AI newsjack + "teach me" close) ✅ (7d FINAL, back-captured 2026-08-29: 8,361 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7492948245141225472/
**Published (URN-decoded):** 2026-08-11 14:21 UTC
**Topic tag:** #ai-newsjack #anthropic
**Hook type:** trending-entity news anchor in the first 6 words
**Structure:** news → mechanism (2 layers) → contrarian "does it matter?" → open question to the audience
**Visual:** none captured
**Length:** ~170 words
**CTA:** "Teach me in the comments"

**Full post text:**
> Anthropic just dropped invisible watermarks into Claude.
> Everyone is panicking over it. But does it even matter?
> First, what actually happens. Claude now marks everything it creates on 2 layers:
> 1. Text: an invisible mark hidden inside the words. You can't see it. Machines can. Copy it, paste it anywhere, the mark comes along.
> 2. Files: Every file Claude creates carries a signed digital signature that shows where it came from. It's built into the model itself.
> So every proposal, post, and email you polished with AI can now be traced.
> But... does it matter? Everyone knows everyone works with AI. That stopped being a secret somewhere in 2023.
> So a machine can prove AI touched your text. Fine. It still can't tell who had the idea, who made the calls. The thinking has no watermark.
> And one thing I'd love to understand: How does this even work? It's clear how they mark files, but how do they hide a mark inside words without changing how they read? Teach me in the comments.

**Metrics (7d FINAL — captured 2026-08-29 at ~18d, includes long tail):**
- Impressions: **8,361** → **verdict: ✅**
- Reactions: 41 · **Comments: 87** · Reposts: 2 · Saves: 5 · Sends: 4
- Profile viewers from post: 16 · **Followers gained: 4**
- Comments/reactions ratio: **212%** — the highest comment-dominant post in the entire log

**Analysis:**
- What worked: (1) the contrarian-AI-trending-tool lane holds — named tool in the first 6 words + a contrarian frame, no tactical prescription. (2) **"Teach me in the comments" is the strongest comment engine ever measured on this account**: 87 comments against 41 reactions. The engagement gap left deliberately open, with a genuine knowledge question, beats every closed ending in the log. (3) "The thinking has no watermark" is a clean quotable principle.
- What didn't: **87 comments and 8,361 impressions converted to only 4 followers.** Under the KPI adopted 2026-08-23 this is the central finding: comment volume is not follower conversion. The comments are people teaching Lior, which builds no reason to subscribe.
- vs. Lior's baseline: **157% above the 3,255 median**; 10th-highest final of n=52.
- vs. top-creator patterns: matches the confirmed contrarian-AI lane (Paperclip 30K → Anthropic 93K → Google/Base44 146K), at the low end of that lane's range.

**Learnings applied going forward:** The "teach me" close is now a **proven comment lever and a disproven follower lever**. Under the follower KPI it belongs in the 10% reach-play budget, not the 60% conversion budget. Also note: this newsjack ran ~1 day after the news, and its follow-up explainer two days later collapsed (see 08-17) — the lane is day-one only.

---

### 2026-08-12 — "Galit finished dental school this week" (spouse-milestone → founder-process parallel) ✅ (7d FINAL, back-captured 2026-08-29: 8,253 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7493297762961088512/
**Published (URN-decoded):** 2026-08-12 13:30 UTC
**Topic tag:** #personal #process #milestone
**Hook type:** named-person concrete anchor, 6 words
**Structure:** scene (3 specifics) → recognition → principle → tribute
**Visual:** none captured (likely photo — not verifiable at back-capture)
**Length:** ~130 words
**CTA:** none

**Full post text:**
> Galit finished dental school this week.
> The best masterclass I've ever seen.
> Six years, zero shortcuts:
> - Three hours on the road every day, Tel Aviv to Jerusalem and back.
> - Coming home from the clinic and opening the books again.
> - Studying through our engagement, through our wedding, through every holiday in between.
> Watching her, I recognized the same thing that builds companies.
> Most days, it looks stuck. Some days it looks like failing. Then one day, it breaks through.
> A degree or a company. Same rule. Success is a process, and most of it happens when nobody claps.
> People sometimes ask about the best deal I ever closed. It was in May 2025, when she said yes.
> Congratulations Doctor ❤️ Galit Vainshtein Pozin

**Metrics (7d FINAL — captured 2026-08-29 at ~17d, includes long tail):**
- Impressions: **8,253** → **verdict: ✅**
- **Reactions: 166** (highest reaction count of any post in the August block) · Comments: 31 · Reposts: 0 · Saves: 0 · Sends: 0
- Profile viewers from post: 44 · **Followers gained: 14**
- Engagement rate: 2.4%

**Analysis:**
- What worked: (1) the personal-milestone-with-founder-bridge rule is confirmed again — the wellness/personal lane works precisely when the founder lesson is explicit ("I recognized the same thing that builds companies"). (2) "Most of it happens when nobody claps" is the quotable. (3) Named, tagged, specific: a real person, real route, real dates. Zero AI slop risk.
- What didn't: **0 saves and 0 reposts.** This is affinity content, not utility content — nobody keeps it. Under the save-first axis adopted 2026-08-23 this post is the pure counter-example.
- vs. Lior's baseline: **154% above the 3,255 median**; 11th-highest final of n=52.
- **Follower efficiency: 14 followers on 8,253 impressions = 1.70 per 1,000** — against 0.48/1K for the watermark newsjack at nearly identical reach. **The warmer post converted 3.5x better at the same reach.**

**Learnings applied going forward:** This is the strongest evidence yet for the 2026-08-23 KPI change. Two posts, ~8.3K impressions each, one week apart: the newsjack won comments 87-to-31, the personal milestone won followers 14-to-4. **Reach parity, 3.5x follower gap.** The affinity layer converts; the reach play does not.

---

### 2026-08-13 — "3 weeks abroad. Came back lifting heavier than when I left." (travel-discipline listicle) 🟡 (7d FINAL, back-captured 2026-08-29: 3,340 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7493660560673239040/
**Published (URN-decoded):** 2026-08-13 13:31 UTC
**Topic tag:** #discipline #travel #habits
**Hook type:** two-beat anomaly hook (setup + counter-intuitive result)
**Structure:** old pattern → 3 changes → honest caveats → principle → PS question
**Visual:** none captured
**Length:** ~150 words
**CTA:** "What's the first habit that dies when you travel?"

**Full post text:**
> 3 weeks abroad. Came back lifting heavier than when I left. (3 small changes did it.)
> First time in 10 years.
> The old pattern, every trip: - Train for months - Finally hit a peak - Board a plane - Land 4 months behind
> This time I changed 3 things:
> 1. Trained anyway, even short sessions in whatever gym the hotel had.
> 2. First hour in every hotel, a delivery order of protein and fruit straight to the room.
> 3. Water all day.
> It works. Not pretending it was perfect. Desserts happened. Some sessions were 40 minutes. And sleep? I wanted my 8 hours every night. Most nights, I lost that fight. Did my best there too.
> But a business trip stopped being a reset button.
> Consistency on the road beats perfection at home.
> PS: What's the first habit that dies when you travel?

**Metrics (7d FINAL — captured 2026-08-29 at ~16d, includes long tail):**
- Impressions: **3,340** → **verdict: 🟡**
- Reactions: 57 · Comments: 8 · Reposts: 0 · Saves: 2 · Sends: 0
- Profile viewers from post: 23 · **Followers gained: 2**
- Engagement rate: 2.0%

**Analysis:**
- What worked: the two-beat anomaly hook (line 1 setup, line 2 counter-intuitive payoff) and the honest caveats block, which is the anti-AI-slop signal that keeps this readable.
- What didn't: (1) **no founder bridge.** Unlike the Galit post, this never crosses back to building companies — "consistency on the road beats perfection at home" is a wellness principle, not an operator principle. That is the difference between 8,253 and 3,340. (2) The odd-number rule is satisfied (3 changes) but the content is a productivity/wellness tip, which the CEO relevance filter flags.
- vs. Lior's baseline: **+2.6% against the 3,255 median** — dead centre.
- **Follower efficiency: 0.60 per 1,000.**

**Learnings applied going forward:** Confirms the wellness-needs-founder-bridge rule for the sixth time. Same author, same week, same personal register: with the bridge (Galit) 8,253/14 followers; without it (gym) 3,340/2 followers.

---

### 2026-08-16 — "This role is probably not for you. Top 0.1%, or keep scrolling." (executive-assistant hiring post, negative-filter hook) ✅ (7d FINAL, back-captured 2026-08-29: 9,818 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7494747044570431489/
**Published (URN-decoded):** 2026-08-16 13:29 UTC
**Topic tag:** #hiring #standards
**Hook type:** negative filter / disqualification opener
**Structure:** filter → role reality (3 bullets) → what you get → apply link
**Visual:** none captured
**Length:** ~130 words
**CTA:** "Think you're in the 0.1%? Apply." + link

**Full post text:**
> This role is probably not for you.
> Top 0.1%, or keep scrolling.
> If intensity stresses you out, if last-minute changes throw you off- this isn't the seat.
> 200 employees, constant work travel, and a VERY packed schedule.
> I'm looking for the best executive assistant in Israel.
> What does that actually mean?
> • An intense pace, every day.
> • A standard of execution most people would rather not sign up for.
> • Working closely with a hyperactive CEO who doesn't compromise.
> What you get out of it: High salary and in one year you'll learn what takes most people a decade. Room to learn and grow, high compensation, and a real seat in the decisions that matter.
> Think you're in the 0.1%? Apply. https://lnkd.in/d_xNvYgA

**Metrics (7d FINAL — captured 2026-08-29 at ~13d, includes long tail):**
- Impressions: **9,818** → **verdict: ✅** (2nd-highest final of the August block)
- Reactions: 32 · Comments: 5 · Reposts: 0 · Saves: 4 · Sends: 2
- Profile viewers from post: 49 · **Followers gained: 5**
- Engagement rate: 0.4% — **the lowest engagement rate of any ✅ post in the log**

**Analysis:**
- What worked: the negative-filter hook is a genuine reach engine. 9,818 impressions on a job ad, with no story and no news anchor, is the highest a pure hiring post has ever reached here.
- What didn't: (1) **the reach is job-seeker reach, not audience reach.** 32 reactions and 5 comments on ~10K impressions means the distribution came from LinkedIn's jobs graph, not from resonance. (2) It converted 5 followers — 0.51 per 1,000, in the bottom band. (3) Note the earlier rule "no hiring CTA in story posts" is not violated here because this is an honest job ad, not a story that bait-and-switches. But it is also not brand content: it makes no argument a stranger would follow Lior for.
- **The "200 employees" figure appears here.** Vault rule says the public number is **"250 employees"**. ✅ SETTLED 2026-08-30: Reut confirmed the company has 200 employees. The live post and the profile headline were right, the old 250 rule was wrong. Fixed at source in CLAUDE.md and in memory.
- vs. Lior's baseline: **202% above the 3,255 median**; 5th-highest final of n=52.

**Learnings applied going forward:** Hiring posts are a **reach anomaly, not a content win** — high impressions, near-zero engagement, weak follower conversion. Log them separately from authored content when computing the content baseline; they inflate reach medians without teaching anything about the audience.

---

### 2026-08-17 — "How does Claude hide a watermark inside words?" (explainer follow-up to the 08-11 newsjack) 🔴 (7d FINAL, back-captured 2026-08-29: 1,428 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7495109902072291328/
**Published (URN-decoded):** 2026-08-17 13:30 UTC
**Topic tag:** #ai-explainer #anthropic
**Hook type:** question hook + hype parenthetical
**Structure:** question → 3-step mechanism → open question close
**Visual:** none captured
**Length:** ~160 words
**CTA:** "Do you see any reason to remove it?"

**Full post text:**
> How does Claude hide a watermark inside words? (The explanation will blow you away)
> Anthropic started marking everything Claude writes. Text and files. Files are the easy half. But an invisible mark inside plain text sounds like magic. So here's how it actually works:
> 1. You ask, Claude picks a word. Ask about the weather in London, and it needs one word. Cloudy/ grey/ overcast. All three are true. All three read the same to you.
> 2. A secret key makes the choice. The key, plus the words right before it, decides which one wins. You'd never notice. Either word was fine anyway.
> 3. The pattern gives it away. Anyone with the same key runs the math backward and spots a pattern human writing would never produce.
> It's Google DeepMind's method, wired into the model.
> So how do you get rid of it? I could write a whole guide on this. But should we even bother? The mark proves Claude was involved. So what? Do you see any reason to remove it?

**Metrics (7d FINAL — captured 2026-08-29 at ~12d, includes long tail):**
- Impressions: **1,428** → **verdict: 🔴**
- Reactions: 37 · Comments: 19 · Reposts: 0 · Saves: 3 · Sends: 0
- Profile viewers from post: 5 · **Followers gained: 0**
- Engagement rate: 3.9%

**Analysis:**
- What worked: it answered the exact question the 08-11 post asked the audience, which is good faith and good craft.
- What didn't: **this is the cleanest day-one-only proof in the log.** Identical topic, identical account, six days apart: the newsjack did 8,361, the explainer did 1,428 — a **5.9x collapse**. The news window closed. (2) "(The explanation will blow you away)" is hype-promise copy that the audience discounts. (3) A mechanism walkthrough is a tactical-explainer body, which is the exact shape that has bombed six times in this lane (Grok 1,347, Fable5-beach 1,222, MS+Anthropic 1,175, find-skills 792, Master Prompt 546).
- vs. Lior's baseline: **56% below the 3,255 median.**
- **0 followers gained** despite 19 comments.

**Learnings applied going forward:** Two hard confirmations. **(1) Newsjacks are day-one assets; a follow-up on the same news six days later loses ~6x.** **(2) The AI lane still bombs whenever the body is a mechanism explainer instead of an operator verdict** — n≈7 now. The 2026-08-23 spine recommendation ("the operator's read on AI commerce") is the right correction: verdict, not explanation.

---

### 2026-08-18 — "100K followers on Instagram this week" (milestone + doubters + assume-it-will-work thesis) 🟡 (7d FINAL, back-captured 2026-08-29: 4,828 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7495472575293222913/
**Published (URN-decoded):** 2026-08-18 13:32 UTC
**Topic tag:** #milestone #conviction #personal-brand
**Hook type:** credential-milestone anchor with number, 6 words
**Structure:** milestone → doubters quoted → callback to AutoDS → contrarian method → numbers → mission → principle
**Visual:** none captured
**Length:** ~140 words
**CTA:** none (closes on a principle)

**Full post text:**
> 100K followers on Instagram this week.
> (People I respect said drop it).
> You're Israeli. Your accent is too heavy. Americans won't follow you.
> Same music I heard before AutoDS. Different words, same doubt, right up until the exit.
> Most people wait for proof before they commit.
> I went the other way. Assumed it would work, then worked like it was already true.
> That meant 3 agencies that were replaced. Months of views from an audience I never aimed for.
> The first 60K took almost two years. The last 40K took three months.
> Nobody handed me a playbook when I started.
> Now my mission is to give someone else the nerve to start before they feel ready.
> Assume it will work.
> Worst case, you were wrong. Best case, you walk the whole road there smiling (:

**Metrics (7d FINAL — captured 2026-08-29 at ~11d, includes long tail):**
- Impressions: **4,828** → **verdict: 🟡** (172 impressions short of ✅)
- Reactions: 89 · Comments: 22 · Reposts: 0 · Saves: 2 · Sends: 0
- Profile viewers from post: 45 · **Followers gained: 0**
- Engagement rate: 2.3%

**Analysis:**
- What worked: (1) the line-2 parenthetical counter-hook is exactly the one sanctioned parenthesis exception and it lands. (2) "The first 60K took almost two years. The last 40K took three months." is the strongest single data line of the August block — concrete, asymmetric, memorable. (3) Warm engagement, second-highest reaction count of the block.
- What didn't: **0 followers gained on 4,828 impressions and 89 reactions.** This is the sharpest KPI paradox in the log: a well-liked post that converted nobody. Reading: the post is a *report on a win already achieved*. There is no promise of more, so there is nothing to subscribe to. (2) It is also a scoreboard post, and the 2026-08-06 finding said scoreboards are first-degree posts — this one earned a bigger network than that rule predicted but converted exactly as badly.
- vs. Lior's baseline: **48% above the 3,255 median.**

**Learnings applied going forward:** Reinforces the rule promoted 2026-08-06 and sharpens it for the follower KPI: **a milestone converts followers only when it hands the reader something to take away.** The give-back version (08-05, 7 lessons) did 11,422 and gained followers; the pure-milestone version does 4,828 and gains zero. Both use the same credential anchor.

---

### 2026-08-20 — "Every founder goes through the same stations" (6-stage founder-journey map) 🔴 BOMB (7d FINAL, back-captured 2026-08-29: 1,084 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7496213079307968514/
**Published (URN-decoded):** 2026-08-20 14:34 UTC
**Topic tag:** #founder-journey #resilience
**Hook type:** universal-claim opener
**Structure:** 6-item numbered abstraction ladder
**Visual:** none captured
**Length:** ~120 words
**CTA:** none ("Trust your grind (:")

**Full post text:**
> Every founder goes through the same stations. (I struggled for years.)
> 1. START. You ship before you feel ready, because ready never comes.
> 2. GET NO. The market pushes back. A launch nobody notices, a trial that never converts, a bad review from a user.
> 3. BREAK THROUGH. You build your way around the no. Real products come from this phase.
> 4. GET NO. AGAIN. BIGGER. The next rejection scales with you. Bigger company, bigger stakes, same feeling.
> 5. SCALE AGGRESSIVELY. You hire faster than you can learn names. When something finally works, you bet the company on it.
> 6. NEW GAME, NEXT PEAK. The prize for winning a level is a harder level.
> Trust your grind (:

**Metrics (7d FINAL — captured 2026-08-29 at ~9d, includes long tail):**
- Impressions: **1,084** → **verdict: 🔴 BOMB**
- Reactions: 39 · Comments: 14 · Reposts: 0 · Saves: 1 · Sends: 1
- Profile viewers from post: 4 · **Followers gained: 0**
- Engagement rate: 5.0% (first-degree-only signature again)

**Analysis:**
- What didn't: (1) **reductive-list opener with no operator scene — this is now the 5th confirmed bomb of that exact format** (70% rule 1,783, 10-80-10 1,701, Master Prompt 546, CEO-3-rules 2,083, this 1,084). The rule has held for five months without a single exception. (2) **Six items — an even number** — against the odd-numbers rule (3/5/7). (3) Not one AutoDS number, date, product or person appears anywhere in the post. It could have been written by any founder about any company, which is precisely what the interest-graph algorithm cannot place. (4) This is book material (the "dealing with no" thesis) compressed into a LinkedIn abstraction, and the compression removed everything specific.
- vs. Lior's baseline: **67% below the 3,255 median**; 6th-lowest of n=52.

**Learnings applied going forward:** The reductive-list bomb rule is now n=5 and should be treated as absolute. Also flag for the book workstream: **the "6 stations" framing is strong source material and weak post material** — it needs one station rendered as a real AutoDS scene with a date and a number, not all six as labels.

---

### 2026-08-25 — "Sold my business to Fiverr for $92M with this 47-slide deck" (free lead-magnet / open-sourced artifact) ⭐⭐ EXCEPTIONAL (in-flight @ 4d: **66,524 imp** — 3rd-highest post in the log)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7498008927662567424/
**Published (URN-decoded):** 2026-08-25 13:30 UTC
**Topic tag:** #exit #artifact #save-first
**Hook type:** credential + artifact anchor, 11 words, number in first 7
**Structure:** credential hook → parenthetical give-away → why he has standing → 3-line counter-intuitive advice → the artifact, free
**Visual:** native document / off-platform template link
**Length:** ~115 words
**CTA:** "Full 47-slide template: {link}" — **ungated**

**Full post text:**
> Sold my business to Fiverr for $92M with this 47-slide deck.
> (Now I'm open-sourcing it.)
> Since the exit, founders keep reaching out to consult on their sale processes. One piece of advice helped us more than anything else.
> So if you want to sell yours one day, start here:
> - Don't pitch your dream buyer first.
> - Book meetings with companies you would never sell to.
> - Practice on them.
> Watch which slide loses the room, then fix it while nothing is at stake.
> By the time the buyer you actually want sits down, your deck has already survived every hard question.
> This deck is the one that survived that process. Copy the structure. Fill in your numbers.
> Full 47-slide template: https://lnkd.in/d8ZhwTdY

**Metrics (@ ~4d, captured 2026-08-29):**
- Impressions: **66,524** → **tracking ⭐⭐ EXCEPTIONAL**
- Reactions: 316 · Comments: 60 · Reposts: 1
- **Saves: 167** — by a wide margin the most-saved post ever logged
- Sends on LinkedIn: 9 · Link visits: 52
- **Profile viewers from post: 1,179** · **Followers gained: 86**
- Engagement rate: 0.57%

**Analysis:**
- What worked: **everything the 2026-08-23 save-first thesis predicted, at the top of its range.** (1) A concrete, enumerable, specific artifact the reader expects to need again — 47 slides, not a concept. (2) The credential is in service of the artifact, not the other way round: the $92M number exists to establish that the deck worked. (3) **Ungated.** The A/B already recorded in memory (comment-gate 55 imp vs free download 23,111 imp on identical copy) is now settled beyond argument — the free version is at 66,524 and still climbing. (4) 167 saves against a log where 5 saves was a strong post: the save is the mechanic, and saves are what carried it into second-degree distribution.
- What didn't: only 52 link visits against 167 saves and 66K impressions — **people are saving the post, not fetching the deck.** The artifact's promise is doing the work more than the artifact itself. Worth watching, because a save that never converts to a visit teaches nothing about the reader.
- **⚠️ The $92M figure.** Vault rule: Fiverr's 20-F states $55.658M total consideration plus up to $36M earn-out; $92M is media-sourced. It is now in the hook of the account's third-biggest post ever. This is a standing exposure, not a new one, but it is now maximally visible. Flag to Reut, not actionable by this scan.
- vs. Lior's baseline: **1,944% above the 3,255 median.** Behind only Google/Base44 (146,506) and Anthropic MD→HTML (92,959).
- **Followers: 86 from one post.** Against a 963/month baseline, one post delivered ~9% of a typical month. The per-post win condition is 150+ in 48h; this did 86 in 4d, which is short of the bar but is **~6x the next-best post in the log** and the bar itself was set provisionally with no data of this kind.

**Learnings applied going forward:** This is the single most important result since the KPI change. **The save-first artifact post is now the confirmed follower engine**, and it beat the reach lane on its own terms. Concretely: (1) never gate; (2) the artifact must be countable in the hook (47 slides); (3) the credential's job is to prove the artifact worked. Next test is whether a *series* of these on a fixed rhythm compounds — which is exactly the signature-series recommendation. 7d FINAL due 2026-09-01.

---

### 2026-08-26 — "There's a reason Claude keeps giving you mid output" (Claude model-routing decision tree) ✅ (in-flight @ 3d: 6,271 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7498374442956533760/
**Published (URN-decoded):** 2026-08-26 13:43 UTC
**Topic tag:** #ai #decision-tree #save-first
**Hook type:** diagnosis-of-reader's-problem opener
**Structure:** problem → confession → 3-step routing tree → principle close
**Visual:** model-tree graphic (the Gemini-prompted model map in O-output)
**Length:** ~140 words
**CTA:** none

**Full post text:**
> There's a reason Claude keeps giving you mid output.
> It's not (only) about your prompt. It's the model you keep defaulting to.
> Anthropic ships four models. Most of us use one.
> I used to run Fable for everything. Assumed the strongest wins. But only ~10% of tasks actually need it.
> So I built this map to sort out my everyday tasks:
> Step 1: Does your task need a complex answer? ☑️ Yes: use Opus or Fable. ☑️ No: use Haiku or Sonnet.
> Step 2: In a hurry? ☑️ Yes: Haiku. Instant. Chat only, no heavy files. ☑️ No: Sonnet. Runs 70% of my week.
> Step 3: Would you clear a weekend for this? ☑️ Yes: Fable. Deep research. Analytical decisions. ☑️ No: Opus. Modeling, code review, deep analysis.
> When Opus gets stuck, escalate to Fable. Everything else, route down the tree.
> The upgrade is learning when to step down.

**Metrics (@ ~3d, captured 2026-08-29):**
- Impressions: **6,271** → **tracking ✅**
- Reactions: 48 · Comments: 19 · Reposts: 1 · **Saves: 12** · Sends: 2
- Profile viewers from post: 10 · **Followers gained: 2**
- Engagement rate: 1.1%

**Analysis:**
- What worked: a decision checklist is one of the five legal save-first formats, and it produced the second-highest save count of the block (12).
- What didn't: (1) **⚠️ "It's not (only) about your prompt. It's the model you keep defaulting to." is the banned "not X, it's Y" contrast template**, in the slot the rules specifically guard, and per the 2026-08-24 platform note that construction is reportedly auto-suppressed as AI slop. This post reaching 6,271 anyway is not a licence; it is a post that may have been capped. (2) **It fails the CEO relevance filter** — this is a tool-routing tip, exactly the productivity/tool-tip content the brand bans, and it also contradicts the recorded stack fact that Lior runs **Hermes Agent + OpenAI Codex** since June 2026. (3) **2 followers on 6,271 impressions = 0.32 per 1,000**, the worst conversion in the August block. Useful content, wrong seat: it sells tool knowledge, not operator access.
- vs. Lior's baseline: **93% above the 3,255 median.**

**Learnings applied going forward:** A save-first *format* is not enough — the artifact must come from the operator's seat. A model-routing tree is a creator's artifact and converts like one. Contrast directly with the exit deck (86 followers) and the give-back listicle: both are things only Lior could hand over. **Flag the "not X, it's Y" instance to the agency; two of these in the last month is drift.** 7d FINAL due 2026-09-02.

---

### 2026-08-27 — "THE ACTUAL STEPS TO GROW A SaaS COMPANY" (all-caps 4-step operator playbook) 🔴 (in-flight @ 2d: 1,124 imp)
**Post URL:** https://www.linkedin.com/feed/update/urn:li:activity:7498735026294136834/
**Published (URN-decoded):** 2026-08-27 13:35 UTC
**Topic tag:** #saas #operator-playbook #save-first
**Hook type:** all-caps promise + credential parenthetical
**Structure:** 4 steps, each with 2 checkbox tactics + a stated Rule
**Visual:** none captured
**Length:** ~230 words (longest of the block)
**CTA:** none captured in the visible portion

**Full post text (visible portion):**
> THE ACTUAL STEPS TO GROW A SaaS COMPANY:
> (The ones I used turning 0 INTO A $20M+ ARR COMPANY)
> - Step 1: Listen to your paying customers
> ☑️ Set up listening at scale, not one loud call at a time
> ☑️ Automated surveys at signup, at exit, plus funnel drop-off data
> Rule: You'll learn the most from the ones who leave
> - Step 2: Find what they'll actually pay for
> ☑️ Look past what they ask for, find what they pay to solve
> ☑️ At AutoDS, we thought they came to manage stores. They came to find what to sell.
> Rule: The gap is your next product
> - Step 3: Map the funnel
> ☑️ Lay out the customer's journey end to end, then mark every stage you don't own
> ☑️ At AutoDS, two gaps showed up: building the store and bringing traffic
> Rule: The gaps around your product are worth more than the features inside it
> - Step 4: Build the missing stage
> ☑️ At AutoDS, Build Your Store AI closed the first gap […]

**Metrics (@ ~2d, captured 2026-08-29):**
- Impressions: **1,124** → **tracking 🔴**
- Reactions: 48 · Comments: 16 · Reposts: 1 · Saves: 2 · Sends: 0
- Profile viewers from post: 5 · **Followers gained: 1**
- Engagement rate: 5.8% (first-degree-only signature)

**Analysis:**
- What worked: the content itself is genuinely operator-seat — real AutoDS product decisions, real gap analysis, the Build Your Store origin. On substance this is the closest of the three recent posts to the recommended spine.
- What didn't: (1) **The all-caps hook plus the ☑️ emoji manifest is the Chris Donnelly / Jasmin Alić lead-magnet layer the vault explicitly bans as of 2026-08-23.** It reads as creator content, and the account's audience appears to have priced it as such immediately. (2) An even-numbered list (4 steps) against the odd-numbers rule. (3) At ~230 words with 12 structural elements it violates one-idea-per-post. (4) Two days after a 66K post, this did 1,124 — the post-breakout slot was spent on the weakest format of the month.
- vs. Lior's baseline: **65% below the 3,255 median.**

**Learnings applied going forward:** Strong evidence that **the packaging, not the substance, sets the ceiling.** Same operator standing as the exit deck, opposite presentation, ~59x less reach. Concretely: no all-caps hooks, no ☑️ manifests, odd-numbered lists only. 7d FINAL due 2026-09-03.

---

### BACK-CAPTURED FINALS — the four posts left in-flight at the 2026-08-09 scan
All four are now well past 7d and are locked here from the 28-day Creator Analytics window captured 2026-08-29. ⚠️ **Method note: these are lifetime-to-date values, not clean 7d values.** All four had plateaued by their last reading, so the drift is small, but each may run marginally above its true 7d mark.

| Post | Last in-flight reading (08-09) | FINAL (locked 2026-08-29) | Verdict |
|------|-------------------------------|---------------------------|---------|
| 2026-08-03 "Don't take advice from me" (podcast promo) | 1,529 @ 5.7d | **1,713** | 🔴 |
| 2026-08-04 "wealthy friend / founder who froze 3 products" (borrowed parable) | 1,039 @ 4.7d | **1,174** | 🔴 BOMB |
| 2026-08-05 "At 28, I sold my business to Fiverr / 7 things" (credential give-back listicle) | 8,864 @ 3.7d | **11,422** | ✅⭐ |
| 2026-08-06 "the secret behind Shopify's 18% jump" (trending-entity newsjack) | 3,832 @ 2.7d | **4,581** | 🟡 |

**The 08-05 give-back listicle beat its own projection by ~11%.** The 08-09 scan projected 9.5–10.3K at lock; it finished at **11,422**, making it the **7th-highest post in the log** and the highest non-⭐-lane final ever. It kept compounding for days after every other post in its block had frozen, which is long-tail behaviour previously seen only in the Anthropic and Google ⭐⭐ posts. Combined with the 08-25 exit deck, the give-back/artifact structure now owns two of the account's top seven results.

**The 08-06 Shopify newsjack landed inside its revised band** (the 08-09 scan revised it down from 5–7K to ~4,200–4,800 after the 48h doubling test came back negative at 1.36x; it locked at 4,581). The projection method holds.

**The 08-04 parable confirms the 2026-08-06 finding at final lock.** 1,174 against the 07-28 shutdown post's 3,494 on an identical thesis — ~3x, separated only by whose story it is. With the 08-10 Jim Rohn post (687) the borrowed-story rule is now n=3 and unanimous.


---

## Rolling Benchmarks

**Lior's baseline (refresh 2026-05-31, n=15 final-locked posts):**
- Sorted impressions: 518, 546, 792, 1,701, 1,783, 1,892, 2,066, 2,070, 2,083, 2,530, 3,352, 4,614, **18,009**, 30,009, 92,959
- Median impressions: **2,070** (n=15, position 8 = 2,070; effectively unchanged from prior 2,075)
- Mean impressions: ~10,934 (heavily skewed by Anthropic 93K + Paperclip 30K + now Birthday 18K)
- Top 10% threshold: **30,009** (Paperclip floor); Anthropic at 92,959 is the ceiling; Birthday 18,009 is now the 3rd-highest final-locked post
- 🟡 floor (middling band starts): 2,500
- 🔴 ceiling (under-resonating): 2,499
- Note: **10 of 15 final-locked posts sit in 🔴 band (under 2,500).** **5 above the 🔴 cap: Anthropic (93K ⭐⭐), Paperclip (30K ⭐), Birthday "31/10 lessons" (18,009 ⭐ — FIRST non-AI ⭐), Founder Salary trap (4,614 🟡), Funnel-conversion (3,352 🟡).** Wim Hof cold-feet (2,530) sits right at the 🟡 floor. There are now TWO ⭐ lanes: contrarian-AI (Anthropic, Paperclip) and credential-milestone (Birthday).
- **NEWLY LOCKED 2026-06-06:** Tough-days-Israeli-tech **14,798 imp ✅⭐ EXCEPTIONAL** (7d FINAL, back-capture) — under the 15K absolute line but **top-10% of all Lior posts (5th-highest of n=18 finals)**; the most-reshared post in the log (15 reposts); first EXCEPTIONAL in the market-empathy + value-first-hiring lane. Brings the final-locked set to **n=18**.
- **NEWLY LOCKED 2026-06-04:** Google/Base44-killer **146,506 imp ⭐⭐⭐ ALL-TIME RECORD** (7d FINAL) — surpasses Anthropic 92,959 by ~58%; the contrarian-AI lane's highest ceiling yet. Brought the final-locked set to n=17.
- **NEWLY LOCKED 2026-06-10:** 34,454-layoffs advice-listicle **4,686 imp 🟡** (7d FINAL, back-capture) — same layoff/market-empathy theme as Tough-days (14,798 ✅⭐) but generic advice with no named anchors / no hiring offer → ~3.2x lower reach, 0 organic reposts. Confirms the reshare engine is the multiplier, not the empathy theme. Brings the final-locked set to **n=19**; 11 of 19 now sit in the 🔴 band, with 5 in 🟡 (Funnel 3,352, Founder Salary 4,614, 34,454-layoffs 4,686, plus Wim Hof 2,530 at the floor).
- **NEWLY LOCKED 2026-06-11:** "900 prompts" vibe-coding **5,825 imp ✅** (7d FINAL) — comedic caption-only-hook + payoff-in-visual; the FIRST ✅ in the log on **pure relatability** (no news anchor, no contrarian thesis, no credential). Reach-led, engagement thin (51 react / 3 comm / 0 reshares, ~0.93% rate). Confirms a new repeatable reach format. Brings the final-locked set to **n=20**; the ✅+ tier is now Anthropic (93K), Paperclip (30K), Birthday (18K), Tough-days (14.8K), Google (146.5K) + "900 prompts" (5,825) = 6 above the 5K floor.
- In-flight (not yet final, refreshed 2026-06-14): **accent-dealbreaker vulnerability (1,738 @ ~6d — Wim-Hof reach band, comments frozen at 4; tracking 🔴/🟡; 7d FINAL due 2026-06-15)**; **Founder's-Guide secondhand-listicle (1,799 @ ~5d — high comment-ratio [9 comm] but no reach wave, first-degree cap; tracking 🔴/🟡; 7d FINAL due 2026-06-16)**; **AutoDS-talks-to-Claude product-launch (1,633 @ ~3-4d — AI-tool name without contrarian frame, 4 reshares creeping; tracking 🔴/🟡; 7d FINAL due 2026-06-17)**; **Anthropic-repricing-Claude (2,124 @ ~48h — contrarian-AI news anchor + tactical-prescription body + vendor-lock-in meta-principle; above the tactical-bomb floor, below the commentary mega-winners; tracking 🟡/🔴; 7d FINAL due 2026-06-19)**.
- **NEWLY LOCKED 2026-06-02:** Microsoft+Anthropic agents workshop **1,175 imp 🔴 BOMBED** (7d FINAL) — AI lane but tactical-prescription body. Brings the final-locked set to n=16; 11 of 16 now sit in the 🔴 band.

- **NEWLY LOCKED 2026-07-12 (14-day-outage back-capture, 4 finals + 4 in-flight):** 8 posts published 07-03→07-10, first-logged this run. Four are effectively 7d-FINAL: **250-people/autonomy 3,374 🟡, Forbes-30u30 3,224 🟡, WhatsApp-Meta 3,032 🟡, Fable5-back/"beach" 1,222 🔴 BOMB.** Four in-flight: I'm-31/co-founder 3,909 🟡, Ofir/macro-manager 3,404 🟡, Fable5-team 3,027 🟡, Grok-4.5 1,141 🔴 (2d). **Zero cleared the 5K ✅ floor — the soft-reach regime that ran all through June continues into July (whole batch sits 1.1K–3.9K).** Two lanes separated cleanly: (a) **AI-model-news without a contrarian thesis stays sub-2K** — Fable5-beach 1,222 + Grok 1,141 extend that dead-end to **n=6**; (b) **founder-journey + macro-manager-autonomy posts reliably hit the 3.0–3.9K 🟡 band** (I'm-31, Ofir, 250-people, Forbes). Best single post: I'm-31/co-founder (3,909, first-person scene + credential). ⚠️ Full n-recount of the baseline array is overdue (last clean recount was n=20 on 2026-06-11; ~10 finals have since been added via notes only).

- **NEWLY LOCKED 2026-07-15 (2 finals):** **I'm-31/co-founder 4,175 🟡** (7d FINAL, back-capture ~8d — best final of the July batch, still under the 5K ✅ floor) and **Fable5-team-of-four 3,459 🟡** (7d FINAL — the top AI-model post of the batch, original "team of four" metaphor + signed illustration). Both confirm the two lanes that held all month: founder-journey (I'm-31) and the single AI-model format that clears 3K (original metaphor + signed art, never a spec sheet). Neither cleared 5K — the soft-reach regime persists into mid-July. Still in-flight this run: Ofir/macro-manager 3,619 @ 6d (7d due 07-16), Grok-4.5 1,302 @ 5d 🔴 (7d due 07-17), plus two new 07-14 posts — **disability/Paul-promotion 3,433 @ 19h 🟡** (best 24h start of the batch, human/culture lane, watch for a reshare wave; 7d due 07-21) and **DotDev-Toronto 1,424 @ 24h 🔴/🟡** (conference-announcement, reach-capped as the lane predicts; 7d due 07-21).

- **NEWLY LOCKED 2026-07-16 (1 final):** **Ofir/macro-manager 3,659 🟡** (7d FINAL — reach fully plateaued, +1% over the 6d capture). Fifth straight July final in the 3.0–4.2K 🟡 band (with I'm-31 4,175, Fable5-team 3,459, 250-people 3,374, Forbes 3,224); the founder-journey / macro-manager-autonomy lane is now the most reliable middle-of-the-band producer in the log, and still nothing clears the 5K ✅ floor — the soft-reach regime is now ~7 weeks unbroken. In-flight this run: **new 2026-07-15 Shopify-#1-affiliate-partner 3,581 @ 17h 🟡** (proof/case-study lane, best 24h-window start since the July batch began, self-reposted; 7d due 07-22); Paul-disability climbing well (4,326 @ ~2d 🟡, +26%/day, watch for the reshare wave; 7d due 07-21); DotDev-Toronto 1,498 @ 2d 🔴 (cap holding); Grok-4.5 1,320 @ 6d 🔴 (frozen, will lock 🔴 on 07-17).

- **NEWLY LOCKED 2026-07-19 (1 final) + REGIME CRACK (2 in-flight over 5K):** **Grok-4.5 locked 1,347 🔴 BOMB** (9d, 7d slot missed 07-17/18 with the Mac asleep) — the contrarian *question* CTA couldn't save a first-impression/spec-sheet body; extends the AI-model-news-without-a-real-thesis dead-end to **n≈6** (Grok 1,347, Fable5-beach 1,222, Microsoft+Anthropic 1,175, find-skills 792, Master Prompt 546). **The bigger signal: two in-flight July posts crossed the 5K ✅ floor for the first time in ~7 weeks** — Shopify-#1-affiliate **5,249 @ ~4d ✅** (proof/case-study, best reach-climb of the batch, +47% off the 17h capture; 7d due 07-22) and Paul-disability **5,072 @ ~5d ✅** (culture/named-teammate reveal, log's deepest comment ratio; 7d due 07-21). If both hold, they'd be the first ✅-band posts since "900 prompts" (5,825, 2026-06-11) and would confirm TWO reliable non-AI ✅ lanes: concrete-proof founder-journey and human/culture-reveal. Also in-flight: new 2026-07-16 trainer/discipline→business-parallel **2,952 @ 3d 🟡** (highest in-flight comment ratio ~46%; 7d due 07-23); DotDev-Toronto **1,691 @ ~5-6d 🔴** (reach-capped, will lock 🔴 07-21). ⚠️ Data-integrity: the two 07-14 posts (Paul, DotDev) have URN mismatches between the log and the live feed — flagged in each entry, resolve in the Monday digest. ⚠️ Full n-recount of the baseline array is still overdue (last clean recount n=20, 2026-06-11).

- **2026-07-20 scan (0 finals, 0 new posts — PUBLISHING GAP):** No new post since 2026-07-16. That is a **4-day silence (07-17 → 07-20)**, the longest gap in the July batch; worth raising with Reut/the agency in the Monday digest since cadence, not content, is now the binding constraint on the Q3 reach target. Both 5K-band posts held on their refresh: **Shopify-#1-affiliate 5,343 ✅** (+1.8%, 7d locks 07-22) and **Paul-disability 5,248 ✅** (+3.5%, 7d locks 07-21) — both climbs have flattened but sit comfortably above the floor, so the ~7-week ✅ drought should break with two finals this week and confirm the two non-AI ✅ lanes (concrete-proof founder-journey + human/culture reveal). **DotDev-Toronto 1,707 🔴** fully plateaued (+1%, locks 07-21 as predicted by the conference lane). **Trainer/discipline 3,060 🟡** (+3.7%) — notable negative result: its log-high ~46% comment ratio produced **no** second reach wave, and reactions/comments were frozen at 39/18 for a full 24h. That weakens the "high comment ratio precedes a reach wave" hypothesis; comment depth looks like an audience-warmth signal, not a distribution one, exactly as the DotDev reaction spike was. ✅ **Data-integrity flag from 07-19 is CLOSED:** DOM `data-urn` extraction confirmed Paul = 7482790928798093312 and DotDev = 7482426311492190210 (the two entries had swapped URNs; the previously-logged 7483024680992440320 exists nowhere in the feed). Both corrected in place — no digest action needed. ⚠️ Full n-recount of the baseline array is **still** overdue (last clean recount n=20, 2026-06-11; ~11 finals since added via notes only) — this is now the largest known debt in the log and should be scheduled.

- **2026-07-22 scan — 3 FINALS LOCKED, ✅ DROUGHT BROKEN, 1 BREAKOUT IN-FLIGHT, BASELINE RECOUNT DONE.** Finals: **Paul-disability 5,721 ✅**, **Shopify-#1-affiliate 5,624 ✅**, **DotDev-Toronto 1,784 🔴** (the 07-21 slot was missed with the Mac asleep, so the two 07-14 posts locked at 8d). **Two ✅ finals in one week ends the ~7-week drought that ran since "900 prompts" (5,825, 2026-06-11)** and confirms two repeatable non-AI ✅ lanes: **concrete-proof founder-journey** (promise put in writing → the number that proves it was kept) and **human/culture reveal with a named real teammate**. Important mechanism correction: **neither ✅ was carried by reshares** (1 and 2 reposts at lock). The old "this lane's ceiling is set by reposts" hypothesis is wrong for these two — both cleared 5K on sustained algorithmic reach. Combined with the trainer post's engagement freezing at 39/18 for three straight days while impressions kept creeping, the evidence is now decisive: **engagement depth is an audience-warmth signal, not a distribution one.**
  **3 new posts after a 4-day silence, and one is a breakout: 2026-07-20 Messi/"the lazy method" at 10,299 @ 2d ⭐** — the highest reach since Tough-days (14,798, 2026-05-28) and ~3x the July batch ceiling, from a brand-new lane: **cultural-moment newsjack with zero AI content**. It matches the ⭐ DNA exactly (globally-trending anchor in the first 7 words + a counter-intuitive number carrying the argument + the thesis IS the body, not the CTA) and proves **the anchor does not have to be AI — it has to be trending, and the thesis has to be the body.** That is the precise structural inverse of the AI-model dead-end (Grok 1,347, Fable5-beach 1,222). Also in-flight: **AutoDS-on-Anthropic-connectors 2,008 @ 1d 🔴/🟡** (product-launch lane, capping around 2K as it always does; the eBay-ban origin callback is what keeps it from reading as product marketing) and **today's DotDev-learnings/"make other people rich" 319 @ 1h** — which is the direct A/B test of the conference lane: same conference, same week, announcement version locked 1,784 🔴 vs this post-event operator-scene version with stage numbers and a stated thesis. Watch it.
  ⚠️ Digest flags: (1) the Messi post's "Busy players run more. Great players run right." sits very close to the banned "not X, it's Y" contrast template — the agency is drifting toward it; (2) today's post closes fully resolved with no engagement gap, and its first two lines are inverted (the "best business advice" line lands before the advice); (3) the 4-day publishing silence 07-17→07-20 preceded the breakout, so cadence remains the binding constraint on the Q3 reach target.

- ✅ **BASELINE RECOUNT COMPLETE (2026-07-22) — closes the debt outstanding since 2026-06-11.** Full final-locked array, **n=31**:
  518, 546, 792, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, 2,530, 3,032, 3,224, 3,352, 3,374, 3,459, 3,659, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,224** (position 16) — up from 2,070 at the n=15 recount. The median rose because the July 🟡 band (3.0–4.7K) is genuinely denser and healthier than the April/May body of work, not because the ceiling moved.
  - Mean: ~11,400 (skewed by the three ⭐⭐ outliers)
  - **Top 10% threshold: 30,009** (Paperclip floor; Google 146,506 is the ceiling)
  - **Bottom 10% threshold: ≤792** (find-skills 792, Master Prompt 546, Treat-yourself 518)
  - Band distribution: **🔴 under 2,500 → 14 of 31 (45%)** · **🟡 2,500–4,999 → 9 of 31 (29%)** · **✅ 5,000+ → 8 of 31 (26%)**
  - The 🔴 share has fallen from 10-of-15 (67%) to 14-of-31 (45%). Trajectory is improving.

- **2026-07-23 scan — 1 FINAL LOCKED, 1 NEW POST, BASELINE NOW n=32.** Final: **trainer/discipline→business-parallel 3,286 🟡** (7d FINAL, +0.4% over the 6d capture, reach fully plateaued). Updated array, **n=32**:
  518, 546, 792, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, 2,530, 3,032, 3,224, **3,286**, 3,352, 3,374, 3,459, 3,659, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,255** (n=32, mean of positions 16 and 17 = 3,224 and 3,286) — up from 3,224 at the n=31 recount.
  - Band distribution: **🔴 under 2,500 → 14 of 32 (44%)** · **🟡 2,500–4,999 → 10 of 32 (31%)** · **✅ 5,000+ → 8 of 32 (25%)**
  - Top 10% threshold unchanged at 30,009; bottom 10% unchanged at ≤792.
  **Two findings from this run.**
  **(1) The Messi breakout is a fast-burst, not a climber.** 10,299 @ 2d → **10,395 @ 3d (+0.9%)**. Its entire reach was delivered inside the first 48h and then stopped, which matches the Birthday post's reach-cap behavior rather than the Anthropic/Google long tail. Operational consequence for the cultural-moment newsjack lane: **ship while the moment is live, because day one sets the ceiling** — there is no later recovery, and a slow start cannot be rescued. Still on track to lock ~10.5K, the 6th-highest final in the log and the highest since Tough-days (14,798).
  **(2) The conference lane looks topic-capped, not craft-capped.** The 07-22 DotDev-learnings post hit its **24h checkpoint at 2,488 — below the 2,500 🟡 floor** — despite being the best-built conference post in the log (stage numbers, stated thesis, real operator standing). Its engagement is the warmest of the current set (68 reactions / 23 comments, ~34% comment ratio), and by the rule this log confirmed on 07-22, that warmth will not convert to reach. Provisional conclusion: **Lior's audience does not follow him to a partner's developer event**, so conference content is relationship maintenance, not reach, and should not occupy slots that need to clear 5K. Confirm or overturn at the 07-29 lock.
  **New post 2026-07-23:** guerrilla-marketing coffee-truck war story (140 @ 27m) — the **third straight DotDev-anchored post**, but the first with a real scene, escalation, and an antagonist. It is the clean test of finding (2): if a true operator war story clears ~3.5K, format beats topic and the lane is salvageable; if it lands in the same 2–3.5K band, topic is the ceiling and the digest should recommend ending the DotDev run.
  ⚠️ Digest flags: (1) **the "not X, it's Y" contrast-template drift is now a pattern, not a one-off** — Messi's "Busy players run more. Great players run right." (07-20) and today's "You can rent a booth. You can't buy buzz." (07-23), two instances in four days, both in the closing-principle slot the rules specifically guard; raise it with the agency. (2) Three consecutive posts anchored on the same conference is a topic-concentration risk during the week the log's only breakout came from an unrelated cultural moment. (3) Cadence has recovered (posts on 07-20, 07-21, 07-22, 07-23) after the 4-day 07-17→07-20 silence.

- **2026-07-24 scan — 0 finals, 1 NEW post (first-ever reshare), COFFEE-TRUCK 24h LOCKED, "FORMAT vs TOPIC" TEST ANSWERED (provisionally: TOPIC WINS).** No 7d FINAL crossed today (Messi 7d due ~07-27, AutoDS-connectors 07-28, DotDev-learnings 07-29, coffee-truck 07-30), so no notification triggers met → silent completion. Followers **11,337**. Refreshes captured:
  - **Coffee-truck guerrilla 24h checkpoint LOCKED at 2,114 🔴** (43 react / 11 comm / 0 reposts). This settles the test the 07-23 scan set up: the best-built of the three DotDev posts opened **below** the recap (2,488 @ 24h) and roughly at the flat announcement's pace. All three conference posts now cluster in the same ~1.7K–2.5K band at equivalent checkpoints **regardless of craft** → strong evidence the conference topic is the reach ceiling, not execution. **Format did not beat topic.** 7d FINAL 07-30 confirms.
  - **DotDev-learnings/"make other people rich" 3,150 @ ~2d 🟡** (82 react / 23 comm) — recovered above the 🟡 floor after the 2,488 24h dip; still the warmest-engagement post of the set. 7d FINAL due 07-29.
  - **AutoDS-Anthropic-connectors 2,404 @ ~3d 🔴/🟡** (75 react / 18 comm / 2 reposts, +20% off the 2,008 24h) — product-launch lane capping around 2–2.5K as it always does. 7d FINAL due 07-28.
  - **Messi/"lazy method" 10,511 @ ~4d ⭐** (92 react / 27 comm, +1.1% over the 3d capture) — confirms the 07-23 finding that this is a **fast-burst, not a climber**: ~99% of its reach landed in the first 48h and it has been flat since. On track to lock ~10.5K, 6th-highest final in the log. 7d FINAL due ~07-27.
    - **07-26 refresh (6d):** 10,632 imp (93 react / 27 comm / 0 reposts / 5 saves), +1.2% over the 4d capture — flat as predicted. 7d lock ~10,650, 6th-highest final in the log (n=32). 7d FINAL 07-27 (tomorrow).
  - **NEW: first-ever quote-repost** — Lior reshared teammate Ronen Anaby's DotDev recap with ~30 words of team-pride commentary (500 @ 5h, 30 react / 4 comm). Logged as a new format; reshares under-reach authored posts and don't fit the authored-scoring model, so treated as a soft credibility/relationship post, not a reach slot.
  ⚠️ Digest flags: (1) **Topic concentration is now extreme — 4 of the last 5 posts are DotDev/Shopify-anchored** (coffee-truck, learnings, this reshare, + the 07-14 announcement); the only non-DotDev post in the window, Messi, is also the only breakout. The conference lane is both reach-capped AND crowding out the slots. Strongest digest recommendation this week: **end the DotDev run and free the calendar for trending-cultural-moment or concrete-proof founder-journey posts.** (2) The "format beats topic" hypothesis for the conference lane is provisionally **refuted** at 24h — hold for the 07-30 lock but prepare to retire the lane. (3) The contrast-template drift ("not X, it's Y") flagged 07-22/07-23 still stands for the agency.

- **2026-07-26 scan — 0 finals, 0 new posts (2-day PUBLISHING GAP 07-25→07-26), all 4 in-flight refreshed. Silent completion** (no 7d lock crossed today; nothing hit an exceptional/bomb notification trigger). Followers **11,358** (+21 since 07-24). No new post since the 07-24 reshare — the weekend was silent, so **Messi remains the only non-DotDev post in the last six** and the topic-concentration flag from 07-24 is unchanged going into the Monday digest. Refreshes:
  - **Messi/"lazy method" 10,632 @ 6d ⭐** (93 react / 27 comm / 5 saves, +1.2% over 4d) — flat, fast-burst confirmed a third time. **Locks tomorrow (7d FINAL 07-27) at ~10,650, the 6th-highest final in the log.**
  - **DotDev-learnings/"make other people rich" 3,480 @ 4d 🟡** (90 react / 23 comm, +10.5% over 2d) — best-reaching of the three DotDev posts and still climbing inside the 🟡 band. 7d due 07-29.
  - **AutoDS-Anthropic-connectors 2,530 @ 5d 🟡** (76 react / 18 comm / 2 reposts, +5.2% over 3d) — nudged just over the 2,500 🟡 floor, the highest a pure product-launch post has reached in the log (its lane usually caps ~2K; the eBay-ban origin callback is what lifted it). 7d due 07-28.
  - **Coffee-truck guerrilla 2,315 @ 3d 🔴** (46 react / 23 comm, +9.5% over 24h) — still under the 🟡 floor and the lowest of the three DotDev posts despite being the best-built. 7d due 07-30.
  - **Ronen reshare 872 @ 2d** (soft) — reshare suppression confirmed; aging off.
  **One consolidated finding this run: the conference lane orders cleanly by CRAFT *within* a fixed topic ceiling.** At comparable ages the three DotDev posts sit learnings-recap 3,480 > announcement-lane / coffee-truck 2,315 > (the 07-14 announcement locked 1,784), and the best-crafted *scene* (coffee-truck) is NOT the highest — the one with the hardest stage numbers + a stated thesis (learnings) is. So craft buys a few hundred impressions of position inside the band but never a band change; **topic sets the ceiling, execution sets the rank underneath it.** This refines (does not overturn) the 07-24 "format did not beat topic" call and is the cleanest evidence yet for retiring the DotDev run after the 07-29/07-30 locks. Digest flags from 07-24 (extreme topic concentration; contrast-template drift) all still stand; add: **the weekend publishing gap means the agency shipped nothing 07-25→07-26, so cadence is again a live concern for the Q3 reach target.**

- **2026-08-02 scan — 6 FINALS LOCKED, 5 NEW POSTS, BASELINE NOW n=36, AND ONE ~300x NATURAL EXPERIMENT.** First scan since 2026-07-26 (six-day outage, 07-27→08-01, Mac asleep), so this run back-captures four 7d FINALs past their slots plus one reshare. Followers **11,570** (+212 since 07-26). LinkedIn's own 7-day rollup: **11,680 impressions, +48% vs the prior 7 days**, 256 reactions / 84 comments / 0 reposts / 10 saves.
  **Finals locked:** **Messi/"lazy method" 10,771 ⭐** (6th-highest final in the log; 79% out-of-network, the mechanical proof of the newsjack lane), **DotDev-learnings/"make other people rich" 3,777 🟡**, **AutoDS-Anthropic-connectors 2,811 🟡** (highest product-launch post ever logged), **coffee-truck guerrilla 2,562 🟡**, plus the Ronen reshare **1,208** (unscored) and a post-FINAL drift on the trainer post (3,286 → 3,361, locked value stands).
  **Updated final-locked array, n=36:**
  518, 546, 792, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, 2,530, **2,562**, **2,811**, 3,032, 3,224, 3,286, 3,352, 3,374, 3,459, 3,659, **3,777**, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, **10,771**, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,255** (n=36, mean of positions 18 and 19 = 3,224 and 3,286) — unchanged from the n=32 recount; the four new finals landed either side of the median and cancelled out.
  - Mean: ~10,300 (still dominated by the three ⭐⭐ outliers)
  - **Top 10% threshold: 18,009** (top 4 = Google 146,506, Anthropic 92,959, Paperclip 30,009, Birthday 18,009). **Changed from 30,009** — with n=36 the top decile is 3.6 posts, so Birthday is now inside it and Messi (10,771) is just outside.
  - **Bottom 10% threshold: ≤1,175** (bottom 4 = Treat-yourself 518, Master Prompt 546, find-skills 792, MS+Anthropic 1,175). The in-flight 07-31 republish at **693** would enter this band directly.
  - Band distribution: **🔴 under 2,500 → 14 of 36 (39%)** · **🟡 2,500–4,999 → 13 of 36 (36%)** · **✅ 5,000+ → 9 of 36 (25%)**. The 🔴 share keeps falling (67% at n=15 → 45% at n=31 → 39% now), but every post added this run landed 🟡 or below.
  **Three findings from this run.**
  **(1) A proven post is a proven TEMPLATE, never a proven TEXT.** The 07-31 anniversary post is a near-verbatim republish of the 1-year Fiverr-anniversary post that did **200K+**. It did **693** — a ~300x collapse with copy, structure, author and account held constant. Its engagement rate is the **highest in the entire log (7.9%)**, so the audience that saw it loved it; distribution simply refused to serve it. That combination — record warmth, record-low reach — is the fingerprint of duplicate-content suppression, not of a weak post. Add to the playbook: reuse the spine (milestone hook → origin reminder → three numbered choices → give-back close), rewrite every sentence, bring this year's numbers and at least one story the original did not contain. The saved memory template needs this caveat attached.
  **(2) The conference lane is closed.** All three DotDev posts finished inside a 2.0K band (learnings 3,777 > coffee-truck 2,562 > announcement 1,784) and none approached 5K. Craft ordered them; topic capped them. The coffee-truck post — the only one with a scene, an escalation and an antagonist — finished 1,215 below the flat recap. **"Format beats topic" is refuted.** Retire the lane as a reach slot.
  **(3) Topic concentration moved from Shopify to the exit story, and the week got worse, not better.** Four of the five new posts are origin/exit/credential content (07-30 then-vs-now, 07-31 anniversary republish, 08-01 accidental-founder, plus the 07-28 AI thesis as the only outlier). Batch reach: 3,350 / 2,223 / 2,207 / 1,213 / 693 — **zero cleared the 🟡 floor except the shutdown post, and the batch median (2,207) is 32% below the log median.** The single best post of the week by every craft measure, the **profitable-company shutdown (3,350 @ 4d 🟡)**, is also the only one that is neither a conference post nor an exit-anniversary post. Same lesson as the Messi week, one month later: the calendar keeps filling with the same story, and the only posts that travel are the ones that are not it.
  ⚠️ Digest flags: (1) **the "not X, it's Y" contrast drift is now n=4** (Messi 07-20, coffee-truck 07-23, shutdown 07-29's "easy math / actually tests you", plus the 07-28 "Building was the hard part. Now it's the free part.") — it has become the agency's default pivot device and it is a hard-rule violation; (2) **hook discipline is slipping** — the 08-01 hook runs 25 words against the under-10 rule, and 07-28 opens on a calendar year instead of a named anchor; (3) "Sold AutoDS to Fiverr for MILLIONS" in caps (07-30) cuts against the never-arrogant rule; (4) **cadence is finally healthy** — five posts in five days, 07-28→08-01, the best run in the log; the constraint has moved from cadence back to topic selection; (5) the scan itself was down 07-27→08-01, so four 7d slots were back-captured late (values are post-window and therefore mild over-reads, ~1–2% based on observed tail rates).

- **2026-08-04 scan — 1 FINAL LOCKED, 1 CHECKPOINT LOCKED, 1 NEW POST, BASELINE NOW n=37. Creator Analytics restored after a 2-day outage.** Chrome was signed back in as Lior, so every impressions number below is real — this closes the 08-03 gap where five posts refreshed on public engagement counts only. Followers **11,600** (+30 since 08-02). Impressions were readable inline on the activity feed, no per-post analytics navigation needed.
  **FINAL locked:** **07-28 AI-moat thesis 2,402 🔴** (7d, on the day). **Checkpoint locked:** **08-01 accidental-founder 1,522 🔴 at 72h.**
  **Updated final-locked array, n=37:**
  518, 546, 792, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, **2,402**, 2,530, 2,562, 2,811, 3,032, 3,224, 3,286, 3,352, 3,374, 3,459, 3,659, 3,777, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, 10,771, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,224** (n=37, position 19) — down from 3,255 at n=36. First median *decline* since the n=15 baseline; the post added this run landed below it.
  - Mean: ~10,090 (still dominated by the three ⭐⭐ outliers)
  - **Top 10% threshold: 18,009** (unchanged — top 4 = Google 146,506, Anthropic 92,959, Paperclip 30,009, Birthday 18,009)
  - **Bottom 10% threshold: ≤1,175** (unchanged — bottom 4 = Treat-yourself 518, Master Prompt 546, find-skills 792, MS+Anthropic 1,175). The in-flight 07-31 republish (778 @ 4d) will enter this band at its 08-07 lock.
  - Band distribution: **🔴 under 2,500 → 14 of 37 (38%)** · **🟡 2,500–4,999 → 14 of 37 (38%)** · **✅ 5,000+ → 9 of 37 (24%)**
  - ⚠️ **Arithmetic correction to the 2026-08-02 entry:** that scan reported the n=36 bands as 14 🔴 / 13 🟡 / 9 ✅. Recounting the array directly gives **13 🔴 / 14 🟡 / 9 ✅** at n=36 — one post was miscategorised across the 2,500 boundary. The n=37 figures above are counted from the array and supersede it. The 🔴-share trend line is unaffected (67% at n=15 → 45% at n=31 → 36% at n=36 → 38% now).
  **Three findings from this run.**
  **(1) The AI lane's anchor rule is now a hard rule, not a hypothesis.** The 07-28 post locked at 2,402 with a correct contrarian thesis and a calendar year in the hook slot. The two mega-winners in the same lane both named a trending entity inside the first 7 words (Anthropic 92,959; Google/Base44 146,506) — roughly **40x the reach for the same argument with a different anchor**. Combined with the six-post AI-model dead-end (Grok 1,347, Fable5-beach 1,222, MS+Anthropic 1,175, find-skills 792, Master Prompt 546), the lane's shape is fully mapped: **named trending entity + contrarian thesis = ⭐; thesis without an entity = low 2Ks; entity without a thesis = sub-1.5K.** Both halves are required.
  **(2) Craft compliance did not rescue the batch, which points the diagnosis at topic and CTA.** The new 08-03 post is the most rule-compliant draft in weeks — 5-word hook, no "I" opener, a proper "vs." line, odd-numbered list, and the **first post in five with no "not X, it's Y" construction** — and it opened at 1,099 @ 17h, on pace for 🔴. Meanwhile the batch's best performer remains the 07-29 shutdown post (3,464 @ 6d), whose distinguishing feature is subject matter, not execution. **Reading: after three weeks of data the binding constraint on this account is what the posts are about and where they send the reader, not how well they are written.** The 08-03 lock on 08-10 is the clean test — if a fully compliant post still finishes 🔴, that conclusion is confirmed.
  **(3) The origin/exit run finished as the worst-performing consecutive block in the log.** Six straight posts, 07-28 → 08-03, with locked-or-projected finals of **~3.5K / 2,324 / ~830 / ~1.8K / 1,099 / 2,402** — a block median around 2,100, **35% below the log median**, with zero posts clearing the 🟡 floor except the shutdown post, and the block containing the log's soon-to-be 4th-worst post. The only post in the window that is neither an exit-anniversary nor an origin story is also the only one above the median. This is the third consecutive month the same pattern appears (Shopify/DotDev in July, exit story now): **topic concentration, not craft and not cadence, is what caps these blocks.**
  ⚠️ Digest flags: (1) **Contrast-template drift closed the week at n=4** (Messi 07-20, coffee-truck 07-23, shutdown 07-29, AI-thesis 07-28) but the 08-03 post broke the streak — worth telling the agency what changed rather than only what is wrong; (2) **the 08-03 post routes to an off-platform podcast link in the first comment**, a format LinkedIn under-distributes — if podcast promotion continues, the episode's best idea should carry the post on its own and the link should be a footnote, which this draft nearly achieves; (3) **cadence remains healthy** — six posts in seven days, 07-28 → 08-03, with only 08-02 silent; the constraint has stayed on topic selection since 07-28; (4) three 7d locks land in the next four days (07-29 → 08-05, 07-30 → 08-06, 07-31 → 08-07) and the 07-31 republish is expected to enter the bottom-10% band, which will trigger a notification on lock.

- **2026-08-05 scan — 1 FINAL LOCKED, 1 CHECKPOINT LOCKED, 1 NEW POST, BASELINE NOW n=38. Median recovers to 3,255.** Chrome logged in as Lior and Creator Analytics readable; impressions came inline off the activity feed and the two posts past the top-5 cap were back-captured by direct URL.
  **FINAL locked:** **the shutdown post at 3,494 🟡** (7d, locked at 7.7d after the date correction below). **Checkpoint locked:** **08-03 "Don't take advice from me" 1,304 🔴 at the 24h checkpoint** (captured at ~42h — the 24h mark fell between scan runs).
  **Updated final-locked array, n=38:**
  518, 546, 792, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, 2,402, 2,530, 2,562, 2,811, 3,032, 3,224, 3,286, 3,352, 3,374, 3,459, **3,494**, 3,659, 3,777, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, 10,771, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,255** (n=38, mean of positions 19 and 20 = 3,224 and 3,286) — back up from 3,224 at n=37, because the post added this run landed above it. The median has now oscillated 3,255 → 3,224 → 3,255 across three locks, i.e. it is stable and the account's centre of gravity is ~3.2K.
  - Mean: ~10,622 (still dominated by the three ⭐⭐ outliers)
  - **Top 10% threshold: 18,009** (unchanged — top 4 = Google 146,506, Anthropic 92,959, Paperclip 30,009, Birthday 18,009)
  - **Bottom 10% threshold: ≤1,175** (unchanged — bottom 4 = Treat-yourself 518, Master Prompt 546, find-skills 792, MS+Anthropic 1,175). The 07-30 republish (794 @ 5d) locks into this band tomorrow and will displace MS+Anthropic from the bottom four.
  - Band distribution: **🔴 under 2,500 → 14 of 38 (37%)** · **🟡 2,500–4,999 → 15 of 38 (39%)** · **✅ 5,000+ → 9 of 38 (24%)**. 🔴-share trend: 67% at n=15 → 45% at n=31 → 36% at n=36 → 38% at n=37 → 37% now. Flat for three runs.
  **Three findings from this run.**
  **(1) The craft-versus-topic test is close to answered, and topic is winning.** Two data points landed together. The shutdown post — the most completely executed draft of the last month, full Top-12 playbook, documentary personal artifact, open-question close — locked at **3,494**, a mid-🟡 barely above the median. The 08-03 post — the most rule-compliant hook in three weeks — locked its 24h checkpoint at **1,304** and is on pace for 🔴. **Craft sets the floor on this account; it does not set the ceiling.** The ⭐ posts in this log all bought their reach with subject matter (a named trending entity, or a credential with a give-back), never with execution quality.
  **(2) A new failure shape appeared: cold on reach AND cold on network.** Every 🔴 in the 07-28 → 08-03 block carried high reactions on low reach — his own network showed up, strangers did not. The 08-04 focus parable broke that: **9 reactions at 18h**, against 31–53 for every comparable post in the window, on the softest 18h reach in the log. The distinguishing feature of that post is that **the story belongs to a stranger** ("a wealthy friend told me about this founder"). Working hypothesis, now worth testing deliberately: **second-hand parables underperform first-hand operator stories so badly that even his own network disengages.** If the 08-11 lock confirms it, it becomes a hard rule — every story needs Lior's own stake and Lior's own numbers.
  **(3) The topic-concentration cap has now run for eight straight posts.** 07-28 → 08-04, locked or projected: ~3.5K / ~2.4K / ~0.8K / ~1.7K / 2,402 / ~1.7K / ~0.8K. Block median ≈ 1,700, **48% below the log median**, with exactly one post above the median in eight. Seven of the eight are origin, exit-anniversary, credential or focus content — the same three subjects in rotation. This is the third consecutive month the same diagnosis lands: **topic variety, not craft and not cadence, is the binding constraint on this account.**
  ⚠️ Digest flags: (1) **the contrast-template drift stays broken at two posts running** (08-03 and 08-04 both clean) — tell the agency what changed, not only what is wrong; (2) **the 08-04 post shipped without ALT text**, which breaks a standing posting rule and is the second mechanical miss in a week; (3) **the 08-04 self-repost went out ~16h after the original**, roughly double the 6-8h window; (4) **two 7d locks land tomorrow (2026-08-06)** — the "At 21" post at ~2.4K 🔴 and the republish at ~810 🔴, the latter entering the bottom-10% band and triggering a notification; (5) ⚠️ **dates on four entries were one day late and have been corrected in-line** — future scans should decode the activity URN (`id >> 22` = epoch ms) rather than trust LinkedIn's rounded relative age label.

- **2026-08-06 scan — 2 FINALS LOCKED, 1 CHECKPOINT LOCKED, 1 NEW POST, BASELINE NOW n=40. The nine-post 🔴/🟡 block broke, and the credential give-back rule got its matched control.** Chrome logged in as Lior; impressions read inline off the activity feed for recent posts and by direct `/analytics/post-summary/urn:li:activity:...` URL for the two past the feed's render window. Followers **11,662** (+62 since 08-05).
  **FINALS locked:** **"At 21 … Me at 31" 2,393 🔴** (7d, captured at 7.75d — the mark fell after yesterday's scan) and **the 2-year Fiverr anniversary republish 806 🔴 BOMB** (locked at 6.7d, ~6h short of the true mark; tail was +12/24h so the 7d value is 806-812). **Checkpoint locked:** **08-04 focus parable 939 🔴 at 24h**, captured at ~42h.
  **Updated final-locked array, n=40:**
  518, 546, 792, **806**, 1,175, 1,222, 1,347, 1,701, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, **2,393**, 2,402, 2,530, 2,562, 2,811, 3,032, 3,224, 3,286, 3,352, 3,374, 3,459, 3,494, 3,659, 3,777, 4,175, 4,614, 4,686, 5,624, 5,721, 5,825, 10,771, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,128** (n=40, mean of positions 20 and 21 = 3,032 and 3,224) — **down from 3,255**, the sharpest single-run median drop since the n=15 baseline, because both posts locked this run landed in the bottom half and one of them landed in the bottom four.
  - Mean: ~10,171 (still dominated by the three ⭐⭐ outliers)
  - **Top 10% threshold: 18,009** (unchanged — top 4 = Google 146,506, Anthropic 92,959, Paperclip 30,009, Birthday 18,009)
  - **Bottom 10% threshold: ≤806** — **changed.** The republish enters the bottom four (Treat-yourself 518, Master Prompt 546, find-skills 792, republish 806) and **displaces MS+Anthropic 1,175**, exactly as the 08-05 scan projected.
  - Band distribution: **🔴 under 2,500 → 16 of 40 (40%)** · **🟡 2,500-4,999 → 15 of 40 (37%)** · **✅ 5,000+ → 9 of 40 (23%)**. 🔴-share trend: 67% at n=15 → 45% at n=31 → 36% at n=36 → 38% at n=37 → 37% at n=38 → **40% now — the first increase in the trend line.**
  **Three findings from this run.**
  **(1) The credential-milestone rule now has a matched control, and the give-back is the whole variable.** Two posts, same account, same audience, seven days apart, same credential anchor: **"At 21 … Me at 31" — the scoreboard with no lesson — locked 2,393 with 0 followers gained. "At 28, I sold my business to Fiverr" — the same credential plus 7 lessons handed to the reader — is at 5,412 impressions, 4 followers and 93 profile viewers in 17 hours.** That is **~2.3x the reach at a fraction of the age**, with the give-back as the only structural difference. It replicates the Birthday post (18,009 ⭐, credential + 10 lessons) against a control the log did not have before. **Promote to a hard rule: the credential-milestone lane travels on what the milestone teaches, never on the milestone itself. A scoreboard post is a first-degree post; a give-back post is a distribution post.**
  **(2) The craft-versus-topic question is answered in both directions, and the answer is structural.** The 08-03 post — the most rule-compliant draft in three weeks — refreshed at 1,357 with engagement frozen and is going to lock 🔴; craft compliance did not rescue it. The 08-05 post cleared 5K in 17 hours **without** a trending news anchor, a contrarian thesis or an off-platform CTA, and it is still exit-anniversary content, i.e. the same saturated topic as the nine posts before it. **Reading: craft sets the floor, and what buys reach back inside a saturated topic is not a new subject but a give-back structure — something the reader can take away and keep.** Saves track this cleanly: 8 saves at 17h on the new post against 0-2 for everything else in the block.
  **(3) The borrowed-story failure is now the sharpest single-variable result in the log after the republish.** The 08-04 parable locked its 24h checkpoint at **939** with 12 reactions, 2 profile viewers and 0 followers — cold on reach *and* cold on network, a failure shape that appears nowhere else. Its thesis is identical to the 07-28 shutdown post's, which did **3,494** with the same argument told as Lior's own decision over his own dissolution letter. **~3x on identical subject matter, separated only by whose story it is.** Confirm at the 08-11 lock and promote: every story needs Lior's own stake and Lior's own numbers.
  ⚠️ Digest flags: (1) **the "not X, it's Y" contrast drift stays broken at four posts running** (08-03, 08-04, 08-05, and the 08-05 self-repost) — after an n=4 run of violations in July this is a real correction and the agency should be told what changed, not only what is wrong; (2) **the self-repost is going out ~16h after the original for the second run in a row**, roughly double the 6-8h rule — the single cheapest mechanical fix available; (3) the 08-04 parable shipped **without ALT text**, the second mechanical miss in a week; (4) **cadence is healthy** — posts on 08-03, 08-04, 08-05 and a self-repost on 08-06, with a small gap only on 08-02; (5) **eleven consecutive posts now draw on Lior's own origin/exit/focus story** — the 08-05 result narrows but does not close the topic-concentration flag, since it shows the structure can be fixed without changing the subject; (6) three 7d locks land in the next five days: 07-31 origin post → 08-07 at ~1,650 🔴, 08-03 → 08-10 at ~1,500 🔴, 08-04 parable → 08-11 at ~1,100 🔴, with the 08-05 post's 7d falling 08-12; (7) ⚠️ **the entry headers for the 07-29/07-30/07-31 posts still carry dates one day later than their URN-decoded publish times** — the true dates are recorded inside each entry and in the header verdicts, and future scans should keep decoding `id >> 22` = epoch ms rather than trusting LinkedIn's rounded relative age label; (8) six older posts show post-FINAL drift on this scan (Messi 10,811 vs locked 10,771; DotDev-learnings 4,077 vs 3,777; Shopify-affiliate 5,910 vs 5,624; trainer 3,425 vs 3,286; AutoDS-connectors 2,937 vs 2,811; coffee-truck 2,635 vs 2,562) — **locked values stand**, but the drift runs 1-8% and is worth remembering when comparing a fresh in-flight number against an old locked one.



**What's worked best (so far, updated 2026-05-31):**
1. **2026-05-27 Google/Base44-killer / "narrow the niche"** — **146,506 imp ⭐⭐⭐ ALL-TIME RECORD (7d FINAL LOCKED 2026-06-04)** (trending-tool news anchor + founder-fear-mirror + "narrow the niche" contrarian defense; surpasses Anthropic by ~58%)
2. **2026-05-10 Anthropic / MD→HTML workflow** — **92,959 impressions ⭐⭐** (trending-tool insider scoop + tribe-callout + 3 prompts + meta-principle close)
3. 2026-04-20 Paperclip / zero-human-company — 30,009 impressions ⭐ (contrarian take on trending tool)
4. **2026-05-24 Birthday "31 / 10 lessons"** — **18,009 impressions ⭐ EXCEPTIONAL (7d FINAL LOCKED)** (first non-AI ⭐-lane post; credential-anchored milestone listicle; reach-capped after 24h)
5. **2026-05-28 Tough-days-Israeli-tech / "DMs are open"** — **14,798 imp ✅⭐ EXCEPTIONAL (7d FINAL LOCKED 2026-06-06, top-10% of Lior's posts)** (layoff-empathy hook + named casualties + value-first hiring CTA; 15 reposts = log's most-shared post; first EXCEPTIONAL in the market-empathy lane)
6. **2026-06-04 "900 prompts" vibe-coding** — **5,825 impressions ✅ (7d FINAL LOCKED 2026-06-11)** (comedic caption-only-hook + payoff-in-visual; first ✅ on pure relatability, no news anchor / no thesis / no credential; reach-led, thin engagement — new repeatable reach format)
7. **2026-05-06 Founder Salary trap** — 4,614 impressions 🟡 (setup-twist hook + topic novelty / unprecedented in log)
7. **2026-05-18 Funnel-conversion 40% / Shopify partner thanks** — 3,352 impressions 🟡 (proof/case-study; 9 reshares is the lane signature)
8. 2026-04-20 Wim Hof / cold feet — 2,662 impressions @ 11d, 60 likes, 12 comments (personal vulnerability — best engagement rate, only post with sustained long-tail growth)

**What's flopped (so far, updated 2026-06-02):**
1. **2026-05-14 "Treat yourself like a product"** — **518 impressions 🔴 WORST (7d FINAL locked)** (wellness post without founder-bridge; rule confirmed)
2. **2026-05-12 Master Prompt / 5-step playbook** — **546 impressions 🔴 FINAL** (tactical AI-use playbook without news anchor — confirms creator-lane productivity tips bomb)
3. 2026-04-30 find-skills — 792 impressions 🔴 BOMBED
3a. **2026-07-30 Fiverr 2-year anniversary REPUBLISH** — **806 impressions 🔴 BOMB (7d FINAL locked 2026-08-06)** — near-verbatim republish of a post that did 200K+; ~250x collapse with copy, author and account held constant. Highest engagement rate in the log (7.4%) on the 4th-lowest reach = duplicate-content suppression. **A proven post is a proven TEMPLATE, never a proven TEXT.**
3b. **2026-05-26 Microsoft+Anthropic agents workshop** — **1,175 impressions 🔴 BOMBED (7d FINAL locked 2026-06-02)** (AI-trending hook naming Microsoft + Anthropic, but tactical-prescription/infra-checklist body — confirms the AI lane bombs without a contrarian commentary frame)
4. 2026-04-13 10-80-10 rule — 1,701 impressions
5. 2026-04-13 70% rule carousel — 1,783 impressions
6. 2026-04-28 Wim Hof sequel "5 days taught me" — 1,892 impressions 🔴
7. 2026-04-28 "I got rejected" / Director of Partnerships — 2,066 impressions
8. 2026-04-24 Modball partnership — 2,070 impressions
9. **2026-05-21 CEO-job-in-3-rules** — **2,083 impressions 🔴 FINAL** (reductive-list opener without operator scene = 4th confirmation)

**Pattern hypothesis (n=14, strengthened):**
- **The contrarian-AI-trending-tool lane is now confirmed repeatable across THREE sub-frames.** Paperclip 30K (failure-report) + Anthropic 92K (insider-workflow) + Google/Base44-killer (in-flight 22K @ 17h ⭐⭐ — founder-fear-mirror) = three ⭐-tier posts in three distinct sub-lanes. Common DNA: trending tool name in first 7-11 words + contrarian or proprietary frame + no productivity-tip body + minimal/no CTA.
- **Tactical AI-use tips bomb.** Master Prompt (546) + find-skills (792) + Microsoft+Anthropic-agents-workshop (887 @ 24h, tracking 🔴) — all in AI lane but tactical-prescription, not topical commentary. **The lane works only with a news anchor AND a commentary frame, never with tactical prescriptions or productivity tips.**
- **Reductive-list opener without operator scene = 4-time confirmed BOMB.** 70% rule (1,783), 10-80-10 (1,701), Master Prompt (546), CEO-3-rules (2,083). Force a specific scene/number/AutoDS moment into the body or skip the format.
- **Wellness/personal posts need an operator-stake bridge.** Treat-yourself (518) confirmed 3rd flop.
- **Setup-twist hook holds.** Founder Salary trap 🟡 (4,614) + Coffee/100-videos pending. Strong sub-pattern.
- **Credential-anchored milestone lane is now a CONFIRMED separate ⭐ lane (7d FINAL).** Birthday "31 / 10 lessons" locked at **18,009 ⭐ EXCEPTIONAL** — first non-AI ⭐ ever. DNA: credential hook (Fiverr exit / Forbes 30u30) + occasion (birthday) + 10 punchy save-card lines + humble give-back close, no CTA. Reach-caps in the high-teens-thousand range (vs 30K+ for contrarian-AI), but a decisive, repeatable ⭐.
- **Hiring CTAs work IF value is delivered in full FIRST (n=1, in-flight).** Tough-days-Israeli-tech (13,400 @ ~2.5d, 15 reposts) pairs a layoff-empathy post with "my DMs are open" — and it's the most-reshared post in the log. The opposite of "I got rejected" 🔴 (bait-and-switch: promised a story, delivered a job listing). **Rule: the hiring ask must read as a gift/offer of help layered onto a complete value post, never as the payload the hook baited.**
- **The contrarian-AI lane keeps raising its own ceiling.** Paperclip 30K → Anthropic 93K → Google/Base44 144K-and-climbing. Each iteration higher. The Google post's active ingredient appears to be the personal-stake news anchor + founder-fear-mirror, not just the trending-tool name.


- **2026-08-29 scan — 20-DAY OUTAGE CLOSED. 12 FINALS LOCKED, 3 IN-FLIGHT, BASELINE NOW n=52, AND THE ACCOUNT'S 3rd-BIGGEST POST EVER IS RUNNING.** No scan ran between 2026-08-10 and 2026-08-28 (Mac asleep / app closed — see Scan Issues). Chrome was logged in as Lior this run and Creator Analytics was fully readable. Method: post list and lifetime impressions from `/analytics/creator/top-posts/?metricType=IMPRESSIONS&timeRange=past_28_days`, publish times by URN decoding (`id >> 22` = epoch ms), per-post saves / sends / profile viewers / **followers gained** from `/analytics/post-summary/urn:li:activity:{id}/`. ⚠️ **Two transient Chrome-extension disconnects and one stale-render fault** (the analytics SPA served the previous post's numbers on a 3s wait); every reading below was re-verified with `location.pathname` echoed alongside the metrics and cross-checked against the top-posts list. **Followers 12,698** (+1,036 since 11,662 on 2026-08-06).

  **Updated final-locked array, n=52:**
  518, 546, **687**, 792, 806, **1,084**, **1,174**, 1,175, 1,222, 1,347, **1,428**, 1,701, **1,713**, 1,783, 1,784, 1,892, 2,066, 2,070, 2,083, 2,393, 2,402, 2,530, 2,562, 2,811, 3,032, 3,224, 3,286, **3,340**, 3,352, 3,374, 3,459, 3,494, 3,659, 3,777, 4,175, **4,581**, 4,614, 4,686, **4,828**, 5,624, 5,721, 5,825, **8,253**, **8,361**, **9,818**, 10,771, **11,422**, 14,798, 18,009, 30,009, 92,959, 146,506
  - **Median impressions: 3,255** (n=52, mean of positions 26 and 27 = 3,224 and 3,286) — **up from 3,128** at n=40. The twelve posts added split 5 below / 7 above the old median, and the top of the new cohort is much stronger than anything July produced.
  - Mean: ~8,914 (down from 10,171 — the outliers are being diluted by a denser body of work, which is a healthy direction)
  - **Top 10% threshold: 14,798** — **changed**, up from 18,009. Top five = Google 146,506, Anthropic 92,959, Paperclip 30,009, Birthday 18,009, Tough-days 14,798.
  - **Bottom 10% threshold: ≤806** — unchanged in value, but the membership changed: Treat-yourself 518, Master Prompt 546, **Jim Rohn 687 (new)**, find-skills 792, republish 806.
  - Band distribution: **🔴 under 2,500 → 21 of 52 (40%)** · **🟡 2,500-4,999 → 18 of 52 (35%)** · **✅ 5,000+ → 13 of 52 (25%)**. 🔴-share trend: 67% at n=15 → 45% at n=31 → 36% at n=36 → 38% at n=37 → 37% at n=38 → 40% at n=40 → **40% now.** Flat for three runs; the account is not getting worse, it is getting more bimodal.

  **FOLLOWER KPI — first full reading since the 2026-08-23 change.**
  - **Total followers 12,698.** Net new in the last 7 days (Aug 23-29, Creator Analytics cumulative chart): **815**. Net new since the 08-06 scan (23 days): **+1,036**. August month-to-date is tracking **~1,150-1,200**, against a 963/month baseline and the proposed Q4 ladder of 1,400 / 1,800 / 2,200.
  - **The month was made by one post.** Of the ~1,036 followers added since 08-06, the 08-25 exit-deck post is directly credited with **86**, and the 815-follower week is the week it ran. Every other post in the block combined contributed **28**.
  - **Followers gained per 1,000 impressions, August block (the number to manage by):**

  | Date | Post | Imp | Followers | per 1K |
  |------|------|-----|-----------|--------|
  | 08-25 | exit deck (ungated artifact) | 66,524 | **86** | 1.29 |
  | 08-12 | Galit / dental school | 8,253 | **14** | **1.70** |
  | 08-16 | EA hiring | 9,818 | 5 | 0.51 |
  | 08-11 | Anthropic watermarks | 8,361 | 4 | 0.48 |
  | 08-26 | Claude model tree | 6,271 | 2 | 0.32 |
  | 08-13 | travel / lifting | 3,340 | 2 | 0.60 |
  | 08-10 | Jim Rohn / "they ask" | 687 | 1 | 1.46 |
  | 08-27 | SaaS steps | 1,124 | 1 | 0.89 |
  | 08-17 | watermark explainer | 1,428 | **0** | 0.00 |
  | 08-18 | 100K IG followers | 4,828 | **0** | 0.00 |
  | 08-20 | founder stations | 1,084 | **0** | 0.00 |

  **Five findings from this run.**

  **(1) The save-first artifact thesis is confirmed, and it is now the account's best follower engine by an order of magnitude.** The 08-25 exit deck: 66,524 impressions, **167 saves**, 1,179 profile viewers, **86 followers**. Saves were previously a 0-8 metric on this account; 167 is a different regime. The A/B recorded in memory (identical copy: comment-gated 55 imp, ungated 23,111) is settled — the ungated version is at 66,524 and still climbing. The 08-05 give-back listicle locking at **11,422** (up from a projected 9.5-10.3K) puts the same structure at #7 in the log. **Two of the top seven results are now give-back/artifact posts, and the structure did not exist in the account four weeks ago.**

  **(2) Reach and follower conversion are genuinely decoupled — the KPI change was correct, and here is the matched pair.** 08-11 watermark newsjack: 8,361 imp, 87 comments, **4 followers**. 08-12 Galit milestone: 8,253 imp, 31 comments, **14 followers**. Reach parity to within 1%, one week apart, same account. The newsjack won comments 87-to-31; the personal post won followers **3.5x**. Comment volume is not subscription intent. **"Teach me in the comments" is a proven comment lever and a disproven follower lever** — it belongs in the 10% reach-play budget.

  **(3) Newsjacks are day-one assets. The follow-up loses ~6x.** 08-11 watermark newsjack 8,361 → 08-17 watermark explainer **1,428**, same topic, six days apart, same account. And the explainer's body is a mechanism walkthrough, which extends the AI-tactical-explainer bomb list to **n≈7** (Grok 1,347, Fable5-beach 1,222, MS+Anthropic 1,175, find-skills 792, Master Prompt 546, watermark explainer 1,428). The 2026-08-23 spine recommendation — **operator verdict, never explanation** — is the correct correction and this is its cleanest supporting pair.

  **(4) Packaging sets the ceiling, not substance.** 08-27 "THE ACTUAL STEPS TO GROW A SaaS COMPANY" carries real AutoDS product decisions and the Build Your Store origin — genuinely operator-seat material — and did **1,124**, two days after a 66K post. Its hook is all-caps and its body is a ☑️ emoji manifest: the Chris Donnelly / Jasmin Alić lead-magnet layer the vault banned on 2026-08-23. Same standing as the exit deck, opposite presentation, **~59x less reach.**

  **(5) The borrowed-story rule is now unanimous at n=3, and the reductive-list bomb is at n=5.** Borrowed stories: Jim Rohn 687, wealthy-friend parable 1,174 (final), Treat-yourself 518 — all cold on reach *and* cold on network, a failure shape that appears nowhere else. Reductive-list opener with no operator scene: 70% rule 1,783, 10-80-10 1,701, Master Prompt 546, CEO-3-rules 2,083, founder-stations 1,084. Five months, zero exceptions. Treat both as absolute.

  **⚠️ Four flags for the Monday digest.**
  - **"Not X, it's Y" drift has resumed.** 08-26: "It's not (only) about your prompt. It's the model you keep defaulting to." Per the 2026-08-24 platform note this construction is reportedly auto-suppressed as AI slop, so this is now a distribution rule, not a taste rule. Raise with the agency.
  - **Team-size copy contradicts the vault rule.** The 08-16 hiring post says "200 employees" and Lior's live profile headline says "200+ employees"; CLAUDE.md used to say 250. ✅ SETTLED 2026-08-30: Reut confirmed 200 is correct; CLAUDE.md and memory were updated.
  - **The $92M figure is now in the hook of the account's 3rd-biggest post ever.** Fiverr's 20-F states $55.658M plus up to $36M earn-out. Standing exposure, newly maximised visibility.
  - **Cadence is erratic and it is costing slots.** August published on 10, 11, 12, 13, 16, 17, 18, 20, 25, 26, 27 — with a **four-day silence 08-21 → 08-24** immediately before the breakout, and nothing on 08-28. Against the 3/week Sept → 5/week Q4 ramp, the problem is no longer volume, it is rhythm: there is still no fixed-day signature series.

  **Next locks:** 08-25 exit deck **2026-09-01** (projecting 70-80K, would be the 3rd-highest final ever), 08-26 model tree 2026-09-02 (projecting ~6.5-7K ✅), 08-27 SaaS steps 2026-09-03 (projecting ~1.2-1.3K 🔴).

---

## Monthly Synthesis

<!-- At end of each month, append:
### {Month YYYY}
**Posts published:** {N}
**Avg engagement:** {vs previous month}
**Best-performing pattern:** {hook + structure + visual combo}
**Worst-performing pattern:** {same format}
**Proposed style guide updates:** {bullets — require approval before merging}
-->

_Empty — first synthesis after month 1._
