# Putting the pitch page on liorpozin.com

For whoever has the Base44 login. App id `6989baa373c3a2fb4ba41f9a`.
File to paste: `base44-embed.html`, in this same folder.

## What this is

A one-page guest pitch for The Diary of a CEO, written in Lior's voice, to be sent to
FlightStory's producers. It is not a marketing page and it is not part of the site's
navigation. It exists so we can send one clean link from his own domain.

## The five steps

1. **Create a new page** in Base44, blank, full width.
2. **Give it an unguessable path.** Not `/doac` and not `/podcast`. Something like
   `/p/8fk2qz`. The page carries a story Lior has never told publicly, so the URL should
   not be findable by typing a guess.
3. **Do not add it to the navigation**, the sitemap, or the footer links.
4. **Paste the whole of `base44-embed.html` into one custom HTML block.** It is a single
   self-contained block: fonts, styles, both photographs and the small script are all
   inside it. Nothing else needs uploading.
5. **Publish, then open it on a phone.** That is how the producers will read it.

## Things not to change

- **Both photographs are embedded in the file as data URIs.** Do not swap them for
  uploads, do not compress them, do not lift them into Base44's media library. The file
  is about 690 KB because of them and that is expected.
- **Every style in the file is scoped to `#lp-pitch`.** It cannot touch the rest of the
  site, and the site's own CSS should not touch it. If the site has a global rule on
  `img`, `p` or `h1` that leaks in, tell me and I will armour those.
- **The page is locked to the light palette** so it looks the same for every visitor
  regardless of their dark mode setting. The comment at the end of the style block says
  how to flip it to dark if we ever want that.
- **`<meta name="robots" content="noindex, nofollow">` is at the top of the file.** If
  Base44 strips meta tags from HTML blocks, set noindex on the page in Base44's own SEO
  settings instead. This one matters.
- **No tracking, no pixels, no analytics on this page.** It goes to one production team.

## After it is live

Send me the URL and I will check it on mobile and desktop before it goes to anyone.

## Two things still open, unrelated to Base44

- The age at the arrest needs Lior's confirmation. It is the first line of the page.
- The podcast link at the bottom goes to Real Life Superpowers. If he would rather lead
  with a different episode, it is a one line change.
