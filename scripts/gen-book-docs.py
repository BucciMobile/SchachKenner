#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate data/books/README.md and licenses/books-public-domain.md from scripts/books-manifest.json."""
import json, os

ROOT = os.path.join(os.path.dirname(__file__), "..")
m = json.load(open(os.path.join(ROOT, "scripts", "books-manifest.json"), encoding="utf-8"))

LANGS = {"en": "English", "de": "Deutsch", "fr": "Français", "es": "Español", "it": "Italiano",
         "ru": "Русский", "pt": "Português", "sv": "Svenska"}

# ---------- data/books/README.md ----------
lines = ["# data/books/ — freely licensed chess books (hosted)",
         "",
         "Full-text chess books whose copyright has **expired** (all published ≤ 1929 → public domain",
         "in the US; most items additionally carry an explicit **Public Domain Mark 1.0** on the Internet",
         "Archive). License evidence per book: [`licenses/books-public-domain.md`](../licenses/books-public-domain.md)",
         "+ raw archive.org metadata in [`licenses/raw/`](raw/) (SHA-256 below).",
         "",
         "Regenerate with `python scripts/fetch-books.py` (manifest: `scripts/books-manifest.json`).",
         ""]
total = sum(b["bytes"] + (b.get("pdf_bytes") or 0) for b in m)
lines.append(f"**{len(m)} books, {total/1e6:.1f} MB total, {len(set(b['lang'] for b in m))} languages.**")
lines.append("")
lines.append("Each book is hosted as a **scan PDF with the original page images / chess diagrams** (`<id>.pdf`)")
lines.append("plus the OCR **plain text** (`<id>.txt`, or `.docx` where archive.org offers no text file) for")
lines.append("full-text search. Chess books are useless without their diagrams — the PDFs are the primary format.")
lines.append("")
for lang in sorted(set(b["lang"] for b in m), key=lambda l: LANGS.get(l, l)):
    lines.append(f"## {LANGS.get(lang, lang)} (`{lang}/`)")
    lines.append("")
    lines.append("| Book | Author | Year | PDF (scan, with diagrams) | Plain text | Source |")
    lines.append("|---|---|---|---|---|---|")
    for b in sorted([x for x in m if x["lang"] == lang], key=lambda x: x["year"]):
        fn = os.path.basename(b["file"])
        if b.get("pdf_file"):
            pfn = os.path.basename(b["pdf_file"])
            pdf = f"[`{pfn}`]({lang}/{pfn}) `{b['pdf_sha256'][:16]}…`"
            if b.get("pdf_bytes", 0) < 1_000_000:
                pdf += " (text-layer PDF — archive.org has no scan PDF for this item)"
        else:
            pdf = "— (no PDF on archive.org; hosted as .docx)"
        lines.append(f"| {b['title']} | {b['author']} | {b['year']} | {pdf} | [`{fn}`]({lang}/{fn}) `{b['sha256'][:16]}…` | [archive.org]({b['source']}) |")
    lines.append("")
open(os.path.join(ROOT, "data", "books", "README.md"), "w", encoding="utf-8").write("\n".join(lines))

# ---------- licenses/books-public-domain.md ----------
L = ["# Chess books — public-domain evidence (Internet Archive) ✅ HOSTED",
     "",
     "All books hosted in `data/books/` were retrieved from the **Internet Archive** on **2026-11-20 (UTC)**.",
     "",
     "## Why these books are public domain",
     "",
     "1. **Age rule:** every book was first published **≤ 1929**. In the US, works published before 1930",
     "   are in the public domain (95-year term has long expired; 17 U.S.C. §302).",
     "2. **Explicit mark:** most items additionally carry the license field",
     "   `licenseurl = http(s)://creativecommons.org/publicdomain/mark/1.0/` (**Public Domain Mark 1.0**)",
     "   in their archive.org metadata — i.e. the uploader explicitly dedicates the scan to the public domain.",
     "   The raw metadata JSON of every item is preserved in [`raw/`](raw/) as `ia-<id>.metadata.json`.",
     "",
     "   (Capablanca's *Chess Fundamentals*, 1921 item `chessfundamental00capa`, has no license field but is",
     "   PD by the age rule; archive.org also hosts PD-marked copies of the same work,",
     "   e.g. `chess-fundamentals-jose-raul-capablanca-berserker-books-final` with `publicdomain/mark/1.0`.)",
     "",
     "## Hosted files (SHA-256 of each hosted file: scan PDF + plain text, retrieved 2026-11-20 UTC)",
     "",
     "| Lang | Book (year) | Hosted files | SHA-256 | IA item | licenseurl |",
     "|---|---|---|---|---|---|"]
for b in sorted(m, key=lambda x: (x["lang"], x["year"])):
    if b.get("pdf_file"):
        files = f"`{b['file']}`<br>`{b['pdf_file']}`"
        shas = f"`{b['sha256']}`<br>`{b['pdf_sha256']}`"
    else:
        files = f"`{b['file']}`"
        shas = f"`{b['sha256']}`"
    L.append(f"| {b['lang']} | {b['title']} ({b['year']}) | {files} | {shas} | [details/{b['id']}]({b['source']}) | {b['licenseurl'] or '— (PD by age, pre-1930)'} |")
L += ["",
      "## Rule for future additions",
      "",
      "A book may be hosted in `data/books/` only if **either** its archive.org/Gutenberg metadata carries an",
      "explicit PD/CC0 license field, **or** it was first published ≤ 1929 (PD in the US by age) — with the raw",
      "metadata saved to `licenses/raw/` and the SHA-256 of the hosted file listed above. Everything else: link only.",
      "",
      "## Deliberately NOT listed (scam warning)",
      "",
      "We do **not** list 'free book — you only pay shipping' offers or shops that sell public-domain books as",
      "if they were their own copyrighted product. Only genuine PD/CC sources (and publisher pages that give the",
      "file away for free) are linked in `categories/09-books-and-learning.md`.",
      ""]
open(os.path.join(ROOT, "licenses", "books-public-domain.md"), "w", encoding="utf-8").write("\n".join(L))
print("written: data/books/README.md + licenses/books-public-domain.md,", len(m), "books")
