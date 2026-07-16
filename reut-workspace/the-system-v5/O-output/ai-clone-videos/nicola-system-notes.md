# Nicola AI Clone Video System — Learning Notes

Captured 2026-07-13 from Nicola's public Notion guide (1:1 LIVE STAGE).
Project: learn to produce hyper-realistic AI clone videos of Lior without filming him,
for trendy reels and scene-based formats. Reut learns from Nicola; Claude co-learns.

## Source links

| Resource | Link | Access |
|---|---|---|
| Nicola 1:1 LIVE STAGE guide | https://nicola-ai.notion.site/1-1-LIVE-STAGE-33d87bd9c35481edbb21d077d95cdde1 | ✅ public, captured below |
| All Requests & Prompts | https://nicola-ai.notion.site/All-Requests-Prompts-Copy-Paste-33d87bd9c3548158a435d0719232779d | ✅ public, captured below |
| Miro board | https://miro.com/app/board/uXjVG4RJp5M=/ | 🔒 needs login |
| Nicola materials (Drive) | https://drive.google.com/drive/folders/1r_c16djPf--XAzTLZdtItcfal0hnXx7w | 🔒 needs login |
| Guides + materials (Drive) | https://drive.google.com/drive/folders/11fenvpP1NCC8qBwb_yshaGp9foSq8DUv | 🔒 needs login |
| Our G-Drive folder | https://drive.google.com/drive/folders/13jkpwzlQaXUu-qZCStrwi_R05WvuXTft | 🔒 needs login |
| Lior-Reut Notion workspace | https://app.notion.com/p/Lior-Reut-38e87bd9c3548001a442e4b1e744b393 | 🔒 needs login |
| Content review board | https://app.notion.com/p/8e887bd9c3548222b90f012e0b781fd4 | 🔒 needs login |
| DFY Guides Library | https://app.notion.com/p/Nicola-AI-Video-Guides-Library-34087bd9c35481b786eac29f46a1cb69 | 🔒 needs login |
| Book 1:1 with Nicola | https://calendly.com/nicola-aiavatar/book-your-1-1-private-consultation-clone | — |

## Toolchain

ChatGPT (prompt engineering, two dedicated folders: NANOBANANA for images, VEO for video)
→ HiggsField (image generation) → LUPA (upscale) → VEO (video generation)
→ ElevenLabs (voice change) → CapCut (collect clips) → human editor (assemble).

## The 8-step workflow (1:1 LIVE STAGE format)

Format: two people in a live talk / on-stage Q&A setting. "You" = the expert (Lior),
"Subject" = the other person asking/answering (e.g. the woman asking questions).

### Step 1 — Idea
Define BEFORE touching tools: who is the subject, their business/niche, hook + message.
Find a reference video on IG/TikTok matching the desired setting. Screenshot the subject.

### Step 2 — Subject image
1. ChatGPT → NANOBANANA folder → new chat → upload subject screenshot → ask for a
   HiggsField prompt (keep distinctive features, modernize outfit, remove on-screen text,
   background/lighting unchanged, face slightly changed so it's not the same person).
2. HiggsField: upload screenshot as reference + paste ChatGPT prompt → generate.
3. LUPA upscale: Precision mode, 6K, grain OFF.

### Step 3 — Your image (Lior)
Same process with Lior's photo as subject and a stage reference (e.g. Hormozi photo)
for posture/setting. Same LUPA settings.

### Step 4 — Script
- Write the full conversation as natural dialogue.
- Google Doc, Arial 11 — visual line-length check. Max 2 lines per VEO clip.
- Split into YOUR lines and SUBJECT lines. Each `|` separator = one VEO clip.
- Lines are NOT chronological — intentional, to minimize generations. Editor reorders
  using the full script.
- Typical size: 5 clips per person.

### Step 5 — VEO project setup
New project named `[YOUR NAME] [SUBJECT DESCRIPTION]`. Upload both upscaled images.

### Step 6 — Generate clips
- Subject clips first, then yours.
- ChatGPT → VEO folder → new chat → upload the AI image → request a VEO JSON prompt
  (see prompt library). Key constraints baked in: subject never looks at camera,
  natural gestures matching speech, relaxed attitude, one named opening gesture,
  static camera, no text.
- VEO settings: LITE mode. 8 generations for the very first clip, 4 for all others.
- Pick best clip by movements, gestures, tone → save → into CapCut immediately.
- Clips 2+: STAY in the same ChatGPT chat, send the short update template
  (new gesture + new line only).
- Voiceover bug fix: if part of the line comes out as voiceover, first send
  "no voiceover — the subject must visibly speak every single word including [words]".
  Fallback: separate clip for just those words, padded with filler words.

### Step 7 — Voice change (ElevenLabs)
Voice Changer on all clips, per person. Options: preset voice / create new / clone real
voice. Output: 2 audio-swapped files, one per person.

### Step 8 — Send to editor
Deliver 3 things: full script (chronological reference), file 1 = all subject clips,
file 2 = all your clips. Editor reorders, cuts, assembles.

## Prompt library (copy-paste, replace [BRACKETS])

### 1. NANOBANANA image-prompt request
```
I want a prompt that recreates this image with a slightly different style for the person.
Keep the [DISTINCTIVE FEATURES] look,
but update the jacket to a more modern [YEAR] vibe and add a bit of color to the outfit.
Remove any text on screen and any symbols in the corners.
Do not change the background or lighting at all — everything in the environment stays exactly the same.
Only adjust the outfit and slightly change the face so it is not the exact same person but still looks similar.
```

### 2. HiggsField prompt (example output for Hat Business subject)
Hyper-realistic RAW cinematic photo, same posture/angle/framing as reference,
modernized outfit with tasteful color accents, natural skin texture with pores and
micro-imperfections, soft directional stage lighting, dark curtain background, shallow
DOF with blurred audience, full-frame 85mm, no text/UI, sharp focus face + upper body,
cinematic grading. (Paste whatever ChatGPT generates for YOUR subject.)

### 3. VEO clip 1 request (ChatGPT → VEO folder, upload AI image)
```
give me a prompt for Veo following the instructions in sources.
the subject in the photo speaks in a natural and realistic way.
the subject never looks at the camera and keeps looking straight ahead like in the photo for the entire video.
the subject makes natural, realistic gestures that match what he is saying.
subject attitude is relaxed.
the first gesture the subject makes is [DESCRIBE OPENING GESTURE].
line he says: "[PASTE SUBJECT'S FIRST LINE HERE]"
```

### 4. VEO clips 2+ request (same chat!)
```
now same subject and attitude, instead of [PREVIOUS GESTURE] he [NEW GESTURE]
while speaking in a natural and calm way.
new line: "[PASTE NEXT LINE HERE]"
```
If no specific gesture: just update the line.

### 5. VEO JSON prompt shape (what ChatGPT returns; paste into VEO)
Fields: description / style ("photorealistic cinematic") / camera ("static medium shot,
eye-level, no zoom, no movement") / lighting / room / elements[] / motion (begins
speaking immediately, named first gesture, minimal realistic gestures, mouth movement
minimal and realistic) / audio ("The subject says: '...'") / ending (keeps looking
forward, no scene changes) / text: "none" / keywords[] incl. "9:16", "no camera eye
contact", "static camera", "high detail", "skin texture", "natural performance".

### 6. Voiceover fix
```
no voiceover — the subject must visibly speak every single word
including "[PROBLEMATIC WORDS]"
```

## Reference example (Hat Business, Nicola's demo)

Concept: cowboy-hat business owner at $2M/yr wants $5M, no time to record content,
solution = AI cloning. 5 subject clips + 5 "you" clips; expert's last clip carries the
CTA ("comment INFO below"). Full line-by-line table lives on the prompts page.

## Our first task (active)

1:1 session video: Lior on stage answering a woman's questions.
- Reut made version 1 — not good.
- Nicola recorded a Loom explaining what's wrong → Claude summarizes the Loom and
  drives the fix list. (Loom link pending from Reut.)

## Companion files (this folder)

- miro-workflow-notes.md — the CURRENT core pipeline from the Miro board: NanoBanana
  PRO images, LUPA 6K Precision, Veo 3.1 with the 7-part plain-text prompt structure.
  Where it conflicts with the Notion guide above, the Miro version wins.
- prompts-real-pic-and-outfit.md — 9 tested NanoBanana image prompts (podcast /
  executive / late-night setups) + the outfit-swap prompt, from Nicola's docx pack.
- v1-loom-feedback-2026-07-13.md — Nicola's critique of v1 + rebuild plan.

## Open items

- [x] Loom critique summarized 2026-07-13 → see v1-loom-feedback-2026-07-13.md
- [x] Miro board captured 2026-07-13 (via screenshot) → miro-workflow-notes.md
- [x] Copy-paste prompt docx pack converted → prompts-real-pic-and-outfit.md
- [ ] Send Nicola the exact v1 prompt + platform screenshot (he suspects Gemini, correctly)
- [ ] Rebuild v2 per the fix list (real Pinterest reference, Google Flow, fixed camera, tonality)
- [ ] Course library (clientclub.net) is login-gated — view via Reut's Chrome or exports
- [ ] Still missing: the "sources" instruction docs inside Nicola's ChatGPT
      NANOBANANA + VEO projects (the prompts reference them)
- [ ] Access Miro board / Drive folders / private Notion (via Reut's Chrome or exports)
- [ ] Learn the "instructions in sources" ChatGPT project files Nicola references
      (the VEO folder has source docs we haven't seen — likely in the Drive materials)
- [ ] Adapt the CTA line for Lior's brand (Nicola's demo CTA is his own DFY funnel)
