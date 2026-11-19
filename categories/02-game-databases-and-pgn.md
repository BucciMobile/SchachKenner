# 2 · Game databases & PGN downloads

[Back to README](../README.md)

## 🔎 Can you find PGN files on the internet?

**Yes — PGN (Portable Game Notation) is the standard plain-text format** for chess games
and is freely downloadable from many sites. Common formats you will encounter:

| Format | Extension | Notes |
|---|---|---|
| PGN | `.pgn` | Standard text format (tags + moves). Convert/clean with [pgn-extract](../categories/07-tools-libraries-scripts.md) |
| EPD | `.epd` | Positions only (FEN + ops), used for test suites |
| SCID database | `.si4` / `.sdf` | Binary DB format of Scid/Scid vs. PC |
| ChessBase | `.cbh` | Commercial (ChessBase) — **do not redistribute** |

> ⚠️ **Only CC0-licensed files are hosted in this repo** (see below). Everything else is
> linked, never mirrored — EU database right may protect curated collections, and several
> sites explicitly forbid redistribution (see
> [`licenses/link-only-sources.md`](../licenses/link-only-sources.md)).
> Fetch originals locally with [`scripts/fetch-pgn.sh`](../scripts/fetch-pgn.sh).

## ⬇ Hosted in this repo (explicit permission — CC0)

| File | License | Contents |
|---|---|---|
| [`data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn`](../data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn) | CC0 1.0 | 2,000-game PGN sample from the official lichess 2026-10 export |
| [`data/pgn/lichess/lichess-puzzles-sample-1000.csv`](../data/pgn/lichess/lichess-puzzles-sample-1000.csv) | CC0 1.0 | 1,000-puzzle CSV sample from the official lichess puzzle export |
| [`data/pgn/lichess/groups/`](../data/pgn/lichess/groups/README.md) | CC0 1.0 | the 2,000 games **pre-sorted into 51 groups**: by opening (top 15), by ECO code (top 20), by rating band, by time control, by result — index with counts in [`groups/README.md`](../data/pgn/lichess/groups/README.md) |

🔍 **Interactive explorer:** filter/search/sort these games live in the browser (time control, Elo slider, opening, ECO A–E, event, result, player search, copyable PGNs, own-file upload) at **https://BucciMobile.github.io/SchachKenner/** — source in [`docs/index.html`](../docs/index.html). |

Permission evidence: [`licenses/lichess-database-cc0.md`](../licenses/lichess-database-cc0.md).
Full dumps (GBs) are **not** hosted — get them from https://database.lichess.org/ or via
[`scripts/fetch-pgn.sh`](../scripts/fetch-pgn.sh).

## 🗄 Subcategory A — Massive structured databases (full dumps)

| Resource | Size / content | License / access | Link |
|---|---|---|---|
| lichess open database | Billions of games; monthly dumps (standard + variants), elite subset (≥2400), puzzles, evals | **CC0** — redistribution explicitly allowed; sample hosted above | https://database.lichess.org/ |
| lichess elite database | Subset, both players ≥ 2400 Elo | CC0 | https://database.lichess.org/#elite |
| Lumbras Gigabase | ~9.6M games, SCID + PGN | CC BY-NC 4.0 (credit, non-commercial) — evidence in `licenses/`; click-gated download | https://lumbrasgigabase.com/en/ |
| FICS games archive | All games ever played on the Free Internet Chess Server | Free download, no explicit license → link only | https://www.ficsgames.org/ |
| Caïssabase (legacy) | Formerly free ~5M curated SCID games (site discontinued 2025) | Historical | https://chessprogramming.org/Caissabase |

## 📰 Subcategory B — Weekly news & curated/themed collections (PGN)

| Resource | What you get | Access | Link |
|---|---|---|---|
| The Week in Chess (TWIC) | Weekly PGN of current master games + full archive since 1994 | Free download — **link only** (no redistribution grant) | https://www.theweekinchess.com/twic |
| ChessEssentials PGN downloads | Curated PGN collections (players, events, themes) | Free download — **link only** | https://chessessentials.com/chess-pgn-downloads/ |
| PGN Mentor | 1M+ GM games sorted by player/opening/event | Free — **link only** (© 64 Squares) | https://www.pgnmentor.com/ |
| BeginChess PGN downloads | PGNs extracted from classic (public-domain) books | Free — **link only** | https://www.beginchess.com/ |

## 🌐 Subcategory C — Web databases (search & play online — link only)

| Resource | What you get | Link |
|---|---|---|
| 365Chess | Large online game DB + opening explorer + trainer | https://www.365chess.com/ |
| chessgames.com | Largest online collection incl. historical masters; bulk download needs paid membership | https://www.chessgames.com/ |

## ⚖️ Legal notes — are chess games copyrighted?

- Chess Stack Exchange — *Who owns the copyright to the results of chess games?* (EU database right): https://chess.stackexchange.com/questions/47956/
- Chess Stack Exchange — *Chess games ownership…* (raw moves = facts; annotations can be protected): https://chess.stackexchange.com/questions/16437/
- Law Stack Exchange — *Are chess games copyrighted?* (Germany vs. US): https://law.stackexchange.com/questions/60030/
- Our own audit with raw evidence: [`licenses/`](../licenses/)
