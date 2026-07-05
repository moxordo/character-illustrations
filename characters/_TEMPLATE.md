---
name: <slug>                # file name without .md; used in "as <name>" matching
display_name: <what to call it in prose and reports>
palette: single-accent      # single-accent | semantic-triad (see references/style-dna.md)
accents:
  accent: "#e8730e"         # single-accent: the one emphasis color
  # semantic-triad instead uses three keys:
  # orange: "#e8842c"       # main flow, paths, arrows
  # red: "#c9382e"          # warnings, problems, key results
  # blue: "#3a6fc4"         # secondary notes, system/brain state, AI-meta
label_language: match-input # match-input | a fixed language ("English", "Chinese", …)
watermark: none             # none | exact text for scripts/add_watermark.py
---

# <Display Name>

## Character definition

One paragraph: what this character is, and the standing rule that it is not a mascot,
not a sticker, not cute decoration — a deadpan worker gravely doing a slightly
ridiculous job inside the system being drawn.

## Form

- Silhouette and body construction (shapes, proportions).
- Eyes / face (keep expression blank, calm, deadpan, serious).
- Limbs (thin stick limbs work well; arms only when the action needs hands).
- Texture, if any (keep it a few strokes, never dense).
- Outline always slightly irregular and hand-drawn, never a perfect vector shape.

## Personality

- 3–6 bullets. Baseline: unbothered, very serious about a mildly absurd job,
  dry humor, a little clumsy but not dumb, like a low-key system operator.

## Action library

Actions this character typically performs (the core action of each image):
hauling, pulling lines together, stuck in a breakpoint, operating a lever,
becoming a funnel, cracking/splitting, stamping, leading a path, holding a
warning sign, reaching but not catching, carrying/building/sorting/recording.
Adapt and extend to fit the character's body.

## Don'ts

- Not over-cute, not a children's-cartoon character.
- No elaborate clothing, emoji faces, or sparkly eyes.
- Never just standing in a corner watching.
- Never upstaging the structure it explains.

## SVG recipe

How to draw this character with SVG primitives (used by references/svg-workflow.md):

- Body: <paths/shapes, fills, strokes>.
- Face: <eye shapes, sizes, placement>.
- Limbs: <stroke widths, poses>.
- Scale: primary character ≈ 15–25% of canvas height; smaller when repeated.
- The wobble filter supplies hand-drawn irregularity — build clean shapes.

## Image-gen prompt block

One paragraph, ready to paste into references/prompt-template.md, describing the
character's form + deadpan demeanor + "must perform the core conceptual action,
not decorate the scene" + "never cute".

## The test

If removing the character leaves the image's core metaphor fully standing, the
character is too decorative. Rewrite so the character performs the action.
