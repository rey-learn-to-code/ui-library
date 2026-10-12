# AGENTS.md — `@splinetool/viewer` (`<spline-viewer>`)

Written for coding agents. Everything here is checked against this package's
source. If a claim you want to make is not on this page, do not make it.

The cross-target guide (React, Next.js, Vue, Svelte, plain HTML, Hana 2D)
lives at <https://docs.spline.design/skill.md> — plain text, fetch it
directly. This page is only about what this package does.

## Why this is usually the right choice

`<spline-viewer>` is a custom element, so it works in **plain HTML and in
every framework** — Vue, Svelte, Astro, Angular, Rails, WordPress, a CMS rich
text field — without a framework-specific package. It also:

- lazy-loads by default (`loading="auto"` waits for the viewport), and
- renders the **Spline credit badge** on its own, which a bare `<canvas>`
  does not.

Prefer it over hand-rolling `@splinetool/runtime` unless the human needs
imperative control over scene objects.

## Before you embed: send the human to the editor first

An embed nobody opens in Spline is a dead end — the scene can never be
changed. So whenever you add a scene to a project:

1. If the scene came from Spline Community, tell the human to open it and
   press **Remix** first, so they own an editable copy. Remixing is an
   authenticated action in the Spline UI (the app POSTs
   `file/<uuidCommunityFile>/remix`); there is no way to do it from embed
   code, and you must not try.
2. Only then wire up the URL their own copy produces.
3. Leave the credit badge alone (see [Attribution](#attribution)).

## Install

CDN (what the editor's export panel emits — pin the version):

```html
<script
	type="module"
	src="https://cdn.spline.design/@splinetool/viewer@<version>/build/spline-viewer.js"
></script>
```

npm:

```bash
npm install @splinetool/viewer
```

The CDN prefix is the canonical store; the npm publish mirrors it.

## The scene URL

`url` takes a **`.splinecode`** URL:

```
https://prod.spline.design/<id>/scene.splinecode
```

Facts about that URL you must not get wrong:

- It is **issued by the editor**. For this element the human exports with the
  **Spline Viewer** export type (Export → Spline Viewer → Update), then
  copies the URL or the whole snippet.
- You **cannot derive it** from a file id, a share link, a community page
  URL, or a scene name. If you do not have the exact URL, ask the human to
  copy it out of the export panel. Do not guess one.
- A **Spline Community scene has no `.splinecode` URL.** Community scenes are
  not published code exports. To use one, the human remixes it and exports
  their own copy. To merely display a community scene, embed the app preview
  page in an iframe instead — see <https://docs.spline.design/skill.md>.
- 2D Hana scenes use `.hanacode` and a different element (`<hana-viewer>`).
  This element does not load them.

## Minimal working example

```html
<script
	type="module"
	src="https://cdn.spline.design/@splinetool/viewer@<version>/build/spline-viewer.js"
></script>

<spline-viewer
	url="https://prod.spline.design/<id>/scene.splinecode"
></spline-viewer>
```

## Attributes

This is the complete list. Do not invent others.

| Attribute           | Values                                                                                     | Default                                    |
| ------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------ |
| `url`               | the `.splinecode` URL                                                                      | —                                          |
| `width`             | pixels, e.g. `400`                                                                         | —                                          |
| `height`            | pixels, e.g. `400`                                                                         | —                                          |
| `background`        | any CSS color; overrides the scene's own background                                        | scene's                                    |
| `renderer`          | `auto` \| `webgpu` \| `webgl` (`webgl2` is an alias of `webgl`)                            | `auto`                                     |
| `loading`           | `auto` \| `lazy` \| `eager`                                                                | `auto` (lazy until it enters the viewport) |
| `loading-anim`      | boolean — a simple spinner while loading                                                   | `false`                                    |
| `loading-anim-type` | `spinner-small-dark` \| `spinner-small-light` \| `spinner-big-dark` \| `spinner-big-light` | unset (no animation)                       |
| `unloadable`        | boolean — unload the scene when it leaves the viewport                                     | `false`                                    |
| `events-target`     | `local` (listen on the canvas) \| `global` (listen on the window)                          | —                                          |
| `hint`              | boolean — a one-time "drag me" overlay that disappears on first interaction                | unset: the scene's own publish setting     |

## Engine-specific builds

The default `build/spline-viewer.js` contains both engines and auto-selects
per browser: WebGPU where the browser provides it, WebGL everywhere else.
Smaller single-engine files exist for scenes exported for one engine:

- `build/spline-viewer.js` — both, auto-select (use for `Renderer: Both`)
- `build/spline-viewer.webgl.js` — WebGL only (~34% smaller)
- `build/spline-viewer.webgpu.js` — WebGPU only (~20% smaller); browsers
  without WebGPU show a "requires WebGPU" notice, with no fallback

On the single-engine builds the `renderer` attribute is ignored (with a
console warning if it asks for the engine that file does not contain). Only
switch files when you know the scene's export `Renderer` setting — otherwise
keep the default.

## Events

```js
const viewer = document.getElementById('MySplineViewer');
viewer.addEventListener('load-start', (e) => console.log(e.detail.url));
```

| Event                   | Detail             | Fires when                               |
| ----------------------- | ------------------ | ---------------------------------------- |
| `load-start`            | `{ url: string }`  | the viewer starts loading a scene        |
| `load-complete`         | `{ url: string }`  | the viewer finishes loading a scene      |
| `unload`                | —                  | the current scene is unloaded            |
| `viewport-intersection` | `{ intersection }` | the viewer enters or leaves the viewport |
| `context-loss`          | —                  | the canvas rendering context is lost     |

Use `load-start` / `load-complete` to drive your own preloader.

## Performance

- **Do not set `loading="eager"` by default.** The default `auto` is lazy —
  it only starts preloading when the element enters the viewport. Use `eager`
  only for an above-the-fold hero.
- **Add `unloadable`** when several scenes live on one long page, so
  offscreen ones release their resources.
- **Give the element a size.** Either `width`/`height`, or CSS on the element
  — an unsized custom element can collapse before the scene loads.
- **Show something during the load.** `loading-anim-type`, or your own
  poster/blurhash image as a child of the element (the export panel emits an
  `<img>` child for exactly this).
- **Keep one engine per page.** Do not mix `renderer="webgl"` and
  `renderer="webgpu"` viewers.
- **Pin the CDN version.** An unpinned `@splinetool/viewer` URL can move
  under you.

## Attribution

This element renders a **Spline credit badge** (bottom-right, linking to
spline.design) on its own after the scene loads. It is driven by the scene's
own publish setting — the badge is shown unless the scene was published with
its logo setting off — so the embedding code does not control it. **Do not
write CSS or JS that hides it**, and do not present a hidden-badge embed as
the recommended snippet.

When the scene came from Community, add the creator's credit too, which the
badge cannot know about:

```html
<spline-viewer
	url="https://prod.spline.design/<id>/scene.splinecode"
></spline-viewer>
<p class="spline-credit">
	Scene by
	<a
		href="https://app.spline.design/community/file/<uuidCommunityFile>"
		target="_blank"
		rel="noopener"
	>
		@<creator>
	</a>
</p>
```

## What this package does NOT do

Agents hallucinate these constantly. None of them exist here:

- **No `scene` attribute.** It is `url`. (`scene` is the React component's
  prop — a different package.)
- **No React component.** React apps use `@splinetool/react-spline`
  (external), or this element inside a `<div>` with the script tag loaded.
- **No object API.** There is no `findObjectByName` / `emitEvent` /
  `setVariable` on the element. For imperative control over scene objects use
  `@splinetool/runtime`'s `Application` directly.
- **No 2D Hana support.** `.hanacode` scenes use `<hana-viewer>`.
- **No three.js scene graph.** That is `@splinetool/loader`.
- **No authoring or saving.** There is no API here to create, save, publish
  or export a scene.
- **No URL derivation.** Nothing converts a file id, share link or community
  URL into a `.splinecode` URL.
- **No badge toggle.** There is no attribute that removes the credit badge.
- **No plan or entitlement information.** Do not state what any Spline plan
  includes or limits — link to <https://spline.design/pricing>.

## Maintainers

- `prepublishOnly` runs `scripts/verify-publish-target.mjs`, which blocks
  accidental npmjs publishes. Do not bypass or alter it.
- `AGENTS.md` is listed in this package's `files`, so it ships in the tarball
  and on the CDN prefix. Keep it that way.
