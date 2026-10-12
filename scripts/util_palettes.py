"""Self-made curated palettes (not scraped). Computes WCAG contrast text/background & primary-fg/primary.
Usage: python3 -I util_palettes.py <out_dir>"""
import json, os, sys
out = sys.argv[1]
P = [
 ("Bright Ocean", "ocean-light", "light", "#f7fafc", "#ffffff", "#0f172a", "#475569", "#0369a1", "#ffffff", "#e0f2fe", "#0e7490"),
 ("Pine Forest", "pine-forest", "light", "#f6f8f4", "#ffffff", "#1c2a1e", "#4b5d4e", "#2f6b3a", "#ffffff", "#e3efe0", "#a16207"),
 ("Milk Coffee", "milk-coffee", "light", "#faf6f1", "#fffdf9", "#2b1d14", "#6b5545", "#7c4a24", "#ffffff", "#f1e4d6", "#b45309"),
 ("Lotus", "lotus", "light", "#fdf7f9", "#ffffff", "#2a1520", "#6d4a5a", "#be185d", "#ffffff", "#fce7f3", "#15803d"),
 ("Minimal Gray", "minimal-gray", "light", "#fafafa", "#ffffff", "#171717", "#525252", "#171717", "#fafafa", "#f4f4f5", "#2563eb"),
 ("Sunny Orange", "sunny-orange", "light", "#fffaf3", "#ffffff", "#1f1300", "#5f4b32", "#c2410c", "#ffffff", "#ffedd5", "#0f766e"),
 ("Tech Violet", "tech-violet", "light", "#f8f7ff", "#ffffff", "#1e1b3a", "#57537a", "#6d28d9", "#ffffff", "#ede9fe", "#0891b2"),
 ("Midnight Blue", "midnight-blue", "dark", "#0b1120", "#111a2e", "#e2e8f0", "#94a3b8", "#60a5fa", "#0b1120", "#1e293b", "#f472b6"),
 ("Graphite", "graphite-dark", "dark", "#111111", "#1a1a1a", "#ededed", "#a1a1a1", "#ededed", "#111111", "#262626", "#22c55e"),
 ("Dark Moss", "moss-dark", "dark", "#0f1410", "#161d17", "#e6efe6", "#9fb3a2", "#86efac", "#0f1410", "#1f2a21", "#fbbf24"),
 ("Neon Night", "neon-night", "dark", "#0d0a1a", "#151027", "#f1ecff", "#a99fc9", "#c084fc", "#0d0a1a", "#221a3d", "#2dd4bf"),
 ("Terracotta", "terracotta-dark", "dark", "#1a1210", "#241915", "#f5e9e2", "#bfa597", "#fb923c", "#1a1210", "#33241e", "#93c5fd"),
]
def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + 0.05) / (lb + 0.05), 2)
res = []; css = ["/* Self-made palettes (not taken from any website) — free to use. Apply: <html data-palette=\"ocean-light\"> */"]
for name, slug, mode, bg, surf, text, muted, prim, primfg, sec, acc in P:
    c = {"background": bg, "surface": surf, "text": text, "text-muted": muted, "primary": prim,
         "primary-foreground": primfg, "secondary": sec, "accent": acc}
    chk = {"text/background": cr(text, bg), "text-muted/background": cr(muted, bg),
           "primary-foreground/primary": cr(primfg, prim), "primary/background": cr(prim, bg)}
    res.append({"name": name, "slug": slug, "mode": mode, "colors": c, "contrast_wcag": chk,
                "passes_AA_normal_text": all(chk[k] >= 4.5 for k in ("text/background", "text-muted/background", "primary-foreground/primary"))})
    css.append(f"[data-palette=\"{slug}\"] {{ color-scheme: {mode};")
    css += [f"  --c-{k}: {v};" for k, v in c.items()] + ["}"]
json.dump({"license": "CC0 — self-made for ui-library", "palettes": res}, open(os.path.join(out, "palettes.json"), "w"), ensure_ascii=False, indent=1)
open(os.path.join(out, "palettes.css"), "w").write("\n".join(css) + "\n")
for r in res: print(r["slug"], r["contrast_wcag"], r["passes_AA_normal_text"])
