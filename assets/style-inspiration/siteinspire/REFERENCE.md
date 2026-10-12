# Siteinspire — reference (link only)

- Site: https://www.siteinspire.com/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A long-running showcase of beautiful websites, leaning toward **typography, minimalism, editorial, studio/agency portfolios, architecture, fashion**.
- Each site lists the studio/agency that built it → handy for finding "the style of a particular studio".
- Good for: choosing an aesthetic mood and a way of using type for premium brands.

## How to browse / filter
- Popular Categories are split into 4 groups: **Styles** (Typographic, Minimal, Grid Layout, Unusual Layout...), **Types** (Portfolio, E-Commerce...), **Subjects** (Fashion, Art, Photography, Design & Art Direction...), **Platforms**.
- Each category shows how many sites it has (e.g. Typographic ~2,100, Minimal ~850).
- Pagination at the bottom (Page 1, 2, 3...). Has a "weekly edit" newsletter.

## Notes
- A Vercel Security Checkpoint blocks automated access — browse with a browser only.

## Sample prompt: have AI learn a layout / style from a reference URL

> Use this once you have picked a sample website on this site. Replace the parts inside `<...>`. The AI should only learn the **structure, spacing rhythm, text hierarchy and color scheme** — never copy the original site's text, logos, images or code.

```text
You are a UI designer and front-end developer. Analyze this reference website: <REFERENCE_URL>
(if you cannot open it, use the screenshots I attach).

1. List the sections top to bottom (name, purpose, grid layout: columns, alignment, image/text ratio).
2. Extract design tokens: type scale (px/rem), weights, line-heights, spacing scale, radii, shadows, colour palette (background, text, accent) as estimated HEX values.
3. Describe motion/interactions (hover, scroll, transitions) in words.
4. Then build a NEW page for my project: <PROJECT_DESCRIPTION>, following the same layout spirit but:
   - with my own copy, brand and imagery (use Unsplash/Pexels placeholders if needed),
   - without copying the original's text, logos, images or source code,
   - stack: <HTML + Tailwind CSS | Next.js + Tailwind + shadcn/ui>, font: <Inter / other>, icons: Lucide.
5. Make it responsive (375px, 768px, 1440px) and WCAG AA contrast compliant.
```
