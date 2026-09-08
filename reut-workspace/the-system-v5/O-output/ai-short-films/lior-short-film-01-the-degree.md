# Short film 01 — "The Degree"
15 seconds. Lior Pozin. Built on the reference reel structure (DbzbABRAb-G) + the craft layer of the Emotional on the Beach prompt.

Date: 2026-09-06
Status: prompt package ready, not generated

---

## 1. The story choice

Canonical, from his own mouth on podcast E97:
> His parents asked "when's the degree?" until the exit.

That is the exact Lior equivalent of the reference reel's "MOM SAID I'D FAIL". It is true, it is on record, and it is a doubter line that costs him nothing to tell.

Paired with the age-21 beat: eBay killed his 7-year main account, so he opened 100 of them and wrote the software himself.

One idea in the film: **they kept asking about the degree while the thing was already being built.**

---

## 2. The device that makes 15 seconds work

**You never see the young man's face. The only face reveal is present-day Lior at 12.0s.**

This does three things at once:
- solves the age problem. We cannot generate a believable 21-year-old Lior from a photo of a 31-year-old. So we do not try.
- keeps the mother a backlit silhouette, so we are not putting a real private person's face into an AI film.
- makes the reveal the payoff. The film pays off on his actual face, not on a car or a watch.

Every young-Lior shot is over the shoulder, from behind, or hands-only. This is the same constraint the beach prompt used to keep the family distant.

---

## 3. Grade shift = the story

Deliberate departure from the beach prompt, which held one flat grade for 12 seconds.

Here the grade carries the arc:
- Shots 1 to 4: warm-dim bedroom night, single laptop source, heavy shadow, tungsten hallway spill, low saturation.
- Shots 5 to 6: cool clean daylight office, wide soft ambient, no shadow, still low saturation.

Same low-contrast, under-exposed, film-grain discipline throughout. The temperature is what moves.

---

## 4. Captions

Burned in, one to four words at a time, bold white with hard black outline, centered lower third. Reference-reel style.

```
0.0s   WHEN ARE YOU GETTING A DEGREE?
5.5s   EBAY BANNED MY ACCOUNT AT 21
9.0s   SO I OPENED 100 MORE
12.5s  THEY STOPPED ASKING
```

No voiceover. No music bed until 12.0s, then one low sustained note under the reveal, or nothing at all.

---

## 5. IMAGE LAYER — character reference sheet for present-day Lior

Run this once with a real, current, front-facing photo of Lior as @image1 and an outfit reference as @image2. Output becomes @image1 for the video prompt. Only the reveal shots need it, but generate it anyway so the film can be extended into a series.

```
Create an ultra-realistic professional character reference sheet of the exact adult man from @image1. Preserve his facial identity and overall appearance consistently in every panel. He wears the complete outfit, shoes, jewelry and accessories from @image2 exactly as shown. Keep the same outfit identical in every view. Keep his hairstyle and facial hair exactly consistent with @image1. Arrange multiple photographs of the SAME man on one neutral muted studio background in this exact layout: LEFT LARGE PANEL: Half-body FRONT view, framed approximately from the waist up. He stands relaxed facing the camera with a calm, level expression, not smiling. His upper-body outfit is clearly visible. MIDDLE LARGE PANEL: Half-body THREE-QUARTER BACK/SIDE view, framed approximately from the waist up. He stands naturally turned slightly away from the camera so the side and back of the outfit can be clearly seen. UPPER RIGHT PANEL: Close-up FRONT portrait of his face, matching @image1 exactly. His face fills most of the panel. LOWER RIGHT LEFT PANEL: Full-body FRONT view, head to feet, standing naturally and showing the complete outfit from @image2. LOWER RIGHT RIGHT PANEL: Full-body THREE-QUARTER BACK/SIDE view, head to feet, naturally showing the complete outfit from the side and back. Every panel must show the exact SAME adult man with the same face, body proportions, hairstyle, facial hair, outfit and accessories. Professional fashion model reference sheet with clean panel divisions and consistent studio lighting. Maximum photographic realism. Render every panel as a genuine RAW studio photograph of a real human. Realistic natural skin with visible pores, fine skin grain, subtle uneven pigmentation, natural under-eye texture, slight natural sheen, fine facial hairs and small real imperfections. Realistic eyes with visible iris fibers and natural moisture. Individual eyelashes, eyebrow hairs and facial hair. Natural hair with thousands of individually visible strands, realistic hairline, natural scalp transition and subtle flyaways. Facial hair must show realistic individual hairs, natural density and subtle irregularities. The outfit from @image2 must have realistic fabric texture, stitching, folds, natural tension and physically accurate material details. Soft directional studio lighting with natural dimensional shadows. Muted, slightly desaturated, true-to-life color grading. Professional RAW photography quality and realistic optical depth. No beauty filter, no skin smoothing, no airbrushing, no waxy or plastic skin, no CGI appearance. The final result should look like five real professional photographs of the same man from the same photoshoot, arranged together as one clean character reference sheet.
```

---

## 6. VIDEO LAYER — master 15 second prompt

Feed the character sheet as @image1. If the model caps below 15s, split at the 8.5s mark and cut the two halves together; the grade shift lands on that seam anyway.

```
EVERY SINGLE SHOT IS HANDHELD. Shot as if a real person is holding the camera, constant gentle shake, natural breathing sway, small drifts and corrections, slightly off-level horizons, faint motion blur at the frame edges. Never a tripod, never a gimbal, never stabilized, never locked off. The motion is soft and slow in the bedroom shots and quicker and looser in the night montage. Smooth 60fps, natural real-life speed, no slow motion. No dialogue. Nobody speaks. Silent apart from ambient sound.

SETTING ONE, SHOTS 1 TO 4, DETAILED
A small bedroom in a modest apartment in a hot dry Israeli city, night, mid 2010s. The room: a cheap laminate desk pushed against the wall under a window with metal roller shutters half closed, thin horizontal bars of orange streetlight cutting across the wall behind it. A worn office chair with a cracked armrest. Beige floor tiles, scuffed. A single overhead fixture switched off, so the only light in the room is the laptop screen and a strip of warm tungsten spill from the hallway doorway behind him. On the desk: an old aluminium laptop, a cheap wired mouse, a tangle of chargers, a glass of water with condensation, a spiral notebook covered in handwriting and crossed-out numbers, a roll of packing tape, scissors. On the wall above the desk: a grid of small paper notes stuck up with masking tape, handwritten, uneven, some peeling at a corner. On the floor around the chair: flat poly mailers, bubble wrap offcuts, a cardboard box with the flaps open, a pair of trainers kicked off. A wardrobe with one door not quite shut. A bed in the corner, unmade, with a folded stack of packed parcels on it where a pillow should be. Behind him through the open doorway: a narrow hallway, warm tungsten light, a coat hook, the edge of a kitchen counter, the flicker of a television somewhere off to the side.

SETTING TWO, SHOTS 5 TO 6, DETAILED
A modern open-plan technology office, daytime, overcast light through a full glass wall. Long desks in rows receding into the depth of frame, dual monitors, cable trays, mesh chairs. People working at the far desks, none of them close enough to read, none of them looking at camera. A whiteboard on the far wall covered in diagrams. Plants in plain pots. Concrete ceiling, exposed ducting, soft even ambient light with no hard shadow. A glass meeting room to one side with people inside, silent behind the glass.

GRADE
Very low saturation throughout. Very low contrast throughout. Fine natural film grain in every frame. Deliberately under exposed.
SHOTS 1 TO 4 are warm and dim, lit only by laptop screen and hallway tungsten spill, deep unlit corners, amber and dark brown and dull orange, screen light cool on his face and hands against that warmth.
SHOTS 5 TO 6 are cool and clean, flat overcast daylight, pale grey and soft white and desaturated blue, no shadow, no warmth at all.
The temperature change from shot 4 to shot 5 is the only visual event that carries any weight. No golden hour, no orange sunset, no crushed blacks, no blown highlights, no HDR, no bloom, no lens flare, no vivid colour anywhere.

THE YOUNG MAN, SHOTS 1 TO 4
Early twenties, slim build, short dark hair. He wears a plain washed grey t-shirt and dark track shorts, barefoot. HIS FACE IS NEVER VISIBLE AT ANY POINT IN SHOTS 1 TO 4. He is filmed only from behind, over the shoulder, from the back of the head, or hands-only. No reflection of his face in the laptop screen or the window. No profile. Nothing readable. He is a back, a pair of shoulders, a pair of hands.

THE WOMAN IN THE DOORWAY, SHOT 1
An adult woman standing in the bedroom doorway, backlit by the warm hallway light behind her so that she reads as a dark silhouette with a soft warm rim on her hair and shoulders. HER FACE IS NEVER READABLE. No features, no expression, no detail. She stands with one hand still on the door frame, weight on one leg, and she is talking. Her posture is tired and ordinary, not angry.

THE MAN, SHOTS 5 TO 6
He looks exactly like the man in the character sheet @image1. Same face, same identity, same build, same hair, same facial hair. He wears the exact outfit from @image1. Early thirties, calm, level, not smiling. Same seated posture as the young man in shot 4: leaning slightly forward, forearms on the desk, shoulders squared to a laptop.

AUDIO
No music, no score, no dialogue, no intelligible speech. Natural sound only. Shots 1 to 4: the hum of a laptop fan, a hard-drive tick, the click of a mouse, tape ripping off a roll, a plastic mailer crinkling, an air conditioner outside the shutters, a scooter passing far below, the muffled unintelligible murmur of a television down the hallway, a woman's voice speaking in the doorway, warm and close but the words never clear. Shots 5 to 6: flat office room tone, distant keyboards, a chair rolling, muted voices behind glass, air handling.

TIMELINE, 6 SHOTS

0.0 to 2.5s, OVER HIS SHOULDER TOWARD THE DOORWAY. Camera low and close behind his right shoulder, so the back of his head, his shoulder and the edge of the chair sit large, soft and dark in the near foreground on one side of frame. Past him: the desk edge, the glow of the laptop washing up the wall of paper notes, and beyond it the open bedroom door with the woman standing in it, small, backlit, a silhouette against warm hallway light. She is talking, one hand on the door frame. He does not turn around. His head stays facing the screen. Only his shoulders rise and settle once with a breath. Camera drifting very slightly. Sound: her voice warm and unclear, laptop fan, television murmur.

2.5 to 5.5s, OVER HIS SHOULDER ONTO THE SCREEN. Camera tighter behind his left shoulder now, angled down toward the laptop, his shoulder and the back of his head soft and dark filling one edge. On the screen, readable but slightly out of focus: a marketplace seller dashboard, a listing grid, and across the top a flat red banner. His hands sit still on the keyboard, not typing. He does not move for the whole shot. One long breath. The paper notes on the wall soft in the background. Camera drifting, breathing. Sound: laptop fan, one distant scooter, the doorway now quiet.

5.5 to 8.5s, NIGHT MONTAGE, HANDS AND ROOM ONLY. Faster handheld, looser, quicker drift. A sequence of overlapping fragments in the same room with no face at any point: hands typing fast in the screen glow, veins and tendons visible; a hand pressing a fresh paper note onto the wall next to a dozen others; the same wall a moment later with three times as many notes; a hand tearing packing tape across a mailer; the water glass now empty; the light through the shutters shifting from black to pale grey to black again as nights pass; the stack of packed parcels on the bed growing taller between fragments. The camera never rises above shoulder height and never finds his face. Sound: tape, keyboard, mailer crinkle, air conditioner, the room tone tightening.

8.5 to 11.0s, WIDE, FROM BEHIND, THE ROOM FULL. Camera far back and low near the bedroom door, looking in past the door frame so the frame is slightly boxed in by the dark edge of the doorway. The room is now packed. Parcels stacked floor to ceiling along both walls, on the bed, under the desk, in the open wardrobe. The wall above the desk is entirely covered in paper notes. He is small in frame, seen only from behind, sitting in the chair in the middle of it, lit by the laptop, shoulders forward, completely still. The doorway is empty behind the camera. Hold. Camera breathing gently. Sound: laptop fan, air conditioner, nothing else.

11.0 to 13.0s, MATCH CUT, SAME FRAMING, TEN YEARS LATER, HIS FACE. Identical camera position and identical framing to the previous shot, but the world has changed around him and the grade has gone cool and flat. He is in the same seated posture, same shoulders-forward lean, same distance from camera, but now in the modern office, and now the camera arcs slowly around to his side and settles on a three-quarter front angle at chest height. HIS FACE IS FULLY VISIBLE FOR THE FIRST TIME IN THE FILM. He matches @image1 exactly. He is working, not performing, eyes on the screen, level and unhurried. Rows of desks and people receding behind him. Sound: office room tone, distant keyboards, a rolling chair.

13.0 to 15.0s, SLOW PUSH, HE LOOKS UP. Same three-quarter front angle, camera easing in very slightly, still handheld and breathing. He finishes something on the keyboard, then lifts his eyes off the screen and looks off to the side of the lens, not into it, and holds. No smile. No nod. Just a man who stopped for a second. Behind him the office keeps moving, soft and out of focus. Hold to the end. Cut.

VISUAL STYLE
EVERY SHOT IS HANDHELD WITH VISIBLE BUT GENTLE CAMERA MOTION. Soft shake, sway, drift, breathing, slightly off-level horizons. No tripod, no gimbal, no stabilization, no static frames.
THE YOUNG MAN'S FACE IS NEVER SEEN IN SHOTS 1 TO 4. Not in profile, not in reflection, not partially. Back of head, over the shoulder, and hands only. This is absolute.
THE WOMAN IN THE DOORWAY IS ALWAYS A BACKLIT SILHOUETTE. Her face is never readable at any point. Posture and rim light only.
THE FIRST AND ONLY FACE IN THE FILM IS HIS, AT 11.0s. He must match @image1 exactly, same face, same build, same hair, same outfit. No substitutions.
SHOT 4 AND SHOT 5 MUST SHARE THE SAME CAMERA POSITION AND FRAMING so the cut reads as a match cut across ten years.
GRADE SHIFT: warm dim tungsten and screen glow for shots 1 to 4, cool flat overcast daylight for shots 5 to 6. Low contrast, low saturation, under exposed, film grain in both halves.
Ultra-realistic RAW skin with visible pores of uneven size, pronounced skin grain, real stubble at individual lengths and uneven density, natural uneven pigmentation, genuine under-eye texture, fine lines, real subsurface scattering. Screen light falling correctly and unevenly across skin, cool on one side and unlit on the other. Real eyes with visible iris fibres, faint sclera vessels, natural moisture, authentic soft catchlights from the laptop. Anatomically correct hands, correct finger count and joint bend, real knuckle creases, raised veins and tendon movement while typing. Real hair strand by strand with a realistic hairline and natural scalp transition.
No beauty filter, no smoothing, no airbrushing, no plastic or wax skin, no CGI sheen.
Real environmental detail: scuffed floor tiles, dust visible in the beam of screen light, fingerprints and grease on the laptop palm rest, worn lettering on the keyboard, curling corners on the taped paper notes, creased and re-used cardboard, real tape texture with air bubbles under it, chipped paint on the door frame, condensation ring on the desk from the glass.
Realistic optical depth of field with the hallway and the far end of the office falling into genuine soft focus. Smooth 60fps.
Natural audio only, no music, no score, no dialogue, no intelligible words at any point.
```

---

## 7. Post copy for the reel

Caption under the video, IG:

Nobody asks about the degree anymore.

At 21 eBay closed the account that was paying my rent. Seven years of selling, gone in one email. I opened 100 new ones and wrote software so I could actually manage them. That software is AutoDS.

My parents kept asking about the degree for years after that. They stopped somewhere around the acquisition.

If you are building something nobody in your house understands yet, that is not the signal you think it is.

---

## 8. Series potential

Same device, same 15 second shape, one true doubter line each time:
- 02: the VAT crisis. Advisor wants 30K he does not have. Ends on the first conference room, full.
- 03: DSM-Tool. The competitor he was afraid of for years. Ends on the acquisition signature.
- 04: walking away from the PE deal one day before closing. Ends on an unsigned page.

Each one reuses the same character sheet, the same grade-shift logic, and the same face-reveal-at-the-end rule.
