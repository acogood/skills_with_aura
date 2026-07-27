# memegen.link reference (for linkedin-meme-picker)

Everything needed to build and verify a meme URL. Read this before constructing any URL.

## URL shape

```
https://api.memegen.link/images/{template_id}/{top}/{bottom}.png?width=1200
```

- **Multi-panel** templates take extra path segments, e.g. Gru's Plan: `/gru/{p1}/{p2}/{p3}.png`
  (the 4th panel auto-repeats the 3rd — the "stare").
- **One-sided:** put `_` (single underscore) on the blank side.
- `width=1200` keeps it crisp on LinkedIn. `watermark=none` is stripped for anonymous users, so omitting
  it is fine.

## Template ids are SHORT codes — confirm them

Friendly names are **not** ids and 404 to a placeholder PNG (`change-my-mind`, `two-buttons`, `gru-plan`
all fail). Verified ids:

| id | meme | best for |
|----|------|----------|
| `drake` | Drakeposting | reject X / approve Y contrast |
| `cmm` | Change My Mind | stating the post's thesis (comment magnet) |
| `ds` | Daily Struggle (two buttons) | a sweaty either/or choice |
| `gru` | Gru's Plan | a plan that backfires in the last panel |
| `db` | Distracted Boyfriend | tempted by the shiny wrong thing |
| `disastergirl` | Disaster Girl | smug in front of the fire you caused |
| `fine` | This is Fine | denial while it burns |
| `fry` | Futurama Fry | not sure if X or Y |
| `success` | Success Kid | a small, earned win |
| `mordor` | Boromir | one does not simply X |
| `buzz` | Buzz Lightyear | X, X everywhere |

Don't trust memory for an id. Confirm against the live list:

```bash
curl -s https://api.memegen.link/templates/ \
 | python3 -c "import sys,json;[print(t['id'],'|',t['name']) for t in json.load(sys.stdin) if 'change' in t['name'].lower()]"
```

(swap the search term) — or just build the URL and run the render check below.

## Text encoding

| character | encode as |
|-----------|-----------|
| space | `_` |
| literal hyphen `-` | `--` |
| literal underscore `_` | `__` |
| apostrophe / single quote `'` | `''` |
| double quote `"` | `""` |
| `?` | `~q` |
| `%` | `~p` |
| `#` | `~h` |
| `/` | `~s` |
| newline | `~n` (or `%0A`) |

Commas and `$` render literally. Keep each line 2–6 words for readability.

## Verify-render gate (mandatory before presenting or downloading)

```bash
curl -sSL -f --retry 6 --retry-delay 2 --retry-all-errors -o out.png "$URL"
file out.png        # must report: PNG image data
# AND size must be > ~200KB. A ~90KB image = wrong template id (placeholder);
# a few-hundred-byte HTML body = transient "Application Error" → retry.
```

**Batch downloads** — avoid shell re-parsing of `$`, `''`, `~` in captions by driving from a data file:

```bash
# data file: one "filename url" pair per line
while read -r name url; do
  [ -z "$name" ] && continue
  curl -sSL -f --retry 6 --retry-delay 2 --retry-all-errors -o "$MEMES/$name" "$url"
  file "$MEMES/$name" | grep -q "PNG image" && echo "OK $name" || echo "FAIL $name"
done < urls.tsv
```

## LinkedIn usage

Single-image post: `width=1200` is fine; memes read well square-ish. Attach the PNG as the post's image;
the written post stays as the caption. The bar for shipping a meme is the DM/save test, not the laugh.
