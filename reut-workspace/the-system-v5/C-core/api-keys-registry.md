# API Keys Registry

Track which external services are connected to your system.

## Connected Services

| Service | Purpose | Connected | Status |
|---------|---------|-----------|--------|
| HeyGen | AI avatar videos (Lior clone experiments) | 2026-07-13 | Active |
| ElevenLabs | Lior voice clone, TTS, voice changer | 2026-07-13 | Active |
| [Name] | [What it does] | [Date] | Active / Inactive |

### HeyGen

**Connected:** 2026-07-13
**Purpose:** Avatar-based AI videos of Lior; testing ground alongside the Nicola/VEO pipeline
**Used by:** ai-clone-videos workstream (O-output/ai-clone-videos/)
**Key location:** `HEYGEN_API_KEY` in `~/.zshrc` (never in this file)

**Account assets (as of 2026-07-13):**
- Avatars: "lior pozin -- 4" `131f53725be34f9ebd1f74d29075f0d2`, "-- 6" `a71d15113af347a390a88416b137e497`, "-- 8" `7050de8d78a54204b800030e34ef6844`, "-- 9" `4c8589c0e7b642108c1515b786eba48c`
- Lior voice, ElevenLabs PVC import (newest 2026-06-27): `62b70600136945ddaa2c5c08461c0825`
- ElevenLabs integration already connected (3 imported Lior voices)
- Quota at connect time: 600 API credits

**Capabilities:** create avatar videos via API (`/v2/video/generate`), list avatars/voices, photo avatars
**Limitations:** API credits separate from plan credits; watermark depends on plan

### ElevenLabs

**Connected:** 2026-07-13
**Purpose:** Lior's cloned voice for AI videos; TTS; Voice Changer for Nicola's VEO pipeline Step 7
**Used by:** ai-clone-videos workstream; HeyGen (voices imported via integration)
**Key location:** `ELEVENLABS_API_KEY` in `~/.zshrc` (never in this file)

**Account assets (as of 2026-07-13):**
- "liors voice" Professional Voice Clone (PVC): `qAPjJ0gODMxl3kFXrSy6`
- Plan: Scale, 6.01M chars/mo (35K used), 1 of 2,200 voice slots
- Already integrated into HeyGen (3 imported Lior voice variants there)

**Capabilities:** TTS with the clone, Speech-to-Speech voice changer (`/v1/speech-to-speech`), dubbing
**Limitations:** Lior's voice is a biometric asset — clone stays on this company account only

---

## Service Details

### [Service Name]

**Connected:** [Date]
**Purpose:** [What you use it for]
**Used by:** [Which agents/workflows use it]

**Capabilities:**
- [What it can do]

**Limitations:**
- [What it can't do]

**Setup Notes:**
- [Any special configuration]

---

## CRITICAL: Security

**NEVER store actual API keys in this file.**

This file only tracks WHICH services are connected and their capabilities.

Keep your actual keys in:
- Claude Code settings
- Environment variables
- Your system's secure storage

---

### Example Entry

| Service | Purpose | Connected | Status |
|---------|---------|-----------|--------|
| Google Gemini | Image generation, visual content | 2024-01-15 | Active |

### Google Gemini

**Connected:** 2024-01-15
**Purpose:** Generate images and visual content for social posts, newsletters, and presentations
**Used by:** Copywriter Agent (when visual content is requested)

**Capabilities:**
- Generate images from text prompts
- Multiple styles (photorealistic, illustration, abstract)
- Multiple sizes and aspect ratios

**Limitations:**
- No text in images (usually)
- May need multiple attempts for specific styles
- Rate limits apply

**Setup Notes:**
- API key set in Claude Code MCP settings
- Use Gemini 2.0 Flash for best results
- Keep prompts specific for better outputs

---

## How to Add a New Service

1. Use `T-tools/02-prompts/BONUS/08-connect-api-keys.md`
2. Follow the setup instructions for your service
3. Update this table with the new service

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
