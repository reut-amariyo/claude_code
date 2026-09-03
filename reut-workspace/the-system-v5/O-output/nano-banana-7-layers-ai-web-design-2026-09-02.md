# Nano Banana prompt — 7 Layers of AI Web Design (2026-09-02)

Reference: Jake Ward's "5 Layers of SEO in 2026" concentric-arc diagram, 899 reactions,
199 comments, 109 reposts. Structure borrowed, content is the 7 steps from the Fable 5.1 post,
palette and type swapped to Lior's VI.

Swaps from the reference:
- 5 arcs to 7 arcs, one per step, foundation innermost.
- Coral gradient to Claude's own palette, per Reut 2026-09-02. Clay orange #D97757 on cream
  #F0EEE6 with near-black #141413 type. This is a deliberate deviation from the VI's
  monochrome-plus-5%-accent rule, and it is the right call here because the subject of the
  post is Claude, so the palette reads as topical rather than decorative. Lior's type system
  and lockup carry the brand instead of the color.
- Author photo chip to the [ life is beta ] lockup.
- JetBrains Mono for the title and headings, Inter for everything small.

Visual-family note: the save-first spec prefers a real screenshotted artifact over a designed
card. This lands as a signed illustration instead, which is one of the four legal families,
because it carries his lockup and his type system rather than reading as a marketing graphic.

## The prompt

```
A clean, premium infographic poster designed for LinkedIn.
Canvas size 1080 x 1350 pixels, 4:5 portrait aspect ratio.

LAYOUT
A large title at the top left-aligned across the full width, then seven concentric arcs
stacked from the bottom of the canvas upward, like ripples or nested rainbow bands. The
innermost, smallest arc sits at the bottom center. Each following arc is larger and arcs
over the one below it. All seven arcs are visible and clearly separated by thin hairline
strokes.

TITLE
"Fable 5.1 Web Design"
Set in JetBrains Mono Bold, very large, near-black ink, left aligned at the top with generous
white space above it. This is the only text in the title, nothing before it and nothing after it.

SUBTITLE
Directly beneath the title, much smaller, Inter Regular, warm brown-gray:
"What separates an AI-built page from a premium one"

EACH ARC contains, centered inside its band:
- a small rounded pill with the layer number
- a bold two or three word heading
- one line of smaller supporting text below the heading

Working from the OUTERMOST arc at the top down to the INNERMOST arc at the bottom:

Layer 7 - "Make it look at itself" - "Fable 5.1 screenshots the full scroll and catches what broke"
Layer 6 - "Win on mobile" - "Desktop animation dies on a small screen unless you ask"
Layer 5 - "Never invent a button" - "Hand Fable 5.1 components that already exist"
Layer 4 - "Bring the reference" - "Name the site and the exact element you want from it"
Layer 3 - "Make the scroll talk back" - "Fading text and layers moving at different speeds"
Layer 2 - "Name the buyer" - "Pain, person and promise, or the page reads generic"
Layer 1 - "Lock the brand first" - "Colors, type and visual language before a single screen"

SATELLITE CHIPS
Small rounded rectangular chips with thin outlines and short labels sit scattered along each
arc band, some on the left side, some on the right side, positioned as if orbiting that layer.
Use these exact labels, four per layer:

Layer 7: "Broken layers", "Awkward cuts", "Off-frame elements", "Full scroll"
Layer 6: "390px", "Touch targets", "Layout shift", "Phone preview"
Layer 5: "Buttons", "Cards", "Sections", "Animations"
Layer 4: "21st.dev", "Godly", "Awwwards", "Motion Sites"
Layer 3: "Fade-in", "Parallax", "Sticky nav", "Reveal on scroll"
Layer 2: "Pain", "Person", "Promise", "Audience"
Layer 1: "Colors", "Type", "Logo", "Visual language"

FOOTER
Centered at the very bottom, inside the innermost arc, a small rounded container holding the
text "Lior Pozin" in Inter Bold with "[ life is beta ]" directly beneath it in JetBrains Mono,
smaller and lighter.

COLOR
Warm and terracotta, using Anthropic's Claude palette.
Background: cream, hex #F0EEE6.
Typography: near-black ink, hex #141413.
Accent: Claude clay orange, hex #D97757.

The seven arcs are filled with tints of the clay orange #D97757, stepping gradually more
saturated toward the center. The outermost arc is the palest wash of orange, barely tinted
against the cream, and each arc inward is a step warmer and deeper, so the innermost
foundation band is the strongest orange on the page. Separate the bands with hairline strokes
in a slightly deeper terracotta.

The seven layer-number pills are solid Claude clay orange #D97757 with cream text.
The satellite chips are cream with thin warm gray outlines and near-black text.
No gray anywhere. Every neutral on the page is warm.

TYPOGRAPHY
JetBrains Mono for the title, the layer headings and the tagline. Inter for the supporting
lines and the chip labels. Generous letter spacing on the title. High contrast, no drop
shadows, no glows, no gradients other than the gentle step between arc fills.

STYLE
Editorial, calm, technical. Flat vector. Sharp edges, precise alignment, plenty of negative
space. No photographs, no icons, no emoji, no 3D effects, no decorative illustration.

TEXT ACCURACY
Render every piece of text exactly as written above, spelled correctly, including "21st.dev",
"Awwwards", "390px", "Fable 5.1" and "[ life is beta ]" with its brackets and lowercase letters.

Do not include any Anthropic or Claude logo, wordmark or icon anywhere in the image.
```

## If the first render garbles the small text

Nano Banana degrades on dense small type. Two fallbacks, in order:
1. Rerun with the chips cut to two per layer. The layer headings are what carry the post.
2. Drop to 5 arcs by merging steps 1 and 2 into "Set the brand and the audience" and steps
   5 and 6 into "Reuse components and verify on phone". Five arcs matches the reference
   exactly and gives every label more room.

## ALT text for the post

"A diagram titled Fable 5.1 Web Design, showing seven nested arcs. The innermost
layer is locking the brand first and the outermost is having the model screenshot the full
scroll to catch what broke."

## Sizing (2026-09-02)

Export at 1080 x 1350, 4:5. That is the tallest ratio LinkedIn renders in the feed without
cropping, so it buys the most vertical space. The first render was already 4:5, so the
cramping came from band thickness, not from the proportion.

If it still reads tight, in this order:
1. Cut chips from four per layer to two.
2. Merge to five layers, which matches the donor reference and gives each band about 40% more room.

A 1200 x 1200 square is the alternative. It gives the chips more horizontal room and every
band less vertical room, which trades one crowding problem for another. Not recommended.

LinkedIn also downscales feed images to roughly 552px wide on desktop, so anything smaller
than the chip labels will not survive. That is the real constraint on how many chips fit.

## Heading fix (Reut 2026-09-02)

"Win the phone" is not idiomatic English. You can win on mobile, you do not win a phone.
Changed to "Win on mobile", which keeps the imperative register the other six headings use.
Alternates considered: "Test it on a phone", "Check the mobile version", "Survive the phone".
