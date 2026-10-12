# Curated (curated.design) — reference (link only)

- Site: https://www.curated.design/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A hand-picked gallery of websites "worth learning from", sorted by **industry** and **style**; has **Sections** and **Templates** areas.
- Good for: choosing sample websites for AI to learn layout from, especially tech products (AI, dev tools, SaaS, web3, fintech).

## How to browse / filter
- Browse bar by industry: Agency, Artificial Intelligence, Assets, Design Tools, Desktop Apps, Development Tools, E-commerce, Education, Finance, Marketing, Mobile Apps, Portfolio, Productivity, Tech, Web Apps, Web3.
- **Filters (Pro)**: Styles, Visuals, Attributes, Popular tags, Media (Animated/video or Static), Date added — pick several conditions, then Apply.
- Shortcut ⌘K for quick search across All / Websites / Sections / Templates.

## Notes
- Advanced filters are part of the Pro plan; browsing by industry and searching are free.

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
