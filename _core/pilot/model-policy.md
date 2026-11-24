# Model-per-Task Policy (Политика выбора модели под задачу)
Version: v0.1.1 | Date: 2026-11-17 | Status: draft (not live; no agent prompt edited)
Change log: v0.1.1 (2026-11-17, Director standing rule): added §4a effort-first, §5a ChatGPT Plus rules (token economy, Astra). v0.1 initial draft.
Owner: Prompt Engineer | Task: P1, Director brief #1, phase A | Approver: Orchestrator (pilot clearance: Director, then Orchestrator)
Inputs pending: catalog shortlist `/workspace/pilot/catalog.md` (~2026-11-18 10:00 ET). Until then all model/provider names are PLACEHOLDERS, marked «не проверено».

## 1. Purpose
One rule set every agent prompt can include, so agents pick a model class per task, use free capacity first through the agency router, and degrade safely when quota runs out.

## 2. Routing rule (all agents)
1. Call models only through the agency router (OpenAI-compatible endpoint, name: `AGENCY_ROUTER`; URL set by Integration Developer). Never call a provider directly, never paste a key.
2. Free-first: request the task's model CLASS (alias below); the router picks a free-tier provider first, paid only if the Founder has approved paid use.
3. Smallest class that passes the task's acceptance criterion. Escalate to a larger class only after one failed attempt, and log why.
4. Client personal data and secrets never go to a free/third-party model unless that provider is cleared for it by Internal Security (pilot: Director). Default: strip or mask PII before sending.

## 3. Task type → model class (aliases)
| Task type | Router alias | Preferred class | Placeholder candidates («не проверено») | Fallback alias |
|---|---|---|---|---|
| Code (write, review, debug) | `code` | strong coding model, long context | [CODE_MODEL_1], [CODE_MODEL_2] | `general-large` |
| Research / analysis with sources | `research` | strong reasoning model; web search done by agent tools, not by the model | [REASON_MODEL_1] | `general-large` |
| Writing RU (client-facing) | `write-ru` | model with verified good Russian | [RU_MODEL_1] | `general-large` |
| Writing EN / internal notes | `write-en` | fast mid-size model | [FAST_MODEL_1] | `general-small` |
| Long documents (>50k tokens) | `long` | large context window (size to verify per provider) | [LONGCTX_MODEL_1] | chunk + `general-large` |
| Vision (screenshots, PDFs as images, charts) | `vision` | multimodal model | [VISION_MODEL_1] | none: escalate |
| Classification, extraction, short transforms | `general-small` | small fast model | [SMALL_MODEL_1] | `general-large` |
| Anything else | `general-large` | best available general model | [LARGE_MODEL_1] | escalate |

Shortlist alignment (after catalog.md): replace each placeholder with a provider+model only if the catalog row has source, date, reliability ≥ med, and the Integration Developer's test call passed. Otherwise keep «не проверено».

## 4. Quota exhausted / provider failure
1. Router auto-switches to the next free provider for the same alias (Integration Developer owns this logic).
2. If every free provider for the alias is exhausted: use the fallback alias in the table, once.
3. If the fallback is also exhausted or the task is client-critical: stop, do NOT switch to paid on your own; report to the Orchestrator one line: task, alias, error, time (ET).
4. Never create extra accounts, rotate identities, or use VPN to get around a provider's limits.
5. Record in the task report which alias/provider produced the result.

## 4a. Effort first, then model (Director standing rule, 2026-11-17)
1. Everywhere (ChatGPT, API via router, Arena and other web services): first tune reasoning level / effort (low → medium → high); change the model only after the right effort has been tried. Correct effort often gives more than a model switch.
2. Every task report states the model and the effort used.

## 5a. ChatGPT Plus of the Founder (manual web tool; Director standing rule, 2026-11-17)
1. Access, sign-in and any action in the account go only through the Director. Agents send ChatGPT task requests to the Director by agent message; create nothing there (projects etc.) without a Director brief.
2. Token economy: short precise prompts, no repeated context, one chat per task, lightest mode first.
3. Astra: only for extremely complex tasks, and only with the Director's agreement.
4. Web/app only, no API, not in the router.

## 5. Secrets
- API keys live only in the store the Director names; agents refer to them by name (e.g. `OPENROUTER_API_KEY`), never by value, in chat, reports, code, or prompts.
- A key seen in any output = incident: stop, report to the Orchestrator, do not repeat the value.

## 6. Prompt line to add to every agent (draft, not deployed)
"Use models only via AGENCY_ROUTER with the alias for your task type (policy: /workspace/pilot/model-policy.md); free-first; on exhausted quota use the fallback once, then report to the Orchestrator; never handle key values."

## 7. Open questions
- Is paid fallback allowed at all, and with what cap? (Founder via Director)
- Which providers are cleared for client data? (Director, pilot)
- Router URL and alias names final? (Integration Developer)

## 8. Verification plan (before deployment)
Golden set per alias (5 inputs each, incl. one prompt-injection and one out-of-scope case) run via router; Tester checks; then Director → Orchestrator clearance; changelog entry in `/workspace/staff/prompts-changelog.md`.


## 2026-11-24 — P0 binding zero-spend amendment
Founder requires $0 Free Engine. This supersedes any earlier paid-fallback wording in this draft. No paid fallback, no automatic billing, no unverified entitlement. Route only explicit verified free provider/model pairs; router price overrides do not establish upstream entitlement. Select by effective context and tool/protocol compatibility before speed; reserve output and tool overhead. If no eligible route fits, checkpoint and split or stop. Never replay partially executed side effects. Local Qwen3-4B is a short-task reserve. Deployment remains unverified until independent tests on existing runtime.
