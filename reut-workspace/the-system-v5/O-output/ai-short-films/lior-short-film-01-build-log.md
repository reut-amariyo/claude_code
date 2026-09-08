# Short film 01 "The Degree" — build log
Photoreal. Built scene by scene. Each step gets its prompt, its output, and a go/no-go before the next.

Master spec: [[lior-short-film-01-the-degree]]

---

## STEP 0 — young Lior character sheet

**Target age: 21.** That is the age of the story, 2016, the year eBay closed his account. If you want a younger cut for a later film in the series, the age-14 e-cig story is the one, and it needs its own sheet.

### What I need from you

1. **One current photo of Lior.** Front-facing, even light, neutral expression, no sunglasses, no hat, face filling a decent part of the frame. A clean portrait beats a good-looking photo here.
2. **A real photo of Lior at 18-22 if one exists.** If Reut can get one from him, we skip age regression entirely and the whole step gets easier and better. Ask before we generate.

Drop them in this folder as `ref-lior-current.jpg` and `ref-lior-young.jpg`.

### Note on the face-hidden device

The master spec hides the young man's face for all of shots 1 to 4 and reveals present-day Lior at 11.0s. We now test whether a 21-year-old Lior actually holds up photoreal. Two outcomes, both fine:

- Age regression looks like him → we can show the face in shot 3 or 4 and make the reveal a match cut of two faces instead of one. Stronger.
- Age regression drifts → we keep him hidden exactly as specced, and nothing is lost.

Do not decide this before looking at the output.

---

### PROMPT 0A — identity test, single portrait

Run this first. It is one image, it is cheap, and it tells us in thirty seconds whether the whole approach works. Feed the current photo of Lior as @image1.

```
An ultra-photorealistic RAW portrait photograph in documentary realism style of the same man as the reference image @image1, rendered as he would have looked at 21 years old.

AGE REGRESSION RULES. Preserve his identity exactly: the same bone structure, the same eye shape and eye colour, the same nose shape and bridge, the same ear shape and set, the same lip shape, the same brow position, the same hairline pattern, the same head shape and proportions, the same distinctive asymmetries. Change only what age itself changes: a slightly softer and less defined jawline, a leaner face with less mass in the cheeks and neck, a thinner neck, slimmer shoulders, a lighter and patchier stubble growth rather than a full even beard, no crow's feet, no nasolabial lines, no forehead lines, and thicker hair with a fuller hairline. He must read unmistakably as the same person, twenty-one years old. Not a different man. Not a boy. Not a teenager. A 21-year-old man.

FRAMING. Vertical 9:16. Chest-up front-facing portrait at eye level, centered, face occupying a large part of the frame, shoulders squared to camera. Neutral expression, mouth closed, not smiling, eyes looking directly into the lens. Tired but level.

WARDROBE. A plain washed grey cotton crew-neck t-shirt, slightly too big at the shoulders, the collar a little stretched out from wear. Nothing else. No jewellery, no watch, no chain, no logo, no branding of any kind.

SETTING AND LIGHT. A small dim bedroom at night. The only light source is a laptop screen just below and in front of him, out of frame, throwing a cool uneven light up onto his face and chest from a low angle, bright on the planes facing it and falling off fast into unlit shadow on the sides of his face and under his jaw. A single strip of warm tungsten spill from a hallway doorway behind him puts a faint warm edge on one shoulder and the side of his hair. Everything else in the room is dark. Behind him, deep in soft focus, the suggestion of a wall with small paper notes taped to it and the dark shape of a wardrobe. Nothing readable.

REALISM. Shot on an 85mm f/1.4 lens, RAW, shallow depth of field, realistic optical falloff. Fully natural skin with visible pores of uneven size, real skin grain, natural uneven pigmentation, a little redness at the nose and around the nostrils, genuine under-eye texture with faint shadow from tiredness but no wrinkles, real subsurface scattering where the screen light passes through the ear and the edge of the nostril. Individual eyebrow hairs. Individual eyelashes. Patchy young stubble with real individual hairs at uneven lengths and uneven density along the jaw and upper lip, thin and incomplete rather than full. Real eyes with visible iris fibres, faint vessels in the sclera, natural moisture, and a single hard rectangular catchlight from the laptop screen in each eye. Hair rendered strand by strand with a realistic hairline, natural scalp transition and a few flyaways. Real cotton t-shirt with an honest visible weave, a soft worn collar, and natural fabric folds at the shoulder.

GRADE. Very low saturation. Very low contrast. Deliberately under exposed. Cool screen light against warm tungsten spill, deep unlit shadow, no fill. Fine natural film grain. No colour pop of any kind.

FORBIDDEN. No beauty filter. No skin smoothing. No airbrushing. No waxy or plastic skin. No CGI sheen. No stylization. No cinematic exaggeration. No dramatic rim lighting. No lens flare. No bloom. No HDR. No crushed blacks. No blown highlights. No teeth. No smile. No logos. No text. No watermark.

The final image must look like a real photograph taken on a real camera in a real bedroom in the mid 2010s, of a real 21-year-old who is unmistakably the same person as @image1.
```

**Go/no-go:** put it next to the reference photo. If a stranger would say "that is the same guy, younger", we proceed. If not, we run 0A again with the age dialled to 24 before giving up, since a smaller regression holds identity better.

---

### PROMPT 0B — young Lior character reference sheet

Only after 0A passes. Feed the **approved 0A output** as @image1, not the original photo. The sheet has to lock the age-regressed face, not the current one.

```
Create an ultra-realistic professional character reference sheet of the exact young man from @image1. Preserve his facial identity, his apparent age of 21, and his overall appearance consistently in every panel. Keep his hairstyle, hairline and light patchy stubble exactly consistent with @image1 in every panel.

WARDROBE, identical in every panel. A plain washed grey cotton crew-neck t-shirt, slightly oversized at the shoulders with a soft stretched collar. Dark navy cotton track shorts, plain, no stripes. Bare feet. No jewellery, no watch, no chain, no bracelet, no rings. No logos, no branding, no text on any garment.

LAYOUT. Arrange multiple photographs of the SAME young man on one neutral muted grey studio background in this exact layout.
LEFT LARGE PANEL: Half-body FRONT view, framed from the waist up. He stands relaxed facing the camera, arms at his sides, neutral expression, not smiling.
MIDDLE LARGE PANEL: Half-body THREE-QUARTER BACK view, framed from the waist up, turned so the back of his head, the back of his neck and the shoulders and back of the t-shirt are clearly visible.
UPPER RIGHT PANEL: Close-up FRONT portrait of his face, matching @image1 exactly, face filling most of the panel.
LOWER RIGHT LEFT PANEL: Full-body FRONT view, head to bare feet, standing naturally, showing the complete outfit.
LOWER RIGHT RIGHT PANEL: Full-body DIRECT BACK view, head to bare feet, seen entirely from behind, showing the back of the head, the back of the t-shirt and the back of the shorts.

CONSISTENCY. Every panel must show the exact SAME young man with the same face, the same apparent age, the same body proportions, the same hairstyle, the same stubble and the same outfit. He is slim and lightly built, narrow shouldered, with the build of a 21-year-old who does not train.

REALISM. Maximum photographic realism. Render every panel as a genuine RAW studio photograph of a real human. Realistic natural skin with visible pores, fine skin grain, subtle uneven pigmentation, natural under-eye texture, slight natural sheen and small real imperfections. Realistic eyes with visible iris fibres and natural moisture. Individual eyelashes and individual eyebrow hairs. Patchy young facial hair with realistic individual hairs at uneven lengths and uneven density, thin and incomplete, never a full even beard. Natural hair with thousands of individually visible strands, a realistic hairline, natural scalp transition and subtle flyaways. Realistic cotton jersey texture on the t-shirt with an honest weave, visible stitching at the collar and hem, and natural fabric drape and folds. Real bare feet with correct anatomy, correct toe count and realistic skin.

LIGHT AND GRADE. Soft directional studio lighting with natural dimensional shadows, consistent across every panel. Muted, slightly desaturated, true-to-life colour grading. Very low saturation, low contrast. Professional RAW photography quality and realistic optical depth.

FORBIDDEN. No beauty filter, no skin smoothing, no airbrushing, no waxy or plastic skin, no CGI appearance, no stylization, no glamour lighting, no logos, no text, no watermark.

The final result should look like five real professional photographs of the same 21-year-old man from the same photoshoot, arranged together as one clean character reference sheet.
```

The direct-back and three-quarter-back panels matter more than usual on this one. Shots 1, 2 and 4 of the film are filmed from behind him, so the model needs a locked reference for the back of his head and the back of that t-shirt, not just his face.

---

### Note for the record

This film dramatizes Lior's own documented story with a synthetic image of him. That is fine and it is his to tell. It should read as a made film and never be presented as archive footage of 2016.

---

## STEP 1 — scene 1 (doorway, 0.0 to 2.5s)
Pending step 0 approval.

## STEP 2 — scene 2 (the suspension banner, 2.5 to 5.5s)
Pending.

## STEP 3 — scene 3 (night montage, 5.5 to 8.5s)
Pending.

## STEP 4 — scene 4 (the full room, 8.5 to 11.0s)
Pending.

## STEP 5 — scene 5 (match cut to the office, 11.0 to 13.0s)
Pending. Needs the present-day Lior character sheet from the master spec.

## STEP 6 — scene 6 (he looks up, 13.0 to 15.0s)
Pending.
