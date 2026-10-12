# 21st.dev (https://21st.dev/) — links only, NOT downloaded

A community library of more than 12,000 React + Tailwind components (hero, pricing, navbar, buttons, cards, animated backgrounds, text effects...).

## Why nothing was downloaded
- The source code is only available with an account + API key: the registry `https://21st.dev/r/<author>/<name>` returns error 403 "Authentication required"; the detail pages also leave the code area empty when you are not logged in.
- 21st.dev's terms forbid automated collection (scraping) of both content and descriptive data (names, descriptions, tags) without written permission. So this library keeps no copies.

## How to use it when building a website
1. Go to a category page to choose, for example: https://21st.dev/community/components/s/hero , .../s/pricing , .../s/button , .../s/card , .../s/background , .../s/footer , .../s/navigation-menu . Add `.md` to the end of a link to see a compact text version.
2. Each component clearly states its license (usually MIT) and author — read these before using it.
3. To install into React: create a free account, get an API key at https://21st.dev/mcp, then run the command shown on the page, in the form
   `npx shadcn@latest add "https://21st.dev/r/<author>/<name>?api_key=$API_KEY_21ST"` (free accounts are limited to a number of uses per day).
4. Many components on 21st actually come from open libraries already in this library (Magic UI, Aceternity, shadcn...) — look there first.

Plain HTML: not applicable (React components).
