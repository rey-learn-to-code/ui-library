# Rive Marketplace – interactive animations (.riv)

Source: https://rive.app/marketplace/ — status: **a curated set of 70 files downloaded**.

## What was downloaded
- `riv/` – 70 public `.riv` files (the exact files the marketplace uses to play its previews, downloadable without logging in):
  the 30 most-liked featured files + files found by searching for the keywords icon, button, loader, toggle, hover.
- `thumbs/` – a preview image for each file.
- `rive-index.json` – details for each file: name, author, original page link, **license**, tags, artboard name, state machine/animation names.
- `runtime/` – the Rive player (MIT): `rive.js` + `rive.wasm` (from `@rive-app/canvas` 2.44.1), plus the `.tgz` packages of `@rive-app/canvas` and `@rive-app/react-canvas` 4.36.0.

## License – remember to give credit
All 70 files are **CC BY 4.0**: commercial use and modification are allowed, but you **must credit the author**
(for example: "Animation 'Bubble Button' by <author> – rive.app, CC BY 4.0"). Author names are in `rive-index.json`.
The downloaded files are runtime (playback) files and cannot be opened for editing in the Rive editor; to edit one, click "Remix" on the website (requires an account – you do this yourself).

## Using it in plain HTML
```html
<canvas id="c" width="400" height="400"></canvas>
<script src="runtime/rive.js"></script>
<script>
  new rive.Rive({
    src: "riv/24900-46503-bubble-button.riv",
    canvas: document.getElementById("c"),
    autoplay: true,
    stateMachines: "State Machine 1",   // use the exact name from rive-index.json
    onLoad: function () { this.resizeDrawingSurfaceToCanvas(); }
  });
</script>
```
The `rive.wasm` file must sit next to `rive.js` (or let the library fetch it from a CDN). You must open the page through a web server (for example `npx serve`), not by opening the file directly.

## Using it in React
```bash
npm install @rive-app/react-canvas
```
```jsx
import { useRive } from "@rive-app/react-canvas";
export function BubbleButton() {
  const { RiveComponent } = useRive({
    src: "/riv/24900-46503-bubble-button.riv",   // put the file in the public/riv/ folder
    stateMachines: "State Machine 1",
    autoplay: true,
  });
  return <RiveComponent style={{ width: 300, height: 300 }} />;
}
```
