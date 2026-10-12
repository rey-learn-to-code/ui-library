#!/usr/bin/env python3
"""Download all ambientCG assets (CC0) in the 1K-JPG version (zips are extracted).

- Material/Decal/Atlas/Terrain/...: "1K-JPG" variant
- HDRI (no 1K-JPG): "1K" variant (1k .exr/.hdr file + tonemapped image)
- 3DModel (no 1K-JPG): "SQ-1K-JPG" variant
- Substance (.sbsar) is skipped (not usable on the web).
Safe to re-run any number of times (finished assets have a .done file and are skipped).
How to run:  python3 -I download_ambientcg.py [--limit N]
"""
import argparse, json, os, sys, time, zipfile, urllib.request, urllib.error, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "assets", "3d-materials", "ambientcg")
LOG = os.path.join(ROOT, "scripts", "logs", "ambientcg.log")
API = "https://ambientcg.com/api/v2/full_json?include=downloadData,tagData,displayData,imageData&limit=500&offset=%d"
UA = "goodstack-ui-library-3d-materials/1.0 (personal offline CC0 asset toolkit; python-urllib)"
PREFER = ["1K-JPG", "1K", "SQ-1K-JPG"]
MAX_UNZIP = 1 << 30  # 1 GB unzip limit per zip
_lock = threading.Lock()


def log(msg):
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    with _lock:
        print(line, flush=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def http_get(url, tries=6):
    delay = 5
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=180)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                ra = e.headers.get("Retry-After")
                wait = int(ra) if ra and ra.isdigit() else delay
                log("  HTTP %s, waiting %ss: %s" % (e.code, wait, url))
                time.sleep(wait); delay = min(delay * 2, 300); continue
            raise
        except Exception as e:
            if i < tries - 1:
                log("  network error (%s), retrying in %ss" % (e, delay))
                time.sleep(delay); delay = min(delay * 2, 300); continue
            raise


def download(url, dest, size=None):
    if os.path.exists(dest) and (size is None or os.path.getsize(dest) == size):
        return 0
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    with http_get(url) as r, open(tmp, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    if size and os.path.getsize(tmp) != size:
        os.remove(tmp)
        raise IOError("wrong size %s" % url)
    os.replace(tmp, dest)
    return os.path.getsize(dest)


def safe_extract(zpath, dest):
    with zipfile.ZipFile(zpath) as z:
        total = 0
        for info in z.infolist():
            n = info.filename.replace("\\", "/")
            if n.startswith("/") or ".." in n.split("/") or ":" in n:
                raise ValueError("unsafe zip path: %r" % n)
            total += info.file_size
        if total > MAX_UNZIP:
            raise ValueError("zip too large when extracted (%d bytes)" % total)
        # Skip DirectX normal maps and Blender files: websites only need NormalGL maps (saves ~6 GB).
        keep = [i for i in z.infolist() if not i.is_dir()
                and "NormalDX" not in i.filename and not i.filename.endswith(".blend")]
        z.extractall(dest, members=keep)
        return sorted(i.filename for i in keep)


def downloads_of(a):
    out = []
    df = a.get("downloadFolders")
    if not isinstance(df, dict):
        return out
    for fold in df.values():
        cats = fold.get("downloadFiletypeCategories")
        if isinstance(cats, dict):
            for c in cats.values():
                out += c.get("downloads", [])
    return out


def pick(a):
    ds = {d["attribute"]: d for d in downloads_of(a) if d.get("filetype") == "zip"}
    for p in PREFER:
        if p in ds:
            return ds[p]
    return None


def process(a):
    aid = a["assetId"]
    d = os.path.join(OUT, a["dataType"], aid)
    done = os.path.join(d, ".done")
    if os.path.exists(done):
        with open(done, encoding="utf-8") as f:
            return json.load(f), 0
    dl = pick(a)
    if not dl:
        return None, 0
    os.makedirs(d, exist_ok=True)
    zpath = os.path.join(d, dl["fileName"])
    got = download(dl["downloadLink"], zpath, dl.get("size"))
    files = safe_extract(zpath, d)
    os.remove(zpath)  # delete the zip after extracting to save space
    thumb = (a.get("previewImage") or {}).get("256-JPG-242424")
    if thumb:
        try:
            got += download(thumb, os.path.join(d, "thumb.jpg"))
            files.append("thumb.jpg")
        except Exception as e:
            log("  could not download thumbnail %s: %s" % (aid, e))
    info = {"variant": dl["attribute"], "files": [os.path.join(a["dataType"], aid, f) for f in files]}
    with open(done, "w", encoding="utf-8") as f:
        json.dump(info, f)
    return info, got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    assets, off = [], 0
    while True:
        with http_get(API % off) as r:
            page = json.loads(r.read().decode("utf-8"))
        fa = page.get("foundAssets", [])
        assets += fa
        off += len(fa)
        if not fa or off >= page.get("numberOfResults", 0):
            break
        time.sleep(1)
    log("== ambientCG: %d assets on the API" % len(assets))
    # priority: HDRI, 3DModel, Material, then the other types
    order = {"HDRI": 0, "3DModel": 1, "Material": 2}
    assets.sort(key=lambda x: (order.get(x["dataType"], 3), x["assetId"]))
    if a.limit:
        assets = assets[: a.limit]
    idx_path = os.path.join(OUT, "index.json")
    index, total, n, skipped = {}, 0, 0, 0
    with ThreadPoolExecutor(max_workers=min(a.workers, 4)) as ex:
        futs = {ex.submit(process, x): x for x in assets}
        for fu in as_completed(futs):
            x = futs[fu]; n += 1
            try:
                info, got = fu.result()
                total += got
                if info is None:
                    skipped += 1
                else:
                    index[x["assetId"]] = {
                        "id": x["assetId"], "name": x.get("displayName"), "type": x["dataType"],
                        "categories": [x.get("displayCategory")] if x.get("displayCategory") else [],
                        "tags": x.get("tags", []), "variant": info["variant"],
                        "license": "CC0-1.0", "source": x.get("shortLink"), "files": info["files"],
                    }
            except Exception as e:
                log("ERROR %s: %s" % (x["assetId"], e))
            if n % 25 == 0 or n == len(assets):
                log("%d/%d (skipped %d with no 1K version; %.1f MB newly downloaded this session)" % (n, len(assets), skipped, total / 1e6))
            if n % 200 == 0:
                write_index(idx_path, index)
    write_index(idx_path, index)
    log("DONE. %d assets in the index." % len(index))


def write_index(p, index):
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(sorted(index.values(), key=lambda e: (e["type"], e["id"])), f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)


if __name__ == "__main__":
    main()
