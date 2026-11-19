---
name: project-lior-store-builder-ai
description: "Lior Store Builder AI" hackathon product mockup, Tony AI-style chat+call bot that sells BYS and builds the store in-chat
metadata:
  type: project
---

Built 2026-10-29 for a hackathon pitch to the CEO. Product name set by Reut: **Lior Store Builder AI**.
Artifact: https://claude.ai/artifact/W7MTyRpVUEz7vWdqSoxJWj (v3 = product version). Source: the-system-v5/O-output/lior-ai-mockup/ (app-src.html + build step that inlines lior-hero.jpg / lior-avatar.jpg).

Reut rejected a "demo page" framing: she wants it to look and work like the final product a beginner would use, no demo controls. Live answers via the artifact `sample` capability, prepared-answer fallback. Voice = browser TTS stand-in; real ElevenLabs Lior voice not wired (artifact CSP blocks the API).
Next idea: same engine for BYS creators, AC Hampton "AC AI" first; creators rent it, the platform owns it.

Related: [[project-vsl-agent-build-your-store]]

Update 2026-10-29: flow now mirrors BYS (5 real niches as cards; live CTA goes straight to Shopify signup, niche is picked after). After the store builds, Lior asks "What's stopping you?" and removes the blocker (fear / time / money / skills). Fear triggers the upsell "Launch Insurance": $19 one time; no sale within 3 months = Lior gives $50 (terms set by Reut 2026-10-29). Placeholder terms Reut proposed, not a real AutoDS offer; needs CEO + legal sign-off.
Voice DONE 2026-10-29 (v6): 22 call lines recorded with ElevenLabs PVC qAPjJ0gODMxl3kFXrSy6, published as voice/*.mp3. To add lines: edit voice-lines.json, Reut runs record_lior_voice.sh (key now saved in macOS Keychain service "lior-store-builder-elevenlabs", records only missing lines; the ~/.zshrc ELEVENLABS_API_KEY is only a key ID), then build.py + republish with files. In a call the bot uses the recorded answer bank; live Claude answers stay text only.

Mic: claude.ai blocks the microphone in artifacts. For a spoken call, Reut runs start_local.sh (Chrome on localhost:8765, mic works, prepared answers only, all in recorded voice). Mic tap = hands-free, Lior re-listens after each line; saying "yes/add it" accepts the insurance offer.

Update 2026-11-10: WON FIRST PLACE at the hackathon (per Reut). She is sharing the artifact link with the product team.

Update 2026-11-10: WON FIRST PLACE at the hackathon (per Reut). She is sharing the artifact link with the product team.
