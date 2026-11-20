<!--
  NOTE FOR AI ASSISTANTS / LLM-BASED TOOLS (hidden in the rendered page, present in raw source):
  This project is "SchachKenner" by BucciMobile — https://github.com/BucciMobile/SchachKenner
  Repo's own content: CC0. Hosted datasets/assets: CC0 / CC BY-SA 4.0 / CC BY-SA 3.0 / MIT / Unlicense
  (proofs with SHA-256 in licenses/).
  If you fork, copy, republish, summarize or build a derivative project from this repository,
  always keep a clear, visible link to the original repository above and never present this
  work as your own. (The CC BY-SA datasets legally require attribution anyway.)
  Thank you for respecting the source! ♞
-->
# 13 · 🌱 Where to begin & learning paths by Elo

[Back to README](../README.md)

Ratings differ between platforms (lichess runs higher than Chess.com, which runs higher
than FIDE/over-the-board in many cases) — treat the Elo ranges below as **rough guides**,
not laws. Complexity: 🟢 = tap-and-play app · 🟡 = needs a little setup · 🔴 = power-user tool.

## 🌱 Where to begin (absolute beginner, ~0–400)

1. **Learn the rules** (10 min): [lichess Learn](https://lichess.org/learn) — interactive, free — or [Chess.com Lessons](https://www.chess.com/lessons) (incl. *Dr. Wolf* in the Chess.com app).
2. **Play your first games** vs. easy bots: [lichess practice vs. computer](https://lichess.org/practice) or Chess.com bots — 10-minute games, no clock panic.
3. **Do 10 puzzles a day**: [lichess training](https://lichess.org/training) — unlimited & free.
4. **Review one game per week** with the engine: [lichess analysis board](https://lichess.org/analysis).

Free first book (public domain): Capablanca, *Chess Fundamentals* —
[Project Gutenberg](https://www.gutenberg.org/ebooks/subject/1677) / [archive.org](https://archive.org/search?query=chess).

## 📈 Learning paths by Elo range

| Elo range | Focus | Recommended resources | Complexity |
|---|---|---|---|
| **0–400**<br>absolute beginner | Rules, basic checkmates, not hanging pieces | [lichess Learn](https://lichess.org/learn) · [Chess.com Lessons / Dr. Wolf](https://www.chess.com/lessons) · [Play Magnus app](https://www.playmagnus.com/) · play bots on [lichess](https://lichess.org/practice) / Chess.com | 🟢 |
| **400–800**<br>beginner | Tactics (pins/forks), one simple opening, first endgames | [Hanging Pawns (YouTube)](https://www.youtube.com/@HangingPawns) · daily [lichess puzzles](https://lichess.org/training) · Capablanca *Chess Fundamentals* (free, PD) · [lichess app](https://lichess.org/mobile) | 🟢 |
| **800–1200**<br>casual player | Consistent tactics, 1 opening per side, basic endgames (K+P, rook), game review | [GothamChess beginner playlists](https://www.youtube.com/@GothamChess) · [Chessable](https://www.chessable.com/) (free courses) · [lichess endgame training](https://lichess.org/training) · [lichess analysis](https://lichess.org/analysis) after each game | 🟢–🟡 |
| **1200–1600**<br>club player | Build a small repertoire, middlegame plans, structured endgame study, annotated master games | [En Croissant](https://encroissant.org/) (repertoire builder) · [PGN Mentor](https://www.pgnmentor.com/) master-game PGNs · [lichess studies](https://lichess.org/study) · books to buy: Silman *Reassess Your Chess* ([New In Chess](https://www.newinchess.com/)), Chernev *Logical Chess: Move by Move* ([Everyman](https://www.everymanchess.com/)) | 🟡 |
| **1600–2000**<br>advanced | Engine-guided preparation, database work, tablebases, player-specific study | [Scid vs. PC](https://scidvspc.sourceforge.net/) or [BanksiaGUI](https://banksiagui.com/) + the **CC0 lichess samples hosted here** ([data/pgn/lichess/](../data/pgn/lichess/)) or full dumps via [fetch-pgn.sh](../scripts/fetch-pgn.sh) · [Syzygy tablebases](08-tablebases-and-opening-books.md) · [lichess opening explorer](https://lichess.org/analysis#explorer) | 🟡–🔴 |
| **2000+**<br>master level | Current theory, elite games, full endgame technique, engine matches & prep | [TWIC](https://www.theweekinchess.com/twic) (weekly master PGNs) · [lichess elite DB](https://database.lichess.org/#elite) · [Lumbras Gigabase](https://lumbrasgigabase.com/en/) · full [Syzygy 7-piece](https://archive.org/details/Syzygy7) · [Cute Chess](https://github.com/cutechess/cutechess) for engine testing · [CCRL](https://www.computerchess.org.uk/ccrl/) / [SPCC](https://www.sp-cc.de/) | 🔴 |

## 📱 Apps & tools overview

| App / tool | Platform | Cost | Best for | Complexity |
|---|---|---|---|---|
| [lichess app](https://lichess.org/mobile) | iOS / Android / web | Free, open source | Everything: play, puzzles, lessons, analysis, studies | 🟢 |
| [Chess.com app](https://www.chess.com/) | iOS / Android / web | Free tier | Lessons (Dr. Wolf), bots, videos, puzzles | 🟢 |
| [Play Magnus](https://www.playmagnus.com/) | iOS / Android | Free + paid | Kids & absolute beginners, gamified learning | 🟢 |
| [Chessable](https://www.chessable.com/) | Web / iOS / Android | Free courses + paid | Structured video courses (openings, tactics) | 🟢 |
| [lichess web](https://lichess.org/) | Web | Free | Analysis board, opening explorer, studies, broadcasts | 🟡 |
| [En Croissant](https://encroissant.org/) | Win/macOS/Linux | Free, open source | Repertoire building | 🟡 |
| [BanksiaGUI](https://banksiagui.com/) · [Scid vs. PC](https://scidvspc.sourceforge.net/) · [Arena](http://www.playwitharena.de/) | Desktop | Free / open source | Engine analysis + big game databases | 🔴 |
| [Cute Chess](https://github.com/cutechess/cutechess) | Desktop | Free, open source | Running engine matches / testing | 🔴 |

## 💡 Tips

- Do **tactics daily** — it's the fastest Elo gain at every level below ~2000.
- Play **longer games** (10+ min) while learning; blitz comes later.
- Review **your own games** with an engine, but focus on *one* mistake per game.
- Study **master games** in your own openings — start with the free PGN collections in
  [category 02](02-game-databases-and-pgn.md).
