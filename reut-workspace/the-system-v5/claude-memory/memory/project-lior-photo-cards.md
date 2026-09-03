---
name: project-lior-photo-cards
description: "Photo-card generator for Lior LinkedIn visuals (Squibb-style photo + big headline + highlighted number), built 2026-08-16; script, variants, and the photo constraint that makes or breaks it."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9ac5d240-048f-42b7-b27a-7a5200f780df
  modified: 2026-08-15T21:25:56.242Z
---

Reut saw a Simon Squibb card on 2026-08-16 and asked for the same style for Lior on LinkedIn. Built as a repeatable renderer, not a one-off image.

- Script: `the-system-v5/T-tools/01-skills/scripts/render_photo_card.py`, JSON spec in, PNG out. Docs + copy rules: `the-system-v5/O-output/photo-cards/README.md`.
- Layout: real photo top ~71%, uppercase 2-line headline below, `{{...}}` marks the highlighted number, `[ life is beta ]` lockup with hairlines across the photo bottom, optional kicker block top-left.
- 3 variants: `block` (graphite container block behind the number, most on-brand per [[lior-visual-identity-vi]] where the container's job is "highlight"), `sand` (graphite band, warm sand number), `plain` (quietest).
- Fonts committed to `T-tools/assets/fonts/` (JetBrains Mono + Inter) so no font install is needed.

**Why:** the design is only half the asset. The card survives the LinkedIn 4-visual-families rule ([[lior-top-8-10k-playbook]]) only as a *personal artifact*, which means a real candid Lior photo. A studio portrait or stock shot turns it into a marketing-team graphic, which is a hard fail.

**How to apply:** when Reut wants a LinkedIn visual for a post with a number in it, reach for this instead of designing something new. Headline follows the same hook rules as a post: under 10 words, setup line then payoff line, highlight is always a number or hard noun. Blocked input is usually photos, not code, so a candid Lior shoot list is the real dependency.

Gotcha: headless Google Chrome `--screenshot` hangs indefinitely on Reut's Mac, so the renderer is pure PIL at 3x supersampling. Do not rebuild HTML-to-PNG pipelines here expecting Chrome to work.
