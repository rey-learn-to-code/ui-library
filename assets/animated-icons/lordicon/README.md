# Lordicon – animated icons (Lottie)

Source: https://lordicon.com/ — status: **partial** (only the player + a list of icon names, NO icon files).

## Why the icon files could not be downloaded
- Lordicon's free license (https://lordicon.com/licenses) is only granted **when you create an account**, with conditions:
  you must **credit the author**, you may not modify the icons (based on CC BY-ND 4.0, commercial use allowed),
  and CDN embeds are limited to 1 million loads. So this library does not bulk-download icon files.
- In addition, this computer blocks the domains `cdn.lordicon.com` and `media.lordicon.com` (they point to 127.0.0.1), so neither the JSON files nor the preview images could be downloaded.

## What is in this folder
- `lordicon-public-index.json` – 18,066 icons taken from lordicon.com's public sitemap: family (system / wired / doodle), style (outline, solid, flat...), name, icon page link, preview image link. This list **includes both free and paid icons** (the sitemap does not say which is which).
- `packages/` – the player (MIT license):
  - `lordicon.js` – a standalone build of `@lordicon/element` 3.0.2 (one file, drop it straight into HTML).
  - `lordicon-element-3.0.2.tgz` (new version) and `lord-icon-element-4.1.2.tgz` (old version, package name `lord-icon-element`).

## How to get a free icon
1. Log in to lordicon.com (you do this yourself) and pick an icon labeled Free.
2. Click "Embed" to get the embed code, or download the `.json` file into your website folder.
3. Add credit in the footer, for example: `Icons by Lordicon.com` (with a link to lordicon.com).

## Using it in plain HTML
```html
<script type="module" src="packages/lordicon.js"></script>
<lord-icon src="/icons/lock.json" trigger="hover" style="width:64px;height:64px"></lord-icon>
```
`trigger` decides when the icon plays: `hover` (mouse over), `click`, `loop` (repeats forever), `in` (when it appears on screen)...

## Using it in React
```bash
npm install @lordicon/element
```
```jsx
import { defineElement } from "@lordicon/element";
defineElement();               // call once, for example in main.jsx
export function LockIcon() {
  return <lord-icon src="/icons/lock.json" trigger="hover" style={{ width: 64, height: 64 }} />;
}
```
