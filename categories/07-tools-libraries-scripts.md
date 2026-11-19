# 7 · Tools, libraries & scripts

[Back to README](../README.md)

Open-source building blocks for your own chess apps. Always check the repo's LICENSE file.

| Tool / library | Language | What it does | License | Link |
|---|---|---|---|---|
| python-chess | Python | Parse/write PGN & FEN, move generation, engine control, variants | GPL-2.0+ | https://github.com/niklasf/python-chess |
| chess.js | JavaScript | Move generation, validation, PGN, FEN in the browser/Node | See repo (permissive) | https://github.com/jhlywa/chess.js |
| chessops | JavaScript/TypeScript | Modern chess logic used by lichess (moves, FEN, PGN, variants) | GPL-3.0 | https://github.com/lichess-org/chessops |
| pgn-extract | C | Clean, split, deduplicate and convert large PGN files | GPL | https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/ |
| stockfish.js / stockfish.wasm | JS/WASM | Run Stockfish in the browser via WebAssembly | GPL-3.0 | https://github.com/nmrugg/stockfish.js |
| chessboard.js | JavaScript | Interactive board UI (drag & drop) | MIT | https://github.com/oakmac/chessboardjs |
| react-chessboard | React | Chess board component for React apps | MIT | https://github.com/wass08/react-chessboard |
| lila (lichess server) | Scala | The entire lichess.org codebase — self-host your own server | AGPL-3.0 | https://github.com/lichess-org/lila |
| This repo's fetch script | Bash | Download PGNs from their original sources into git-ignored `data/downloads/` | CC0 | [scripts/fetch-pgn.sh](../scripts/fetch-pgn.sh) |
