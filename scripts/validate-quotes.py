#!/usr/bin/env python3
"""Validate the daily-quote pool (data/quotes/quotes.json) and the README markers.

Checks (run by .github/workflows/quote-check.yml on PRs):
- JSON loads; >= 10 quotes; unique ids
- every quote: non-empty English text, author with born/died, died <= 1955
  (public domain in the EU as of 2026 - see licenses/quotes-public-domain.md)
- every quote has >= 2 source URLs (http/https)
- no excluded (controversial) player appears anywhere in the pool
- README.md contains exactly one daily-quote:start / daily-quote:end marker pair
- update-quote.py --check passes (rendered block matches a pool entry)
"""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
POOL = ROOT / "data" / "quotes" / "quotes.json"
README = ROOT / "README.md"

# Players deliberately excluded because of documented negative headlines
# (see licenses/quotes-public-domain.md section 3), plus players who died after
# 1955 (not public domain in the EU yet). Matched as whole words against the
# author field of each pool entry.
EXCLUDED_AUTHORS = [
    "Fischer", "Alekhine", "Bogoljubow", "Tartakower", "Rubinstein",
    "Marshall", "Tal",
]
MAX_DIED_YEAR = 1955  # EU public domain (life+70) as of 2026


def fail(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    data = json.loads(POOL.read_text(encoding="utf-8"))
    quotes = data.get("quotes", [])
    if len(quotes) < 10:
        fail(f"pool has {len(quotes)} quotes, need >= 10")

    ids = set()
    for q in quotes:
        qid = q.get("id", "")
        if not qid or qid in ids:
            fail(f"missing/duplicate id: {qid!r}")
        ids.add(qid)
        if not q.get("quote", "").strip():
            fail(f"{qid}: empty quote")
        if not re.fullmatch(r"[\x20-\x7e\u2013\u2014\u2018\u2019\u201c\u201d\u00e9\u00e8\u00e0\u00f3\u00ed\u00f1\u00e1\u00fa\u00f6\u00fc\u00df\u0161\u010d\u017e\u0105\u0142\u0159\u0159\s.,;:!?()\u00ab\u00bb'-]+", q["quote"]):
            fail(f"{qid}: quote is not plain English text: {q['quote']!r}")
        author = q.get("author", "")
        if not author:
            fail(f"{qid}: missing author")
        for bad in EXCLUDED_AUTHORS:
            if re.search(rf"\b{re.escape(bad)}\b", author):
                fail(f"{qid}: excluded player {bad!r} in author {author!r}")
        died = q.get("died")
        if not isinstance(died, int) or died > MAX_DIED_YEAR:
            fail(f"{qid}: author {author} died {died!r}, must be <= {MAX_DIED_YEAR} (PD in EU as of 2026)")
        if q.get("born", 0) >= died:
            fail(f"{qid}: born >= died for {author}")
        srcs = q.get("sources", [])
        urls = [s for s in srcs if urlparse(s).scheme in ("http", "https")]
        if len(urls) < 2:
            fail(f"{qid}: needs >= 2 http(s) sources, has {len(urls)}")
        if not q.get("pdBasis"):
            fail(f"{qid}: missing pdBasis")

    text = README.read_text(encoding="utf-8")
    for marker in ("<!-- daily-quote:start -->", "<!-- daily-quote:end -->"):
        if text.count(marker) != 1:
            fail(f"README.md must contain exactly one {marker!r}")

    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "update-quote.py"), "--check"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        fail(f"update-quote.py --check failed: {r.stderr.strip()}")

    authors = sorted({q["author"] for q in quotes})
    print(f"OK: {len(quotes)} verified public-domain quotes; authors: {', '.join(authors)}")


if __name__ == "__main__":
    main()
