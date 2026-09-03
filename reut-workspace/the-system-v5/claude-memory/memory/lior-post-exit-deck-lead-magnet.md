---
name: lior-post-exit-deck-lead-magnet
description: The exit-deck lead magnet A/B, 2026-08-24/25 - identical copy died at 55 impressions with a comment-gate CTA and finished at 66,682 given away free. Confirmed by Reut as Lior's best FOLLOWER post ever; it is now the signature-series format.
metadata:
  type: project
---

Cleanest natural experiment in the log: the **same post copy**, two days running, one variable changed.

**Version A, 2026-08-24, killed.** Hook "Sold my business to Fiverr for $92M with this 47-slide
deck", body identical, image = a grid of all 47 slides. CTA was the comment gate modelled on
Yurii Rebryk: "Leave any comment & like the post / Add me in connections / I will send you the
link in the DM". **55 impressions at 1h, 15 members reached, 78% in-network.** The 17 comments were
all people Reut asked directly via a link to the post, so organic reach really was ~55. Deleted
the same evening.

**Version B, 2026-08-25, worked.** Same hook and body. No gate: no comment ask, no like ask, no
connection ask. Native LinkedIn **document carousel** instead of a single image, and the download
link in the first comment. **23,111 impressions at first read. FINAL, confirmed 2026-08-29: 66,682 impressions,
317 reactions, 60 comments, 1 repost, and ~80 connection requests.** It kept distributing for
four days, which narrative posts never do.

**Reut, 2026-08-29: this is the best post we have ever had on LinkedIn, because of the follower
volume, which we have never seen before.** That settles the follower-KPI question: the artifact
giveaway is the follower engine, not personal narrative.

## What this proves

1. **The comment-to-receive lead-magnet layer is suppressed on this account.** It was tested on
   the strongest possible asset, a first-party artifact with a $92M number attached, and still
   died. This confirms the standing ban in the-system-v5/CLAUDE.md rather than overturning it.
   Do not retest. See [[feedback-linkedin-comments-manual-posting]].
2. **Giving the asset away beats gating it, on every metric that matters.** Version B produced ~80
   connection requests with no ask at all. A LinkedIn connection auto-follows, so that is ~80 net
   followers from one post, against the 150/48h win condition in
   [[feedback-linkedin-kpi-followers-not-impressions]].
3. **Native document carousels distribute.** Portrait 1080x1350, hook page, one idea per card,
   closing card. First format in the log to clear 20K without a newsjack or a tagged giant.
4. **Never ask people to comment via a direct link.** LinkedIn's early test measures engagement
   from people it showed the post to in the feed; an off-feed burst does not feed that test and
   patterns as a pod.

## Why it converts followers, as opposed to why it reached

Reach came from the carousel, the ungated link, the $92M/Fiverr anchor in the first 8 words, and
the four-day tail. Follows came from something else, and only this second list is worth copying:

- The reader ends the interaction OWNING something. Every other post asks them to agree or feel.
- Nobody else can give this artifact away. A prompt pack is a commodity; a deck that actually
  moved a company to an actual buyer exists once. The scarcity IS the credential.
- A follow here is a bet on the next one. "He gives away real internal documents, there will be
  more." That is the subscription decision the mega-accounts run on, see
  [[feedback-linkedin-kpi-followers-not-impressions]].
- The body gave ONE counterintuitive tactic, not a list of ten. A list reads as content; one
  tactic reads as access, and it proves the artifact is worth having.
- Generosity with zero ask attached.

## Reusable shape

Hook with a first-party number → one piece of advice, not a list → the artifact as a document
carousel → "no need to comment", link in the first comment. Assets and scripts live in
`the-system-v5/O-output/exit-deck-lead-magnet/` (`build_carousel_sections.py` renders the deck to
a portrait carousel from any PDF).

**Now promoted to the signature series: one first-party artifact giveaway every two weeks.**
Full template, the 7 beats, 7 drafted next posts and the kill-list live in
`the-system-v5/O-output/linkedin-artifact-giveaway-series-2026-08-29.md`.
Hard rule for the series: the document must be one Lior ACTUALLY USED. A document written for
the post is a lead magnet and the scarcity evaporates.
