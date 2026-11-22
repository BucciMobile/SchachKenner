# SchachKenner daily puzzles — hosted PGNs

9000 chess puzzles (3000 easy / 3000 medium /
3000 hard by lichess puzzle rating), one PGN per puzzle in
`<level>/<PuzzleId>.pgn`. Each PGN carries `SetUp`/`FEN` (the position to solve, side to move
is the solver) plus the full solution line as movetext and as `Solution`/`SolutionSAN` headers.

- **Source:** lichess puzzle database export <https://database.lichess.org/lichess_db_puzzle.csv.zst>
  (6M+ rated, tagged puzzles) — **CC0 1.0**, proof: [licenses/lichess-database-cc0.md](../../licenses/lichess-database-cc0.md)
- **Selection:** deterministic sample (seed 20261121, 3000 per band) built by
  `scripts/build-puzzles.py`; validate with `scripts/validate-puzzles.py`.
- **Daily rotation:** `docs/puzzles.html` picks, per UTC day (`floor(Date.now()/86400000)`),
  one puzzle per level: `ids[(dayIndex + levelOffset) % ids.length]` — see `data/puzzles/index.json`.
- **Machine-readable index:** [data/puzzles/index.json](../puzzles/index.json) + per-level
  [easy.json](../puzzles/easy.json) / [medium.json](../puzzles/medium.json) / [hard.json](../puzzles/hard.json)
  (fen, moves, san, rating, themes, gameUrl per puzzle).

Generated 2026-11-22 UTC. Repo content: CC0.
