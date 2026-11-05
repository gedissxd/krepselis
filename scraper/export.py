"""Turn picks.json (from pick.py) into the PRICES constant used by src/app.html."""
import json, sys, datetime
d = json.load(open(sys.argv[1], encoding="utf8"))
out = {"date": sys.argv[3] if len(sys.argv) > 3 else datetime.date.today().isoformat()}
for st, name in (("barbora", "maxima"), ("rimi", "rimi")):
    out[name] = {k: [[v["name"], v["price"], int(round(v["g"])), v["url"]] for v in c] for k, c in d[st].items() if c}
json.dump(out, open(sys.argv[2], "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
print({s: len(out[s]) for s in ("maxima", "rimi")})
