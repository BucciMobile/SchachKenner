#!/usr/bin/env python3
"""validate-puzzles.py — CI check for the hosted daily-puzzle dataset.

Verifies (exits non-zero on any failure):
  * data/puzzles/index.json exists, >= 2000 puzzles total, >= 600 per level, unique ids
  * every referenced data/puzzles/<level>.json and data/pgn/puzzles/<level>/<id>.pgn exists
  * every PGN parses (python-chess), has SetUp/FEN + PuzzleId headers matching the index,
    and its mainline is exactly the entry's solution (legal moves, correct SAN)
  * the daily selection rule produces valid ids for a range of UTC dates
  * manifest.json SHA-256 hashes match (if manifest exists)

Usage: python3 scripts/validate-puzzles.py [--repo .]
Requires: python-chess (pip install python-chess)
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

import chess
import chess.pgn

LEVELS = ["easy", "medium", "hard"]
LEVEL_OFFSET = {"easy": 0, "medium": 1, "hard": 2}


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(here, "..")))
    args = ap.parse_args()
    repo = args.repo
    pdir = os.path.join(repo, "data", "puzzles")
    index_path = os.path.join(pdir, "index.json")
    if not os.path.exists(index_path):
        fail(f"missing {index_path} — run scripts/build-puzzles.py first")
    index = json.load(open(index_path, encoding="utf-8"))

    count = index.get("count", 0)
    if count < 2000:
        fail(f"only {count} puzzles, need >= 2000")
    seen = set()
    for lv in LEVELS:
        meta = index["levels"][lv]
        ids = meta["ids"]
        if len(ids) < 600:
            fail(f"level {lv}: only {len(ids)} puzzles, need >= 600")
        if len(set(ids)) != len(ids):
            fail(f"level {lv}: duplicate ids")
        dup = seen.intersection(ids)
        if dup:
            fail(f"level {lv}: ids also present in another level: {sorted(dup)[:5]}")
        seen.update(ids)
        lf = os.path.join(pdir, meta["file"])
        if not os.path.exists(lf):
            fail(f"missing {lf}")
        level_data = json.load(open(lf, encoding="utf-8"))
        entries = level_data["puzzles"]
        if sorted(entries.keys()) != sorted(ids):
            fail(f"level {lv}: index ids and {meta['file']} entries differ")
        for pid, e in entries.items():
            for k in ("fen", "side", "moves", "san", "rating", "pgn"):
                if k not in e:
                    fail(f"{lv}/{pid}: entry missing '{k}'")
            pgn_path = os.path.join(repo, e["pgn"])
            if not os.path.exists(pgn_path):
                fail(f"{lv}/{pid}: missing PGN {e['pgn']}")
                continue
            with open(pgn_path, encoding="utf-8") as fh:
                game = chess.pgn.read_game(fh)
            if game is None:
                fail(f"{lv}/{pid}: PGN does not parse")
                continue
            h = game.headers
            if h.get("PuzzleId") != pid:
                fail(f"{lv}/{pid}: PGN PuzzleId header is {h.get('PuzzleId')!r}")
            if h.get("SetUp") != "1" or h.get("FEN") != e["fen"]:
                fail(f"{lv}/{pid}: PGN FEN/SetUp mismatch")
            board = game.board()
            if board.fen() != e["fen"] or board.is_game_over():
                fail(f"{lv}/{pid}: start position invalid or already over")
            node = game
            uci_line, san_line = [], []
            while not node.is_end():
                node = node.variation(0)
                uci_line.append(node.move.uci())
                san_line.append(board.san(node.move))
                board.push(node.move)
            if uci_line != e["moves"]:
                fail(f"{lv}/{pid}: PGN movetext {uci_line} != index moves {e['moves']}")
            if san_line != e["san"]:
                fail(f"{lv}/{pid}: SAN mismatch")
    print(f"index OK: {count} puzzles, levels " + ", ".join(f"{lv}={index['levels'][lv]['count']}" for lv in LEVELS))

    # daily selection rule must yield valid ids for a range of dates
    day0 = int(datetime(2026, 1, 1, tzinfo=timezone.utc).timestamp() // 86400)
    for d in range(day0, day0 + 400):
        for lv in LEVELS:
            ids = index["levels"][lv]["ids"]
            pick = ids[(d + LEVEL_OFFSET[lv]) % len(ids)]
            if pick not in index["levels"][lv]["ids"]:
                fail("selection rule produced invalid id")
    print("selection rule OK for 400 consecutive UTC days")

    # the rotation rule must be identical in index.json, docs/puzzles.html and bot/src/puzzles.js
    def read(rel):
        p = os.path.join(repo, rel)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else None
    idx_rule = index.get("selection", {})
    assert idx_rule.get("utcDayIndex", "").startswith("floor(Date.now() / 86400000)"), "index.json selection rule drifted"
    for rel in ("docs/puzzles.html", "bot/src/puzzles.js"):
        src = read(rel)
        if src is None:
            continue
        if "Math.floor(d.getTime() / 86400000)" not in src and "floor(Date.now() / 86400000)" not in src:
            fail(f"{rel}: utcDayIndex formula missing/drifted")
        for lv in LEVELS:
            if f"{lv}: {LEVEL_OFFSET[lv]}" not in src:
                fail(f"{rel}: LEVEL_OFFSET for {lv} missing/drifted")
        if "PUZZLE_WINDOW_DAYS = 7" not in src:
            fail(f"{rel}: PUZZLE_WINDOW_DAYS = 7 missing/drifted (7-day visibility window)")
    print("rotation + 7-day window rules in sync across index.json / docs/puzzles.html / bot/src/puzzles.js")

    manifest_path = os.path.join(pdir, "manifest.json")
    if os.path.exists(manifest_path):
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        for f, want in manifest.get("sha256", {}).items():
            got = sha256_file(os.path.join(pdir, f))
            if got != want:
                fail(f"sha256 mismatch for {f}: {got} != {want}")
        print("manifest sha256 OK")

    print("ALL PUZZLE CHECKS PASSED")


if __name__ == "__main__":
    main()
