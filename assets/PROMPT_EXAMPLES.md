# Example prompts for building websites with AI using the UI library

This file has 20 example prompts, all written in English. English prompts usually give more consistent results with Cursor, v0, Lovable, Bolt and Claude Code. (A "prompt" is the instruction text you type into an AI tool.)

## How to use them
1. Pick the example that fits what you need to do.
2. Replace the parts inside `<...>` with your own details.
3. Attach, or point to the path of, the assets in the library (the "Where to find it" column below).
4. Paste the whole prompt into the AI tool.

**Quick lookup: where things are** (paths start from the `ui-library/assets/` folder)

| What you need | Where to find it |
|---|---|
| Reference prompts or templates | `prompt-templates/` (getlayers, motionsites, aura-build: see `prompts-index.json`) |
| Example layouts | `layouts/` (land-book, lapa-ninja, curated-design). These are reference links |
| Styles, user flows | `style-inspiration/` (siteinspire, dark-design, mobbin) |
| Effects with code | `effects/` (reactbits, aceternity, magicui), `effect-references/codrops/repos/` (30 MIT repos) |
| Animation libraries | `motion/` (gsap, motion, animejs) |
| Buttons, forms, tables | `ui-kits/` (shadcn/ui, daisyUI, Flowbite), `ready-blocks/` |
| Icons | `icon/` (lucide, phosphor, heroicons), `animated-icons/` |
| Fonts | `font/` (google-fonts, fontshare, typewolf) |
| Colors, themes | `colors/` (radix-colors, coolors, realtimecolors), `shadcn-themes/` |
| Text sizes | `type-scales/` (typescale, utopia) |
| Photos, videos | `photos-videos/GUIDE.md` (Unsplash, Pexels, Pixabay: search by hand or call the API) |
| Backgrounds, illustrations, 3D, mockups | `nen/` (backgrounds), `3d-icons/`, `3d-interactive/`, `3d-materials/`, `mockup/` |
| Empty/error/loading states | `ui-states/` |
| Sample data | `sample-data/` |

**A general rule to add to every prompt:** only learn the layout and design spirit from reference sites. Don't copy other websites' text, logos, images or code. The website must be responsive (works on every screen size), meet WCAG AA contrast, and respect `prefers-reduced-motion`.

---

## 1. Build a hero section from a reference
```text
Build a hero section for <product> (<one-line description>) in the layout spirit of <reference URL>.
Stack: Next.js + Tailwind + shadcn/ui. Heading font <Satoshi from Fontshare | Inter>, body font <Inter>. Icons: Lucide.
Colours: background <#0B0B0F>, text <#F5F5F7>, accent <#7C5CFF>.
Include: small badge, two-line headline, subcopy, primary + secondary CTA, product image/mockup, customer logo row.
Add a staggered text reveal with Motion (disabled under prefers-reduced-motion).
```

## 2. A full landing page from a set of references
```text
Create a one-page landing page for <project>. Section order: Header, Hero, Logo cloud, Features (3–6 cards), How it works (3 steps), Testimonials, Pricing (3 tiers), FAQ, Final CTA, Footer.
Layout references: <URL 1> (hero), <URL 2> (pricing), <URL 3> (footer).
Use shadcn/ui (Button, Card, Accordion, Badge), Lucide icons, font <...>, palette <...>.
Write the copy in Vietnamese, concise and benefit-led.
```

## 3. Reuse a prompt from the template library and rebrand it
```text
Here is the original prompt I copied from <MotionSites/GetLayers> (used for my own project under their licence):
<<<PASTE PROMPT>>>
Keep the structure, motion and craft. Replace all branding with <brand>, copy with <description>, palette with <HEX...>, fonts with <...>.
Background video/image: swap for <my Pexels video / Unsplash image link>.
Output <a self-contained index.html | a Next.js component>.
```

## 4. Learn a layout from a reference URL
```text
Analyze <reference URL>: list sections, grid (columns, alignment), type scale, spacing, colours (estimated HEX), motion.
Then build a NEW page for <project> in the same spirit with my own content and imagery. Do not copy the original text, logos, images or code.
```

## 5. Turn a Codrops effect into a component
```text
Read the code in ui-library/assets/effect-references/codrops/repos/<RepoName>/ (MIT).
Re-implement the effect as a React + TypeScript component <ComponentName> using GSAP (ScrollTrigger if needed), with props <images, speed...>.
Apply it to <product image grid / page headline>. Keep the MIT notice in the file. Replace demo images with mine.
```

## 6. Add a ready-made effect (React Bits / Aceternity / Magic UI)
```text
In my Next.js + Tailwind project, add the <effect name> effect from <React Bits | Aceternity UI | Magic UI> (code in ui-library/assets/effects/<...>).
Place it in <section>. Map its colours to my existing theme variables. Check mobile performance and disable it under reduced motion.
```

## 7. Color palette → shadcn/Tailwind theme
```text
My palette: <HEX x5> (from Coolors/Realtime Colors). Assign background/foreground/primary/secondary/accent/muted/border roles.
Generate a 50–950 primary scale, check WCAG AA contrast, then export :root and .dark CSS variables in shadcn/ui theme format (OKLCH).
```

## 8. Font pairing and type scale
```text
Pick a font pairing for a <luxury / friendly / technical> brand with full Vietnamese diacritics support, from Google Fonts or Fontshare.
Build a fluid type scale with clamp() (Utopia style: ratio <1.25> mobile, <1.333> desktop) for h1–h6, body, small.
Output next/font config and CSS variables. Test with the sample "Tiếng Việt có dấu: ắ ặ ẫ ố ợ ữ ỹ" (Vietnamese with diacritics).
```

## 9. A consistent icon set
```text
Use only <Lucide | Phosphor (regular weight) | Heroicons outline> across the site. 20px inside buttons, 24px in feature cards, stroke 1.5.
Replace all existing icons/emoji with matching icons. Add aria-hidden to decorative icons and aria-label to icon-only buttons.
```

## 10. Pricing section
```text
Build a 3-tier pricing section (<Basic / Pro / Enterprise>) following <reference URL>. Monthly/yearly toggle (<20>% off yearly), highlighted middle tier, feature lists with Lucide Check/X icons, per-tier CTA, short FAQ below.
Show prices in VND using Intl.NumberFormat('vi-VN').
```

## 11. Live photos from the Unsplash/Pexels API
```text
Create /api/photos calling the <Unsplash|Pexels> API (key in env, never exposed to the client), cached for 1 hour.
Render an image grid with next/image and attribution per provider rules (see ui-library/assets/photos-videos/GUIDE.md). Unsplash: hotlink the returned URLs, add UTM params, and hit download_location when a user selects a photo.
```

## 12. Hero background video
```text
Add a hero background video using <compressed mp4 from Pexels/Pixabay>. autoplay muted loop playsinline, poster image, object-fit: cover, gradient overlay for AA-readable text.
Pause when off-screen (IntersectionObserver) and under reduced motion. Serve a lighter 720p source on mobile.
```

## 13. Scroll animations (GSAP/Motion)
```text
Add scroll-driven motion to this page: section titles fade up, subtle image parallax, staggered card grid reveal, count-up stats.
Use <GSAP + ScrollTrigger | Motion (whileInView)>. Animate transform/opacity only, disable under reduced motion, no layout shift (CLS = 0).
```

## 14. Decorative backgrounds (gradient, grid, noise)
```text
Create a decorative background for <hero/section> in a <blurred mesh gradient | SVG blob | noise grain | GetLayers-style WebGL gradient> style.
Lightweight CSS/SVG (<10KB), pointer-events: none, behind content, with a dark-mode variant.
```

## 15. Dark theme style
```text
Convert the UI to a dark theme inspired by <dark.design URL>: near-black background with a <blue/violet> tint, primary text #EDEDED, secondary text ≥4.5:1 contrast, 1px translucent borders, soft glow on the primary button, softly shadowed product shots.
Keep light mode as an option (next-themes).
```

## 16. Onboarding / sign-up flow learned from a real app
```text
Design a <n>-step <onboarding | sign-up | checkout> flow for <app>, referencing how <app name> does it (my own screenshots/description).
Per step: goal, components, copy, primary action. Build with React + shadcn/ui (Form, Input, Progress), zod validation, and loading/error/success states.
```

## 17. Empty, error and loading states
```text
For the <orders list> page add: loading skeletons (react-loading-skeleton or shadcn Skeleton), an empty state with illustration, title, guidance and action button (PatternFly empty-state pattern), and a GOV.UK-style error summary at the top of forms linking to each invalid field.
```

## 18. Device mockups and product showcase images
```text
Show my app screenshot (<path>) inside a pure-CSS <iPhone | MacBook | browser> frame (no copyrighted mockup images), with a subtle 3D tilt on hover and soft shadow. Responsive, with descriptive alt text.
```

## 19. Sample data for building the interface
```text
Generate mock data for <product page / dashboard>: <30> products (Vietnamese product names, VND prices, category, rating, image), user avatars via DiceBear, shaped like DummyJSON /products.
Save as data/mock.ts with TypeScript types so it can be swapped for a real API later.
```

## 20. Quality review before handover
```text
Audit the whole page against this checklist:
1) WCAG AA colour contrast (WebAIM Contrast Checker criteria) and WAVE-style accessibility errors: image alt, form labels, heading order, visible focus.
2) Responsive at 360, 390, 768, 1024, 1440px (Chrome DevTools Device Mode).
3) Performance: correctly sized images (WebP/AVIF, compressed with Squoosh), lazy loading, font-display: swap, no unused libraries.
4) Reduced motion and keyboard navigation.
List issues by severity and fix them directly.
```
