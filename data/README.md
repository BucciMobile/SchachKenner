# `data/` — hosting policy

This folder is the **only** place where third-party files may be hosted in this repo.
Everything else in the repo is links to the original sources.

## Rules

1. A file may be added here **only** if the source *explicitly* permits redistribution
   (e.g. CC0, public domain, CC BY/CC BY-NC with attribution, permissive code licenses).
2. Every hosted file **must** have:
   - an entry in [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) (file, source
     URL, license, hashes), and
   - a **permission evidence** file in [`../licenses/`](../licenses/) with the verbatim
     license quote, retrieval date (UTC), and the raw license page (SHA-256) in
     `licenses/raw/`.
3. Never add: copyrighted books/PDFs, annotated games from commercial databases, bulk
   dumps from chess.com / chessgames.com, paid puzzle sets, unlicensed images, or
   collections whose site grants no redistribution right (TWIC, PGN Mentor,
   ChessEssentials, FICS, 365chess — see `licenses/link-only-sources.md`).
4. Prefer **small, useful samples** over giant dumps; big datasets stay at their source
   (e.g. lichess monthly dumps — fetch them with `scripts/fetch-pgn.sh`).

## Currently hosted (with explicit permission)

```
data/pgn/
├── lichess/                  # CC0 — 2,000 standard rated games (2026-10) + 1,000-puzzle CSV + groups/
├── lichess-chess960/         # CC0 — 1,000 Chess960 rated games (2026-10) + groups/
├── lichess-atomic/           # CC0 — 1,000 Atomic rated games (2026-10) + groups/
├── lichess-standard-2019/    # CC0 — 1,000 standard games (2019-12, older era) + groups/
├── lichess-broadcast/        # CC BY-SA 4.0 (attributed) — 300 broadcast games (2026-10) + groups/
├── classic-games/            # CC0 — Tal: Life and Games + My Memorable 60 + groups/
├── tcec/                     # CC BY-SA 3.0 (attributed) — 200 engine games, TCEC S29 Div P + groups/
└── masters/                  # MIT — Fischer + Euwe master games + groups/
```

Each dataset folder has a `README.md` (source, SHA-256, license) and `groups/`
(pre-sorted files + index, regenerate with `python scripts/split-pgn.py`).
Interactive explorer for all datasets: https://buccimobile.github.io/SchachKenner/

Permission evidence: [`licenses/`](../licenses/) — `lichess-database-cc0.md`,
`lichess-variants-and-broadcasts.md`, `classic-games-cc0.md`

## What goes where

```
data/
├── README.md            ← this policy
├── pgn/<source>/        ← hosted PGN/CSV samples (explicit permission only, see licenses/)
└── downloads/           ← git-ignored; filled locally by scripts/fetch-pgn.sh, never committed
```
