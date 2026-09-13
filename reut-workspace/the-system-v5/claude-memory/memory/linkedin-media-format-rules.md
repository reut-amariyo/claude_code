---
name: linkedin-media-format-rules
description: How LinkedIn actually renders video, GIF and images, learned the hard way on 2026-09-07 — GIF in the image slot is the format that survives both desktop and mobile
metadata:
  type: reference
---

Learned by shipping a chart animation on 2026-09-07 and watching it break twice.

- **9:16 video** gets pillarboxed on desktop. Heavy black bars, content shrinks.
- **4:5 video** fixes desktop, then LinkedIn's MOBILE player scales video to fill the phone screen
  and crops the sides. Labels at the frame edges get cut off.
- **LinkedIn overlays roughly the bottom 10% of any video** with the caption and the controls, and
  the top with the author header. Nothing important can live in either band.
- **An animated GIF uploaded in the IMAGE slot is never cropped, never zoomed, and carries no player
  chrome.** It autoplays and loops inline. This is how Charlie Hills posts his animated infographics.
  Keep it under about 1MB or LinkedIn may flatten it to a static frame. Dragging a GIF into the
  video slot converts it to video and reintroduces the cropping.
- **Static images are never cropped** on either platform. Safest of all.
- **Documents (PDF)** render as a swipeable carousel, never cropped. The format behind the best
  follower post on the account, see [[lior-post-exit-deck-lead-magnet]].

**Rule of thumb:** one visual with no motion → image. More than one beat → document. Motion that
is genuinely the point → GIF in the image slot. Native video only when nothing else will do.

Rendering pipeline that works locally with no installs: build the animation as a self-contained
HTML page that exposes a seek function, drive Chrome headless over the DevTools protocol with
`--remote-debugging-port`, capture each frame with Page.captureScreenshot, then assemble with
ffmpeg. One Chrome instance for all frames. Launching Chrome per frame is roughly 30x slower.

Related: [[linkedin-posting-rules]], [[lior-post-claude-to-codex-migration]].
