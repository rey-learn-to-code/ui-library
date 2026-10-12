# Coolors — reference (link only)

- Site: https://coolors.co/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A fast **color palette** generator: press the space bar to generate a random 5-color palette, lock the colors you like, and generate again.
- Also has a community palette library (Explore), palettes from a photo, a contrast checker, palette previews on sample interfaces, and a gradient maker.
- Good for: quickly picking 4–6 brand colors.

## How to browse / filter
- Generator: Space = generate colors; lock icon = keep a color; drag to reorder; adjust the shade/HSL of each color.
- Explore: search by color or keyword (e.g. "pastel", "dark"), sort by Trending/Popular.
- Export: URL, CSS, SVG, PNG, PDF, code (some advanced formats/features are part of the Pro plan).

## Notes
- A palette is just simple data (HEX codes) — use it freely; an account is only needed to save palettes.
- The site uses a Cloudflare bot check, so it could not be re-checked directly today; the description above is based on known public features and may change.

## Sample prompt: bring a color palette into a website

```text
My palette: <HEX1, HEX2, HEX3, HEX4, HEX5> (from <Coolors/Realtime Colors>).
1. Assign roles: background, foreground/text, primary, secondary, accent, muted, border; generate a 50–950 scale for primary.
2. Check WCAG AA contrast for body and large text; if a pair fails, suggest the nearest passing shade.
3. Export as (a) CSS variables in :root and .dark, (b) Tailwind config (theme.extend.colors) or shadcn/ui theme variables (HSL/OKLCH).
4. Produce a matching dark mode.
```
