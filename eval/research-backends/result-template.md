# Research-backend comparison — <TOPIC>

> Fill-in sheet for one run of `harness.md`. Copy into the run folder as `result.md` and complete it.
> Arm A = Perplexity MCP · Arm B = built-in `WebSearch`/`WebFetch` fallback (MCP ignored).

- **Run:** `content-workspace/eval-runs/research-backends/<RUN>/`
- **Date:** <YYYY-MM-DD>
- **Topic / angle:** <one line>
- **Audience profile:** `<…/profiles/…profile….md>`
- **Style card:** `<…/profiles/…style….md>`
- **Research path:** direct research-then-draft · or skill: `<post-enricher | lookalike-content>`

---

## Raw research (links to saved files)

- Arm A: `arm-a-research.md`
- Arm B: `arm-b-research.md`

Quick characterization of what each backend returned (1-2 lines each):

- **Arm A (MCP):** <synthesized + cited? how many sources? freshest date?>
- **Arm B (WebSearch):** <which pages fetched? any blocked/paywalled? freshest date?>

---

## Scores (1-5, higher is better)

| # | Dimension | Arm A (MCP) | Arm B (WebSearch) | Winner | Notes |
|---|---|:---:|:---:|:---:|---|
| 1 | Recency | _ | _ | _ | |
| 2 | Specificity (named examples / real numbers) | _ | _ | _ | |
| 3 | Source verifiability (citable URLs, dates) | _ | _ | _ | |
| 4 | Post quality / voice-fit | _ | _ | _ | |
| 5 | Practical (latency, graceful degradation) | _ | _ | _ | |
| | **Total / 25** | **_** | **_** | **_** | |

**Verifiability spot-check:** <which 1-2 URLs did you open per arm; did they support the claim?>

**Practical notes:** <rough latency per arm; any failures, paywalls, blocked pages (e.g. LinkedIn); how it degraded>

---

## Drafted posts

### Arm A — Perplexity MCP (`arm-a-post.md`)

```
<paste the Arm A LinkedIn post>
```

### Arm B — WebSearch fallback (`arm-b-post.md`)

```
<paste the Arm B LinkedIn post>
```

---

## Verdict

**Winner:** <Arm A | Arm B | tie> (<total> vs <total>)

<2-3 sentences: which backend produced the better-supported, better-voiced post for this topic, and the main trade-off.>

**Recommendation:** <When is the WebSearch fallback good enough? Where does it visibly lose? Any fix to feed back into the skills' fallback mini-procedure.>
