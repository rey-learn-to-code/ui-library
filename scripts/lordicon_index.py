"""Build lordicon-public-index.json from public lordicon.com sitemaps (metadata only).
Usage: python3 -I lordicon_index.py <out.json> <sitemap.xml>...
"""
import json, re, sys
out = []
for f in sys.argv[2:]:
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r"<url><loc>(https://lordicon\.com/icons/([^/]+)/([^/]+)/([^<]+))</loc>(.*?)</url>", s, re.S):
        url, family, style, slug, rest = m.groups()
        num, _, name = slug.partition("-")
        imgs = re.findall(r"<image:loc>([^<]+)</image:loc>", rest)
        out.append({"family": family, "style": style, "slug": slug, "number": num, "name": name.replace("-", " "),
                    "page_url": url,
                    "preview_svg": next((i for i in imgs if i.endswith(".svg")), None),
                    "preview_gif": next((i for i in imgs if i.endswith(".gif")), None)})
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False)
from collections import Counter
print(len(out), Counter((o["family"], o["style"]) for o in out).most_common(20))
