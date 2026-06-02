#!/usr/bin/env python3
"""Per-handle reply outcome report — data to prune the X reply whitelist.

Aggregates every reply attempt logged in O-output/x-performance-log/replies.jsonl
by author handle, then flags whitelist accounts that are pure 403 walls or have a
low success rate. This is the data layer for the fix in
[[x-reply-pipeline-whitelist-collapse]]: the whitelist now strictly wins over the
auto-blocker, so accounts that never accept a reply must be pruned by hand using
real outcomes rather than guessed at.

Usage:
    reply_whitelist_stats.py [--min-attempts N] [--min-success-rate PCT] [--all]

    --min-attempts      attempts before a 0-success handle is prune-recommended (default 4)
    --min-success-rate  success-rate floor in percent below which a handle is flagged (default 20)
    --all               also show non-whitelist authors we've replied to

Reads only — never modifies the whitelist or blocklist. Use its recommendations to
edit ~/.scout-reply-whitelist.json yourself.
"""

import argparse
import json
import sys
from pathlib import Path

PERFORMANCE_LOG = Path(__file__).resolve().parents[3] / "O-output" / "x-performance-log" / "replies.jsonl"
WHITELIST_FILE = Path.home() / ".scout-reply-whitelist.json"
BLOCKED_AUTHORS_FILE = Path.home() / ".scout-blocked-authors.json"


def norm(handle):
    return (handle or "").lower().lstrip("@")


def load_handle_set(path, key):
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text())
        return {norm(h) for h in data.get(key, [])}
    except (json.JSONDecodeError, KeyError):
        return set()


def load_stats():
    """Return {handle: {success, fail_403, fail_other, last_success, last_403}}."""
    stats = {}
    unattributed = {"success": 0, "fail_403": 0, "fail_other": 0}
    if not PERFORMANCE_LOG.exists():
        return stats, unattributed
    for line in PERFORMANCE_LOG.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        handle = norm(rec.get("author"))
        status = rec.get("status")
        when = rec.get("replied_at", "")
        # Older records predate the author field; bucket them as unattributed so
        # totals stay honest rather than silently dropping them.
        if not handle:
            if status == "success":
                unattributed["success"] += 1
            elif rec.get("failure_kind") == "403_reply_restricted" or "403" in str(rec.get("error_message", "")):
                unattributed["fail_403"] += 1
            elif status == "failed":
                unattributed["fail_other"] += 1
            continue
        s = stats.setdefault(handle, {
            "success": 0, "fail_403": 0, "fail_other": 0,
            "last_success": "", "last_403": "",
        })
        if status == "success":
            s["success"] += 1
            s["last_success"] = max(s["last_success"], when)
        elif rec.get("failure_kind") == "403_reply_restricted" or "403" in str(rec.get("error_message", "")):
            s["fail_403"] += 1
            s["last_403"] = max(s["last_403"], when)
        elif status == "failed":
            s["fail_other"] += 1
    return stats, unattributed


def rate(s):
    attempts = s["success"] + s["fail_403"] + s["fail_other"]
    return (100.0 * s["success"] / attempts) if attempts else None


def fmt_row(handle, s, flag):
    attempts = s["success"] + s["fail_403"] + s["fail_other"]
    r = rate(s)
    r_str = f"{r:5.0f}%" if r is not None else "   --"
    last = s["last_success"][:10] if s["last_success"] else (
        f"403:{s['last_403'][:10]}" if s["last_403"] else "never")
    return (f"  {flag:2} @{handle:<16} att {attempts:>3}  "
            f"ok {s['success']:>3}  403 {s['fail_403']:>3}  err {s['fail_other']:>3}  "
            f"rate {r_str}  last {last}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-attempts", type=int, default=4)
    ap.add_argument("--min-success-rate", type=float, default=20.0)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    whitelist = load_handle_set(WHITELIST_FILE, "handles")
    blocked = load_handle_set(BLOCKED_AUTHORS_FILE, "authors")
    stats, unattributed = load_stats()

    if not PERFORMANCE_LOG.exists():
        print(f"No performance log yet at {PERFORMANCE_LOG}.", file=sys.stderr)
        print("Run some replies first — stats accrue as reply_x.py logs outcomes.", file=sys.stderr)
        sys.exit(0)

    empty = {"success": 0, "fail_403": 0, "fail_other": 0, "last_success": "", "last_403": ""}

    print(f"\nX REPLY WHITELIST — per-handle outcomes  (source: {PERFORMANCE_LOG.name})")
    print("=" * 78)

    prune, keep, untested = [], [], []
    for h in sorted(whitelist):
        s = stats.get(h, dict(empty))
        attempts = s["success"] + s["fail_403"] + s["fail_other"]
        r = rate(s)
        if attempts == 0:
            untested.append(h)
            flag = "?"
        elif s["success"] == 0 and attempts >= args.min_attempts:
            prune.append(h); flag = "X"
        elif r is not None and r < args.min_success_rate and attempts >= args.min_attempts:
            prune.append(h); flag = "x"
        else:
            keep.append(h); flag = "OK"
        print(fmt_row(h, s, flag))

    print("-" * 78)
    print(f"  Legend: OK=keep  x/X=prune candidate  ?=untested (no attempts yet)")
    print(f"  Thresholds: prune if attempts>={args.min_attempts} and "
          f"(0 successes OR success-rate<{args.min_success_rate:.0f}%)")

    if prune:
        print(f"\n  >> PRUNE {len(prune)} (never/rarely accept a reply): "
              + ", ".join(prune))
    if untested:
        print(f"  >> UNTESTED {len(untested)} (no reply attempts logged yet): "
              + ", ".join(untested))
    if keep:
        print(f"  >> KEEP {len(keep)}: " + ", ".join(keep))

    # Sanity check: a whitelisted handle sitting in the active blocklist means the
    # exemption fix regressed — surface it loudly.
    leaked = sorted(whitelist & blocked)
    if leaked:
        print(f"\n  !! WARNING: {len(leaked)} whitelisted handles are in the active "
              f"blocklist — the exemption may have regressed: {', '.join(leaked)}")

    tot = sum(v for s in stats.values() for k, v in s.items() if k in ("success", "fail_403", "fail_other"))
    una = sum(unattributed.values())
    if una:
        print(f"\n  Note: {una} older log records have no author field "
              f"(success {unattributed['success']}/403 {unattributed['fail_403']}/err {unattributed['fail_other']}) "
              f"— excluded from per-handle rows. {tot} attributed.")

    if args.all:
        others = sorted(set(stats) - whitelist)
        if others:
            print("\n  NON-WHITELIST authors replied to:")
            for h in others:
                print(fmt_row(h, stats[h], "·"))
    print()


if __name__ == "__main__":
    main()
