#!/usr/bin/env python3
"""Download all Poly Haven assets (CC0) at 1k resolution.

- HDRIs: <id>_1k.hdr + tonemapped .jpg image
- Textures: 1k jpg maps (diff, nor_gl, rough, arm, ao, disp)
- Models: 1k gltf + .bin + 1k textures
Safe to re-run any number of times (skips files that are already fully downloaded).
How to run:  python3 -I download_polyhaven.py [--limit N] [--types hdris,textures,models]
"""
import argparse, json, os, sys, time, urllib.request, urllib.error, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "assets", "3d-materials", "polyhaven")
LOG = os.path.join(ROOT, "scripts", "logs", "polyhaven.log")
API = "https://api.polyhaven.com"
UA = "goodstack-ui-library-3d-materials/1.0 (personal offline CC0 asset toolkit; python-urllib)"
TEX_MAPS = ["Diffuse", "nor_gl", "Rough", "arm", "AO", "Displacement"]
_lock = threading.Lock()
FULL_TONEMAPPED = False


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
            return urllib.request.urlopen(req, timeout=120)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                ra = e.headers.get("Retry-After")
                wait = int(ra) if ra and ra.isdigit() else delay
                log("  HTTP %s, waiting %ss: %s" % (e.code, wait, url))
                time.sleep(wait); delay = min(delay * 2, 300); continue
            raise
        except Exception as e:  # network errors
            if i < tries - 1:
                log("  network error (%s), retrying in %ss" % (e, delay))
                time.sleep(delay); delay = min(delay * 2, 300); continue
            raise


def get_json(url):
    with http_get(url) as r:
        return json.loads(r.read().decode("utf-8"))


def download(url, dest, size=None):
    """Download a file; skip it if it already exists with the right size. Returns the number of newly downloaded bytes."""
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
    if size is not None and os.path.getsize(tmp) != size:
        os.remove(tmp)
        raise IOError("wrong size %s" % url)
    os.replace(tmp, dest)
    return os.path.getsize(dest)


def safe_rel(p):
    p = p.replace("\\", "/")
    if p.startswith("/") or ".." in p.split("/"):
        raise ValueError("unsafe path: %r" % p)
    return p


def plan_asset(kind, aid, files):
    """Return a list of (url, rel_path, size)."""
    jobs = []
    if kind == "hdris":
        h = files.get("hdri", {}).get("1k", {}).get("hdr")
        if h:
            jobs.append((h["url"], "%s_1k.hdr" % aid, h.get("size")))
        t = files.get("tonemapped")
        if FULL_TONEMAPPED and t:  # full-res version ~24MB/file, off by default
            jobs.append((t["url"], "%s_tonemapped.jpg" % aid, t.get("size")))
        else:  # 1024px tonemapped jpg preview (~100KB) from the Poly Haven CDN
            jobs.append(("https://cdn.polyhaven.com/asset_img/primary/%s.png?format=jpeg&width=1024" % aid,
                         "%s_tonemapped_1024.jpg" % aid, None))
    elif kind == "textures":
        for m in TEX_MAPS:
            j = files.get(m, {}).get("1k", {}).get("jpg")
            if j:
                jobs.append((j["url"], safe_rel(j["url"].rsplit("/", 1)[1]), j.get("size")))
        jobs.append(("https://cdn.polyhaven.com/asset_img/thumbs/%s.png?width=256" % aid, "thumb.png", None))
    elif kind == "models":
        g = files.get("gltf", {}).get("1k", {}).get("gltf")
        if g:
            jobs.append((g["url"], safe_rel(g["url"].rsplit("/", 1)[1]), g.get("size")))
            for rel, inc in g.get("include", {}).items():
                jobs.append((inc["url"], safe_rel(rel), inc.get("size")))
        jobs.append(("https://cdn.polyhaven.com/asset_img/thumbs/%s.png?width=256" % aid, "thumb.png", None))
    return jobs


def process(kind, aid, meta):
    d = os.path.join(OUT, kind, aid)
    done = os.path.join(d, ".done")
    fcache = os.path.join(d, "_files.json")
    if os.path.exists(done) and os.path.exists(fcache):
        with open(fcache, encoding="utf-8") as f:
            jobs = plan_asset(kind, aid, json.load(f))
        return [os.path.join(kind, aid, r) for _, r, _ in jobs], 0
    os.makedirs(d, exist_ok=True)
    files = get_json("%s/files/%s" % (API, aid))
    with open(fcache, "w", encoding="utf-8") as f:
        json.dump(files, f)
    jobs = plan_asset(kind, aid, files)
    got = 0
    for url, rel, size in jobs:
        got += download(url, os.path.join(d, rel), size)
    open(done, "w").close()
    return [os.path.join(kind, aid, r) for _, r, _ in jobs], got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="download only N assets per type (for testing)")
    ap.add_argument("--types", default="hdris,textures,models")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--full-tonemapped", action="store_true", help="download full-res tonemapped images (~24MB/HDRI)")
    a = ap.parse_args()
    global FULL_TONEMAPPED
    FULL_TONEMAPPED = a.full_tonemapped
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    idx_path = os.path.join(OUT, "index.json")
    index = {}
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            index = {e["id"]: e for e in json.load(f)}
    total_bytes = 0
    for kind in a.types.split(","):
        assets = get_json("%s/assets?t=%s" % (API, kind))
        ids = sorted(assets)
        if a.limit:
            ids = ids[: a.limit]
        log("== %s: %d asset" % (kind, len(ids)))
        n = 0
        with ThreadPoolExecutor(max_workers=min(a.workers, 4)) as ex:
            futs = {ex.submit(process, kind, i, assets[i]): i for i in ids}
            for fu in as_completed(futs):
                aid = futs[fu]; m = assets[aid]; n += 1
                try:
                    local, got = fu.result()
                    total_bytes += got
                    index[aid] = {
                        "id": aid, "name": m.get("name"), "type": kind[:-1],
                        "categories": m.get("categories", []), "tags": m.get("tags", []),
                        "authors": list((m.get("authors") or {}).keys()),
                        "license": "CC0-1.0", "source": "https://polyhaven.com/a/%s" % aid,
                        "files": sorted(local),
                    }
                    if n % 25 == 0 or n == len(ids):
                        log("%s %d/%d (%.1f MB newly downloaded this session)" % (kind, n, len(ids), total_bytes / 1e6))
                except Exception as e:
                    log("ERROR %s/%s: %s" % (kind, aid, e))
                if n % 100 == 0:
                    write_index(idx_path, index)
        write_index(idx_path, index)
    log("DONE. Total newly downloaded this session: %.1f MB" % (total_bytes / 1e6))


def write_index(p, index):
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(sorted(index.values(), key=lambda e: (e["type"], e["id"])), f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)


if __name__ == "__main__":
    main()
