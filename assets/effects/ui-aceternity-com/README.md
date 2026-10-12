# Aceternity UI (https://ui.aceternity.com/) — FREE part only

Very "eye-catching" React + Tailwind + Motion effects (light-beam backgrounds, 3D cards, spotlight, lamp, globe...).
Downloaded 119 free items (111 components + 8 blocks) through the public registry `https://ui.aceternity.com/registry/<name>.json`. The other 176 items are Pro (the server returns error 401 – login/payment required), so they were NOT downloaded.

License: see `LICENCE_aceternity.txt` — you may use them in your own end products (websites, apps), but you may not redistribute the source code or resell it as a template/library.

## What is inside
- `src/<name>/...` — the `.tsx` source code, already extracted (for example `src/3d-card/components/ui/3d-card.tsx`).
- `registry_json/<name>.json` — the original JSON file (includes the list of packages to install under `dependencies`).
- `results.json` — list of download attempts: `status` 200 = downloaded, 401 = Pro (skipped).

## Using it in React
- Quick: `npx shadcn@latest add https://ui.aceternity.com/registry/3d-card.json`.
- Manual: copy the `.tsx` file from `src/<name>/` into your project, install the packages listed in the JSON's `dependencies` (usually `motion`, `clsx`, `tailwind-merge`), and create a `cn` function in `lib/utils.ts`.

## Using it in plain HTML
Not usable directly (these are React components).
