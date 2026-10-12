# Shadcnblocks (https://www.shadcnblocks.com/) — FREE part only

Ready-made interface blocks for shadcn/ui (hero, pricing table, FAQ, footer, login...).

## What is inside
- `github_shadcn-ui-blocks/` — Shadcnblocks' own public GitHub repo (`shadcnblocks/shadcn-ui-blocks`), license MIT + Commons Clause (`github_shadcn-ui-blocks/LICENSE.md`). The block code is in `github_shadcn-ui-blocks/src/block/` (`.git` removed).
- `free_blocks_list.json` — a list of 156 free items (113 blocks + 43 small components) taken from the public page https://www.shadcnblocks.com/blocks/free: name, description, page link, and install command.
- `TERMS_shadcnblocks.txt`, `LICENSE_shadcnblocks_site.txt` — the site's terms.

Note: Shadcnblocks' terms forbid bulk-downloading the registry with automated tools (only the shadcn CLI is allowed) and forbid collecting the free blocks into your own library/collection. So this library keeps only the official GitHub repo + the list of names/links; when you need a block, install it directly into the real project with the command below. Pro (paid) blocks are not included here.

## Using it in React
- `npx shadcn@latest add https://www.shadcnblocks.com/r/hero1.json` (use the exact command from `free_blocks_list.json`). The project must already have run `npx shadcn@latest init`.
- Or open `github_shadcn-ui-blocks/src/` to view/copy the included blocks.

## Using it in plain HTML
Not usable directly (React + Tailwind components); you can look at the Tailwind classes to rebuild it in HTML.
