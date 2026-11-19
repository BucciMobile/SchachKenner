#!/usr/bin/env python3
"""Split the hosted CC0 lichess PGN sample into sensible groups.

Reads:  data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn
Writes: data/pgn/lichess/groups/<criterion>/<group>.pgn  +  groups/README.md index

Groupings: by-opening (top 15 + other), by-eco (top 20 + other),
by-rating-band, by-time-control, by-result.

The source is CC0 (https://database.lichess.org/), so derived groups are CC0 too.
Usage:  python scripts/split-pgn.py        (run from the repo root)
"""
import os, re, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'data/pgn/lichess/lichess-standard-2026-10-sample-2000-games.pgn')
OUT = os.path.join(ROOT, 'data/pgn/lichess/groups')


def render(tags, moves):
    head = '\n'.join(f'[{k} "{v}"]' for k, v in tags.items())
    return head + '\n\n' + moves + '\n'


def parse_games(path):
    games, cur_tags, cur_moves = [], {}, []

    def flush():
        if cur_tags or cur_moves:
            games.append((dict(cur_tags), ' '.join(cur_moves).strip()))

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
    if base < 180:
        return 'bullet'
    if base < 480:
        return 'blitz'
    if base < 1500:
        return 'rapid'
    return 'classical'


GROUPS = {
    'by-opening': lambda t: t.get('Opening', 'unknown'),
    'by-eco': lambda t: t.get('ECO', 'no-eco'),
    'by-rating-band': rating_band,
    'by-time-control': tc_class,
    'by-result': lambda t: {'1-0': 'white-wins-1-0', '0-1': 'black-wins-0-1',
                            '1/2-1/2': 'draws', '*': 'other'}.get(t.get('Result', '*'), 'other'),
}
TOP = {'by-opening': 15, 'by-eco': 20}   # keep top-N named groups, rest -> other.pgn


def main():
    games = parse_games(SRC)
    print('games parsed:', len(games))
    index = defaultdict(list)

    for crit, fn in GROUPS.items():
        buckets = defaultdict(list)
        for tags, moves in games:
            buckets[fn(tags)].append((tags, moves))
        top = set()
        if crit in TOP:
            top = {k for k, _ in Counter(buckets.keys()).most_common(TOP[crit])}

        def label_of(key):
            if crit not in TOP or key in top:
                return key
            return 'other'

        os.makedirs(os.path.join(OUT, crit), exist_ok=True)
        files = defaultdict(list)  # label -> [(tags, moves)]
        for key, items in buckets.items():
            files[label_of(key)].extend(items)
        for label, items in files.items():
            path = os.path.join(OUT, crit, slug(label) + '.pgn')
            with open(path, 'w', encoding='utf-8') as f:
                for tags, moves in items:
                    f.write(render(tags, moves) + '\n')
            index[crit].append((label, f'{crit}/{slug(label)}.pgn', len(items)))
        print(crit, '->', len(files), 'groups')

    total = len(games)
    lines = ['# Grouped samples — lichess CC0 (2,000 games, 2026-10 export)', '',
             f'Derived from [`../lichess-standard-2026-10-sample-2000-games.pgn`](../lichess-standard-2026-10-sample-2000-games.pgn)',
             '(CC0 — see [`licenses/lichess-database-cc0.md`](../../../licenses/lichess-database-cc0.md)).',
             'Regenerate with `python scripts/split-pgn.py` (from the repo root).', '']
    for crit in ['by-opening', 'by-eco', 'by-rating-band', 'by-time-control', 'by-result']:
        lines += [f'## {crit} ({sum(c for _, _, c in index[crit])} games)', '',
                  '| Group | Games | File |', '|---|---|---|']
        for label, file, cnt in sorted(index[crit], key=lambda x: -x[2]):
            lines.append(f'| {label} | {cnt} ({cnt / total:.1%}) | [`{file.split("/")[-1]}`](../{file}) |')
        lines.append('')
    with open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('index written:', os.path.join(OUT, 'README.md'))


if __name__ == '__main__':
    main()
