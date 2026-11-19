#!/usr/bin/env bash
# fetch-pgn.sh — download PGN collections from their ORIGINAL sources.
#
# Link-first policy: files land in data/downloads/ which is GIT-IGNORED.
# They are never committed to this repo — the repo links to the sources instead.
#
# Usage:  bash scripts/fetch-pgn.sh            # fetch all entries below
#         bash scripts/fetch-pgn.sh twic       # fetch only entries containing "twic"
set -euo pipefail

OUT="$(cd "$(dirname "$0")/../data/downloads" && pwd)"
mkdir -p "$OUT"

# name|url  — edit/add entries as needed. Grab exact URLs from the source pages
# (see categories/02-game-databases-and-pgn.md).
ENTRIES="
lichess-standard-2026-01.pgn.zst|https://database.lichess.org/lichess_db_standard_rated_2026-01.pgn.zst
lichess-elite-2026-01.pgn.zst|https://database.lichess.org/lichess_db_elite_2026-01.pgn.zst
lumbras-gigabase|https://lumbrasgigabase.com/en/
twic-latest|https://www.theweekinchess.com/twic
chessessentials-pgn|https://chessentials.com/chess-pgn-downloads/
pgnmentor|https://www.pgnmentor.com/
fics-archive|https://www.ficsgames.org/
"

fetch() {
  local name="$1" url="$2"
  if [[ "$url" =~ ^https?://[^/]+/?$ ]]; then
    echo "!! $name: '$url' is a page, not a file — open it and add the direct file URL. Skipping."
    return 0
  fi
  echo "==> $name"
  echo "    $url"
  if command -v curl >/dev/null; then
    curl -fL --retry 3 --continue-at - -o "$OUT/$name" "$url" || wget -O "$OUT/$name" "$url"
  else
    wget -O "$OUT/$name" "$url"
  fi
}

FILTER="${1:-}"
echo "$ENTRIES" | while IFS='|' read -r name url; do
  [[ -z "$name" ]] && continue
  if [[ -n "$FILTER" && "$name" != *"$FILTER"* ]]; then continue; fi
  fetch "$name" "$url"
done

echo
echo "Done. Files are in: $OUT"
echo "Reminder: these files are git-ignored and must NOT be committed."
echo "Unpack lichess dumps with:  zstd -d <file>.zst"
