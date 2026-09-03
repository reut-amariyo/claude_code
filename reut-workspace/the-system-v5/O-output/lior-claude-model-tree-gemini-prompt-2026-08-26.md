# Gemini image prompt — Claude Model Tree infographic
Date: 2026-08-26
Goes with: lior-claude-model-map-2026-08-26.md
Format: LinkedIn portrait 1200 x 1500
Brand source: ~/Desktop/brand/LIOR POZIN PB VI.pdf, pages 44 (fonts), 47 (palette), 49 (logo)

---

## Exact brand values pulled from the VI, not from memory

| Role in the VI | Hex |
|---|---|
| Graphite, typography and structure | #171818 |
| Medium Gray, grids and hierarchy | #686868 |
| Light Gray | #9E9D9D |
| Off White, backgrounds and containers | #E7E6E6 |
| White, focus points and emphasis | #FFFFFF |
| Sand, the only accent, used sparingly | #D9BC9A |

Fonts: JetBrains Mono for titles and model names, Inter for body text.
Signature element: the Container, a plain rectangular block.
Icon: a white vertical rectangle inside a solid graphite circle.
Wordmark: L1OR POZ1N, both I letters written as the numeral 1.
Motto lockup: [ life is beta ]

---

## PROMPT — written for Nano Banana

Lives standalone in gemini-prompt-claude-model-tree.txt. Prose, not a numbered spec, because Nano Banana reads a described scene far better than a bulleted brief and quietly drops items from long lists.

A flat vector infographic in a 4:5 portrait format, styled like a Swiss editorial diagram: strictly rectangular, sharp corners everywhere, thin dark grey connector lines, wide margins and a lot of empty space. The page background is light warm grey #E7E6E6. Question boxes are white #FFFFFF with a thin #171818 border and #171818 text. The four model boxes at the bottom are solid near-black #171818 with light #E7E6E6 text. The only accent colour in the whole image is a soft sand #D9BC9A, used exclusively on the small YES and NO branch labels. No gradients, no shadows, no glow, no rounded corners, no icons, no arrows, no emoji.

At the top left, in large bold monospace type, the title reads "Claude Model Tree". The top right corner is left completely empty, a clean bare square of background about 120 by 120 pixels with absolutely nothing in it.

Below the title, one white box centred on the page asks "Does your task need a complex answer?". Two thin lines drop from it, one to the lower left labelled "NO" and one to the lower right labelled "YES", each label sitting in a small sand-coloured rectangle.

The left line leads down to a white box reading "In a hurry?". The right line leads down to a white box reading "Would you clear a weekend for this?". Each of those two boxes splits again into two labelled lines: under "In a hurry?" the left line is "YES" and the right line is "NO"; under "Would you clear a weekend for this?" the left line is "NO" and the right line is "YES".

Those four lines land on four solid near-black boxes standing side by side in a single row across the bottom of the tree. Each box has the model name on the first line in bold monospace and a smaller sentence underneath in clean sans-serif. From left to right they read:
"Haiku 4.5" with "Instant. Chat only, no heavy files."
"Sonnet 5" with "Runs 70% of my week. The default."
"Opus 5" with "Modeling, code review, deep analysis."
"Fable 5" with "Deep research. Analytical decisions."
The YES branch of "In a hurry?" connects to Haiku 4.5 and its NO branch connects to Sonnet 5. The NO branch of "Would you clear a weekend for this?" connects to Opus 5 and its YES branch connects to Fable 5.

Directly beneath the Fable 5 box sits one small rectangle outlined in sand #D9BC9A containing the line "Careful. Only ~10% of tasks actually need it."

Across the very bottom runs a full-width near-black band with light text on two left-aligned lines: "When Opus gets stuck, escalate to Fable." and "Everything else, route down the tree."

Under that band, at the bottom left, the wordmark "L1OR POZ1N" is set in bold sans-serif with both I letters written as the numeral 1. At the bottom right, in small widely spaced monospace, sits "[ life is beta ]".

Render every quoted string exactly as written, correctly spelled, and legible at phone size. Do not add any words, labels, captions, logos or decorative elements that are not listed here.

---

## Working with Nano Banana

- **Text load is the risk.** There are 15 separate strings here. Nano Banana renders text better than most image models but not perfectly at this density. Read every label before approving.
- **Iterate, do not restart.** It is an editing model. If one label is wrong, reply in the same thread with the single fix, for example "keep everything identical, only fix the Sonnet 5 line to read exactly: Runs 70% of my week. The default." Starting a new generation rerolls the whole layout.
- **It likes to fill space.** If it puts something in the reserved top right square, reply: "remove everything from the top right corner and leave it empty".
- **Fallback if the text keeps breaking:** ask it for the frame only, with the boxes and lines and no words at all, then set the type in Canva with the real JetBrains Mono and Inter from reut-workspace/the-system-v5/T-tools/assets/fonts/. That gets you a perfect result in one pass instead of five rerolls.

## The Claude logo

Step 2 of the prompt reserves an empty 120 x 120 square in the top right corner. Drop the real Claude mark in there yourself in Canva after Gemini renders.

Why not ask Gemini for it: image models redraw known logos wrong almost every time, and a mangled Anthropic mark on a post about Anthropic models is the one error this audience will catch instantly.

Two options for the mark once you place it:
1. **Original coral.** The Claude mark stays its real color. It becomes the single spot of foreign color on the page, which reads as a source badge rather than a brand element. This is my recommendation.
2. **Single-color graphite #171818.** Sits fully inside Lior's system and looks cleaner, but a recolored third-party logo can read as sloppy to anyone who knows the brand.

Do not recolor it to Sand. Sand is Lior's human-layer accent and using it on someone else's logo reads as if Anthropic is part of his identity system.

---

## Notes for Reut

- If Gemini garbles the text, ask it once: "Regenerate. Keep the exact same layout and colors. Fix the spelling so every label matches my text word for word."
- Gemini will not have JetBrains Mono or Inter by name. If the type comes back generic, the fastest fix is to rebuild the same layout in Canva with the real fonts, which are already committed at reut-workspace/the-system-v5/T-tools/assets/fonts/.
- Check the four connections before approving. Copy and graphic have to route identically or they fight each other.
- ALT text for LinkedIn upload:
  "Decision tree for choosing a Claude model. First question, does your task need a complex answer. If no, are you in a hurry. Yes leads to Haiku 4.5, no leads to Sonnet 5. If yes, would you clear a weekend for this. No leads to Opus 5, yes leads to Fable 5."
