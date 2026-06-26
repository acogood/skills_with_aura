# HTML Template Guide

This document describes how to generate the client-facing HTML version of the content audience profile. The HTML file should contain the same content as the markdown profile, styled as a clean, modern, single-page document.

## Requirements

- **Single file** — all CSS inline in a `<style>` block. No external stylesheets except a Google Font.
- **One Google Font** — load via CDN link in `<head>`. Choose a distinctive but readable font pairing. For example:
  - Headings: `DM Sans`, `Plus Jakarta Sans`, `Outfit`, or `Sora`
  - Body: same as headings (single font family, weight variation) or a complementary serif for body text
  - Do NOT use Inter, Roboto, or Arial
- **No JavaScript required** — this is a static document
- **Print-friendly** — include `@media print` rules

## Design Direction

The design should feel like a modern internal strategy document — think Linear, Notion, or Stripe's documentation. Professional but not corporate. Clean but not sterile.

**Key design principles:**
- Generous whitespace — let the content breathe
- Clear visual hierarchy — the 10 sections should be easy to scan
- Tables should be well-formatted and readable (the vocabulary library table is the centrepiece)
- Validation hooks should stand out visually — they're used frequently by downstream skills
- Subtle section dividers — not heavy horizontal rules
- The profile metadata (client name, audience, platform, date) should be prominent at the top

## Colour Palette

If a brand colour was extracted from the client's website during scraping, use it as the accent colour (section headers, table header background, links). Keep the rest neutral.

If no brand colour was extracted, use a default professional palette:
- Background: `#FFFFFF` or `#FAFAFA`
- Text: `#1A1A2E` (near-black, not pure black)
- Section headers: `#0F172A` (slate-900)
- Accent: `#2563EB` (blue-600) for highlights, table headers, and the priority indicators
- Muted text: `#64748B` (slate-500) for metadata and secondary info
- Table borders: `#E2E8F0` (slate-200)
- Table header bg: accent colour at 10% opacity
- Validation hook bg: `#F8FAFC` (slate-50) with a left border accent

## Layout Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Content Audience Profile: [Audience Label] — [Client Name]</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]+[Family]:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* All CSS here — see styling rules below */
  </style>
</head>
<body>
  <div class="container">
    <header>
      <!-- Profile metadata: client name, audience label, platform, date -->
    </header>
    <main>
      <!-- 10 sections -->
    </main>
    <footer>
      <!-- Profile footer note -->
    </footer>
  </div>
</body>
</html>
```

## Styling Rules

**Container:**
- Max-width: `780px` (comfortable reading width)
- Centered: `margin: 0 auto`
- Padding: `3rem 2rem`

**Header:**
- Client name: large, bold
- Audience label: `h1`, the main title
- Metadata (platform, tier, date): smaller, muted colour, displayed as a row of pills/tags or a simple line

**Section headers (h2):**
- Section number included: "1. Audience Identity"
- Bottom border or underline in accent colour
- Generous margin-top for section separation (`3rem`)

**Body text:**
- Line height: `1.7` for readability
- Font size: `16px` base
- Paragraph spacing: `1rem`

**Tables (vocabulary library, measurement log):**
- Full width
- Subtle borders (`1px solid` in slate-200)
- Header row: accent colour background (low opacity), bold text
- Cell padding: `0.75rem 1rem`
- Alternating row backgrounds (optional, subtle)

**Validation hooks:**
- Displayed as a visually distinct block — either:
  - Blockquote style with left accent border + light background
  - Or as individual cards with subtle shadow
- Each hook should be clearly separate and scannable

**Pain point priority indicators:**
- 🔴 P1, 🟠 P2, 🟡 P3 — use the emoji or coloured dots/badges
- The priority label should be visually prominent

**Anti-triggers:**
- Consider displaying these in a visually distinct "warning" style — light red/amber background or similar — to reinforce that these are things to avoid

**Situational framings:**
- Displayed in italics or in a blockquote style — they're narrative scenarios meant to be read as vivid descriptions

**Print styles (`@media print`):**
- Remove any background colours that waste ink
- Ensure tables don't break across pages
- Keep font sizes readable
- Hide any interactive elements (there shouldn't be any, but just in case)

## Content Mapping

Every section from the markdown profile maps directly to the HTML. Don't restructure or reorder — the 10-section format is intentional and should be preserved. The HTML is a presentation layer over the same content, not a redesign.

## Filename

Save as: `content-audience-profile.html` in the same `./profiles/` directory as the markdown version.
