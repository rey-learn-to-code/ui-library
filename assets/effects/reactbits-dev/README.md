# React Bits (https://reactbits.dev/)

More than 100 animated effects: moving text, animated backgrounds, cursors, 3D cards... License: **MIT + Commons Clause** (`repo/LICENSE.md`) — you may use them in your own websites/products, but you may **not** resell the library itself.

## What is inside
- `repo/` — source code from GitHub `DavidHDev/react-bits` (`.git` removed; the `public/` folder, ~211MB, holds demo images/videos).
- Each effect comes in 4 versions; pick the one that matches your project type:
  - `repo/src/content/<Group>/<Name>/` — JavaScript + plain CSS.
  - `repo/src/tailwind/...` — JavaScript + Tailwind.
  - `repo/src/ts-default/...` — TypeScript + CSS.
  - `repo/src/ts-tailwind/...` — TypeScript + Tailwind.
- Groups: `Animations`, `Backgrounds`, `Components`, `TextAnimations`, `Micro`.

## Using it in React
- Copy the effect's folder (the `.jsx/.tsx` file + `.css` if there is one) into your project, and install the packages it `import`s (for example `motion`, `gsap`, `ogl`, `three`).
- Or use the CLI as shown on the site (shadcn or jsrepo), for example `npx shadcn@latest add @react-bits/SplitText-TS-TW` (variants: JS-CSS, JS-TW, TS-CSS, TS-TW).

## Using it in plain HTML
Not usable directly (these are React components).
