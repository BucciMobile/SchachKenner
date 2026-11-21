#!/usr/bin/env bash
# fetch-puzzles.sh — download the lichess PUZZLE database export (CC0 1.0) used by
# scripts/build-puzzles.py to build data/pgn/puzzles/ + data/puzzles/.
#
# Link-first policy: the dump lands in data/downloads/ which is GIT-IGNORED —
# it is never committed. Only the derived, validated samples are committed.
#
# Usage:  bash scripts/fetch-puzzles.sh
set -euo pipefail

OUT="$(cd "$(dirname "$0")/../data/downloads" && pwd)"
mkdir -p "$OUT"

URL="https://database.lichess.org/lichess_db_puzzle.csv.zst"
F="$OUT/lichess_db_puzzle.csv.zst"

echo "==> lichess_db_puzzle.csv.zst"
echo "    $URL  (~310 MB, CC0 — see licenses/lichess-database-cc0.md)"
if command -v curl >/dev/null; then
  curl -fL --retry 3 --continue-at - -o "$F" "$URL" || wget -O "$F" "$URL"
else
  wget -O "$F" "$URL"
fi

echo
echo "Done: $F"
echo "build-puzzles.py reads the .zst directly if python module 'zstandard' is installed"
echo "(pip install zstandard). To unpack manually instead:  zstd -d $F"
echo "Reminder: data/downloads/ is git-ignored and must NOT be committed."
