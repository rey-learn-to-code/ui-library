# Heroicons – icons from the Tailwind CSS team (324 icons × 4 styles)

Source: https://heroicons.com/ — npm package `heroicons` 2.2.0.
License: MIT (free, commercial use allowed, keep the `LICENSE` file).

## What is in this folder
- `svg/outline/` – outline strokes, 24px.
- `svg/solid/` – solid fill, 24px.
- `svg/mini/` – solid fill, 20px (for buttons, input fields).
- `svg/micro/` – solid fill, 16px (for very small spots).
- `icons-index.json` – icon names and the path for each style (Heroicons has no keywords, so search by name only).
- `sprite-outline.svg`, `sprite-solid.svg` – all 24px icons combined, each icon is a `<symbol id="icon-name">`.
- `packages/` – the original npm package, for reference.

## Using it in plain HTML
- Paste the SVG file's contents straight into the page; change its color with CSS `color`.
- Or `<img src="svg/outline/home.svg" width="24" alt="">`.
- Sprite:
```html
<svg width="24" height="24"><use href="sprite-outline.svg#home"></use></svg>
```

## Using it in React
```bash
npm install @heroicons/react
```
```jsx
import { HomeIcon } from "@heroicons/react/24/outline";   // or /24/solid, /20/solid, /16/solid
<HomeIcon className="size-6 text-blue-500" />
```
