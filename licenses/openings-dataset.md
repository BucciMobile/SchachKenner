# Openings dataset (`data/openings/openings.json`) — derived in-repo ✅ HOSTED

- **What:** 26 most-played openings (ECO families), each with the majority mainline
  (max 12 plies, computed from game frequency) + original explanation notes.
- **Derivation (fully in-repo, no external content):**
  `scripts/build-openings.py` reads only the hosted **standard** PGN datasets
  `data/pgn/{lichess, lichess-standard-2019, classic-games, masters, historic-masters}`
  — licenses **CC0** (lichess exports), **MIT** (Dragjon/chessdatabase), **Unlicense**
  (thechessdog/pawn) — see their proofs in `licenses/`. The CC BY-SA datasets
  (TCEC, lichess broadcasts) and all variant datasets are **excluded** from the
  derivation, so the output needs no attribution.
- **Copyright analysis:** move sequences of games are facts (not copyrightable in the
  US; the CC0/MIT/Unlicense sources explicitly waive any sui-generis database rights).
  Opening names and ECO codes are facts/classification systems. All explanation texts
  (intro, variants & traps, per-move notes) are **original wording written for this
  repo** → CC0. Wikipedia is only linked.
- **Output:** `data/openings/openings.json` (canonical) + `docs/openings.json` (copy
  served by GitHub Pages), SHA-256 `2ad8dee380c234df533ec067dddc4454fa2914c16cbb3c7d8f2aa45b51e62ce8`,
  built 2026-11-20 UTC. Regenerate with `python scripts/build-openings.py`.
- **Verdict:** ✅ hosted — derived from explicitly free sources + own text.
