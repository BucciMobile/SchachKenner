# ♞ SchachKenner — About

<p align="center">
  <img src="assets/img/banner.svg" width="512" alt="Chess board banner with white and black pieces (livius set, public domain)">
</p>

A curated, **link-first** collection of free & open-source chess resources — for players,
programmers and researchers. We link to the original sources (copyright-safe by design)
and host only files whose license explicitly allows redistribution, with the permission
proof in [`licenses/`](licenses/).

[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![link-check](https://github.com/BucciMobile/SchachKenner/actions/workflows/link-check.yml/badge.svg)](https://github.com/BucciMobile/SchachKenner/actions/workflows/link-check.yml)

> 🆕 **New!** Try the [**interactive PGN explorer**](https://BucciMobile.github.io/SchachKenner/) — filter & search **all hosted games at once (≈20,000 games from 12 datasets, CC0 / CC BY-SA / MIT / Unlicense)** live in your browser (mobile-friendly 📱): **date range (year 1610–2026 / last 3–12 months / custom)**, Elo slider, opening search, ECO A–E, event type, result, player search — the table re-sorts automatically and every game shows its copyable PGN. (Single-dataset selection is tucked away inside the collapsible filter panel.)
>
> 🆕 **New!** [**Play & analyze in your browser**](https://BucciMobile.github.io/SchachKenner/play.html) — every game in the explorer has a **▶ Play / Analyze** button that deep-links straight into the tool (`play.html?src=<raw-pgn-url>&game=<index>`): step through games on a board with the livius piece set, **play against Stockfish 16 (WASM, runs fully client-side — GitHub Pages allows no multi-threading, so we use the official single-thread build)** or **analyze any position** (eval bar, best-move arrow, principal variation). Our own code is **CC0**; libraries (chess.js 1.4.0 **BSD-2-Clause**, Stockfish.js 16 **GPLv3**) are loaded **unmodified from the official jsDelivr CDN** with attribution — retrieval proofs in [`licenses/`](licenses/). Mobile-friendly 📱

## <img src="assets/img/pieces/livius/wb.svg" width="20" alt="bishop"> AI transparency

This repository is curated **with AI assistance** (Mistral Vibe) — openly, because we
believe transparency about tools builds trust. A human maintainer steers the research
and reviews every entry; every hosted file carries a verifiable license proof in
[`licenses/`](licenses/); all links are checked weekly by CI. Curious how and why? See
the *“How and why we use AI”* section at the bottom of this page.

---

## <img src="assets/img/pieces/livius/wn.svg" width="20" alt="knight"> What's inside

| Category | What you'll find | Browse |
|---|---|---|
| 🌱 Where to begin & paths by Elo | Step-by-step start + apps/tools per rating level (0–400 … 2000+) | [13-where-to-begin-learning-paths.md](categories/13-where-to-begin-learning-paths.md) |
| 🕹 Play & learn online | Free servers, lessons, studies | [01-play-and-learn-online.md](categories/01-play-and-learn-online.md) |
| ♟ Game databases & PGN downloads | Millions of games as PGN/SCID (lichess CC0, TWIC, Lumbras, FICS, …) | [02-game-databases-and-pgn.md](categories/02-game-databases-and-pgn.md) |
| 📖 Openings & repertoires | Opening explorers, ECO datasets, repertoire tools, opening books | [03-openings-and-repertoires.md](categories/03-openings-and-repertoires.md) |
| 🧩 Puzzles & tactics | 6M+ lichess puzzles (rated & tagged), training modes | [04-puzzles-and-tactics.md](categories/04-puzzles-and-tactics.md) |
| 🤖 Chess engines (open source) | Stockfish, lc0, Fairy-Stockfish + rating lists | [05-engines.md](categories/05-engines.md) |
| 🔍 Analysis software & GUIs | lichess, BanksiaGUI, Scid vs. PC, Arena, Cute Chess | [06-analysis-gui.md](categories/06-analysis-gui.md) |
| 🧰 Tools, libraries & scripts | python-chess, chess.js, chessops, pgn-extract, … | [07-tools-libraries-scripts.md](categories/07-tools-libraries-scripts.md) |
| 🗄 Tablebases & opening books | Syzygy ≤ 7 pieces, Gaviota, Polyglot `.bin` books | [08-tablebases-and-opening-books.md](categories/08-tablebases-and-opening-books.md) |
| 📚 Books & learning material | Public-domain classics (Project Gutenberg, archive.org), courses | [09-books-and-learning.md](categories/09-books-and-learning.md) |
| 🎨 Graphics, piece sets & fonts | Cburnett SVGs, lichess piece sets, 3D-printable pieces | [10-graphics-pieces-fonts.md](categories/10-graphics-pieces-fonts.md) |
| 🤖 Datasets & ML | lichess game/puzzle dumps, Hugging Face & Kaggle mirrors | [11-datasets-and-ml.md](categories/11-datasets-and-ml.md) |
| 💬 Communities, wikis & news | Chess Programming Wiki, forums, rating sites, news | [12-communities-wikis-news.md](categories/12-communities-wikis-news.md) |
| 🏆 Famous games & legendary sidelines | Immortal/Opera Game, Marshall Attack, Najdorf, Berlin… | [14-famous-games-and-legendary-sidelines.md](categories/14-famous-games-and-legendary-sidelines.md) |

## <img src="assets/img/pieces/livius/wp.svg" width="20" alt="pawn"> Direct downloads hosted in this repo

Only sources with **explicit redistribution permission** are hosted here — proof in
[`licenses/`](licenses/):

- 📥 [`data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn`](data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn) — 2,000 games, **CC0**
- 📥 [`data/pgn/lichess/lichess-puzzles-sample-1000.csv`](data/pgn/lichess/lichess-puzzles-sample-1000.csv) — 1,000 puzzles, **CC0**
- 📂 [`data/pgn/lichess/groups/`](data/pgn/lichess/groups/README.md) — the 2,000 games **pre-grouped into 51 files**: by opening / ECO / rating band / time control / result
- ♟ [`data/pgn/lichess-chess960/`](data/pgn/lichess-chess960/) — 1,000 Chess960 games, **CC0**, with groups
- 📡 [`data/pgn/lichess-broadcast/`](data/pgn/lichess-broadcast/) — 300 broadcast games, **CC BY-SA 4.0** (attributed), with groups
- 🏛 [`data/pgn/classic-games/`](data/pgn/classic-games/) — classic games (Tal, Memorable 60), **CC0**, with groups
- ♟ [`data/pgn/lichess-atomic/`](data/pgn/lichess-atomic/) — 1,000 Atomic games, **CC0**, with groups
- 🗓 [`data/pgn/lichess-standard-2019/`](data/pgn/lichess-standard-2019/) — 1,000 games from **2019**, **CC0** (for date-range filtering), with groups
- 🤖 [`data/pgn/tcec/`](data/pgn/tcec/) — 200 engine games (TCEC S29), **CC BY-SA 3.0** attributed, with groups
- 👑 [`data/pgn/masters/`](data/pgn/masters/) — Fischer & Euwe master games, **MIT**, with groups
- 🆕 [**Interactive PGN explorer — live in your browser**](https://BucciMobile.github.io/SchachKenner/) — filter the games by time control, Elo range slider, opening, ECO category (A–E), event type, result, player name; the table re-sorts automatically and every game shows its copyable PGN. Also loads your own PGN files. Optimized for mobile 📱
- 🆕 [**Play & analyze tool — live in your browser**](https://BucciMobile.github.io/SchachKenner/play.html) — board view with move navigation, **play vs Stockfish 16 WASM** (client-side), **position analysis** (eval bar + best move + PV), and a **🔗 share button** that copies a short text + deep link (`?src=…&game=…`, used by the explorer's ▶ button). Engine/lib licenses: GPLv3 / BSD-2-Clause, loaded unmodified via CDN, proofs in [`licenses/`](licenses/)

> "Database exports are released under the Creative Commons CC0 license. … You can
> download, modify and redistribute them, without asking for permission."
> — [database.lichess.org](https://database.lichess.org/) (evidence: [licenses/lichess-database-cc0.md](licenses/lichess-database-cc0.md))

Full multi-GB dumps stay at their sources — fetch them locally with
[`scripts/fetch-pgn.sh`](scripts/fetch-pgn.sh) (output is git-ignored).

## <img src="assets/img/pieces/livius/br.svg" width="20" alt="rook"> How we stay copyright-safe

1. **Link, don't copy** — every resource points to its original source (e.g.
   [chessessentials.com/chess-pgn-downloads](https://chessessentials.com/chess-pgn-downloads/)).
2. **Host only with explicit permission** — hosted files are listed in
   [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md); the permission evidence (verbatim
   quote, raw page copy, SHA-256, retrieval date) is in [`licenses/`](licenses/).
3. **Chess games are facts — curated collections can be protected** (EU database right),
   so collections like TWIC/PGN Mentor/ChessEssentials are always linked, never mirrored —
   see [licenses/link-only-sources.md](licenses/link-only-sources.md).

## <img src="assets/img/pieces/livius/bk.svg" width="20" alt="king"> Legal & removal requests

If you believe content in this repo infringes your rights (copyright, trademark,
personal data/GDPR, …): see **[REMOVAL_REQUESTS.md](REMOVAL_REQUESTS.md)** — copyright
claims go through [GitHub's DMCA form](https://github.com/contact/dmca), everything else
via the [removal-request issue template](.github/ISSUE_TEMPLATE/removal-request.md).
We acknowledge within 48 h, decide within 7 days, and log actions in
[REMOVAL_LOG.md](REMOVAL_LOG.md).

## <img src="assets/img/pieces/livius/wq.svg" width="20" alt="queen"> Contributing

Found a great free resource? Open an issue with the
[resource template](.github/ISSUE_TEMPLATE/resource-submission.md) or send a PR —
please read [CONTRIBUTING.md](CONTRIBUTING.md) first (short version: link-first, license
evidence required for hosted files, no copyrighted uploads). Code of conduct:
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). License of this repo's own content:
[CC0](LICENSE). Disputes about existing content: [REMOVAL_REQUESTS.md](REMOVAL_REQUESTS.md).

---

<p align="center"><img src="assets/img/divider.svg" width="640" alt=""></p>

## <img src="assets/img/pieces/livius/wk.svg" width="20" alt="king"> Shoutout — thanks to all the sources we use and link to

> 💡 **Inspiration:** this repo was inspired by the German chess podcast
> [**ELOjäger – Der Schachpodcast**](https://open.spotify.com/show/0Vb66GFKHFMbpTUvuQYyZG)
> by David & Sebastian — still active (latest: Folge 40, Nov 2026). Listen on
> [Spotify](https://open.spotify.com/show/0Vb66GFKHFMbpTUvuQYyZG) ·
> [Apple Podcasts](https://podcasts.apple.com/us/podcast/eloj%C3%A4ger-der-schachpodcast/id1783522132) ·
> [Podimo](https://podimo.com/en/shows/elojager-der-schachpodcast) ·
> [RSS](https://anchor.fm/s/fd2d9df0/podcast/rss) 🎧

This project stands on the shoulders of these sites, projects and people:

- **Game data:** [lichess open database](https://database.lichess.org/) (CC0) ·
  [The Week in Chess](https://www.theweekinchess.com/twic) ·
  [ChessEssentials PGN downloads](https://chessessentials.com/chess-pgn-downloads/) ·
  [PGN Mentor](https://www.pgnmentor.com/) ·
  [Lumbras Gigabase](https://lumbrasgigabase.com/en/) (CC BY-NC 4.0) ·
  [FICS games archive](https://www.ficsgames.org/) ·
  [365Chess](https://www.365chess.com/) · [chessgames.com](https://www.chessgames.com/) ·
  [Chess.com](https://www.chess.com/)
- **Play & training:** [lichess.org](https://lichess.org/) · [FICS](https://www.freechess.org/) ·
  [ICC](https://www.chessclub.com/) · [PlayChess](https://www.playchess.com/) ·
  [Play Magnus app](https://www.playmagnus.com/) · [Chessable](https://www.chessable.com/)
- **Engines:** [Stockfish](https://github.com/official-stockfish/Stockfish) ·
  [lc0](https://github.com/LeelaChessZero/lc0) ·
  [Fairy-Stockfish](https://fairy-stockfish.github.io/) ·
  [CCRL](https://www.computerchess.org.uk/ccrl/) · [SPCC](https://www.sp-cc.de/)
- **Software & GUIs:** [BanksiaGUI](https://banksiagui.com/) ·
  [Scid vs. PC](https://scidvspc.sourceforge.net/) · [Arena](http://www.playwitharena.de/) ·
  [Cute Chess](https://github.com/cutechess/cutechess) ·
  [En Croissant](https://encroissant.org/) · [ChessBase](https://en.chessbase.com/)
- **Libraries & tools:** [python-chess](https://github.com/niklasf/python-chess) ·
  [chess.js](https://github.com/jhlywa/chess.js) ·
  [chessops](https://github.com/lichess-org/chessops) ·
  [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) ·
  [stockfish.js](https://github.com/nmrugg/stockfish.js) ·
  [chessboard.js](https://github.com/oakmac/chessboardjs) ·
  [react-chessboard](https://github.com/wass08/react-chessboard) ·
  [lila (lichess server)](https://github.com/lichess-org/lila) ·
  [chess-openings dataset](https://github.com/lichess-org/chess-openings) ·
  [Polyglot](https://github.com/ddugovic/polyglot) ·
  [free opening books](https://github.com/gmcheems-org/free-opening-books)
- **Tablebases:** [Syzygy](https://chessprogramming.org/Syzygy_Bases) ·
  [syzygy1/tb](https://github.com/syzygy1/tb) · [archive.org Syzygy7](https://archive.org/details/Syzygy7) ·
  [Gaviota](https://chessprogramming.org/Gaviota_Tablebases)
- **Books & learning:** [Project Gutenberg chess shelf](https://www.gutenberg.org/ebooks/subject/1677) ·
  [Internet Archive](https://archive.org/search?query=chess) ·
  [lichess Learn](https://lichess.org/learn) · [lichess Studies](https://lichess.org/study) ·
  [Chess.com Lessons](https://www.chess.com/lessons) ·
  [GothamChess](https://www.youtube.com/@GothamChess) ·
  [Hanging Pawns](https://www.youtube.com/@HangingPawns) ·
  [chessbrah](https://www.youtube.com/@ChessBrah)
- **🎙 Podcasts (DE):** [ELOjäger – Der Schachpodcast](https://open.spotify.com/show/0Vb66GFKHFMbpTUvuQYyZG)
  (David & Sebastian — Taktik, Eröffnungen, Turniererlebnisse; aktiv, zuletzt 11/2026) ·
  [Apple Podcasts](https://podcasts.apple.com/us/podcast/eloj%C3%A4ger-der-schachpodcast/id1783522132) ·
  [RSS](https://anchor.fm/s/fd2d9df0/podcast/rss)
- **Graphics:** [livius/meridian SVG piece sets](https://github.com/kmar/chess_svg_piece_sets) (**public domain** — used for this page's banner & icons, see `assets/img/`) · [Cburnett SVG pieces (Wikimedia Commons)](https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces) ·
  [lichess piece sets](https://github.com/lichess-org/lila/tree/master/public/piece) ·
  [Printables](https://www.printables.com/search?q=chess%20pieces) · [Thingiverse](https://www.thingiverse.com/search?q=chess+pieces) ·
  [Twemoji](https://github.com/twitter/twemoji)
- **Datasets:** [Hugging Face — Lichess/chess-puzzles](https://huggingface.co/datasets/Lichess/chess-puzzles) ·
  [Kaggle chess datasets](https://www.kaggle.com/datasets?search=chess)
- **Knowledge & community:** [Chess Programming Wiki](https://chessprogramming.org/) (CC BY-SA) ·
  [Chess Stack Exchange](https://chess.stackexchange.com/) ·
  [r/chess](https://www.reddit.com/r/chess/) · [r/ComputerChess](https://www.reddit.com/r/ComputerChess/) ·
  [lichess forum](https://lichess.org/forum) · [2700chess](https://2700chess.com/) ·
  [ChessBase News](https://en.chessbase.com/news) · [Chess.com News](https://www.chess.com/news)

*No affiliation with any of them — if you believe content here infringes your rights, follow
[REMOVAL_REQUESTS.md](REMOVAL_REQUESTS.md) (DMCA form for copyright, issue template
otherwise); actions are logged in [REMOVAL_LOG.md](REMOVAL_LOG.md).*

---

## <img src="assets/img/pieces/livius/bq.svg" width="20" alt="queen"> How and why we use AI

We use AI (Mistral Vibe) to research, structure and maintain this collection — openly
and deliberately, because we believe that being upfront about the tools we use builds
more trust than hiding them.

**Our own knowledge drives the research.** The maintainer of this repo is a chess
enthusiast, and his knowledge of the chess landscape — which sites and tools are
worth listing, which collections raise legal questions, where the pitfalls are — is
the input that steers what the AI investigates, compares and drafts. The AI does the
fetching, summarizing and formatting; a human decides what goes into the repo and
reviews every entry before it is published.

**Legal foundations are much easier to research this way.** Questions like *“May we
redistribute these PGN files?”*, *“How does GitHub's DMCA process actually work?”*,
*“Does the EU database right cover curated game collections?”* or *“Are player
usernames in PGNs personal data under the GDPR?”* can be researched systematically in
minutes instead of days. Still, we never rely on AI output alone for legal questions:
every legal claim in this repo is checked against primary sources, and the raw pages
plus their SHA-256 hashes are preserved in [`licenses/raw/`](licenses/raw/) so anyone
can re-verify them independently. Nothing in this repository is legal advice.

**Quality gates stay human.** Links are checked automatically every week
([workflow](.github/workflows/link-check.yml)), hosted files require a documented
permission in [`licenses/`](licenses/), and takedown requests follow the process in
[REMOVAL_REQUESTS.md](REMOVAL_REQUESTS.md). Everything we create here ourselves is
released under [CC0](LICENSE).
