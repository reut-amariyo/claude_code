# HiggsField Prompt — Lior Podcast Interview Look (2026-08-30)

Replaces the old "change nothing in the video" edit prompt. That one was a preservation
prompt, it can only protect what already exists. This one is a generation prompt: it
describes the shot we want, so the model has something to aim at.

Key fix carried over: the line "Say it again please" belongs to a SECOND, off-camera
male voice (the interviewer), never to Lior.

---

## PROMPT A — main shot, Lior answering (copy-paste)

Photorealistic podcast interview, one continuous take, no cuts. Vertical 9:16, medium close-up framed from mid-chest up, subject centered and dominant in frame.

The same man as in the reference, identity locked frame by frame: exact face, bone structure, hairline, beard, skin tone and natural skin texture with visible pores and subtle asymmetry, his hands, and the same clothing as the reference.

Watch replacement, the one deliberate change: remove the Apple Watch on his left wrist and replace it with a Patek Philippe Aquanaut 5167R-001. 18k rose gold rounded octagonal case with a warm pink-gold shine, brown embossed dial with the Aquanaut checkerboard grid pattern, applied luminous gold Arabic numerals, and a matching brown Tropical composite rubber strap with the same embossed grid, on a rose gold folding clasp. Case around 40mm, sitting slightly loose just behind the wrist bone. Realistic metal behavior: warm gold reflections that shift as his hand moves, soft specular highlights on the polished bezel, a real contact shadow where the strap meets skin. No square screen, no digital display, no black rubber sport band, no rectangular case. His wrist, hand and sleeve stay exactly as in the reference.

He is seated in a dark, high-end podcast studio, deep in the middle of a long conversation, not at the start of one. A broadcast microphone on a boom arm enters from the left toward his mouth, clearly visible but never crossing his face. Behind him, dark acoustic slat panels fall softly out of focus with a warm practical lamp glowing far back on the right.

Performance: calm, low, unhurried delivery with real pauses between thoughts, a light Israeli accent, slight forward lean when he makes his point. Eye contact stays on the interviewer just off the lens, never into the camera. One relaxed hand gesture at chest height, small head tilts, natural blinking. His smile is small and closed-mouth, teeth barely visible, never a wide grin.

He says: "[LIOR LINE HERE]"

Then a second male voice, off camera, further from the mic, warmer and slightly higher than his, says: "Say it again please." While that line plays, Lior does not speak. He holds eye contact, gives one small nod, and stays still for half a beat before answering.

Camera: locked on a tripod, zero movement, no zoom, no push-in. 50mm lens at f/2, shallow depth of field, focus fixed on his eyes.

Lighting: soft key at 45 degrees above camera left shaping his cheek, gentle warm fill on the shadow side, subtle rim light separating him from the dark background. Warm, restrained, consistent from first frame to last.

Audio: dialogue only over quiet studio room tone. No music, no audience, no reverb.

Do not: move the camera, morph or reshape the face, change skin, lighting or color mid-shot, add people, add captions or text or logos, add music, animate a wide smile, let the lip sync drift off the words, or let the watch flicker, change model, or revert to an Apple Watch at any point in the shot.

---

## PROMPT B — cutaway, interviewer line only

Same studio, same continuous-take realism. The subject from the reference is listening, not talking. Vertical 9:16, medium close-up, camera locked.

He listens: mouth closed and still, eyes on the interviewer off lens, one slow blink, one small nod, a faint closed-mouth smile starting at the corner of his mouth. His hands rest still. Absolutely no lip movement, he is not speaking in this shot.

On his left wrist, the same Patek Philippe Aquanaut 5167R-001 as the previous shot: rose gold rounded octagonal case, brown embossed checkerboard dial, brown Tropical rubber strap, rose gold folding clasp. Identical watch, identical position on the wrist. No Apple Watch, no digital display.

Off camera, a male interviewer's voice says: "Say it again please."

Lighting, lens, framing and background identical to the previous shot so the two cut together seamlessly. Dialogue plus quiet room tone only.

Do not: animate his lips, move the camera, change framing or lighting, add text or music, or change the watch.

---

## Watch reference

Patek Philippe Aquanaut 5167R-001, rose gold, brown dial (2022).
https://wristaficionado.com/products/patek-philippe-aquanaut-5167r-001-rose-gold-brown-dial-2022

Feed a still of the watch as a second reference image if the tool accepts one. Text alone
gets the color and shape right but usually loses the embossed grid on the dial and strap.

## Notes for the render

- Paste PROMPT A once per Lior clip, swapping only the [LIOR LINE HERE] bracket.
- Keep every clip 6-8s. Add a throwaway word at the end of each line so delivery speeds
  up, the editor cuts it.
- Two images max across the whole video, one per character, same venue. Carried from
  Nicola's Loom.
- Render in Google Flow / Veo for the final if HiggsField leaves a watermark.
- Check the watch on every frame where his left hand crosses frame. Wrist swaps are the
  first thing to break when the hand moves fast, so keep gestures slow and at chest height.
- Cheaper alternative if the video keeps reverting: swap the watch on the still image first
  (NanoBanana, two-image outfit prompt), then animate from the corrected still.

---

## IMAGE PROMPT — build the still first, then animate

Do this before any video. Fix the watch in a single frame, approve it, and animate from
that corrected still. Video models rarely invent a watch correctly, but they copy one
that is already in the source frame.

**Upload two images:** image 1 = the Lior photo we want to animate. image 2 = a clean
product shot of the Aquanaut, ideally a 3/4 angle showing dial and strap together, plain
background, as high res as the page has.

### Two-image prompt (copy-paste)

Photorealistic RAW photograph. Keep image 1 exactly as it is: same man, same face, bone structure, hairline, beard, skin tone and natural skin texture with visible pores, same expression, same pose, same hands and finger positions, same clothing, same microphone, same background, same lighting, same framing and crop.

Change one thing only. Remove the Apple Watch from his left wrist and put the watch from image 2 in its place: Patek Philippe Aquanaut 5167R-001, 18k rose gold rounded octagonal case, brown embossed dial with the Aquanaut checkerboard grid, applied luminous gold Arabic numerals, brown Tropical composite rubber strap with the same embossed grid, rose gold folding clasp.

The watch must sit on his wrist the way a real 40mm watch sits: correct scale against his forearm, slightly loose just behind the wrist bone, strap curving with the wrist and casting a soft contact shadow where it meets skin. The case picks up the same warm key light as his face and hands, with soft specular highlights on the polished bezel and a natural gold reflection on the underside. Dial legible, grid pattern visible, no warped text or fake logo.

Shot on 85mm f/1.4, shallow depth of field, focus on his face with the wrist naturally slightly softer. No stylization, no beauty retouching, no color grade change.

Do not: alter his face, skin, hair, expression, pose or clothing, change the background or lighting, crop or rezoom the frame, leave any square screen, digital display or black sport band, duplicate the watch, or add a second watch on the right wrist.

### Text-only fallback if the tool takes one image

Same prompt, replace "the watch from image 2" with the full spec sentence starting at
"Patek Philippe Aquanaut 5167R-001, 18k rose gold...". Expect to lose the embossed grid
on the dial and strap. Two images is worth the extra upload.

### Check before you animate

- [ ] Scale reads right against his forearm, not oversized
- [ ] Strap bends with the wrist, no floating band
- [ ] Contact shadow under the strap
- [ ] Gold matches the room's warm light, not a flat orange
- [ ] Face and background pixel-identical to the source

---

## LIP-SYNC PROMPT — drop Lior's real voice onto the rendered clip

For the 13.04s render hf_20260830_122222 (720x1280, 24fps, watch corrected).
Upload the video + the voice file, mute the video's original audio track first.

### Prompt (copy-paste)

Use the uploaded audio file as the only voice in this video. Replace the existing audio track completely and re-sync his mouth to the new speech, word by word, from the first frame to the last.

Keep everything else in the source video exactly as it is, frame by frame: his identity, face, bone structure, skin texture, beard, hair, eyes and blinking, head movements, hand gestures, the rose gold Patek Philippe Aquanaut on his left wrist with its brown dial and brown strap, the ring on his finger, his black t-shirt, the microphone and boom arm, the wooden table, the dark acoustic panels, the warm lamp on the right, the lighting, the framing and the camera timing.

Only the mouth, jaw and the muscles immediately around them may change, and only as much as the new words require. Lip shapes must match the consonants and vowels of the audio, the jaw opens and closes on the syllables, the corners of the mouth move naturally with his speech, and he closes his mouth during pauses. His smile stays small and closed-mouth, teeth barely visible, never a wide grin.

When his hand passes in front of his mouth, keep the hand in front. Do not erase it, do not make the mouth show through it, do not shift the hand to reveal the lips.

Do not: change his identity or face proportions, morph or smear the jaw, add teeth that were not there, change skin tone or lighting, alter the watch, move the camera, re-crop the frame, add background music, add captions or text, or leave any of the original voice audible under the new one.

### Flags before you upload

- The video is 13.04s. Trim the voice file to 13.0s or shorter, otherwise the tail gets
  cut mid-word. If it is shorter, the last seconds render as silence with a moving mouth.
- Around 0:01 his hand crosses in front of his mouth. That is the single most likely
  place for the sync to break. Check that frame first in the output.
- If the tool re-renders the whole face instead of the mouth region, re-run with only the
  first paragraph plus the negatives. Long identity lists sometimes push these models into
  a full regeneration.
