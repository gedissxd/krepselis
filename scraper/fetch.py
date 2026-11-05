import sys, os, time, urllib.parse, subprocess
sys.path.insert(0, os.path.dirname(__file__)); from queries import Q
out = sys.argv[1]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
for k, q in Q.items():
    for store, url in (("barbora", "https://barbora.lt/paieska?q="), ("rimi", "https://www.rimi.lt/e-parduotuve/lt/paieska?pageSize=80&query=")):
        f = f"{out}/{store}_{k}.html"
        if os.path.exists(f) and os.path.getsize(f) > 5000: continue
        r = subprocess.run(["curl","-sS","-L","-m","30","-A",UA,"-H","Accept-Language: lt","-o",f,"-w","%{http_code}",url+urllib.parse.quote(q)],capture_output=True,text=True)
        print(store, k, r.stdout, r.stderr.strip()[:80], flush=True)
        time.sleep(1.0)
