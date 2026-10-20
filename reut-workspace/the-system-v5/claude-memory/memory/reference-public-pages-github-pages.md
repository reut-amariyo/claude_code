---
name: reference-public-pages-github-pages
description: How Lior/Reut public web pages get hosted - GitHub Pages under reut-amariyo, one repo per page, Reut clicks create + Pages toggle, Claude pushes; first page is "The 50 Who Taught Me"
metadata:
  type: reference
---

Set up 2026-09-21 for the "50 who taught me" list page (Lior's recommend-profiles post).

**Live:** https://reut-amariyo.github.io/lior-50/  · source `~/Projects/lior-50` (git, remote
`git@github.com:reut-amariyo/lior-50.git`, branch main, `.nojekyll`, full HTML skeleton with OG tags).
A claude.ai artifact of the same page exists (https://claude.ai/artifact/XQCNLH1BaUKaCaxgWZ2Fkq)
but Reut wanted a real website link, so GitHub Pages is the canonical one.

**Why GitHub Pages:** no `gh` CLI on the Mac, and the auto-mode classifier blocks Claude from
reading gh tokens or driving github.com in Chrome (treated as credential handling). SSH push
as reut-amariyo works. So the split is: Reut does 2 clicks, Claude does the rest.

**Recipe for the next page:**
1. Claude builds `~/Projects/<name>/index.html`, `git init`, commit, `git remote add origin
   git@github.com:reut-amariyo/<name>.git`.
2. Reut: github.com/new → name → Public → Create (no README). Say "נוצר".
3. Claude: `git push -u origin main`.
4. Reut: repo Settings → Pages → Branch: main, / (root) → Save. Pages did NOT auto-enable.
5. Live at https://reut-amariyo.github.io/<name>/ within ~2 min. Poll with curl.
Give Reut the steps in Hebrew, numbered 1-2-3, she asked for that format.

**Second page, 2026-10-01:** https://lior-pozin.github.io/founder-brain/ · source `~/Projects/founder-brain`, remote `git@github.com:lior-pozin/founder-brain.git`. "The Founder Brain" lead magnet: 13 card-framed slides, voice-interview prompt, blank template `founder-brain.md`.
**Reut does NOT want "reut-amariyo" in Lior-facing URLs.** Lior pages now live under the free GitHub org **lior-pozin** (created 2026-10-01; `liorpozin` is someone else's org). New repo URL: github.com/organizations/lior-pozin/repositories/new. Org creation free-plan link: github.com/account/organizations/new?plan=free (the default page pushes paid plans).
**Custom domain (offered, not done):** GoDaddy CNAME `list` → `reut-amariyo.github.io`, then
add `CNAME` file + enforce HTTPS in repo Pages settings. Lior's site is Base44 (liorpozin.com),
see [[lior-website-base44]]; embedding there is the alternative.

**Photos on these pages:** LinkedIn avatar URLs expire and are CSP-blocked, so download with a
browser UA, PIL-fit to 112px, embed as base64 (50 photos ≈ 190 KB). Profiles that hide their
photo from logged-out view return a 489-byte placeholder; fallback = X avatar via unavatar.io.
