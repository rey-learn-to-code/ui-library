"""Extract tweakcn built-in theme presets by READING (not running) utils/theme-presets.ts
and config/theme.ts. Writes themes.json + one CSS file per theme (shadcn/ui variables).
Usage: python3 -I util_tweakcn_extract.py <repo_dir> <out_dir>"""
import json, os, re, sys

repo, out = sys.argv[1], sys.argv[2]

def parse_obj_literal(src, start):
    """Parse a simple JS object literal (string/identifier keys, string values, nested objects,
    `...spread` of identifiers resolved via ENV). Returns (obj, end_index)."""
    i = start
    def ws(i):
        while i < len(src):
            if src[i].isspace(): i += 1
            elif src.startswith("//", i): i = src.index("\n", i)
            elif src.startswith("/*", i): i = src.index("*/", i) + 2
            else: break
        return i
    def string(i):
        q = src[i]; j = i + 1; buf = []
        while src[j] != q:
            if src[j] == "\\": buf.append(src[j + 1]); j += 2
            else: buf.append(src[j]); j += 1
        return "".join(buf), j + 1
    def ident(i):
        m = re.compile(r"[A-Za-z_$][\w$]*").match(src, i); return m.group(0), m.end()
    def value(i):
        i = ws(i)
        if src[i] == "{": return obj(i)
        if src[i] in "\"'": return string(i)
        name, j = ident(i)
        return ENV.get(name, name), j
    def obj(i):
        assert src[i] == "{"; i += 1; d = {}
        while True:
            i = ws(i)
            if src[i] == "}": return d, i + 1
            if src.startswith("...", i):
                name, i = ident(i + 3); d.update(ENV[name])
            else:
                if src[i] in "\"'": k, i = string(i)
                else: k, i = ident(i)
                i = ws(i); assert src[i] == ":", src[i-40:i+40]; i += 1
                v, i = value(i); d[k] = v
            i = ws(i)
            if src[i] == ",": i += 1
    return obj(ws(start))

ENV = {}
cfg = open(os.path.join(repo, "config/theme.ts"), encoding="utf-8").read()
for name in ["DEFAULT_FONT_SANS", "DEFAULT_FONT_SERIF", "DEFAULT_FONT_MONO"]:
    m = re.search(name + r"\s*=\s*", cfg); s = m.end()
    while cfg[s].isspace(): s += 1
    q = cfg[s]; e = cfg.index(q, s + 1); ENV[name] = cfg[s + 1:e]
for name in ["defaultLightThemeStyles", "defaultDarkThemeStyles"]:
    m = re.search(r"export const " + name + r"\s*=\s*", cfg)
    ENV[name], _ = parse_obj_literal(cfg, m.end())
COMMON = re.findall(r'"([\w-]+)"', cfg[cfg.index("COMMON_STYLES"):cfg.index("];", cfg.index("COMMON_STYLES"))])

src = open(os.path.join(repo, "utils/theme-presets.ts"), encoding="utf-8").read()
m = re.search(r"defaultPresets[^=]*=\s*", src)
presets, _ = parse_obj_literal(src, m.end())

COLOR_KEYS = [k for k in ENV["defaultLightThemeStyles"] if k not in COMMON and not k.startswith("font")]

def shadows(st):
    c, op = st["shadow-color"], float(st["shadow-opacity"])
    x, y, b, s = st["shadow-offset-x"], st["shadow-offset-y"], st["shadow-blur"], st["shadow-spread"]
    def col(mult): return f"color-mix(in srgb, {c} {round(op*mult*100, 1)}%, transparent)"
    s2 = f"{float(s.replace('px','') or 0) - 1:g}px"
    one = lambda mult: f"{x} {y} {b} {s} {col(mult)}"
    two = lambda oy, ob: f"{one(1)}, {x} {oy} {ob} {s2} {col(1)}"
    return {"shadow-2xs": one(0.5), "shadow-xs": one(0.5), "shadow-sm": two("1px", "2px"),
            "shadow": two("1px", "2px"), "shadow-md": two("2px", "4px"), "shadow-lg": two("4px", "6px"),
            "shadow-xl": two("8px", "10px"), "shadow-2xl": one(2.5)}

os.makedirs(os.path.join(out, "css"), exist_ok=True)
themes = {}
for key, p in presets.items():
    light = {**ENV["defaultLightThemeStyles"], **p["styles"].get("light", {})}
    dark = {**ENV["defaultDarkThemeStyles"], **{k: light[k] for k in COMMON if k in light}, **p["styles"].get("dark", {})}
    themes[key] = {"label": p.get("label", key), "light": light, "dark": dark}
    lines = [f"/* tweakcn preset: {p.get('label', key)} ({key}) — extracted from jnsahaj/tweakcn (Apache-2.0) */", ":root {"]
    for k, v in light.items(): lines.append(f"  --{k}: {v};")
    lines.append(f"  --tracking-normal: {light['letter-spacing']};")
    for k, v in shadows(light).items(): lines.append(f"  --{k}: {v};")
    lines += ["}", "", ".dark {"]
    for k, v in dark.items():
        if k in COMMON or k.startswith("font"): continue
        lines.append(f"  --{k}: {v};")
    for k, v in shadows(dark).items(): lines.append(f"  --{k}: {v};")
    lines += ["}", ""]
    open(os.path.join(out, "css", f"{key}.css"), "w", encoding="utf-8").write("\n".join(lines))

json.dump({"source": "https://github.com/jnsahaj/tweakcn utils/theme-presets.ts", "license": "Apache-2.0",
           "count": len(themes), "themes": themes}, open(os.path.join(out, "themes.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# Tailwind v4 mapping (shared by every theme file)
tw = ["/* Tailwind CSS v4: map shadcn variables to utilities. Import AFTER one theme file. */", "@theme inline {"]
for k in COLOR_KEYS:
    if k.startswith("shadow") or k in ("radius",): continue
    tw.append(f"  --color-{k}: var(--{k});")
tw += ["  --font-sans: var(--font-sans);", "  --font-serif: var(--font-serif);", "  --font-mono: var(--font-mono);",
       "  --radius-sm: calc(var(--radius) - 4px);", "  --radius-md: calc(var(--radius) - 2px);",
       "  --radius-lg: var(--radius);", "  --radius-xl: calc(var(--radius) + 4px);"]
for s in ["2xs", "xs", "sm", "", "md", "lg", "xl", "2xl"]:
    n = f"shadow-{s}" if s else "shadow"; tw.append(f"  --{n}: var(--{n});")
tw += ["  --tracking-normal: var(--tracking-normal);", "}", "", "body { letter-spacing: var(--tracking-normal); }", ""]
open(os.path.join(out, "css", "_theme-inline-tailwind-v4.css"), "w").write("\n".join(tw))
print(len(themes), "themes")
