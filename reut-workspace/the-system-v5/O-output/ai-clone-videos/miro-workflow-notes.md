# Nicola's Miro Workflow — Image / Upscale / Video (Veo 3.1)

Captured 2026-07-13 from Reut's screenshot of the Miro board
(https://miro.com/app/board/uXjVG4RJp5M=/). This is the CORE 3-part pipeline and it
updates the Notion guide in two ways: images are created in **NanoBanana PRO** (not
HiggsField), and video prompts target **Veo 3.1** with a plain-text 7-part structure
(not the JSON from the Notion guide). Treat this as the current method.

## 1 — IMAGE

- Decide who you want to clone and what you want to create (e.g. "me in a high
  authority setup"). References can include the setup, outfit, accessories, or
  anything else you want to add to the image.
- Go to the NANOBANANA project inside ChatGPT. Upload the face of the subject you
  want to clone + any references.
- Request to ChatGPT (structure for the prompt):

```
Write me a prompt for NanoBanana PRO following the rules described in the sources of
this project. Strictly follow that structure, do not change it.

I want the exact same subject to be represented in the photo, with the same skin
texture, face shape, and everything exactly as in Photo #1 that I provided.
From there, you need to describe THE SUBJECT:
- The pose of the subject (sitting, standing, etc.)
- The attitude of the subject (smiling, crying, serious, neutral)
- What he is doing
- Where he is looking (directly at the camera / not at the camera)
- What he is wearing (describe or refer to the reference image to copy the style)
- Any additional relevant details about the subject
Then describe the CAMERA AND SETUP:
- The frame (mid-body, full-body, close-up of the face, etc.)
- The setup (describe the environment or refer to the reference image to copy the style)
```

- Create the image in NanoBanana. **Always generate multiple images for the same
  prompt.**
- If something is wrong with the prompt: tell ChatGPT
  `give me the same exact prompt, but change: ...` — type only what you want to
  change, nothing else.
- Once you have the image you like → Part 2.

## 2 — UPSCALE

- LUPA, **6K Precision always**, grain off.
- Only upscale images in which the subject is CLOSE to the camera. If the subject is
  far away and skin texture is not clearly visible, upscaling is somewhat useless.

## 3 — VIDEO (Veo 3.1)

Decide your script and optimize it for Veo 3.1.

### Script formatting guidelines
- **Commas** = natural pause in the speech.
- **Exclamation points** = phrase delivered with strong confidence.
- Length: adapt the script to fit **~8 seconds maximum**; ideally max 2 lines
  (Google Doc, Arial 11), minimum 1 line, maximum 2 lines.
- Phrase too long → cut at the most natural point.
- Phrase too short → add the beginning of the next sentence (only if it doesn't
  interrupt the meaning), or add filler words.
- To extend for better final delivery, Nicola usually adds:
  `"Oh and by the way this is crazy guys!"` (or a longer variation) — cut in editing.

### Structure of the video prompt (7 parts, plain text)
1. **Subject Behavior** — speaks naturally and realistically; communication style
   natural, not exaggerated.
2. **Tone** — relaxed and calm / excited and powerful. ← set per line (the v1 miss)
3. **Language** — American English (or any you choose).
4. **Gestures** — must match the meaning of the sentence; movements remain centered.
5. **Camera** — 100% stable, no zoom at any point, no push-in or pull-out, no camera
   shake, subject stays at the exact same distance for the entire video, no
   perspective changes.
6. **Audio & Visual Restrictions** — no on-screen text, no music, no background
   voices, no other people speaking, only the subject speaks.
7. **Script** — exact phrase: "YOUR PHRASE"

### Example prompt (verbatim from board)
```
The subject in the photo speaks and communicates in a natural and realistic way.
Tone: excited and energetic.
Gestures: aligned with the meaning of the sentence, always centered and at chest height.
Language: American English.
Camera: no zoom, 100% stable for the entire video.
The subject remains at the same distance from the camera for the entire video.
No on-screen text.
No music.
No additional voices.
Only the subject speaks.
Phrase:
"Being first you need to stay ahead of the game! If all your competitors are doing
something, do the opposite!"
```

### Generation economics
- **Always create videos in FAST / lower priority first because it's free.** Goal:
  evaluate whether the prompt is good and the phrase length appropriate.
- If both are satisfactory → regenerate in QUALITY mode and select the best version.

### Batch trick — additional videos, same subject + setup
Once the first video works, tell ChatGPT:
```
From now on, I will type only the phrase I want the subject to say.
Each time, create a new prompt using the exact same structure and format as before,
with the same photo, the same subject, and the same overall attitude.
Only adapt the gestures so they match the meaning and energy of the new phrase.
```
From there you literally type only the new phrase and copy-paste each new prompt.

## Differences vs the Notion 1:1 LIVE STAGE guide

| Topic | Notion guide | Miro board (current) |
|---|---|---|
| Image tool | HiggsField | NanoBanana PRO |
| Video prompt | JSON via ChatGPT VEO folder | 7-part plain-text structure |
| Veo version | unspecified ("VEO LITE") | Veo 3.1, FAST free → QUALITY |
| Clip length | max 2 lines | ~8s max, 1-2 lines, punctuation controls pacing |
