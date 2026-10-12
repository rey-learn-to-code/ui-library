"""Strip an HTML file to readable text (no scripts/styles). Usage: python3 -I util_html2text.py in.html out.txt"""
import sys, re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.skip = 0; s.out = []
    def handle_starttag(s, t, a):
        if t in ("script", "style", "noscript", "svg", "nav", "header", "footer"): s.skip += 1
        if t in ("p", "div", "li", "h1", "h2", "h3", "h4", "br", "tr", "pre"): s.out.append("\n")
        if t in ("h1", "h2", "h3", "h4"): s.out.append("#" * int(t[1]) + " ")
        if t == "li": s.out.append("- ")
    def handle_endtag(s, t):
        if t in ("script", "style", "noscript", "svg", "nav", "header", "footer") and s.skip: s.skip -= 1
    def handle_data(s, d):
        if not s.skip: s.out.append(d)
p = P(); p.feed(open(sys.argv[1], encoding="utf-8", errors="ignore").read())
txt = re.sub(r"[ \t]+", " ", "".join(p.out)); txt = re.sub(r"\n\s*\n+", "\n\n", txt)
open(sys.argv[2], "w").write(txt.strip() + "\n")
