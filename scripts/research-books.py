#!/usr/bin/env python3
"""Research freely-licensed chess books: Project Gutenberg + Internet Archive.
Prints candidate books with id/title/year/license evidence URL.
"""
import json, re, sys, urllib.request, urllib.parse

UA = {"User-Agent": "Mozilla/5.0 (SchachKenner research; github.com/BucciMobile/SchachKenner)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def ia_search(q, rows=40):
    url = ("https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({
        "q": q, "fl[]": ["identifier", "title", "year", "licenseurl", "language"],
        "rows": rows, "page": 1, "output": "json"}))
    d = json.loads(get(url))
    return d["response"]["docs"]

def gutenberg_search(query, rows=25):
    url = "https://www.gutenberg.org/ebooks/search/?query=" + urllib.parse.quote(query)
    html = get(url)
    out = []
    for m in re.finditer(r'href="(/ebooks/(\d+)/?)"[^>]*>(.*?)</a>', html, re.S):
        title = re.sub(r"<[^>]+>", "", m.group(3)).strip()
        out.append((int(m.group(2)), title))
    seen, res = set(), []
    for bid, t in out:
        if bid not in seen:
            seen.add(bid); res.append((bid, t))
    return res[:rows]

def main():
    print("=== Project Gutenberg — chess subject shelf (1677) first page:")
    try:
        html = get("https://www.gutenberg.org/ebooks/subject/1677")
        for m in re.finditer(r'href="(/ebooks/(\d+)/?)"[^>]*>(.*?)</a>', html, re.S)[:0]:
            pass
        ids = re.findall(r'/ebooks/(\d+)/', html)
        print("  ids:", ids[:40])
    except Exception as e:
        print("  ERR", e)

    for q in ["chess", "schach", "échecs", "ajedrez", "шахматы", "scacchi"]:
        print(f"=== Gutenberg search: {q}")
        try:
            for bid, t in gutenberg_search(q, 15):
                print("  ", bid, "|", t[:70])
        except Exception as e:
            print("   ERR", e)

    print("=== Internet Archive — PD/CC0 chess books (licenseurl contains publicdomain/zero):")
    for q in [
        'title:(chess) AND mediatype:texts AND licenseurl:*publicdomain*',
        'title:(chess) AND mediatype:texts AND licenseurl:*zero*',
        'title:(schach) AND mediatype:texts AND licenseurl:*publicdomain*',
        'title:(échecs OR echecs) AND mediatype:texts AND licenseurl:*publicdomain*',
        'title:(ajedrez) AND mediatype:texts AND licenseurl:*publicdomain*',
        'title:(шахматы OR shakhmaty) AND mediatype:texts AND licenseurl:*publicdomain*',
        'subject:"Chess" AND mediatype:texts AND year:[* TO 1929] AND licenseurl:*',
    ]:
        print("--- q:", q)
        try:
            for d in ia_search(q, 25):
                print("  ", d.get("year", "?"), "|", d["identifier"], "|", (d.get("title") or "")[:55], "|", d.get("licenseurl", ""), "|", d.get("language"))
        except Exception as e:
            print("   ERR", e)

if __name__ == "__main__":
    main()
