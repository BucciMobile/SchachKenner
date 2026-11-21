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
| **lichess variant exports (Chess960)** + **broadcast exports** | ✅ CC0 (variants) / **CC BY-SA 4.0 with attribution** (broadcasts) | **Hosted** in `data/pgn/lichess-chess960/`, `data/pgn/lichess-broadcast/` | [lichess-variants-and-broadcasts.md](lichess-variants-and-broadcasts.md) |
| **Classic games PGN** (brianerdelyi/ChessPGN: Tal, Memorable 60) | ✅ **CC0-1.0** | **Hosted** in `data/pgn/classic-games/` | [classic-games-cc0.md](classic-games-cc0.md) |
| **lichess Atomic 2026-10 + standard 2019-12** | ✅ CC0 (same export grant) | **Hosted** in `data/pgn/lichess-atomic/`, `data/pgn/lichess-standard-2019/` | [lichess-variants-and-broadcasts.md](lichess-variants-and-broadcasts.md) |
| **TCEC Season 29 engine games** | ✅ **CC BY-SA 3.0** (attribution) | **Hosted** in `data/pgn/tcec/` | [tcec-ccbysa3.md](tcec-ccbysa3.md) |
| **Master games Fischer/Euwe** (Dragjon/chessdatabase) | ✅ **MIT** | **Hosted** in `data/pgn/masters/` | [masters-mit.md](masters-mit.md) |
| **Historic masters 1610–1899** (thechessdog/pawn, 10,942 games) | ✅ **Unlicense** (PD sources) | **Hosted** in `data/pgn/historic-masters/` (merged by century) | [historic-masters-unlicense.md](historic-masters-unlicense.md) |
| **lichess Crazyhouse / Horde / KingOfTheHill 2026-10** | ✅ CC0 (same export grant) | **Hosted** in `data/pgn/lichess-crazyhouse/` etc. | [lichess-variants-and-broadcasts.md](lichess-variants-and-broadcasts.md) |
| chess.com | ❌ No — User Agreement forbids download/copy/distribute/scraping | Link only | [link-only-sources.md](link-only-sources.md) |
| chessgames.com | ❌ No — bulk database download requires paid membership; no redistribution grant | Link only | [link-only-sources.md](link-only-sources.md) |
| The Week in Chess (TWIC) | ❌ No explicit redistribution permission found | Link only | [link-only-sources.md](link-only-sources.md) |
| PGN Mentor | ❌ No — "Copyright © 2025 64 Squares", software sold commercially | Link only | [link-only-sources.md](link-only-sources.md) |
| ChessEssentials | ❌ No license/terms found (page sits behind a JS lander) | Link only | [link-only-sources.md](link-only-sources.md) |
| FICS / ficsgames.org | ❌ No explicit license statement found | Link only | [link-only-sources.md](link-only-sources.md) |
| 365chess.com | ❌ No explicit redistribution permission found | Link only | [link-only-sources.md](link-only-sources.md) |
| **chess.js 1.4.0** (jhlywa/chess.js) — JS chess rules/PGN library | ✅ **BSD-2-Clause** — use & redistribution allowed, copyright notice + license text must be retained | **Loaded unmodified via official jsDelivr CDN** in `docs/index.html` / `docs/play.html` (not vendored); attribution + license link in the tool footer | [chessjs-bsd2.md](chessjs-bsd2.md) |
| **Stockfish.js 16** (nmrugg/stockfish.js v16.0.0) — WASM chess engine | ✅ **GPLv3** — verbatim redistribution allowed with license text + Corresponding Source (the engine file itself carries the GPL header) | **Loaded unmodified via official jsDelivr CDN** in `docs/play.html` (single-thread build — GitHub Pages sends no COOP/COEP, so no SharedArrayBuffer); attribution + source link in the tool footer; nothing vendored or patched | [stockfishjs-gpl3.md](stockfishjs-gpl3.md) |
| **Ko-fi support button PNG** | ✅ Owner-provided asset (uploaded by repo owner BucciMobile, 2026-11-20); Ko-fi-branded button linking to Ko-fi is Ko-fi's intended button use | **Hosted** in `assets/img/ko-fi-button.png`, shown in README (top) + `docs/play.html` header, linking to the owner's Ko-fi goal | [ko-fi-button.md](ko-fi-button.md) |
| **17 public-domain chess books in 8 languages** (Internet Archive items, all published ≤ 1929) | ✅ Most items carry an explicit **Public Domain Mark 1.0** (`licenseurl` in the IA metadata); the rest are PD in the US by age (pre-1930) | **Hosted** full texts in `data/books/<lang>/` with per-file SHA-256; raw IA metadata JSON per item in `raw/ia-*.metadata.json` | [books-public-domain.md](books-public-domain.md) |
| **Openings dataset** (`data/openings/openings.json`, 26 openings) | ✅ Derived in-repo from CC0/MIT/Unlicense PGN datasets (CC BY-SA datasets excluded); move lines & ECO codes are facts; explanation texts are original (CC0) | **Hosted** in `data/openings/` + served copy `docs/openings.json`; generator scripts in `scripts/` | [openings-dataset.md](openings-dataset.md) |

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
a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499  raw/brianerdelyi-ChessPGN-LICENSE.txt
040827200dcb55ba55a976c7ca25da2b7023525999c9f7110b37106a78b7db7c  raw/TCEC-tcecgames-README.md
43959ed7d06a8db78d3ce56527a9f076dc7386ac65ac09f319055f9717d49536  raw/Dragjon-chessdatabase-LICENSE.txt
6b0382b16279f26ff69014300541967a356a666eb6b0b91b422f6862f6b7dad17e  raw/thechessdog-pawn-LICENSE.txt
cf12ca700f556c7b333f5a6b84f821f03ef97c974553afafb6bf35194390295d  raw/thechessdog-pawn-README.md
```

### SHA-256 of the CDN library evidence (retrieved 2026-11-20 UTC via cdn.jsdelivr.net)

```
0b3a3c2b4432a26bb18f9d06f5bba4de015bcc980306b7db28b06025495e2186  raw/chess.js-1.4.0-LICENSE.txt
36a258fdfb5e76d0816bf2b63dab3c917a0a8652f943da0e6be7e9b543765dfd  raw/chess.js-1.4.0-package.json
8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903  raw/nmrugg-stockfish.js-v16.0.0-license.txt
f6e73445b3839cdb3edefa312269dd73a6f9fefe95669d2cc1ef9a44d6a8b498  raw/nmrugg-stockfish.js-v16.0.0-Readme.md
8724dfec4c94814234fb3887e5dd37e7354c50efbffdae7266885c7634bec41f  raw/nmrugg-stockfish.js-v16.0.0-package.json
e2958bb89fc6ee0faedde87284bbb7e14da2ab224f06ca1bd82e62eaca87d00b  raw/nmrugg-stockfish.js-v16.0.0-stockfish-nnue-16-single.js
c56ccacd49ecde8b6e9484d51853a421dd69c517539c89b469daee32df351bea  raw/ko-fi-button.png
```

### SHA-256 of the archive.org metadata evidence for the 17 hosted PD chess books (retrieved 2026-11-20 UTC)

```
52f45e01abdcf09028ec0aceeec329c39dc3a700f7ef71a9f94885a63cbe258d  raw/ia-20200309_20200309_0752.metadata.json
a2cf88376eaad2834612d6c5f16458a9e28dc107d7dd26533356198a805ba78d  raw/ia-3-5_pertrov_chess.metadata.json
b481387f3d805ef275ba1c7ac785b14939fb2deac438b9906a8fabd06b2dca97  raw/ia-ChessMadeEasyOrTheGamesOfGioachin.metadata.json
75636a0717c9faa1fd49571c8882912a0f428b21975127c754e01dcf8a92a07f  raw/ia-LarobokISchackForNyborjare.metadata.json
8a28c550b4c40394b20782741df228fee90463d1a6d5695bf661f5b87a3882a5  raw/ia-TavernerChessProblemsMadeEasy.metadata.json
1e4545e916e92a4df7473252d22807c2a9e237c0024111e8fd9b163dabb5cc78  raw/ia-blathy-vielzugige-schachaufgaben.metadata.json
ec9e6a088f94bb895c133eb17b08f075ce683720eb2565f3473a23fbb2e4e698  raw/ia-bub_gb_8PtlpgB4Wm4C.metadata.json
8256d37cb1a7f07c14e8dd5e7d237481b36b9349bc5b228fb614947b861ed75  raw/ia-bub_gb_RicCAAAAYAAJ.metadata.json
0e9012012142c3cf25aafbed594496ebdfd2c94df683fc9f65aed93c34192954  raw/ia-bub_gb__dwCAAAAYAAJ.metadata.json
c79dd341ed5b7d64235b9885587ffd545ace699284cca62d8f0d1fe6881e7197  raw/ia-bub_gb_cikCAAAAYAAJ.metadata.json
94a8d0d6207f013ac207b0ac9fa4163e0317b50e425a5dea2515073b2a3ecb0b  raw/ia-bub_gb_d69AAAAAcAAJ.metadata.json
6c845dc8d61775f8c473225331edc5274b36b9349bc5b228fb614947b861ed75  raw/ia-bub_gb_nE8UAAAAQAAJ.metadata.json
1222903f73c213b13b3fa5dfdbc2aaf8ebbda432d7c124bbc9017919ea19aa69  raw/ia-bub_gb_w95-78eDjFAC.metadata.json
1cc91932968bf98061b903eb3c2ea4bcdfbd48c544d55dcd35f8cfd5999b1fde  raw/ia-chessfundamental00capa.metadata.json
fe2e89448e7de081598d2caafaef616bbaa83b8b018d8d02460a0639e8a907bb  raw/ia-lasker-s-manual-of-chess.metadata.json
2bc2d7fc161afaf5ef37afcc2aad1f888d0709fb094b16530b98b5c1cc1f3f6e  raw/ia-nimzowitsch-my-system.metadata.json
3ea4ee4d64aab5920148ecc78068a6d9f5a34cfb2b1bb960a9f1796a30d489e6  raw/ia-osensocomumnoxadrez.metadata.json
```

The hosted openings dataset (`data/openings/openings.json` + `docs/openings.json`, built 2026-11-20 UTC):

```
2ad8dee380c234df533ec067dddc4454fa2914c16cbb3c7d8f2aa45b51e62ce8  data/openings/openings.json
```

## Rule for future additions

A file may be hosted in `data/` only if you add a markdown file here that contains:
source URL, retrieval date (UTC), the **verbatim quote** that grants redistribution,
the license name/URL, the SHA-256 of the raw page (copy in `raw/`), and the resulting
verdict. If no explicit grant exists → link only.
