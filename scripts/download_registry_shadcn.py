"""Download shadcn-style registry items (public JSON) and extract their source code into files.

Usage:
  python3 -I download_registry_shadcn.py <list_file> <dest_dir>
list_file: one "name<TAB>json_url" per line.
Output: <dest>/registry_json/<name>.json, <dest>/src/<path in JSON>, <dest>/results.json (results summary)
Items that return 401/403 (Pro / login required) are skipped and recorded.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (ui-library collector)"


def fetch(url):
    for attempt in range(5):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(2 ** attempt * 2)
                continue
            return e.code, b""
        except Exception:
            time.sleep(2 ** attempt)
    return 0, b""


def safe_join(base, rel):
    rel = rel.replace("\\", "/").lstrip("/")
    parts = [p for p in rel.split("/") if p not in ("", ".", "..")]
    return os.path.join(base, *parts)


def handle(item, out):
    name, url = item
    code, body = fetch(url)
    if code != 200:
        return {"name": name, "url": url, "status": code}
    try:
        data = json.loads(body)
    except ValueError:
        return {"name": name, "url": url, "status": "bad-json"}
    with open(os.path.join(out, "registry_json", name + ".json"), "wb") as f:
        f.write(body)
    n = 0
    for fi in data.get("files", []) or []:
        content = fi.get("content")
        if not content:
            continue
        dest = safe_join(os.path.join(out, "src", name), fi.get("path") or (name + ".tsx"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        n += 1
    time.sleep(0.3)
    return {"name": name, "url": url, "status": 200, "files": n,
            "title": data.get("title"), "description": data.get("description"),
            "dependencies": data.get("dependencies"), "registryDependencies": data.get("registryDependencies")}


def main():
    lst, out = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.join(out, "registry_json"), exist_ok=True)
    os.makedirs(os.path.join(out, "src"), exist_ok=True)
    items = []
    with open(lst, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "\t" in line:
                items.append(tuple(line.split("\t", 1)))
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(lambda it: handle(it, out), items))
    with open(os.path.join(out, "results.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    ok = sum(1 for r in res if r["status"] == 200)
    print(f"ok={ok} / {len(res)}; skipped={[r['name'] for r in res if r['status'] != 200][:15]}")


if __name__ == "__main__":
    main()
