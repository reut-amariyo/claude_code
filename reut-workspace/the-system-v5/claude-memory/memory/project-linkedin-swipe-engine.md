---
name: project-linkedin-swipe-engine
description: Bright Data harvests ~92 top LinkedIn creators daily at 08:00, ranks the 72h window vs each creator's median, Claude writes donor-structure teardowns for Lior posts
metadata:
  type: project
---

Started 2026-09-06 as a manual second-profile plan; rebuilt 2026-09-20 on **Bright Data**
(Reut: "defaults on everything"). The second LinkedIn profile plan is DROPPED. This is the
industrialised version of [[feedback-build-on-proven-structures]].

**Everything lives in** `reut-workspace/the-system-v5/O-output/linkedin-swipe-engine/`
- `scripts/harvest.py` — modes `probe` / `backfill N` / `daily` / `report` / `merge <snapshot>`
- `data/creators.json` — 103 creators with resolved slugs; `harvestable:false` on 11 whose
  activity is hidden from logged-out view (Armand Ruiz, Marily Nika, Katelyn Bourgoin,
  Luke Matthews, Sabrina Ramonov, Liam Ottley, Sahar Mor, Sabri Suby, Charlie Hills,
  Mustafa Suleyman, Barsee). No scraper without a login can read them.
- `data/posts.jsonl` — one line per post with a metrics snapshot per day (1,087 posts
  backfilled 2026-09-20, 15 per creator); `data/baselines.json` medians; `data/lior-fit.json`
  is Claude's ✅/⚠️/❌ per post URL; `data/raw/` gitignored snapshots
- `daily-reports/YYYY-MM-DD-report.md` — section 1 by script, sections 2-5 by Claude
- `02-report-spec.md` has the v2 scoring note; `00-setup-guide.md` is marked superseded

**Schedule:** desktop-app scheduled task `linkedin-swipe-daily`, cron `0 8 * * *` local.
Runs only while the Claude desktop app is open on Reut's Mac; a missed run fires on next
launch. Chosen over a cloud routine because a cloud commit every morning would conflict
with Reut's local vault and daily backup commits.

**Bright Data facts (verified 2026-09-20):**
- Key at `~/.config/brightdata/api_key` (never in chat, never in the vault). Account had
  5,000 free credits; first "Customer is not active" error cleared itself once Reut opened
  the dashboard.
- Dataset `gd_lyy3tktm25m4avu764` "LinkedIn posts", `type=discover_new&discover_by=profile_url`,
  `limit_per_input=5` daily. ~2-6 min per job. Returns likes, comments, text, media, doc page
  count, author followers, top comments. **No repost count.** Join key is
  `discovery_input.url`; error records carry `input.url` instead. Post URL slug ≠ creator slug
  means the creator reposted someone else (33% of records), excluded from scoring.
- "No posts found for this profile" is deterministic = activity hidden, not a retry case.
  Profile dataset `gd_l1viktl72bvl7bjuj0` gives name + followers to check a slug cheaply.
- Post text can contain U+2028; never `splitlines()` the JSONL.

**Scoring:** `score = comments x3 + likes x1`, `final = score x min(post/median, 10)`;
multiplier only if 100+ likes or 20+ comments; median needs 5+ posts aged 24h+.
Impressions excluded per [[feedback-linkedin-kpi-followers-not-impressions]].

**Hard rules:**
- 🛑 Claude never posts, follows, or clicks on LinkedIn. Reading via Bright Data only.
- The Hebrew top-5 in chat must carry each post's full URL on its own line (Reut asked
  for clickable links, 2026-09-20).
- Teardown-only daily; Lior drafts on request. Structure only, never the donor's wording.
- 🚫 **Alex Hormozi is barred as a donor** (Reut, 2026-09-20, "אל תיתן לי את אלכס הורמוזי"),
  tracked for data only, never a teardown, never in the Hebrew top-5.
- Donor moratoriums apply: Ruben Hassid and Amber Spears tracked, barred
  ([[feedback-diversify-inspiration-creators]]). Quote cards / aphorisms that win reach
  but no followers are skipped as donors and noted in "pattern of the day".
- Never run the Bright Data job more than twice a day.
- 🚫 Gary Vaynerchuk barred as a donor too (Reut 2026-09-21), `donor: red`.
- Bright Data has NO keyword/topic discovery for LinkedIn posts (docs verified 2026-09-21: only
  collect-by-URL, discover-by-profile-url, discover-by-company-url, discover-by-url). The engine can only
  read creators we name, so "what's trending in AI" is bounded by the creator list. The AI save-content
  creators (Armand Ruiz, Sabrina Ramonov, Liam Ottley, Sahar Mor, Barsee, Luke Matthews...) are exactly the
  hidden ones. `download()` now retries while the snapshot endpoint still says "building" (crash 2026-09-21).

**Day-1 finding (2026-09-20):** three independent top-20 posts were first-party artifacts
with under 60 words of body text (Denk's 2022 CTO email x7, Partaker's "book page" photo
x3.2, Matt Gray's 7-page scorecard). Third external confirmation of
[[lior-post-exit-deck-lead-magnet]]. New visual family to try: the photographed book page.
