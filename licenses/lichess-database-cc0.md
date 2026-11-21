# lichess database exports — CC0 (redistribution explicitly allowed) ✅ HOSTED

- **Source page:** https://database.lichess.org/ (retrieved 2026-11-19 UTC)
- **Raw evidence:** [raw/database.lichess.org.2026-11-19.html](raw/database.lichess.org.2026-11-19.html)
  SHA-256: `0e2083b7f71b0b446794d5b8c5c38e4a2e9711c845258edfb8b8d67c66b3fe04`
- **License:** Creative Commons **CC0 1.0 Universal** (public domain dedication)
  — official text: https://creativecommons.org/publicdomain/zero/1.0/legalcode
  (the page links the summary at https://tldrlegal.com/license/creative-commons-cc0-1.0-universal)
- **Also relevant:** lichess Terms of Service (https://lichess.org/terms-of-service, raw copy
  in `raw/`) — users grant lichess a broad license for content they submit; the *database
  exports* are additionally dedicated to CC0 as quoted below.
- Note: the export **tooling** repo `lichess-org/database` is AGPL-3.0 — that license covers
  the code, not the exported data.

## Verbatim quote from the source page

> "Database exports are released under the Creative Commons CC0 license. Use them for
> research, commercial purpose, publication, anything you like. You can download, modify
> and redistribute them, without asking for permission."

> "Broadcast games are released under the Creative Commons Attribution-ShareAlike 4.0
> license." (https://creativecommons.org/licenses/by-sa/4.0/) — broadcasts are therefore
> **not** part of the CC0 grant and are not hosted here.

## What we host because of this grant

| File in `data/pgn/lichess/` | Derived from | Contents | SHA-256 |
|---|---|---|---|
| `lichess-standard-2026-10-sample-2000-games.pgn` | https://database.lichess.org/standard/lichess_db_standard_rated_2026-10.pgn.zst | first 2,000 games of the 2026-10 standard rated export (4.8 MB) | `8d1d92363f31b7b573edc2c84fd9bff007e49c9010bb4409e58ef29010061afd` |
| `lichess-puzzles-sample-1000.csv` | https://database.lichess.org/lichess_db_puzzle.csv.zst | header + first 1,000 rows of the puzzle export (190 KB) | `5f5486c5b06c20bf48a680ddd1ce853985f6b52ddf81a8b08699bce40a86a07e` |
| `data/puzzles/index.json` | https://database.lichess.org/lichess_db_puzzle.csv.zst (2026-11 dump) | daily-puzzle index: 2,400 puzzles (800 each easy <1200 / medium 1200–1700 / hard >1700), deterministic sample seed 20261121 via `scripts/build-puzzles.py` | `18ba451ffbd974f2933fbb6ff1980f5ecab2b6db8ac014d2289a3e9fa8cb221b` |
| `data/puzzles/easy.json` / `medium.json` / `hard.json` | same | full entries per level (FEN, solution moves/SAN, rating, themes, gameUrl) | `4ef4d8543dea6a67c2ee3edc5a8c960c64ca86d77f2e1061b24e51869844ce8d` / `54e8172bd138fa73f592c59fcdd6557c3d8de25ca354b83077809537f9653414` / `01f1fb8e49567908d15ce7b3b6f1254f9c12ddd65a7a00a7fed37d1082fcee36` |
| `data/pgn/puzzles/<level>/<PuzzleId>.pgn` (2,400 files, 9.5 MB) | same | one PGN per puzzle (SetUp/FEN + solution line + Solution/SolutionSAN headers) | per-file hashes reproducible via `scripts/validate-puzzles.py`; dataset manifest in `data/puzzles/manifest.json` |

Full monthly dumps (GBs) remain at the source — see `scripts/fetch-pgn.sh` and
`scripts/fetch-puzzles.sh`. Samples are taken from the first games/rows of the official
export files on 2026-11-19 UTC; the puzzle dataset was built from the 2026-11-01 puzzle
export (retrieved 2026-11-21 UTC).
