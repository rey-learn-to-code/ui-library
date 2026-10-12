# Font library — how to use it (plain-English guide)

This folder contains free fonts to use on websites, with a focus on fonts that support Vietnamese.

| Folder | What's in it |
|---|---|
| `google-fonts/repo/ofl`, `apache`, `ufl` | Every Google Fonts font (one folder per font, with its license file `OFL.txt` / `LICENSE.txt` / `UFL.txt`). |
| `google-fonts/fonts-index.json` | A list of every Google font: name, style (category), designer, license, available weights, file paths, and whether it supports Vietnamese (`"vietnamese": true`). |
| `google-fonts/fonts-vietnamese.json` | Only the Google fonts **that have Vietnamese diacritics** (accent marks). Pick your fonts from this list. |
| `fontshare/` | The spot for Fontshare fonts (see `fontshare/NOTES.md` — they may not have downloaded because of network issues). |
| `typewolf/NOTES.md` | Notes on using the Typewolf site to learn how to pair fonts (just a link). |
| `font-pairings-vietnamese.md` | About 30 heading + body font pairs, all with Vietnamese diacritics, with CSS code. |

> Quick terms:
> - **Font** = a set of letter shapes. **Family** = one font in several weights (thin, regular, bold…).
> - **Weight** = a number from 100 → 900. 400 is regular text, 700 is bold.
> - **Variable font** = a single file that contains every weight; its file name usually includes `[wght]`.
> - **CSS** = the website's "decoration sheet", which sets colors, text sizes, fonts…

---

## 1. Finding a font with Vietnamese diacritics

Open `google-fonts/fonts-vietnamese.json` and search for the font name (for example `"Be Vietnam Pro"`). The `"files"` line tells you where the file is, for example:

```
repo/ofl/bevietnampro/BeVietnamPro-Regular.ttf
```

This path starts from the `google-fonts/` folder.

---

## 2. Using a font in a plain HTML page (`@font-face`)

`@font-face` is like "telling the browser: I have a font called X, and its file is here".

**Step 1.** Copy the font files into your project, for example `my-site/fonts/BeVietnamPro-Regular.ttf` and `BeVietnamPro-Bold.ttf`.
(Tip: convert them to `.woff2` to make them about 50% smaller, for example with the command `pip install --user fonttools brotli` and then `python3 -m fontTools.ttLib.woff2 compress BeVietnamPro-Regular.ttf`.)

**Step 2.** In your CSS file (for example `my-site/style.css`), add:

```css
@font-face {
  font-family: "Be Vietnam Pro";          /* the name you'll use to call the font */
  src: url("fonts/BeVietnamPro-Regular.ttf") format("truetype");
  font-weight: 400;                       /* regular text */
  font-style: normal;
  font-display: swap;                     /* show text right away instead of a blank page */
}
@font-face {
  font-family: "Be Vietnam Pro";
  src: url("fonts/BeVietnamPro-Bold.ttf") format("truetype");
  font-weight: 700;                       /* bold text */
  font-style: normal;
  font-display: swap;
}

body { font-family: "Be Vietnam Pro", system-ui, sans-serif; }
```

For a **variable font** (one file for every weight):

```css
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter[opsz,wght].ttf") format("truetype");
  font-weight: 100 900;                   /* a range instead of a single number */
  font-display: swap;
}
```

**Step 3.** In `index.html`, make sure you have `<meta charset="utf-8">` and link the CSS:

```html
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
```

---

## 3. Using a font in Next.js

Next.js has a built-in tool called `next/font`: it downloads the font automatically when the site is built and serves it from your own website (fast, and it doesn't depend on Google while the site is running).

### Option A — From Google (`next/font/google`)

Open the file `app/layout.tsx` (the "frame" file that wraps every page):

```tsx
import { Be_Vietnam_Pro, Lora } from "next/font/google";

const body = Be_Vietnam_Pro({
  subsets: ["vietnamese", "latin"],   // "vietnamese" is REQUIRED to get the diacritics
  weight: ["400", "700"],             // non-variable fonts must list their weights
  display: "swap",
  variable: "--font-body",            // creates a CSS variable you can use elsewhere
});
const heading = Lora({ subsets: ["vietnamese", "latin"], variable: "--font-heading" });

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi" className={`${body.variable} ${heading.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

If a font name has spaces, replace them with underscores: `Be Vietnam Pro` → `Be_Vietnam_Pro`. (`lang="vi"` tells the browser the page is in Vietnamese; use `lang="en"` for an English site.)

Then in `app/globals.css`:

```css
body { font-family: var(--font-body), system-ui, sans-serif; }
h1, h2, h3 { font-family: var(--font-heading), Georgia, serif; }
```

### Option B — Using font files from your computer (`next/font/local`)

Copy the files into your project, for example `app/fonts/` (or `public/fonts/`), then in `app/layout.tsx`:

```tsx
import localFont from "next/font/local";

const myFont = localFont({
  src: [
    { path: "./fonts/BeVietnamPro-Regular.ttf", weight: "400", style: "normal" },
    { path: "./fonts/BeVietnamPro-Bold.ttf",    weight: "700", style: "normal" },
  ],
  display: "swap",
  variable: "--font-body",
});
// add myFont.variable to <html className=...> just like in Option A
```

Use Option B for Fontshare fonts (which aren't on Google) or when you want to be sure nothing is loaded from outside sites.

### Using it with Tailwind CSS v4

In `app/globals.css`:

```css
@theme inline {
  --font-sans: var(--font-body);
  --font-serif: var(--font-heading);
}
```

Then the classes `font-sans` / `font-serif` will use your fonts.

---

## 4. Checking Vietnamese diacritics

A font that "supports Vietnamese" must display **all** letters correctly, including the ones with two marks stacked on top of each other.

**Method 1 — check by eye.** Paste the sample below into a page, set the font you're testing, and look at it in lowercase, uppercase, bold and italic:

```
Ạ Ắ Ằ Ẳ Ẵ Ặ Ấ Ầ Ẩ Ẫ Ậ Ơ Ờ Ở Ỡ Ợ Ư Ừ Ử Ữ Ự Đ Ể Ễ Ỹ Ỵ
ạ ắ ằ ẳ ẵ ặ ấ ầ ẩ ẫ ậ ơ ờ ở ỡ ợ ư ừ ử ữ ự đ ể ễ ỹ ỵ
Tiếng Việt có dấu: “Quý khách vui lòng đặt hàng trước 17 giờ.”
```

(The last line means: "Vietnamese with diacritics: 'Customers, please place your order before 5 p.m.'")

Signs of a problem: some letters switch to a different font (they look "out of tune"), marks overlap each other, the top of a mark gets cut off, or you see empty boxes □.

**Method 2 — look it up in the list.** For Google fonts: look for `"vietnamese": true` in `google-fonts/fonts-index.json`. In Next.js, if a font doesn't support it, writing `subsets: ["vietnamese"]` will show an error as soon as you run the site.

**Method 3 — check with a command** (needs `pip install --user fonttools`):

```bash
python3 -c "
from fontTools.ttLib import TTFont; import sys
cmap = TTFont(sys.argv[1]).getBestCmap()
miss = [c for c in 'ạắằẳẵặơưữđẫểỹỵẠẮỰĐ' if ord(c) not in cmap]
print('All Vietnamese diacritics present' if not miss else 'Missing: ' + ' '.join(miss))
" duong/dan/toi/font.ttf
```

(Replace `duong/dan/toi/font.ttf` — "path/to/font.ttf" — with the real path to your font file. The Vietnamese letters inside the command are the test characters, so leave them as they are.)

**Note:** if you cut a font down to a smaller set of characters yourself (subsetting), you must keep the Vietnamese character ranges `U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB`.

---

## 5. Licenses — the quick version

- **OFL** (SIL Open Font License): free for personal and commercial use, and can be embedded in websites/apps. You may not sell the font files on their own. Keep the `OFL.txt` file with the font if you redistribute it.
- **Apache 2.0**, **UFL** (Ubuntu Font Licence): similar; commercial use is allowed; keep the license file.
- **ITF Free Font License** (Fontshare): free for personal and commercial use; you may not resell or redistribute the font files as a product of their own. Read the license file included in each downloaded package.

This is a summary for reference, not legal advice; for an important product, read the full license file itself.
