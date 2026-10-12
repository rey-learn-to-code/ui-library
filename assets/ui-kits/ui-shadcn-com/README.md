# shadcn/ui (https://ui.shadcn.com/)

The most popular React + Tailwind interface kit. License: MIT (see `repo/LICENSE.md`).

## What is inside
- `repo/` — a copy of the source code from GitHub `shadcn-ui/ui` (`.git` folder removed).
- Component code (buttons, dialogs, tables...): `repo/apps/v4/registry/new-york-v4/ui/` (about 60 `.tsx` files).
- Ready-made interface blocks (login, sidebar, dashboard): `repo/apps/v4/registry/new-york-v4/blocks/`.
- Charts: `repo/apps/v4/registry/new-york-v4/charts/`; usage examples: `repo/apps/v4/registry/new-york-v4/examples/` and `repo/apps/v4/examples/`.
- New versions by "base" (Radix / Base UI / React Aria): `repo/apps/v4/registry/bases/`.
- Docs (MDX): `repo/apps/v4/content/docs/`.

## Using it in React (Next.js/Vite)
- Quick way: in a project that already has Tailwind, run `npx shadcn@latest init`, then `npx shadcn@latest add button` (replace `button` with the component name).
- Manual way: copy the `.tsx` file from `ui/` into your project's `components/ui/`, install the packages that file `import`s (for example `@radix-ui/...`, `class-variance-authority`), and create a `cn` function in `lib/utils.ts`.

## Using it in plain HTML
Cannot be used directly (these are React components). You can open the `.tsx` files to look at the Tailwind classes and copy them into HTML.
