---
name: X Success Metric — Bookmarks Weighted 3x
description: Bookmarks signal high-intent engagement on X. Weight 3x in x-analyst ingest. Likes are vanity; bookmarks predict deal flow and follower growth.
type: feedback
originSessionId: d1e3a08e-5052-4b9e-bfd6-a474226bc44b
---
When ranking which X posts "won" the week, bookmarks beat likes every time.

**Weighting (apply in x-analyst-daily and x-analyst-weekly):**
- Bookmarks: ×3
- Replies: ×2
- Reposts: ×2
- Likes: ×1
- Views: context only, not score

A post with 50 bookmarks + 200 likes outranks a post with 10 bookmarks + 800 likes.

**Why:** Wiz of Ecom system (2026-05-01, 147K views) — bookmarks signal someone wants to come back, save the idea, or send it to a teammate. That's the highest-intent action on X short of a DM. Likes are reflex; bookmarks predict the audience that converts to inbound DMs and deal flow. For Lior (founder personal brand, not entertainment), bookmarks are the leading indicator that operator/SaaS-CEO peers are paying attention.

**How to apply:**
- Update `fetch_post_performance.py` to surface bookmarks as a top-line column.
- x-analyst-weekly's "winning topics/perspectives/vehicles" report should rank by the weighted score above, not raw likes.
- Reut's weekly review should ask "which post got the most bookmarks?" before "which got the most likes?"
- If a post hits high likes but low bookmarks, it was entertaining but not useful — don't double down on that pattern.
