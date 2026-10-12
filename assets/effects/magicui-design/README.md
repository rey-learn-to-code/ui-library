# Magic UI (https://magicui.design/)

A free animated-effects library for React + Tailwind + Motion (moving text, grid backgrounds, marquees, shimmering buttons...). License: MIT (`repo/LICENSE.md`).

## What is inside
- `repo/` — source code from GitHub `magicuidesign/magicui` (`.git` removed).
- Component code: `repo/apps/www/registry/magicui/` (about 79 files).
- Usage examples for each component: `repo/apps/www/registry/example/` (about 170 files).
- Component list (registry): `repo/registry.json`; docs: `repo/apps/www/content/`.

## Using it in React
- `npx shadcn@latest add @magicui/marquee` (or `npx shadcn@latest add "https://magicui.design/r/marquee.json"`) (replace `marquee` with the component name).
- Or copy files from `registry/magicui/` into `components/magicui/`, then install `motion` and any packages the file `import`s.

## Using it in plain HTML
Not usable directly (these are React components). Use it only as a reference for ideas/CSS.
