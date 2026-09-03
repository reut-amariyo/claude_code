---
name: feedback-no-powerpoint-deliverables
description: NEVER deliver .pptx to Reut — she has no working PowerPoint. Decks go out as PDF (review) + Google Slides or Keynote (editable). Same family as the no-.docx rule.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 794d5a09-df7d-4250-a315-ae71de9e82be
  modified: 2026-08-03T15:00:07.629Z
---

Reut (2026-08-03, during the exit-deck template work): "אף פעם אל תכין בפאוור פוינט תזכור את זה" — never prepare deliverables in PowerPoint.

**Why:** PowerPoint.app exists on her Mac but she cannot use it (no license). A .pptx deliverable is a dead end for her, exactly like .docx ([[feedback-no-word-export]]).

**How to apply:**
- Deck deliverables: PDF for review + an editable version she can open — Google Slides (she asked for this first) or native Keynote (.key). Keynote IS installed and opens/converts pptx fine.
- pptx may still be used internally as an intermediate format (pptxgenjs generation, Keynote import, Google Slides import) — just never as the thing handed to her.
- Keynote AppleScript: `export` (PDF / slide images) works on pptx-opened docs, but `save ... in` a .key errors with -1708; convert by opening the pptx in Keynote and using File > Save manually, or upload to Google Slides.
