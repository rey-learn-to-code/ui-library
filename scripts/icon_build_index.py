"""Build icons-index.json + sprite for lucide / phosphor / heroicons.
Usage: python3 -I icon_build_index.py <ui-library/assets/icon>
Reads only local files (SVG + metadata as text); executes nothing.
"""
import json, os, re, sys

root = sys.argv[1]


def rel(*p):
    return "/".join(p)


def sprite(out_path, items):
    """items: list of (id, svg_path). Builds <symbol> sprite."""
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
    for sid, path in items:
        s = open(path, encoding="utf-8").read()
        m = re.search(r"<svg([^>]*)>(.*)</svg>", s, re.S)
        if not m:
            continue
        attrs, body = m.group(1), m.group(2)
        vb = re.search(r'viewBox="([^"]+)"', attrs)
        keep = []
        for a in ("fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin"):
            v = re.search(r'\s%s="([^"]+)"' % a, attrs)
            if v:
                keep.append('%s="%s"' % (a, v.group(1)))
        parts.append('<symbol id="%s" viewBox="%s" %s>%s</symbol>'
                     % (sid, vb.group(1) if vb else "0 0 24 24", " ".join(keep), body.strip()))
    parts.append("</svg>")
    open(out_path, "w", encoding="utf-8").write("\n".join(parts))


# Lucide
d = os.path.join(root, "lucide")
tags = json.load(open(os.path.join(d, "tags.json"), encoding="utf-8"))
names = sorted(f[:-4] for f in os.listdir(os.path.join(d, "svg")) if f.endswith(".svg"))
idx = [{"name": n, "tags": tags.get(n, []), "files": {"outline": rel("svg", n + ".svg")}} for n in names]
json.dump(idx, open(os.path.join(d, "icons-index.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("lucide", len(idx))

# Phosphor
d = os.path.join(root, "phosphor")
meta_src = open(os.path.join(d, "packages", "core-metadata.index.mjs"), encoding="utf-8").read()
ptags = {}
for m in re.finditer(r'name:\s*"([^"]+)",\s*pascal_name:[^\n]*\n(.*?)tags:\s*\[(.*?)\]', meta_src, re.S):
    ptags[m.group(1)] = re.findall(r'"([^"]+)"', m.group(3))
weights = ["regular", "thin", "light", "bold", "fill", "duotone"]
names = sorted(f[:-4] for f in os.listdir(os.path.join(d, "svg", "regular")) if f.endswith(".svg"))
idx = []
for n in names:
    files = {}
    for w in weights:
        fn = n + ".svg" if w == "regular" else "%s-%s.svg" % (n, w)
        if os.path.exists(os.path.join(d, "svg", w, fn)):
            files[w] = rel("svg", w, fn)
    idx.append({"name": n, "tags": [t for t in ptags.get(n, []) if t != "*new*"], "files": files})
json.dump(idx, open(os.path.join(d, "icons-index.json"), "w", encoding="utf-8"), ensure_ascii=False)
sprite(os.path.join(d, "sprite-regular.svg"),
       [(n, os.path.join(d, "svg", "regular", n + ".svg")) for n in names])
print("phosphor", len(idx), "with tags:", sum(1 for i in idx if i["tags"]))

# Heroicons (no tags upstream)
d = os.path.join(root, "heroicons")
styles = ["outline", "solid", "mini", "micro"]
names = sorted(f[:-4] for f in os.listdir(os.path.join(d, "svg", "outline")) if f.endswith(".svg"))
idx = []
for n in names:
    files = {s: rel("svg", s, n + ".svg") for s in styles if os.path.exists(os.path.join(d, "svg", s, n + ".svg"))}
    idx.append({"name": n, "tags": [], "files": files})
json.dump(idx, open(os.path.join(d, "icons-index.json"), "w", encoding="utf-8"), ensure_ascii=False)
for s in ("outline", "solid"):
    sprite(os.path.join(d, "sprite-%s.svg" % s), [(n, os.path.join(d, "svg", s, n + ".svg")) for n in names])
print("heroicons", len(idx))
