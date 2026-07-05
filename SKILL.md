---
name: character-illustrations
description: Generate hand-drawn, deadpan 16:9 concept illustrations starring a pluggable recurring character (peanut, xiaohei, or a custom character defined on the fly). This skill should be used when the user asks for a "peanut illustration", "xiaohei illustration", concept sketch, explainer figure, article/doc illustration, shot list, or any white-background hand-drawn visual metaphor starring a recurring character. Handles both a short prompt (one image) and a full article/doc (shot list, then a batch). Default rendering is local SVG + headless Chrome (exact text, editable sources); an image-gen prompt template is available as an alternative backend.
---

# Character Illustrations

## Overview

Turn one idea — a judgment, process, contrast, state, or metaphor — into a 16:9 hand-drawn concept illustration that reads in about one second: pure white background, wobbly black line art, lots of whitespace, restrained accent color, one idea per image.

The recurring character is **pluggable**. Each character lives as a profile in `characters/` (form, personality, action library, palette, SVG recipe, image-gen prompt block). The character must **perform the core action** of the image — if removing the character leaves the metaphor fully intact, the character is too decorative and the composition must be rewritten.

## Step 1: Resolve the character

1. **Named character** ("peanut", "xiaohei", "as <name>") → load `characters/<name>.md`.
2. **New character described** ("a deadpan mushroom", "our mascot: a grumpy cloud") → copy `characters/_TEMPLATE.md`, fill every section from the user's description (inventing sensible defaults for gaps), save as `characters/<slug>.md`, and state in the reply that the profile was saved for reuse.
3. **No character mentioned** → default to `peanut` and say so.

The profile's frontmatter carries the per-character config: palette mode, accent hexes, label language, watermark. Everything downstream reads from it.

## Step 2: Digest the input

- **Short prompt** → one image. Do not inflate a one-liner into a series.
- **Article / doc / Notion page** → extract the cognitive anchors (core judgments, breakpoints, input→output loops, before/after shifts, common pitfalls, role-state changes) and propose a **shot list**, default 4–8 images (1–3 for short pieces, hard ceiling 9). For each shot: where it sits in the doc, theme, core idea, structure type, what the character is doing, suggested elements, suggested labels.
- If the user only asked for planning/analysis, stop at the shot list. If the user clearly asked to generate, do not stop for confirmation.

## Step 3: Compose first, then draw

Before drawing each image, state in a few lines (enough for the user to catch a wrong take, not an essay):

- **Metaphor** — the fresh low-tech metaphor invented for this idea (see `references/composition-patterns.md`; never reuse a prior composition).
- **Character's action** — what the character is physically doing to drive the idea.
- **Labels** — the short handwritten labels that will appear, in the input's language unless the profile pins one. Label every actor in multi-actor scenes.
- **Composition** — where the character sits, the main object, how the eye moves.

## Step 4: Draw

Pick the backend:

- **SVG backend (default)** — follow `references/svg-workflow.md`: author the SVG (wobble filter, hand fonts, the profile's SVG recipe), render with headless Chrome at 2x. Use this in Claude Code; it guarantees exact label text and keeps editable sources.
- **Image-gen backend** — only when an image generation tool is actually available in the environment, fill `references/prompt-template.md` with the profile's prompt block and generate each image separately. Never combine multiple ideas into one generated image.

Style rules for both backends live in `references/style-dna.md`.

## Step 5: QA and iterate

Render, then **look at the output** (Read the PNG) and run `references/qa-checklist.md`. Regenerate or edit when the character is decorative, the canvas is over 60% full, it reads as a flowchart/PPT, labels collide or overflow, a type-title appears top-left, the style drifts cute, or an off-palette color creeps in.

## Step 6: Watermark, save, report

1. If the profile's `watermark` is not `none`, apply it with `scripts/add_watermark.py --text "<watermark>"` (needs Pillow; create a venv if none exists: `python3 -m venv /tmp/wm-venv && /tmp/wm-venv/bin/pip install Pillow`).
2. Save final PNGs to one **shared per-character folder**: `~/Downloads/<character>-illustrations/` — not a new per-topic folder. Continue the sequential numbering across batches (`01-topic.png`, `02-topic.png`, …): list the folder first and pick the next number. Keep editable SVGs and unwatermarked PNGs in `sources/` with matching names.
3. Report: how many images, what each is for, the save path, and which images are solid vs optional. Let the images do the talking — no style-theory lectures.

## Resources

- `characters/_TEMPLATE.md` — blank character profile; copy to define a new character.
- `characters/peanut.md` — deadpan in-shell peanut (single warm-orange accent, watermark).
- `characters/xiaohei.md` — 小黑, solid-black creature with white dot eyes (orange/red/blue semantic palette).
- `references/style-dna.md` — shared visual DNA: line, whitespace, palette modes, label rules, hard nos.
- `references/composition-patterns.md` — structure types, fresh-metaphor method, multi-actor labeling, anti-copy rules.
- `references/svg-workflow.md` — default backend: SVG authoring + headless Chrome rendering.
- `references/prompt-template.md` — alternative backend: fill-in-the-blanks image-gen prompt.
- `references/qa-checklist.md` — pass criteria, failure signals, iteration moves.
- `scripts/add_watermark.py` — exact-text watermark, bottom-right quiet margin.
