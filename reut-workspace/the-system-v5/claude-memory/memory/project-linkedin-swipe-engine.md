---
name: project-linkedin-swipe-engine
description: Dedicated LinkedIn research profile following 100 top AI + general creators, harvested daily into a ranked donor-structure report for Lior posts
metadata:
  type: project
---

Started 2026-09-06. Reut is creating a SECOND LinkedIn profile on a new Gmail, whose feed
is 100% the 100 best AI-niche and general LinkedIn creators. Every day the top-performing
posts get harvested, ranked, and torn down into donor structures for Lior posts. This is
the industrialised version of [[feedback-build-on-proven-structures]].

**Everything lives in** `reut-workspace/the-system-v5/O-output/linkedin-swipe-engine/`
- `00-setup-guide.md` — account creation, warm-up schedule, daily harvest ritual
- `01-creators-100.md` — the list, 60 AI / 40 general, split into 3 follow waves
- `02-report-spec.md` — scoring formula and report structure
- `creator-baselines.md` — median engagement per creator, built over 3 weeks
- `inbox/` — Reut drops `YYYY-MM-DD-harvest.md` here
- `daily-reports/` — Claude writes `YYYY-MM-DD-report.md` here

**Scoring:** `(reposts x4) + (comments x2) + (reactions x1)`, then multiplied by
this-post / that-creator's-median. Impressions excluded, not visible on others' posts
and not the KPI. Reposts weighted highest because they buy outside distribution.

**Hard rules for this project:**
- 🛑 Claude NEVER logs in, follows, installs, or clicks anything. Reut does every action
  herself so LinkedIn does not see automation. Claude produces copy-paste material only.
- The research account never posts. It reads.
- Tooling is AuthoredUp, which Reut already has. It shows inline engagement while
  browsing and saves posts to collections, but it does NOT track other creators
  overnight, so the harvest is a 5-minute manual pass by Reut. Taplio's post database
  is the optional upgrade that automates it, and it must never be connected to the
  new LinkedIn account, search-only use.
- Risk flagged and accepted by Reut on 2026-09-06: a second profile violates LinkedIn's
  one-account rule and can link back to her main account. Warm-up pacing in the setup
  guide is the mitigation. Never bulk-paste profile URLs, always search-then-follow.
- Donor moratoriums still apply to the output: Ruben Hassid and Amber Spears stay on the
  follow list for data but are barred as donor structures.
  See [[feedback-diversify-inspiration-creators]].
