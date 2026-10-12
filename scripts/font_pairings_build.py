"""Generate font-pairings-vietnamese.md; every font is verified against fonts-index.json
(subset "vietnamese") AND by checking Vietnamese glyphs in the actual font files' cmap.

Usage: python3 -I font_pairings_build.py <font_dir>
"""
import json, os, sys
from fontTools.ttLib import TTFont

BASE = sys.argv[1]
GF = os.path.join(BASE, "google-fonts")
idx = {r["name"]: r for r in json.load(open(os.path.join(GF, "fonts-index.json"), encoding="utf-8"))}
VI = "ạắằẳẵặơưữđẫểỹỵẠẮỰĐ"

# (style label, heading, heading weight, body, use case)
PAIRS = [
    ("Modern, neutral", "Be Vietnam Pro", 700, "Inter", "Company websites, SaaS, dashboards"),
    ("Elegant, editorial", "Playfair Display", 700, "Source Sans 3", "Blogs, magazines, restaurants"),
    ("Classic, long reads", "Lora", 700, "Open Sans", "Personal blogs, long articles"),
    ("Journalism", "Merriweather", 900, "Merriweather Sans", "News sites, online magazines"),
    ("Tech", "Space Grotesk", 700, "IBM Plex Sans", "Startups, technical products"),
    ("Friendly", "Nunito", 800, "Nunito Sans", "Education, children, community"),
    ("Bold, eye-catching", "Oswald", 600, "Roboto", "Sports, events, landing pages"),
    ("Premium minimal", "Cormorant Garamond", 600, "Montserrat", "Fashion, cosmetics, weddings"),
    ("Academic", "EB Garamond", 600, "Noto Sans", "Books, research, libraries"),
    ("Bright startup", "Plus Jakarta Sans", 800, "Manrope", "Apps, fintech, landing pages"),
    ("Maximum readability", "Lexend", 600, "Lexend", "Education, content for all ages"),
    ("Modern editorial", "Fraunces", 700, "Work Sans", "Creative brands, studios"),
    ("Distinctive", "Bricolage Grotesque", 800, "Public Sans", "Agencies, portfolios"),
    ("Literary", "Crimson Pro", 600, "Literata", "Stories, e-books, literary blogs"),
    ("Serious, trustworthy", "Noto Serif", 700, "Noto Sans", "Banking, legal, government agencies"),
    ("Soft", "Quicksand", 700, "Mulish", "Spas, health care, mother & baby"),
    ("Engineering", "IBM Plex Serif", 600, "IBM Plex Sans", "Technical documentation, businesses"),
    ("Developer docs", "Inter", 700, "Inter", "Docs, tech blogs (code: JetBrains Mono)"),
    ("Graceful", "Prata", 400, "Lato", "Hotels, real estate"),
    ("Energetic", "Archivo", 800, "Barlow", "Sports, logistics, industry"),
    ("Warm", "Alegreya", 700, "Alegreya Sans", "Bookshops, cafes, culture"),
    ("Quick news reading", "Roboto Slab", 700, "Roboto", "News, aggregator blogs"),
    ("Refined", "Spectral", 600, "Raleway", "Photography and architecture portfolios"),
    ("Big magazine", "Newsreader", 600, "Source Sans 3", "Long-form journalism"),
    ("Playful", "Baloo 2", 700, "Quicksand", "Food, drinks, youth products"),
    ("Soft modern", "Onest", 700, "Onest", "Apps, online services"),
    ("Geometric", "Josefin Sans", 700, "Lora", "Cafes, vintage brands"),
    ("Futuristic", "Unbounded", 700, "Inter", "Web3, technology, digital events"),
    ("Cards & invitations", "Dancing Script", 700, "Montserrat", "Wedding cards, gifts, flower shops"),
    ("Extra-bold headings", "Anton", 400, "Work Sans", "Posters, promotions, banners"),
    ("Vietnamese business", "Be Vietnam Pro", 800, "Noto Serif", "Company profiles, reports"),
    ("Classic editorial", "Bitter", 700, "Fira Sans", "Tutorial blogs, learning materials"),
]

CATS = {"SERIF": "serif", "SANS_SERIF": "sans-serif", "DISPLAY": "sans-serif", "HANDWRITING": "cursive", "MONOSPACE": "monospace"}


def check(name):
    r = idx.get(name)
    assert r and r["vietnamese"], f"{name}: not in index or no vietnamese subset"
    path = os.path.join(GF, r["files"][0])
    cmap = TTFont(path, lazy=True).getBestCmap()
    miss = [c for c in VI if ord(c) not in cmap]
    assert not miss, f"{name}: missing {miss} in {path}"
    return r


def gparam(name, weights):
    return name.replace(" ", "+") + ":wght@" + ";".join(str(w) for w in sorted(set(weights)))


def nextid(name):
    return name.replace(" ", "_")


out = ["# Heading + body font pairing suggestions (with Vietnamese accents)", "",
       "All fonts below are **free** on Google Fonts (OFL/Apache license — commercial use allowed) and **verified to support Vietnamese accents**: they have the `vietnamese` subset in `google-fonts/fonts-index.json` and also contain all of the characters " + " ".join(VI) + " in the actual font file (checked with fontTools).",
       "", "This list was put together for this library. Fontshare fonts are not included yet because they could not be downloaded to check their accents (see `fontshare/NOTES.md`).", "",
       "How to use: copy the `<link>` snippet into the `<head>` of your HTML file and the CSS snippet into your CSS file. For Next.js, use the names in the `next/font/google` line (see `README.md` section 3).",
       "", "Sample text: *Tiếng Việt có dấu — Quý khách vui lòng đặt hàng trước 17 giờ. Ửng hồng, ngỡ ngàng, Đặng Thị Kỳ Duyên.*", ""]

for i, (label, h, hw, b, use) in enumerate(PAIRS, 1):
    rh, rb = check(h), check(b)
    fams = [gparam(h, [hw] + ([400, 700] if h == b else []))] if h == b else [gparam(h, [hw]), gparam(b, [400, 700])]
    href = "https://fonts.googleapis.com/css2?" + "&".join("family=" + f for f in fams) + "&display=swap"
    title = f"{h} + {b}" if h != b else f"{h} (one font for both headings and body)"
    out += [f"## {i}. {title}", "",
            f"- Style: {label}. Good for: {use}.",
            f"- Headings: {h} ({rh['category'].lower()}, weight {hw}) — `google-fonts/{rh['dir']}`",
            f"- Body: {b} ({rb['category'].lower()}) — `google-fonts/{rb['dir']}`",
            f"- Next.js: `import {{ {nextid(h)}{'' if h == b else ', ' + nextid(b)} }} from \"next/font/google\"` with `subsets: [\"vietnamese\", \"latin\"]`",
            "", "```html", f'<link rel="preconnect" href="https://fonts.googleapis.com">',
            f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
            f'<link rel="stylesheet" href="{href}">', "```", "", "```css",
            f'h1, h2, h3 {{ font-family: "{h}", {CATS[rh["category"]]}; font-weight: {hw}; line-height: 1.2; }}',
            f'body {{ font-family: "{b}", {CATS[rb["category"]]}; font-weight: 400; line-height: 1.65; }}',
            "```", ""]

out += ["---", "", "**Font pairing tips:**", "",
        "- One serif font + one sans-serif font is the safest combination.",
        "- Use at most 2 font families per website; use font weights (400/600/700) to create contrast.",
        "- Vietnamese body text should use a `line-height` of 1.6–1.75 because the accents take extra height.",
        "- Use handwriting/decorative fonts (Dancing Script, Anton) only for short headings, never for paragraphs.", ""]
with open(os.path.join(BASE, "font-pairings-vietnamese.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("pairs", len(PAIRS), "ok")
