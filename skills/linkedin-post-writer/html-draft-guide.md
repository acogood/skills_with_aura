# HTML Template Guide — LinkedIn Post Drafts

This document describes how to generate the HTML version of the drafts output.

## Requirements

- **Single file** — all CSS inline in a `<style>` block
- **One Google Font** — load via CDN. Use `DM Sans`, `Plus Jakarta Sans`, `Outfit`, or `Sora`. Do NOT use Inter, Roboto, or Arial.
- **No JavaScript required** — static document
- **Print-friendly** — include `@media print` rules

## Design Direction

This is a **selection tool** — the user needs to compare 2-3 post variants and pick one to ship. Each
variant should render as a complete, self-contained card that reads the way the post will look on
LinkedIn: short stacked lines, generous line spacing, the hook visually prominent. Make side-by-side
(or stacked, on mobile) comparison easy.

## Variant Accent Colours

Give each variant a distinct accent so they're easy to tell apart at a glance:

- **Variant 1** — `#2563EB` (blue-600)
- **Variant 2** — `#D97706` (amber-600)
- **Variant 3** — `#7C3AED` (purple-600)

Default palette:
- Background: `#FAFAFA`
- Card background: `#FFFFFF`
- Card border / left rule: the variant accent (4px solid left border)
- Card shadow: subtle `rgba(0,0,0,0.05)`
- Text: `#1A1A2E`
- Muted text (metadata, "why this angle", source): `#64748B`

## Layout

**Header:**
- Topic as the main title
- Core argument as a prominent subtitle
- Audience / style / proof-source as muted metadata lines
- A brief instruction: "Two to three angles on the same post. Pick one, or tell the writer to tighten one."

**Variant cards:**
Each variant as a large card with:
- **Angle label** as a coloured badge (e.g. "Data-led", "Story-led", "Contrarian")
- **The post body** rendered as it would appear on LinkedIn:
  - The hook line larger and bold (it's the thing that earns the click)
  - Short stacked lines with real line breaks — preserve the F-pattern; do not collapse into one prose blob
  - At most one emoji; no hashtags; no inline links
- **"Why this angle"** line — muted, at the bottom of the card
- **First-comment link** — if present, shown muted as "First comment: [url]"

**Card styling:**
- Generous padding and line-height (LinkedIn posts breathe)
- Left border in the variant's accent colour (4px solid)
- Subtle shadow for depth
- Clear separation between cards (margin or divider)

## Container

- Max-width: `720px` (close to a LinkedIn post column, so wrapping previews realistically)
- Centered with generous padding

## Print Styles

```css
@media print {
  body { font-size: 11pt; }
  .card { break-inside: avoid; box-shadow: none; border-left: 3px solid #999; }
}
```

## Filename

Save alongside the markdown version in `content-workspace/content/drafts/`:
`draft-YYYY-MM-DD-[slug].html`
