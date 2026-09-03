# Photo cards — the "Squibb layout" in Lior's visual identity

Reference that started this: Simon Squibb's card. Real photo on top, one short
uppercase headline below, one number carrying the whole payoff, logo lockup on
the photo. It works because the number does the hooking and the photo proves a
human was there.

Rebuilt inside Lior's VI instead of copied:

| Squibb | Lior |
|---|---|
| Condensed sans, red highlight | JetBrains Mono ExtraBold, graphite container block or warm sand |
| SIMONSQUIBB.COM logo, centered on photo | `[ life is beta ]` lockup with hairlines, same position |
| White band | Off White `#F2F0EC` or Graphite `#1C1C1A` |
| Bright brand colors | Monochrome, 5% warm sand accent only |

## Render one

```bash
python3 T-tools/01-skills/scripts/render_photo_card.py O-output/photo-cards/demo-spec.json
```

The spec is JSON, one object or a list. Full field docs are in the script header.

```json
{
  "photo":   "O-output/photo-cards/lior-office.jpg",
  "kicker":  "AUTODS · 2017",
  "line1":   "WE STARTED WITH ZERO FUNDING",
  "line2":   "IT ENDED IN A {{$92M}} EXIT",
  "variant": "block",
  "byline":  "Lior Pozin · architect of growth",
  "focus":   "50% 30%",
  "out":     "O-output/photo-cards/2026-08-16-zero-funding.png"
}
```

`{{ }}` marks the highlight. Works on `line1` too, but use it once per card.
`focus` moves the crop, first number is horizontal, second is vertical, so a
face high in the frame wants something like `"50% 20%"`.

## The three variants

- **block** — off-white band, graphite headline, the highlight sits inside an
  inverted graphite block. Most on-brand: in the VI the container block's stated
  job is "highlight / focal point". Default choice.
- **sand** — graphite band, off-white headline, highlight in warm sand. Darkest
  and loudest in a feed. Use when the card has to win against a busy photo.
- **plain** — off-white band, warm sand highlight as text only. The quiet one,
  for a card that sits under a heavy post.

Sizes: `portrait` 1080×1350 (LinkedIn default, most feed real estate) or
`square` 1080×1080.

## Copy rules for the headline

Two lines, and they are a hook, so the vault hook rules apply.

1. Line 1 is the setup, line 2 lands the payoff. Never the reverse.
2. Under 10 words total. The auto-fit shrinks type to fit, but a card that
   shrinks below ~44px has too many words.
3. The highlight is a number or a hard noun. `$92M`, `250 PEOPLE`, `3 A DAY`,
   `ZERO`. Never a verb, never an adjective.
4. No parentheses, no em dashes, no "not X, it's Y".
5. Both lines must be true and publicly sayable. `$92M` exit and `250 employees`
   are cleared. `100 engineers` is not, ever.

## The photo is the constraint, not the design

LinkedIn visual rule: only 4 families, and this card lives in **personal
artifact**. That holds only while the photo is a real Lior moment — office,
stage, warehouse, laptop, a room with people in it. The second it becomes a
stock shot or a posed studio portrait on a brand background, the card reads as
a marketing-team graphic and the family rule kills it.

Squibb's card works for the same reason: two men on a Paris street, phone
photo, nobody art-directed it.

Shoot list worth building so this engine has fuel: Lior at the desk mid-call,
the AutoDS floor, a stage shot from the back of the room, a hotel-lobby laptop,
whiteboard mid-argument.

## Demos in this folder

`demo-A-block.png`, `demo-B-sand.png`, `demo-C-plain.png` — layout tests only.
The photo in them is a crop from the E97 podcast graphic used as a stand-in, so
judge the typography and ignore the teal background. `_demo-placeholder-lior.jpg`
is that crop.

## Fonts

`T-tools/assets/fonts/` — JetBrains Mono Regular/Bold/ExtraBold, Inter
Regular/SemiBold. Committed so the renderer works on any machine without a
font install.
