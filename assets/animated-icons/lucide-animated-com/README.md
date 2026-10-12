# lucide-animated (https://lucide-animated.com/)

More than 460 animated Lucide icons (they move when you hover over them), written in React + Motion. Source repo confirmed from the website itself: GitHub `pqoqubbw/icons`.
License: MIT (`repo/LICENSE`); the author's README adds a condition: you may use them in personal/commercial projects, but you may not redistribute or resell the icon set.

## What is inside
- `repo/icons/` — each icon is one `.tsx` file (for example `repo/icons/accessibility.tsx`), about 469 files.
- `repo/registry.json` — shadcn-style icon list; everything else is the code of the demo website.

## Using it in React
- `npx shadcn@latest add "https://lucide-animated.com/r/activity.json"` (replace `activity` with the icon name) → the file ends up in `components/icons/`.
- Or copy files from `repo/icons/` into your project, install `motion` (`npm i motion`) and create a `cn` function in `lib/utils.ts` (same as shadcn).

## Using it in plain HTML
Not usable directly (these are React components). For plain HTML, use Lucide's static icons or another folder under `animated-icons/`.
