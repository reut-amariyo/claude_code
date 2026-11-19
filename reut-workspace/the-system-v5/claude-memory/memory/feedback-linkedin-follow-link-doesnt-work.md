---
name: feedback-linkedin-follow-link-doesnt-work
description: "LinkedIn \"followMember=\" discovery URL does NOT show a follow prompt off-LinkedIn; never offer it as a one-click follow link for a website"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 124d8d67-95fa-4b55-9605-c705f0a4f3e1
  modified: 2026-11-11T09:07:28.895Z
---

The URL `linkedin.com/(comm/)mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=<vanity>` comes from LinkedIn emails. Tested 2026-11-11 by Reut with a non-follower: no follow pop-up, only a generic "Recommended for you" list. The prompt seems to need LinkedIn's own email tracking context. LinkedIn has no public one-click follow link for personal profiles.

**Why:** I promised Reut it would work, put it into liorpozin.com (Webflow, unpublished), and it failed her test. I reverted the card to `linkedin.com/in/liorpozin/`.

**How to apply:** For "follow Lior on LinkedIn" CTAs, link to the profile. If she wants a prompt, it has to be our own pop-up on the site. Note: the Chrome LinkedIn session is Lior's own account, so it can't be used to test follow flows for him. liorpozin.com is on Webflow (site "Lior Pozin", Premium plan), not Base44 any more.

**Update same day:** Victoria Effer uses exactly the `/comm/` link in her Instagram bio, so it likely works in the LinkedIn mobile app (taps from IG = phones). Added a script to Webflow → Site settings → Custom code → Footer: on phones only, a tap on the LinkedIn card (`a.preview-item__inner`) swaps to the `/comm/` follow link; computers keep the profile link. Saved, not yet published or tested on a phone by a non-follower. If the phone test fails, delete that script block.

**Final, 2026-11-11:** The phone-only script was published to staging (lior-pozin.webflow.io). Reut tested on a phone with a non-follower in the LinkedIn app: still no follow prompt. Script deleted and staging republished clean. DEAD END on every device: never offer the followMember link again. Note: liorpozin.com production was last published ~2026-10-19, so the Designer holds weeks of someone else's unpublished changes. Never publish production without checking with Reut first.

**Correction, later 2026-11-11:** the "failed" phone test was done by someone who ALREADY follows Lior, so it proved nothing. Reut confirmed the raw link DOES show the follow prompt when opened directly on a phone; it doesn't on a computer. Re-added a v2 phone-only script (same-tab navigation so the LinkedIn app catches it) to Webflow footer code, published to staging lior-pozin.webflow.io only. Waiting on a real test: non-follower, phone, tapping the card on staging. Any follow-prompt test must use a NON-follower account.

**WORKS, 2026-11-11:** Reut tested lior-pozin.webflow.io on a phone with a non-follower: the follow prompt pops up. The v2 phone-only script (same-tab navigation, footer custom code) is the solution. Production liorpozin.com still pending: publishing it also ships the other unpublished Designer changes.
