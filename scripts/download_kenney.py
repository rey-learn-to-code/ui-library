#!/usr/bin/env python3
"""Download all free asset packs (CC0) from kenney.nl/assets.

Lists packs from the public category pages (3D first, then 2D, Textures, Audio, then the main page),
takes the "Continue without donating..." link (free zip, no account needed) and extracts it into
kenney/<category>/<slug>/ (keeping License.txt). Packs without a free zip link are skipped and logged.
Safe to re-run any number of times.
How to run:  python3 -I download_kenney.py [--limit N]
"""
import argparse, html, json, os, re, time, zipfile, urllib.request, urllib.error, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "assets", "3d-materials", "kenney")
LOG = os.path.join(ROOT, "scripts", "logs", "kenney.log")
BASE = "https://kenney.nl/assets"
UA = "goodstack-ui-library-3d-materials/1.0 (personal offline CC0 asset toolkit; python-urllib)"
CATS = ["3D", "2D", "Textures", "Audio"]
MAX_UNZIP = 2 << 30
_lock = threading.Lock()
RE_ASSET = re.compile(r"href=['\"]https://kenney\.nl/assets/([a-z0-9][a-z0-9\-]*)['\"]")
RE_ZIP = re.compile(r"href=['\"](https://kenney\.nl/media/pages/assets/[^'\"]+?\.zip)['\"]")
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
RE_TAG = re.compile(r"href=['\"]https://kenney\.nl/assets/tag:([^'\"]+)['\"]")
NOT_ASSET = {"category", "tag", "page"}


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


def get_text(url, tries=6):
    with http_get(url, tries) as r:
        return r.read().decode("utf-8", "replace")


def download(url, dest):
    if os.path.exists(dest):
        return 0
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    with http_get(url) as r, open(tmp, "wb") as f:
        expected = r.headers.get("Content-Length")
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    if expected and os.path.getsize(tmp) != int(expected):
        os.remove(tmp)
        raise IOError("incomplete download %s" % url)
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
            raise ValueError("zip too large (%d bytes)" % total)
        z.extractall(dest)
        return sorted(i.filename for i in z.infolist() if not i.is_dir())


def list_category(path):
    """Walk the /assets/<path>/page:N pages until there are no new packs."""
    slugs, page = [], 1
    while page < 200:
        url = "%s/%s" % (BASE, path) if page == 1 else "%s/%s/page:%d" % (BASE, path, page)
        url = url.replace("assets//", "assets/").rstrip("/")
        try:
            t = get_text(url, tries=2 if page > 1 else 6)
        except urllib.error.HTTPError as e:
            if page > 1 and e.code in (404, 500):  # page past the last one -> Kenney returns 500
                break
            raise
        new = [s for s in dict.fromkeys(RE_ASSET.findall(t)) if s.split(":")[0] not in NOT_ASSET and s not in slugs]
        if not new:
            break
        slugs += new
        page += 1
        time.sleep(0.5)
    return slugs


def process(slug, cat):
    d = os.path.join(OUT, cat, slug)
    done = os.path.join(d, ".done")
    if os.path.exists(done):
        with open(done, encoding="utf-8") as f:
            return json.load(f), 0
    page = get_text("%s/%s" % (BASE, slug))
    m = RE_ZIP.search(page)
    if not m:
        return {"skipped": True, "reason": "no free zip link"}, 0
    zurl = html.unescape(m.group(1))
    title = RE_TITLE.search(page)
    name = html.unescape(title.group(1).split("·")[0].strip()) if title else slug
    tags = sorted(set(html.unescape(t) for t in RE_TAG.findall(page)))
    os.makedirs(d, exist_ok=True)
    zpath = os.path.join(d, zurl.rsplit("/", 1)[1])
    got = download(zurl, zpath)
    files = safe_extract(zpath, d)
    os.remove(zpath)
    info = {"name": name, "tags": tags, "zip_url": zurl,
            "files_count": len(files),
            "license_file": next((os.path.join(cat, slug, f) for f in files if f.lower().endswith("license.txt")), None),
            "sample_files": [os.path.join(cat, slug, f) for f in files[:15]]}
    with open(done, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False)
    return info, got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    plan = {}  # slug -> cat (first category the pack was seen in)
    for cat in CATS:
        s = list_category("category:%s" % cat)
        log("category %s: %d packs" % (cat, len(s)))
        for x in s:
            plan.setdefault(x, cat)
    for x in list_category(""):
        plan.setdefault(x, "Other")
    items = list(plan.items())  # order: 3D, 2D, Textures, Audio, Other
    log("== Kenney: %d packs" % len(items))
    if a.limit:
        items = items[: a.limit]
    idx_path = os.path.join(OUT, "index.json")
    index, total, n = [], 0, 0
    # submit in priority order; the pool is small so 3D packs run first
    with ThreadPoolExecutor(max_workers=min(a.workers, 4)) as ex:
        futs = {ex.submit(process, s, c): (s, c) for s, c in items}
        for fu in as_completed(futs):
            s, c = futs[fu]; n += 1
            try:
                info, got = fu.result()
                total += got
                if info.get("skipped"):
                    log("SKIPPED %s: %s" % (s, info["reason"]))
                else:
                    index.append(dict(id=s, type=c, license="CC0-1.0",
                                      source="%s/%s" % (BASE, s), local_path=os.path.join(c, s), **info))
            except Exception as e:
                log("ERROR %s: %s" % (s, e))
            if n % 10 == 0 or n == len(items):
                log("%d/%d packs (%.1f MB newly downloaded this session)" % (n, len(items), total / 1e6))
    index.sort(key=lambda e: (e["type"], e["id"]))
    with open(idx_path + ".tmp", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    os.replace(idx_path + ".tmp", idx_path)
    log("DONE. %d packs in the index." % len(index))


if __name__ == "__main__":
    main()
