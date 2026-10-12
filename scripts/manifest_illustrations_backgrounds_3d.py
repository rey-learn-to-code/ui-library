"""Write catalog/manifest/illustrations_backgrounds_3d.json. Usage: python3 -I manifest_illustrations_backgrounds_3d.py <library_root>"""
import sys, os, json, subprocess
R = sys.argv[1]
def sz(p):
    p = os.path.join(R, p)
    return subprocess.run(["du", "-sh", p], capture_output=True, text=True).stdout.split()[0] if os.path.exists(p) else None
def cnt(p, ext):
    n = 0
    for _, _, fs in os.walk(os.path.join(R, p)):
        n += sum(f.lower().endswith(ext) for f in fs)
    return n
E = []
def add(url, status, local, lic, items, notes, usage):
    E.append({"url": url, "status": status, "local_path": local, "license": lic,
              "size": sz(local) if local else None, "items": items, "notes": notes, "usage": usage})
add("https://undraw.co/illustrations", "link-only", None, "unDraw License (free, no attribution needed; bundling into collections/scraping is forbidden)", 0,
    "The unDraw license forbids automated downloads and bundling/redistributing illustrations as a collection, and robots.txt blocks /api/ and the SVG files for AI bots, so nothing was bulk-downloaded.",
    "Go to undraw.co, pick your main color, then download individual SVGs as needed for empty states, onboarding, landing pages; no attribution needed.")
add("https://storyset.com/", "link-only", None, "Storyset/Freepik: free with attribution; robot downloads and adding to libraries/collections are forbidden", 0,
    "The Storyset terms forbid downloading with robots/tools and adding the content to databases, collections or libraries, so only the link is saved.",
    "Download illustrations one by one by hand (you can adjust colors/animation on the website) and credit 'Illustration by Storyset' with a link to storyset.com.")
add("https://www.humaaans.com/", "link-only", None, "CC0 (Pablo Stanley)", 0,
    "The download button leads to Gumroad (pablostanley.gumroad.com/l/humaaans), which asks for an email; there is no public direct download link, so only the link is saved.",
    "Download the Sketch/Figma/SVG pack yourself via Gumroad or use it on Blush; it is CC0 so it is free to use — combine characters for landing pages.")
add("https://haikei.app/", "link-only", None, "SVG generator app; the free plan needs no sign-up (details on the Pricing page)", 0,
    "Haikei is an online SVG background generator with no downloadable asset pack; instead, 40 original SVG backgrounds were created in assets/backgrounds/generated.",
    "Open haikei.app to create waves, blobs, layers... then export SVG/PNG; or use the self-made set in this library (recolor with the --bg-* CSS variables).")
add("https://www.svgbackgrounds.com/", "link-only", None, "Free plan requires attribution; Pro plan is paid (not verified because access was blocked)", 0,
    "The site returns a Cloudflare challenge (403) to automated access; it was not bypassed, so only the link is saved and the terms were not checked directly.",
    "Open it in a browser, customize the background and copy the CSS/SVG code; if you use the free version, give credit as described on the site.")
add("https://www.fffuel.co/", "link-only", None, "fffuel license: personal/commercial use, no attribution needed; sharing/redistributing the images is forbidden", 0,
    "fffuel is a set of SVG generators (blobs, waves, noise, gradients...) with no downloadable pack, and the license forbids redistributing the images, so nothing was downloaded into the library.",
    "Use tools like sssurf, gggrain, ssshape to create SVGs for each project and save them directly in that project.")
add("https://shots.so/", "link-only", None, "Online mockup generator app (has paid plans)", 0,
    "Shots is a web-based mockup generator with no public downloadable assets, so only the link is saved.",
    "Upload a screenshot to shots.so to place it in a device frame with a background and shadow, then export a product showcase image.")
add("https://mockupbro.com/", "link-only", None, "Free online mockup generator (per the site's terms)", 0,
    "MockupBro is an online mockup generator (upload a design, then download the image) with no downloadable template pack, so only the link is saved.",
    "Pick a template (device, print, shirt, packaging), upload your design and download the mockup image without a watermark.")
add("https://mockuphone.com/", "downloaded", "assets/mockup/mockuphone-com",
    "Source code Apache-2.0; device frame images CC BY 3.0 (attribution required, see ATTRIBUTION.txt)",
    cnt("assets/mockup/mockuphone-com", ".png"),
    "Downloaded 342 PNG device frames (mockup_templates) and device_info.json from the open-source repo oursky/mockuphone.com using a sparse checkout. Also includes 2 CSS device frame sets (MIT) in assets/mockup/css-devices.",
    "Place your screenshot under the PNG frame using the coordinates in device_info.json, or use devices.css to build the frame in HTML/CSS; credit MockUPhone as described in ATTRIBUTION.txt.")
add("https://shapefest.com/", "link-only", None, "Shapefest License: may be used in projects; redistributing as a library is forbidden, even for free", 0,
    "Downloading the packs requires a login/All Access, and the license forbids redistributing them as a library, so nothing was downloaded into the library.",
    "Log in yourself and download the free 512px pack when you need 3D illustrations for landing pages or slides; do not bundle them into a collection.")
add("https://icons8.com/illustrations", "link-only", None, "Icons8: free version requires attribution (link to icons8), limited resolution; per the Icons8 terms", 0,
    "The site returns 403 to automated access and full downloads need an account/payment, so only the link is saved (the terms were not checked directly).",
    "Browse in a web browser, download the free PNGs and credit Icons8 as instructed; buy a plan if you need SVG/no attribution.")
add("https://old.3dicons.co/", "downloaded", "assets/3d-icons/old-3dicons-co", "CC0 1.0 (Vijay Verma)",
    cnt("assets/3d-icons/old-3dicons-co/png", ".png"),
    "Downloaded all of 3dicons V1: 120 icons x 3 angles x 4 styles from the public CDN listed in the CC0 repo realvjy/3dicons, plus png/index.json and the site source code.",
    "Use the 3D PNGs as icons/illustrations for landing pages, slides, apps; CC0, so no attribution needed. Look up names/categories in png/index.json.")
os.makedirs(os.path.join(R, "catalog/manifest"), exist_ok=True)
json.dump(E, open(os.path.join(R, "catalog/manifest/illustrations_backgrounds_3d.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E), "entries")
