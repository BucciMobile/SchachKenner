# `data/` — hosting policy

This folder is the **only** place where files from third parties may be hosted in this
repo. Everything else in the repo is links to the original sources.

## Rules

1. A file may be added here **only** with a license that explicitly allows
   redistribution and attribution as needed: CC0, public domain, MIT, BSD, Apache-2.0,
   CC BY / CC BY-SA (attribution!), or a copyleft license for code (GPL/AGPL/LGPL).
2. Every hosted file **must** be listed in [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md)
   with: file, source URL, license, author.
3. Never add: copyrighted books/PDFs, annotated games from commercial databases,
   bulk dumps from chessgames.com / chess.com, paid puzzles, unlicensed images,
   or curated PGN collections from other sites (link to them instead — see
   [category 2](../categories/02-game-databases-and-pgn.md)).
4. Prefer **small, useful samples** over giant dumps (GitHub file-size limits and
   kindness to cloners). Big datasets stay at their source (e.g. lichess dumps).

## What goes where

```
data/
├── README.md            ← this policy
├── downloads/           ← git-ignored; filled locally by scripts/fetch-pgn.sh
└── <topic>/             ← hosted files with permissive licenses only,
    └── LICENSE or NOTICE per subfolder
```

## Good candidates for hosting (with license check)

- CC0/public-domain piece sets (e.g. lichess sets that are PD)
- The `lichess-org/chess-openings` ECO dataset (open data)
- Small public-domain PGN samples from Project Gutenberg books
- Your own CC0-licensed tools/configs
