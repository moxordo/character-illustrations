---
name: monkey
display_name: the monkey
palette: single-accent
accents:
  accent: "#e8730e"         # warm orange — harmonizes with the brown fur
label_language: match-input # origin stickers are Korean
watermark: none
---

# The Monkey

## Character definition

A small warm-brown monkey adapted from a Korean sticker set. The sticker original is cute and expressive (blush, teary eyes, dramatic poses); this stylized version keeps the silhouette and two-tone coloring but swaps the personality to the house register: a deadpan worker, gravely and calmly doing a slightly ridiculous job inside the system being drawn. Not a mascot, not a sticker, not cute decoration.

## Form

- Round head, slightly wide; warm brown fur.
- Cream lower-face patch (muzzle up over the eye line) — the eyes sit ON the cream patch.
- Two small round ears at the sides, brown with cream inner.
- Small dark dot eyes; tiny flat mouth. **No blush, no sparkle, no tears, no eyebrows** — those belong to the sticker original, not this stylization.
- Compact rounded body, smaller than the head; optional cream belly patch.
- Thin stick limbs (house convention), very dark brown.
- Thin tail ending in a single curl — the monkey signature; keep it visible in most poses.
- Outline slightly irregular and hand-drawn, never a perfect vector shape.

## Colors (character identity — exempt from the annotation palette)

- Fur: `#b7885c` (flat, no gradient)
- Face/belly/inner-ear: `#f4e8d5`
- Outline and limbs: `#2f2419` (near-black warm dark)
- These fills are the character, the way xiaohei's solid black is; annotations still obey the profile accent rules.

## Personality

- Completely unbothered; the sticker drama is gone.
- Very serious about a job that is mildly absurd.
- Like a low-key system operator who clocked in and is just doing the work.
- Dry humor; never sells cuteness.
- A little clumsy, but not dumb.

## Action library

- Hauling something oversized (box, log, giant pencil).
- Pulling lines together to gather sources; climbing or hanging by the tail to reach a high shelf or cable.
- Stuck inside a break in a belt or pipe.
- Operating a "judgment" lever inside a machine.
- Sorting items into drawers; weighing things on a scale.
- Hanging a warning sign; recording on a clipboard.
- Reaching out of a hole but unable to catch what comes.
- The tail may assist the job (hooking, hanging, holding a tool) — good source of quiet absurdity.

## Don'ts

- No blush marks, teary eyes, sparkles, or emoji-pack expressions (un-sticker it).
- Not an over-cute mascot, not a children's-cartoon character.
- No elaborate clothing or props unrelated to the job.
- Never just standing in a corner watching.
- Never upstaging the structure it explains.

## SVG recipe

- Head: circle, fill `#b7885c`, stroke `#2f2419` at 3px; at primary scale r ≈ 95–115 on a 1600×900 canvas.
- Face patch: wide cream (`#f4e8d5`) rounded shape covering the lower ~60% of the head, no stroke (or 1px self-colored).
- Ears: two circles r ≈ 0.25×head-r at the head's horizontal midline, brown with a smaller cream inner circle.
- Eyes: two dark dots (r ≈ 5–7 at primary scale) on the cream patch, wide-set; mouth = one short 10–14px line. Nothing else on the face.
- Body: rounded capsule below the head, ~0.8×head width, fill `#b7885c`, same stroke; optional cream belly ellipse.
- Limbs: `#2f2419` stick lines at 5–6px, round caps; small oval hands/feet optional.
- Tail: 3px `#2f2419` line from the lower back, ending in one loop (a `C`-curve into a small spiral).
- Scale: primary ≈ 15–25% of canvas height; smaller when repeated.
- The wobble filter supplies irregularity — build clean shapes and let the filter roughen them.

## Image-gen prompt block

A small deadpan monkey with a round head, warm flat brown fur, a cream lower-face patch, small round ears, tiny dark dot eyes, a tiny flat mouth, a compact rounded body, thin dark stick limbs, and a thin tail ending in a single curl. Hand-drawn, slightly uneven outline, flat muted colors, blank serious expression — no blush, no sparkly eyes, never cute. The monkey must perform the core conceptual action, not decorate the scene.

## The test

If removing the monkey leaves the image's core metaphor fully standing, the monkey is too decorative. Rewrite so the monkey performs the action.
