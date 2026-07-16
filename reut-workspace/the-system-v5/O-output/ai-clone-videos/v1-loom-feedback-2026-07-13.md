# Nicola's Loom Feedback on v1 — 2026-07-13

Loom: https://www.loom.com/share/628dcccec5d24db3a005a7e5ee68552f
Video reviewed: "download (1) (1).mp4" (28s, 1080x1920, woman asks from audience / Lior answers on stage)

Verdict: rejected. "Honestly, I don't like it." Encouraging close: "this is just the
beginning… we will increase the quality a lot."

## v1 script (transcribed)

WOMAN: I have an idea for a business, but I'm terrified.
LIOR: Of what?
WOMAN: Quitting my job. Everyone says you need to go all in.
LIOR: Who said you need to quit? Your salary is your runway.
WOMAN: So how do I start?
LIOR: Just start. Get one paying customer this month.
WOMAN: Just one customer?
LIOR: One real customer teaches you more than a year of planning. Start now. Fix later.

Note: Nicola did NOT criticize the script content — he said given this script, the
1:1 format is the right one. The problems are all execution.

## The 6 problems

1. **The base image, not just the video.** The lighting is "a bit too perfect" — reads
   AI. Fix: search Pinterest for real photos ("live conference questions"), pick a real
   setup/background with a real person, then swap only the face and subject. Real
   scene + swapped person > fully generated scene.

2. **Format mixing.** v1 blends two formats: audience-question style and the 1:1 stage
   style. For this script use the pure 1:1 format: exactly TWO images, one of her and
   one of Lior on stage, then cut between them in editing.

3. **Moving camera.** Nicola dislikes camera movement here. Camera must be FIXED
   (matches his JSON prompt spec: static, no zoom, no movement).

4. **No tonality, too slow, too many pauses.** Biggest performance note. Fix: read the
   script line by line, decide the tonality that line needs (e.g. "terrified" for her
   opener, excited/energetic elsewhere) and write it explicitly into the tone-and-
   attitude part of the prompt.

5. **Pacing tricks.**
   - Add throwaway words at the END of a phrase; the AI speaks faster to fit them in,
     and the editor cuts them off.
   - Merge script line 1 + line 2 into one clip when the same image is used.
   - Generate 6s or 8s clips instead of 4s so delivery and pacing feel faster/denser.

6. **Gemini watermark.** The sparkle symbol bottom-right = generated in Gemini, not
   Google Flow (VEO). Confirmed visible in frames. The symbol must not be there.

## Nicola asked Reut to send him

- [ ] The exact prompt/request used to create v1
- [ ] A screenshot of the platform used to generate (or confirmation it was Gemini)

## Rebuild plan for v2

1. Pinterest: find 2 real reference photos — a woman asking a question at a live
   conference, and a speaker on stage (Lior's posture reference).
2. Create the 2 images per the guide (NANOBANANA prompt → HiggsField face/subject
   swap on the REAL background → LUPA Precision 6K no grain).
3. Regenerate all clips in Google Flow (VEO, LITE mode) — never Gemini.
4. Every clip prompt: fixed camera + explicit tone-and-attitude per line.
5. Use 6-8s clips, merge short exchanges, pad line-ends with cuttable filler words.
6. Editor cuts between her and him per the full script.
