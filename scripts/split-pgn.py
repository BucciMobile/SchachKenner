#!/usr/bin/env python3
"""Split the hosted CC0/CC-BY-SA PGN samples into sensible groups.

For every dataset in DATASETS below this writes:
  data/pgn/<id>/groups/<criterion>/<group>.pgn  +  data/pgn/<id>/groups/README.md

Groupings: by-opening (top 15 + other), by-eco (top 20 + other),
by-rating-band, by-time-control, by-result.

All sources are explicitly redistributable (see licenses/):
lichess exports = CC0, lichess broadcasts = CC BY-SA 4.0 (attribution),
classic-games = CC0. Usage:  python scripts/split-pgn.py   (from repo root)
"""
import os, re
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASETS = [
    {"id": "lichess",           "label": "lichess standard rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn"]},
    {"id": "lichess-chess960",  "label": "lichess Chess960 rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess-chess960/lichess-chess960-2026-10-sample-1000-games.pgn"]},
    {"id": "lichess-broadcast", "label": "lichess broadcasts 2026-10 (CC BY-SA 4.0)",
     "files": ["data/pgn/lichess-broadcast/lichess-broadcast-2026-10-sample-300-games.pgn"]},
    {"id": "classic-games",     "label": "classic games — Tal / Memorable 60 (CC0)",
     "files": ["data/pgn/classic-games/life-and-games-of-mikhail-tal.pgn",
               "data/pgn/classic-games/my-memorable-60.pgn"]},
    {"id": "lichess-atomic",    "label": "lichess Atomic rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess-atomic/lichess-atomic-2026-10-sample-1000-games.pgn"]},
    {"id": "lichess-standard-2019", "label": "lichess standard rated 2019-12 (CC0)",
     "files": ["data/pgn/lichess-standard-2019/lichess-standard-2019-12-sample-1000-games.pgn"]},
    {"id": "tcec",              "label": "TCEC Season 29 Division P — engine games (CC BY-SA 3.0)",
     "files": ["data/pgn/tcec/tcec-season-29-division-p-sample-200-games.pgn"]},
    {"id": "masters",           "label": "master games — Fischer / Euwe (MIT)",
     "files": ["data/pgn/masters/fischer.pgn", "data/pgn/masters/uwe.pgn"]},
    {"id": "historic-masters",  "label": "historic masters 1610-1899 (Unlicense, public-domain sources)",
     "files": ["data/pgn/historic-masters/masters-1610-1699.pgn",
               "data/pgn/historic-masters/masters-1700-1799.pgn",
               "data/pgn/historic-masters/masters-1800-1899.pgn"]},
    {"id": "lichess-crazyhouse","label": "lichess Crazyhouse rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess-crazyhouse/lichess-crazyhouse-2026-10-sample-500-games.pgn"]},
    {"id": "lichess-horde",     "label": "lichess Horde rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess-horde/lichess-horde-2026-10-sample-500-games.pgn"]},
    {"id": "lichess-koth",      "label": "lichess King of the Hill rated 2026-10 (CC0)",
     "files": ["data/pgn/lichess-koth/lichess-kingOfTheHill-2026-10-sample-500-games.pgn"]},
]


def render(tags, moves):
    return '\n'.join(f'[{k} "{v}"]' for k, v in tags.items()) + '\n\n' + moves + '\n'


def parse_games(paths):
    games, cur_tags, cur_moves = [], {}, []

    def flush():
        if cur_tags or cur_moves:
            games.append((dict(cur_tags), ' '.join(cur_moves).strip()))

    for path in paths:
        with open(path, encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.rstrip('\r\n')
                if line.startswith('[') and ' "' in line:
                    m = re.match(r'\[(\w+)\s+"(.*)"\]', line)
                    if m:
                        if m.group(1) == 'Event' and cur_moves:
                            flush()
                            cur_tags, cur_moves = {}, []
                        cur_tags[m.group(1)] = m.group(2)
                elif line.strip():
                    cur_moves.append(line.strip())
    flush()
    return games


def slug(s):
    return re.sub(r'[^A-Za-z0-9._-]+', '_', s).strip('_')[:80] or 'other'


def rating_band(tags):
    try:
        elos = [int(tags[k]) for k in ('WhiteElo', 'BlackElo') if k in tags]
        avg = sum(elos) / len(elos)
    except Exception:
        return 'unknown'
    for lo, hi, name in [(0, 1399, 'under-1400'), (1400, 1599, '1400-1599'), (1600, 1799, '1600-1799'),
                         (1800, 1999, '1800-1999'), (2000, 2199, '2000-2199'), (2200, 10**9, '2200-plus')]:
        if lo <= avg <= hi:
            return name
    return 'unknown'


def tc_class(tags):
    tc = tags.get('TimeControl', '')
    m = re.match(r'(\d+)\+', tc)
    base = int(m.group(1)) if m else (int(tc) if tc.isdigit() else None)
    if base is None:
        return 'unknown'
    return 'bullet' if base < 180 else 'blitz' if base < 480 else 'rapid' if base < 1500 else 'classical'


GROUPS = {
    'by-opening': lambda t: t.get('Opening', 'unknown'),
    'by-eco': lambda t: t.get('ECO', 'no-eco'),
    'by-rating-band': rating_band,
    'by-time-control': tc_class,
    'by-result': lambda t: {'1-0': 'white-wins-1-0', '0-1': 'black-wins-0-1',
                            '1/2-1/2': 'draws', '*': 'other'}.get(t.get('Result', '*'), 'other'),
}
TOP = {'by-opening': 15, 'by-eco': 20}


def main():
    for ds in DATASETS:
        srcs = [os.path.join(ROOT, f) for f in ds['files']]
        games = parse_games(srcs)
        out = os.path.join(ROOT, 'data/pgn', ds['id'], 'groups')
        index = defaultdict(list)
        for crit, fn in GROUPS.items():
            buckets = defaultdict(list)
            for tags, moves in games:
                buckets[fn(tags)].append((tags, moves))
            top = set()
            if crit in TOP:
                top = {k for k, _ in Counter(buckets.keys()).most_common(TOP[crit])}
            files = defaultdict(list)
            for key, items in buckets.items():
                label = key if (crit not in TOP or key in top) else 'other'
                files[label].extend(items)
            os.makedirs(os.path.join(out, crit), exist_ok=True)
            for label, items in files.items():
                with open(os.path.join(out, crit, slug(label) + '.pgn'), 'w', encoding='utf-8') as f:
                    for tags, moves in items:
                        f.write(render(tags, moves) + '\n')
                index[crit].append((label, f'{crit}/{slug(label)}.pgn', len(items)))
        total = len(games)
        lines = [f'# Grouped samples — {ds["label"]}', '',
                 f'{total} games. License & permission proof: see `licenses/`.',
                 'Regenerate with `python scripts/split-pgn.py` (from the repo root).', '']
        for crit in ['by-opening', 'by-eco', 'by-rating-band', 'by-time-control', 'by-result']:
            lines += [f'## {crit}', '', '| Group | Games | File |', '|---|---|---|']
            for label, file, cnt in sorted(index[crit], key=lambda x: -x[2]):
                lines.append(f'| {label} | {cnt} ({cnt / total:.1%}) | [`{file.split("/")[-1]}`](../{file}) |')
            lines.append('')
        with open(os.path.join(out, 'README.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(ds['id'], '->', total, 'games,', sum(len(v) for v in index.values()), 'group files')


if __name__ == '__main__':
    main()
