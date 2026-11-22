# data/openings/ — the 26 most-played openings, derived from this repo's own datasets

`openings.json` powers the [Learn tool](https://BucciMobile.github.io/SchachKenner/learn.html).

- **Move lines:** majority mainline (most frequent SAN path, max 12 plies) per ECO family,
  computed by `scripts/build-openings.py` from the hosted standard-game datasets
  (**CC0 / MIT / Unlicense only** — the CC BY-SA datasets TCEC/broadcast are excluded).
- **Explanations:** original text written for this repo (CC0) — per-opening intro,
  variants & traps, and a note for every move (`scripts/opening-notes.py`).
- Opening names / ECO codes are facts; Wikipedia articles are linked, not copied.

| File | SHA-256 |
|---|---|
| `openings.json` | `2ad8dee380c234df533ec067dddc4454fa2914c16cbb3c7d8f2aa45b51e62ce8` |

Regenerate: `python scripts/build-openings.py` (writes this file and `docs/openings.json`).
License evidence: [`licenses/openings-dataset.md`](../../licenses/openings-dataset.md).
