# Contributing

Thanks for helping make this the best copyright-safe chess resource list on GitHub! ♞

## ⚠️ Uploads only via pull request — no direct file uploads

To keep the repo copyright-safe, **files are never accepted by direct upload**:

- Only the repo owner has write access (verified: no other collaborators), so external
  contributors can only open **forks + pull requests** — GitHub has no "upload to someone
  else's repo" flow for non-collaborators.
- The `main` branch is **protected**: PRs require 1 approving review, force-pushes and
  branch deletion are disabled, and the `link-check` workflow runs on every PR.
- Every PR must tick the checklist in `.github/PULL_REQUEST_TEMPLATE.md` (license
  evidence in `licenses/`, no copyrighted uploads, link check, AI disclosure).
- Issue attachments are **not** hosted content — they are ignored for the repo's data
  policy and can be removed any time (see `REMOVAL_REQUESTS.md`).

## The rules (please read before submitting)

1. **Link-first.** Add a link to the original source — do not upload another site's
   files (PGN collections, books, images, databases) into this repo.
2. **Files in `data/` only with an explicit redistribution permission** (e.g. CC0)
   **and** an entry in `THIRD_PARTY_NOTICES.md` (source URL, license, SHA-256) **and**
   a permission-evidence file in `licenses/` containing the verbatim license quote,
   retrieval date (UTC), and the raw license page in `licenses/raw/`. If you are unsure
   about the license: link only.
3. **Never upload:** copyrighted books/PDFs, annotated games from commercial databases
   (ChessBase Mega Database etc.), bulk dumps from chessgames.com / chess.com,
   paid puzzle sets, or piece graphics without a clear license.
4. **PGN rule of thumb:** raw move lists are facts and generally not copyrightable (US),
   but a *curated collection* can be protected in the EU (database right). So: link to
   collections like chessessentials.com or TWIC; don't mirror them. Users can fetch the
   originals locally with `scripts/fetch-pgn.sh`.

## How to add a resource

- One resource per row in the matching file under `categories/`.
- Format (markdown table): `| Name | What it is | Access / license | Link |`
- Pick the closest category; if none fits, propose a new one in your PR.
- Keep descriptions short (one line) and factual. Add a ⭐ in the README highlights
  only for truly standout resources.
- **Always state the license/access type** (e.g. "Open source — GPL-3.0",
  "Free download", "Web — link only", "CC0", "CC BY-SA 4.0").

## Pull requests

- Small PRs, one topic each. Update the category file and, if needed, the README TOC.
- Run `bash scripts/fetch-pgn.sh --help` is not needed — just make sure no file under
  `data/downloads/` is committed (it is git-ignored).
- Links are checked weekly by CI (lychee); please don't add dead links.
- **AI-assisted PRs are welcome** — please disclose AI assistance in the PR description
  and make sure a human has reviewed the content (same standard as the rest of this
  repo; see the "How and why we use AI" section in the README).

## Issues

Use the "New chess resource" issue template and fill in: name, URL, category,
license, and whether we may host the file in `data/`.

**Removal/takedown requests** (copyright, trademark, privacy, …) are handled per
[REMOVAL_REQUESTS.md](../REMOVAL_REQUESTS.md) — please use the "Removal request"
template or GitHub's DMCA form, not a regular issue.
