# Fontshare — download status

Link: https://www.fontshare.com/ (fonts by Indian Type Foundry, under the ITF Free Font License — free for personal and commercial use).

**Not downloaded yet (2026-10-09):** the current internet provider's DNS servers (203.113.131.1 / 203.113.188.1) return `127.0.0.1` for `api.fontshare.com` and `cdn.fontshare.com` (both point to the CDN service `*.b-cdn.net`), so this computer cannot connect to the font download API. The `www.fontshare.com` site still opens, but its font data comes from that same API.

## How to download when the network allows it
1. Change the computer's DNS (for example 1.1.1.1 or 8.8.8.8) or use a different network, then test with: `curl -sI https://api.fontshare.com/v2/fonts`.
2. Run (from the `ui-library` folder):
   ```bash
   python3 -m pip install --user fonttools   # to check Vietnamese diacritics
   python3 -E scripts/font_fontshare.py assets/font/fontshare
   ```
   The script gets the font list from the public API, downloads the zip package of each font family (no login needed), unzips it into `families/<slug>/`, and creates `fontshare-index.json` with a `vietnamese` column (checked with fontTools against the letters ạ ắ ằ ẳ ẵ ặ ơ ư ữ đ ẫ ể ỹ).
3. Or download each font by hand on the website (Download button) and unzip it into `families/`.
