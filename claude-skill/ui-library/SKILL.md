---
name: ui-library
description: Use when building or styling any website or web UI (landing page, hero, pricing, navbar, dashboard, animation, icons, fonts, colors, 3D, illustrations) — a local library of free downloaded UI components, effects, icons, Vietnamese-capable fonts, shadcn themes, 3D assets and prompts at {{LIBRARY_PATH}}. Check it before writing UI from scratch or fetching assets from the web.
---

# UI Library: local toolkit for building websites

Root: `{{LIBRARY_PATH}}` (called `L` below). Overview in `L/README.md`, setup in `L/SETUP.md`.

## Quick lookup (read the JSON files, don't crawl big folders)
Pre-built data files live in `L/tool/data/`. All paths inside them are relative to `L`.
- `catalog.json`: 75 sources, each with status, license, notes, usage and `readme`.
- `components.json`: ~1,160 components with fields `lib`, `name`, `cat`, `stack` (react|html), `path`, `variants`. Libraries: React Bits (Backgrounds, TextAnimations, Animations, Components), Magic UI, shadcn/ui (ui and blocks), Aceternity free, Shadcnblocks free, lucide-animated, daisyUI, Flowbite, Codrops demos.
- `icons.json`: lucide, phosphor, heroicons. Each set has `base` and `items` as `[name, tags, files]`.
- `fonts.json`: Google Fonts; flag `vi` = supports Vietnamese. Vietnamese font pairings: `L/assets/font/font-pairings-vietnamese.md`.
- `colors.json`: 42 tweakcn themes (CSS), AA-contrast palettes, typescale CSS and Utopia fluid type.
- `images.json`: generated SVG backgrounds (recolour with `--bg-*` CSS variables), 3dicons, DiceBear avatars, Mockuphone device frames.
- `assets3d.json`: HDRIs, materials, models from Poly Haven, ambientCG, Kenney (CC0) and Rive `.riv` files — only what is downloaded on this machine.
- `prompts.json`: 6,700+ website templates (GetLayers, MotionSites, Aura). Most are links only; entries with `has_prompt_text` include the text.
- Example prompts: `L/assets/PROMPT_EXAMPLES.md`. Pre-delivery website checklist: `L/assets/checklists/CHECKLIST.md`.

Filter with `jq` or `python3 -c`, e.g. `jq '.[]|select(.lib=="React Bits" and .cat=="Backgrounds")|.name' L/tool/data/components.json`.

## Not stored in the repo — download on demand
- **Font files** (`L/assets/font/google-fonts/repo/`): the list is in `fonts-index.json`; fetch files with `python3 -I L/scripts/download_fonts.py "Font Name"` (or `--vietnamese`, `--all`). If a font in `fonts.json` has no file locally, download it first.
- **3D materials** (`L/assets/3d-materials/`): see `L/assets/3d-materials/README.md`. For one asset, prefer the source site (polyhaven.com, ambientcg.com, kenney.nl/assets, all CC0). Whole collections: `L/scripts/download_polyhaven.py`, `download_ambientcg.py`, `download_kenney.py` (large; use `--limit N`).

## Rules
1. **Prefer library assets** over writing from scratch or downloading from the web. Read the source's `README.md` / `REFERENCE.md` first.
2. **Copy files into the project.** Never import directly from `L`. React components: copy the `.tsx` into `components/`. Fonts: copy into `public/fonts` or use `next/font`.
3. **Pick Vietnamese-capable fonts** (`vi: true`) for any Vietnamese page.
4. **Respect licenses:**
   - Rive (CC BY), Mockuphone (CC BY 3.0) and unDraw need attribution — add a credit line in the footer or About page and tell the user.
   - React Bits, Shadcnblocks (Commons Clause), Aceternity and lucide-animated may be used in websites but the libraries must not be redistributed.
   - Never publish or share the whole library; the GitHub repo must stay private.
5. **The user is not a developer.** Explain simply and always name the file paths you used.
6. After adding assets, run `python3 L/scripts/build_tool.py` to refresh the data, then commit and push (`git -C L add -A && git -C L commit -m "..." && git -C L push`) so other machines get it.

Lookup page for the user: double-click `L/OPEN_TOOL.command`; it opens `http://localhost:8765/tool/`.
