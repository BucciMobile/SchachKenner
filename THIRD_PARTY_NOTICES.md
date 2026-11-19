# Third-Party Notices

This repo is **link-first**: almost everything is linked to its original source and is
not hosted here. The table below lists every third-party asset that IS hosted inside
`data/`. The **proof of permission** for each hosted asset (verbatim license quote, source
URL, retrieval date, SHA-256 of the raw license page) lives in [`licenses/`](licenses/).

## Hosted assets

| File | Source | License | Permission evidence |
|---|---|---|---|
| `data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn` (2,000 games, 4.8 MB, SHA-256 `8d1d92363f31b7b573edc2c84fd9bff007e49c9010bb4409e58ef29010061afd`) | https://database.lichess.org/standard/lichess_db_standard_rated_2026-10.pgn.zst | **CC0 1.0** — "You can download, modify and redistribute them, without asking for permission." | [licenses/lichess-database-cc0.md](licenses/lichess-database-cc0.md) |
| `data/pgn/lichess/lichess-puzzles-sample-1000.csv` (1,000 puzzles, 190 KB, SHA-256 `5f5486c5b06c20bf48a680ddd1ce853985f6b52ddf81a8b08699bce40a86a07e`) | https://database.lichess.org/lichess_db_puzzle.csv.zst | **CC0 1.0** (same grant) | [licenses/lichess-database-cc0.md](licenses/lichess-database-cc0.md) |
| `assets/img/pieces/livius/*.svg` (12 piece SVGs) | https://github.com/kmar/chess_svg_piece_sets (set `livius`, Martin Sedlák) | **Unlicense / public domain** — freely copyable, even commercially | [licenses/chess-pieces-cc0.md](licenses/chess-pieces-cc0.md) |
| `assets/img/banner.svg`, `assets/img/divider.svg` | our own composition from the public-domain pieces above | **CC0** (own work) | [licenses/chess-pieces-cc0.md](licenses/chess-pieces-cc0.md) |

Both samples were taken from the first entries of the official export files on
2026-11-19 (UTC). Full dumps stay at the source (see `scripts/fetch-pgn.sh`).

## Licensed but linked (not hosted)

| Source | License | Why linked, not hosted | Evidence |
|---|---|---|---|
| Lumbras Gigabase | CC BY-NC 4.0 (share with credit, non-commercial) | Bulk files are click-gated on their site; we link for download | [licenses/lumbras-gigabase-cc-by-nc.md](licenses/lumbras-gigabase-cc-by-nc.md) |

## Link-only sources (no explicit redistribution permission)

chess.com, chessgames.com, TWIC, PGN Mentor, ChessEssentials, FICS/ficsgames.org,
365chess.com — see [licenses/link-only-sources.md](licenses/link-only-sources.md).

## License reminders for common chess assets

| Asset | Typical license | Attribution required? |
|---|---|---|
| Raw chess games / PGN move lists | Facts — not copyrightable in the US; EU database right may protect *curated collections* | Link the source collection |
| lichess game & puzzle exports | **CC0 1.0** (broadcasts: CC BY-SA 4.0) | No (CC0), but credit is appreciated |
| Cburnett SVG piece set (Wikimedia Commons) | CC BY-SA 3.0 / GFDL | **Yes** — name "Cburnett" + link |
| Chess Programming Wiki content | CC BY-SA 4.0 | **Yes** |
| Engines (Stockfish, lc0, …) | GPL-3.0 | License obligations for code distribution |
| Project Gutenberg / archive.org books | Public domain (per item) | Check each item |
