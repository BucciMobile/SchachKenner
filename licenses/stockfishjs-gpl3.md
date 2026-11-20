# Stockfish.js 16 (nmrugg/stockfish.js v16.0.0) — GPLv3 ✅ used via CDN (unmodified, with attribution)

- **Source:** https://github.com/nmrugg/stockfish.js — npm package `stockfish@16.0.0`
  (based on the official Stockfish engine, https://github.com/official-stockfish/Stockfish)
- **How we use it:** `docs/play.html` loads the **official single-thread WASM build
  unmodified** from the jsDelivr CDN mirror of the npm package and runs it fully
  client-side in the browser:
  - `https://cdn.jsdelivr.net/npm/stockfish@16.0.0/src/stockfish-nnue-16-single.js`
  - `https://cdn.jsdelivr.net/npm/stockfish@16.0.0/src/stockfish-nnue-16-single.wasm`
  - the neural net `…/src/nn-5af11540bbfe.nnue` (loaded by the engine at runtime through
    the same `locateFile` path)

  Nothing is vendored or modified in this repo. GPLv3 §4–6 obligations for
  **conveying verbatim copies** are met because the distributed files themselves carry the
  license header (see below) and a link to the full license text
  (`license.txt` / `Copying.txt` in the same package); we additionally name the project,
  version and license in the footer of `docs/play.html` and link the source repository
  (which is the “Corresponding Source” for this build) here.
- **License header embedded in the engine file (verbatim, first lines of
  `stockfish-nnue-16-single.js`):**
  > `/*! Stockfish.js 16 (c) 2023, Chess.com, LLC — https://github.com/nmrugg/stockfish.js
  > — License: GPLv3 … Based on Stockfish (c) T. Romstad, M. Costalba, J. Kiiski,
  > G. Linscott and other contributors. https://github.com/official-stockfish/Stockfish */`
- **Raw copies (retrieved 2026-11-20 UTC via cdn.jsdelivr.net, SHA-256):**
  - [raw/nmrugg-stockfish.js-v16.0.0-license.txt](raw/nmrugg-stockfish.js-v16.0.0-license.txt) (full GPLv3 text) — `8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903`
  - [raw/nmrugg-stockfish.js-v16.0.0-Readme.md](raw/nmrugg-stockfish.js-v16.0.0-Readme.md) (“License: GPLv3”, lists the single-threaded flavor) — `f6e73445b3839cdb3edefa312269dd73a6f9fefe95669d2cc1ef9a44d6a8b498`
  - [raw/nmrugg-stockfish.js-v16.0.0-package.json](raw/nmrugg-stockfish.js-v16.0.0-package.json) (`"license": "GPL"`) — `8724dfec4c94814234fb3887e5dd37e7354c50efbffdae7266885c7634bec41f`
  - [raw/nmrugg-stockfish.js-v16.0.0-stockfish-nnue-16-single.js](raw/nmrugg-stockfish.js-v16.0.0-stockfish-nnue-16-single.js) (the engine JS incl. embedded license header) — `e2958bb89fc6ee0faedde87284bbb7e14da2ab224f06ca1bd82e62eaca87d00b`
- **Technical note:** GitHub Pages sends no COOP/COEP headers, so no SharedArrayBuffer →
  only the **single-thread** build (`stockfish-nnue-16-single.*`) can run there. That is
  exactly the build we load.
- **License URL:** https://www.gnu.org/licenses/gpl-3.0.html — Corresponding Source:
  https://github.com/nmrugg/stockfish.js (tag `v16.0.0`) and
  https://github.com/official-stockfish/Stockfish
- **Verdict:** GPLv3 permits running and redistributing the engine; for verbatim
  redistribution the license text + source offer must accompany it — the upstream files
  carry the header and the package ships `license.txt`, and we link both here and in the
  tool footer. Mere linking/loading from the official CDN with attribution is
  unproblematic. ✅ (We deliberately do NOT vendor or patch GPL code into this repo.)
- **Related, link-only:** [En Croissant](https://github.com/franciscoBSalgueiro/en-croissant)
  (GPL-3.0, Tauri desktop app) is mentioned as a full-featured desktop alternative —
  naming/linking is explicitly fine under GPL.
