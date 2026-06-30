# HTML Style Guide — Writing Style Card

This document describes how to generate the client-facing HTML version of the Writing Style Card. Same design philosophy as the audience profile HTML — clean, modern, scannable.

## Requirements

- **Single file** — all CSS inline in a `<style>` block
- **One Google Font** — load via CDN. Choose a distinctive but readable pairing. Do NOT use Inter, Roboto, or Arial. Good options: `DM Sans`, `Plus Jakarta Sans`, `Outfit`, `Sora`.
- **No JavaScript required** — static document
- **Print-friendly** — include `@media print` rules

## Design Direction

Same design sensibility as the audience profile HTML — Linear/Notion-inspired. But with one key difference: the Style Card is shorter and more reference-oriented. It should feel like a designer's spec sheet — dense, scannable, quick to reference.

**Key design elements:**

- The **Vibe** line should be visually prominent — it's the one-liner people will reference most
- The **TL;DR** bullets should stand out as the quick-reference section
- The **Do/Don't table** should be the visual centrepiece — well-formatted with clear contrast between the two columns
- The **Vocab & Phrases** lean-into/avoid lists should use subtle colour coding (green tint for lean-into, red/amber tint for avoid)
- **Hook Patterns** and **Close Patterns** should be formatted as labelled cards or list items where the pattern name is bold and visually distinct from the description

## Colour Palette

Use the same accent colour as the audience profile HTML if one exists. If generating independently, use a complementary but distinct accent — if the audience profile used blue, the style card could use a warm slate or muted green. This creates visual distinction between the two documents while keeping them in the same family.

Default palette:
- Background: `#FFFFFF` or `#FAFAFA`
- Text: `#1A1A2E`
- Section headers: `#0F172A`
- Accent: `#7C3AED` (purple-600) or `#059669` (emerald-600) — something distinct from the audience profile's blue
- Muted text: `#64748B`
- Table borders: `#E2E8F0`
- Do column: subtle green tint `#F0FDF4`
- Don't column: subtle red tint `#FEF2F2`
- Lean-into bg: `#F0FDF4` (green-50)
- Avoid bg: `#FEF2F2` (red-50)

## Layout Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Style Card: [Style Name] — [Client Name]</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* All CSS here */
  </style>
</head>
<body>
  <div class="container">
    <header>
      <!-- Style name, vibe line, metadata (client, date, mode, platform, sample count) -->
    </header>
    <main>
      <!-- TL;DR -->
      <!-- Key Principles -->
      <!-- Voice & Tone -->
      <!-- Structure & Formatting -->
      <!-- Hook Patterns -->
      <!-- Close Patterns -->
      <!-- Devices & Patterns -->
      <!-- Syntax & Mechanics -->
      <!-- Vocab & Phrases -->
      <!-- Do / Don't -->
      <!-- Adaptation Notes (Mode 3 only) -->
    </main>
    <footer>
      <!-- Style Card footer note -->
    </footer>
  </div>
</body>
</html>
```

## Specific Styling Notes

**Container:**
- Max-width: `720px` (slightly narrower than the audience profile — this is a reference doc, not a report)
- Centered with generous padding

**Vibe line:**
- Large italic text, slightly muted colour
- Visually distinct from everything else — it's the headline

**TL;DR section:**
- Highlighted background (light grey or accent at 5% opacity)
- Slight border-radius, padding
- Feels like a callout box

**Key Principles:**
- Numbered list with bold numbers
- Each principle as its own visually distinct block

**Hook and Close Patterns:**
- Pattern name as a bold label
- Description as regular text
- Visual separation between each pattern (spacing or subtle divider)

**Syntax & Mechanics:**
- Formatted as a definition list or compact table
- Labels bold, values in regular weight

**Do/Don't table:**
- Two-column table
- Do column: white or green-tinted background
- Don't column: red/amber-tinted background
- Clear header row
- Good cell padding

**Vocab lean-into/avoid:**
- Two side-by-side lists or a two-column layout
- Green tint for lean-into, red tint for avoid
- Each word/phrase as a tag or pill shape (optional — plain list also works)

**Adaptation Notes (Mode 3 only):**
- Visually distinct section — different background or border
- Clearly labelled as adaptation context, not part of the core style rules

## Print Styles

```css
@media print {
  body { font-size: 11pt; }
  .container { max-width: 100%; padding: 0; }
  /* Remove background colours that waste ink */
  /* Ensure tables don't break across pages */
  table { page-break-inside: avoid; }
  /* Keep the Do/Don't table together */
}
```

## Filename

Save as: `writing-style-card.html` in `./profiles/`.
