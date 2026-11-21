#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze hosted standard PGN datasets: top ECO codes by frequency + majority mainline per ECO."""
import os, re, sys, json, collections
import chess

ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "pgn")
VARIANT_DIRS = {"lichess-atomic", "lichess-crazyhouse", "lichess-horde", "lichess-koth", "lichess-chess960"}

def split_games(text):
    chunks = re.split(r"\r?\n\r?\n", text)
    games, i = [], 0
    while i < len(chunks):
        c = chunks[i]
        if c.strip().startswith("["):
            mv = chunks[i + 1] if i + 1 < len(chunks) else ""
            games.append((c, mv)); i += 2
        else:
            i += 1
    return games

def tags_of(hdr):
    return dict(re.findall(r'\[(\w+)\s+"([^"]*)"\]', hdr))

def san_list(movetext):
    t = movetext
    t = re.sub(r"\{[^}]*\}", " ", t, flags=re.S)
    t = re.sub(r";[^\n]*", " ", t)
    prev = None
    while prev != t:
        prev = t; t = re.sub(r"\([^()]*\)", " ", t)
    t = re.sub(r"%[^\n]*", " ", t)
    out = []
    for tok in t.split():
        s = re.sub(r"^\d+\.+", "", tok)
        if not s or s in ("1-0", "0-1", "1/2-1/2", "*") or re.fullmatch(r"\$\d+", s): continue
        out.append(re.sub(r"[!?]+$", "", s))
    return out

# 1) count ECO over all standard top-level files
eco_count = collections.Counter()
eco_names = collections.defaultdict(collections.Counter)
games_by_eco = collections.defaultdict(list)
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != "groups"]
    ds = os.path.basename(dirpath)
    if ds in VARIANT_DIRS:
        dirnames[:] = []
        continue
    for fn in filenames:
        if not fn.endswith(".pgn"): continue
        text = open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace").read()
        for hdr, mv in split_games(text):
            tags = tags_of(hdr)
            if tags.get("Variant", "Standard") != "Standard": continue
            if tags.get("SetUp") == "1": continue
            eco = tags.get("ECO", "")
            if not eco or not mv.strip(): continue
            eco_count[eco] += 1
            eco_names[eco][tags.get("Opening", "?")] += 1
            games_by_eco[eco].append(san_list(mv))

top = eco_count.most_common(30)
print("=== TOP 30 ECO by game count (hosted standard datasets) ===")
for eco, n in top:
    name = eco_names[eco].most_common(1)[0][0]
    print(f"{eco}  {n:6d}  {name[:60]}")

# 2) majority mainline for top 25
def majority_line(sans_list, max_plies=12, min_support=5):
    tree = {}  # tuple(prefix) -> Counter of next san
    counts = collections.Counter()
    for sans in sans_list:
        counts[tuple(sans[:max_plies])] += 1
    # walk greedily: at each node pick most common next move with enough support
    line = []
    prefix = ()
    support = len(sans_list)
    while len(line) < max_plies:
        nxt = collections.Counter()
        for sans in sans_list:
            if len(sans) > len(line) and tuple(sans[:len(line)]) == prefix:
                nxt[sans[len(line)]] += 1
        if not nxt: break
        best, cnt = nxt.most_common(1)[0]
        if cnt < min_support and len(line) >= 6: break
        line.append(best)
        prefix = tuple(line)
    return line

print("\n=== majority mainline (top 25) ===")
result = {}
for eco, n in top[:25]:
    name = eco_names[eco].most_common(1)[0][0]
    line = majority_line(games_by_eco[eco])
    result[eco] = {"name": name, "games": n, "line": line}
    print(f"{eco} {name[:45]:45s} ({n:5d}) {' '.join(line)}")

json.dump(result, open(os.path.join(os.path.dirname(__file__), "openings-analysis.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nwritten scripts/openings-analysis.json")
