---
name: reference-lior-reut-weekly-gemini-notes
description: Lior/Reut Weekly meetings get auto Gemini notes in a Google Doc; how to read them and how thin they are
metadata:
  type: reference
---

The recurring **Lior / Reut Weekly** (Nov 2026: Thursday ~14:50 IST) produces a "Notes by Gemini" Google Doc. Example, 2026-11-12: https://docs.google.com/document/d/1-tuQxoI5bzQfezlgiegNfe9zoJysAsnY04ia0euCRCQ/edit

**How to read:** not public, and the built-in browser isn't signed in to Google. Use Claude in Chrome. In the doc tab, fetch `/export?format=txt&tab=<id>` and get tab ids by regex `t\.[a-z0-9]{10,14}` on the page HTML. There are two tabs: Quick notes and Notes. No transcript tab.

**Quality:** Gemini notes are short and vague, often "No suggested next steps". The summary Reut pastes in Hebrew is much richer. Treat the Gemini doc as a cross-check for date, attendees and stray topics. File into the existing `B-brain/meetings/` note for that date, never a duplicate. See [[project-plaud-meeting-recordings]], [[project-lior-ai-app-hub]].
