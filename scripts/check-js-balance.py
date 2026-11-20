import re, sys

def strip_strings(sc):
    sc = re.sub(r"//[^\n]*", "", sc)
    sc = re.sub(r"/\*.*?\*/", "", sc, flags=re.S)
    sc = re.sub(r"'(?:\\.|[^'\\\n])*'", "''", sc)
    sc = re.sub(r'"(?:\\.|[^"\\\n])*"', '""', sc)
    sc = re.sub(r"`(?:\\.|[^`\\])*`", "``", sc, flags=re.S)
    return sc

ok_all = True
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", s, re.S)
    for i, sc in enumerate(scripts):
        sc2 = strip_strings(sc)
        bal = {c: sc2.count(c) for c in "{}()[]"}
        ok = bal["{"] == bal["}"] and bal["("] == bal[")"] and bal["["] == bal["]"]
        ok_all = ok_all and ok
        print(f, "script", i, "len", len(sc), bal, "OK" if ok else "MISMATCH")
print("ALL OK" if ok_all else "PROBLEMS FOUND")
