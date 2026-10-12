# Lapa Ninja — reference (link only)

- Site: https://www.lapa.ninja/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- More than 7,300 landing pages (since 2015) and 15,000+ full-page screenshots, with screen-recording videos.
- Very detailed categories by industry (Software, AI, Health & Fitness, eCommerce, Portfolio, Creative...).
- Good for: finding landing pages in the same industry as your project and learning how they arrange text, images and CTAs.

## How to browse / filter
- Home page: "Latest Web Design Inspiration"; each entry has an industry tag → click the tag to filter by category.
- Use the search box with industry/product keywords.
- "Visit Website" opens the original website. According to the site, unlimited access (categories, older versions, filters, search) comes with a paid plan.
- Besides the gallery there are design-learning sections and books/resources (with their own download terms).

## Notes
- Ads/sponsored entries are mixed in (Webflow, Framer...).
- Cloudflare blocks automated access — browse manually only.

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
