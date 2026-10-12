#!/usr/bin/env python3
"""Download Google Fonts files into assets/font/google-fonts/repo/ (not stored on GitHub).

The font list (fonts-index.json) is already in the library; this script only fetches the font files.

Usage (run from the ui-library folder):
  python3 -I scripts/download_fonts.py "Be Vietnam Pro" "Inter"   # only these families (fast)
  python3 -I scripts/download_fonts.py --vietnamese                # the 543 families that support Vietnamese (~1 GB)
  python3 -I scripts/download_fonts.py --all                       # every family (~2.7 GB)
Safe to run again: files that already exist are skipped.
"""
import argparse, json, os, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GF = os.path.join(ROOT, "assets", "font", "google-fonts")
RAW = "https://raw.githubusercontent.com/google/fonts/main/"


def fetch(rel):
    dest = os.path.join(GF, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "skip"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    url = RAW + urllib.parse.quote(rel[len("repo/"):])
    try:
        with urllib.request.urlopen(url, timeout=120) as r, open(dest + ".part", "wb") as f:
            while chunk := r.read(1 << 16):
                f.write(chunk)
        os.replace(dest + ".part", dest)
        return "ok"
    except Exception as e:
        print(f"  failed: {rel} ({e})")
        return "fail"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*", help="font family names, e.g. \"Be Vietnam Pro\"")
    ap.add_argument("--vietnamese", action="store_true", help="all families that support Vietnamese")
    ap.add_argument("--all", action="store_true", help="every family")
    a = ap.parse_args()
    fonts = json.load(open(os.path.join(GF, "fonts-index.json"), encoding="utf-8"))
    if a.all:
        chosen = fonts
    elif a.vietnamese:
        chosen = [f for f in fonts if f.get("vietnamese")]
    elif a.names:
        want = {n.lower() for n in a.names}
        chosen = [f for f in fonts if f["name"].lower() in want]
        missing = want - {f["name"].lower() for f in chosen}
        if missing:
            print("Not found in fonts-index.json:", ", ".join(sorted(missing)))
    else:
        ap.print_help()
        return 1
    files = [p for f in chosen for p in f.get("files", []) + f.get("license_files", [])]
    print(f"{len(chosen)} families, {len(files)} files -> {os.path.join(GF, 'repo')}")
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(fetch, files))
    print(f"Done: {res.count('ok')} downloaded, {res.count('skip')} already there, {res.count('fail')} failed.")
    return 1 if res.count("fail") else 0


if __name__ == "__main__":
    sys.exit(main())
