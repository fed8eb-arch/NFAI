# Technical assessment — module-02 prototype

Date of this assessment: 2026-11-23, America/Los_Angeles (PT, UTC-8).  
Order: t458u (BUY + INTEGRATE + BUILD). This file assesses the existing prototype. It does not extend the code.

The prototype is **not deprecated**. Code and the 2026-11-23 run are kept. Further feature work is paused until this assessment is accepted.

## What exists

Path: `missions/001-growth-os/track-b-growth-os/module-02-prototype/`

| File | Role |
|---|---|
| `detect.py` | String match for brand/competitor names and URL citations in model text. Does not fetch or verify URLs. |
| `measure.py` | Queries the local LiteLLM route (`http://127.0.0.1:4000/v1`, model `free-chat`). Writes JSON and CSV. Loads `LITELLM_MASTER_KEY` from the environment; does not print or write the key. |
| `test_detect.py` | Unit tests (no network, no API key). |
| `config.wireready.json` | Brand WireReady, four official-site competitors, 10 unbranded buyer questions. |
| `output/run-2026-11-23-wireready.json` and `.csv` | One live run, 2026-11-23. |

Pilot brand in the config is the public site [wireready-pilot.netlify.app](https://wireready-pilot.netlify.app) (Dallas-area data center electrical construction and apprenticeship preparation). That choice is a Track B proposal, not yet accepted by the Founder.

The script states in its own output: this measures only the local `free-chat` route, not ChatGPT, Gemini, Perplexity, or other consumer AI search engines.

## Tests

Re-run on 2026-11-23 after this assessment was opened, in the prototype directory:

```
python3 test_detect.py
Ran 13 tests in 0.022s
OK
```

Coverage: name and alias matches, possessives, word boundaries (including short token `FSG`), URL punctuation stripping, domain citation (`www.` ignored), empty answers, summary rates, config shape (10 questions), CSV flatten helper. There is no automated live-HTTP test (by design: no key in CI, no spend).

## Live run results (actual numbers)

File: `output/run-2026-11-23-wireready.json`

| Field | Value |
|---|---|
| Started (UTC) | 2026-11-24T00:35:33.545360+00:00 (2026-11-23 16:35:33 PT) |
| Finished (UTC) | 2026-11-24T00:37:59.654627+00:00 (2026-11-23 16:37:59 PT) |
| Requested model | `free-chat` |
| Returned model field | `free-chat` (the API did not name an upstream model in this run) |
| Questions | 10 |
| HTTP | all 10 returned 200; `ok=true` for all 10 |
| Brand mentions (WireReady / aliases) | **0 / 10** (rate 0.0) |
| Brand URL citations | **0 / 10** |
| Watch-list competitor mentions (GCATS, PowerBoy Electrical Services, Allied Contractors, FSG) | **0 / 10** each |
| Watch-list competitor URL citations | **0 / 10** each |
| Answers that contained at least one URL string | 6 of 10 (Q01, Q05, Q07–Q10) |
| Q03 visible answer | **empty** (`answer` length 0) |
| Q03 usage | `completion_tokens=800`, `reasoning_tokens=800`, `cost=0` |
| Latency | 6.620–18.037 s per question; sum 142.093 s |
| Reported cost | `cost: 0` on all 10 calls |

The empty Q03 answer matches a failure mode independently recorded in [`INFRA.md`](../../INFRA.md): `free-chat` can spend the entire `max_tokens` budget on `reasoning_tokens` and return no visible content. This run used `max_tokens=800`. Several other answers also hit 800 completion tokens and may be truncated.

The model named additional firms and URLs that were **not** on the watch list (for example in Q01). Those names were not independently verified in this task and are not treated as facts. Mention flags only count the configured watch list.

A shorter smoke test of the same router earlier the same day returned `model=mistral-Nemo-Instruct-2407` for a one-word prompt. The visibility run’s `returned_model` field was `free-chat`. Both observations are recorded; the upstream model is not assumed.

## Gaps versus the Shestakov measurement protocol and production module 02

Protocol in the PDF (Shestakov pp. 44, 47, 49–51; catalogued in [Track A services.md](../../track-a-rush-conf/services.md)):

1. Use **real engines**: ChatGPT, Gemini, Perplexity, and Alice — not a substitute model.
2. 20–30 (or 100) real buyer questions, then **repeat the same set after 30 days**.
3. One answer is not a measurement: Surfer figures cited on p. 49–50 say a single run is chance; the slide discusses 100 or 400 repeats to tighten a rate.
4. Share of Voice is only an intermediate metric. The text of the answer (accuracy, sentiment, errors) must be read. Presence alone can look “green” while the answer is harmful.
5. GA4 and Metrica miss this demand: visits may be recorded as direct. Ask in the form and on the call where the lead heard about the brand.
6. Technical access: pages must be readable without JavaScript; `robots.txt` must not block `OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`.

The prototype covers only a repeatable logger and a string-match layer on **one free router model**, with a single pass of 10 questions. It does not meet items 1–6.

## Versus ready services (do not become a reseller)

Ready offerings named in the PDFs or adjacent official sites, useful as **inputs** to module 02:

| Ready service | Official URL checked 2026-11-23 | Role vs this prototype |
|---|---|---|
| ChatGPT, Gemini, Perplexity, Alice | [chatgpt.com](https://chatgpt.com/), [gemini.google.com](https://gemini.google.com/), [perplexity.ai](https://www.perplexity.ai/), [alice.yandex.ru](https://alice.yandex.ru/) | These are the measurement targets. The prototype does not query them. |
| Rush Analytics (AI Results Tracker listed on the English site) | [rush-analytics.com](https://rush-analytics.com/) (HTTP 200; “first 7 days are free, no credit card” on the homepage that day) and [rush-analytics.ru](https://www.rush-analytics.ru/) | A vendor tracker could scale multi-engine collection. It is not NFAI’s product to resell. |
| Surfer, Semrush (AI visibility / research cited by Shestakov) | [surfer.ai/pricing](https://surfer.ai/pricing/), [semrush.com/pricing](https://www.semrush.com/pricing/) | Paid research and visibility suites. Exact plan amounts were not extracted from JS-heavy pricing pages in this pass. |
| Yandex Webmaster, «Видимость сайта в Алисе AI» | [webmaster.yandex.ru](https://webmaster.yandex.ru/) | Official Alice visibility metric (claimed on the slide as added April 2026). Relevant for RU properties, not a substitute for US engines. |

Recommendation (pending Founder acceptance, no signup now):

- **Keep** the prototype as a starting **integration / quality-control / cost-control** layer: structured questions, logs, mention/citation detection, CSV/JSON, tests, zero incremental model spend on `free-chat`.
- **Do not** report its 0/10 WireReady figure as AI Share of Voice in ChatGPT, Gemini, Perplexity, or Alice.
- **Integrate** the real engines and the Shestakov protocol (multi-run, sentiment/accuracy, 30-day repeat) when the Founder approves accounts. Build only the parts that give NFAI vendor independence and QC (harness, scoring, evidence store).
- **Consider buying** one tracker later for scale, as a tool NFAI operates for clients, not as a white-label resale. No payment without a separate yes.

## What this assessment does not change

No production site was edited. No new account was created. No new money was spent. The live WireReady site was only read as a public page when the config was prepared.


## 2026-11-24 — supplemental offline acceptance review

Executor/reviewer: ChatGPT in the agency conversation, isolated temporary Linux sandbox, not Buddy's box, Windows, Claude or Codex. No HTTP/model calls, keys, deployment, feature changes or product work. The exact detector source was reconstructed from GitHub text and verified with `git hash-object detect.py`: 2addd710f12595031a9319065ec688d4d87f2694. Direct raw GitHub download from this sandbox failed DNS; connector read was used. Twelve supplemental synthetic assertions executed, eight passed (possessive, partial word, alias, punctuation, www, subdomain, unrelated suffix, empty answer). Four candidate acceptance assertions failed: explicit :443 port (netloc rather than hostname), URL with userinfo accepted as a citation (reject credential-bearing URLs under proposed validation policy), mixed Cyrillic/Latin word boundaries (ASCII-only boundary), denominator includes failed rows (current all-questions metric is defined by existing code; report valid-response rate separately, not a silent replacement). These are new review cases, not a rerun of historical 13 tests or an independent agent's formal acceptance. No source changes.

Stored JSON blob f4a82619925317aa717f04ca810f7110b12ab3ac independently parsed: 10 questions, 10 ok, Q03 empty, 6 with URL strings, 0 brand/competitor mentions/citations, requested route free-chat. The valid nonempty response count is 9; HTTP success is not usable-answer success. CSV exists (blob 5bea86926ae41ca22950f091cafdfa64fda78399); multiline answers mean physical line count is not row count. Static measure.py review (3616aec7c0b6c55519898e8f5c088c4a1a33241d): config controls API base while bearer key is sent to it; constrain allowed endpoint before any future execution, reject credential-bearing URLs; raw HTTP error detail is written into reports, redact before persistence; output filename only date+brand can overwrite a run; keep unique immutable run IDs. Router billing/actual upstream not established by HTTP status. URL string match is not proof of citation validity or recommendation. Recommendations require accepted assessment and explicit scope before implementation. No commercial or production readiness claim. Keep WireReady HOLD; no new run or network requests. Independent acceptance remains pending.
