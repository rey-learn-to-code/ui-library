# Website checklist before you send the link

All the tools below work online or are built into the browser, so this library only stores links and instructions; nothing is downloaded to your computer.

Work through 4 steps in order: (1) text colors are easy to read, (2) the page is easy for everyone to use, (3) the layout doesn't break on phones, (4) images are light so the page loads fast.

---

## 1. Is the text clear enough? (contrast)

Tool: https://webaim.org/resources/contrastchecker/ (free, no account needed)

"Contrast" is how different the text color is from the background color. The bigger the difference, the easier the text is to read, especially in bright sunlight or for people with weaker eyesight.

How to do it:
1. Open your CSS file and find the text color code (for example `color: #6b7280`) and the background color code (for example `background: #ffffff`).
2. Paste the text color into the **Foreground** box and the background color into the **Background** box.
3. Read the result:
   - Normal text (paragraphs, buttons, input boxes): needs **WCAG AA ≥ 4.5:1**, meaning it shows **Pass**.
   - Large text (from about 24px, or 18.66px bold): only needs **≥ 3:1**.
   - Input box borders and important icons: should be **≥ 3:1**.
4. If it shows **Fail**: drag the "Lightness" slider to make the text darker or the background lighter, then copy the new color code into your CSS.

Color pairs to check:
- [ ] Main text / page background
- [ ] Secondary text (light gray) / page background. This is the one that fails most often.
- [ ] Text on the main button / button color
- [ ] Text on cards / card background
- [ ] Links / page background
- [ ] If the site has a dark theme (dark mode): check all the pairs above again

Tip: `assets/colors/generated-palettes/palettes.json` has ready-made color sets with contrast already calculated. If you use Radix Colors (`assets/colors/radix-colors/`), use step 11 or 12 for text on a step 1 or 2 background.

---

## 2. Is the page easy for everyone to use? (accessibility)

Tool: https://wave.webaim.org/ (paste the link of a page that's already online). The Chrome/Firefox extension version works with pages still running on your own computer (localhost).

"Accessibility" means that blind people using screen-reader software, people who only use a keyboard, and older people can all use the page.

How to do it:
1. Go to wave.webaim.org, paste the website address and press Enter.
2. Look at the panel on the left:
   - **Errors** (red): must be fixed.
   - **Contrast Errors**: text colors aren't clear enough, go back to Step 1.
   - **Alerts** (yellow): worth reviewing, not required.
3. Click each icon on the page to see where the problem is, then copy the error description and give it to AI to fix.

Common problems and how to fix them:
- [ ] Image missing `alt`: add a short description, for example `<img src="..." alt="White T-shirt product photo">`. If an image is only decoration, write `alt=""`.
- [ ] Input box without a label: every `<input>` needs a `<label for="...">`.
- [ ] Icon-only button: add `aria-label="Open menu"`.
- [ ] Headings skip levels (from h1 to h4): reorder them as h1, h2, h3.
- [ ] Missing `lang`: for a Vietnamese site, use `<html lang="vi">` (use `lang="en"` for an English site).
- [ ] Links that only say "click here": change the text so it says clearly where the link goes.

Check yourself with the keyboard too (no tool needed):
- [ ] Press **Tab** repeatedly: you can reach every button and link, and you can always see an outline showing where you are.
- [ ] You can open the menu and close dialogs (popups) with **Enter** or **Esc**.
- [ ] Forms show errors clearly: see the example at `assets/ui-states/govuk-error-summary/demo.html`.

---

## 3. Does the layout break on phones?

Tool: Chrome DevTools, Device Mode, built into Chrome. Guide: https://developer.chrome.com/docs/devtools/device-mode

"DevTools" is a set of tools for web makers, built into Chrome. "Device Mode" imitates a phone screen right on your computer.

How to do it:
1. Open the website in Chrome.
2. Press **F12** (on Mac: **Cmd + Option + I**).
3. Press **Ctrl + Shift + M** (on Mac: **Cmd + Shift + M**), or click the phone/tablet icon in the top corner.
4. In the top bar, pick a device (iPhone SE, iPhone 14 Pro Max, Galaxy...) or pick "Responsive" and drag the edge to change the width.
5. Try these widths: **320px** (the smallest phones), **375px**, **390px**, **768px** (tablet), **1280px** (desktop).

What to check:
- [ ] No horizontal scrollbar. If there is one, some element is wider than the screen.
- [ ] Text isn't too small: paragraphs are 16px or larger.
- [ ] Buttons are big enough to tap with a finger (about 44×44px) and aren't crammed together.
- [ ] Images and videos shrink to fit the screen. Add the CSS `img, video { max-width: 100%; height: auto; }`.
- [ ] The menu collapses into a ☰ button and opens properly.
- [ ] Wide data tables are wrapped in their own horizontally scrolling box: `<div style="overflow-x:auto">`.
- [ ] The HTML file has the line `<meta name="viewport" content="width=device-width, initial-scale=1">`.

Tip for finding the element that overflows sideways: in DevTools, open the **Console** tab, paste the line below and press Enter. Overflowing elements will get a red outline.

```js
document.querySelectorAll('*').forEach(el => { if (el.scrollWidth > document.documentElement.clientWidth) el.style.outline = '2px solid red'; });
```

Extra check: the **Lighthouse** tab in DevTools, choose **Mobile**, then click **Analyze page load**. You'll get scores for Performance, Accessibility and SEO.

---

## 4. Compress images so the page loads fast

Images are usually the heaviest part of a page. Try to keep each image under about **200 KB**; large background images under about **400 KB**.

### The easiest way: Squoosh (in the browser)

- https://squoosh.app/: free. Images are processed **on your own computer, not uploaded to a server**.
- Drag an image onto the page. In the right-hand column, choose the **WebP** or **AVIF** format and a quality of about **70–80**. Drag the middle slider to compare before and after, then click the download button.
- If the image is too big, turn on **Resize** and set the maximum width to about **1600px**. Images inside small cards only need about **800px**.
- Open source (Apache-2.0): https://github.com/GoogleChromeLabs/squoosh

A note on the command-line version of Squoosh: the packages `@squoosh/cli` / `npx @squoosh/cli` (last version 0.7.3, from 2023) and `@squoosh/lib` are **no longer maintained**. Their package page says "Project no longer maintained". Don't use them for new projects.

### Compressing many images at once with a command (instead of squoosh-cli)

The "command line" means typing commands into Terminal instead of clicking with the mouse.

- **sharp-cli** (uses the sharp library, actively maintained). Run the command inside the folder that holds your images:
  ```bash
  npx sharp-cli -i "images/*.jpg" -o images-webp/ -f webp -q 78 resize 1600
  ```
- **cwebp** (Google's official WebP tool). On Mac, install it with `brew install webp`:
  ```bash
  cwebp -q 78 -resize 1600 0 photo.jpg -o photo.webp
  ```
- **avifenc** (AVIF, smaller than WebP). Install with `brew install libavif`: `avifenc -q 60 photo.jpg photo.avif`
- In a Next.js project: use the `<Image>` component from `next/image` to compress and convert formats automatically.

(In these commands, `images` and `photo` are example names. Replace them with your own.)

### Other online tools (links only)

- https://www.iloveimg.com/: crop, resize and compress many images at once. **Images are uploaded to their servers**, so don't use it for private photos or client photos.
- https://www.photopea.com/: layer-based photo editing like Photoshop, right in the browser. The free version has ads. Export with **File → Export as → WEBP/JPG**.

### Image checklist
- [ ] Converted to WebP or AVIF (photos), or SVG (logos, icons).
- [ ] Images aren't more than 2 times larger than the space they're shown in.
- [ ] Images have `width` and `height` (or `aspect-ratio`) so the page doesn't jump when they finish loading.
- [ ] Images below the first screen have `loading="lazy"`.
- [ ] The big image at the top of the page (hero) does **not** use `lazy`, and has `fetchpriority="high"`.

---

## Quick summary before sending the link

- [ ] Contrast passes AA (WebAIM Contrast Checker)
- [ ] WAVE shows no red errors
- [ ] The site works with the Tab key
- [ ] No horizontal scrollbar at 320px width
- [ ] Images are compressed (Squoosh / sharp-cli / cwebp)
- [ ] Lighthouse Mobile: Performance and Accessibility both above 90
