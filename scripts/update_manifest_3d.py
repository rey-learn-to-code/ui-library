#!/usr/bin/env python3
"""Update catalog/manifest/3d_materials.json from the actual numbers on disk.
How to run:  python3 -I update_manifest_3d.py
"""
import json, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = os.path.join(ROOT, "assets", "3d-materials")
OUTF = os.path.join(ROOT, "catalog", "manifest", "3d_materials.json")
TOTAL = {"polyhaven": 997 + 867 + 521, "ambientcg": 2901 - 209, "kenney": 216}  # number of assets on the API when this script was written (2026-10-09)


def running(name):
    r = subprocess.run(["pgrep", "-f", name], capture_output=True, text=True)
    return bool(r.stdout.strip())


def stats(slug):
    d = os.path.join(BASE, slug)
    done, size = 0, 0
    for dp, dns, fns in os.walk(d):
        for f in fns:
            if f == ".done":
                done += 1
            try:
                size += os.path.getsize(os.path.join(dp, f))
            except OSError:
                pass
    return done, "%.1fGB" % (size / 1e9) if size > 1e9 else "%dMB" % (size / 1e6)


def entry(url, slug, script, license_, note_full, usage):
    done, size = stats(slug)
    bg = running(script)
    complete = done >= TOTAL[slug] * 0.99 and not bg
    cmd = "cd ui-library/scripts && nohup python3 -I %s > logs/%s.nohup.out 2>&1 &" % (script, slug)
    note = note_full % {"done": done, "total": TOTAL[slug]}
    if not complete:
        note += (" Downloading in the background, not finished yet." if bg else " Download not finished.") + " Resume with: `%s` (skips files already downloaded)." % cmd
    return {"url": url, "status": "downloaded" if complete else "partial",
            "local_path": "assets/3d-materials/" + slug, "license": license_,
            "size": size, "items": done, "notes": note, "usage": usage}


def main():
    data = [
        entry("https://polyhaven.com/", "polyhaven", "download_polyhaven.py", "CC0-1.0",
              "Downloaded %(done)s/%(total)s Poly Haven assets at 1k: HDRIs (.hdr + jpg preview), PBR textures (diff, nor_gl, rough, arm, ao, disp) and glTF models; list in index.json.",
              "Three.js/R3F: load HDRIs with RGBELoader or drei's <Environment files=\"..._1k.hdr\" />; load models with GLTFLoader/useGLTF; assign textures to MeshStandardMaterial. model-viewer: <model-viewer src=\"x_1k.gltf\" environment-image=\"y_1k.hdr\">."),
        entry("https://ambientcg.com/", "ambientcg", "download_ambientcg.py", "CC0-1.0",
              "Downloaded %(done)s/%(total)s ambientCG assets as unzipped 1K-JPG (PBR materials, decals, atlases; HDRIs as 1K .exr with tonemapped images; models as SQ-1K-JPG); Substance .sbsar skipped.",
              "Three.js/R3F: load the *_Color, *_NormalGL, *_Roughness, *_AmbientOcclusion maps with TextureLoader/useTexture and assign them to MeshStandardMaterial; for .exr HDRIs use EXRLoader or drei's <Environment files>."),
        entry("https://kenney.nl/assets", "kenney", "download_kenney.py", "CC0-1.0",
              "Downloaded %(done)s/%(total)s free Kenney packs (3D first, then 2D, Textures, Audio), unzipped into one folder per pack, License.txt kept.",
              "3D packs include Models/GLB or GLTF: use useGLTF (R3F), GLTFLoader (Three.js) or <model-viewer src=\".../Models/GLB format/x.glb\">. Use 2D/UI packs' PNG/SVG as normal images; play .ogg sounds with the <audio> tag."),
    ]
    os.makedirs(os.path.dirname(OUTF), exist_ok=True)
    with open(OUTF, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    for e in data:
        print(e["url"], e["status"], e["items"], e["size"])


if __name__ == "__main__":
    main()
