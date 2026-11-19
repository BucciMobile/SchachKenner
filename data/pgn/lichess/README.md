# lichess samples — CC0 1.0 (hosted with explicit permission)

Both files are unmodified prefixes of the **official lichess database exports**, which
are dedicated to the public domain:

> "Database exports are released under the Creative Commons CC0 license. Use them for
> research, commercial purpose, publication, anything you like. You can download, modify
> and redistribute them, without asking for permission." — https://database.lichess.org/
> (retrieved 2026-11-19 UTC; evidence: [`licenses/lichess-database-cc0.md`](../../../licenses/lichess-database-cc0.md))

| File | Source export | Contents | SHA-256 |
|---|---|---|---|
| `lichess-standard-2026-10-sample-2000-games.pgn` | `standard/lichess_db_standard_rated_2026-10.pgn.zst` | first 2,000 rated standard games of October 2026, PGN with clock comments | `8d1d92363f31b7b573edc2c84fd9bff007e49c9010bb4409e58ef29010061afd` |
| `lichess-puzzles-sample-1000.csv` | `lichess_db_puzzle.csv.zst` | header + first 1,000 rated puzzles (FEN, solution moves, rating, themes) | `5f5486c5b06c20bf48a680ddd1ce853985f6b52ddf81a8b08699bce40a86a07e` |

Full monthly dumps (several GB, `.zst`) are **not** hosted here — download them from
https://database.lichess.org/ or via `scripts/fetch-pgn.sh` (lands in git-ignored
`data/downloads/`). Broadcast games are CC BY-SA 4.0, not CC0, and are not hosted.

## 📂 Grouped samples — [`groups/`](groups/README.md)

The 2,000-game sample is additionally split into **sensible groups** (each game appears
once per criterion, still CC0 — derived works are covered by the same grant):

| Criterion | Groups | Examples |
|---|---|---|
| `by-opening/` | top 15 openings + other | Caro-Kann, French, Sicilian, London System… |
| `by-eco/` | top 20 ECO codes + other | C00, C41, D02… |
| `by-rating-band/` | 7 bands | under-1400 … 2200-plus |
| `by-time-control/` | 4 classes | bullet, blitz, rapid, classical |
| `by-result/` | 3 classes | white wins, black wins, draws |

Index with per-group game counts and links: [`groups/README.md`](groups/README.md).
Regenerate with `python scripts/split-pgn.py` from the repo root.
