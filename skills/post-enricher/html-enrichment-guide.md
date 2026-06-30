# HTML Template Guide — Post Enrichment Options

This document describes how to generate the HTML version of the enrichment options output.

## Requirements

- **Single file** — all CSS inline in a `<style>` block
- **One Google Font** — load via CDN. Use `DM Sans`, `Plus Jakarta Sans`, `Outfit`, or `Sora`. Do NOT use Inter, Roboto, or Arial.
- **No JavaScript required** — static document
- **Print-friendly** — include `@media print` rules

## Design Direction

This is a selection tool — the user needs to compare 3 enrichment options and pick one. Each option should feel like a complete, self-contained card. The design should make it easy to compare the three side by side (or stacked on mobile).

## Colour-Coded Enrichment Types

Each enrichment type gets a distinct accent colour:

- **Story Integration** — `#D97706` (amber-600) — warmth, narrative
- **Example / Case Study** — `#2563EB` (blue-600) — evidence, data
- **Authority Quote** — `#7C3AED` (purple-600) — credibility, weight

Default palette:
- Background: `#FAFAFA`
- Card background: `#FFFFFF`
- Card border: enrichment type accent at 30% opacity
- Card shadow: subtle `rgba(0,0,0,0.05)`
- Text: `#1A1A2E`
- Muted text: `#64748B`
- Source text: `#64748B`, italic

## Layout

**Header:**
- Core argument as the main title
- Audience and style card info as muted text
- A brief explanation: "Three options to strengthen your post. Pick one or combine."

**Enrichment Cards:**
Each enrichment as a large card with:
- **Type label** as a coloured badge (Story / Case Study / Quote)
- **Title line** — bold, prominent (the story label, example company name, or quote attribution)
- **Body content** — the story text, case study, or quote itself
  - Stories: regular prose
  - Case studies: prose with the source on its own line, muted
  - Quotes: blockquote styling with large quotation marks
- **Connection line** — the "why this works" sentence, slightly muted, at the bottom of the card
- **Source attribution** — for case studies and quotes, clearly formatted

**Card styling:**
- Generous padding
- Left border in the enrichment type's accent colour (4px solid)
- Subtle shadow for depth
- Clear separation between cards (margin or divider)

**Story card specifics:**
- The story text in regular prose
- The connection/lesson as a separate paragraph, slightly muted

**Case study card specifics:**
- Company/person name prominent
- Numbers/outcomes bold or highlighted
- Source as a separate muted line

**Quote card specifics:**
- Large opening quotation mark as a decorative element
- Quote text slightly larger than body
- Attribution below: name, credential, source — all on one line, muted

## Container

- Max-width: `780px`
- Centered with generous padding

## Print Styles

```css
@media print {
  body { font-size: 11pt; }
  .card { break-inside: avoid; box-shadow: none; border-left: 3px solid #999; }
}
```

## Filename

Save alongside the markdown version in `./content/`:
`enrichment-YYYY-MM-DD-[talking-point-name].html`
