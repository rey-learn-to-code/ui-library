"""Pre-generate DiceBear avatars (CC0 / MIT styles only) via the public HTTP API.
Usage: python3 -I util_dicebear_avatars.py <out_dir>
"""
import json, os, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor

OUT = sys.argv[1]
STYLES = {  # style: license of the artwork
    "lorelei": "CC0 1.0", "notionists": "CC0 1.0", "open-peeps": "CC0 1.0",
    "pixel-art": "CC0 1.0", "thumbs": "CC0 1.0", "shapes": "CC0 1.0",
    "identicon": "CC0 1.0", "rings": "CC0 1.0", "glass": "CC0 1.0",
    "initials": "MIT (code-generated, no artwork)",
}
SEEDS = ["An Nguyen", "Binh Tran", "Chi Le", "Dung Pham", "Giang Hoang", "Ha Vu", "Hieu Dang",
         "Hoa Bui", "Khanh Do", "Lan Ngo", "Long Duong", "Mai Ly", "Minh Truong", "Nam Dinh",
         "Ngoc Phan", "Phuong Ha", "Quan Vo", "Thao Lam", "Trang Mai", "Viet Cao"]

def fetch(style, seed):
    slug = seed.lower().replace(" ", "-")
    path = os.path.join(OUT, style, slug + ".svg")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path, "skip"
    url = f"https://api.dicebear.com/9.x/{style}/svg?seed=" + urllib.parse.quote(seed)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ui-library-toolkit/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(data)
            time.sleep(0.25)
            return path, "ok"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5 * (attempt + 1)); continue
            return path, f"http {e.code}"
        except Exception as e:
            time.sleep(2); err = str(e)
    return path, "fail"

jobs = [(s, seed) for s in STYLES for seed in SEEDS]
with ThreadPoolExecutor(max_workers=3) as ex:
    res = list(ex.map(lambda a: fetch(*a), jobs))
bad = [r for r in res if r[1] not in ("ok", "skip")]
index = {"api": "https://api.dicebear.com/9.x/<style>/svg?seed=<seed>",
         "styles": {s: {"license": STYLES[s], "count": len(SEEDS)} for s in STYLES},
         "seeds": SEEDS}
with open(os.path.join(OUT, "index.json"), "w") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
print("total", len(res), "errors", len(bad), bad[:5])
