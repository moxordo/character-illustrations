# SVG Backend — Author, Render, Iterate

The default backend in Claude Code (no image-gen tool needed). Advantages: label text is always exact (no model typos), sources stay editable, and iteration is deterministic — edit the SVG, re-render.

## 1. Author the SVG

Canvas skeleton (1600×900 = 16:9):

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <filter id="wob1" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="7" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="6"/>
    </filter>
    <!-- duplicate with different seed per major group so edges don't repeat -->
  </defs>
  <rect width="1600" height="900" fill="#ffffff"/>
  <g filter="url(#wob1)"><!-- line art group --></g>
  <g><!-- text labels: NO wobble filter — keep text crisp --></g>
</svg>
```

Conventions:

- **Wobble**: `feTurbulence + feDisplacementMap` on each line-art group; vary `seed` between groups. Never apply it to `<text>` — the hand font already looks handwritten, and displacement garbles glyphs.
- **Strokes**: `stroke="#111"`, width 2.5–3.5, `fill="none"`, `stroke-linecap="round"`, `stroke-linejoin="round"`. Keep lines thin; no heavy outlines.
- **Fonts**: `font-family="'Bradley Hand', 'Comic Sans MS', cursive"` (Bradley Hand ships with macOS). CJK handwriting fonts are often download-on-demand and absent — check before relying on them. Chinese: `'Hannotate SC', 'Kaiti SC', sans-serif`. Korean: `'Nanum Pen Script', 'Apple SD Gothic Neo', sans-serif` (falls back to the clean sans; a slight per-label `rotate(-1..2)` keeps it from feeling sterile). Minimum ~20px at this canvas; labels in the character profile's palette colors get `fill` only, no stroke.
- **Character**: follow the active profile's **SVG recipe** section. Build clean shapes — the wobble filter supplies the hand-drawn irregularity.
- **Accents**: use the profile's exact hexes; check style-dna.md for what each accent is allowed to mean.
- Dashed strokes (`stroke-dasharray="6 7"`) read as "sketchy guide line" — good for motion paths and secondary flows.

## 2. Render with headless Chrome

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --hide-scrollbars \
  --window-size=1600,900 --force-device-scale-factor=2 \
  --default-background-color=FFFFFFFF \
  --screenshot="$PWD/out.png" "file://$PWD/fig.svg"
```

Produces a 3200×1800 PNG. The `width`/`height` attributes on the `<svg>` element are required so Chrome sizes it to the viewport exactly.

## 3. QA loop

Read the rendered PNG and run `references/qa-checklist.md`. Fix in the SVG (positions, collisions, density, colors), re-render, re-check. Typical SVG-specific issues: label/stroke collisions, elements clipped at edges, a group missing its wobble filter (reads as sterile vector), text too small after downscaling for chat preview.

## 4. Watermark and file layout

- If the profile defines a watermark, apply it to the rendered PNG with `scripts/add_watermark.py` (Pillow required — no system-wide install exists; use a venv: `python3 -m venv /tmp/wm-venv && /tmp/wm-venv/bin/pip install Pillow`).
- Final watermarked PNGs → `~/Downloads/<character>-illustrations/NN-topic.png` (one shared folder per character, numbering continues across batches — list the folder to find the next `NN`).
- Editable SVG + unwatermarked PNG → `~/Downloads/<character>-illustrations/sources/NN-topic.svg|.png`.
