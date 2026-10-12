# CodePen — reference (link only)

- Site: https://codepen.io/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- The biggest front-end code playground: millions of "Pens" (HTML/CSS/JS) with effects, animations, layouts, components and shaders.
- Good for: finding a specific effect someone has already built, seeing the code right next to the result, and forking it to experiment.

## How to browse / filter
- Search box (search by keyword: "glassmorphism card", "scroll text reveal", "gsap marquee"...) → filter by Pens / Projects / Collections.
- Trending / Picks / Challenges sections show standout pens; follow skilled authors.
- Open a Pen → see the 3 panels HTML/CSS/JS; the Settings button shows which external libraries are loaded (GSAP, Three.js...).
- You can view without logging in; forking/saving needs an account.

## Notes
- **License**: public Pens are MIT by default (according to CodePen's license page) unless the author says otherwise or is a PRO member who made it private — always check the license/author note in the Pen before using it, and keep the copyright notice.
- This site could not be re-checked directly today (automated access is blocked); see https://blog.codepen.io/documentation/licensing/ to be sure.

## Sample prompt: have AI learn an effect from a reference demo

```text
Here is a reference effect demo: <DEMO_URL> (source: <GITHUB/CODEPEN_URL if any>, license: <MIT/...>).
1. Briefly explain how the effect works (technique: CSS transition, clip-path, SVG filter, GSAP ScrollTrigger, WebGL shader...).
2. Re-implement it as <a React + TypeScript component | plain HTML/CSS/JS snippet> for my project, applied to <element: CTA button / product image grid / hero headline>.
3. Use <GSAP | Motion | plain CSS>. Respect prefers-reduced-motion and avoid layout shift (animate transform/opacity where possible).
4. If you adapt MIT-licensed source, keep its copyright notice in the file.
```
