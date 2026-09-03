---
name: project-bluesky-mirror-pipeline
description: Auto-mirror of agency X posts to Bluesky AND Threads as lightly-refreshed (non-identical) versions
metadata: 
  node_type: memory
  type: project
  originSessionId: eb2e0ecc-b95e-412c-8b77-47051e86a6d5
  modified: 2026-08-02T09:55:52.703Z
---

Built 2026-06-09. The external agency publishes original posts to X (@lior_pozin) but does NOT want identical text on Bluesky. This pipeline auto-detects each new agency X post and publishes a lightly-REFRESHED (non-identical) version to Bluesky only.

**Decision:** fully automatic (no approval gate) + "light refresh" (same idea/numbers, new opener + reworded, ≤300 chars). Chosen by Reut.

**Long-post handling (>300 chars) — UPDATED 2026-06-14: ALWAYS ONE ≤300 post.** Reut switched posting to Metricool (Bluesky-only), and the Metricool poster does single posts only (no native thread). So condense/edit every long X post (incl. threads) down to ONE tight ≤300 post, dropping the weakest supporting points if a manifesto/thread won't fit. The earlier "smart hybrid → native Bluesky thread" path is retired for the standing pipeline.

**POSTING = Metricool, two networks (UPDATED 2026-06-23: added Threads).** As of 2026-06-23 the mirror publishes the SAME ≤300-char refreshed text to BOTH Bluesky and Threads, each via a separate Metricool call: `post_bluesky_metricool.py` then `post_threads_metricool.py`. Threads was chosen via Metricool (not Meta Graph API) because Metricool already holds the Threads connection for the "Lior Pozin" blog (`networksData.threadsData='lior'`) — no Meta token needed. Verified the Threads provider works by posting a `--draft` first. Kept the two calls separate (not one combined providers array) so the proven Bluesky path is untouched and Threads is purely additive; mark after Bluesky success even if Threads fails (re-run would double-post Bluesky). GOTCHA: the older `post_social.py` posts to BOTH X and Bluesky — never use it for a mirror (it would re-post to X). `post_bluesky_metricool.py` sets `providers=[{"network":"bluesky"}]`, `post_threads_metricool.py` sets `[{"network":"threads"}]` (500-char cap). No-arg schedule = publishes ~2 min from now; pass an ISO datetime/`HH:MM` to schedule.

**AGENCY PUBLISHING STACK (confirmed by Reut 2026-06-23):** the external agency publishes via **Hypefury for X** and **Taplio for LinkedIn**. This does NOT affect the mirror — detection reads the live x.com profile regardless of which tool published, so Hypefury posts are caught normally. Note: Hypefury often adds auto-retweets / auto-plug replies; these are already filtered by the mirror's skip rules (skip reposts + posts starting with "@"). Taplio/LinkedIn is irrelevant to this pipeline (separate LinkedIn workstream).

**DETECTION = Grok x_search, headless (UPDATED 2026-08-02 — Chrome is GONE).** Metricool was ruled out 2026-06-09: it lags 1-2 days on posts made DIRECTLY on X and exposes zero thread metadata. Detection then ran through the Chrome MCP for ~2 months, which forced the task to stay local and made it fail whenever Chrome was closed or logged out. As of 2026-08-02 the whole detect+dedup flow is ONE headless call: `mirror_x_to_bluesky.py fetch-candidates --days 2` (Grok x_search, needs `XAI_API_KEY`). It internally drops reposts/replies-to-others, applies the state log, runs the live Bluesky twin-guard (auto-marking twins), and merges consecutive self-replies into one `text`. The SKILL.md now forbids opening any browser. Empty array = nothing to do.

**IMAGE-ONLY TEASERS must be skipped (learned 2026-08-02).** Some agency posts carry their real content in attached screenshots, e.g. the Jul 31 PMF post whose text was only "I left a very long reply in the comments 👇". `fetch-candidates` returns them because the text is technically original, but there is nothing to mirror without the image. Judgment call: `mark` them so they stop resurfacing every run, and report as an image-only skip.

**X THREADS:** an X thread = N separate tweets (each its own tweet_id), continuation tweets are self-replies. The mirror reads all consecutive @lior_pozin self-replies in order, then condenses to a tight 2-3 post Bluesky thread (smart hybrid), NOT a 1:1 mirror. First real run (2026-06-09): mirrored Lior's "bootstrapped → sold to Fiverr at 28" origin-story thread (8 X tweets → 3 Bluesky posts).

**How it works (detection via Chrome, posting via AT Protocol — no new API access):**
- `T-tools/01-skills/scripts/mirror_x_to_bluesky.py` — `mark <tweet_id>`, `is-mirrored <tweet_id>` (state-log gate), `bluesky-recent --limit N` (real-time recent Bluesky texts via atproto, used to skip scout/post_social cross-posts already on Bluesky), plus fallback `list-pending`/`bootstrap` (Metricool). State log: `O-output/bluesky-mirror-log.json` by tweet_id.
- `T-tools/01-skills/scripts/post_bluesky_metricool.py` — CURRENT poster (since 2026-06-14). Schedules a Bluesky-ONLY post via Metricool (provider=bluesky, METRICOOL_TOKEN). `arg1`=text (errors if >300), optional `arg2`=ISO datetime or `HH:MM` (default +2 min). Single post only.
- `T-tools/01-skills/scripts/post_bluesky.py` — LEGACY direct-atproto poster (BSKY_HANDLE/BSKY_APP_PASSWORD). Supports native threads (N args). No longer the default; kept for manual/thread use.
- **Cloud-routine migration (in progress 2026-08-02).** The old "must stay local" reason (Chrome) is dead — detection is headless now, the repo `reut-amariyo/claude_code` is on GitHub, and the state log is git-tracked, so a cloud routine is technically viable. ONE blocker remains: the cloud environment needs `METRICOOL_TOKEN`, `BSKY_HANDLE`, `BSKY_APP_PASSWORD`, `XAI_API_KEY`, which today live only in Reut's local `~/.zshrc`. Only Reut can add those to the cloud env. Two hard requirements when it moves: (1) the cloud run MUST commit+push `bluesky-mirror-log.json` or the next run re-mirrors everything; (2) the LOCAL `bluesky-mirror` task must be DISABLED at the same time, or local and cloud diverge on the state log and double-post.
- **Why this matters:** the local task only fires while the Mac is awake AND the Claude app is open. It went silent 114h over the weekend of 2026-07-28→08-02 for exactly that reason. The downtime alert can't help, since nothing runs to send it until the Mac wakes up.
- State log: `O-output/bluesky-mirror-log.json` keyed by tweet_id.
- Skill/command: `/bluesky-mirror`. Scheduled task `bluesky-mirror` runs cron `0 8-22/2 * * *` (every 2h, 08:00–22:00).

**Two dedup safety nets (both required):**
1. tweet_id state log — never mirror the same post twice (needed because the Bluesky version is REWRITTEN, so text won't match on re-check).
2. Live Bluesky-twin check — skips any X post that already has a near-identical Bluesky post. This is what prevents double-posting of scout/Reut posts made via `post_social.py` (which already hit both networks).

**Limitations:** Metricool sync lag means "shortly after" (~15min–2h), not instant. Media/images are NOT carried to Bluesky (text only). For truly instant, would need direct X API. Was bootstrapped with 145 existing posts so history isn't back-filled.

Related: [[feedback-post-social-no-help-flag]], [[feedback-bluesky-reply-sequential-not-parallel]], [[feedback-metricool-replies-untracked]].
