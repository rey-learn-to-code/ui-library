"""Build fonts-index.json + fonts-vietnamese.json from a google/fonts checkout.

Usage: python3 -I font_google_index.py <repo_dir> <out_dir>
Parses each METADATA.pb (protobuf text format) with simple line parsing.
"""
import json, os, re, sys

repo, out = sys.argv[1], sys.argv[2]
KV = re.compile(r'^\s*(\w+)\s*:\s*(.+?)\s*$')


def val(v):
    v = v.strip()
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1].encode('latin-1', 'backslashreplace').decode('unicode_escape', 'replace') if '\\' in v else v[1:-1]
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def parse(path):
    fam = {"categories": [], "subsets": [], "fonts": [], "axes": []}
    stack = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith('#'):
                continue
            if s.endswith('{'):
                stack.append({"_k": s[:-1].strip()})
                continue
            if s == '}':
                blk = stack.pop()
                k = blk.pop("_k")
                if not stack:
                    if k == 'fonts':
                        fam["fonts"].append(blk)
                    elif k == 'axes':
                        fam["axes"].append(blk)
                continue
            m = KV.match(s)
            if not m:
                continue
            k, v = m.group(1), val(m.group(2))
            if stack:
                stack[-1][k] = v
            elif k == 'category':
                fam["categories"].append(v)
            elif k == 'subsets':
                fam["subsets"].append(v)
            elif k in ('name', 'designer', 'license', 'date_added', 'stroke', 'classifications', 'primary_script'):
                fam.setdefault(k, v)
    return fam


rows = []
for lic_dir in ('ofl', 'apache', 'ufl'):
    base = os.path.join(repo, lic_dir)
    if not os.path.isdir(base):
        continue
    for d in sorted(os.listdir(base)):
        meta = os.path.join(base, d, 'METADATA.pb')
        if not os.path.isfile(meta):
            continue
        try:
            fam = parse(meta)
        except Exception as e:  # keep going on odd files
            print('skip', meta, e, file=sys.stderr)
            continue
        rel = os.path.relpath(os.path.join(base, d), os.path.dirname(repo))
        files = [x for x in os.listdir(os.path.join(base, d))]
        lic_files = [x for x in files if x.upper().startswith(('OFL', 'LICENSE', 'UFL'))]
        rows.append({
            "name": fam.get("name", d),
            "dir": rel,
            "category": fam["categories"][0] if fam["categories"] else None,
            "designer": fam.get("designer"),
            "license": fam.get("license", lic_dir.upper()),
            "date_added": fam.get("date_added"),
            "subsets": fam["subsets"],
            "vietnamese": "vietnamese" in fam["subsets"],
            "variable_axes": [{"tag": a.get("tag"), "min": a.get("min_value"), "max": a.get("max_value")} for a in fam["axes"]],
            "styles": sorted({f"{f.get('weight')}{'i' if f.get('style') == 'italic' else ''}" for f in fam["fonts"]},
                             key=lambda x: (int(x.rstrip('i')) if x.rstrip('i').isdigit() else 0, x)),
            "files": [os.path.join(rel, f["filename"]) for f in fam["fonts"] if "filename" in f],
            "license_files": [os.path.join(rel, x) for x in lic_files],
        })

rows.sort(key=lambda r: r["name"].lower())
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'fonts-index.json'), 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
vi = [r for r in rows if r["vietnamese"]]
with open(os.path.join(out, 'fonts-vietnamese.json'), 'w', encoding='utf-8') as f:
    json.dump([{k: r[k] for k in ("name", "dir", "category", "designer", "license", "styles", "variable_axes", "files")} for r in vi],
              f, ensure_ascii=False, indent=1)
print(f"families={len(rows)} vietnamese={len(vi)} files={sum(len(r['files']) for r in rows)}")
