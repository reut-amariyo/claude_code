# Short film 02 — "The Signature"
15 seconds. Photoreal. Difficulty 2/10. Three shots of five seconds, generated separately.

Date: 2026-09-06
Status: character sheet locked, ready to generate shot 1

---

## The story

Canonical, from the Lior OS. Two years before Fiverr, a private equity firm ran a six-month negotiation and full due diligence on AutoDS. He walked away a day before closing, because the buyer intended to cut staff and run it for cash. The people who would have been cut were the ones who had taken below-market salaries since day one.

One idea in the film: **he had the money in front of him and he did not sign.**

No firm named. No number named. Fiverr not named. One man, one contract, a pen he puts down.

---

## Why this is easy to execute

One character. One room. One grade. Nobody else in frame. Nothing in the environment changes between shots. Three clips of five seconds, each generated on its own, cut hard together in any editor. If a shot comes back wrong you regenerate that shot and nothing else in the film moves.

**The only physical action in the whole film is capping a pen.** Same discipline as the single breath in the beach reference, which is why that one is a 2/10.

---

## STEP 0 — done

The character reference sheet already exists and is better than what we would have generated. It carries five body views including a direct back and a top-down, plus hair profile, watch construction, garment texture, footwear, skin and stubble, eye detail and a colour palette.

Feed that sheet as **@image1** into every shot below. Nothing else needs generating first.

### Two calls I made after seeing the wardrobe

**1. The watch comes off for this film.** Shot 2 is a close-up on his hand holding a pen next to a blank signature line. A rose gold Patek in a warm pendant pool would be the brightest object in that frame, sitting right beside the thing the audience is supposed to be looking at, in a film whose entire point is that he turned down money to protect his team. It also happens to be the single hardest object in the wardrobe to render, and a mangled dial reads as AI instantly.

If you want it in anyway, delete `No watch,` from the HIM block in all three prompts and add this sentence at the end of that block:

```
He wears a rose gold cushion-cased dive-style watch with a brown textured rubber strap and a brown grid-patterned dial on his left wrist. The dial text and numerals must be soft and never legible.
```

**2. The all-black outfit needs a separation light.** A black t-shirt against a dark night office merges into the background and the whole frame goes to mud. Every prompt below carries a SEPARATION block that puts a faint cool edge from the office monitors behind him on his shoulders, neck and hairline. This is not decoration, the shots do not read without it.

### Check on every render

The `[BETA]` wordmark on the chest. Models garble short text. If it comes back as `[BEIA]` or `[BFTA]`, regenerate. Do not accept a near miss on his own tagline.

---

## Captions

Burned in, bold white with a hard black outline, centered lower third, one line at a time.

```
0.5s    A DAY BEFORE SIGNING
5.5s    THEY WANTED TO CUT THE PEOPLE WHO BUILT IT
11.0s   SO I DIDN'T SIGN
```

No voiceover. No music. If you want a bed, one low sustained note from 10.0s and nothing before it.

---

## Pipeline

Two stages per shot, same as the reference pack.

**Stage A — GPT Image 2.** Upload the character reference sheet as the reference image, set the output to portrait 9:16, run the IMG prompt. This produces the first frame of the shot. Regenerate until the frame is right. This is where all the work happens, because a good first frame decides the whole clip.

**Stage B — Seedance 2.5.** Feed the approved still as the start frame, run the short VID prompt, 5 seconds.

The VID prompts are deliberately short. The image already carries the face, the wardrobe, the room, the light and the grade. A long video prompt fights the image instead of animating it.

---

## SHOT 1 — 0.0 to 5.0s. He is reading.

### 1-IMG — GPT Image 2, portrait 9:16

```
An ultra-photorealistic RAW photograph in documentary realism style, vertical 9:16, of the exact same man as the reference image. Preserve his facial identity exactly: same face, same short dark brown wavy hair with a faded taper at the sides, same short dark beard and stubble at uneven density, same brown eyes, same thick dark eyebrows, same build.

WARDROBE. He wears a black oversized cotton crew-neck t-shirt with a small white sans-serif wordmark reading [BETA] in square brackets printed centred on the chest, and black straight-cut cotton trousers. No watch, no bracelet, no ring, no chain, no jewellery of any kind. No other logos, no other text and no other branding anywhere on the clothing.

SCENE. A glass-walled meeting room inside a modern technology office, late at night. He is seated alone at a long pale oak table with visible grain and faint ring marks, leaning slightly forward, forearms resting on the table on either side of a thick stack of printed contract pages. Five empty mesh office chairs are pushed in around the table at slightly uneven angles. The contract is around eighty pages, held with a black clip at the corner, the top page dense with small text and tabbed down one edge with small coloured sticky flags. Beside it a plain black pen with the cap on. A closed laptop pushed to one side. A glass of water, half full, with condensation and a ring under it. A phone face down. A whiteboard on the far wall with old diagrams half rubbed out and the faint ghost of previous marker still showing. Through the glass wall behind him: the open-plan office, dark, rows of empty desks receding into depth, monitors off, a scatter of small standby LEDs, one cleaner's light left on far at the back, and beyond that a window wall with black city night and scattered distant lights, no skyline detail, no landmarks.

HIS STATE. He is reading the contract. He is not looking up and not looking at the camera. His expression is level and unhurried, mouth closed, not smiling, not troubled, not dramatic. The face of a man reading carefully.

CAMERA. Shot on an 85mm lens at f/2, from across the table, low, roughly at table height, framing him from the chest up. The near edge of the table and the corner of the contract stack sit soft and dark in the very bottom of frame. The office behind him falls into genuine soft focus. Slightly off-level horizon, as if handheld.

LIGHT. A single warm pendant light hangs low over the centre of the table and is the only light source in the room. It puts a warm pool on the table, on the paper, and on the top of his head, his shoulders and the bridge of his nose, and his eyes sit slightly in shadow under his brow. Deep unlit shadow in the corners of the room.

SEPARATION. His t-shirt is black and the room behind him is dark, so he must not merge into the background. A faint cool edge of light from the monitors and standby LEDs in the office behind the glass catches the top of his shoulders, the side of his neck and the outer edge of his hair, separating him cleanly from the darkness. Subtle and cool, never a bright rim, never a halo, never dramatic.

GRADE. Very low saturation, very low contrast, soft gentle falloff, deliberately under exposed. Warm pendant pool against cool dark blue-grey. Fine natural film grain. No golden hour, no orange cast, no vivid colour, no crushed blacks, no blown highlights, no HDR, no bloom, no lens flare.

REALISM. Ultra-realistic RAW skin with visible pores of uneven size, pronounced skin grain, real beard and stubble hairs at individual lengths and uneven density, natural uneven pigmentation, genuine under-eye texture, fine lines, real subsurface scattering where the pendant light catches the top of his ear. Real brown eyes with visible iris fibres, faint sclera vessels, natural moisture and a small soft catchlight from the pendant. Individual eyelashes and eyebrow hairs. Hair rendered strand by strand with a realistic hairline and natural scalp transition. Anatomically correct hands, correct finger count and joint bend, real knuckle creases, visible tendon and vein structure on the backs of the hands resting on the table. Real heavy black cotton jersey with an honest visible weave, a soft ribbed collar and natural folds at the elbow and shoulder, reading as black cloth and not as a flat silhouette. Real paper with genuine weight, slightly uneven page edges, real printed text density and real sticky flags with a slight lift. Real oak grain and faint cool reflections on the glass wall.

FORBIDDEN. Nobody else in the room and nobody visible anywhere in the office behind the glass. The only text anywhere in the image is the [BETA] wordmark on his chest, spelled exactly B E T A inside square brackets. All printed text on the contract is soft and unreadable, and no real name, logo, company name or brand appears anywhere. No beauty filter, no skin smoothing, no airbrushing, no waxy or plastic skin, no CGI sheen, no stylization, no cinematic exaggeration, no watermark.
```

### 1-VID — Seedance 2.5, 5 seconds, from the approved still

```
Animate the provided image. Keep the framing, the wardrobe, the room, the light and the colour exactly as they are in the image. Do not add anything and do not change anything.

CAMERA. Handheld throughout. Constant gentle shake, natural breathing sway, small drifts and corrections, a slightly off-level horizon. Never a tripod, never a gimbal, never stabilized, never locked off. The motion is soft and slow and never jerky. One continuous take, no cut.

ACTION. He is reading the contract. For the first three seconds he is completely still apart from breathing and the small natural movement of his eyes across the page. Then he turns one page, slowly, with one hand, and settles back into reading. Nothing else happens. He never looks up and never looks at the camera. He never speaks.

AUDIO. No music, no score, no dialogue. Natural sound only: the low hum of air handling, a distant fan somewhere in the building, one page settling, his slow breathing.

FORBIDDEN. No second person appears. Nobody walks past behind the glass. No new light source. No zoom, no push, no crane, no reveal. No slow motion. Smooth 60fps at natural real-life speed.
```

---

## SHOT 2 — 5.0 to 10.0s. The blank signature line.

### 2-IMG — GPT Image 2, portrait 9:16

```
An ultra-photorealistic RAW photograph in documentary realism style, vertical 9:16, shot from just behind and above a seated man's right shoulder and angled steeply down onto a table. The man is the exact same man as the reference image and only his shoulder and the side of his head are visible, large, soft and dark, out of focus along one edge of the frame. He wears a black oversized cotton crew-neck t-shirt. No watch, no bracelet, no ring, no jewellery of any kind on either hand or wrist.

THE FRAME. The image is dominated by the last page of a printed contract lying flat on a pale oak table in a warm pool of light. The page has dense small printed text across the top, and below it a long empty horizontal signature line with a small printed name block underneath it. The signature line is completely blank. There is no ink and no signature anywhere on the page. His right hand rests on the table beside the page, holding a plain black pen loosely with the cap still on, the pen not touching the paper. A second hand rests flat on the page. Behind the page and out of focus: the edge of a thick clipped stack of contract pages, a half full glass of water with a ring under it, a phone face down, and the dark blur of an empty meeting room.

SCENE. A glass-walled meeting room inside a modern technology office, late at night. Through the glass behind, far out of focus, the dark open-plan office with rows of empty desks and a scatter of small standby LEDs.

CAMERA. Shot on an 85mm lens at f/2 from a high angle behind his shoulder. Shallow depth of field. The page is the sharpest thing in the frame and everything else falls away.

LIGHT. A single warm pendant light hanging low over the table is the only light source. It puts a warm pool on the paper and the hands and falls off fast into darkness at the edges of the frame.

SEPARATION. His black shoulder in the near foreground must not merge into the dark room. A faint cool edge from the office lights behind catches the top of his shoulder and the outer edge of his hair.

GRADE. Very low saturation, very low contrast, deliberately under exposed. Warm pendant pool against cool dark blue-grey. Fine natural film grain. No orange cast, no vivid colour, no crushed blacks, no blown highlights, no bloom, no lens flare.

REALISM. Ultra-realistic RAW skin on the hands with visible pores, real skin grain, natural uneven pigmentation, genuine knuckle creases, visible tendons and raised veins on the back of the hand, fine dark hairs on the forearm, real fingernails with realistic nail beds and slight natural irregularity. Anatomically correct hands, correct finger count, correct joint bend, a natural relaxed grip on the pen with realistic finger pressure. Real paper with genuine weight, a slight curl at the free edge, a faint sheen where the light hits it at an angle, and a real soft shadow cast by the pen onto the page. Real pen with a moulded plastic body, a slightly worn clip and one real specular highlight. Real heavy black cotton jersey on the shoulder with an honest weave and natural folds.

FORBIDDEN. THE SIGNATURE LINE IS BLANK. No ink, no signature, no writing of any kind on the page. NO TEXT IN THE IMAGE IS LEGIBLE. The printed text is realistic in density and layout but soft enough that no word can be read, and no real name, logo, company name or brand appears anywhere. His face is not visible. Nobody else is in the frame. No beauty filter, no smoothing, no airbrushing, no waxy or plastic skin, no CGI sheen, no watermark.
```

### 2-VID — Seedance 2.5, 5 seconds, from the approved still

```
Animate the provided image. Keep the framing, the wardrobe, the room, the light and the colour exactly as they are in the image. Do not add anything and do not change anything.

CAMERA. Handheld throughout. Constant gentle shake, natural breathing sway, small slow drifts. Never a tripod, never a gimbal, never stabilized. Soft and slow, never jerky. One continuous take, no cut.

ACTION. Almost nothing moves. The hand holding the pen stays where it is and makes one small involuntary shift of the fingers on the pen at around two seconds. Around three seconds the flat hand on the page presses down very slightly and settles. He does not sign. The pen never touches the paper. His shoulder rises and falls once with a slow breath.

AUDIO. No music, no score, no dialogue. Natural sound only: air handling, a distant fan, the faint sound of a hand settling on paper, his slow breathing close on the microphone.

FORBIDDEN. The signature line stays blank for the entire clip. No ink appears at any point. No writing. No second person. No zoom, no push, no reveal. No slow motion. Smooth 60fps at natural real-life speed.
```

---

## SHOT 3 — 10.0 to 15.0s. He puts the pen down.

### 3-IMG — GPT Image 2, portrait 9:16

Same room and wardrobe as 1-IMG, wider, and this is the moment before he moves.

```
An ultra-photorealistic RAW photograph in documentary realism style, vertical 9:16, of the exact same man as the reference image. Preserve his facial identity exactly: same face, same short dark brown wavy hair with a faded taper at the sides, same short dark beard and stubble at uneven density, same brown eyes, same thick dark eyebrows, same build.

WARDROBE. He wears a black oversized cotton crew-neck t-shirt with a small white sans-serif wordmark reading [BETA] in square brackets printed centred on the chest, and black straight-cut cotton trousers. No watch, no bracelet, no ring, no chain, no jewellery of any kind. No other logos, no other text and no other branding anywhere on the clothing.

SCENE. The same glass-walled meeting room inside a modern technology office, late at night. He is seated alone at a long pale oak table. In front of him a thick stack of printed contract pages held with a black clip, with a plain black pen lying flat on top of it. Five empty mesh office chairs pushed in around the table at slightly uneven angles. A closed laptop pushed to one side, a half full glass of water with a ring under it, a phone face down, a whiteboard on the far wall with old diagrams half rubbed out. Through the glass wall behind him: the dark open-plan office, rows of empty desks receding into depth, monitors off, a scatter of small standby LEDs, and beyond it a window wall with black city night and scattered distant lights.

HIS STATE. He has sat back into the chair. His forearms have left the table and his hands rest in his lap out of frame. His shoulders are dropped. His head is turned slowly away from the table and he is looking out through the glass wall at the dark empty office, not at the camera. Level and contained. No frown, no jaw clench, no smile, no relief, no triumph. Thinking, not reacting.

CAMERA. Shot on an 85mm lens at f/2, from across the table, low, roughly at table height, framing him from the chest up but wider than a standard portrait so that the empty chairs and more of the empty room read on either side of him. The contract stack with the pen on it sits in the warm pool of light in the lower part of frame. Slightly off-level horizon, as if handheld.

LIGHT. A single warm pendant light hanging low over the centre of the table is the only light source. Warm pool on the table, the contract and the pen, and on his shoulders and the side of his turned face. Deep unlit shadow in the corners of the room.

SEPARATION. His t-shirt is black and the room behind him is dark, so he must not merge into the background. A faint cool edge of light from the monitors and standby LEDs in the office behind the glass catches the top of his shoulders, the side of his neck and the outer edge of his hair. Subtle and cool, never a bright rim, never a halo.

GRADE. Very low saturation, very low contrast, soft gentle falloff, deliberately under exposed. Warm pendant pool against cool dark blue-grey. Fine natural film grain. No orange cast, no vivid colour, no crushed blacks, no blown highlights, no HDR, no bloom, no lens flare.

REALISM. Ultra-realistic RAW skin with visible pores of uneven size, pronounced skin grain, real beard and stubble hairs at individual lengths and uneven density, natural uneven pigmentation, genuine under-eye texture, fine lines, real subsurface scattering. Real brown eyes with visible iris fibres, faint sclera vessels, natural moisture and a small soft catchlight from the pendant. Individual eyelashes and eyebrow hairs. Hair strand by strand with a realistic hairline and natural scalp transition. Real heavy black cotton jersey with an honest visible weave, natural folds and real drape as he sits back, reading as black cloth and not as a flat silhouette. Real paper stack with genuine thickness, slightly uneven page edges and a real soft shadow under the pen. Real pen with a moulded plastic body and one specular highlight. Real oak grain, real chair mechanics, faint cool reflections on the glass wall that never show the camera.

FORBIDDEN. Nobody else in the room and nobody visible anywhere in the office behind the glass. The only text anywhere in the image is the [BETA] wordmark on his chest, spelled exactly B E T A inside square brackets. All other text is soft and unreadable, and no real name, logo, company name or brand appears anywhere. No beauty filter, no skin smoothing, no airbrushing, no waxy or plastic skin, no CGI sheen, no stylization, no watermark.
```

### 3-VID — Seedance 2.5, 5 seconds, from the approved still

The still is the END of the movement, so this one runs the action toward it. If the model handles it badly, generate a second still with him still leaning forward and the pen in his hand, and animate from that instead.

```
Animate the provided image. Keep the framing, the wardrobe, the room, the light and the colour exactly as they are in the image. Do not add anything and do not change anything.

CAMERA. Handheld throughout. Constant gentle shake, natural breathing sway, small drifts and corrections, a slightly off-level horizon. Never a tripod, never a gimbal, never stabilized. Soft and slow, never jerky. One continuous take, no cut.

ACTION. He holds still for the first two seconds, looking out through the glass at the dark office. Then his chest rises and falls with one slow deep breath and his shoulders settle. He holds there, completely still apart from breathing, to the end of the clip. His head does not turn back. He never looks at the camera. He never speaks. His expression stays level and contained the whole time. No smile, no frown, no sigh.

AUDIO. No music, no score, no dialogue. Natural sound only: air handling, a distant fan, the faint creak of an office chair settling, his slow breathing.

FORBIDDEN. He does not pick the pen back up. He does not touch the contract. No second person appears and nobody walks past behind the glass. No zoom, no push, no crane, no reveal. No slow motion. Smooth 60fps at natural real-life speed.
```

---

## Assembly

Three clips, five seconds each, cut hard on the frame. No transitions, no crossfades. Captions on at 0.5s, 5.5s and 11.0s. Total 15 seconds.

Reject any render where: the `[BETA]` wordmark is misspelled, the signature line has ink on it, his shape merges into the dark background, a second person appears in the office behind the glass, or any text on the contract is readable.

---

## Post copy for the reel

Two years before the exit, I had a deal on the table from a private equity firm. Six months of negotiation. Full due diligence. Everything done.

Then it became clear what they intended to do with the company. Cut the team, run it for cash, move on.

Those were people who had taken below-market salaries since day one because they believed we would get somewhere.

I walked away the day before closing. Two years later we sold for more than four times that offer.

The deal you refuse is a decision about who you are willing to be.

---

## Series

Same shape every time. One man, one room, one object, one small physical action.

- 03: the VAT crisis. A kitchen table at night, a bank letter, a phone he does not pick up.
- 04: the DSM-Tool fear. His desk, a competitor's homepage on screen, he closes the laptop.
- 05: the first conference. An empty rented hall, rows of empty chairs, he stands at the front and says nothing.

Film 01, "The Degree", is archived and still good. It needs two character sheets and an age regression, so it waits until this pipeline is proven.
