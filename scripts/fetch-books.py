#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download freely-licensed (public-domain) chess books from the Internet Archive
into data/books/<lang>/ and save the per-item metadata JSON (license evidence)
into licenses/raw/. Prints a manifest table with SHA-256.

Usage: python scripts/fetch-books.py
"""
import hashlib, json, os, sys, urllib.request, urllib.parse, time

ROOT = os.path.join(os.path.dirname(__file__), "..")
UA = {"User-Agent": "Mozilla/5.0 (SchachKenner research; github.com/BucciMobile/SchachKenner)"}

# id | lang | author | title | year | license evidence
BOOKS = [
    ("nimzowitsch-my-system",            "en", "Aron Nimzowitsch",    "My System (1925)",                                   "1925", "PD-mark"),
    ("lasker-s-manual-of-chess",         "en", "Emanuel Lasker",      "Lasker's Manual of Chess (1925 ed.)",                "1925", "PD-mark"),
    ("chessfundamental00capa",           "en", "José Raúl Capablanca","Chess Fundamentals",                                "1921", "pre-1930 US PD (+ PD-marked twin on IA)"),
    ("ChessMadeEasyOrTheGamesOfGioachin","en", "Gioachino Greco",     "Chess Made Easy — The Games of Greco",               "1750", "PD-mark"),
    ("TavernerChessProblemsMadeEasy",    "en", "H. Taverner",         "Chess Problems Made Easy",                           "1924", "PD-mark"),
    ("bub_gb__dwCAAAAYAAJ",               "en", "Howard Staunton",     "The Chess-Player's Companion",                       "1849", "PD-mark"),
    ("bub_gb_d69AAAAAcAAJ",               "en", "ed. Howard Staunton", "The Chess Tournament — London 1851",                 "1852", "PD-mark"),
    ("bub_gb_RicCAAAAYAAJ",               "de", "various",             "Berliner Schach-Erinnerungen (Greco & Lucena)",      "1859", "PD-mark"),
    ("blathy-vielzugige-schachaufgaben", "de", "Ottó Bláthy",         "Vielzugige Schachaufgaben (mate-in-many problems)", "1890", "PD-mark"),
    ("bub_gb_cikCAAAAYAAJ",               "fr", "François-André Philidor", "Analyse du jeu des échecs (1803 ed.)",           "1803", "PD-mark"),
    ("bub_gb_nE8UAAAAQAAJ",               "fr", "D. Legall / ed.",     "Nouveau traité du jeu des échecs",                   "1833", "PD-mark"),
    ("bub_gb_8PtlpgB4Wm4C",               "es", "Francisco D. Philopon? (ed.)", "Compendio de los elementos teóricos y prácticos del ajedrez", "1838", "PD-mark"),
    ("bub_gb_w95-78eDjFAC",               "it", "Domenico Lorenzo Ponziani", "Il giuoco degli scacchi",                      "1837", "PD-mark"),
    ("3-5_pertrov_chess",                 "ru", "Alexander Petrov",    "Шахматная игра (Schachmatnaja igra), parts III–V",    "1824", "PD-mark"),
    ("20200309_20200309_0752",            "ru", "N. N. (strategy textbook)", "Шахматы и основы их стратегии",              "1924", "PD-mark"),
    ("osensocomumnoxadrez",              "pt", "Miessen (trans.)",    "O Senso Comum no Xadrez",                            "1917", "PD-mark"),
    ("LarobokISchackForNyborjare",       "sv", "Swedish chess assoc.","Lärobok i schack för nybörjare",                      "1920", "PD-mark"),
]

def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def main():
    manifest = []
    for ident, lang, author, title, year, ev in BOOKS:
        # 1) metadata (license evidence)
        meta = json.loads(get(f"https://archive.org/metadata/{urllib.parse.quote(ident)}"))
        md = meta.get("metadata", {})
        lic = md.get("licenseurl", "")
        out_meta = os.path.join(ROOT, "licenses", "raw", f"ia-{ident}.metadata.json")
        with open(out_meta, "wb") as f:
            f.write(json.dumps(meta, ensure_ascii=False, indent=1).encode("utf-8"))
        # 2) full text file (djvu.txt preferred)
        txt_name = None
        for fn in meta.get("files", []):
            n = fn.get("name", "")
            if n.endswith("_djvu.txt"):
                txt_name = n
                break
        if not txt_name:
            for fn in meta.get("files", []):
                n = fn.get("name", "")
                if n.endswith(".txt"):
                    txt_name = n
                    break
        if not txt_name:
            print("SKIP (no txt):", ident); continue
        outdir = os.path.join(ROOT, "data", "books", lang)
        os.makedirs(outdir, exist_ok=True)
        out = os.path.join(outdir, f"{ident}.txt")
        if os.path.exists(out) and os.path.getsize(out) > 0:
            with open(out, "rb") as f:
                data = f.read()
        else:
            data = get(f"https://archive.org/download/{urllib.parse.quote(ident)}/{urllib.parse.quote(txt_name)}", binary=True)
            with open(out, "wb") as f:
                f.write(data)
        h = sha256(data)
        manifest.append(dict(id=ident, lang=lang, author=author, title=title, year=year,
                             evidence=ev, licenseurl=lic, file=os.path.relpath(out, ROOT),
                             bytes=len(data), sha256=h, source=f"https://archive.org/details/{ident}"))
        print((f"{lang} | {ident} | {len(data)//1024} KB | {title[:50]} | lic={lic}").encode("ascii", "backslashreplace").decode())
        time.sleep(1)
    with open(os.path.join(ROOT, "scripts", "books-manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("\nmanifest written: scripts/books-manifest.json,", len(manifest), "books")

if __name__ == "__main__":
    main()
