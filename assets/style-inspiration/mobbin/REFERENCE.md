# Mobbin — reference (link only)

- Site: https://mobbin.com/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A UI/UX reference library from **real apps and websites** (according to the site: ~621,500 screens), including Apps, Sites, Screens, **Flows** (step-by-step user journeys: onboarding, sign-up, checkout, paywall...), Animations, UI Elements.
- Good for: designing product flows (not just landing pages) — see how big apps handle onboarding/checkout/settings.

## How to browse / filter
- Filter by platform (iOS, Android, Web), by app, by screen type/UI element, and by flow.
- Search in natural language (e.g. "paywall that makes upgrading feel worth it").
- Has an MCP so AI agents can access Mobbin — only on the Pro/Team plans.

## Notes
- **Account required**: "Join for free" gives limited viewing; the full library, image downloads and MCP need a paid plan. This library did NOT log in to or download anything from Mobbin.
- The screenshots show other companies' interfaces — use them for learning only, do not put them into your product.

## Sample prompt: learn a user flow

```text
I am designing a <onboarding | sign-up | checkout | paywall> flow for <APP_DESCRIPTION>.
Reference: the similar flow in <APP_NAME> (screenshots attached / described: <...>).
1. Summarize each step: goal, UI components, key copy, primary/secondary actions.
2. Point out good UX patterns (reduced friction, progress, confirmation, error/empty states).
3. Propose my flow (minimum steps) and build each screen in <React + Tailwind + shadcn/ui> with loading/empty/error states.
Do not copy the reference app's branding, copy or imagery.
```

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
