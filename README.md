# UI Library

A private collection of free resources for building websites quickly, gathered from the 75 sources listed in `catalog/sites.json`, plus a lookup page that runs on your own computer.

> **New computer?** Follow **[SETUP.md](SETUP.md)**: a step-by-step guide from zero to a working library.

## Open the lookup page

Double-click **`OPEN_TOOL.command`**. Your browser opens `http://localhost:8765/tool/`. Keep the Terminal window open while you use the page; closing it stops the page.

If macOS blocks the file ("unidentified developer"), right-click it, choose **Open**, then choose **Open** again.

## What the lookup page has

| Tab | Contents |
|---|---|
| Catalog | The 75 sources: download status, license, what was collected, how to use it |
| Components | About 1,160 components (React Bits, Magic UI, shadcn/ui, Aceternity free, Shadcnblocks free, lucide-animated, daisyUI, Flowbite, Codrops demos). Click one to see and copy the code |
| Prompts | About 6,780 website templates from GetLayers, MotionSites and Aura, with links to the original pages |
| Icons | About 3,970 icons (Lucide, Phosphor, Heroicons). Click to copy the SVG code |
| Fonts | 2,031 Google Fonts, 543 of which support Vietnamese. Preview and copy CSS (font files must be downloaded first, see below) |
| Colors & Themes | 42 shadcn themes (tweakcn), accessible color palettes, type scales |
| Images | Generated SVG backgrounds, 3D icons, avatars, device frames |
| 3D | HDRIs, materials and models (Poly Haven, ambientCG, Kenney) and Rive animations. Only shows what is downloaded on this computer |
| Guides | How to use each source, a website checklist, 20 example prompts |

## Folders

| Folder | What's inside |
|---|---|
| `assets/<group>/<source>/` | The downloaded resources. Each source has a `README.md` or `REFERENCE.md` and its license file |
| `catalog/` | The master list of sources (`sites.json`) and `manifest/*.json` files describing each source |
| `tool/` | The lookup page. `tool/data/*.json` is generated automatically; don't edit it by hand |
| `scripts/` | Download scripts and `build_tool.py`, which refreshes the lookup page data |
| `claude-skill/` | The instructions that tell Claude Code how to use this library (installed by `install.sh`) |

Groups inside `assets/`: `3d-icons`, `3d-interactive`, `3d-materials`, `animated-icons`, `backgrounds`, `checklists`, `colors`, `effect-references`, `effects`, `font`, `icon`, `layouts`, `mockup`, `motion`, `photos-videos`, `prompt-templates`, `ready-blocks`, `sample-data`, `shadcn-themes`, `style-inspiration`, `type-scales`, `ui-kits`, `ui-states`.

## What is NOT on GitHub (download when needed)

Two folders are too big for GitHub. Their lists are kept, but the files are downloaded on demand:

| Folder | Size if fully downloaded | How to get it |
|---|---|---|
| `assets/font/google-fonts/repo/` | about 2.7 GB | `python3 -I scripts/download_fonts.py "Font Name"`, or `--vietnamese`, or `--all` |
| `assets/3d-materials/` | about 19 GB | One item: download it from the website. A whole collection: run a download script. See [assets/3d-materials/README.md](assets/3d-materials/README.md) |

## Handy commands

Run these in Terminal from inside the `ui-library` folder:

| Command | What it does |
|---|---|
| `bash update.sh` | Gets the newest version from GitHub |
| `bash save.sh "what changed"` | Uploads your changes to GitHub |
| `python3 scripts/build_tool.py` | Refreshes the lookup page after adding resources |

## License notes

- **Free to use (CC0, MIT, ISC, OFL):** Poly Haven, ambientCG, Kenney, 3dicons, Lucide, Phosphor, Heroicons, Google Fonts, shadcn, Magic UI, daisyUI, Flowbite.
- **Credit required:** Rive (CC BY 4.0, credit each author), Mockuphone (CC BY 3.0), and unDraw if added later. See `ATTRIBUTION.txt` in each source folder.
- **OK inside your websites, but never resell or share the whole set:** React Bits and Shadcnblocks (Commons Clause), Aceternity, lucide-animated.
- **This collection is for personal use only.** Keep the GitHub repository **private** and don't share the folder.

## Unfinished items

- **Fontshare:** the internet provider blocks this site's domain. Change the computer's DNS to 1.1.1.1, then run:
  `python3 -E scripts/font_fontshare.py assets/font/fontshare`
- **unDraw:** download the SVG files manually with a browser into `assets/illustrations/undraw-co/svg/`, together with unDraw's permission email.
