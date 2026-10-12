# Lucide – thin outline icon set (2,134 icons)

Source: https://lucide.dev/icons/ — npm packages `lucide-static` 1.54.0 and `lucide-react` 1.54.0.
License: ISC (free, commercial use allowed, keep the `LICENSE` file).

## What is in this folder
- `svg/` – each icon is its own SVG file, for example `svg/house.svg`.
- `icons-index.json` – searchable list: icon name, keywords (tags), file path.
- `tags.json` – Lucide's original keywords.
- `sprite.svg` – all icons combined into one file (each icon is a `<symbol id="icon-name">`).
- `font/` – icon font version (`lucide.css` + `lucide.woff2`...).
- `packages/` – the original npm packages (.tgz) for reference; no need to install them.

## Using it in plain HTML
1. **Paste the SVG directly**: open `svg/house.svg`, copy all of its contents and paste it into your HTML. Change the color with CSS `color`, because the icons use `stroke="currentColor"`.
2. **Use it as an image**: `<img src="svg/house.svg" width="24" height="24" alt="Home">` (with this method you cannot change the color with CSS).
3. **Use the sprite** (light and tidy when you use many icons). The symbols in the sprite have no stroke settings of their own, so you must set the stroke attributes on the `<svg>` tag:
```html
<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
  <use href="sprite.svg#house"></use>
</svg>
```
4. **Icon font**: include `font/lucide.css`, then write `<i class="icon-house"></i>`.

## Using it in React
```bash
npm install lucide-react
```
```jsx
import { House, Search } from "lucide-react";
<House size={24} color="#111" strokeWidth={1.5} />
```
The component name is the icon name with the first letter of each word capitalized (`arrow-right` → `ArrowRight`).
