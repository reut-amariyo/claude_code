# פרומפט לBase44 — אפליקציה נפרדת, לא על האתר של ליאור

הדף הזה נבנה כאפליקציה עצמאית בBase44, לא כעמוד בתוך liorpozin.com.
אחרי הבנייה מעלים את שתי התמונות ומחליפים שתי כתובות.

תמונות להעלות: `lior-nasdaq-times-square.jpg` ו-`lior-stage.webp`

---

## הפרומפט, להעתיק כמו שהוא

```
Build a single static page. Nothing else.

Hard rules, do not deviate:
- ONE page only. No navigation bar, no footer, no menu, no sidebar, no cookie banner.
- No forms, no email capture, no contact block, no buttons other than the two links already in the HTML.
- No analytics, no tracking pixels, no chat widget, no consent script.
- The page must NOT be linked from anywhere and must not appear in a sitemap.
- Set the page to noindex, nofollow in the SEO settings.
- Give the page an unguessable URL path, for example /p/8fk2qz. Do not use /doac, /podcast, /pitch or anything guessable.
- Page title: Lior Pozin

Use the HTML below EXACTLY as it is. Do not redesign it, do not restyle it, do not substitute fonts, do not change the colours, do not reorder the sections, do not "improve" the copy. Render it as given.

Two images: I will upload them separately. After you build the page, replace the placeholder URL_OF_PHOTO_1 with the URL of the Times Square photo, and URL_OF_PHOTO_2 with the URL of the photo on stage.

Here is the HTML:

<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;700&display=swap">
<style>#lp-pitch {
    --paper:#F4F3EF; --surface:#FFFFFF; --ink:#17171B; --mid:#6C6C75;
    --line:#DCDAD3; --hair:#E6E4DD; --sand:#9C7E52;
    --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
    --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  }
  @media (prefers-color-scheme: dark){#lp-pitch:not([data-theme="light"]) {
      --paper:#111114; --surface:#1A1A1E; --ink:#EDECE7; --mid:#93939C;
      --line:#2D2D34; --hair:#26262C; --sand:#CDAE83;
    }
  }#lp-pitch[data-theme="dark"] {
    --paper:#111114; --surface:#1A1A1E; --ink:#EDECE7; --mid:#93939C;
    --line:#2D2D34; --hair:#26262C; --sand:#CDAE83;
  }#lp-pitch {
    background:var(--paper); color:var(--ink);
    font-family:var(--sans); font-size:16px; line-height:1.62;
    padding-inline:22px; padding-block:0; -webkit-font-smoothing:antialiased;
  }#lp-pitch .wrap {max-width:680px; margin:0 auto;}#lp-pitch p {margin:0;}#lp-pitch a {color:inherit;}#lp-pitch /* masthead */
  header {padding-block:56px 0;}#lp-pitch h1 {font-family:var(--mono); font-weight:700; margin:0;}#lp-pitch h1 .a {
    display:inline; font-size:clamp(27px,6.8vw,46px); line-height:1.46;
    letter-spacing:-.035em; background:var(--ink); color:var(--paper);
    padding:.1em .28em; box-decoration-break:clone; -webkit-box-decoration-break:clone;
  }#lp-pitch h1 .b {
    display:block; margin-top:22px; font-size:clamp(18px,4.2vw,28px);
    line-height:1.5; letter-spacing:-.03em; color:var(--ink);
    max-width:30ch; text-wrap:balance;
  }#lp-pitch h1 .money {
    background:var(--sand); color:var(--paper);
    padding:.08em .26em; box-decoration-break:clone; -webkit-box-decoration-break:clone;
    white-space:nowrap;
  }#lp-pitch figure {margin:34px 0 0;}#lp-pitch figure img {
    display:block; width:100%; height:auto; max-width:100%;
    border:1px solid var(--line);
  }#lp-pitch .standfirst {
    font-size:18.5px; line-height:1.6; color:var(--ink); max-width:46ch;
    margin:34px 0 0;
  }#lp-pitch /* timeline */
  .tl {
    position:relative;
    margin:56px 0 0; padding-left:26px; border-left:1px solid var(--line);
    display:flex; flex-direction:column; gap:36px;
  }#lp-pitch .tl-fill {
    position:absolute; left:-1px; top:0; width:1px; height:0;
    background:var(--sand); transition:height .12s linear;
  }#lp-pitch .entry {position:relative; scroll-margin-top:74px;}#lp-pitch .entry::before {
    content:""; position:absolute; left:-30px; top:9px;
    width:7px; height:7px; border-radius:50%;
    background:var(--paper); border:1px solid var(--sand);
    transition:background .25s, transform .25s;
  }#lp-pitch .entry.on::before {background:var(--sand); transform:scale(1.25);}
  @media (prefers-reduced-motion:reduce){#lp-pitch .tl-fill, #lp-pitch .entry::before {transition:none;}
  }#lp-pitch .age {
    font-family:var(--mono); font-size:11px; font-weight:700; letter-spacing:.16em;
    text-transform:uppercase; color:var(--sand); display:block; margin-bottom:9px;
  }#lp-pitch .said {
    font-family:var(--mono); font-weight:700; font-size:clamp(17px,3.6vw,21px);
    line-height:1.34; letter-spacing:-.02em; margin:0 0 10px; text-wrap:balance;
  }#lp-pitch .body {font-size:16.5px; line-height:1.62; color:var(--mid);}#lp-pitch .body b {color:var(--ink); font-weight:500;}#lp-pitch /* sections */
  section {margin-top:64px; padding-top:44px; border-top:1px solid var(--line);}#lp-pitch h2 {
    font-family:var(--mono); font-weight:700; font-size:12px; letter-spacing:.18em;
    text-transform:uppercase; color:var(--mid); margin:0 0 30px;
  }#lp-pitch .beliefs {display:flex; flex-direction:column; gap:38px;}#lp-pitch .belief {display:flex; gap:20px; align-items:flex-start;}#lp-pitch .bn {
    font-family:var(--mono); font-size:12px; font-weight:700; color:var(--sand);
    flex:none; padding-top:5px; font-variant-numeric:tabular-nums;
  }#lp-pitch .bmain {flex:1; min-width:0;}#lp-pitch .btitle {
    font-family:var(--mono); font-weight:700; font-size:clamp(17px,3.6vw,21px);
    line-height:1.34; letter-spacing:-.02em; margin:0 0 12px; text-wrap:balance;
  }#lp-pitch .bbody {font-size:16.5px; line-height:1.62; color:var(--mid);}#lp-pitch .bbody p + p {margin-top:.85em;}#lp-pitch .bbody .kicker {color:var(--ink); font-weight:500;}#lp-pitch .pull {
    font-family:var(--mono); font-weight:700; font-size:clamp(17px,3.8vw,22px);
    line-height:1.42; letter-spacing:-.02em; color:var(--ink);
    margin:0 0 1.1em; padding-left:16px; border-left:2px solid var(--sand);
    max-width:32ch; text-wrap:balance;
  }#lp-pitch .pull span {display:block;}#lp-pitch .nos {display:flex; flex-direction:column; gap:.6em; margin:1em 0;}#lp-pitch .nos span {display:block; padding-left:14px; border-left:2px solid var(--hair);}#lp-pitch .going p + p {margin-top:1em;}#lp-pitch .going {font-size:17.5px; line-height:1.6; max-width:48ch;}#lp-pitch .going .big {font-family:var(--mono); font-weight:700; font-size:clamp(18px,4vw,23px); letter-spacing:-.02em; line-height:1.34;}#lp-pitch .tape {
    display:inline-flex; gap:12px; align-items:center; text-decoration:none;
    border:1px solid var(--line); background:var(--surface); padding:14px 18px;
  }#lp-pitch .tape:hover {border-color:var(--ink);}#lp-pitch .tape .dot {width:8px; height:8px; border-radius:50%; background:var(--sand); flex:none;}#lp-pitch .tape .t {font-weight:600; font-size:15.5px;}#lp-pitch .site {color:var(--sand); text-decoration:none; border-bottom:1px solid var(--line);}#lp-pitch .site:hover {border-bottom-color:var(--sand);}#lp-pitch figure.stage {margin:52px 0 0;}#lp-pitch figure.stage img {display:block; width:100%; height:auto; border:1px solid var(--line);}#lp-pitch footer {margin-top:44px; padding-block:30px 64px; border-top:1px solid var(--line);}#lp-pitch .sign {font-family:var(--mono); font-size:12px; line-height:1.9; color:var(--mid);}#lp-pitch .sign b {color:var(--ink); font-weight:700;}#lp-pitch .beta {font-family:var(--mono); font-size:12px; color:var(--sand); letter-spacing:.08em; margin-top:18px;}

  @media (max-width:480px){#lp-pitch .tl {padding-left:20px;}#lp-pitch .entry::before {left:-24px;}#lp-pitch .belief {gap:14px;}
  }

  #lp-pitch{max-width:100%; margin:0 auto;}
  #lp-pitch img{max-width:100%; height:auto;}

  /* locked to the light palette so it renders identically for every visitor.
     to flip the whole page to dark, swap these six values for the dark set in the block above. */
  #lp-pitch{
    color-scheme:light;
    --paper:#F4F3EF !important; --surface:#FFFFFF !important; --ink:#17171B !important;
    --mid:#6C6C75 !important; --line:#DCDAD3 !important; --hair:#E6E4DD !important;
    --sand:#9C7E52 !important;
  }
</style>
<div id="lp-pitch">
<div class="wrap">

  <header>
    <h1>
      <span class="a">At 13 I was arrested.</span>
      <span class="b">At 28 I sold my bootstrapped company to Fiverr for <span class="money">$92 million</span>.</span>
    </h1>

    <figure>
      <img src="URL_OF_PHOTO_1"
           alt="Lior Pozin standing in Times Square in a white BETA t-shirt, in front of the Nasdaq tower, which is showing a black and white photograph of him as a small boy above the words about building a $92M company exit and his name as CEO and co-founder of AutoDS.">
    </figure>

    <p class="standfirst">I did not grow up with money. My parents were immigrants from Ukraine.
      I am 31, and my target is to be a billionaire by 45.</p>
  </header>

  <div class="tl">
    <div class="tl-fill" id="tlfill"></div>

    <article class="entry" id="age-10">
      <span class="age">Age 10</span>
      <p class="said">My father locked my computer. I broke the password.</p>
      <p class="body">That was my first hack, and the first time I understood that a no is not final.</p>
    </article>

    <article class="entry" id="age-13">
      <span class="age">Age 13</span>
      <p class="said">I was arrested.</p>
      <p class="body">A fight with another boy. <b>I have never spoken about this anywhere.</b></p>
    </article>

    <article class="entry" id="age-14">
      <span class="age">Age 14</span>
      <p class="said">The school threw me out.</p>
      <p class="body">The same year I made my first $40 selling online. I started earning from
        e-commerce to buy shoes and a skateboard, things I could not afford.</p>
    </article>

    <article class="entry" id="age-21">
      <span class="age">Age 21</span>
      <p class="said">eBay closed the account that paid my bills.</p>
      <p class="body">It was my only income. Seven years of work gone in a morning. I opened 100
        stores instead of one, then wrote the software to run them. That software became AutoDS.</p>
    </article>

    <article class="entry" id="age-23">
      <span class="age">Age 23</span>
      <p class="said">I became a millionaire.</p>
      <p class="body">All I wanted was to give other people the chance I had to build for myself:
        earn online, from anywhere, with nobody's permission. <b>1.8 million people use it now, and
        more than a billion dollars has been earned through it by people I have never met.</b></p>
    </article>

    <article class="entry" id="age-26">
      <span class="age">Age 26</span>
      <p class="said">I turned down $30 million for the company.</p>
      <p class="body">A private equity firm wanted to buy it. Six months of due diligence, everyone
        ready to sign. Then I understood the plan: cut the team, squeeze the company for cash.
        <b>Those people had been with me for years, on salaries below what the market would have
        paid them. I could not do that to them. I walked away the day before closing.</b></p>
    </article>

    <article class="entry" id="age-28">
      <span class="age">Age 28</span>
      <p class="said">Fiverr bought my company for a reported $92 million.</p>
      <p class="body">23 days from first call to signed, with 200 people on the team. Built with
        no investors, not one dollar from anyone outside.</p>
    </article>

    <article class="entry" id="age-29">
      <span class="age">Age 29</span>
      <p class="said">Forbes put me on the 30 Under 30 list.</p>
      <p class="body">(My mother still asks when I am going back to programming.)</p>
      <p class="body">That was also when I started paying attention to my own wellbeing. A Tony
        Robbins conference every year since. A Wim Hof retreat. Ice baths. Training. What I eat.</p>
      <p class="body"><b>About 10 hours of my week go into working on myself. Therapy, mentors,
        gym, learning. It is the first thing most founders cut when the calendar fills up, and the
        last thing I will ever cut.</b></p>
    </article>

    <article class="entry" id="age-31">
      <span class="age">Age 31</span>
      <p class="said">I am still the CEO, and I am already building the next thing.</p>
      <p class="body">Founder of four products, and Shopify's #1 partner and affiliate.
        <b>The next one I have not talked about anywhere,
        and I am ready to talk about it with you.</b></p>
    </article>

  </div>

  <section>
    <h2>My core beliefs</h2>
    <div class="beliefs">

      <div class="belief">
        <span class="bn">01</span>
        <div class="bmain">
          <p class="btitle">A no is not final.</p>
          <div class="bbody">
            <p>A life is mostly made of other people's no's. The only decision left is which ones
              you accept.</p>
            <div class="nos">
              <span>A school said no to me at 14. I was selling online by the end of that year.</span>
              <span>eBay said no at 21. I opened 100 stores and wrote the software that became AutoDS.</span>
              <span>I said no to $30 million the day before signing, because the plan was to cut my team. Two years later Fiverr paid $92 million.</span>
            </div>
            <p class="kicker">Every no I was given took me somewhere better. That is my engine.</p>
          </div>
        </div>
      </div>

      <div class="belief">
        <span class="bn">02</span>
        <div class="bmain">
          <p class="btitle">Life is a game, and there is no finish line.</p>
          <div class="bbody">
            <p>The game was the point. Money is how it keeps score. Every level has the same shape:
              a problem I cannot solve, and a version of me who has to become the person who can.</p>
            <p class="kicker">Treat it like a game. The day it stops being fun, you're playing the
              wrong one.</p>
          </div>
        </div>
      </div>

      <div class="belief">
        <span class="bn">03</span>
        <div class="bmain">
          <p class="btitle">Life is beta.</p>
          <div class="bbody">
            <p>Nothing I have built has ever been finished, including me. I ship before it is ready
              and let reality tell me what to fix. Every version of me so far has been replaced by a
              better one, and this one will be too.</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <section>
    <h2>Hear me unscripted</h2>
    <a class="tape" href="https://reallifesuperpowers.com/podcast/lior-pozin-co-founder-ceo-autods/" target="_blank" rel="noopener">
      <span class="dot"></span>
      <span class="t">Real Life Superpowers</span>
    </a>
  </section>

  <figure class="stage">
    <img src="URL_OF_PHOTO_2" alt="Lior Pozin speaking on stage with a headset microphone, a clicker in his hand, in front of a large screen.">
  </figure>

  <footer>
    <p class="sign"><b>Lior Pozin</b><br>Co-founder and CEO, AutoDS, part of Fiverr<br>
      <a class="site" href="https://liorpozin.com" target="_blank" rel="noopener">liorpozin.com</a></p>
    <p class="beta">[ life is beta ]</p>
  </footer>

</div>

<script>
  (function () {
    var entries = Array.prototype.slice.call(document.querySelectorAll('.entry'));
    var fill = document.getElementById('tlfill');
    var tl = document.querySelector('.tl');
    if (!entries.length || !tl) return;


    var queued = false;
    function paint() {
      queued = false;
      var line = window.innerHeight * 0.55;
      var active = -1;
      entries.forEach(function (el, n) {
        var top = el.getBoundingClientRect().top;
        var passed = top < line;
        el.classList.toggle('on', passed);
        if (passed) active = n;
      });
      var tlTop = tl.getBoundingClientRect().top;
      var h = active < 0 ? 0 : (entries[active].getBoundingClientRect().top - tlTop) + 13;
      fill.style.height = Math.max(0, Math.min(tl.offsetHeight, h)) + 'px';
    }
    function onScroll() {
      if (queued) return;
      queued = true;
      requestAnimationFrame(paint);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    paint();
  })();
</script>
</div>

```

---

## אחרי הבנייה

1. להעלות את שתי התמונות
2. להחליף `URL_OF_PHOTO_1` בכתובת של תמונת הנאסד"ק
3. להחליף `URL_OF_PHOTO_2` בכתובת של תמונת הבמה
4. לוודא ש-noindex דלוק ושהכתובת לא ניתנת לניחוש
5. לפרסם ולפתוח בטלפון

## אם Base44 מנסה לעצב מחדש

להגיד לו: "Do not redesign. Render the HTML exactly as I gave it."
אם הוא ממשיך לשנות, לבנות עמוד ריק ולהדביק את `base44-paste-this.html` כבלוק HTML ידני.
