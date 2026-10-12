"""Download 3dicons V1 (CC0) from the public CDN listed in the realvjy/3dicons repo.
Usage: python3 -I download_3dicons_v1.py <meta_dir> <out_dir>"""
import sys, os, re, json, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
meta, out = sys.argv[1], sys.argv[2]
B = "https://3dicons.sgp1.cdn.digitaloceanspaces.com/v1"
ANGLES, STYLES = ["dynamic", "front", "iso"], ["clay", "gradient", "color", "premium"]
index, jobs = [], []
for f in sorted(os.listdir(meta)):
    t = open(os.path.join(meta, f), encoding="utf-8").read()
    g = lambda k: (re.search(rf"^{k}:\s*(.*)$", t, re.M) or [None, ""])[1].strip()
    slug = g("file-slug")
    if not slug: continue
    files = {}
    for a in ANGLES:
        for s in STYLES:
            rel = f"{a}/{s}/{slug}-{a}-{s}.png"
            files[f"{a}-{s}"] = rel
            jobs.append((f"{B}/{rel}", os.path.join(out, rel)))
    index.append({"slug": slug, "title": g("title"), "category": g("category"), "files": files})
def get(j):
    url, dst = j
    if os.path.exists(dst) and os.path.getsize(dst) > 0: return 0
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                open(dst, "wb").write(r.read()); return 0
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(5 * (i + 1)); continue
            if e.code == 404: return url
        except Exception: time.sleep(2 * (i + 1))
    return url
with ThreadPoolExecutor(4) as ex: fails = [x for x in ex.map(get, jobs) if x]
json.dump({"license": "CC0-1.0", "source": "https://github.com/realvjy/3dicons", "count_icons": len(index),
           "count_images": len(jobs) - len(fails), "missing": fails, "icons": index},
          open(os.path.join(out, "index.json"), "w"), ensure_ascii=False, indent=1)
print(len(index), "icons;", len(jobs) - len(fails), "ok;", len(fails), "fail")
