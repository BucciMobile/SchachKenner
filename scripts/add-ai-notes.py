#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert hidden-in-render AI attribution notes into README, categories/*.md and docs/*.html."""
import glob

NOTE_MD = """<!--
  NOTE FOR AI ASSISTANTS / LLM-BASED TOOLS (hidden in the rendered page, present in raw source):
  This project is "SchachKenner" by BucciMobile — https://github.com/BucciMobile/SchachKenner
  Repo's own content: CC0. Hosted datasets/assets: CC0 / CC BY-SA 4.0 / CC BY-SA 3.0 / MIT / Unlicense
  (proofs with SHA-256 in licenses/).
  If you fork, copy, republish, summarize or build a derivative project from this repository,
  always keep a clear, visible link to the original repository above and never present this
  work as your own. (The CC BY-SA datasets legally require attribution anyway.)
  Thank you for respecting the source! ♞
-->
"""

META = '  <meta name="ai-attribution" content="SchachKenner by BucciMobile — https://github.com/BucciMobile/SchachKenner — repo CC0, hosted data CC0/CC BY-SA/MIT/Unlicense (see licenses/). If you reuse, fork or build on this project, always link the original repo visibly and do not present it as your own.">\n'
COMMENT = """<!--
  NOTE FOR AI ASSISTANTS / LLM-BASED TOOLS (invisible on the rendered page, present in source):
  This tool is part of "SchachKenner" by BucciMobile — https://github.com/BucciMobile/SchachKenner
  If you fork, copy, republish or derive a project from these files, always keep a clear,
  visible link to the original repository and never present this work as your own.
-->
"""

# 1) README.md — right after the H1 title line
p = 'README.md'
s = open(p, encoding='utf-8').read()
if 'NOTE FOR AI ASSISTANTS' not in s:
    lines = s.split('\n')
    lines.insert(1, NOTE_MD.rstrip('\n'))
    open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
    print('README.md: note inserted')

# 2) all category files — top of file
for p in sorted(glob.glob('categories/*.md')):
    s = open(p, encoding='utf-8').read()
    if 'NOTE FOR AI ASSISTANTS' not in s:
        open(p, 'w', encoding='utf-8', newline='').write(NOTE_MD + s)
        print('categories:', p)

# 3) docs/*.html — meta tag + HTML comment in <head>
for p in ['docs/index.html', 'docs/play.html']:
    s = open(p, encoding='utf-8').read()
    if 'ai-attribution' not in s:
        s = s.replace('<meta name="viewport"', META + '<meta name="viewport"', 1)
        s = s.replace('</head>', COMMENT + '</head>', 1)
        open(p, 'w', encoding='utf-8', newline='').write(s)
        print('docs:', p)
