---
name: x-reply-pipeline-whitelist-collapse
description: "Root cause of the X reply drought — the 403 auto-blocker is cannibalizing the curated reply whitelist, collapsing the candidate pool toward zero."
metadata: 
  node_type: memory
  type: project
  originSessionId: 39c3c926-aa5b-41c7-9ea3-71c531229fc1
---

# X Reply Pipeline — Whitelist Collapse (found 2026-05-20)

The X reply bot (`find_reply_target.py`) runs in **curated mode**: it queries Grok for fresh posts ONLY from an 18-account whitelist (`~/.scout-reply-whitelist.json`, accounts believed to allow replies). A separate auto-blocker (added 2026-05-19, commit cbad81b "Add auto-blocking for 403-restricted X reply authors") adds any author whose reply 403s to `~/.scout-blocked-authors.json`.

**The two lists are fighting each other.** As of 2026-05-20: **12 of the 18 whitelisted accounts are now also blocked** (adamwathan, arvidkahl, dvassallo, hnshah, hwchase17, jasonlk, lennysan, levelsio, nathanbarry, shaanvp, swyx, thisiskp_). Only 6 remain usable: anthilemoon, joshpigford, justinjackson, marc_louvion, rosiesherry, samparr.

With the pool down to 6 accounts and 56 tweets already in the replied-log, scheduled runs keep failing with "All found tweets already replied to" or "All Grok candidates failed handle/blocked filter." Grok/credits are fine — it's pool exhaustion.

**Why:** The whitelist premise ("these accounts allow replies") is false for most of its members — the X API Free tier can't pre-verify `reply_settings`, so replies still 403 and the auto-blocker correctly flags them, eroding the whitelist over time. This is the upstream cause of the 6-week reply drought tracked in [[lior-x-data-rules]] Rule 4 ("Reply drought = account-wide collapse").

**How to apply:** When the reply bot reports no usable target, this is the likely cause — don't assume Grok/credits. Fix options for Reut to decide: (1) expand the whitelist with genuinely open-reply accounts, (2) stop auto-blocking whitelisted accounts (or cap blocklist TTL so blocks expire), or (3) reconsider the whitelist approach entirely if Free-tier `reply_settings` can't be verified. Counts are a 2026-05-20 snapshot and will drift — re-check the two JSON files before acting.

## RESOLVED 2026-05-23 (option 2 implemented)

The whitelist no longer erodes. Three changes shipped:
1. **Consumer defense** — `find_reply_target.py` blocked-authors filter now computes `load_blocked_authors() - whitelist`, so a whitelisted handle is never dropped even if it's in the blocklist file.
2. **Writer prevention** — `reply_x.py` `add_blocked_author()` now loads the whitelist and returns early (logs "is whitelisted — 403 ignored") instead of writing a whitelisted handle to `~/.scout-blocked-authors.json`.
3. **One-time cleanup** — removed the 12 stale whitelisted handles from the active `authors` list in `~/.scout-blocked-authors.json` (history kept for audit; backup at `~/.scout-blocked-authors.json.bak-2026-05-23`). Usable pool restored to 18/18; 9 genuine non-whitelist 403 blocks remain.

Whitelist now strictly wins over the auto-blocker. If the pool collapses again it's a *different* cause (e.g. all 18 already in the replied-log, or Grok returning nothing) — not whitelist erosion.

## Per-handle tracking + the zero-success finding (2026-05-23)

Added data-driven pruning so the whitelist is curated by outcomes, not guesses:
- `reply_x.py` now writes `author` (+ `failure_kind`) to every record in `O-output/x-performance-log/replies.jsonl`, on both success and failure paths.
- New read-only reporter `T-tools/01-skills/scripts/reply_whitelist_stats.py` aggregates per handle (attempts/ok/403/err, success rate, last outcome) and flags prune candidates. Run: `python3 reply_whitelist_stats.py [--min-attempts N] [--min-success-rate PCT] [--all]`. Default prune rule: attempts≥4 AND (0 successes OR rate<20%). It also warns if any whitelisted handle leaks back into the active blocklist (regression canary). Historical 403 authors were backfilled into replies.jsonl by joining the blocklist history on tweet_id (provenance flag `author_backfilled`; backups `*.bak-2026-05-23`).

**STARK FINDING:** across all 39 logged reply attempts there are **ZERO successes** — every attempt 403'd with the identical message: *"Reply to this conversation is not allowed because you have not been mentioned or otherwise engaged by the author of the post you are replying to."*

## API-wall investigation (2026-05-23) — it is NOT the whitelist

Read-only X API v2 probe with the OAuth1a creds in ~/.zshrc (X_API_KEY/SECRET, X_ACCESS_TOKEN/SECRET; no bearer token). Findings that kill every cheap hypothesis:
- **Write permission IS present:** `GET /2/users/me` returns header `x-access-level: read-write-directmessages`. Tokens are not read-only.
- **Correct account:** id 1587050424196112391, @lior_pozin.
- **Already Premium:** `verified: true, verified_type: "blue"`. Verification is not the missing lever. Account age fine (created 2022-10-31). **Followers only 276** / following 180 / 646 tweets.
- **Targets are OPEN:** `GET /2/tweets?tweet.fields=reply_settings` on the 403'd tweets returns `reply_settings: "everyone"` for all sampled — anyone may reply. (The old code comment claiming GET /2/tweets 401s on Free tier is STALE — it returned 200.)

So: write perms OK + Premium + correct account + targets open, yet 100% of replies 403. The error message blames the target, but the target allows everyone. **Conclusion: this is an account/app-level restriction on AUTOMATED replies, not a target setting and not the whitelist.** Best-fit cause: a low-trust (276-follower) account auto-replying via API into big founders' conversations (levelsio/swyx/jasonlk…) trips X's anti-spam reply gate. Curating/pruning the whitelist cannot fix this.

**Remaining unknowns (need a write action to resolve):** (a) does a MANUAL reply from the app to one of these "everyone" tweets succeed? (b) does an API reply succeed RIGHT NOW (restriction may be temporary; last failure 2026-05-19)? Definitive test = post one API reply to an open tweet and delete immediately, or have Lior reply manually. **Recommendation:** pause/curtail the auto-reply pipeline until ONE reply is confirmed to land — don't keep burning attempts or curating a whitelist that isn't the bottleneck. The whitelist-wins fix + per-handle tracking still stand and are correct; they're just not sufficient on their own.

## RESOLVED via live write tests + pipeline pause (2026-05-23)

Ran three live write tests on @lior_pozin (post + immediate delete) to map exactly what the account can do:
- **Reply to a stranger's "everyone" tweet → 403** "...not been mentioned or otherwise engaged by the author..."
- **Quote-post a stranger's tweet → 403** "...not been mentioned or are not part of the conversation thread..."
- **Standalone original post → SUCCESS** (posted id 2058164576697332140, deleted cleanly).

**Definitive conclusion:** X has @lior_pozin in a limited state that blocks API *interaction with strangers' posts* (replies AND quotes) but allows *original* posts. This is platform anti-spam on a low-trust (276-follower) account doing automated cold replies — NOT fixable in code, NOT the whitelist, NOT the target's settings. It likely self-prolongs while the automation keeps hammering 403s.

**Actions taken:**
1. **Disabled all 15 `scout-reply-x-01..15` scheduled tasks** (the X auto-reply jobs). They produced 0 successes and only 403s. Bluesky reply tasks (`scout-reply-01..10`) and `scout-day` (5 original X posts/day via Metricool) were LEFT ENABLED — those work and are Lior's real X presence.
2. **Guard in `reply_x.py`:** detects the account-restriction wording, logs `failure_kind: "account_reply_restricted"`, prints a loud "ACCOUNT REPLY-RESTRICTED" message, and does NOT block the author (it's not author-specific). Genuine per-author 403s (different wording) still block as before.

**To re-enable X replies later:** first confirm the restriction lifted — run the live API reply+delete test (or have Lior reply manually). Only re-enable scout-reply-x tasks once a reply actually lands. Recovery is driven by stopping automation + organic trust/follower growth, not by code. Lior's X activity meanwhile = original posts (scout-day) + Bluesky replies.

## Auto-recovery canary (added 2026-05-23)

A weekly scheduled task **`x-reply-canary`** (Sundays ~09:04 local) detects when the restriction lifts. It runs `T-tools/01-skills/scripts/reply_restriction_canary.py`, which posts ONE test reply to a live "everyone" tweet and deletes it within ~1s. Result is written to `~/.scout-x-reply-canary-status.json` (status: LIFTED | RESTRICTED | INCONCLUSIVE; exit 0/10/20). While RESTRICTED it stays silent. On **LIFTED** it: (1) re-enables ONLY `scout-reply-x-01` and `-02` (deliberately NOT all 15 — full cold-reply volume would re-trip the spam flag), (2) notifies Reut, (3) appends a "RESTRICTION LIFTED" note here. To check manually anytime: run the canary script directly, or `reply_whitelist_stats.py`. As of 2026-05-23 the canary confirms status = RESTRICTED.

## Still RESTRICTED 2026-06-01 (17 days, manual run by x-analyst-weekly)

Ran `reply_restriction_canary.py` manually during the weekly analysis: **STATUS: RESTRICTED, exit 10**, same wording, on a confirmed `reply_settings:"everyone"` target. The account-level block has now held **17 straight days** (since 2026-05-15) with no lift. No code action taken — re-confirmed there is nothing to fix in the pipeline.

**Implication for X strategy (carried into [[lior-x-data-rules]] Rule 1 + weekly hypothesis):** API replies remain dead. The only replies that have actually reached the timeline (the May 26 cluster — @edzitron 981, @DavidSacks 864, @dee_bosa 362, @gregisenberg 337 imp) were posted **manually via the web UI** — none appear in `replies.jsonl` (which logs only API attempts, all 403). So the working high-reach channel is **manual replies**: the pipeline should DRAFT replies + surface open-reply mid-tier targets, and Lior/Reut posts them by hand. Do not keep re-running the canary frequently — each attempt is a 403 that may prolong the flag; the scheduled Sunday canary is sufficient.
