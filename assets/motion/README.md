# Animation with code: GSAP, Motion, Anime.js

This folder contains 3 libraries for adding movement (animation) to websites, already downloaded to this computer (on 2026-10-09).

> A "library" is like a ready-made toolbox: you don't have to write the animation math yourself, you just call a command such as `animate(...)`.

| Library | Version | License | Folder |
|---|---|---|---|
| GSAP (with ScrollTrigger, SplitText, Flip, MorphSVG...) | 3.15.0 | GSAP Standard "no charge" license (free, with its own terms) | `gsap/` |
| Motion (formerly called Framer Motion) | 14.0.0 | MIT | `motion/` |
| Anime.js | 4.5.0 | MIT | `animejs/` |

## What's in each folder

- `gsap/npm_gsap/` – the full npm package. The files you can use directly in HTML are in `gsap/npm_gsap/dist/` (for example `gsap.min.js`, `ScrollTrigger.min.js`).
- `gsap/repo_GSAP/` – the source code from GitHub greensock/GSAP (this repo has no demo folder; the official demos live on gsap.com and CodePen).
- `gsap/LICENSE_GSAP_standard-license.txt` – the GSAP license text. In short: free to use for websites and apps, including commercial ones; you may **not** use GSAP to build a drag-and-drop animation builder that competes with Webflow.
- `motion/npm_motion/` – the `motion` package (works for both plain HTML and React). File for a `<script>` tag: `motion/npm_motion/dist/motion.js`.
- `motion/npm_framer-motion/` – the `framer-motion` package (the old name, still used by older React projects).
- `motion/repo_motion_examples/` – examples taken from the motiondivision/motion repo: `dev/react/src/examples/` (about 150 React examples) and `dev/html/public/examples/`, `dev/html/public/animate-layout/` (HTML examples).
- `animejs/npm_animejs/` – the npm package. File for a `<script>` tag: `animejs/npm_animejs/dist/bundles/anime.umd.min.js`.
- `animejs/repo_anime/examples/` – 24 ready-made examples (each folder has an `index.html` + `index.js`), such as scrolling text, SVG line drawing, a draggable carousel, and page scrolling.

Note: the examples are kept as they are so you can **read them for reference**; don't run `npm install` inside the downloaded folders.

---

## Option 1: Plain HTML website (no React)

You only need to add a `<script>` tag near the end of your `index.html` file, just before `</body>`.
You have 2 choices: use a local file (copy the file into your project) or use a CDN (a free server on the internet that hands out the file).

### GSAP + ScrollTrigger (animation as you scroll the page)

```html
<!-- Using a CDN -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js"></script>
<!-- Or use local files: copy the 2 files from gsap/npm_gsap/dist/ into your js/ folder -->
<!-- <script src="js/gsap.min.js"></script> <script src="js/ScrollTrigger.min.js"></script> -->

<script>
  gsap.registerPlugin(ScrollTrigger);
  // Elements with the class "the" slide up and fade in when you scroll to them
  gsap.from(".the", {
    y: 60, opacity: 0, duration: 0.8, stagger: 0.15,
    scrollTrigger: { trigger: ".the", start: "top 80%" }
  });
</script>
```

### Motion (the HTML version)

```html
<script src="https://cdn.jsdelivr.net/npm/motion@14.0.0/dist/motion.js"></script>
<!-- Or the local file: motion/npm_motion/dist/motion.js -->
<script>
  const { animate, inView, stagger } = Motion;
  animate(".hop", { scale: [0.8, 1], opacity: [0, 1] }, { duration: 0.5, delay: stagger(0.1) });
  inView(".muc", (el) => { animate(el, { opacity: 1, y: [40, 0] }); });
</script>
```

Or as a module (modern browsers):

```html
<script type="module">
  import { animate } from "https://cdn.jsdelivr.net/npm/motion@14.0.0/+esm";
  animate("h1", { opacity: [0, 1] }, { duration: 1 });
</script>
```

### Anime.js v4

```html
<script src="https://cdn.jsdelivr.net/npm/animejs@4.5.0/dist/bundles/anime.umd.min.js"></script>
<!-- Or the local file: animejs/npm_animejs/dist/bundles/anime.umd.min.js -->
<script>
  const { animate, stagger } = anime;
  animate(".o-vuong", { x: 250, rotate: "1turn", delay: stagger(100), loop: true, alternate: true });
</script>
```

Note: Anime.js v4 is called differently from v3 (v3 uses `anime({...})`, v4 uses `animate(target, {...})`). When you ask AI to write code, say "Anime.js v4" clearly.

---

## Option 2: React project (Vite, Next.js...)

In a React project, you install the library with a command in the terminal, inside **your project folder** (not this library folder):

```bash
npm install gsap @gsap/react   # GSAP
npm install motion             # Motion
npm install animejs            # Anime.js
```

### GSAP in React

```jsx
import { useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";
gsap.registerPlugin(ScrollTrigger, useGSAP);

export default function Hero() {
  const box = useRef(null);
  useGSAP(() => {
    gsap.from(box.current, { y: 80, opacity: 0, duration: 1, scrollTrigger: box.current });
  }, { scope: box });
  return <div ref={box}>Hello</div>;
}
```

### Motion in React

```jsx
import { motion } from "motion/react";

export default function Card() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      whileHover={{ scale: 1.03 }}
      transition={{ duration: 0.5 }}
    >
      Product card
    </motion.div>
  );
}
```

Older projects that use `import { motion } from "framer-motion"` still work; new projects should use `motion/react`.

### Anime.js in React

```jsx
import { useEffect, useRef } from "react";
import { animate } from "animejs";

export default function Logo() {
  const ref = useRef(null);
  useEffect(() => {
    const a = animate(ref.current, { rotate: 360, duration: 1500, loop: true });
    return () => a.pause(); // clean up when leaving the page
  }, []);
  return <div ref={ref}>★</div>;
}
```

---

## Which library should you choose?

- **React + interface effects (fade in, hover, page transitions):** Motion – the shortest code.
- **Complex scroll-based animation, pinning sections, timeline-driven sequences:** GSAP + ScrollTrigger.
- **Text, SVG shapes, playful movement, lightweight plain HTML sites:** Anime.js.
- If a visitor has turned on "reduce motion" on their device, you should tone down effects with `@media (prefers-reduced-motion: reduce)` (Motion has `useReducedMotion` built in, GSAP has `gsap.matchMedia()`).

## Tips for asking AI

Give the AI the path to a specific example (for example `animejs/repo_anime/examples/svg-line-drawing/`) and say: "Make an effect like this example for my page's heading, using Anime.js v4".
