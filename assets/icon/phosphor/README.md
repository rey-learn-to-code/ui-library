# Phosphor – icon set in 6 weights (1,512 icons × 6 styles)

Source: https://phosphoricons.com/ — npm package `@phosphor-icons/core` 2.1.1.
License: MIT (free, commercial use allowed, keep the `LICENSE` file).

## What is in this folder
- `svg/<style>/` – 6 styles: `regular` (normal), `thin` (very thin), `light` (thin), `bold` (heavy), `fill` (solid), `duotone` (two tones).
  File names: the regular style is `house.svg`; other styles add a suffix, for example `svg/bold/house-bold.svg`.
- `icons-index.json` – icon names, keywords (tags) and the path for each style.
- `sprite-regular.svg` – all regular-style icons combined into one file, each icon is a `<symbol id="icon-name">`.
- `packages/` – the original npm package and the name/keyword data file (for reference only).

## Using it in plain HTML
- Paste the SVG file's contents straight into the page; change the color with CSS `color` (the icons use `fill="currentColor"`).
- Or `<img src="svg/regular/house.svg" width="24" alt="">`.
- Sprite:
```html
<svg width="24" height="24" fill="currentColor"><use href="sprite-regular.svg#house"></use></svg>
```
- Quick option with no download: the `@phosphor-icons/web` package (include the script from a CDN, then write `<i class="ph ph-house"></i>`, `<i class="ph-bold ph-house"></i>`).

## Using it in React
```bash
npm install @phosphor-icons/react
```
```jsx
import { House } from "@phosphor-icons/react";
<House size={32} weight="duotone" color="#4f46e5" />
```
`weight` accepts: `thin`, `light`, `regular`, `bold`, `fill`, `duotone`.
