# Flowbite (https://flowbite.com/) — free version

A set of Tailwind components with a small amount of JavaScript (dropdown menus, modals, tabs, carousels...), works well with plain HTML. License: MIT (`repo/LICENSE.md`). The paid Flowbite Pro version is **not** included here.

## What is inside
- `repo/` — source code from GitHub `themesberg/flowbite` (`.git` removed).
  - Docs + HTML examples for each component: `repo/content/` (for example `repo/content/components/navbar.md` contains HTML snippets you can copy).
  - JavaScript code: `repo/src/components/`.
  - `repo/llms.txt`, `repo/llms-full.txt`: text-only docs, good for giving to AI to read.
- `npm/dist_pkg/` — the unpacked `flowbite` 4.0.2 npm package. Ready-to-use files: `npm/dist_pkg/dist/flowbite.min.css`, `npm/dist_pkg/dist/flowbite.min.js`.

## Using it in plain HTML
```html
<link href="https://cdn.jsdelivr.net/npm/flowbite@4.0.2/dist/flowbite.min.css" rel="stylesheet" />
<!-- at the end of <body> -->
<script src="https://cdn.jsdelivr.net/npm/flowbite@4.0.2/dist/flowbite.min.js"></script>
```
Copy the component's HTML snippet from `repo/content/components/*.md` into your page. Without internet, point to the 2 files in `npm/dist_pkg/dist/`.

## Using it in React
Use the separate `flowbite-react` library (`npm i flowbite-react`), or paste the HTML into JSX (change `class` to `className`) and call `initFlowbite()` inside `useEffect`.
