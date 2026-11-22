#!/usr/bin/env python3
"""build-puzzles.py — build the SchachKenner daily-puzzle dataset from the lichess
puzzle export (CC0 1.0 — see licenses/lichess-database-cc0.md).

Download the source first:  bash scripts/fetch-puzzles.sh

Outputs (committed to the repo):
  data/puzzles/index.json            small index: level id pools, counts, selection rule
  data/puzzles/<level>.json          full entries per level (fen, moves, san, rating, ...)
  data/puzzles/manifest.json         counts + SHA-256 of the files above
  data/pgn/puzzles/<level>/<id>.pgn  one PGN per puzzle (SetUp/FEN header + solution line)
  data/pgn/puzzles/README.md         dataset description + license

Difficulty bands (lichess puzzle rating): easy < 1200, medium 1200-1700, hard > 1700.
Selection is deterministic (fixed seed), so re-running on the same input reproduces
the same dataset. Daily rotation rule (must match docs/puzzles.html and
bot/src/puzzles.js):  ids[(utcDayIndex + levelOffset) % ids.length]  with
utcDayIndex = floor(unixMillis / 86400000) and levelOffset easy=0, medium=1, hard=2.

Usage:
  python3 scripts/build-puzzles.py [--csv data/downloads/lichess_db_puzzle.csv[.zst]]
                                    [--per-level 800] [--seed 20261121] [--repo .]
Requires: python-chess (pip install python-chess); zstandard only if reading .zst.
"""
import argparse
import csv
import hashlib
import io
import json
import os
import random
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone

import chess
import chess.pgn

LEVELS = ["easy", "medium", "hard"]
LEVEL_LABEL = {"easy": "Leicht", "medium": "Mittel", "hard": "Schwer"}
LEVEL_BAND_TEXT = {"easy": "<1200", "medium": "1200-1700", "hard": ">1700"}
LEVEL_OFFSET = {"easy": 0, "medium": 1, "hard": 2}


def level_for_rating(rating):
    if rating < 1200:
        return "easy"
    if rating <= 1700:
        return "medium"
    return "hard"


def open_maybe_zst(path):
    if path.endswith(".zst"):
        try:
            import zstandard
        except ImportError:
            sys.exit("reading .zst needs 'pip install zstandard' (or unpack with zstd -d first)")
        dctx = zstandard.ZstdDecompressor()
        return io.TextIOWrapper(dctx.stream_reader(open(path, "rb")), encoding="utf-8")
    return open(path, encoding="utf-8", newline="")


def scan_candidates(csv_path, cap_per_level):
    """Stream the export, keep the first cap_per_level rows per difficulty band."""
    buckets = {lv: [] for lv in LEVELS}
    with open_maybe_zst(csv_path) as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            try:
                rating = int(row["Rating"])
            except (KeyError, ValueError):
                continue
            lv = level_for_rating(rating)
            if len(buckets[lv]) >= cap_per_level:
                if all(len(b) >= cap_per_level for b in buckets.values()):
                    break
                continue
            moves = (row.get("Moves") or "").split()
            if not moves or not row.get("FEN") or not row.get("PuzzleId"):
                continue
            buckets[lv].append({
                "id": row["PuzzleId"],
                "fen": row["FEN"],
                "moves": moves,
                "rating": rating,
                "themes": row.get("Themes") or "",
                "gameUrl": row.get("GameUrl") or "",
            })
    return buckets


def validate_and_enrich(cand):
    """Check FEN + solution line with python-chess; return entry dict or None."""
    try:
        board = chess.Board(cand["fen"])
    except ValueError:
        return None
    if board.is_game_over():
        return None
    sans = []
    try:
        for uci in cand["moves"]:
            mv = chess.Move.from_uci(uci)
            if mv not in board.legal_moves:
                return None
            sans.append(board.san(mv))
            board.push(mv)
    except ValueError:
        return None
    side = "w" if chess.Board(cand["fen"]).turn else "b"
    return {
        "fen": cand["fen"],
        "side": side,
        "moves": cand["moves"],
        "san": sans,
        "rating": cand["rating"],
        "themes": cand["themes"],
        "gameUrl": cand["gameUrl"],
    }


def puzzle_pgn(pid, level, entry, generated):
    game = chess.pgn.Game()
    game.headers["Event"] = "SchachKenner Daily Puzzle"
    game.headers["Site"] = "https://github.com/BucciMobile/SchachKenner"
    game.headers["Date"] = generated
    game.headers["PuzzleId"] = pid
    game.headers["Difficulty"] = level
    game.headers["Rating"] = str(entry["rating"])
    if entry["themes"]:
        game.headers["Themes"] = entry["themes"]
    if entry["gameUrl"]:
        game.headers["GameUrl"] = entry["gameUrl"]
    game.headers["Solution"] = " ".join(entry["moves"])
    game.headers["SolutionSAN"] = " ".join(entry["san"])
    board = chess.Board(entry["fen"])
    game.setup(board)
    node = game
    for uci in entry["moves"]:
        node = node.add_main_variation(chess.Move.from_uci(uci))
    return str(game).rstrip() + "\n"


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
    default_csv = os.path.join(ap.get_default("repo"), "data", "downloads", "lichess_db_puzzle.csv.zst")
    ap.add_argument("--csv", default=default_csv if os.path.exists(default_csv) else
                    os.path.join(ap.get_default("repo"), "data", "downloads", "lichess_db_puzzle.csv"))
    ap.add_argument("--per-level", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=20261121)
    ap.add_argument("--scan-cap", type=int, default=12000,
                    help="max candidates kept per level while scanning the export")
    args = ap.parse_args()

    if not os.path.exists(args.csv):
        sys.exit(f"input not found: {args.csv}\nrun: bash scripts/fetch-puzzles.sh")

    generated = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    generated_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"scanning {args.csv} ...")
    buckets = scan_candidates(args.csv, args.scan_cap)
    for lv in LEVELS:
        print(f"  {lv}: {len(buckets[lv])} candidates")

    rng = random.Random(args.seed)
    data_dir = os.path.join(args.repo, "data")
    puzzles_dir = os.path.join(data_dir, "puzzles")
    pgn_dir = os.path.join(data_dir, "pgn", "puzzles")
    # clean previous build output (README.md is regenerated below)
    shutil.rmtree(puzzles_dir, ignore_errors=True)
    shutil.rmtree(pgn_dir, ignore_errors=True)
    os.makedirs(puzzles_dir, exist_ok=True)

    index_levels = {}
    manifest = {"generated": generated_iso, "seed": args.seed, "perLevel": args.per_level,
                "source": "https://database.lichess.org/lichess_db_puzzle.csv.zst",
                "license": "CC0 1.0 — licenses/lichess-database-cc0.md",
                "bands": {lv: LEVEL_BAND_TEXT[lv] for lv in LEVELS}, "levels": {}, "sha256": {}}
    total = 0
    for lv in LEVELS:
        cands = buckets[lv]
        if len(cands) < args.per_level:
            sys.exit(f"not enough candidates for {lv}: {len(cands)} < {args.per_level}")
        picked = rng.sample(cands, args.per_level)
        picked.sort(key=lambda c: c["id"])
        entries = {}
        os.makedirs(os.path.join(pgn_dir, lv), exist_ok=True)
        skipped = 0
        for cand in picked:
            entry = validate_and_enrich(cand)
            if entry is None:
                skipped += 1
                continue
            pid = cand["id"]
            entry["level"] = lv
            entry["pgn"] = f"data/pgn/puzzles/{lv}/{pid}.pgn"
            entries[pid] = entry
            with open(os.path.join(pgn_dir, lv, f"{pid}.pgn"), "w", encoding="utf-8") as fh:
                fh.write(puzzle_pgn(pid, lv, entry, generated))
        ids = sorted(entries.keys())
        if len(ids) < args.per_level // 2:
            sys.exit(f"too many invalid puzzles in {lv}: kept {len(ids)} of {args.per_level}")
        level_file = f"{lv}.json"
        with open(os.path.join(puzzles_dir, level_file), "w", encoding="utf-8") as fh:
            json.dump({"level": lv, "label": LEVEL_LABEL[lv], "puzzles": entries}, fh,
                      ensure_ascii=False, separators=(",", ":"))
        index_levels[lv] = {"count": len(ids), "file": level_file, "ids": ids}
        manifest["levels"][lv] = {"count": len(ids), "pgnFiles": len(ids), "skippedInvalid": skipped}
        total += len(ids)
        print(f"  {lv}: wrote {len(ids)} puzzles ({skipped} invalid skipped)")

    index = {
        "format": 1,
        "name": "SchachKenner daily puzzles",
        "source": "https://database.lichess.org/lichess_db_puzzle.csv.zst",
        "sourceNote": "lichess puzzle database export — CC0 1.0, proof in licenses/lichess-database-cc0.md",
        "generated": generated_iso,
        "seed": args.seed,
        "count": total,
        "bands": {lv: {"rating": LEVEL_BAND_TEXT[lv], "label": LEVEL_LABEL[lv]} for lv in LEVELS},
        "levels": index_levels,
        "selection": {
            "rule": "ids[(utcDayIndex + levelOffset) % ids.length]",
            "utcDayIndex": "floor(Date.now() / 86400000)  // UTC day number",
            "levelOffset": LEVEL_OFFSET,
            "note": "identical rule in docs/puzzles.html (client) and bot/src/puzzles.js (bot) — keep in sync",
        },
    }
    with open(os.path.join(puzzles_dir, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
    manifest["count"] = total
    for f in ["index.json", "easy.json", "medium.json", "hard.json"]:
        manifest["sha256"][f] = sha256_file(os.path.join(puzzles_dir, f))
    with open(os.path.join(puzzles_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)

    readme = os.path.join(pgn_dir, "README.md")
    with open(readme, "w", encoding="utf-8") as fh:
        fh.write(f"""# SchachKenner daily puzzles — hosted PGNs

{total} chess puzzles ({index_levels['easy']['count']} easy / {index_levels['medium']['count']} medium /
{index_levels['hard']['count']} hard by lichess puzzle rating), one PGN per puzzle in
`<level>/<PuzzleId>.pgn`. Each PGN carries `SetUp`/`FEN` (the position to solve, side to move
is the solver) plus the full solution line as movetext and as `Solution`/`SolutionSAN` headers.

- **Source:** lichess puzzle database export <https://database.lichess.org/lichess_db_puzzle.csv.zst>
  (6M+ rated, tagged puzzles) — **CC0 1.0**, proof: [licenses/lichess-database-cc0.md](../../licenses/lichess-database-cc0.md)
- **Selection:** deterministic sample (seed {args.seed}, {args.per_level} per band) built by
  `scripts/build-puzzles.py`; validate with `scripts/validate-puzzles.py`.
- **Daily rotation:** `docs/puzzles.html` picks, per UTC day (`floor(Date.now()/86400000)`),
  one puzzle per level: `ids[(dayIndex + levelOffset) % ids.length]` — see `data/puzzles/index.json`.
- **Machine-readable index:** [data/puzzles/index.json](../puzzles/index.json) + per-level
  [easy.json](../puzzles/easy.json) / [medium.json](../puzzles/medium.json) / [hard.json](../puzzles/hard.json)
  (fen, moves, san, rating, themes, gameUrl per puzzle).

Generated {generated_iso} UTC. Repo content: CC0.
""")
    print(f"total: {total} puzzles -> data/pgn/puzzles/, data/puzzles/")


if __name__ == "__main__":
    main()
