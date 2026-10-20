# Avatar test #1: the ICE framework reel, Lior in place of David Fogarty

Reference: https://www.instagram.com/reels/DdQ5A2bj5O5/
David Fogarty, Daily Mentor / The Oodie. 55 s, 9:16, 376 likes, 30 comments.
Goal: replicate the reel 1:1 with Lior's face and the same script, to test whether the
photo + script avatar pipeline can copy an existing reel as-is.
Build order: this works with ANY Photo #1, so run it once with your own selfie first
to check the pipeline, then swap in Lior's photo.

## 1. What the reference does, shot by shot

| Time | On screen | Type |
|---|---|---|
| 0:00-0:06 | David, handheld phone selfie, grey cap, white tee, standing indoors by a window, dark wood beam beside him, gestures with free hand | A-roll |
| 0:06-0:10 | Drew Houston on stage in a Dropbox hoodie, 2 clips | Stock B-roll |
| 0:10-0:14 | A-roll | |
| 0:14-0:16 | Purple card: "ICE" FRAMEWORK, then Impact / Confidence / Ease typing in, first letters red | Motion graphic |
| 0:16-0:42 | A-roll, unbroken, word captions carry it | A-roll |
| 0:42-0:52 | Daily Mentor website screen recording, slow scroll, captions on top | Screen B-roll |
| 0:52-0:55 | A-roll close, "comment COACH" | A-roll |

Caption style: 1-3 words at a time, white uppercase Poppins Bold with a soft black
shadow, centred at the lower third. No emphasis colours. Sentence-case captions only on
the framework card. No music bed audible, voice only. No zooms, the handheld shake is
the only motion.

Ratio: 40 s of A-roll, 15 s of B-roll. Three cutaways in 55 s, which is what keeps a
55 s talking head alive.

## 2. The script, verbatim, for the 1:1 test

--- SCRIPT STARTS ---
Undoubtedly, the best productivity hack to understand what you should be working on next was actually created by the founder of Dropbox.
He even coined the term growth hacking using this framework.
It's called the ICE framework, which stands for impact, confidence and ease.
The process is super simple.
You list every single thing that you could be working on to grow your business, and then you rank it based on the impact that it can have, e.g. how much money it can actually make you.
Then the confidence, how confident are you that it's going to make that much revenue.
And then the ease, such as the ease of implementation.
Then you can either average these out or weight the higher impact ones to actually get what you should be working on.
The problem with this structure is you don't know how easy things are and how confident you should be without a mentor.
This is actually why we created Daily Mentor, so we can tell you what you should be really confident in and what results you can actually expect from doing certain things in e-commerce.
Comment "COACH" and we'll give you the playbook.
--- SCRIPT ENDS ---

~190 words, 55 s at David's pace. Paste as-is into the Script field for the test.

### Two flags before this ever goes near Lior's account

1. The fact is wrong. ICE was created by Sean Ellis, Dropbox's first marketer, who
   also coined "growth hacking". Drew Houston founded Dropbox and has nothing to do
   with ICE. Fine for a private pipeline test, not fine on Lior's feed.
2. Lines 9-11 are David's product pitch. Lior's brand rule is founder journey, never
   product marketing, so the publishable version swaps the last 3 lines.

### Publishable close for Lior, if the test passes

Replace lines 9-11 with:

--- SCRIPT STARTS ---
The problem with ICE is the C. Nobody knows how confident to be on day one.
At AutoDS we fixed that with one rule: confidence comes from customers, not from opinions. If 5 paying users asked for it, confidence is a 10. If nobody did, it is a 2, no matter how much I love the idea.
Comment ICE and I'll send you the sheet we ranked 200 features on.
--- SCRIPT ENDS ---

And fix line 1 to "was actually created by the first marketer at Dropbox".

## 3. The anchor image, Lior version of David's frame

Same framing as David so the replication is honest: arm's-length phone selfie, slight
high angle, bright indoor daylight, window and a dark wood beam. Lior's own look, no
cap, so the face reads instantly.

NanoBanana PRO request, upload a candid Lior photo as Photo #1:

```
Write me a prompt for NanoBanana PRO following the rules described in the sources of this project. Strictly follow that structure, do not change it.
I want the exact same subject to be represented in the photo, with the same skin texture, face shape, hairline, stubble and everything exactly as in Photo #1 that I provided.

THE SUBJECT:
- Pose: standing, holding a phone at arm's length with his right hand just out of frame, head and shoulders filling the frame, face slightly tilted up toward the lens
- Attitude: casual, quick, mid-thought, like recording a voice note to a friend
- Doing: talking directly to the phone camera, left hand slightly raised at shoulder height mid-gesture, fingers loose
- Looking: straight into the phone lens
- Wearing: plain white cotton crew-neck t-shirt, slightly loose, no print, no logo
- Additional: natural skin texture with pores, light stubble, short dark textured hair, no retouching, slight natural skin shine from daylight

CAMERA AND SETUP:
- Frame: vertical 9:16, tight selfie from mid-chest up, high angle from about 20 degrees above eye level, 24mm wide phone lens with mild edge distortion, deep focus
- Lighting: soft overcast daylight from a large window camera-left, flat even exposure, phone-camera look, no studio lighting
- Setup: bright modern apartment interior. A wide dark-stained wooden beam or pillar vertical on the right third of the frame, a white wall and part of a white-framed window behind his left shoulder, pale ceiling visible top left. Domestic, unstaged, slightly messy real-life feel. No on-screen text anywhere.
```

Why match David's frame instead of the dark desk look: the test is whether the tool can
copy an existing reel, so the environment must match the reference. The dark desk
anchor from the Avatar Factory teardown is the one to use for original content.

## 4. B-roll swaps

| Reference | Lior version | How |
|---|---|---|
| Drew Houston stage clips | Same beat, but use a still photo of Sean Ellis or Drew with a slow Ken Burns push, 2 x 2 s | Public press photo, credit in caption if used publicly |
| Purple ICE card | Rebuild in CapCut or Canva: deep purple gradient, white "ICE" FRAMEWORK with a brush underline, then Impact / Confidence / Ease typing in, first letters red | 2.5 s |
| Daily Mentor site scroll | For the 1:1 test keep a screen recording of any landing page. For the publishable version: the ICE sheet itself in Google Sheets, slow scroll, 200 rows of features ranked | 8-10 s |

Image-to-video prompt for the still B-roll:
```
Slow steady push-in on the photograph, 2 seconds, no morphing, faces unchanged, subtle parallax only, photoreal.
```

## 5. Avatar step, in order

1. Photo #1 → NanoBanana PRO with the prompt above → pick the take where the hand is
   clearly separate from the face. Avatar engines smear hands that touch the jaw.
2. LUPA upscale, Precision, 6K, no grain.
3. Voice: ElevenLabs, Lior's cloned voice, the verbatim script, one take, speed 1.05,
   stability around 40 so it sounds like a phone voice note and not a narrator.
4. Avatar Factory, or HeyGen Avatar IV / HiggsField Speak as fallback: upload the
   still + the audio. Generate the full 55 s once. If the hand freezes after 15 s,
   split the script into 3 chunks at the B-roll points, 0:06, 0:16 and 0:42, and
   generate 3 clips. The cutaways hide the joins anyway.
5. Handheld feel: avatar output is tripod-still. In CapCut add "Handheld" camera
   shake at 15-20% strength on every A-roll segment. Without this the selfie framing
   reads as fake immediately.
6. Captions: CapCut auto-captions, Poppins Bold, white, uppercase, black shadow 50%,
   1-3 words per card, lower third. Delete all emphasis colours the template adds.
7. Export 1080x1920, 30 fps, no music.

## 6. What to judge the test on

- Does the mouth hold sync through a 190-word run? Watch 0:20-0:40, the long unbroken
  block, that is where engines drift.
- Do the gestures look like his? Lior talks with both hands, open palms. If the avatar
  only nods, the dark-desk anchor with the lav mic in hand is the safer format.
- Does the handheld shake sell it? Show the export to one person who does not know it
  is AI and ask what he filmed it on.

## 7. Full Lior script, publishable version (2026-09-19)

Same skeleton as David's reel: named-brand hook → framework → 3 steps → the flaw →
the operator fix → CTA. Fact fixed (Sean Ellis, not the founder). Product pitch
replaced with a Lior rule. ~185 words, 55 s at his pace. B-roll cues in [brackets] are
edit notes, not spoken.

--- SCRIPT STARTS ---
The best focus tool I know is a 3-column spreadsheet.
Dropbox's first marketer built it. Not the founder, by the way. Sean Ellis, the guy who coined the term growth hacking.
[B-ROLL: Sean Ellis photo, slow push, 2 s]
It's called ICE. Impact, confidence, ease.
[B-ROLL: ICE card, 2.5 s]
You write down every single thing you could work on to grow the business. Every feature, every campaign, every idea from the last meeting.
Then you ask 3 questions about each one.
How much money can this make? That's impact.
How sure am I about that number? That's confidence.
How fast can we ship it? That's ease.
Score each from 1 to 10, average them, sort the list. Top 3 get done. Everything below the line gets ignored.
Now the part everyone skips. The middle column is a guess. Nobody knows how confident to be on day one.
At AutoDS we fixed that with one rule. Confidence is a number customers give you. If 5 paying sellers asked for it this month, confidence is a 10. If nobody asked, it's a 2. Even when I love the idea.
[B-ROLL: the sheet in Google Sheets, slow scroll, 8 s]
In the end, focus is a spreadsheet. Everything else is talking.
Comment ICE and I'll send you the exact sheet.
--- SCRIPT ENDS ---

### Why these changes

- Hook: David opens with "Undoubtedly, the best productivity hack". Ours opens with a
  concrete object and a number, "3-column spreadsheet", 9 words. The Dropbox name moves
  to line 2 with the correction "Not the founder, by the way", which is both his
  "by the way" aside and a built-in comment bait: people who know the myth will argue.
- The 3 questions are written as a self-interrogation chain, his E97 signature, instead
  of David's list. Same information, sounds like him talking.
- "Everything below the line gets ignored" is his flat-dismissal punchline.
- The flaw beat is the share trigger. David's flaw was "you need a mentor", a sales
  bridge. Ours is "the middle column is a guess", a real problem every founder has
  felt, and the fix is a rule anyone can copy tomorrow. That is what gets saved.
- "In the end" sits on the quotable line, once, per the Hebrew voice notes.
- CTA is an ungated first-party artifact, the exact sheet, same mechanism as the
  exit-deck post. Build the sheet before this goes live.

### Before recording

1. Confirm with Lior that the "5 paying sellers this month" rule is real or that he is
   happy to own it as his rule going forward. Do not ship a rule he would not defend on
   a podcast.
2. The sheet must exist: a Google Sheet with Impact / Confidence / Ease columns, the
   customer-count rule written into the Confidence column header, and 10-15 sample
   rows. That is the deliverable people comment for.
3. Optional 5 s proof insert after "Even when I love the idea": one real AutoDS
   example, the feature that scored a 2 and got killed, with a number. Only if Lior
   gives a true one. Without it the script still works.
