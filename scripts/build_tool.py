"""Combine the catalog + manifests + resource indexes into tool/data/*.json for the lookup page.
Re-run whenever you download more resources:  python3 -I scripts/build_tool.py
"""
import json, os, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TN = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "tool", "data")
os.makedirs(OUT, exist_ok=True)


def load(path, default=None):
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save(name, data):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    n = len(data) if isinstance(data, list) else sum(len(v) for v in data.values() if isinstance(v, list))
    print(f"  {name}: {n}")


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


# 1. Catalog of 75 sites + manifests
manifest = {}
for f in glob.glob(os.path.join(ROOT, "catalog", "manifest", "*.json")):
    for e in load(rel(f), []) or []:
        manifest[e["url"].rstrip("/")] = e
catalog = []
for g in load("catalog/sites.json"):
    sites = []
    for url, desc in g["sites"]:
        m = manifest.get(url.rstrip("/"), {})
        lp = m.get("local_path")
        readme = None
        if lp:
            for name in ("README.md", "REFERENCE.md", "GUIDE.md"):
                if os.path.exists(os.path.join(ROOT, lp, name)):
                    readme = f"{lp}/{name}"
                    break
        sites.append({"url": url, "desc": desc, "status": m.get("status", "link-only"),
                      "local_path": lp, "license": m.get("license"), "size": m.get("size"),
                      "items": m.get("items"), "notes": m.get("notes"), "usage": m.get("usage"),
                      "readme": readme})
    catalog.append({"group": g["group"], "title": g["title"], "sites": sites})
save("catalog.json", catalog)

# 2. UI components (React / HTML)
comps = []


def add_files(lib, files, category=None, stack="react", lic=None):
    for p in sorted(files):
        comps.append({"lib": lib, "name": os.path.splitext(os.path.basename(p))[0],
                      "cat": category, "path": rel(p), "stack": stack, "license": lic})


base = os.path.join(TN, "effects/reactbits-dev/repo/src")
for cat_dir in sorted(glob.glob(os.path.join(base, "ts-tailwind", "*"))):
    cat = os.path.basename(cat_dir)
    for comp in sorted(glob.glob(os.path.join(cat_dir, "*"))):
        name = os.path.basename(comp)
        variants = {}
        for v in ("ts-tailwind", "ts-default", "tailwind", "content"):
            d = os.path.join(base, v, cat, name)
            fs = sorted(x for x in glob.glob(os.path.join(d, "*")) if x.endswith((".tsx", ".jsx", ".css")))
            if fs:
                variants[v] = [rel(x) for x in fs]
        main = variants.get("ts-tailwind", [None])[0]
        if main:
            comps.append({"lib": "React Bits", "name": name, "cat": cat, "path": main, "stack": "react",
                          "license": "MIT + Commons Clause", "variants": variants})
add_files("Magic UI", glob.glob(os.path.join(TN, "effects/magicui-design/repo/apps/www/registry/magicui/*.tsx")), lic="MIT")
add_files("Aceternity (free)", glob.glob(os.path.join(TN, "effects/ui-aceternity-com/src/*/components/ui/*.tsx")), lic="Aceternity: use in your own websites, do not redistribute")
sh = os.path.join(TN, "ui-kits/ui-shadcn-com/repo/apps/v4/registry/new-york-v4")
add_files("shadcn/ui", glob.glob(os.path.join(sh, "ui/*.tsx")), "ui", lic="MIT")
for b in sorted(glob.glob(os.path.join(sh, "blocks/*"))):
    if os.path.isdir(b):
        page = glob.glob(os.path.join(b, "page.tsx")) or glob.glob(os.path.join(b, "**/*.tsx"), recursive=True)[:1]
        if page:
            comps.append({"lib": "shadcn/ui", "name": os.path.basename(b), "cat": "blocks", "path": rel(page[0]),
                          "stack": "react", "license": "MIT", "folder": rel(b)})
add_files("Shadcnblocks (free)", glob.glob(os.path.join(TN, "ready-blocks/shadcnblocks-com/github_shadcn-ui-blocks/src/block/*.tsx")), "blocks", lic="MIT + Commons Clause")
add_files("lucide-animated", glob.glob(os.path.join(TN, "animated-icons/lucide-animated-com/repo/icons/*.tsx")), "animated icons", lic="MIT (do not redistribute)")
add_files("Flowbite (HTML)", glob.glob(os.path.join(TN, "ui-kits/flowbite-com/repo/content/components/*.md")), "components", "html", "MIT")
add_files("daisyUI (HTML)", glob.glob(os.path.join(TN, "ui-kits/daisyui-com/repo/packages/docs/src/routes/(routes)/components/*/+page.md")), "components", "html", "MIT")
for c in comps:
    if c["lib"] == "daisyUI (HTML)":
        c["name"] = c["path"].split("/")[-2]
for d in sorted(glob.glob(os.path.join(TN, "effect-references/codrops/repos/*"))):
    idx = glob.glob(os.path.join(d, "index.html")) or glob.glob(os.path.join(d, "**/index.html"), recursive=True)[:1]
    if idx:
        comps.append({"lib": "Codrops demo", "name": os.path.basename(d), "cat": "demo", "path": rel(idx[0]),
                      "stack": "html", "license": "MIT", "folder": rel(d), "demo": True})
save("components.json", comps)

# 3. Icon
icons = {}
for key, folder, lic in (("lucide", "icon/lucide", "ISC"), ("phosphor", "icon/phosphor", "MIT"), ("heroicons", "icon/heroicons", "MIT")):
    idx = load(f"assets/{folder}/icons-index.json", [])
    icons[key] = {"base": f"assets/{folder}/", "license": lic,
                  "items": [[i["name"], " ".join(i.get("tags") or []), i["files"]] for i in idx]}
with open(os.path.join(OUT, "icons.json"), "w", encoding="utf-8") as f:
    json.dump(icons, f, ensure_ascii=False, separators=(",", ":"))
print("  icons.json:", {k: len(v["items"]) for k, v in icons.items()})

# 4. Prompt
save("prompts.json", load("assets/prompt-templates/prompts-index.json", []))

# 5. Fonts (Google Fonts + Fontshare) — normalize the different index formats that may exist
fonts = []
for src, folder in (("Google Fonts", "font/google-fonts"), ("Fontshare", "font/fontshare")):
    for cand in ("fonts-index.json", "index.json", "fontshare-index.json"):
        idx = load(f"assets/{folder}/{cand}")
        if idx is not None:
            break
    if isinstance(idx, dict):
        idx = next((v for v in idx.values() if isinstance(v, list)), [])
    for x in idx or []:
        files = x.get("files") or x.get("file_paths") or []
        if isinstance(files, dict):
            files = list(files.values())
        files = [p if p.startswith("assets") else f"assets/{folder}/{p}" for p in files if isinstance(p, str)]
        vi = x.get("vietnamese")
        if vi is None:
            vi = "vietnamese" in (x.get("subsets") or [])
        fonts.append({"src": src, "name": x.get("name") or x.get("family"), "cat": x.get("category"),
                      "vi": bool(vi), "license": x.get("license"),
                      "weights": x.get("weights") or x.get("styles"), "files": files[:24]})
save("fonts.json", fonts)

# 6. Colors & themes
themes = load("assets/shadcn-themes/tweakcn/presets/themes.json", {}).get("themes", {})
pal = load("assets/colors/generated-palettes/palettes.json", {}).get("palettes", [])
save("colors.json", {"tweakcn": [{"slug": k, **v, "css": f"assets/shadcn-themes/tweakcn/presets/css/{k}.css"} for k, v in themes.items()],
                     "palettes": pal,
                     "typescale": sorted(rel(p) for p in glob.glob(os.path.join(TN, "type-scales/typescale/*.css"))),
                     "utopia": sorted(rel(p) for p in glob.glob(os.path.join(TN, "type-scales/utopia/fluid/*.css")))})

# 7. Images: self-made backgrounds, 3D icons, avatars, device frames, unDraw (if present)
images = []
bgs = load("assets/backgrounds/generated/index.json", {})
for i in bgs.get("items", []):
    images.append({"set": "Self-made backgrounds (CC0)", "name": i["title"], "tag": i.get("kind"), "path": f"assets/backgrounds/generated/{i['file']}"})
d3 = load("assets/3d-icons/old-3dicons-co/png/index.json", {})
for i in d3.get("icons", []):
    f = i["files"]
    images.append({"set": "3dicons (CC0)", "name": i["title"], "tag": i.get("category"),
                   "path": "assets/3d-icons/old-3dicons-co/png/" + (f.get("dynamic-color") or next(iter(f.values()))),
                   "variants": {k: "assets/3d-icons/old-3dicons-co/png/" + v for k, v in f.items()}})
for p in sorted(glob.glob(os.path.join(TN, "sample-data/dicebear/avatars_svg/*/*.svg"))):
    images.append({"set": "Avatar DiceBear", "name": os.path.basename(p)[:-4], "tag": p.split(os.sep)[-2], "path": rel(p)})
for p in sorted(glob.glob(os.path.join(TN, "mockup/mockuphone-com/repo/**/*.png"), recursive=True)):
    images.append({"set": "Mockuphone device frames (CC BY 3.0)", "name": os.path.basename(p)[:-4], "tag": "mockup", "path": rel(p)})
for p in sorted(glob.glob(os.path.join(TN, "illustrations/undraw-co/svg/*.svg"))):
    images.append({"set": "unDraw (attribution)", "name": os.path.basename(p)[:-4], "tag": "illustration", "path": rel(p)})
save("images.json", images)

# 8. 3D: Poly Haven, ambientCG, Kenney, Rive
assets3d = []
for src, folder in (("Poly Haven", "polyhaven"), ("ambientCG", "ambientcg"), ("Kenney", "kenney")):
    idx = load(f"assets/3d-materials/{folder}/index.json", [])
    if isinstance(idx, dict):
        idx = next((v for v in idx.values() if isinstance(v, list)), [])
    for x in idx:
        files = x.get("files") or x.get("local_files") or []
        if isinstance(files, dict):
            files = [v for v in files.values() if isinstance(v, str)]
        thumb = next((f for f in files if isinstance(f, str) and f.lower().endswith((".jpg", ".png", ".webp"))), None)
        base = f"assets/3d-materials/{folder}/"
        assets3d.append({"src": src, "id": x.get("id"), "name": x.get("name"), "type": x.get("type"),
                         "tags": " ".join((x.get("tags") or []) + (x.get("categories") or [])),
                         "thumb": base + thumb if thumb and not thumb.startswith("assets") else thumb,
                         "folder": base + (x.get("local_path") or (os.path.dirname(files[0]) if files else x.get("id") or ""))})
for x in load("assets/animated-icons/rive/rive-index.json", []):
    assets3d.append({"src": "Rive (CC BY 4.0)", "id": x["slug"], "name": x["title"], "type": "riv",
                     "tags": x.get("author", ""), "thumb": None, "folder": "assets/animated-icons/rive", "page": x.get("page_url")})
save("assets3d.json", assets3d)

# 9. Guide documents (md)
DOC_NAMES = ("README.md", "REFERENCE.md", "DEMOS.md", "GUIDE.md", "CHECKLIST.md", "NOTES.md", "PROMPT_EXAMPLES.md")
docs = sorted(rel(p) for pat in ("*", "*/*", "*/*/*") for p in glob.glob(os.path.join(TN, pat))
              if os.path.basename(p) in DOC_NAMES)
docs += [rel(p) for p in glob.glob(os.path.join(TN, "font/font-pairings-vietnamese.md"))]
save("docs.json", docs)
print("Done ->", rel(OUT))
