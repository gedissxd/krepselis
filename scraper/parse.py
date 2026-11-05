import re, json, html, os, sys
def barbora(path):
    s = open(path, encoding="utf8").read()
    m = re.search(r'window\.b_productList = (\[.*?\]);\s*\n', s, re.S)
    if not m: return []
    out = []
    for p in json.loads(m.group(1)):
        if p.get("status") != "active": continue
        out.append(dict(name=p["title"], price=float(p["price"]), unit=float(p.get("comparative_unit_price") or 0), uu=p.get("comparative_unit") or "",
                        url="https://barbora.lt/produktai/" + (p.get("Url") or "")))
    return out
def rimi(path):
    s = open(path, encoding="utf8").read()
    out = []
    for blk in s.split('class="product-grid__item"')[1:]:
        m = re.search(r"data-gtm-eec-product='([^']*)'", blk)
        if not m: continue
        d = json.loads(html.unescape(m.group(1)))
        if "card__price-wrapper" not in blk and "price-tag" not in blk: continue   # out of stock cards have no price
        u = re.search(r'Kaina už vienetą:\s*([\d,]+)\s*€/(\w+)', blk)
        href = re.search(r'href="(/e-parduotuve/lt/produktai/[^"]+)"', blk)
        out.append(dict(name=d["name"], price=float(d["price"]), unit=float(u.group(1).replace(",", ".")) if u else 0, uu=u.group(2) if u else "",
                        url="https://www.rimi.lt" + href.group(1) if href else ""))
    return out
if __name__ == "__main__":
    d = sys.argv[1]; keys = sys.argv[2].split(",")
    for k in keys:
        for st, fn in (("barbora", barbora), ("rimi", rimi)):
            L = fn(f"{d}/{st}_{k}.html")
            print(f"== {k} {st} ({len(L)})")
            for p in L[:int(sys.argv[3]) if len(sys.argv)>3 else 10]: print(f"   {p['price']:6.2f}  {p['unit']:6.2f}/{p['uu']:3} {p['name'][:70]}")
