#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build data/openings/openings.json (+ docs/openings.json copy for GitHub Pages)
from the repo's OWN licensed standard-game datasets (CC0 / MIT / Unlicense only).

For each curated opening (scripts/opening-notes.py OPENINGS) we take the games whose
Opening/ECO tag matches, compute the majority mainline (most frequent SAN path,
max 12 plies), replay it with python-chess to get UCI moves, and attach our own
CC0 explanation notes (intro + variants/traps + per-move note).

Usage: python scripts/build-openings.py
"""
import os, re, json, hashlib, collections, sys
import chess

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("opening_notes", os.path.join(HERE, "opening-notes.py"))
opening_notes = _ilu.module_from_spec(_spec); _spec.loader.exec_module(opening_notes)
OPENINGS, INTROS, MOVE_NOTES = opening_notes.OPENINGS, opening_notes.INTROS, opening_notes.MOVE_NOTES

# datasets we derive from (all CC0 / MIT / Unlicense — NOT the CC BY-SA ones)
SRC_DIRS = ["lichess", "lichess-standard-2019", "classic-games", "masters", "historic-masters"]
VARIANT = re.compile(r"Variant")

def split_games(text):
    chunks = re.split(r"\r?\n\r?\n", text)
    games, i = [], 0
    while i < len(chunks):
        c = chunks[i]
        if c.strip().startswith("["):
            mv = chunks[i+1] if i+1 < len(chunks) else ""
            games.append((c, mv)); i += 2
        else:
            i += 1
    return games

def tags_of(hdr):
    return dict(re.findall(r'\[(\w+)\s+"([^"]*)"\]', hdr))

def san_list(movetext):
    t = re.sub(r"\{[^}]*\}", " ", movetext, flags=re.S)
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

def eco_num(eco):
    m = re.match(r"([A-E])(\d\d)", eco or "")
    return (m.group(1), int(m.group(2))) if m else None

# authoritative ECO family ranges (letter, lo, hi)
ECO_RANGES = {
 "italian": ("C", 50, 54), "ruylopez": ("C", 60, 99), "scotch": ("C", 44, 45), "evans": ("C", 51, 52),
 "kingsgambit": ("C", 30, 39), "vienna": ("C", 25, 29), "philidor": ("C", 41, 41), "petrov": ("C", 42, 43),
 "fourknights": ("C", 46, 49), "twoknights": ("C", 55, 59), "french": ("C", 0, 19), "sicilian": ("B", 20, 99),
 "carokann": ("B", 10, 19), "scandinavian": ("B", 1, 1), "alekhine": ("B", 2, 5), "pirc": ("B", 7, 9),
 "qga": ("D", 20, 29), "slav": ("D", 10, 19), "semislav": ("D", 43, 49),
 "qgd": ("D", 30, 69),   # Semi-Slav D43–D49 is checked first (ordered list), see below
 "grunfeld": ("D", 70, 99), "london": ("D", 0, 6),
 "kid": ("E", 60, 99), "nimzo": ("E", 20, 42), "qid": ("E", 0, 19), "english": ("A", 10, 39),
}
# order matters: semislav before qgd so D43–D49 lands in Semi-Slav
ORDER = ["semislav", "qgd", "qga", "slav", "grunfeld", "london", "nimzo", "qid", "kid"] + \
        [o[0] for o in OPENINGS if o[0] not in ("semislav", "qgd", "qga", "slav", "grunfeld", "london", "nimzo", "qid", "kid")]

def matches(key, name, eco):
    n = (name or "").lower()
    en = eco_num(eco)
    rng = ECO_RANGES.get(key)
    if en and rng and rng[0] == en[0] and rng[1] <= en[1] <= rng[2]:
        if key == "qgd" and 43 <= en[1] <= 49:
            return False  # that's Semi-Slav
        if key == "italian" and 51 <= en[1] <= 52:
            return False  # C51/C52 = Evans Gambit
        if key == "nimzo" and not (20 <= en[1] <= 42):
            return False
        return True
    kws = next((o[4] or [] for o in OPENINGS if o[0] == key), [])
    if key == "slav":
        return any(k in n for k in kws) and "semi" not in n
    return bool(kws) and any(k in n for k in kws)

def majority_line(sans_list, max_plies=12, min_support=5):
    line, prefix = [], ()
    while len(line) < max_plies:
        nxt = collections.Counter()
        for sans in sans_list:
            if len(sans) > len(line) and tuple(sans[:len(line)]) == prefix:
                nxt[sans[len(line)]] += 1
        if not nxt:
            break
        best, cnt = nxt.most_common(1)[0]
        if cnt < min_support and len(line) >= 6:
            break
        line.append(best)
        prefix = tuple(line)
    return line

def fallback_note(san, board):
    piece = None
    # find which piece moved: parse via board before push — caller passes board BEFORE the move
    return None

def note_for(san, board_before):
    if san in MOVE_NOTES:
        return MOVE_NOTES[san]
    # generic fallback from the moving piece
    # san like Nf3, Bb5, O-O, exd4, Qh4+, Bxf3
    m = re.match(r"^(O-O-O|O-O|([KQRBN])?([a-h])?([1-8])?x?([a-h][1-8]))([+#]?)$", san)
    if not m:
        return "A standard developing move in this opening."
    if m.group(1) == "O-O":
        return "Castles kingside: king to safety, rook to the center — the standard development move."
    if m.group(1) == "O-O-O":
        return "Castles queenside: king to safety, rook onto the d-file."
    dest = m.group(5)
    piece = m.group(3) or ("P" if not m.group(3) else None)
    if piece is None:
        # pawn move: look at board
        frm_file = m.group(4)
        # find pawn on that file that can move to dest
        piece = "P"
    names = {"N": "knight", "B": "bishop", "R": "rook", "Q": "queen", "K": "king", "P": "pawn"}
    p = names.get(piece, "piece")
    if "x" in san:
        return f"Captures on {dest}: wins material/space and opens lines around {dest}."
    if piece == "pawn":
        return f"Advances a pawn to {dest}, staking a claim on the center and opening lines."
    if piece == "knight":
        return f"Develops the knight to {dest}, eyeing the center and key outposts."
    if piece == "bishop":
        return f"Develops the bishop to {dest}, aiming along an open diagonal."
    if piece == "rook":
        return f"Activates the rook to {dest}, often toward an open file."
    if piece == "queen":
        return f"Brings the queen to {dest} — active, but keep it out of early pawn attacks."
    return f"Moves the {p} to {dest}."

def main():
    games_by_key = collections.defaultdict(list)
    src_files = []
    for d in SRC_DIRS:
        dp = os.path.join(ROOT, "data", "pgn", d)
        if not os.path.isdir(dp):
            continue
        for fn in sorted(os.listdir(dp)):
            if not fn.endswith(".pgn"):
                continue
            path = os.path.join(dp, fn)
            src_files.append(os.path.relpath(path, ROOT))
            text = open(path, encoding="utf-8", errors="replace").read()
            for hdr, mv in split_games(text):
                tags = tags_of(hdr)
                if tags.get("Variant", "Standard") != "Standard" or tags.get("SetUp") == "1" or not mv.strip():
                    continue
                name, eco = tags.get("Opening", ""), tags.get("ECO", "")
                for key in ORDER:
                    if matches(key, name, eco):
                        games_by_key[key].append(san_list(mv))
                        break

    out = []
    for key, name, eco_disp, wiki, _kws in OPENINGS:
        sans_list = games_by_key.get(key, [])
        if not sans_list:
            print("SKIP (no games):", key)
            continue
        line = majority_line(sans_list)
        # replay to get UCI + per-move notes
        board = chess.Board()
        moves = []
        for san in line:
            b_before = board.copy()
            mv = board.parse_san(san)
            san_norm = board.san(mv)
            board.push(mv)
            moves.append({"san": san_norm, "uci": mv.uci(), "note": note_for(san_norm, b_before)})
        intro, traps = INTROS.get(key, ("", ""))
        # dominant ECO in this family
        eco_cnt = collections.Counter()
        # recompute quickly from matched games is complex; just take from names pass — skip, use eco_disp
        out.append({
            "key": key, "name": name, "eco": eco_disp,
            "wiki": f"https://en.wikipedia.org/wiki/{wiki}",
            "games": len(sans_list),
            "intro": intro, "traps": traps,
            "line": moves,
        })
        print(f"{key:14s} {name[:38]:38s} games={len(sans_list):5d}  line={' '.join(m['san'] for m in moves)}")

    payload = {
        "generator": "scripts/build-openings.py (SchachKenner) — derived from this repo's own CC0/MIT/Unlicense PGN datasets; explanations are original text (CC0)",
        "license": "CC0-1.0 (repo content) — move lines derived from CC0/MIT/Unlicense sources, see licenses/openings-dataset.md",
        "sources": src_files,
        "openings": out,
    }
    js = json.dumps(payload, ensure_ascii=False, indent=1)
    for p in [os.path.join(ROOT, "data", "openings", "openings.json"),
              os.path.join(ROOT, "docs", "openings.json")]:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8", newline="").write(js)
    h = hashlib.sha256(js.encode("utf-8")).hexdigest()
    print("\nopenings.json:", len(out), "openings,", len(js)//1024, "KB, sha256", h)
    json.dump({"sha256": h, "openings": len(out)}, open(os.path.join(HERE, "openings-build.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
