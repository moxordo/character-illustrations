# QA Checklist

Run after rendering every image. Look at the actual output (Read the PNG).

## Must pass

- 16:9 horizontal; background is clean pure white.
- The character is present and **performs the core action** — remove-the-character test: the metaphor must collapse without it.
- The metaphor is newly invented for this content, not a re-serve of an old composition.
- The image is strange, inventive, interesting — and still clean.
- Main subject ≤ ~60% of the canvas; at least one quiet zone.
- One image = one core structure.
- Labels are few, short, readable; every actor in a multi-actor scene is named.
- Colors match the character profile's palette mode and hexes; accents do only their assigned jobs.
- No title in the top-left corner; the structure type name appears nowhere on the image.

## SVG-backend extras

- No text overlapping strokes or other text; nothing clipped at the canvas edge.
- Labels read at final render size (min ~20px font at 1600×900 before the 2x scale).
- Wobble filter applied to line art but not to text.
- Label text matches the composition spec exactly (the SVG backend never has typos — if text is wrong, the spec was wrong).

## Failure signals → fix

- Character is a bystander / mascot → rewrite so the character does the work.
- Too ordinary → put the character at the center of one strange-but-valid metaphor.
- Too complex → delete nodes; keep one action and 3–5 short labels (actor labels exempt).
- Too cute → deadpan, blank serious expression, not cute, not mascot.
- Too PPT → remove titles, borders, neat grids, extra arrows; redraw as a hand-drawn scene.
- Too close to an old case → keep the meaning, swap the main object and the character's action.
- Text wrong / garbled (image-gen backend) → prefer a local edit; if widespread, reduce label count and regenerate. (On the SVG backend, just fix the SVG.)
- Background not clean white / off-palette color crept in → fix fills, re-render.

## Delivery bar

A good image makes the reader think "that's a bit odd", then read the structure in one second. If the first glance says tutorial page, course slide, or flowchart — not a strange product sketch on blank paper — it does not ship.
