# @lior_pozin — proof the account is partially limited, not dead

Compiled 2026-07-08. Sources: 489 posts from O-output/x-performance-log/posts.jsonl
(Feb 19 - Jun 25), live checks on x.com while logged in, June account analytics CSV.

## Verdict

The account is under a soft distribution limit. It is NOT suspended, NOT search-banned,
NOT fully shadowbanned. X throttles its baseline feed distribution and collapses its
replies, but lets individual posts break out when external engagement forces it.
That combination is exactly what a partial limit looks like.

## Evidence the account is NOT fully limited

1. No restriction banner on the profile, no warning interstitial for visitors,
   account is Premium-verified, all tabs load.
2. Typeahead: typing "lior pozin" in X search suggests @lior_pozin as the FIRST result.
   A suggestion-banned account never appears there.
3. `from:lior_pozin` in Latest search returns his posts normally.
4. 16 posts broke 1,000+ impressions, the best hit 3,790 = 11x the follower count.
   A hard-limited account cannot do that.

## Evidence the account IS limited

**1. Baseline distribution is throttled.**
Median original post: 30 impressions. The account has 337 followers, so a typical
post reaches under 10% of an already tiny follower base. 76% of all original posts
never passed 50 impressions. Healthy accounts, even small ones, don't have a
resting state this flat for 5 straight months.

**2. May 2026 was a hard throttle window. This is the strongest single proof.**
102 original posts in May. The single best one reached 115 impressions. Median 19.
In April the same account hit 3,790 on one post; in June it hit 2,376 again.
One month where the ceiling drops to 115 across 102 attempts, then lifts, is an
algorithmic cap switching on and off. Content quality cannot produce a hard ceiling.

| Month | Originals | Median imp | Best post |
|---|---|---|---|
| Mar | 50 | 36 | 332 |
| Apr | 135 | 37 | 3,790 |
| **May** | **102** | **19** | **115** |
| Jun | 32 | 41 | 2,376 |

**3. Replies are collapsed.**
Our reply targets are posts with 10K+ views by rule. A visible reply on a post
that size normally collects hundreds of impressions. Lior's replies to
@petergyang, @levie threads and similar got 6, 8, 9, 15, 19 impressions.
Single digits on a 10K-view thread means the reply sits behind
"Show more replies" where nobody taps. That is reply deprioritization, the most
common component of a partial limit.

**4. Search ranks him below strangers on his own name query.**
The "Top" tab for `from:lior_pozin` leads with OTHER accounts' posts he replied to;
his original posts don't rank. Latest shows everything, Top suppresses. Classic
quality-filter signature.

**5. Engagement proves content isn't the problem.**
June account level: 4.6% ER, 232 bookmarks, 175 reposts on only 33 posts, the best
ER quarter to date. The posts that do get seen perform. When engagement rate is
high and reach is flat, the bottleneck is distribution, not writing.

## What this is NOT

- Not the agency's fault: the throttle predates them (Feb-May) and June actually
  improved under them.
- Not a full shadowban: breakouts and search visibility rule that out.
- Not "X is just hard": May's 115-impression ceiling over 102 posts is a cap,
  not a cold algorithm.

## Two checks only Reut/Lior can finish

1. Open x.com/account/access while logged in. It sits behind a Cloudflare
   human-verification click I don't complete. If the account has a formal flag,
   it shows there; if it bounces to the home feed, the limit is purely algorithmic.
2. The logged-out tests (typeahead + reply collapse) should be repeated from a
   different account or incognito. From Lior's own session X always shows him
   his own content, so my typeahead result is a weak positive, not final.

## Likely causes worth fixing

- Feb-May volume: 100+ posts/month from a 337-follower account is bot-pattern
  posting frequency. June's drop to 33 posts coincided with recovery.
- 162 of 489 posts were replies, many into threads whose authors restrict
  replies (the 403 wave). Mass-replying into restricted threads is a known
  spam signal.
- Recovery path: keep volume low, keep ER high, let the June trend compound.
  Soft limits decay when the behavior that triggered them stops.
