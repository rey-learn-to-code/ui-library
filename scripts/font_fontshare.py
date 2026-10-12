"""Download all free Fontshare families + build fontshare-index.json.

Usage: python3 -E font_fontshare.py  (-E, not -I: needs fontTools from user site-packages) <out_dir>
Needs api.fontshare.com reachable (some ISP DNS resolvers map *.b-cdn.net to
127.0.0.1 -> switch DNS to 1.1.1.1 / 8.8.8.8 first, then run).
Fonts are only downloaded via the public, no-login download endpoint.
Safe re-run: families already unzipped are skipped.
"""
import io, json, os, sys, time, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor

OUT = sys.argv[1]
API = "https://api.fontshare.com/v2"
UA = {"User-Agent": "ui-library-font-collector/1.0 (personal toolkit)"}
VI = "ạắằẳẵặơưữđẫểỹ"


def get(url, tries=5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < tries - 1:
                time.sleep(5 * (i + 1)); continue
            raise
        except Exception:
            if i < tries - 1:
                time.sleep(3 * (i + 1)); continue
            raise


def list_fonts():
    fonts, page = [], 1
    while True:
        d = json.loads(get(f"{API}/fonts?limit=100&page={page}"))
        batch = d.get("fonts") or d.get("data") or []
        fonts += batch
        if not batch or not d.get("has_more", len(batch) == 100):
            break
        page += 1
    return fonts


def safe_unzip(data, dest):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for m in z.infolist():
            p = os.path.normpath(os.path.join(dest, m.filename))
            if not p.startswith(os.path.abspath(dest) + os.sep) or m.filename.startswith('__MACOSX'):
                continue
            if m.is_dir():
                os.makedirs(p, exist_ok=True); continue
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, 'wb') as f:
                f.write(z.read(m))


def vi_check(folder):
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return None, []
    best, missing_best = None, list(VI)
    for root, _, files in os.walk(folder):
        for fn in files:
            if fn.lower().endswith(('.ttf', '.otf')):
                try:
                    cmap = TTFont(os.path.join(root, fn), lazy=True).getBestCmap() or {}
                except Exception:
                    continue
                missing = [c for c in VI if ord(c) not in cmap]
                if best is None or len(missing) < len(missing_best):
                    best, missing_best = fn, missing
                if not missing:
                    return True, []
    if best is None:
        return None, []
    return False, missing_best


def do(font):
    slug = font.get("slug") or font.get("name", "").lower().replace(" ", "-")
    dest = os.path.join(OUT, "families", slug)
    rec = {"name": font.get("name"), "slug": slug, "category": font.get("category"),
           "designer": ", ".join(d.get("name", "") for d in font.get("designers", []) if isinstance(d, dict)) or None,
           "license": "ITF Free Font License (FFL)", "dir": os.path.relpath(dest, OUT),
           "styles": [s.get("name") or s.get("weight", {}).get("name") for s in font.get("styles", []) if isinstance(s, dict)],
           "api_languages": font.get("languages") or font.get("supported_languages")}
    try:
        if not os.path.isdir(dest) or not os.listdir(dest):
            safe_unzip(get(f"{API}/fonts/download/{slug}"), dest)
            time.sleep(0.5)
        rec["status"] = "ok"
    except Exception as e:
        rec["status"] = f"error: {e}"
    ok, missing = vi_check(dest)
    rec["vietnamese"], rec["vi_missing"] = ok, missing
    rec["files"] = sorted(os.path.relpath(os.path.join(r, f), OUT) for r, _, fs in os.walk(dest) for f in fs
                          if f.lower().endswith(('.ttf', '.otf', '.woff', '.woff2')))
    print(slug, rec["status"], "vi=" + str(ok), flush=True)
    return rec


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    fonts = list_fonts()
    with open(os.path.join(OUT, "fontshare-api-raw.json"), "w", encoding="utf-8") as f:
        json.dump(fonts, f, ensure_ascii=False)
    with ThreadPoolExecutor(3) as ex:
        rows = list(ex.map(do, fonts))
    rows.sort(key=lambda r: (r["name"] or "").lower())
    with open(os.path.join(OUT, "fontshare-index.json"), "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print("families", len(rows), "ok", sum(r["status"] == "ok" for r in rows),
          "vietnamese", sum(r["vietnamese"] is True for r in rows))
