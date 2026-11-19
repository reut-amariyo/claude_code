---
name: feedback-post-followers-undercount-connection-requests
description: "Per-post \"Followers gained\" UNDERCOUNTS: strangers send Lior connection requests instead of following, and pending requests aren't counted. Never judge a post a follower flop from that number alone"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 419d0db2-d6da-4e6c-a2ed-098048abc4cb
  modified: 2026-11-12T06:59:55.048Z
---

Reut, 2026-11-12, on the AI-decks post, which got 22 followers per Creator Analytics: "Treat it as a success. The problem with your follower count is that people send connection requests and you don't see them as followers."

**Why:** Many strangers who like a Lior post press Connect instead of Follow. A pending connection request does not appear in the per-post "Followers gained" number. It only becomes a follower once Lior accepts, and accepted requests are not attributed back to the post. So the per-post follower metric is systematically low.
- The Oct pattern fits this: "profile viewers ≫ follows because strangers connect instead".
- The $38M post brought 200+ connection requests on top of 83 post followers.

**How to apply:**
- When grading a post, never call it a follower flop or under target from "Followers gained" alone.
- Read the conversion signal from three things together:
  1. Followers gained.
  2. Profile viewers from the post.
  3. Pending connection requests that arrived in the 48h after it, if Reut can check linkedin.com/mynetwork/invitation-manager/.
- Treat the provisional "150+ followers in 48h" bar in [[feedback-linkedin-kpi-followers-not-impressions]] as measured on an undercounting metric.
- Defer to Reut's call on success.
- If grading needs precision, ask Reut for the pending-request count around the post date.

Related: [[feedback-linkedin-show-connections-and-followers]], [[lior-post-ai-decks-drives-me-crazy-success]]
