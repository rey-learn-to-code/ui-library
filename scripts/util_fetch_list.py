"""Download URLs listed as JSON [[url, dest_path], ...] with gentle concurrency.
Usage: python3 -I util_fetch_list.py <jobs.json>"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
jobs = json.load(open(sys.argv[1]))
def get(job):
    url, dest = job
    if os.path.exists(dest) and os.path.getsize(dest) > 0: return "skip"
    for a in range(4):
        try:
            req = urllib.request.Request(urllib.parse.quote(url, safe=":/?=&%"), headers={"User-Agent": "ui-library-toolkit/1.0"})
            data = urllib.request.urlopen(req, timeout=60).read()
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "wb").write(data); time.sleep(0.2); return "ok"
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(5*(a+1)); continue
            return f"http {e.code} {url}"
        except Exception as e:
            time.sleep(2)
    return f"fail {url}"
import urllib.parse
with ThreadPoolExecutor(3) as ex: res = list(ex.map(get, jobs))
print(len(res), [r for r in res if r not in ("ok","skip")][:10])
