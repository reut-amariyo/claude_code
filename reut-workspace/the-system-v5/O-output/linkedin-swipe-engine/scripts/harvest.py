#!/usr/bin/env python3
"""
LinkedIn swipe engine — Bright Data harvester.

Modes:
  probe     1 post per creator, verifies every slug resolves to the right person
  backfill  N posts per creator (default 20), builds the per-creator median baseline
  daily     5 posts per creator, merges into the log, writes the day's report skeleton
  report    re-render today's report skeleton from the log without calling Bright Data

Key:  ~/.config/brightdata/api_key  or  env BRIGHTDATA_API_KEY
Data: data/creators.json (roster), data/posts.jsonl (one line per post, metrics history),
      data/runs.jsonl (every Bright Data job), daily-reports/YYYY-MM-DD-report.md
"""
import json, os, re, sys, time, statistics, urllib.request, urllib.parse, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "daily-reports"
DATASET = "gd_lyy3tktm25m4avu764"          # Bright Data "LinkedIn posts"
API = "https://api.brightdata.com/datasets/v3"
WINDOW_H = 72                              # scoring window for the daily report
W_COMMENTS, W_LIKES = 3, 1                 # Bright Data returns no repost count
XM_CAP = 10                                # outlier multiplier ceiling
# Reference-grade bar (Reut, 2026-09-20): a post is a candidate donor only if ALL hold.
# Topic fit is still Claude's call on top of this.
REF_MIN_WORDS = 40                         # text must carry the post; image-only / caption posts never qualify
REF_MIN_XM = 2.0                           # clear outlier for that specific creator
REF_MIN_LIKES, REF_MIN_COMMENTS = 1000, 200  # and strong in absolute terms (either)

def key():
    k = os.environ.get("BRIGHTDATA_API_KEY")
    if not k:
        p = Path.home() / ".config/brightdata/api_key"
        k = p.read_text().strip() if p.exists() else ""
    if not k:
        sys.exit("no Bright Data key: set BRIGHTDATA_API_KEY or ~/.config/brightdata/api_key")
    return k

def req(url, data=None):
    r = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read().decode())

def load_creators(all_=False):
    cs = json.load(open(DATA / "creators.json"))
    return cs if all_ else [c for c in cs if c.get("harvestable", True)]

def load_posts():
    p = DATA / "posts.jsonl"
    if not p.exists(): return {}
    out = {}
    with open(p, encoding="utf-8") as f:
        for line in f:                       # split on \n only; post text can hold U+2028
            if line.strip():
                d = json.loads(line); out[d["id"]] = d
    return out

def save_posts(posts):
    with open(DATA / "posts.jsonl", "w") as f:
        for d in sorted(posts.values(), key=lambda x: x.get("date_posted") or ""):
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------- Bright Data
def trigger(urls, limit):
    q = urllib.parse.urlencode({"dataset_id": DATASET, "type": "discover_new",
        "discover_by": "profile_url", "limit_per_input": limit, "include_errors": "true"})
    body = json.dumps([{"url": u} for u in urls]).encode()
    return req(f"{API}/trigger?{q}", body)["snapshot_id"]

def wait(snapshot_id, every=15, max_min=40):
    t0 = time.time()
    while time.time() - t0 < max_min * 60:
        p = req(f"{API}/progress/{snapshot_id}")
        s = p.get("status")
        print(f"  {dt.datetime.now():%H:%M:%S} {s} records={p.get('records')}", flush=True)
        if s == "ready": return p
        if s == "failed": sys.exit(f"job failed: {p}")
        time.sleep(every)
    sys.exit("timed out waiting for Bright Data")

def download(snapshot_id, tries=10):
    # progress can say "ready" while the snapshot endpoint still answers {"status": "building"} (seen 2026-09-21)
    for _ in range(tries):
        recs = req(f"{API}/snapshot/{snapshot_id}?format=json")
        if isinstance(recs, list): return recs
        print(f"  snapshot not served yet: {recs}", flush=True)
        time.sleep(30)
    sys.exit(f"snapshot {snapshot_id} never became downloadable")

def run_job(mode, limit, creators):
    urls = [c["url"] for c in creators]
    print(f"{mode}: {len(urls)} profiles x {limit} posts", flush=True)
    sid = trigger(urls, limit)
    print("  snapshot", sid, flush=True)
    prog = wait(sid)
    recs = download(sid)
    (DATA / "raw").mkdir(exist_ok=True)
    json.dump(recs, open(DATA / "raw" / f"{sid}.json", "w"))
    with open(DATA / "runs.jsonl", "a") as f:
        f.write(json.dumps({"ts": dt.datetime.utcnow().isoformat(), "mode": mode, "snapshot": sid,
                            "inputs": len(urls), "limit": limit, "records": prog.get("records"),
                            "errors": prog.get("errors")}) + "\n")
    return recs

# ---------------------------------------------------------------- merge
def is_repost(post_url, creator_slug):
    m = re.search(r"/posts/([^_/]+)_", post_url)
    return bool(m) and m.group(1).lower() != creator_slug.lower()

def input_url(r):
    for k in ("discovery_input", "input"):
        v = r.get(k)
        if isinstance(v, dict) and v.get("url"): return v["url"]
        if isinstance(v, str) and "linkedin.com/in/" in v: return v
    return ""

def media_of(r):
    if r.get("document_cover_image") or r.get("document_page_count"): return "document"
    if r.get("videos"): return "video"
    if r.get("images"): return "image"
    if r.get("external_link_data") or r.get("embedded_links"): return "link"
    return "text"

def merge(recs, creators, today):
    by_url = {c["url"].rstrip("/").lower(): c for c in creators}
    posts = load_posts()
    errors, seen_creators, new = [], set(), 0
    for r in recs:
        inp = input_url(r)
        c = by_url.get(inp.rstrip("/").lower())
        if r.get("error") or not r.get("url"):
            errors.append({"creator": c["name"] if c else inp, "error": r.get("error") or "empty"})
            continue
        if not c: continue
        seen_creators.add(c["id"])
        pid = r.get("id") or r["url"]
        likes, comments = int(r.get("num_likes") or 0), int(r.get("num_comments") or 0)
        text = r.get("post_text") or ""
        hook = next((l.strip() for l in text.splitlines() if l.strip()), "")[:120] or "[image-only]"
        imgs = r.get("images") or []
        d = posts.get(pid) or {"id": pid, "url": r["url"], "creator_id": c["id"], "creator": c["name"],
                               "first_seen": today, "snapshots": []}
        new += pid not in posts
        d.update({"date_posted": r.get("date_posted"), "post_type": r.get("post_type"),
                  "media": media_of(r), "doc_pages": r.get("document_page_count"),
                  "author_seen": r.get("user_name"), "author_followers": r.get("user_followers"),
                  "is_repost": is_repost(r["url"], c["slug"]), "hashtags": r.get("hashtags") or [],
                  "hook": hook, "text": text, "image": imgs[0] if imgs else None,
                  "likes": likes, "comments": comments,
                  "score": comments * W_COMMENTS + likes * W_LIKES})
        if not d["snapshots"] or d["snapshots"][-1]["date"] != today:
            d["snapshots"].append({"date": today, "likes": likes, "comments": comments})
        else:
            d["snapshots"][-1] = {"date": today, "likes": likes, "comments": comments}
        posts[pid] = d
    save_posts(posts)
    return posts, errors, seen_creators, new

# ---------------------------------------------------------------- baselines + scoring
def baselines(posts, creators, min_age_h=24, min_n=5):
    now = dt.datetime.now(dt.timezone.utc)
    out = {}
    for c in creators:
        scores = []
        for p in posts.values():
            if p["creator_id"] != c["id"] or p.get("is_repost"): continue
            try: age = (now - dt.datetime.fromisoformat(p["date_posted"].replace("Z", "+00:00"))).total_seconds() / 3600
            except Exception: continue
            if age >= min_age_h: scores.append(p["score"])
        out[c["id"]] = {"n": len(scores), "median": statistics.median(scores) if len(scores) >= min_n else None}
    json.dump(out, open(DATA / "baselines.json", "w"), indent=1)
    return out

def render_report(posts, creators, base, today, errors=None, new=0):
    now = dt.datetime.now(dt.timezone.utc)
    cmap = {c["id"]: c for c in creators}
    fit_path = DATA / "lior-fit.json"                      # {post_url: "✅ note" | "⚠️ note" | "❌ note"}, written by Claude
    fit = json.load(open(fit_path)) if fit_path.exists() else {}
    rows = []
    for p in posts.values():
        try: age = (now - dt.datetime.fromisoformat(p["date_posted"].replace("Z", "+00:00"))).total_seconds() / 3600
        except Exception: continue
        if age > WINDOW_H or p.get("is_repost"): continue
        med = (base.get(p["creator_id"]) or {}).get("median")
        big_enough = p["likes"] >= 100 or p["comments"] >= 20     # tiny posts never get the multiplier
        xm = round(min(p["score"] / med, XM_CAP), 1) if med and big_enough else None
        final = p["score"] * (xm if xm else 1)
        snaps = p["snapshots"]
        if len(snaps) >= 2:
            prev = snaps[-2]; delta = (p["likes"] - prev["likes"], p["comments"] - prev["comments"])
            status = f"climbing +{delta[0]}/+{delta[1]}"
        else:
            status = "NEW"
        words = len((p.get("text") or "").split())
        fol = p.get("author_followers") or 0
        per10k = p["likes"] / fol * 10000 if fol else None
        ref = (words >= REF_MIN_WORDS and (xm or 0) >= REF_MIN_XM
               and (p["likes"] >= REF_MIN_LIKES or p["comments"] >= REF_MIN_COMMENTS)
               and cmap[p["creator_id"]]["donor"] != "red")
        rows.append((final, p, xm, status, round(age), per10k, ref))
    rows.sort(key=lambda x: (-x[6], -x[0]))            # reference-grade first, then by final score
    creators_seen = len({r[1]["creator_id"] for r in rows})
    n_ref = sum(1 for r in rows if r[6])
    L = [f"# Swipe report — {today}", "",
         f"Posts in the {WINDOW_H}h window: **{len(rows)}** from **{creators_seen}** creators. "
         f"New posts logged this run: {new}. **Reference-grade posts (★): {n_ref}.**",
         f"★ = text of {REF_MIN_WORDS}+ words, x{REF_MIN_XM:g}+ the creator's median, and {REF_MIN_LIKES:,}+ likes or {REF_MIN_COMMENTS}+ comments, creator not barred. "
         f"Only ★ rows can become teardowns or go in the morning summary. Image-only posts never qualify.",
         f"Score = comments x{W_COMMENTS} + likes x{W_LIKES}, then x the creator's median where known "
         f"(baselines: {sum(1 for b in base.values() if b['median'])}/{len(creators)} creators).", ""]
    have = {p["creator_id"] for p in posts.values()}
    zero = sorted(c["name"] for c in creators if c["id"] not in have)
    if zero:
        L += [f"⚠️ No posts on file for: " + ", ".join(zero), ""]
    L += ["## 1. Ranked table", "",
          "| Rank | ★ | Creator | Hook | Likes | Comm | /10K fol | xMedian | Final | Media | Age | Status | Donor | Lior fit |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, (final, p, xm, status, age, per10k, ref) in enumerate(rows, 1):
        c = cmap[p["creator_id"]]
        donor = {"green": "🟢", "yellow": "🟡", "red": "🔴 tracked, not usable"}[c["donor"]]
        lf = "🔴 moratorium" if c["donor"] == "red" else fit.get(p["url"], "")
        hook = p["hook"].replace("|", "/")
        L.append(f"| {i} | {'★' if ref else ''} | [{c['name']}]({p['url']}) | {hook} | {p['likes']:,} | {p['comments']:,} | "
                 f"{round(per10k) if per10k else '–'} | {xm if xm else '–'} | {round(final):,} | {p['media']}{'/'+str(p['doc_pages'])+'p' if p.get('doc_pages') else ''} | "
                 f"{age}h | {status} | {donor} | {lf} |")
    L += ["", "## 2. Donor teardowns — ★ rows only, up to 3", "", "_(Claude fills: beat table per ★ post that also passes the topic bar, AI tells to strip, "
          "'why would a stranger follow?'. If there are no ★ rows that pass, write 'No reference-grade post today' and stop.)_", "", "## 3. Pattern of the day", "", "_(Claude fills)_", "",
          "## 4. Watch list", "", "_(Claude fills: creators whose numbers moved sharply)_", ""]
    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"{today}-report.md"
    if out.exists() and "## 2. Donor teardowns" in out.read_text():   # keep Claude's sections on re-render
        tail = out.read_text().split("## 2. Donor teardowns", 1)[1]
        L = L[:next(i for i, x in enumerate(L) if x.startswith("## 2. Donor teardowns"))] + ["## 2. Donor teardowns" + tail]
    out.write_text("\n".join(L))
    return out, rows

# ---------------------------------------------------------------- modes
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "daily"
    today = dt.date.today().isoformat()
    creators = load_creators()
    if mode == "probe" and len(sys.argv) > 2:
        ids = {int(x) for x in sys.argv[2].split(",")}
        creators = [c for c in creators if c["id"] in ids]
    if mode == "probe":
        recs = run_job("probe", 1, creators)
        by_url = {c["url"].rstrip("/").lower(): c for c in creators}
        print(f"\n{'id':>3}  {'roster name':<26} {'author returned':<28} {'followers':>9}  note")
        for r in recs:
            inp = input_url(r)
            c = by_url.get(inp.rstrip("/").lower(), {"id": "?", "name": inp})
            if r.get("error") or not r.get("url"):
                print(f"{c['id']:>3}  {c['name']:<26} {'-- ERROR --':<28} {'':>9}  {r.get('error') or 'no posts'}"); continue
            author = (r.get("user_name") or r.get("user_id") or "")[:28]
            fam = c["name"].split()[-1].lower()
            note = "repost, ignore" if is_repost(r["url"], c.get("slug", "")) else ("" if fam in author.lower() or c["name"].split()[0].lower() in author.lower() else "CHECK NAME")
            print(f"{c['id']:>3}  {c['name']:<26} {author:<28} {str(r.get('user_followers') or ''):>9}  {note}")
        merge(recs, creators, today)
        return
    if mode == "merge":                      # harvest.py merge <snapshot_id>  (no Bright Data call)
        sid = sys.argv[2]
        raw = DATA / "raw" / f"{sid}.json"
        recs = json.load(open(raw)) if raw.exists() else download(sid)
        (DATA / "raw").mkdir(exist_ok=True); json.dump(recs, open(raw, "w"))
        posts, errors, seen, new = merge(recs, creators, today)
        print(f"  merged: {len(recs)} records, {new} new posts, {len(seen)} creators, {len(errors)} errors")
    elif mode in ("backfill", "daily"):
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else (20 if mode == "backfill" else 5)
        recs = run_job(mode, limit, creators)
        posts, errors, seen, new = merge(recs, creators, today)
        print(f"  merged: {len(recs)} records, {new} new posts, {len(seen)} creators, {len(errors)} errors")
    else:
        posts, errors, new = load_posts(), None, 0
    base = baselines(posts, creators)
    out, rows = render_report(posts, creators, base, today, errors, new)
    print(f"  report: {out}  ({len(rows)} posts in window)")

if __name__ == "__main__":
    main()
