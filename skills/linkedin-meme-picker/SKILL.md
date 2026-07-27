---
name: linkedin-meme-picker
description: "Pick and render a meme for a finished LinkedIn post. Reads the post's argument, hook, and the sacred cow it pokes, maps it to a fitting meme concept, chooses the right memegen.link template, writes and encodes the caption, VERIFIES the image actually renders, and returns a meme board (a lead plus an alt per post) with optional PNG downloads. Use when the user has drafted or finalized LinkedIn posts and asks to make a meme for a post, generate memes for a batch, build a meme board, or asks what meme fits a post. Renders through the same free memegen.link API that meme-factory wraps, but adds the judgment meme-factory lacks: which meme fits THIS marketing post, in THIS voice, to earn saves and DM-shares. Not for drafting or rewriting the post (linkedin-post-writer), not the pre-publish go/no-go (linkedin-final-check), not a general or dev-humor meme generator (meme-factory), and not for non-LinkedIn surfaces."
argument-hint: <a ready-to-post file, a single post, or "the queue">
---

# LinkedIn Meme Picker

> **Works standalone.** Point it at a finished LinkedIn post — a file, the ready-to-post queue, or pasted
> text — and it returns a verified meme board. It renders via the free **memegen.link** image API (no key,
> the same API `meme-factory` wraps) and writes its board under `content-workspace/`. Nothing launches
> automatically.

## What it is (and is not)

The judgment layer between a finished post and a meme. `meme-factory` renders any concept you hand it;
this skill decides **which** meme fits a given LinkedIn post and voice, captions it, verifies it renders,
and lays out a batch so a feed of them doesn't look same-y.

- It **picks + captions + verifies + boards**.
- It does **NOT** draft or rewrite the post (`linkedin-post-writer`), gate publish-readiness
  (`linkedin-final-check`), or make generic/dev-humor memes (`meme-factory`).
- **LinkedIn only.**

## Input

Resolve to the publishable post body/bodies:
- A **ready-to-post file** (e.g. `content-workspace/content/ready-to-post-*.md`) → do the whole batch.
- A **single draft/variant or pasted post** → one board entry.

Use only the hook-to-CTA body + its named proof; ignore scaffolding (headers, `Why this template`, notes).

## Workflow

1. **Read the post.** Extract the hook, the core argument, the sacred cow it pokes, and the named proof
   (number / quote / example).
2. **Meme-worthiness gate.** Skip a meme if the post is earnest or emotional and a meme would cheapen it.
   Not every post needs one — say so rather than forcing it.
3. **Pick 1–2 concepts that REINFORCE the thesis** (not decorate). Match voice — read the style card if
   present (scan `content-workspace/profiles/` for a filename containing `style`). A spicy/contrarian
   account can run pointed memes; a buttoned-up one can't.
4. **Optimise for the share signal.** The test is: *would one person screenshot-DM this to a teammate?*
   LinkedIn rewards private shares + substantive comments (depth) over likes. Anchor the meme to a real,
   specific frustration the post names.
5. **Map to a memegen template** — confirm the **real** template id (see `memegen-reference.md`). Friendly
   names like `change-my-mind` / `two-buttons` / `gru-plan` are **not** ids (they are `cmm` / `ds` / `gru`)
   and silently 404 to a placeholder.
6. **Write the caption:** short (2–6 words per line), the post's real claim, encoded per memegen rules.
   Never invent a number or quote the post doesn't have.
7. **Vary templates across a batch** so no two consecutive posts lead with the same format.
8. **VERIFY-RENDER every URL** before presenting (the hard gate — below).
9. **Output.** Write a board to `content-workspace/content/meme-board-<slug>-<date>.md` (lead + alt per
   post, each with its verified URL and one-line caption logic). Offer to download the chosen PNGs to
   `content-workspace/memes/`.

## The verify-render gate (do not skip)

A memegen URL can look fine and still not be your meme: a **wrong template id** returns a small
"template not found" placeholder PNG, and the Heroku-hosted API intermittently returns a tiny HTML
**"Application Error"** page under rapid batches. So never present or download a URL you haven't confirmed:

- `curl -sSL` the URL following redirects; confirm the result is a **real PNG**: `file` reports
  `PNG image data` **and** size > ~200KB. A small HTML/placeholder body = fail — fix the id or encoding.
- Retry transient failures: `--retry 6 --retry-delay 2 --retry-all-errors`.
- For a batch download, drive it from a **data file** (`name url` per line) and `curl "$url"` inside a
  `while read` loop, so the shell never re-parses `$`, `''`, or `~` inside a caption.

Exact commands, the verified template-id table, and the encoding cheat-sheet live in
`memegen-reference.md` in this skill's directory — **read it before building URLs.**

## Selection principles

- **Reinforce, don't decorate** — the meme restates the post's fight in one image.
- **DM/save test over laugh test** — invisible shares are what the algorithm values most.
- **Real, specific frustration** — memes land when they name a pain the reader lives.
- **Voice-match** — defer to the style card; keep the account's register.
- **Variety** — rotate templates across a batch; call out the spread at the end of the board.

## What This Skill Never Does

- Never drafts, rewrites, or re-angles a post — that's `linkedin-post-writer`.
- Never fabricates a stat/quote in a caption — every caption traces to the post's real claim.
- Never presents or saves an **unverified** URL — it must pass the render gate.
- Never guesses a memegen template id — it confirms against the reference/endpoint.
- Never writes into a skill folder — outputs go to `content-workspace/` (board to `content/`, images to
  `memes/`).

## API Integration Summary

Rendering uses the **free memegen.link image API** (no key, URL-based) — the same API `meme-factory`
wraps; optional voice-matching reads the **local style card** (no network). This skill does **NOT** do web
research and does **NOT** fabricate. The rule: build the caption from the post's own claims, confirm every
memegen template id, and **verify each image renders** (real PNG, >~200KB, retry transient errors) before
presenting or downloading — do **NOT** hand over unverified URLs, invent template ids, or create alternative
rendering scripts.
