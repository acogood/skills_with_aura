# Skills with Aura ✨

A collection of [Claude Code](https://code.claude.com) **Agent Skills**, packaged as an
installable plugin marketplace. The first plugin — **`content-writing`** — is a seven-skill
toolkit for researching an audience and then drafting, enriching, and reviewing LinkedIn &
long-form content.

> Built and maintained by [Anton Kogut](https://github.com/acogood). PRs and new skills welcome —
> see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Install

In Claude Code:

```text
/plugin marketplace add acogood/skills_with_aura
/plugin install content-writing@skills-with-aura
```

That's it — the seven skills below become available and Claude will invoke them automatically
when a task matches, or you can call any of them by name.

To update later: `/plugin marketplace update skills-with-aura`.

---

## What's inside — `content-writing`

| Skill | What it does |
|---|---|
| **`talking-point-extractor`** | Pulls post-ready angles from any source (transcript / article / doc) into 4 buckets: Educational, Spicy Take, Data Nugget, Story Spark. *The idea-extraction one.* |
| **`post-enricher`** | Takes a talking point or draft and adds a story, case study, or authority quote — researches recent, **verifiable** proof rather than relying on training knowledge. *"add a story / find me an example / make this more compelling."* |
| **`linkedin-post-writer`** | Drafts a ready-to-post LinkedIn post in 2-3 hook/angle variants from your talking points + enrichment, matched to your audience profile and style card and written to the reviewer's rules. *The drafting step between enrichment and review.* |
| **`linkedin-post-reviewer`** | Reviews LinkedIn drafts (weekly batches, single posts, or hooks) against an embedded best-practice checklist — hook discipline, scannable F-pattern formatting, posting cadence, content-mix balance — in a blunt, opinionated voice. |
| **`writing-style-analyzer`** | Reverse-engineers a creator's voice into a reusable **Style Card** (capture an existing voice / design a new one / model after someone you admire). |
| **`lookalike-content`** | Analyzes a content dump → finds what's working → builds a **Winning Content Profile** → generates 10 lookalike ideas. |
| **`content-audience-profiler`** | Builds a research-backed **content audience profile** any other skill can draw on — *who* you're writing to. |

### How they compose

These are seven **independent** skills — there's no fixed order and nothing auto-runs. Launch any one on its own, or describe what you want and let Claude pick which to run first, next, and so on. They share a single `content-workspace/` directory (see below): each writes its output there and reads a sibling's output from there *if it's present and useful* — otherwise it asks you or proceeds without it.

Combinations people reach for (examples, not a required flow):

- Profile the audience, then capture or design a voice — and write with both in hand.
- Pull talking points from a source → enrich one with a story or stat → draft the LinkedIn post → review it before posting.
- Mine what's already working with `lookalike-content`, then take a resulting idea into `talking-point-extractor`.

---

## Requirements

- **Claude Code** with plugin support.
- **Web research — no API keys required.** `post-enricher`, `writing-style-analyzer`,
  `lookalike-content`, and `content-audience-profiler` do live research with Claude Code's built-in
  **`WebSearch`** (to find sources) and **`WebFetch`** (to read the strongest results and read
  specific pages — a site, a blog, a reviews page). Each skill verifies every cited claim on its own
  source page before using it, holds a recent-specific-citable bar, and degrades gracefully when a
  source is unavailable.
- **Source text is yours to provide.** The skills extract from text you already have (transcript,
  article, doc). Built-in tools **can't reliably fetch a YouTube transcript**, so for a video source
  paste YouTube's **Show transcript** panel or drop a captions file into `content-workspace/sources/` —
  see [getting-a-transcript.md](plugins/content-writing/skills/talking-point-extractor/getting-a-transcript.md).
  firecrawl / `yt-dlp` / a web MCP are optional shortcuts, never required.

---

## Where things are saved (`content-workspace/`)

When a skill reads inputs or saves outputs, it uses a **`content-workspace/`** directory in
your current project:

```
content-workspace/
├── profiles/        ← audience profiles + writing style cards (shared across skills)
├── samples/         ← drop writing samples here for writing-style-analyzer
├── sources/         ← drop transcripts/articles here for talking-point-extractor
├── talking-points/  ← extracted talking points
├── content/         ← enrichments, drafts, content ideas, winning-content DNA
└── data/            ← cleaned content dumps for lookalike-content
```

**Worked examples** ship inside the plugin at
`plugins/content-writing/assets/examples/profiles/` — real audience profiles and creator
style cards (Julian Shapiro, Katelyn Bourgoin, Amanda Natividad, and more) you can copy into
`content-workspace/profiles/` as a starting point.

---

## Repo layout

```
skills_with_aura/                       ← marketplace root
├── .claude-plugin/marketplace.json     ← the catalog Claude Code reads
├── plugins/
│   └── content-writing/
│       ├── .claude-plugin/plugin.json
│       ├── skills/                      ← the seven skills (one folder each, SKILL.md inside)
│       └── assets/                      ← worked examples (audience profiles + style cards)
├── README.md  CONTRIBUTING.md  LICENSE  NOTICE.md
```

Grounded in the official [plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
and [plugins reference](https://code.claude.com/docs/en/plugins-reference) docs.

---

## License

Code and skills in this repo are released under the [MIT License](LICENSE). **Bundled
third-party reference material is *not* MIT-licensed** — see [NOTICE.md](NOTICE.md).
