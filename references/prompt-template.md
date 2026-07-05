# Image-Gen Backend — Prompt Template

Use only when an image generation tool is actually available in the environment. Generate each image on its own; never combine several ideas into one image.

Fill `{…}` from the composition spec and the active character profile (its **Image-gen prompt block** and palette frontmatter).

```text
Generate one standalone 16:9 horizontal concept illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. {palette clause — single-accent: "A single {accent color} accent used sparingly for one point of emphasis (no other colors)." | semantic-triad: "Sparse {orange/red/blue} handwritten annotations."} Clean, deadpan, slightly absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring character required:
{the character profile's "Image-gen prompt block" paragraph}

Theme:
{the idea to illustrate}

Structure type:
{Workflow / System slice / Before-after / Character state / Concept metaphor / Layered method / Map route / Mini comic}

Core idea:
{the single thing this image must express}

Composition:
{the concrete scene: where the character is, what it is doing, the main object, how things flow}

Suggested elements:
{element 1} / {element 2} / {element 3}

Handwritten labels ({language}):
{label 1} / {label 2} / {label 3} / {optional 4} / {optional 5}

Color use:
{single-accent: "Black for all line art and the character. One {accent} as the single accent, used only for the most important thing. No other colors." | semantic-triad: "Black for main line art and the character. Orange for main flow/paths/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state."}

{watermark clause, only if the profile has one: "Watermark handling: Leave a clean quiet margin in the bottom-right corner for an exact watermark added locally after generation. Do not draw the watermark text."}

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use short handwritten labels only; label every actor with who they are. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Invent a fresh visual metaphor for this specific content. Clear but not instructional, interesting but not childish, strange but clean.
```

## Edit prompts

Remove a top-left title:

```text
Edit the provided image. Remove only the handwritten title "{text}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: the character, labels, paths, line style, accents, composition, aspect ratio, and quality. Do not add any new text or objects.
```

Make the character central:

```text
Regenerate this illustration with the same core meaning and simple layout, but make {character} more central to the conceptual action. {character} should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```

Swap the accent color (single-accent profiles):

```text
Regenerate this illustration unchanged except for the accent color: replace {old accent} with {new color}, used in exactly the same restrained way. Keep everything else identical.
```
