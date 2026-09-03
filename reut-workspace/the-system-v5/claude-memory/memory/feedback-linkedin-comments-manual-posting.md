# LinkedIn + X + TikTok/IG posting: NEVER auto-post — Reut posts manually

**Hard rule (LinkedIn 2026-06-10, extended to X 2026-06-11, extended to TikTok/all-platform posts 2026-07-07):** On LinkedIn, X, TikTok, and Instagram, never publish/submit posts, comments, or replies automatically, even after Reut says "מאשר"/"approved". Approval means she approves the DRAFT, not that I should post it. This includes creating scheduled posts or drafts in Metricool on her behalf — on 2026-07-07 I created a draft TikTok post in Metricool (video + caption) and she stopped me: "אני לא רוצה שתפרסם בלעדי, רק תכין לי את הקובץ ואני אפרסם". Deliverable = the media file + caption text; she handles Metricool/upload herself.

Deliverable for any "comment/reply" request on these platforms = **plain-text copy-paste draft + link to the post**. Reut copies and posts herself.

- Applies to comments AND replies on LinkedIn and X.
- "מאשר" / "approved" = approve the draft wording, NOT a green light to post.
- X enforcement (2026-06-11): all 15 `scout-reply-x-*` scheduled tasks disabled; `x-reply-canary` (which would auto re-enable them) disabled; `/scout-replies` skill switched to draft-only. `x-daily-reply-posts` (draft-only digest) stays on — that IS the manual workflow.
- Bluesky (updated 2026-07-09): all `scout-reply-01..10` auto-reply tasks DISABLED per Reut — "the only thing I want on Bluesky is mirroring the X posts". The `bluesky-mirror` task is the ONLY thing that auto-posts to Bluesky. Do not re-enable Bluesky auto-replies.
- Background: on 2026-06-10 I auto-posted 3 LinkedIn comments after "מאשר"; on 2026-06-11 Reut said "אל תגיב אוטומטית יותר באיקס" — she wants to reply manually. Don't repeat.
