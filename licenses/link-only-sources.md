# Link-only sources — no explicit redistribution permission (evidence 2026-11-19 UTC)

These sources are **linked** in the category files but **never hosted** in `data/`,
because their terms do not explicitly allow downloading and redistributing their files.

## chess.com — download/copy/distribute explicitly prohibited ❌

- Source: https://www.chess.com/legal/user-agreement (retrieved 2026-11-19 UTC)
- Raw evidence: [raw/chess.com-legal-user-agreement.2026-11-19.html](raw/chess.com-legal-user-agreement.2026-11-19.html)
  SHA-256: `26234b7cb82eafeac979236c35b14f96c747086f677ae187042133675c4f6df6`
- Verbatim quote:

> "You agree to not use the Services to: **download, modify, copy, distribute, transmit,
> display, perform, reproduce, duplicate, publish, license, create derivative works from,
> or offer for sale any information contained on, or obtained from or through the
> Services**, except for temporary files that are automatically cached by your web browser
> for display purposes, or as otherwise expressly permitted in this Agreement"

> "use any robot, spider, site search/retrieval application, or other manual or automatic
> device or process to retrieve, index, 'data mine,' or in any way reproduce or circumvent
> the navigational structure or presentation of the Services or its contents"

> "D. Artificial Intelligence Restrictions — You may not use automated or artificial
> intelligence (AI) tools to access, scan, scrape, data mine, copy, or use the materials or
> content in the Services; for the purpose of developing training, or improving an AI
> model, machine-learning system, dataset, or competitive product or service."

## chessgames.com ❌

- https://www.chessgames.com/terms.html — bulk database downloads require a paid
  membership; no redistribution grant. (Page blocks plain GET requests — HTTP 405 —
  retrieved 2026-11-19.) → link only.

## The Week in Chess (TWIC) — theweekinchess.com ❌

- Source: https://www.theweekinchess.com/ and https://www.theweekinchess.com/twic
  (retrieved 2026-11-19 UTC)
- Raw evidence: [raw/theweekinchess.com-home.2026-11-19.html](raw/theweekinchess.com-home.2026-11-19.html)
  SHA-256: `687d148f2186bfac792b1633092d2852110dd2ba7f0a4574fca209f2476865e4`
- No explicit redistribution permission is stated anywhere on the site; archive access is
  donation-based. (An old issue, TWIC 74, even discusses the copyright of the compiled
  game collections.) → link only.

## PGN Mentor — pgnmentor.com ❌

- Sources: https://www.pgnmentor.com/ and https://www.pgnmentor.com/download.html
  (retrieved 2026-11-19 UTC)
- Raw evidence: [raw/pgnmentor.com-home.2026-11-19.html](raw/pgnmentor.com-home.2026-11-19.html)
  (`6a8a2cdfe8f4a794b3fd9a939d63fd1f21a469755c76fc8f6f7da36660d3d647`),
  [raw/pgnmentor.com-download.2026-11-19.html](raw/pgnmentor.com-download.2026-11-19.html)
  (`389fc0c27b5771e335d2c532bcbe9e318222c050764f1bf3d83b8df446ae4e1e`)
- Verbatim: "Copyright © 2025 64 Squares." — the companion software is sold for $25; the
  PGN files are offered for download but **no redistribution license** is stated.
  → link only (conservative).

## ChessEssentials — chessessentials.com ❌

- Source: https://chessessentials.com/chess-pgn-downloads/ (retrieved 2026-11-19 UTC)
- Raw evidence: [raw/chessessentials.com-chess-pgn-downloads.2026-11-19.html](raw/chessessentials.com-chess-pgn-downloads.2026-11-19.html)
  SHA-256: `6dc9c7fc93bb488bb0520a6c780a8d3c0fb5486a4711aca49b4c53fac7393023`
- The URL currently returns only a 114-byte JS redirect to a lander page; **no license or
  terms page** could be located that permits redistribution. → link only (conservative).

## FICS games database — ficsgames.org ❌

- Sources: https://www.ficsgames.org/ , /download.html , /about.html (retrieved 2026-11-19 UTC)
- Raw evidence in `raw/ficsgames.org-*.2026-11-19.html`
- The site offers downloads but states **no explicit license** for the game collection.
  → link only (conservative).

## 365chess.com ❌

- https://www.365chess.com/ — web database; no explicit redistribution permission found
  (retrieved 2026-11-19 UTC). → link only.

---

**General legal background** (why we are conservative): raw chess moves are facts and
generally not copyrightable (US Copyright Office), but in the EU a *curated collection*
can be protected by the *sui generis* database right. See:
https://chess.stackexchange.com/questions/47956/ and
https://chess.stackexchange.com/questions/16437/ and
https://law.stackexchange.com/questions/60030/
