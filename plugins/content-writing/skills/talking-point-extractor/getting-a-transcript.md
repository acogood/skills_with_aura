# Getting a transcript (default tools only)

This skill extracts talking points from **source text that already exists** — a transcript, article,
or doc. It does **not** fetch YouTube transcripts for you, and neither do the other content-writing
skills. This file is the canonical how-to for getting a YouTube (or podcast) transcript into the
pipeline using only Claude Code's built-in tools — no API keys, no MCP servers, no extra CLIs.

> **Why this exists:** Claude Code's built-in `WebFetch`/`WebSearch` **cannot reliably pull a YouTube
> transcript** — a JS-rendered watch page comes back as just nav/footer, the caption endpoints need
> signed tokens, and the public transcript proxies block bots or are offline. So the dependable path is
> manual, and it's fast.

---

## The reliable path: paste YouTube's own transcript (do this)

YouTube ships a transcript for almost every video. Copying it takes ~15 seconds and works for every
user with no installs.

1. Open the video on `youtube.com` (desktop browser).
2. Under the video, click **••• (more)** → **Show transcript**. (On some layouts it's a
   **"Show transcript"** button in the description panel.)
3. In the transcript panel, click the **⋮** menu and **toggle timestamps off** if you want clean prose
   (optional — timestamps are useful as `[mm:ss]` source markers and the extractor can use them).
4. Select the whole panel, copy it, and either:
   - **paste it straight into the chat**, or
   - **save it** as `content-workspace/sources/transcript-<slug>.md` (the extractor scans this folder).

### Give the file a header (recommended)

So the source is traceable, start the file with:

```markdown
# Source Transcript: <Video title>
**Channel/Host:** <name> (guest: <name>)
**Video:** https://www.youtube.com/watch?v=<id>
**Published:** <YYYY-MM-DD> · **Duration:** <mm:ss>
**Captions:** YouTube transcript panel, pasted <YYYY-MM-DD>.
```

That's it. Hand the file or pasted text to `talking-point-extractor` and it runs normally.

---

## Best-effort auto-fetch (usually fails — expect to paste)

You can *try* to pull the transcript with built-in tools first, but treat it as a long shot, not the
plan. Attempt the rungs below **in order with `WebFetch`**, stop at the first that returns real caption
text, and **run the verification gate** before using anything. If all fail (the common case), fall back
to the manual path above.

1. **Invidious caption API** (a privacy front-end; public instances rotate and most are down or
   bot-blocked). First list tracks, then fetch the text:
   - `https://<instance>/api/v1/captions/<video_id>` → lists available caption tracks (JSON)
   - `https://<instance>/api/v1/captions/<video_id>?lang=en` → the caption text (WebVTT)
   - Instances to try (any may be dead on a given day): `inv.nadeko.net`, `yewtu.be`,
     `invidious.privacyredirect.com`. Find current ones at the public Invidious instance list.
2. **Piped API** (another front-end; same caveats): `https://<piped-api-instance>/streams/<video_id>` →
   read `subtitles[].url`, then `WebFetch` that subtitle URL.
3. **Reader proxy** `https://r.jina.ai/https://www.youtube.com/watch?v=<id>` — note this typically
   returns the video's **metadata/description, not the transcript**, so it rarely helps for captions.

These depend on third-party services that are rate-limited, blocked, or offline more often than not.
Do not build the workflow around them.

---

## Two hard rules

- **Verification gate.** Before using any fetched text, confirm it is *actually this video's
  transcript*: it should be contiguous spoken text (not nav/footer/UI boilerplate) and should match the
  video — check the title or a distinctive early phrase against the source. If it doesn't verify,
  discard it and use the manual path.
- **Never fabricate.** If you cannot obtain a real transcript, **do not invent or approximate one.**
  A made-up transcript produces confident, wrong talking points. Stop and give the user the manual
  steps above instead. (This mirrors the plugin's standing rule: unsourced/fabricated material is
  dropped, never shipped.)

---

## Optional power-user shortcuts (extra installs — not required, not portable)

If you personally have these set up, they fetch transcripts more reliably — but they are **not** part of
this plugin's default-tools contract, cost money or setup, and must never be assumed present for other
users:

- **firecrawl** (`firecrawl` CLI / MCP) — real headless browser; scrapes a transcript site or the watch
  page. Reliable, but a paid dependency.
- **A Perplexity / other web MCP** — can sometimes retrieve transcript text. Treat as a discovery aid and
  still apply the verification gate.
- **`yt-dlp --write-auto-sub`** — downloads caption files locally if you have it installed.

If you use one of these, save the result into `content-workspace/sources/` with the header above so the
rest of the pipeline stays identical for everyone.
