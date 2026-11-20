#!/usr/bin/env python3
"""Scan all hosted PGN files and classify every game:
standard | chess960 | atomic | crazyhouse | horde | koth | racingkings | broken
A game is 'broken' only if NO board type can replay its movetext (parser-level problem).
Usage: python scripts/scan-pgn-support.py
"""
import os, re, sys, io
import chess, chess.pgn
import chess.variant

ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "pgn")

VARIANTS = [
    ("chess960", lambda fen: chess.Board(fen, chess960=True) if fen else chess.Board(chess960=True)),
    ("atomic", lambda fen: chess.variant.AtomicBoard(fen) if fen else chess.variant.AtomicBoard()),
    ("crazyhouse", lambda fen: chess.variant.CrazyhouseBoard(fen) if fen else chess.variant.CrazyhouseBoard()),
    ("horde", lambda fen: chess.variant.HordeBoard(fen) if fen else chess.variant.HordeBoard()),
    ("koth", lambda fen: chess.variant.KingOfTheHillBoard(fen) if fen else chess.variant.KingOfTheHillBoard()),
    ("racingkings", lambda fen: chess.variant.RacingKingsBoard(fen) if fen else chess.variant.RacingKingsBoard()),
]

def split_games(text):
    chunks = re.split(r"\r?\n\r?\n", text)
    games, i = [], 0
    while i < len(chunks):
        c = chunks[i]
        if c.strip().startswith("["):
            mv = chunks[i + 1] if i + 1 < len(chunks) else ""
            games.append((c, mv))
            i += 2
        else:
            i += 1
    return games

def tags_of(hdr):
    return dict(re.findall(r'\[(\w+)\s+"([^"]*)"\]', hdr))

def san_list(movetext):
    t = movetext
    # brace comments FIRST (lichess comments like { [%clk 0:05:00] } contain '%'!)
    t = re.sub(r"\{[^}]*\}", " ", t, flags=re.S)
    t = re.sub(r";[^\n]*", " ", t)
    prev = None
    while prev != t:                                   # nested variations
        prev = t
        t = re.sub(r"\([^()]*\)", " ", t)
    t = re.sub(r"%[^\n]*", " ", t)                      # PGN escape comments
    toks = []
    for tok in t.split():
        tok = re.sub(r"^\d+\.+", "", tok)              # glued move numbers: 1.d4 -> d4
        if not tok or re.fullmatch(r"\d+\.+(?![0-9a-zA-Z])", tok):
            continue
        if tok in ("1-0", "0-1", "1/2-1/2", "*"):
            continue
        if re.fullmatch(r"\$\d+", tok):
            continue
        if re.fullmatch(r"[-\u2010-\u2015]+|Z0|null", tok, re.I):
            continue
        tok = re.sub(r"[!?]+$", "", tok)
        if tok:
            toks.append(tok)
    return toks

def classify(hdr, movetext):
    tags = tags_of(hdr)
    fen = tags.get("FEN") if tags.get("SetUp") == "1" else None
    sans = san_list(movetext)
    # 1) standard
    try:
        b = chess.Board(fen) if fen else chess.Board()
        for s in sans:
            b.push_san(s)
        return "standard"
    except Exception:
        pass
    # 2) named variants / chess960
    for name, make in VARIANTS:
        try:
            b = make(fen)
            for s in sans:
                b.push_san(s)
            return name
        except Exception:
            continue
    return "broken"

def main():
    total = {}
    broken_list = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != "groups"]   # top-level dataset files only
        for fn in sorted(filenames):
            if not fn.endswith(".pgn"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT)
            text = open(path, encoding="utf-8", errors="replace").read()
            games = split_games(text)
            counts = {}
            for idx, (hdr, mv) in enumerate(games):
                if not mv.strip():
                    continue
                cat = classify(hdr, mv)
                counts[cat] = counts.get(cat, 0) + 1
                if cat == "broken":
                    broken_list.append((rel, idx + 1, tags_of(hdr).get("White", "?"), tags_of(hdr).get("Black", "?")))
            print(f"{rel}: {len(games)} games -> {counts}")
            for k, v in counts.items():
                total[k] = total.get(k, 0) + v
    print("\n=== TOTAL:", total)
    if broken_list:
        print("\n=== BROKEN games (no board type could replay):")
        for b in broken_list[:50]:
            print(" ", b)
    else:
        print("\nNo broken games — every hosted game is replayable by standard chess or a known variant.")

if __name__ == "__main__":
    main()
