"""Collect a curated set of PUBLIC Rive marketplace .riv runtime files (no login).
Usage: python3 -I rive_collect.py <out_dir> [n_featured] [n_per_query]
- listing: public api-cached.rive.app endpoints used by rive.app/marketplace
- license: read from each post's public SSR page (creativecommons link)
- downloads latest revision runtime .riv + thumbnail png; sequential, polite.
"""
import json, os, re, subprocess, sys, time, urllib.parse

out = sys.argv[1]
N_FEAT = int(sys.argv[2]) if len(sys.argv) > 2 else 30
N_Q = int(sys.argv[3]) if len(sys.argv) > 3 else 8
QUERIES = ["icon", "button", "loader", "toggle", "hover"]
UA = {"User-Agent": "Mozilla/5.0 (ui-library toolkit collector)"}
API = "https://api-cached.rive.app/api/community-posts/"


def get(url, binary=False, tries=4):
    # system curl (python 3.9 LibreSSL can't negotiate TLS with these hosts)
    for i in range(tries):
        r = subprocess.run(["curl", "-sL", "--max-time", "120", "-A", UA["User-Agent"],
                            "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code == b"429":
            time.sleep(5 * (i + 1)); continue
        if r.returncode != 0 or not code.startswith(b"2"):
            raise RuntimeError("HTTP %s %s" % (code.decode(), url))
        return body if binary else body.decode("utf-8", "replace")
    raise RuntimeError("429 " + url)


posts = {}
for page in range(4):
    for p in json.loads(get(API + "featured?page=%d&limit=40" % page)):
        posts.setdefault(p["community_post_id"], (p, "featured"))
    time.sleep(0.5)
featured = sorted((v for v in posts.values()), key=lambda x: -x[0]["reaction_count"])[:N_FEAT]
chosen = {p["community_post_id"]: (p, src) for p, src in featured}
for q in QUERIES:
    res = json.loads(get(API + "search?" + urllib.parse.urlencode({"query": q, "page": 0, "limit": 40})))
    res = sorted(res, key=lambda p: -p["reaction_count"])
    k = 0
    for p in res:
        if p["community_post_id"] in chosen:
            continue
        chosen[p["community_post_id"]] = (p, "search:" + q)
        k += 1
        if k >= N_Q:
            break
    time.sleep(0.5)

os.makedirs(os.path.join(out, "riv"), exist_ok=True)
os.makedirs(os.path.join(out, "thumbs"), exist_ok=True)
index = []
for pid, (p, src) in chosen.items():
    revs = sorted(p.get("community_revisions") or [], key=lambda r: r["community_revision_id"], reverse=True)
    rev = next((r for r in revs if r.get("community_files")), None)
    if not rev:
        continue
    slug = rev["slug"]
    page_url = "https://rive.app/marketplace/%s/" % slug
    try:
        html = get(page_url)
    except Exception as e:
        print("page fail", slug, e); continue
    lic = re.search(r'href="(https://creativecommons\.org/[^"]+)"[^>]*>([^<]+)</a></h4><p>License', html)
    if not lic:
        print("no CC license found, skip", slug); continue
    f = rev["community_files"][-1]
    riv_rel = "riv/%s.riv" % slug
    try:
        open(os.path.join(out, riv_rel), "wb").write(get(f["file_url"], binary=True))
    except Exception as e:
        print("riv fail", slug, e); continue
    thumb_rel = None
    if rev.get("thumbnail_url"):
        try:
            thumb_rel = "thumbs/%s.png" % slug
            open(os.path.join(out, thumb_rel), "wb").write(get(rev["thumbnail_url"], binary=True))
        except Exception:
            thumb_rel = None
    index.append({
        "title": rev["title"], "slug": slug, "author": p["owner"]["username"],
        "page_url": page_url, "license": lic.group(2).strip(), "license_url": lic.group(1),
        "tags": rev.get("tags", []), "artboard": rev.get("artboard"),
        "state_machine_or_animation": rev.get("animation"),
        "is_state_machine": rev.get("is_animation_state_machine"),
        "reactions": p["reaction_count"], "source": src,
        "file": riv_rel, "thumbnail": thumb_rel, "runtime_url": f["file_url"],
    })
    print("ok", slug, lic.group(2))
    time.sleep(0.7)

json.dump(index, open(os.path.join(out, "rive-index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("total", len(index))
