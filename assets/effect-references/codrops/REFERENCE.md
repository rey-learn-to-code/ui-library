# Codrops (tympanus.net/codrops) — reference (link only)

- Site: https://tympanus.net/codrops/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- A long-running creative front-end magazine: tutorials + **open-source demos** (hover, scroll animation, page transitions, WebGL/Three.js, GSAP, typography).
- **Demos Hub** (https://tympanus.net/codrops/demos/): according to the site, 500+ free demos, marked "free to use under MIT".
- Good for: learning "high-end" effects, with step-by-step articles and GitHub repos.

## How to browse / filter
- Demos Hub filters by tag (gsap, three.js, scroll, page transition, grid, typography, webgl...) — add `?tag=<tag-name>` to the URL.
- Sections: Tutorials / Articles / Collective (weekly link roundup) / Creative Hub.
- Each demo has 3 links: view the demo, read the article, GitHub source code.

## Notes
- Already saved in this library:
  - `DEMOS.md` + `demos-list.json`: 641 demos (title, demo link, article, GitHub, tags) from the Demos Hub.
  - `github-repos.json`: 347 public repos from github.com/codrops (stars, license).
  - `repos/`: the 30 most-starred repos that have an MIT LICENSE (each file checked) — see `repos/README.md`.
- 219 of 347 older Codrops repos **have no LICENSE file** → not cloned; even though the Demos Hub says MIT, read each demo's README/article before using it commercially.
- Demos by guest authors live in their own personal repos, with their own licenses.
- Images in the demos may have their own sources/credits — replace them with your own images.

## Sample prompt: have AI learn an effect from a reference demo

```text
Here is a reference effect demo: <DEMO_URL> (source: <GITHUB/CODEPEN_URL if any>, license: <MIT/...>).
1. Briefly explain how the effect works (technique: CSS transition, clip-path, SVG filter, GSAP ScrollTrigger, WebGL shader...).
2. Re-implement it as <a React + TypeScript component | plain HTML/CSS/JS snippet> for my project, applied to <element: CTA button / product image grid / hero headline>.
3. Use <GSAP | Motion | plain CSS>. Respect prefers-reduced-motion and avoid layout shift (animate transform/opacity where possible).
4. If you adapt MIT-licensed source, keep its copyright notice in the file.
```
