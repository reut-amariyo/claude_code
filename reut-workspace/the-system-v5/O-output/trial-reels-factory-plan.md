# Trial Reels Factory — 7/day Automation Plan

**Date:** 2026-07-05 · **Requested by:** Reut (via Bilech's brief)
**Goal:** Scale the working IG growth engine — trial reels with "comment X, get the book" lead magnets — from ~3/day manual to 7/day, as automated as possible.

## What's working today (from the 4 example reels on @lior)

| Reel | Format | Results |
|---|---|---|
| [DZ2cTwuxbVb](https://www.instagram.com/reel/DZ2cTwuxbVb/) | "10 startups that don't exist yet (but need to in 2026)" + Comment 'CEO' → 200 startup ideas | 4.3K likes, **969 comments** |
| [DZmqXpKRkkr](https://www.instagram.com/reel/DZmqXpKRkkr/) | Same concept, Comment 'founder' | 1.7K likes, 496 comments |
| [DZ9_G9txfyw](https://www.instagram.com/reel/DZ9_G9txfyw/) | Same concept, new list, Jun 24 | 283 likes, 144 comments |
| [DYupGPox_Db](https://www.instagram.com/reel/DYupGPox_Db/) | "Founders before vs after agents" meme | 15.5K likes |

Key signal: the third repetition of the SAME concept decayed hard (969 → 496 → 144 comments). Scaling to 7/day needs **concept variety**, not copies.

## TikFusion verdict: DO NOT BUY

[tikfusion.com](https://www.tikfusion.com) is not a content tool — it's a video "spoofer" (€199/mo) that alters one video so Instagram's duplicate-detection can't recognize re-uploads. Its market is OnlyFans agencies running 50K spam pages; its pitch is literally "no shadowbans."

1. Running it on @lior — a verified account with real brand equity — is exactly the inauthentic-behavior pattern Meta bans for. The account is the asset; not worth it.
2. It solves a problem we don't have. Each of the 7 daily reels carries a different list/book anyway, so we can generate **genuinely different videos** for free instead of disguised duplicates. Real variation also performs better (see decay above).

## The pipeline (all pieces already in our stack)

```
[1] Lead-magnet library ──► [2] Daily script generator ──► [3] ffmpeg renderer ──► [4] Metricool trial-reel scheduler ──► [5] ManyChat comment→DM ──► [6] Learning loop
```

**1. Lead-magnet library** — 5-10 "books," each with its own comment keyword: 200 Startup Ideas (exists), 200 AI Prompts (BONUS-prompts-pack.pdf exists), 200 AI Tools, 0→1 Playbook, 200 Side-Business Ideas, etc. Claude generates new ones on demand.

**2. Daily generator** — Claude produces 7 listicle scripts/day across rotating concepts ("10 startups that don't exist yet," "10 businesses you can start with $0 and AI," "10 boring niches quietly making millions," "10 SaaS ideas VCs would fund tomorrow"...), each mapped to a magnet + keyword + caption CTA. Runs through voice rules + /hooks scoring.

**3. Renderer** — local ffmpeg template (we already have .ffmpeg-bin + the Nate Herk pipeline): 1080×1920, hook title + animated list over a b-roll/background loop. 7 unique MP4s/day, zero cost. Needs ONE source template video from the current reels to match the look.

**4. Scheduler** — Metricool supports **Trial Reel** as a native content type ([help doc](https://help.metricool.com/how-to-publish-instagram-trial-reels-in-metricool-q27tj)), incl. "share with everyone after trial." We already drive Metricool's API (post_bluesky_metricool.py); extend it for IG trial reels by capturing one manual schedule's payload. Fallback: bulk-schedule a week in the Metricool UI in one sitting. Note: most tools can't post trial reels (native-app feature, not in the public IG API) — Metricool/Publer/Vista are the exceptions.

**5. Comment→DM** — keep whatever currently sends the book (ManyChat?). Caveat from ManyChat community: trial reels sometimes need the specific-reel trigger rather than "next reel"; one automation per keyword. Verify each keyword fires before scaling.

**6. Learning loop** — log per reel: concept / hook / book / keyword / comments / follows → weekly readout of which concepts and books convert. Same pattern as the X performance log.

## What I need from Reut to start building

1. **One source video file** (or the template/assets) from the current reels so the renderer matches the visual style — or unblock instagram.com in the Chrome extension so I can study them.
2. **Which tool** currently runs the comment→book DM (ManyChat?) and which keywords are taken.
3. **List of existing books** + which new ones to generate.
4. Green light to extend the Metricool script for trial reels (one supervised capture session in Chrome).

## Sources
- [Metricool: How to Publish Instagram Trial Reels](https://help.metricool.com/how-to-publish-instagram-trial-reels-in-metricool-q27tj)
- [Publer: Best Tools to Schedule Instagram Trial Reels in 2026](https://publer.com/blog/best-tools-to-schedule-instagram-trial-reels/)
- [ManyChat community: trial reels automation](https://community.manychat.com/general-q-a-43/trial-reels-automation-8878)
- [ManyChat: Post and Reel Comments trigger](https://help.manychat.com/hc/en-us/articles/14281316989724-Instagram-Post-and-Reel-Comments-trigger)
- [TikFusion](https://www.tikfusion.com/)
