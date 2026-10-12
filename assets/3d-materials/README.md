# Free 3D materials (CC0)

This folder holds the "raw ingredients" for building 3D scenes on a website: 360-degree environment images (HDRIs), material surfaces (textures: wood, stone, fabric...), 3D models, and graphics/sound packs. Everything is licensed **CC0**: free to use for anything, including commercial work, and no credit is required.

## Not on GitHub: download it when you need it

This folder is **no longer uploaded to GitHub** (it is far too big). Instead, you re-download it on your own computer whenever you need it, using three small download programs (scripts) in the `scripts/` folder. Each script fetches files from one free source website:

| Script | Source website | What it downloads | Where it saves |
|---|---|---|---|
| `scripts/download_polyhaven.py` | https://polyhaven.com | All HDRIs, textures and models at 1k size | `assets/3d-materials/polyhaven/` |
| `scripts/download_ambientcg.py` | https://ambientcg.com | All materials, decals, HDRIs, 3D models... at 1K size (downloads a zip, unpacks it, then deletes the zip) | `assets/3d-materials/ambientcg/` |
| `scripts/download_kenney.py` | https://kenney.nl/assets | Every free asset pack (3D first, then 2D, Textures, Audio, then everything else), unpacked from its free zip | `assets/3d-materials/kenney/` |

Run them from the library root folder (`ui-library`):

```bash
cd ~/Documents/ui-library
python3 -I scripts/download_polyhaven.py
python3 -I scripts/download_ambientcg.py
python3 -I scripts/download_kenney.py
```

Tip: to try a script quickly first, add `--limit 5` to download only 5 items (for Poly Haven: 5 of each type).

**Removed on 2026-10-12 to save about 6 GB:**
- DirectX normal maps (files named `*NormalDX*`). Web tools such as Three.js use the OpenGL version (`NormalGL` / `nor_gl`), which is kept.
- Blender `.blend` files. Websites use glTF files (`.gltf` / `.glb`), which are kept.

## What's inside

| Folder | Source | Contents |
|---|---|---|
| `polyhaven/hdris/<name>/` | polyhaven.com | `<name>_1k.hdr` (environment image, used as the "sky" and lighting for a scene) + `<name>_tonemapped_1024.jpg` (preview image) |
| `polyhaven/textures/<name>/` | polyhaven.com | The 1k images of one material: `diff` (color), `nor_gl` (bumps and dents), `rough` (roughness), `arm`/`ao` (shadows in creases), `disp` (height) + `thumb.png` |
| `polyhaven/models/<name>/` | polyhaven.com | Model `<name>_1k.gltf` + a `.bin` file + a `textures/` folder + `thumb.png` |
| `ambientcg/<Type>/<name>/` | ambientcg.com | Types `Material`, `Decal`, `Atlas`...: 1K-JPG images (`_Color`, `_NormalGL`, `_Roughness`, `_AmbientOcclusion`, `_Displacement`). Type `HDRI`: a 1K `.exr` file + a `_TONEMAPPED.jpg` image. Type `3DModel`: the SQ-1K-JPG version |
| `kenney/<Category>/<pack>/` | kenney.nl | One folder per pack (3D, 2D, Textures, Audio, Other), each with a `License.txt`. 3D packs have a `Models/GLB format/` folder |

Each source has an `index.json` file (a list of its assets: ID, name, type, category, keywords, file paths) so you can search quickly. For example, to find HDRIs tagged "sunset":

```bash
cd ui-library/assets/3d-materials
python3 -I -c "import json;[print(e['files'][0]) for e in json.load(open('polyhaven/index.json')) if 'sunset' in e['tags']]"
```

Notes:
- Poly Haven: the full-size tonemapped image is about 24 MB per HDRI, so by default only the 1024px preview is downloaded. If you want the full version, add `--full-tonemapped`.
- ambientCG: Substance files (`.sbsar`) are skipped because they can't be used on the web. Zips are unpacked and then deleted.
- Any `.usdc`, `.tres` or `.fbx` files that come along are data for 3D software (Blender, Godot...). Websites don't need them.

## Resuming a download (if it stopped halfway)

You can run the download commands as many times as you like: files that are already fully downloaded are skipped. To run them in the background, open Terminal and run:

```bash
cd ~/Documents/ui-library/scripts
nohup python3 -I download_polyhaven.py > logs/polyhaven.nohup.out 2>&1 &
nohup python3 -I download_ambientcg.py > logs/ambientcg.nohup.out 2>&1 &
nohup python3 -I download_kenney.py    > logs/kenney.nohup.out 2>&1 &
```

- Watch progress: `tail -f logs/polyhaven.log` (same for `ambientcg.log`, `kenney.log`).
- Check whether they are still running: `pgrep -fl "download_(polyhaven|ambientcg|kenney)"`.
- Stop one: `pkill -f download_ambientcg.py` (swap in the matching name).
- Update the summary table after downloading: `python3 -I update_manifest_3d.py` (writes to `catalog/manifest/3d_materials.json`).

## Using them on a website

Copy the files you need into your web project's `public/` folder (the folder for static files that the browser can load directly), then:

**1. model-viewer (the easiest way, HTML only):**

```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js"></script>
<model-viewer src="/3d/ArmChair_01/ArmChair_01_1k.gltf"
              environment-image="/3d/hdri/aerodynamics_workshop_1k.hdr"
              camera-controls auto-rotate style="width:100%;height:400px"></model-viewer>
```

**2. React Three Fiber (React):** `npm install three @react-three/fiber @react-three/drei`

```jsx
import { Canvas } from '@react-three/fiber'
import { useGLTF, Environment, OrbitControls } from '@react-three/drei'

function Ghe() {
  const { scene } = useGLTF('/3d/ArmChair_01/ArmChair_01_1k.gltf')
  return <primitive object={scene} />
}

export default function Canh() {
  return (
    <Canvas camera={{ position: [0, 1, 2] }}>
      <Environment files="/3d/hdri/aerodynamics_workshop_1k.hdr" background />
      <Ghe />
      <OrbitControls />
    </Canvas>
  )
}
```

**3. Material textures (Three.js / R3F):** load the map images, then attach them to a material:

```jsx
import { useTexture } from '@react-three/drei'
const t = useTexture({
  map: '/3d/wood/Wood066_1K-JPG_Color.jpg',
  normalMap: '/3d/wood/Wood066_1K-JPG_NormalGL.jpg',
  roughnessMap: '/3d/wood/Wood066_1K-JPG_Roughness.jpg',
})
// <mesh><boxGeometry /><meshStandardMaterial {...t} /></mesh>
```

Note: use the `NormalGL`/`nor_gl` version (the correct format for Three.js), not `NormalDX`/`nor_dx` (those have been removed anyway). Load ambientCG's `.exr` files with `EXRLoader` (or drei's `<Environment files="...exr">`).
