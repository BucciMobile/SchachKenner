# ♞ Awesome Open Chess

A curated, **link-first** collection of free and open-source resources for chess lovers:
game databases, PGN downloads, engines, analysis software, puzzles, books, piece sets and datasets.

> **Copyright-safe by design.** We link to the original sources instead of copying their content.
> Files are only hosted inside [`data/`](data/) when their license explicitly allows
> redistribution — every hosted file is recorded in
> [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). See the
> [hosting policy](data/README.md) and the [contributing rules](CONTRIBUTING.md).

[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![link-check](https://github.com/BucciMobile/awesome-open-chess/actions/workflows/link-check.yml/badge.svg)](https://github.com/BucciMobile/awesome-open-chess/actions/workflows/link-check.yml)

---

## Contents

| # | Category | Details |
|---|----------|---------|
| 1 | Play & learn online | [categories/01-play-and-learn-online.md](categories/01-play-and-learn-online.md) |
| 2 | Game databases & PGN downloads | [categories/02-game-databases-and-pgn.md](categories/02-game-databases-and-pgn.md) |
| 3 | Openings & repertoires | [categories/03-openings-and-repertoires.md](categories/03-openings-and-repertoires.md) |
| 4 | Puzzles & tactics | [categories/04-puzzles-and-tactics.md](categories/04-puzzles-and-tactics.md) |
| 5 | Chess engines (open source) | [categories/05-engines.md](categories/05-engines.md) |
| 6 | Analysis software & GUIs | [categories/06-analysis-gui.md](categories/06-analysis-gui.md) |
| 7 | Tools, libraries & scripts | [categories/07-tools-libraries-scripts.md](categories/07-tools-libraries-scripts.md) |
| 8 | Tablebases & opening books | [categories/08-tablebases-and-opening-books.md](categories/08-tablebases-and-opening-books.md) |
| 9 | Books & learning material | [categories/09-books-and-learning.md](categories/09-books-and-learning.md) |
| 10 | Graphics, piece sets & fonts | [categories/10-graphics-pieces-fonts.md](categories/10-graphics-pieces-fonts.md) |
| 11 | Datasets & machine learning | [categories/11-datasets-and-ml.md](categories/11-datasets-and-ml.md) |
| 12 | Communities, wikis & news | [categories/12-communities-wikis-news.md](categories/12-communities-wikis-news.md) |

---

## The three rules of this repo

1. **Link, don't copy.** Every resource points to the website that provides it
   (e.g. <https://chessentials.com/chess-pgn-downloads/>). This is what keeps the repo
   free of copyright problems: we never re-host another site's collection.
2. **Host only what is explicitly redistributable.** If a file is placed in `data/`,
   its license must be permissive (CC0, public domain, MIT/BSD/Apache, GPL for code, …)
   and it must be listed with source and license in `THIRD_PARTY_NOTICES.md`.
3. **Chess games are facts — but collections can be protected.** Raw move lists are
   generally not copyrightable (US), yet in the EU a *curated database* can enjoy a
   *sui generis* database right (see
   [Chess Stack Exchange](https://chess.stackexchange.com/questions/47956/who-owns-the-copyright-to-the-results-of-chess-games)).
   Therefore: always link to the source collection (chessessentials, TWIC, …) and never
   mirror their files. To download from the originals *locally*, use
   [`scripts/fetch-pgn.sh`](scripts/fetch-pgn.sh) — its output directory is git-ignored.

---

## Highlights

- ♟ **Game databases:** [lichess open database](https://database.lichess.org/) (millions of games, free monthly dumps),
  [TWIC](https://www.theweekinchess.com/twic), [ChessEssentials PGNs](https://chessentials.com/chess-pgn-downloads/),
  [Lumbras Gigabase](https://lumbrasgigabase.com/en/), [FICS archive](https://www.ficsgames.org/)
- 🧩 **Puzzles:** [lichess training](https://lichess.org/training) + a 6M+ puzzle dump on
  [database.lichess.org](https://database.lichess.org/#puzzles), mirrored on
  [Hugging Face](https://huggingface.co/datasets/Lichess/chess-puzzles) and [Kaggle](https://www.kaggle.com/datasets/lichess/chess-puzzles)
- 🤖 **Engines:** [Stockfish](https://github.com/official-stockfish/Stockfish),
  [lc0](https://github.com/LeelaChessZero/lc0), [Fairy-Stockfish](https://fairy-stockfish.github.io/) (variants)
- 🔍 **Analysis:** [lichess](https://lichess.org/) (AGPL), [BanksiaGUI](https://banksiagui.com/),
  [Scid vs. PC](https://scidvspc.sourceforge.net/), [Arena](http://www.playwitharena.de/),
  [Cute Chess](https://github.com/cutechess/cutechess)
- 🧰 **Libraries:** [python-chess](https://github.com/niklasf/python-chess),
  [chess.js](https://github.com/jhlywa/chess.js), [chessops](https://github.com/lichess-org/chessops),
  [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
- 📚 **Books:** public-domain classics on [Project Gutenberg](https://www.gutenberg.org/ebooks/subject/1677)
  and the [Internet Archive](https://archive.org/search?query=chess)
- ♟ **Graphics:** [Cburnett SVG pieces](https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces) (CC BY-SA/GFDL),
  lichess piece sets in [lichess-org/lila](https://github.com/lichess-org/lila)

---

## Contributing

Found a great free resource? Open an issue with the
[resource template](.github/ISSUE_TEMPLATE/resource-submission.md) or send a PR —
please read [CONTRIBUTING.md](CONTRIBUTING.md) first (short version: link-first, license
required, no copyrighted uploads).

## License

The curated lists and texts in this repository are released under
[CC0 1.0 Universal (public domain dedication)](LICENSE). **Linked or hosted third-party
content remains under its own license** — see `THIRD_PARTY_NOTICES.md` and each source.

## Disclaimer

No affiliation with any linked website. Links are checked automatically once a week
([workflow](.github/workflows/link-check.yml)); if one breaks, please open an issue.
If you believe content in this repo infringes your rights, open an issue and it will be
removed promptly.
