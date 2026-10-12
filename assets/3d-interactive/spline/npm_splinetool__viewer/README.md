# `<spline-viewer>`

Check out the demos and examples at [viewer.spline.design](https://viewer.spline.design).

## Quickstart

```html
<!-- Import the component -->
<script
	type="module"
	src="https://cdn.spline.design/@splinetool/viewer/build/spline-viewer.js"
></script>

<!-- Use it like any other HTML element -->
<spline-viewer
	url="https://prod.spline.design/iEAs8HJFu91daMOq/scene.splinecode"
></spline-viewer>
```

## Installing

The `<spline-viewer>` web component can be installed from [NPM](https://npmjs.org):

```sh
npm install @splinetool/viewer
```

It can also be used directly from our free CDN (pin a version with
`@splinetool/viewer@<version>`):

```html
<script
	type="module"
	src="https://cdn.spline.design/@splinetool/viewer/build/spline-viewer.js"
></script>
```

## Engine-specific builds

The default `spline-viewer.js` contains both rendering engines and
auto-selects per browser: WebGPU wherever the browser provides it, WebGL
everywhere else. If your scene was exported for a single engine (the
`Renderer` setting in the export panel), you can load a smaller build that
only contains that engine — the export panel's code snippet picks the right
file for you:

- `build/spline-viewer.js` — WebGPU + WebGL, auto-select (the default; use
  it for scenes exported with `Renderer: Both`).
- `build/spline-viewer.webgl.js` — WebGL only (~34% smaller).
- `build/spline-viewer.webgpu.js` — WebGPU only (~20% smaller). Browsers
  without WebGPU show a "requires WebGPU" notice, as there is no WebGL
  fallback in this file.

On the single-engine builds the `renderer` attribute is ignored (with a
console warning when it asks for the engine the file doesn't contain).

## Options

### `url`

The url of your Spline export. ex: `https://prod.spline.design/6Wq1Q7YGyM-iab9i/scene.splinecode`.

### `width` (optional)

The desired width of the viewer in pixels. Ex: `width="400"`.

### `height` (optional)

The desired height of the viewer in pixels. Ex: `height="400"`

### `background` (optional)

A css like color that will override the background color of your scene as it was set in the editor. Ex: `background="#ff0000"`.

### `renderer` (optional)

The rendering engine used by the viewer. Possible values are `auto`, `webgpu` and `webgl` (`webgl2` is accepted as an alias of `webgl`). By default (`auto`) the runtime picks the engine per browser: WebGPU wherever the browser provides it — honoring the `Renderer` setting the scene was exported with — and WebGL everywhere else. Set `renderer="webgl"` to force the classic WebGL engine, or `renderer="webgpu"` to force the WebGPU one. Ex: `renderer="webgl"`.

Only meaningful on the default dual-engine `spline-viewer.js` build: the single-engine builds (see [Engine-specific builds](#engine-specific-builds)) contain one engine and ignore this attribute, logging a console warning when it asks for the other engine.

### `loading` (optional)

This option controls the agressiveness of the preload of your scene. Possible values are `auto`, `lazy` and `eager`. By default (`auto`) the behavior is to `lazy` load the scene and only start to preload when the tag enters the viewport. If you need to start loading immediately then you can set `loading="eager"` instead.

### `loading-anim` (optional)

When true (default is false), this option displays a simple spinner preloader during the loading of the spline file.

### `loading-anim-type` (optional)

The type of preloading animation to be displayed while the scene is loading. If undefined no animation is used. Value can be `spinner-small-dark`, `spinner-small-light` ,`spinner-big-dark`, `spinner-big-light` or undefined.

### `unloadable` (optional)

When true (default is false), this options makes the viewer unload the spline element when it leaves the viewport.

### `events-target` (optional)

Values can either be `local` (events listened on the canvas) or `global` (events listened on the window).

### `hint` (optional)

When true (default is false), this option displays an overlay animation suggesting the user should use dragging in order to interact with the scene. This animation disappears as soon as user interacts.

## Events

You can listen for a few custom events on the `spline-viewer` element that are triggered at various moments of its lifecycle.

```js
const mySplineViewer = document.getElementById('MySplineViewer');
mySplineViewer.addEventListener('load-start', (e) => {
	console.log('loading started', e.detail.url);
});
```

### `viewport-intersection`

Triggered when the viewer enters or leaves the viewport. Event contains a `intersection:boolean` detail value.

### `context-loss`

Triggered when the webgl context of the canvas is lost.

### `load-start`

Triggered when the viewer starts loading a scene. Event contains a `url:string` detail value. Use This if you want to display a preloader during loading.

### `load-complete`

Triggered when the viewer finishes loading a scene. Event contains a `url:string` detail value. Use This if you want to display a preloader during loading.

### `unload`

Triggered when the current scene gets unloaded.

## Exporting for `<spline-viewer>` from Spline editor

If you want a scene to be loaded by the `<spline-viewer>` component, you need to export it from Spline editor using the `Spline Viewer` export type. First click on the Export button from the toolbar, then click on the `Spline Viewer` tab on the sidebar of the export modal. Finally click on update and when export is done you can copy paste the code snippet or the exported URL.

Check the [docs](https://docs.spline.design/67b4c8ec0d2b46dd8588a99a7e94db6e) for more details.

## Listening for events outside of the canvas

In case you need the events to be able to listen for your movements outside of the canvas (exemple: a look at event that follow your mouse outside of the canvas), you can set the `Mouse Events` option to `From full window` inside the `Spline Viewer` export options.

© 2025 Spline, Inc.
