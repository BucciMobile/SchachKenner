# licenses/ — Copyright-Nachweise (proof of permission)

This folder documents, for every source we considered hosting, **what its license/terms
explicitly allow**. Only sources with an explicit redistribution permission are hosted
in `data/` — everything else is link-only (see the category files).

## How the evidence was captured

- Each page was retrieved on **2026-11-19 (UTC)** via HTTPS GET with a normal browser
  user agent.
- The **raw HTML** of each page is preserved in [`raw/`](raw/) (file name =
  `<domain>-<page>.2026-11-19.html`), together with its **SHA-256** (below), so the
  evidence can be verified later.
- The decisive passages are quoted verbatim in the per-source markdown files.

## Verdict table

| Source | Explicit permission to download & redistribute? | Decision | Evidence |
|---|---|---|---|
| **lichess database exports** (games + puzzles) | ✅ **Yes — CC0**: "You can download, modify and redistribute them, without asking for permission." (broadcasts: CC BY-SA 4.0) | **Hosted** in `data/pgn/lichess/` (small samples; full dumps stay at source) | [lichess-database-cc0.md](lichess-database-cc0.md) |
| **Lumbras Gigabase** | ✅ Yes, with conditions — **CC BY-NC 4.0**: share with credit, non-commercial only (some files CC BY-SA 4.0) | Licensed to share; bulk download is click-gated on their site, so we **link** and keep the evidence here | [lumbras-gigabase-cc-by-nc.md](lumbras-gigabase-cc-by-nc.md) |
| **Chess piece graphics — livius set** (kmar/chess_svg_piece_sets) | ✅ **Yes — Unlicense / public domain** ("freely … for any purpose, commercial or non-commercial") | **Hosted** in `assets/img/` (banner, icons, divider) | [chess-pieces-cc0.md](chess-pieces-cc0.md) |
| chess.com | ❌ No — User Agreement forbids download/copy/distribute/scraping | Link only | [link-only-sources.md](link-only-sources.md) |
| chessgames.com | ❌ No — bulk database download requires paid membership; no redistribution grant | Link only | [link-only-sources.md](link-only-sources.md) |
| The Week in Chess (TWIC) | ❌ No explicit redistribution permission found | Link only | [link-only-sources.md](link-only-sources.md) |
| PGN Mentor | ❌ No — "Copyright © 2025 64 Squares", software sold commercially | Link only | [link-only-sources.md](link-only-sources.md) |
| ChessEssentials | ❌ No license/terms found (page sits behind a JS lander) | Link only | [link-only-sources.md](link-only-sources.md) |
| FICS / ficsgames.org | ❌ No explicit license statement found | Link only | [link-only-sources.md](link-only-sources.md) |
| 365chess.com | ❌ No explicit redistribution permission found | Link only | [link-only-sources.md](link-only-sources.md) |

## SHA-256 of the raw evidence pages (retrieved 2026-11-19 UTC)

```
26234b7cb82eafeac979236c35b14f96c747086f677ae187042133675c4f6df6  raw/chess.com-legal-user-agreement.2026-11-19.html
6dc9c7fc93bb488bb0520a6c780a8d3c0fb5486a4711aca49b4c53fac7393023  raw/chessessentials.com-chess-pgn-downloads.2026-11-19.html
0e2083b7f71b0b446794d5b8c5c38e4a2e9711c845258edfb8b8d67c66b3fe04  raw/database.lichess.org.2026-11-19.html
59ff8abc020100d90538c23af91cd2a0cdb966b0dcabccfbea0ead6b583dcd23  raw/ficsgames.org-about.2026-11-19.html
fe32badd86dac41f1de63d02c9cc077edbc750c1f7d55843d3425588c53552f2  raw/ficsgames.org-download.2026-11-19.html
41cdd1aad5730ee8dbe8d702c198420ab3cb692dee882a19bb9fe006af1cbb79  raw/lichess.org-terms-of-service.2026-11-19.html
0fa52e0524f0e02affc26b3fac5bfc2c2648e0d58e03e96437eaab2e8421939a  raw/lumbrasgigabase.com-download-area-en.2026-11-19.html
389fc0c27b5771e335d2c532bcbe9e318222c050764f1bf3d83b8df446ae4e1e  raw/pgnmentor.com-download.2026-11-19.html
6a8a2cdfe8f4a794b3fd9a939d63fd1f21a469755c76fc8f6f7da36660d3d647  raw/pgnmentor.com-home.2026-11-19.html
687d148f2186bfac792b1633092d2852110dd2ba7f0a4574fca209f2476865e4  raw/theweekinchess.com-home.2026-11-19.html
ce370b6e6d250544b2a59325f446dbdee192f888d07d147abd714ba31949856c  raw/kmar-chess_svg_piece_sets-livius-LICENSE.txt
dcc9aa22d377aeec106b3102ff988a5438e3a04fa77969604de55fa2f54bbc10  raw/kmar-chess_svg_piece_sets-README.md
```

## Rule for future additions

A file may be hosted in `data/` only if you add a markdown file here that contains:
source URL, retrieval date (UTC), the **verbatim quote** that grants redistribution,
the license name/URL, the SHA-256 of the raw page (copy in `raw/`), and the resulting
verdict. If no explicit grant exists → link only.
