# Realtime Colors — reference (link only)

- Site: https://www.realtimecolors.com/
- Status in this library: **link-only** — no screenshots or page content were downloaded (the images on the site are screenshots of other companies' websites and belong to them).
- Last checked: 2026-10-09

## What this site is good for
- Instantly preview **colors + fonts on a real sample website** (instead of looking at separate color swatches).
- According to the site: free ("100% Free! Forever"), 300K+ users; has a Figma plugin and a VS Code Theme Editor.
- Good for: settling on a 5-color set (text, background, primary, secondary, accent) + a heading/body font pair, and checking both light and dark.

## How to browse / filter
- Toolbar at the bottom of the page: adjust Text, Background, Primary, Secondary, Accent (each box shows a contrast ratio); pick heading/body fonts by group (Serif, Sans Serif, Handwriting, Monospace, Display).
- Shortcuts: Space = random colors; Alt+T = switch Dark/Light; ←/→ = undo/redo; Ctrl+E = Export. Choose a color scheme type: Monochromatic, Analogous, Complementary, Split Complementary, Triadic, Tetradic.
- Has a Templates section (many sample layouts to try colors on) and a Dashboard.
- **Export** (Ctrl+E): CSS, Tailwind CSS, SCSS, Custom Code, Shades, Gradients, QR, download .zip/.png; color formats HEX/RGB/HSL/OKLCH → paste straight into your project.
- The URL contains the color codes → save/share a palette by copying the link.

## Notes
- No login needed for basic use.

## Sample prompt: bring a color palette into a website

```text
My palette: <HEX1, HEX2, HEX3, HEX4, HEX5> (from <Coolors/Realtime Colors>).
1. Assign roles: background, foreground/text, primary, secondary, accent, muted, border; generate a 50–950 scale for primary.
2. Check WCAG AA contrast for body and large text; if a pair fails, suggest the nearest passing shade.
3. Export as (a) CSS variables in :root and .dark, (b) Tailwind config (theme.extend.colors) or shadcn/ui theme variables (HSL/OKLCH).
4. Produce a matching dark mode.
```
