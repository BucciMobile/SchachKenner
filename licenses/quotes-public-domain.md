# Chess quotes pool (`data/quotes/quotes.json`) — public-domain reasoning & verification log

The About page (README.md) shows one quote per UTC day from a hidden pool in
[`data/quotes/quotes.json`](../data/quotes/quotes.json) (rotated by
`scripts/update-quote.py` / `.github/workflows/daily-quote.yml`). This file
documents **why every quote in the pool is copyright-free** and **how each quote
and each author was vetted**.

## 1. Legal basis — public domain only, no "fair use" needed

- **EU/Germany (relevant for this project):** copyright expires 70 years after the
  author's death (UrhG § 69/§ 70). Every author in the pool died in **1955 or
  earlier**, so all their works have been in the **public domain in the EU since at
  latest 1 January 2026**. No permission needed, no license needed.
- **US:** works published **before 1930** are public domain in the US. Many quoted
  works (Philidor 1749, Morphy 1859 testimonials, Anderssen/Steinitz periodicals
  1886–1891, Capablanca's *Chess Fundamentals* 1921, Lasker's *Manual of Chess* 1925
  and *Common Sense in Chess* 1919, Nimzowitsch's *My System* 1925, the 1906
  *American Chess Bulletin*) are pre-1930 and therefore also PD in the US.
- **General rule (for context):** short quotes from *published* works may also be
  used with proper attribution as a "Zitat" (e.g. § 51 UrhG in Germany) even while
  copyright lasts. We nevertheless restrict the pool to **strictly public-domain
  authors (died ≤ 1955)**, so the quotes are free under every relevant regime and no
  one has to rely on a citation exception.
- Short quotations are additionally fine as such (a quotation is not a "work" of its
  own); we keep quotes short and always attribute author + work.

## 2. Verification protocol (no misattribution)

Every quote was verified on **2026-11-23 (UTC)** against **at least two independent
sources**, preferring:

1. **Primary texts** — the authors' own books/periodicals. Several are hosted in
   this repo as public-domain scans in [`data/books/`](../data/books/)
   (e.g. `data/books/en/lasker-s-manual-of-chess.txt`,
   `data/books/en/chessfundamental00capa.txt`, `data/books/en/nimzowitsch-my-system.txt`
   — all pre-1930, PD-Mark on [archive.org](https://archive.org)), and the quotes were
   matched against those texts.
2. **Edward Winter's Chess Notes** on [chesshistory.com](https://www.chesshistory.com/winter/),
   which trace famous chess quotations to their first printing with exact page numbers.
3. Independent quote databases (Wikiquote, FIDE's Open Chess Museum, etc.) as
   corroboration only.

Full per-quote source lists live in `data/quotes/quotes.json` (`sources` arrays).

### Famous lines that were checked and REJECTED (would be misattribution)

| Line | Why rejected |
|---|---|
| "When you see a good move, look for a better one." — *Lasker* | The adage is centuries older (del Rio 1568; Chess Player's Chronicle 1851); Winter: attribution to Lasker is unsourced. |
| "The ability to play chess well is the sign of a wasted life." — *Morphy* | Apocryphal; no evidence Morphy said it (Skeptics StackExchange; Chess Player's Magazine 1866 only shows a similar sentiment). |
| "I see only one move ahead, but it is always the correct one." — *Capablanca* | No known source (Winter, "How Many Moves Ahead"). |
| "The blunders are all there on the board, waiting to be made." — *Tarrasch* | Actually **Tartakower** (Die Hypermoderne Schachpartie 1924, p. 90); Tartakower died 1956 → not PD in the EU yet, so excluded. |
| "Chess is a fairy tale of 1001 blunders" | Tartakower, not Réti → excluded (see above). |
| "Chess is the gymnasium of the mind." — *Anderssen* | Actually Pascal ("gymnase de l'esprit") → excluded. |
| "The winner makes the next-to-last mistake." | Tartakower → excluded. |
| "The hardest game to win is a won game." | Attribution disputed (Capablanca vs. Lasker) → excluded. |
| "A good player is always lucky." — *Capablanca* | Bill Wall: "perhaps never said by Capablanca" → excluded. |

## 3. Author vetting — no players with negative headlines

Each quoted player was checked for documented scandals / negative headlines
(2026-11-23). Quoted players are all clean; several were themselves victims of
antisemitism (Steinitz, Lasker, Tarrasch, Nimzowitsch), which is documented, not a
scandal on their side. Chess-internal disputes (e.g. Lasker's 1910 Schlechter match
rules) are part of chess history, not negative press.

### Deliberately EXCLUDED players (documented negative headlines / controversies)

| Player | Reason | Evidence |
|---|---|---|
| **Bobby Fischer** | Repeated antisemitic statements and Holocaust denial | [Wikipedia — Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer), [Times of Israel / JTA](https://www.timesofisrael.com/bulgarian-game-show-host-quotes-anti-semitic-rant-by-chess-master-bobby-fischer/), [World Jewish Congress](https://www.worldjewishcongress.org/en/news/japan-orders-deportation-of-bobby-fischer) |
| **Alexander Alekhine** | 1941 antisemitic "Aryan and Jewish Chess" articles in the Nazi *Pariser Zeitung* (text found in his own handwriting); played in Nazi-organized tournaments | [chesshistory.com — "Was Alekhine a Nazi?"](https://www.chesshistory.com/winter/extra/alekhine.html), [Wikipedia — Alexander Alekhine](https://en.wikipedia.org/wiki/Alexander_Alekhine), [Wikipedia — 1941 in chess](https://en.wikipedia.org/wiki/1941_in_chess) |
| **Efim Bogoljubow** | Played in Nazi "General Government" tournaments, co-ran a chess school under Hans Frank; alleged formal Nazi party membership; FIDE withheld the GM title in 1951 over alleged fascism | [Wikipedia — Efim Bogoljubow](https://en.wikipedia.org/wiki/Efim_Bogoljubow), [Wikipedia — General Government chess tournament](https://en.wikipedia.org/wiki/General_Government_chess_tournament), [ChessBase — Bogoljubow: A Chess Career](https://en.chessbase.com/post/efim-bogoljubow-a-chess-career) |

### Excluded for copyright reasons (not yet PD in the EU; died after 1955)

Savielly Tartakower (d. 1956), Frank Marshall (d. 1959), Akiba Rubinstein (d. 1961),
Mikhail Tal (d. 1992), etc. — their quotes are *cittable with attribution*, but per
§ 1 we only host strictly PD authors.

## 4. Pool contents

18 quotes, all in English, by: Philidor (1795), Anderssen (1879), Morphy (1884),
Steinitz (1900), Tarrasch (1934), Nimzowitsch (1935), Réti (1929), Capablanca
(1942), Spielmann (1942), Lasker (1941), Maróczy (1951). See
[`data/quotes/quotes.json`](../data/quotes/quotes.json) for text, author, primary
work and per-quote source URLs.
