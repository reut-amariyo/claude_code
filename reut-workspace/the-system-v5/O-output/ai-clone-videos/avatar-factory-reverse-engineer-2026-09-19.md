# Reverse-engineering the "Lior / Avatar Factory" reference video

Source: `~/Downloads/lior ai- avatar factory .mp4`, 34 s, 1080x1920, 2026-09-19.
Watched frame by frame (2 fps contact sheet) + local Whisper transcript.

## 1. What this video actually is

It is an ad for Avatar Factory, made inside Avatar Factory. The tool's own logo appears
on the app mockup at 0:16-0:20 and again in the end card "My team uses Avatar Factory".
The transcript ends with "Comment Avatar and I'll send you the link", a lead-gen close.

That matters for the reverse-engineering: there is no single text-to-video prompt.
The pipeline was **one reference image + a script**, plus two AI B-roll shots and a
motion-graphics edit. Below is each layer so you can rebuild any of them with any
avatar tool (Avatar Factory, HeyGen Avatar IV, HiggsField Speak, Kling Avatar,
Veo 3 with a reference frame).

## 2. Shot list (timecoded)

| Time | Shot | How it was made |
|---|---|---|
| 0:00-0:04 | A-roll: Lior at a dark wood desk, dark office, holding a fluffy lav mic like a lollipop | Reference image → avatar lip-sync |
| 0:04-0:08 | B-roll: Lior from behind, staring up at a huge minimalist wall clock in a concrete loft | Image gen → image-to-video, slow push-in |
| 0:08-0:14 | A-roll again, same desk shot | Same avatar clip, continued |
| 0:14-0:16 | Black card, white kinetic text "So now, this is the process:" | Motion graphics |
| 0:16-0:20 | App mockup: "Upload photo" → photo drops in → "Script" panel fills → cursor hits yellow "Generate" | Screen mockup / After Effects, not a real recording |
| 0:20-0:28 | A-roll, with 6-8 floating "avatar variant" cards orbiting Lior at 0:22-0:25 | Same avatar clip + generated stills composited |
| 0:25-0:28 | B-roll: Lior in profile on a black stool in a white cyc studio, softbox, LED panel, camera operator with headphones | Image gen → image-to-video |
| 0:28-0:31 | Black card: logo + "My team uses Avatar Factory to create these videos." over a grid of ~15 avatar variants | Motion graphics |
| 0:31-0:34 | A-roll close: "Comment AVATAR and I'll send you the link" | Same avatar clip |

Edit signature: word-by-word captions, white Inter-style sans for the sentence, one
emphasis word per phrase in **yellow serif italics** (Instrument Serif / Playfair look).
Yellow #F5F542-ish is the brand colour of the app. Zooms in on every A-roll cut.

## 3. The script (verbatim, 11 lines, ~75 words)

--- SCRIPT STARTS ---
I told my team I'm not spending hours filming content anymore.
As a founder, you have to choose what actually deserves your time.
And if AI can do something without changing the idea or the message, why would I keep doing it manually?
So now this is the process.
Upload a photo of me, add the script, generate.
And you get this.
It's still my ideas, my stories, my content.
I just don't need to be in front of a camera every time.
My team uses Avatar Factory to create these videos.
Comment Avatar and I'll send you the link.
--- SCRIPT ENDS ---

Structure: confession hook → founder principle → logic bridge → 3-step process →
reveal ("and you get this") → objection handled (still my ideas) → tool name → CTA.
This is the template the app's demo videos all follow. For our own use the last two
lines get swapped for Lior's real close.

## 4. Layer 1: the anchor image (the important asset)

This is the still that the whole talking-head is driven from. Everything about it is
chosen to make lip-sync forgiving: static torso, hands anchored on the desk, dark
background, soft even key light, no moving hair or hard shadows.

Use with the NanoBanana PRO structure from `v2-production-plan.md` (upload a real
candid photo of Lior as Photo #1):

```
Write me a prompt for NanoBanana PRO following the rules described in the sources of this project. Strictly follow that structure, do not change it.
I want the exact same subject to be represented in the photo, with the same skin texture, face shape, hairline, stubble and everything exactly as in Photo #1 that I provided.

THE SUBJECT:
- Pose: seated at a dark walnut desk, upper body square to camera, left forearm resting flat on the desk, right hand raised to chest height holding a small wireless lavalier microphone with a grey fluffy windscreen between thumb and index finger, like holding a lollipop
- Attitude: relaxed, direct, mid-sentence, slight closed-mouth half smile
- Doing: talking straight to the camera as if recording a short video
- Looking: directly into the lens
- Wearing: plain black oversized cotton t-shirt with small white monospace chest print that reads [BETA] in square brackets, thin black fabric-strap watch with a gold case on the left wrist, thin gold wedding band
- Additional: natural skin texture with visible pores, 3-day stubble, short dark fade haircut with textured top, no retouching

CAMERA AND SETUP:
- Frame: vertical 9:16, medium shot from mid-chest up, eye level, 50mm look, shallow depth of field
- Lighting: soft large key light from camera-left slightly above eye level, warm practical fill from a lamp behind on the right, no hard shadows, cinematic low-key exposure
- Setup: moody dark home-office studio. Behind him a black matte wall on the left, a vertical dark-wood slat panel on the right with a built-in shelf unit holding a few hardcover books, a small glowing Edison-bulb lamp, and a trailing pothos plant hanging from the top shelf. Black mesh office chair partly visible. Dark walnut desk surface in the foreground. Colour palette black, walnut brown, warm amber, green plant accent. No on-screen text anywhere.
```

Why the lav-in-hand detail: it gives the avatar a fixed prop near the face, which hides
the slightly dead hands most avatar engines produce. Keep it.

## 5. Layer 2: the B-roll images

Same subject rules as above, then swap SUBJECT + SETUP. Both shots are deliberately
"Lior NOT talking" so the avatar engine only has to lip-sync the desk shot.

### B-roll A: the wall clock (0:04-0:08)

```
THE SUBJECT:
- Pose: standing, seen fully from behind, weight even on both feet, arms relaxed at his sides
- Attitude: still, contemplative
- Doing: looking up at an oversized wall clock
- Looking: at the clock, back fully to camera, face not visible
- Wearing: plain black t-shirt, dark charcoal chinos, white low-top sneakers, black strap watch
- Additional: short dark textured haircut visible from behind

CAMERA AND SETUP:
- Frame: vertical 9:16, wide full-body shot, subject in the lower third, clock filling the upper half, eye level, 35mm
- Lighting: bright natural daylight from tall factory windows on the left, soft shadows on a polished concrete floor
- Setup: minimalist industrial loft office. Raw grey concrete wall, one huge round wall clock with a white face, thick black rim and black hour markers, no numbers. Tall black steel-frame windows on the left with city and trees outside, a large potted plant in a concrete planter, a glass-walled meeting room on the right, exposed ductwork on the ceiling. Clean, quiet, almost empty. No on-screen text.
```

Video prompt for this still (Veo / Kling image-to-video, 4-5 s):
```
Slow cinematic push-in toward the man and the clock, camera dolly forward at walking pace, the man stays completely still, the clock's second hand ticks, dust motes in the window light, no camera shake, no other people, photoreal, 24fps.
```

### B-roll B: the studio (0:25-0:28)

```
THE SUBJECT:
- Pose: seated on a tall black metal stool, left profile to camera, both feet on the stool's footrest, leaning slightly forward
- Attitude: engaged, mid-explanation
- Doing: talking to an off-screen interviewer, hands gesturing at chest height, fingers open
- Looking: slightly camera-right, at the interviewer, never at the lens
- Wearing: same black [BETA] t-shirt, black jeans, grey and white New Balance style sneakers, black strap watch
- Additional: same face, hair and stubble as Photo #1

CAMERA AND SETUP:
- Frame: vertical 9:16, wide behind-the-scenes shot, subject on the left third, film crew on the right third
- Lighting: bright white cyclorama studio, one large octagonal softbox top right, one LED panel light on a stand in the middle, clean even exposure
- Setup: seamless white infinity studio. In the right foreground, the back of a camera operator in a black hoodie with over-ear headphones, cinema camera on a tripod with the small flip-out monitor showing the man's face. Light stands with cables on the floor. Making-of, documentary feel. No on-screen text.
```

Video prompt:
```
Static tripod shot, the man on the stool gestures naturally while speaking, the camera operator adjusts focus with a small hand movement, softbox light steady, subtle natural motion only, photoreal, 24fps.
```

## 6. Layer 3: the variant grid (0:22-0:25 and 0:28-0:31)

The floating cards are 6-8 extra stills of the same face in different rooms and shirts,
each one animated for 2-3 seconds. This is the "one photo, endless videos" proof shot.
Generate them as a batch by changing only two lines of the anchor prompt:

- Wearing: white [BETA] tee / black [BETA] tee / plain white tee
- Setup: bright home office with bookshelf and daylight / tan leather armchair by a
  night-time city window / cream sofa in a sunlit living room / grey office with a
  floor lamp / dark studio with a wooden slat wall

Keep the lav mic in hand in every variant, it is the visual thread that says "same
creator, same setup".

## 7. Layer 4: the avatar step

Avatar Factory's own UI in the video shows exactly two inputs: **Upload photo** and
**Script**, with the tagline "Your words. Your voice." So the audio is a voice clone,
not a recording. Rebuilding it in our stack:

1. Anchor image → LUPA upscale, Precision, 6K, no grain, as in Nicola's notes.
2. Script → ElevenLabs with Lior's cloned voice, one take, no music.
3. Image + audio → avatar engine. HeyGen Avatar IV or HiggsField Speak both accept a
   still + audio and produce the hand-and-torso micro-motion seen here. Kling Avatar
   also works. Cap each clip at 15 s and cut between two anchor angles if the script
   runs longer, the same rule Nicola gave for the stage video.
4. B-roll: image-to-video on the two stills above, 4-5 s each.
5. Edit in CapCut: word-by-word captions, one yellow serif emphasis word per line,
   black cards for section breaks, 3-5% punch-in on each A-roll cut.

## 8. Notes before we use it

- Same face, same set, same shirt on every card is what sells the "my avatar" idea.
  The [BETA] tee also reads as our own "[ life is beta ]" lockup, so it fits Lior's VI
  without changing a thing.
- The talking-head is capped under 40 s, matching our IG rule for talking heads.
- Lior should NOT say "my team uses X" for any tool we are not partnered with. If we
  copy this video's structure the last two lines become a Lior close, for example the
  "comment AVATAR" gate becomes a real artifact giveaway.
- The clock B-roll is the strongest visual idea: it says "time" without Lior on
  camera and needs zero lip-sync. Reusable for every founder-time post.
