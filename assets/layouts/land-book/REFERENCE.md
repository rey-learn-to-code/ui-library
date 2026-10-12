# Land-book — reference (link only)

- Site: https://land-book.com/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A curated collection of websites, updated daily: landing pages, portfolios, blogs, e-commerce, templates.
- Has separate areas for **Sections** (single blocks only: hero, pricing, FAQ...), **Mobile**, **Motion** (pages with animation), **OG Images** and **Headlines** (good headlines).
- Good for: choosing the overall layout of a landing page and comparing different ways to place the hero/pricing/footer.

## How to browse / filter
- Top bar: Websites / Sections / Mobile / New / Motion / OG Images / Headlines.
- Filter by page type: Landing, Portfolio, Blog, Ecommerce, Other; by sub-page type: About Us, Career, Sign Up, Pricing, Case Study, Blog Post, Product listing, Product page.
- **Filters** button (color, style, industry...) — some advanced filters are part of the Pro plan.
- Each card links to the original website → open the original site to see the real layout and real responsive behavior.

## Notes
- Some entries are paid templates (Webflow/Framer, with a price) mixed in — watch for the "Buy $.." label.
- The site has bot protection; browse it manually in a browser only.

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
