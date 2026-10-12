# daisyUI (https://daisyui.com/)

A set of ready-made CSS classes built on Tailwind (`btn`, `card`, `navbar`, `modal`...), usable with both React and plain HTML. License: MIT (`repo/LICENSE`, `npm/dist_pkg/LICENSE`).

## What is inside
- `repo/` — source code from GitHub `saadeghi/daisyui` (`.git` removed). Component code: `repo/packages/daisyui/src/components/` (color themes: `src/themes/`); docs + HTML examples: `repo/packages/docs/`.
- `npm/dist_pkg/` — the unpacked `daisyui` 5.7.47 npm package (downloaded with `npm pack`, no scripts run). Full CSS file: `npm/dist_pkg/daisyui.css`; CSS split per component: `npm/dist_pkg/components/`; color themes: `npm/dist_pkg/themes.css` and `npm/dist_pkg/theme/`. The original `.tgz` file is also in `npm/`.

## Using it in plain HTML (easiest)
Paste into `<head>`:
```html
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```
Then write `<button class="btn btn-primary">Button</button>`. To run without internet: replace the CDN link with the `daisyui.css` file above.

## Using it in React (Tailwind 4)
`npm i -D daisyui`, then in your main CSS file add `@plugin "daisyui";` after `@import "tailwindcss";`. Then use `className="btn"`.
