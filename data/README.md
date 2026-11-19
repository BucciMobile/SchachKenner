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
data/pgn/lichess/
├── README.md
├── lichess-standard-2026-10-sample-2000-games.pgn   # CC0 — 2,000 games from the official 2026-10 export
└── lichess-puzzles-sample-1000.csv                  # CC0 — 1,000 puzzles from the official puzzle export
```

Permission evidence: [`licenses/lichess-database-cc0.md`](../licenses/lichess-database-cc0.md)

## What goes where

```
data/
├── README.md            ← this policy
├── pgn/<source>/        ← hosted PGN/CSV samples (explicit permission only, see licenses/)
└── downloads/           ← git-ignored; filled locally by scripts/fetch-pgn.sh, never committed
```
