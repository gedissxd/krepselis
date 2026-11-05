import re, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from parse import barbora, rimi
from rules import RULES, COMMON_X, DRAINED
def pack_grams(p, key):
    n = p["name"]
    if key == "eggs":
        m = re.search(r"(\d+)\s*vnt", n); return int(m.group(1))*60 if m else None
    if key in DRAINED:
        m = re.search(r"/\s*(\d+)\s*g", n)
        if m: return float(m.group(1))
    if p["unit"] > 0 and p["uu"] in ("kg","l"):
        g = p["price"]/p["unit"]*1000
        if key in DRAINED: g *= 0.6
        if key in ("olive","rapeseed"): g *= 0.92
        return round(g)
    return None
def candidates(L, key):
    inc, exc, uu = RULES[key]
    out = []
    for p in L:
        n = p["name"].lower()
        if not all(re.search(r, n) for r in inc): continue
        if re.search(exc, n) or re.search(COMMON_X, n): continue
        if not re.fullmatch(uu, p["uu"].rstrip(".")): continue
        g = pack_grams(p, key)
        if not g or g < 50: continue
        out.append(dict(p, g=g, per_kg=round(p["price"]/g*1000, 2)))
    return sorted(out, key=lambda x: x["per_kg"])
if __name__ == "__main__":
    d = sys.argv[1]; res = {}
    for st, fn in (("barbora", barbora), ("rimi", rimi)):
        res[st] = {}
        for key in RULES:
            c = candidates(fn(f"{d}/{st}_{key}.html"), key)
            res[st][key] = c[:8]
    json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    for key in RULES:
        for st in res:
            c = res[st][key]
            print(f"{key:9} {st:7} " + (" | ".join(f"{x['price']:.2f}€ {x['g']}g {x['name'][:48]}" for x in c[:2]) if c else "-- NONE --"))
