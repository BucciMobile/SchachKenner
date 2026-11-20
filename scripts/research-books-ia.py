#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Internet Archive research: freely-licensed chess books in many languages."""
import json, sys, urllib.request, urllib.parse

UA = {"User-Agent": "Mozilla/5.0 (SchachKenner research; github.com/BucciMobile/SchachKenner)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")

def ia(q, rows=50):
    fl = ["identifier", "title", "year", "licenseurl", "language", "collection"]
    qs = "q=" + urllib.parse.quote(q) + "&" + "&".join("fl[]=" + f for f in fl) + f"&rows={rows}&output=json"
    url = "https://archive.org/advancedsearch.php?" + qs
    return json.loads(get(url))["response"]["docs"]

QUERIES = [
    # PD/CC0-marked chess books, any language
    'chess AND mediatype:texts AND licenseurl:*publicdomain*',
    'chess AND mediatype:texts AND licenseurl:*zero*',
    'schach AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    'echecs AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    'ajedrez AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    'scacchi AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    'шахматы AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    'xadrez AND mediatype:texts AND (licenseurl:*publicdomain* OR licenseurl:*zero*)',
    # old books (pre-1930 => PD in US) in the gutenberg mirror collection
    'collection:gutenberg AND chess',
    'collection:gutenberg AND schach',
    'collection:gutenberg AND echecs',
    'collection:gutenberg AND ajedrez',
    'collection:gutenberg AND шахматы',
]

seen = set()
for q in QUERIES:
    print("### q:", q, file=sys.stderr)
    try:
        for d in ia(q):
            key = d["identifier"]
            if key in seen:
                continue
            seen.add(key)
            print("|".join([
                str(d.get("year", "?")),
                key,
                (d.get("title") or "")[:70].replace("\n", " "),
                str(d.get("language", "")),
                d.get("licenseurl", ""),
            ]))
    except Exception as e:
        print("ERR", q, e, file=sys.stderr)
