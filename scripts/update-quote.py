#!/usr/bin/env python3
"""Rotate the daily quote shown on the About page (README.md).

Reads the verified public-domain quote pool from data/quotes/quotes.json, picks
the quote for the current UTC day with the same deterministic rule as the daily
puzzles (floor(unix_ms / 86400000) % len(quotes)), and renders it as a styled
English blockquote between the <!-- daily-quote:start --> / <!-- daily-quote:end -->
markers in README.md.

Usage:
  python3 scripts/update-quote.py            # update README.md in place (run per release; quote-check validates on every PR)
  python3 scripts/update-quote.py --check    # verify markers exist once and the rendered block matches a pool entry (CI)
  python3 scripts/update-quote.py --date 2026-11-23 --print   # render a specific day without writing
"""
import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POOL = ROOT / "data" / "quotes" / "quotes.json"
README = ROOT / "README.md"
START = "<!-- daily-quote:start -->"
END = "<!-- daily-quote:end -->"

BODY = (
    '<blockquote style="max-width:680px;margin:1.2rem auto;padding:.6rem 0 .6rem 1.2rem;border-left:4px solid #b58863;">\n'
    '  <p style="margin:0;font-size:1.05rem;"><em>\u201c{quote}\u201d</em></p>\n'
    '  <footer style="margin-top:.4rem;font-size:.85rem;opacity:.75;">\u2014 {author} ({born}\u2013{died}) \u00b7 <cite>{work}</cite></footer>\n'
    "</blockquote>"
)


def render_body(q):
    return BODY.format(
        quote=html.escape(q["quote"], quote=True),
        author=html.escape(q["author"], quote=True),
        born=q["born"],
        died=q["died"],
        work=html.escape(q.get("workShort", q["work"]), quote=True),
    )


def render(q):
    return f"{START}\n{render_body(q)}\n{END}"


def load_pool():
    data = json.loads(POOL.read_text(encoding="utf-8"))
    quotes = data["quotes"]
    if not quotes:
        raise SystemExit("quote pool is empty")
    return quotes


def day_index(dt):
    return dt.timestamp() // 86400


def pick(quotes, dt):
    return quotes[int(day_index(dt)) % len(quotes)]





def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify README markers/block instead of writing")
    ap.add_argument("--date", help="UTC date YYYY-MM-DD (for --print/testing)")
    ap.add_argument("--print", dest="do_print", action="store_true", help="print the rendered block, do not write")
    args = ap.parse_args()

    quotes = load_pool()
    if args.date:
        dt = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        dt = datetime.now(timezone.utc)
    q = pick(quotes, dt)
    block = render(q)

    if args.do_print:
        print(block)
        print(f"# id={q['id']} dayIndex={int(day_index(dt))}", file=sys.stderr)
        return

    text = README.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        raise SystemExit(f"expected exactly one {START!r} and one {END!r} in README.md")

    pattern = re.escape(START) + r"\n.*?" + re.escape(END)

    if args.check:
        m = re.search(pattern, text, re.S)
        if not m:
            raise SystemExit("daily-quote markers found but block between them is malformed")
        current = m.group(0)[len(START) + 1 : -len(END)].rstrip("\n")
        if current not in {render_body(x) for x in quotes}:
            raise SystemExit("README daily-quote block does not match any quote in the pool")
        print("daily-quote block OK (matches pool entry)")
        return

    new_text = re.sub(pattern, lambda _: block, text, count=1, flags=re.S)
    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print(f"updated README.md daily quote -> {q['id']} ({q['author']})")
    else:
        print(f"daily quote unchanged ({q['id']})")


if __name__ == "__main__":
    main()
