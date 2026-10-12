"""Generate a set of parametric SVG backgrounds (original work) into assets/backgrounds/generated/.
Colors use the CSS variables --bg-bg, --bg-c1, --bg-c2, --bg-c3 (with default values) and currentColor.
Usage: python3 -I make_svg_backgrounds.py <out_dir>"""
import sys, os, math, random, json

OUT = sys.argv[1]
W, H = 1600, 900
BG, C1, C2, C3 = "var(--bg-bg,#0f172a)", "var(--bg-c1,#6366f1)", "var(--bg-c2,#ec4899)", "var(--bg-c3,#22d3ee)"
items = []


def svg(name, title, kind, body, defs=""):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" '
         f'width="{W}" height="{H}">\n<title>{title}</title>\n'
         f'<desc>Recolor: set the CSS variables bg-bg, bg-c1, bg-c2, bg-c3 (each prefixed with two hyphens) on the parent element when embedding the SVG inline; '
         f'currentColor strokes follow the color property.</desc>\n'
         f'<defs>{defs}</defs>\n<rect width="100%" height="100%" style="fill:{BG}"/>\n{body}\n</svg>\n')
    fn = f"{name}.svg"
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(s)
    items.append({"file": fn, "title": title, "kind": kind})


def f(c, o=1):
    return f'style="fill:{c};fill-opacity:{o}"'


def wave_path(rng, y0, amp, n, base=H):
    pts = [(i * W / n, y0 + rng.uniform(-amp, amp)) for i in range(n + 1)]
    d = f"M0,{base} L{pts[0][0]:.0f},{pts[0][1]:.0f} "
    for (x0, y0_), (x1, y1) in zip(pts, pts[1:]):
        cx = (x0 + x1) / 2
        d += f"C{cx:.0f},{y0_:.0f} {cx:.0f},{y1:.0f} {x1:.0f},{y1:.0f} "
    return d + f"L{W},{base} Z"


def peaks_path(rng, y0, amp, n):
    d = f"M0,{H} "
    for i in range(n + 1):
        d += f"L{i * W / n:.0f},{y0 + rng.uniform(-amp, amp):.0f} "
    return d + f"L{W},{H} Z"


def blob(rng, cx, cy, r, k=8, j=0.35):
    pts = []
    for i in range(k):
        a = 2 * math.pi * i / k
        rr = r * (1 + rng.uniform(-j, j))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = ""
    for i in range(k):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % k], pts[(i + 2) % k]
        if i == 0:
            d += f"M{p1[0]:.0f},{p1[1]:.0f} "
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {p2[0]:.0f},{p2[1]:.0f} "
    return d + "Z"


cols = [C1, C2, C3]

# 1) Waves - 6
for v in range(6):
    rng = random.Random(100 + v)
    layers = 3 + v % 3
    body = ""
    for i in range(layers):
        y = H * (0.45 + 0.5 * i / layers)
        body += f'<path d="{wave_path(rng, y, 40 + 20 * (v % 2), 4 + v)}" {f(cols[i % 3], 0.55 + 0.15 * (i == layers - 1))}/>\n'
    svg(f"waves-{v + 1:02d}", f"Layered waves {v + 1}", "waves", body)

# 2) Layered peaks - 6
for v in range(6):
    rng = random.Random(200 + v)
    layers = 4 + v % 2
    body = ""
    for i in range(layers):
        y = H * (0.35 + 0.55 * i / layers)
        body += f'<path d="{peaks_path(rng, y, 60, 6 + 2 * v)}" {f(cols[v % 3], 0.25 + 0.18 * i)}/>\n'
    svg(f"mountains-{v + 1:02d}", f"Layered peaks {v + 1}", "layered-peaks", body)

# 3) Blob - 6
for v in range(6):
    rng = random.Random(300 + v)
    blur = '<filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>'
    soft = v >= 3
    body = "<g filter=\"url(#b)\">" if soft else "<g>"
    for i in range(3 + v % 3):
        body += f'<path d="{blob(rng, rng.uniform(0.1, 0.9) * W, rng.uniform(0.1, 0.9) * H, rng.uniform(150, 320))}" {f(cols[i % 3], 0.7 if soft else 0.85)}/>\n'
    body += "</g>"
    svg(f"blob-{v + 1:02d}", f"Blob {'soft ' if soft else ''}{v + 1}", "blobs", body, blur if soft else "")

# 4) Grid - 4
for v, (step, fade) in enumerate([(40, False), (80, False), (40, True), (60, True)]):
    pat = (f'<pattern id="g" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
           f'<path d="M{step} 0H0V{step}" fill="none" style="stroke:{C1}" stroke-opacity="0.35" stroke-width="2"/></pattern>')
    defs = pat
    mask = ""
    if fade:
        defs += ('<radialGradient id="m"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>'
                 '<mask id="k"><rect width="100%" height="100%" fill="url(#m)"/></mask>')
        mask = ' mask="url(#k)"'
    body = f'<g style="color:{C1}"><rect width="100%" height="100%" fill="url(#g)"{mask}/></g>'
    svg(f"grid-{v + 1:02d}", f"Grid {step}px{' fading' if fade else ''}", "grid", body, defs)

# 5) Polka dots - 4
for v, (step, r) in enumerate([(24, 1.5), (40, 3), (32, 2), (60, 6)]):
    defs = (f'<pattern id="d" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
            f'<circle cx="{step / 2}" cy="{step / 2}" r="{r * 1.6}" style="fill:{cols[v % 3]}" fill-opacity="0.5"/></pattern>')
    extra = ""
    if v >= 2:
        defs += ('<linearGradient id="fd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/>'
                 '<stop offset="1" stop-color="#000"/></linearGradient><mask id="k"><rect width="100%" height="100%" fill="url(#fd)"/></mask>')
        extra = ' mask="url(#k)"'
    body = f'<g style="color:{cols[v % 3]}"><rect width="100%" height="100%" fill="url(#d)"{extra}/></g>'
    svg(f"dots-{v + 1:02d}", f"Polka dots {step}px", "dots", body, defs)

# 6) Noise/grain - 4
for v, (freq, op) in enumerate([(0.65, 0.18), (0.9, 0.25), (0.45, 0.3), (0.8, 0.15)]):
    defs = (f'<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="3" stitchTiles="stitch"/>'
            f'<feColorMatrix type="saturate" values="0"/></filter>'
            f'<linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:{cols[v % 3]}"/>'
            f'<stop offset="1" style="stop-color:{cols[(v + 1) % 3]}"/></linearGradient>')
    body = (f'<rect width="100%" height="100%" fill="url(#lg)" fill-opacity="{0.9 if v % 2 == 0 else 0.4}"/>'
            f'<rect width="100%" height="100%" filter="url(#n)" opacity="{op}" style="mix-blend-mode:overlay"/>')
    svg(f"grain-{v + 1:02d}", f"Grainy gradient {v + 1}", "noise-grain", body, defs)

# 7) Gradient mesh (simulated with stacked radial gradients) - 6
for v in range(6):
    rng = random.Random(700 + v)
    defs, body = "", ""
    for i in range(4):
        cx, cy = rng.uniform(0, 1), rng.uniform(0, 1)
        defs += (f'<radialGradient id="r{i}" cx="{cx:.2f}" cy="{cy:.2f}" r="{rng.uniform(0.5, 0.8):.2f}">'
                 f'<stop offset="0" style="stop-color:{cols[(i + v) % 3]};stop-opacity:0.9"/>'
                 f'<stop offset="1" style="stop-color:{cols[(i + v) % 3]};stop-opacity:0"/></radialGradient>')
        body += f'<rect width="100%" height="100%" fill="url(#r{i})"/>\n'
    if v >= 3:
        defs += ('<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>'
                 '<feColorMatrix type="saturate" values="0"/></filter>')
        body += '<rect width="100%" height="100%" filter="url(#n)" opacity="0.12"/>'
    svg(f"mesh-{v + 1:02d}", f"Gradient mesh {v + 1}{' with grain' if v >= 3 else ''}", "gradient-mesh", body, defs)

# 8) Extras: diagonal stripes, concentric circles, contour lines - 4
defs = ('<pattern id="s" width="28" height="28" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        f'<rect width="10" height="28" style="fill:{C1}" fill-opacity="0.25"/></pattern>')
svg("diagonal-stripes-01", "Diagonal stripes", "stripes", f'<g style="color:{C1}"><rect width="100%" height="100%" fill="url(#s)"/></g>', defs)
body = "".join(f'<circle cx="{W / 2}" cy="{H / 2}" r="{40 + i * 45}" fill="none" stroke="currentColor" stroke-width="3" stroke-opacity="{0.6 - i * 0.025:.2f}"/>' for i in range(20))
svg("circles-01", "Concentric circles", "concentric", f'<g style="color:{C3}">{body}</g>')
for v in range(2):
    rng = random.Random(800 + v)
    body = ""
    for i in range(18):
        p = wave_path(rng, 40 + i * 50, 25, 6)
        p = "M" + p.split(" L", 1)[1].rsplit(" L", 1)[0]  # drop the closing segment, keep only the curve
        body += f'<path d="{p}" fill="none" stroke="currentColor" stroke-opacity="0.5" stroke-width="3"/>\n'
    svg(f"contours-{v + 1:02d}", f"Contour lines {v + 1}", "topographic", f'<g style="color:{cols[v + 1]}">{body}</g>')

# Preview
cards = "\n".join(
    f'<figure><div class="frame" data-src="{i["file"]}"></div><figcaption><b>{i["file"]}</b><span>{i["kind"]}</span></figcaption></figure>'
    for i in items)
preview = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Self-made SVG backgrounds</title><style>
:root{{--bg-bg:#0f172a;--bg-c1:#6366f1;--bg-c2:#ec4899;--bg-c3:#22d3ee}}
body{{margin:0;font:14px system-ui,sans-serif;background:#111;color:#eee;padding:16px}}
header{{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:16px}}
label{{display:flex;gap:6px;align-items:center}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
figure{{margin:0;background:#1b1b1b;border-radius:8px;overflow:hidden}}
.frame svg{{display:block;width:100%;height:auto;aspect-ratio:16/9}}
figcaption{{display:flex;justify-content:space-between;padding:8px 10px}} figcaption span{{opacity:.6}}
</style></head><body>
<header><h1 style="font-size:18px;margin:0">Self-made SVG backgrounds ({len(items)})</h1>
<label>bg <input type="color" data-v="--bg-bg" value="#0f172a"></label>
<label>c1 <input type="color" data-v="--bg-c1" value="#6366f1"></label>
<label>c2 <input type="color" data-v="--bg-c2" value="#ec4899"></label>
<label>c3 <input type="color" data-v="--bg-c3" value="#22d3ee"></label>
<small>Open through a local server (e.g. python3 -m http.server) so the SVGs are embedded inline and recolor live.</small></header>
<main>{cards}</main>
<script>
document.querySelectorAll('input[data-v]').forEach(i=>i.oninput=()=>document.documentElement.style.setProperty(i.dataset.v,i.value));
let n=0;document.querySelectorAll('.frame').forEach(el=>{{const s=el.dataset.src;fetch(s).then(r=>r.text()).then(t=>{{
  n++;el.innerHTML=t.replace(/id="(\\w+)"/g,'id="$1_'+n+'"').replace(/url\\(#(\\w+)\\)/g,'url(#$1_'+n+')');}})
 .catch(()=>{{el.innerHTML='<img src="'+s+'" style="width:100%;display:block">';}});}});
</script></body></html>"""
open(os.path.join(OUT, "preview.html"), "w", encoding="utf-8").write(preview)
json.dump({"license": "Original work created in ui-library - free to use", "count": len(items),
           "css_vars": ["--bg-bg", "--bg-c1", "--bg-c2", "--bg-c3"], "items": items},
          open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "SVG")
