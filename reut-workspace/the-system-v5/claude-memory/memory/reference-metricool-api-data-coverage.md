---
name: reference-metricool-api-data-coverage
description: Metricool API gives complete Instagram post/reel data for Lior but only partial LinkedIn data from June 2026 - endpoints, blogId, and the coverage trap
metadata:
  type: reference
---

Credentials: `~/.config/metricool/.env` (METRICOOL_API_TOKEN, METRICOOL_USER_ID).
Auth header: `X-Mc-Auth: <token>`. Lior's brand **blogId = 5775125**, userId 4473461.
The env file only names a LinkedIn blogId, but that one blogId covers the whole brand:
Instagram (lior), Threads, Bluesky, X (lior_pozin), LinkedIn, TikTok all hang off it.

Working endpoints (all take `from`/`to` as `YYYY-MM-DDTHH:MM:SS`, plus `blogId`, `userId`):

    /api/v2/settings/brands                  -> brand list + networksData
    /api/admin/simpleProfiles                -> same, with fbBusinessId
    /api/v2/analytics/posts/instagram        -> FEED posts/carousels only, NO reels
    /api/v2/analytics/reels/instagram        -> reels
    /api/v2/analytics/posts/linkedin         -> LinkedIn posts
    /api/v2/analytics/stories/instagram      -> 500 error, does not work

## The coverage trap (verified 2026-08-19)

**Instagram is COMPLETE.** July 2026 returns 97 reels + 17 posts, exactly matching
Instagram's own July monthly recap. Use it for per-month content counts, which
Instagram's web dashboard cannot give (web offers only 7/14/30/90-day windows,
no custom range - that needs the IG app).

**LinkedIn is INCOMPLETE from June 2026 onward.** Metricool only captured posts it
published, and the agency started posting natively around June 1:

| Month | Metricool posts | Metricool impressions | LinkedIn actual | Coverage |
|---|---|---|---|---|
| May | 14 | 294,339 | 292,705 | complete |
| June | 4 | 14,918 | 51,839 | 29% |
| July | 7 | 27,644 | 71,776 | 39% |
| Aug 1-19 | 3 | 11,222 | 55,759 | 20% |

So never quote a LinkedIn post count from Metricool after May 2026. The vault
performance log is also partial (it logged nothing between Jun 12 and Jul 3).
The only real source is LinkedIn Creator Analytics: set the date range, hit Export,
and the downloaded workbook lists every post.

## Second trap: Metricool views are not account views

Summing per-post views does not equal Instagram's account-level views for the same
month, because account views include views on content published earlier. June 2026:
Metricool post-sum 1.26M vs Instagram's 2.44M. Take counts from Metricool, take
views from Instagram.

Related: [[project-500k-ig-100k-linkedin-plan]], [[project-bluesky-mirror-pipeline]],
[[lior-performance-log]]
