# Router Design Draft — "AGENCY_ROUTER" (free-first LLM proxy)

Version: v0.4 draft | Date: 2026-11-17 (v0.2: decisions 13:25 ET in §9; v0.3: Director decisions 13:32 ET in §9; v0.4: Founder zero-spend rule — paid paths rejected, free-only guard §4.2a, reasoning effort §4.3) | Status: DRAFT, design only (nothing registered, no keys, no calls made)
Owner: Integration Developer | Task: D1(a), Director brief #1, phase A | Reviewer: Orchestrator
Access date for every cited doc below: **2026-11-17**. Marks: `[doc]` = stated in official docs cited; `«нет данных»` = not found in official docs; `UNVERIFIED` = nothing tested until Phase B test calls.
Note: all provider/model names are taken from docs as published; model IDs are left as placeholders and are to be read from each provider's `/v1/models` (or console) in Phase B. No endpoint below is invented; each base URL has a source.

## 1. Goal
One OpenAI-compatible endpoint (`AGENCY_ROUTER`) for all agency agents. Agents ask for a model CLASS (alias from `/workspace/pilot/model-policy.md`: `code`, `research`, `write-ru`, `write-en`, `long`, `vision`, `general-small`, `general-large`). The router tries free upstreams first, switches automatically when a quota/limit error occurs, and writes a usage log. No paid upstream is configured until the Founder approves spending (via Director).

## 2. Recommended stack: LiteLLM Proxy
Reasons (all `[doc]`): OpenAI-format proxy over many providers; per-deployment `rpm`/`tpm`/`rpd`/`tpd`; priority `order` with automatic escalation on failure; fallbacks; cooldowns; retries; virtual keys with per-key spend/limits; spend logs.

| Capability | What the docs say | Source |
|---|---|---|
| `config.yaml` sections | `model_list`, `router_settings`, `litellm_settings`, `general_settings`, `environment_variables`; `model_name` = client-facing alias; `litellm_params.model` = upstream; `api_key: "os.environ/NAME"` reads env var; `openai/` prefix + `api_base` = any OpenAI-compatible upstream | https://docs.litellm.ai/docs/proxy/configs |
| Same alias, many deployments | Deployments sharing `model_name` are load-balanced/retried across each other | https://docs.litellm.ai/docs/routing |
| Priority (free-first) | `order` in `litellm_params`: lower = higher priority; on failure (connection error, 404, 429…) router tries `order=2`, then 3…; each order level gets its own retries; then configured fallbacks | https://docs.litellm.ai/docs/routing (section "Deployment Ordering (Priority)") |
| Per-deployment limits | `rpm`, `tpm` in `litellm_params`; also `rpd`/`tpd` (UTC day, optional `daily_reset_time`), enforced via `enforce_model_rate_limits`, which moves a request off a deployment whose daily quota is spent | https://docs.litellm.ai/docs/routing |
| CAVEAT on rpm | If `rpm`/`tpm` is set and `max_parallel_requests` is not, LiteLLM derives a per-process concurrency cap from it (`rpm: 2` → 2 concurrent); over-cap requests get an immediate 429 before any provider call (no queue), which counts as a normal 429 for retries/fallbacks but NOT toward cooldown; cap is per worker, not shared | https://docs.litellm.ai/docs/routing (section "Max Parallel Requests") → run ONE worker or add Redis; verify in Phase B |
| Cooldowns | Per deployment, not per model group. Default `cooldown_time` 5 s. Auto cooldown on: 429 (immediate), >50% failures in the current minute, and 401/404/408. `allowed_fails` / `cooldown_time` settable in `router_settings` and per deployment; recovery is automatic after the period | https://docs.litellm.ai/docs/routing (section "Cooldowns / How Cooldowns Work") |
| Retries | `num_retries`; exponential backoff for `RateLimitError`; generic errors retried immediately; `retry_policy` sets retries per error type (`RateLimitErrorRetries`, `TimeoutErrorRetries`, `AuthenticationErrorRetries`, …); `AllowedFailsPolicy` per error type | https://docs.litellm.ai/docs/routing ("Retries", "Custom Retries, Cooldowns based on Error Type") |
| Fallbacks | `router_settings.fallbacks: [{"a": ["b","c"]}]` in order; `default_fallbacks`; `context_window_fallbacks`; `content_policy_fallbacks`; fallbacks apply after `num_retries`; `disable_fallbacks` per request/key | https://docs.litellm.ai/docs/proxy/reliability |
| Timeouts | `timeout` / `stream_timeout` in `litellm_params`; `request_timeout` in `litellm_settings` (raises Timeout error; per-attempt budget) | https://docs.litellm.ai/docs/proxy/reliability (section "Fallbacks + Retries + Timeouts + Cooldowns") |
| Virtual keys | `/key/generate` (needs `master_key` + Postgres `DATABASE_URL`); per-key `models`, `metadata`, rpm/tpm, budgets; spend per key | https://docs.litellm.ai/docs/proxy/virtual_keys |
| Budgets | Global `litellm_settings.max_budget` + `budget_duration`; key/team/user budgets. Need a DB; without one budgets fail open (not enforced). Budget checks are skipped for models with `input_cost_per_token: 0` AND `output_cost_per_token: 0` set explicitly | https://docs.litellm.ai/docs/proxy/users |
| Spend logs | `/spend/logs`; `LiteLLM_SpendLogs` rows keyed by `request_id`; zero-priced requests still logged with spend 0; `metadata.original_model_group` shows fallback origin | https://docs.litellm.ai/docs/proxy/cost_tracking |
| Logging / redaction | `litellm.turn_off_message_logging: True` stops messages/responses going to logging providers while metadata (spend) is still tracked; each request has `x-litellm-call-id` header | https://docs.litellm.ai/docs/proxy/logging |
| Custom callbacks | `CustomLogger` hooks: `async_log_success_event`, `async_log_failure_event`; per-attempt hooks fire once per real deployment call incl. retries/fallbacks (`async_post_call_failure_deployment_hook(..., fallback_depth)`) — usable for our own usage log and breaker metrics | https://docs.litellm.ai/docs/observability/custom_callback |

Not documented / «нет данных»: jitter in LiteLLM's backoff (docs say "exponential backoff", no jitter mentioned); a separate circuit-breaker feature (cooldown is the documented equivalent); the exact YAML location of `enforce_model_rate_limits` and `enable_pre_call_checks` (Python examples shown, YAML placement to confirm in Phase B); whether `rpd/tpd` need Redis for multi-worker. Running with SQLite instead of Postgres for virtual keys/budgets: «нет данных» (docs require Postgres).

Alternative (sourced, brief): use OpenRouter itself as a single upstream — its docs say it handles provider fallbacks and supports fallback models (https://openrouter.ai/docs/api-reference/limits, https://openrouter.ai/docs/quickstart). Limitation: this only covers OpenRouter's catalog and its own free-model caps (see §3), so it cannot be the whole router. Hugging Face's router is also "powered by OpenRouter" per https://huggingface.co/docs/inference-providers/index.

## 3. Candidate free upstreams (all UNVERIFIED until Phase B test call)
Base URLs are what the official docs show for OpenAI SDK use. Limits are "as documented"; anything else = «нет данных».

| Upstream | OpenAI-compatible base URL (source) | Free tier as documented (source) | Quota-exhaustion signal | Notes / risks |
|---|---|---|---|---|
| **OpenRouter** | `https://openrouter.ai/api/v1` (https://openrouter.ai/docs/quickstart) | Only models with ID ending `:free`. 20 req/min; 50 req/day if <10 credits ever purchased, 1000/day if ≥10 purchased — **REJECTED: no credits, ever (Founder, 17.11; rules.md п.13)** (https://openrouter.ai/docs/api-reference/limits). Daily counter via `GET /api/v1/key` → `free_model_daily_requests` (UTC day) | 429 with `X-RateLimit-*` (+`Retry-After` when present); mid-stream limit arrives as SSE event `finish_reason:"error"` code 429; negative credit balance → 402 even for free models | **Credits REJECTED (Founder, 17.11): plan only for 50/day, `:free` model IDs only.** Docs: extra accounts/keys do NOT raise limits (global capacity) → another reason for 1 account. `:free` model list changes: read from `GET /api/v1/models` |
| **Groq** | `https://api.groq.com/openai/v1` (https://console.groq.com/docs/openai) | Per-model table published (RPM/RPD/TPM/TPD), labelled "base limits for the Developer plan"; e.g. `openai/gpt-oss-120b`: 30 RPM, 1K RPD, 8K TPM, 200K TPD (https://console.groq.com/docs/rate-limits). Whether these = free plan: «нет данных»; the account Limits page is authoritative | 429 + `retry-after`; headers `x-ratelimit-*` (requests = per day, tokens = per minute) | Unsupported fields give 400: `logprobs`, `logit_bias`, `top_logprobs`, `messages[].name`, `n≠1` → set `drop_params` or avoid. Org-level limits |
| **Google AI Studio (Gemini API)** | `https://generativelanguage.googleapis.com/v1beta/openai/` (https://ai.google.dev/gemini-api/docs/openai) | Free tier exists, "limited access to certain models": several Flash/Flash-Lite models list "Free of charge"; top models (e.g. Carbon, Argon) "not available on Free tier" (https://ai.google.dev/gemini-api/docs/pricing). RPM/TPM/RPD per model: «нет данных» in docs (shown only in AI Studio; https://ai.google.dev/gemini-api/docs/rate-limits). Limits are per project, RPD resets midnight Pacific | 429 `RESOURCE_EXHAUSTED` | **Privacy: Free tier content "used to improve our products"** (pricing page) → no client PII/secrets via free Gemini. OpenAI-compat is labelled beta. Some projects "need verification" (rate-limits page) |
| **Mistral (La Plateforme / Studio)** | Base URL: «нет данных» (not found on pages read) | Official docs: "Free mode … **doesn't include API access. Creating API keys and using the API require billing activation and pay-as-you-go**" (https://docs.mistral.ai/admin/billing-usage/usage-limits). A third-party snapshot claims free API quotas — NOT official, rejected | 429 (https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them) | **Likely NOT usable as free upstream** per official docs → flag to Researcher/Director; do not register unless Founder approves billing. Conflicts with the "Mistral free tier" assumption in the Founder materials |
| **Hugging Face Inference Providers** | `https://router.huggingface.co/v1` (https://huggingface.co/docs/inference-providers/pricing) | Free users: **no monthly credits**, usage requires purchased credits; PRO $2/month credits (https://huggingface.co/docs/inference-providers/pricing). So no free tokens for a free account | «нет данных» | **Not free** on a free account → exclude from free-first tiers unless Founder pays. Chat tasks only via this endpoint (index page) |
| **DeepSeek** | `https://api.deepseek.com` (https://api-docs.deepseek.com/) | Sign-up free allowance: «нет данных» (not on pages read). Documented limits are concurrency only: `deepseek-flash` 2500, `deepseek-v4-pro` 500 per account (https://api-docs.deepseek.com/quick_start/rate_limit) | HTTP 429 when concurrency exceeded | Pay-per-token service, no documented free tier → likely paid-only. Request field `user_id` exists (no PII in it) |
| **Qwen (Alibaba Cloud Model Studio / DashScope)** | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` (Singapore; https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen) → needs workspace id, env `DASHSCOPE_API_BASE` | New-user free quota (Singapore, International scope): typically 1,000,000 tokens per model, input+output combined, **valid 90 days** from activation/model release/approval; separate per model; no auto-switch between models; re-registering gives no new quota (https://docs.modelstudio.console.alibabacloud.com/en/model-studio/new-free-quota; https://www.alibabacloud.com/help/en/model-studio/new-free-quota-validity-adjustment). "Free Quota Only" is OFF by default → after quota ends it bills pay-as-you-go (https://www.alibabacloud.com/help/en/model-studio/model-usage-statistics) | With "Free Quota Only" ON: **403 `AllocationQuota.FreeTierOnly`** (not 429!) | MUST enable "Free Quota Only" before first call; router must treat 403 FreeTierOnly as quota-exhausted. Account info completion required before activation (what it asks for: «нет данных» → check for phone/card/KYC). Russia availability: «нет данных» |
| **Z.ai** | `https://api.z.ai/api/paas/v4/` (https://docs.z.ai/guides/overview/quick-start) | Official pricing page lists free models: GLM-4.7-Flash, GLM-4.5-Flash, GLM-4.6V-Flash ("Free" in/out/cache) (https://docs.z.ai/guides/overview/pricing). Limits shown only in console (https://docs.z.ai/help/faq): «нет данных». Third-party reports of 1 concurrent request on free Flash models — unofficial, test in Phase B | 429 with business codes 1302 (rate), 1305 (overloaded), 1308/1310 (usage limit), 1113 (no balance/not a free model) (https://docs.z.ai/api-reference/api-code) | Newer GLM-5.3-Flash is paid per pricing page. Separate international (`api.z.ai`) vs China platform. Send a `User-Agent` header (third-party report) |
| **Poe API** | `https://api.poe.com/v1` (https://creator.poe.com/docs/external-applications/openai-compatible-api) | Uses Poe **subscription points** ("All Poe subscribers can use their existing subscription points"); add-on points purchasable. Free-account API allowance: «нет данных». Rate limit 500 req/min (request-based headers; no token-based limit) | 429 `rate_limit_error`; docs: respect `Retry-After` on 429/503 | Likely needs a paid subscription → not free-first unless Founder approves. Unsupported: `n>1`, audio, `parallel_tool_calls` |

**Zero-spend rule (Founder, 17.11, rules.md п.13): Mistral, Hugging Face, DeepSeek, Poe are EXCLUDED (no free API access in docs → paid only).**
Summary (unverified): realistic free upstreams = OpenRouter `:free`, Groq, Google AI Studio (non-PII only), Z.ai free Flash, Qwen free quota (time-limited, 90 d). Mistral, Hugging Face, DeepSeek, Poe have no documented free API access → candidates for «paid-only / excluded» pending Researcher's catalog.
Arena.ai and "uncensored" web chats: no API in the Founder materials; they are NOT router upstreams (see §7). Their ToS were not reviewed: «нет данных».

## 4. Routing and fallback logic
### 4.1 Tiers per alias (free-first)
Each alias = several deployments; `order` encodes priority. Ties inside one `order` level are picked by the routing strategy.
- **Tier 1 (order 1): free, best quality for the class** — OpenRouter `:free` / Gemini free / Z.ai free (class-dependent).
- **Tier 2 (order 2): free, other provider** — Groq / other `:free`.
- **Tier 3 (order 3): free, time-limited or weak** — Qwen free quota (spend it while valid), small models.
- **Tier 4 (paid): REJECTED permanently (Founder, 17.11; rules.md п.13).** No paid deployment is ever added. When all free tiers are exhausted the request fails with a clear error and an alert; it never goes to a paid model.
Capability classes: **strong-general** (`general-large`, `research`, `code`, `write-ru`), **fast-cheap** (`general-small`, `write-en`), **long-context** (`long`; model must have documented context window; verify per provider; use `context_window_fallbacks` + `enable_pre_call_checks`), **vision** (only models documented as multimodal; no fallback → escalate).
Cross-alias fallbacks follow model-policy.md: class alias → `general-large` once → stop and report (never silently go paid).

### 4.2 Limits, quota exhaustion, retries
- Per-deployment limits go in `litellm_params` (`rpm`, `tpm`, `rpd`, `tpd`) from the provider tables above; values left `# TBD` where «нет данных» until read from each console in Phase B. Set `rpd` = documented daily cap minus ~10% safety margin (OpenRouter: 50 or 1000 per UTC day).
- Quota/limit signals → "exhausted": HTTP 429; Qwen 403 `AllocationQuota.FreeTierOnly`; Z.ai 429 codes 1308/1310/1113; OpenRouter 402 (balance <0). 401/404 = misconfiguration → cooldown + alert (do not retry).
- Cooldown: default 5 s is too short for DAILY quotas. Use per-deployment `cooldown_time` (e.g. 60 s for RPM-type 429; for daily caps rely on `rpd` so the router stops sending before the cap; if a daily 429 still occurs, cooldown until next reset — implement via custom callback if `cooldown_time` alone is insufficient). Per-deployment override is supported `[doc]`.
- Retries: `num_retries: 2`, `retry_policy` with `RateLimitErrorRetries: 1`, `AuthenticationErrorRetries: 0`, `NotFoundErrorRetries: 0`, `TimeoutErrorRetries: 1`; LiteLLM backs off exponentially on 429 `[doc]`. Jitter: «нет данных» → agents' clients add ±20% random delay on their own retries, and per-alias `simple-shuffle` spreads load.
- Honour `Retry-After` / `X-RateLimit-Reset` where the provider sends it (OpenRouter, Groq, Poe docs) — via callback metrics; exact LiteLLM behavior: «нет данных».
- Timeouts: `timeout: 60` (non-stream) / `stream_timeout: 60` per attempt; `request_timeout` global 90; total request budget = (1 + retries) × timeout × tiers — keep agent-side deadline ≥ that or lower `num_retries`.
- Circuit breaker = LiteLLM cooldown (`allowed_fails`: 3 per minute, `cooldown_time`: 30–60 s) `[doc]`; no separate breaker exists in docs.
- Hard stop for paid spend (defence in depth): all free deployments set `input_cost_per_token: 0` and `output_cost_per_token: 0`; global `max_budget: 0` so any model accidentally priced > 0 is blocked, while zero-cost models still pass `[doc: users page "Fallback to free models"]`. Requires Postgres; UNVERIFIED → test in Phase B.
### 4.2a Free-only guard (route is switched off, never goes paid) — Phase B, our code, UNVERIFIED
- **Billing signals → disable the deployment, do not retry elsewhere as paid:** HTTP 402 (e.g. OpenRouter negative balance); Qwen 403 `AllocationQuota.FreeTierOnly`; any response/log with `cost_usd > 0`; any provider dashboard charge > 0 found by the daily check. Our `CustomLogger` writes the deployment to a disabled-list (`/workspace/pilot/router/disabled.json`, path TBD); a pre-call hook skips listed deployments. Re-enable only by the Integration Developer after the cause is checked (or automatically after a documented free-quota reset for plain 429/quota exhaustion).
- **Free limit exhausted → route off until reset:** `rpd`/`tpd` set below the free cap (−10%); on daily-cap 429 the deployment is cooled down until the provider's reset, never replaced by a paid variant.
- **Config validation before start (script, Phase B):** reject the config if any deployment has non-zero `input_cost_per_token`/`output_cost_per_token`, if an OpenRouter model ID does not end with `:free`, if any Fable/Claude-paid or Poe deployment is present, or if Qwen lacks the "Free Quota Only" confirmation flag in our checklist.
- **No payment method on any provider account** (no card saved) — then a provider cannot start charging; if a provider asks for a card, stop and report (rules.md п.13, п.17).
- `max_budget: 0` + zero prices stay as the last line of defence (see above).

- One LiteLLM worker (or Redis) because concurrency caps/cooldown state are per worker `[doc]`.

### 4.3 Reasoning effort (Phase B, to work out)
- Rule (Director, rules.md): first pick effort low → medium → high, only then change model; every report states model + effort.
- LiteLLM accepts the OpenAI-style `reasoning_effort` parameter and passes it to providers that support it (https://docs.litellm.ai/docs/reasoning_content, accessed 2026-11-17). Which of our free upstreams/models support it: «нет данных» → check per provider in Phase B; unsupported → dropped by `drop_params: true`.
- Plan: default `reasoning_effort: low` per alias; agents may raise it per request; log field `reasoning_effort` added to the usage log.

## 5. Usage log
Source of truth: our `CustomLogger` (success + failure + per-attempt hooks) writing one row per attempt; LiteLLM `LiteLLM_SpendLogs` (Postgres) as a secondary cross-check (join on `request_id`).
Fields (whitelist only): `ts_utc`, `ts_et`, `request_id` (= `x-litellm-call-id`), `agent` (from virtual-key alias; one key per agent), `alias` (model_group requested), `original_alias` (before fallback), `upstream` (provider name), `model` (resolved), `reasoning_effort`, `attempt_no`, `fallback_depth`, `status` (ok / 429 / quota_exhausted / timeout / error), `http_code`, `error_code` (provider code only, e.g. 1302), `latency_ms`, `ttft_ms` (if streaming), `prompt_tokens`, `completion_tokens`, `cost_usd` (expected 0), `free_tier` (bool).
NEVER logged: prompts, completions, headers, API keys, user content, PII. Enforce with `litellm_settings.turn_off_message_logging: True` `[doc]` and a callback that copies only whitelisted fields.
Where: SQLite file `/workspace/pilot/router/usage.sqlite` (append-only table `usage`) + Postgres spend logs if virtual keys are used. Path TBD with Director (§9). Retention 90 days, then aggregate-only.
Daily summary (cron, 23:55 ET, output `/workspace/pilot/router/daily/YYYY-MM-DD.md`): requests and tokens per upstream/alias/agent; share served free (target 100%); count of 429/quota events and fallbacks; remaining free quota where an API exposes it (OpenRouter `GET /api/v1/key`; others «нет данных»); deployments in cooldown; alerts (no free capacity left for an alias; cost_usd > 0 seen).

## 6. Draft `config.yaml` skeleton (NO real keys; env var names only)
All model IDs are placeholders. Upstreams use the documented `openai/<model>` + `api_base` form (https://docs.litellm.ai/docs/proxy/configs). Limits marked TBD stay «нет данных» until Phase B.
```yaml
model_list:
  # ---------- alias: general-large ----------
  - model_name: general-large
    litellm_params:
      model: openai/<OPENROUTER_FREE_MODEL_ID>          # must end with :free
      api_base: https://openrouter.ai/api/v1
      api_key: os.environ/OPENROUTER_API_KEY
      order: 1
      rpm: 20                                           # documented free cap
      rpd: 45                                           # 50/day documented, ~10% margin
      timeout: 60
      stream_timeout: 60
      input_cost_per_token: 0
      output_cost_per_token: 0
  - model_name: general-large
    litellm_params:
      model: openai/<GROQ_MODEL_ID>
      api_base: https://api.groq.com/openai/v1
      api_key: os.environ/GROQ_API_KEY
      order: 2
      rpm: 30                                           # table value; confirm on Limits page
      rpd: 900
      tpm: 8000
      input_cost_per_token: 0
      output_cost_per_token: 0
  - model_name: general-large
    litellm_params:
      model: openai/<ZAI_FREE_MODEL_ID>                 # GLM-*-Flash free model per pricing page
      api_base: https://api.z.ai/api/paas/v4/
      api_key: os.environ/ZAI_API_KEY
      order: 2
      max_parallel_requests: 1                          # unofficial report; verify
      input_cost_per_token: 0
      output_cost_per_token: 0
  - model_name: general-large
    litellm_params:
      model: openai/<QWEN_MODEL_ID>
      api_base: os.environ/DASHSCOPE_API_BASE           # https://<WorkspaceId>.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1
      api_key: os.environ/DASHSCOPE_API_KEY
      order: 3                                          # only while 90-day free quota is valid
      input_cost_per_token: 0
      output_cost_per_token: 0

  # ---------- alias: general-small (fast-cheap) ----------
  - model_name: general-small
    litellm_params:
      model: openai/<GEMINI_FREE_FLASH_LITE_ID>
      api_base: https://generativelanguage.googleapis.com/v1beta/openai/
      api_key: os.environ/GEMINI_API_KEY
      order: 1
      rpm: TBD                                          # «нет данных»: read in AI Studio
      rpd: TBD
      input_cost_per_token: 0
      output_cost_per_token: 0
      # NOTE: Gemini free tier = content used to improve Google products -> non-PII tasks only
  - model_name: general-small
    litellm_params:
      model: openai/<GROQ_SMALL_MODEL_ID>
      api_base: https://api.groq.com/openai/v1
      api_key: os.environ/GROQ_API_KEY
      order: 2
      input_cost_per_token: 0
      output_cost_per_token: 0
  # ---------- aliases code / research / write-ru / write-en / long / vision: same pattern ----------
  # long: only deployments with documented context window; vision: only documented multimodal models

router_settings:
  routing_strategy: simple-shuffle          # shuffles inside the same `order` level
  num_retries: 2
  allowed_fails: 3                          # per minute, then cooldown
  cooldown_time: 60                         # seconds; per-deployment override for daily-cap upstreams
  retry_policy:
    RateLimitErrorRetries: 1
    TimeoutErrorRetries: 1
    AuthenticationErrorRetries: 0
    NotFoundErrorRetries: 0
    DefaultRetries: 1
  fallbacks:                                # cross-alias, once, then stop (see model-policy.md)
    - {"code": ["general-large"]}
    - {"research": ["general-large"]}
    - {"write-ru": ["general-large"]}
    - {"write-en": ["general-small"]}
    - {"general-small": ["general-large"]}
  # context_window_fallbacks: [{"general-small": ["long"]}]   # confirm alias set in Phase B
  # enable_pre_call_checks: true            # YAML placement: «нет данных», confirm
  # enforce_model_rate_limits: true         # needed for rpd/tpd; YAML placement: «нет данных», confirm

litellm_settings:
  request_timeout: 90
  drop_params: true                         # Groq rejects some OpenAI fields
  turn_off_message_logging: true            # no prompts/responses in logs
  max_budget: 0                             # any accidentally paid model is blocked (needs DB; verify)
  budget_duration: 30d
  callbacks: ["usage_logger.proxy_handler_instance"]   # our CustomLogger writing whitelisted fields (to be written in Phase B)

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/LITELLM_DATABASE_URL   # Postgres; needed for virtual keys, budgets, spend logs
```
Agent access: one virtual key per agent (`/key/generate`, alias = agent name, `models` = allowed aliases, per-key rpm). Each agent receives only its router key by secret NAME (e.g. `AGENCY_ROUTER_KEY_<AGENT>`), never provider keys.

## 7. Security and compliance
- **Secrets:** only env vars / secret store; config, code, logs, chat and reports contain NAMES only (`OPENROUTER_API_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`, `ZAI_API_KEY`, `DASHSCOPE_API_KEY`, `DASHSCOPE_API_BASE`, `LITELLM_MASTER_KEY`, `LITELLM_DATABASE_URL`). **Storage location: TBD — Director decides in phase B.** Alternative LiteLLM can load keys from secret managers (https://docs.litellm.ai/docs/proxy/configs, section "Load API Keys from Secret Managers"); specifics «нет данных» until chosen.
- **Least privilege:** provider keys live only on the router host; agents hold only per-agent virtual keys limited to their aliases; `master_key` used by the Integration Developer only; key rotation: virtual keys rotate on a schedule (LiteLLM documents key rotation: https://docs.litellm.ai/docs/proxy/virtual_keys); provider keys rotated by re-issuing in the provider console (manual, Director-approved) on leak suspicion or every 90 days.
- **Proxy exposure:** bind to localhost/private interface of the shared box only; no public port.
- **Leak handling:** a key seen in any output = incident → stop, tell Orchestrator, do not repeat value; rotate.
- **Data:** no client PII/secrets to free third-party models by default (policy in model-policy.md); Gemini free tier explicitly uses content to improve products. Other providers' free-tier data/training terms: «нет данных» → Researcher to cover in catalog.
- **ToS / anti-abuse:** exactly one account per provider (OpenRouter docs say extra accounts don't raise limits; Qwen docs say re-registering gives no new free quota). No multi-accounting, no key pooling across identities, no VPN or other circumvention of limits, bot checks, phone/KYC. If a provider asks phone/card/KYC → stop and report (Director decides). Arena.ai and similar web-only chat services: no documented API → not in the router; automating a browser UI is out of scope; their ToS: «нет данных» (not reviewed).
- **Cost safety:** zero spend, permanently (Founder, 17.11); free-only guard §4.2a; no paid deployment ever; zero-cost flags + `max_budget: 0`; Qwen "Free Quota Only" ON before first call (default OFF!).

## 8. Phase B test plan (starts only after Director approves registrations and secret storage)
Per upstream, ONE minimal call through the proxy and one direct call (to separate router bugs from provider issues); prompt = fixed harmless string (`"Reply with the single word: ok"`), `max_tokens` small, no client data.
Record per test in `/workspace/pilot/router/phase-b-results.md`: date/time ET, upstream, base URL, exact model ID used, HTTP status, latency ms (and TTFT if streaming), prompt/completion tokens, rate-limit headers received (names only), quota counters seen (e.g. OpenRouter `GET /api/v1/key`), result PASS/FAIL, error code.
Tests:
1. Direct call per upstream → confirms base URL, auth, model ID, free (cost 0), limits visible.
2. Via router per alias → served by expected `order=1` upstream; log row written with whitelisted fields only.
3. Forced failover: disable/over-limit a tier-1 deployment (e.g. low `rpd` in a test config) → request lands on tier 2; `fallback_depth`/original alias recorded. (Mock flags are stripped on the proxy since v1.85.0 per reliability doc; use real over-limit or a wrong test key in non-prod.)
4. Quota-exhaustion handling per upstream where cheaply testable (OpenRouter 429 headers; Qwen 403 FreeTierOnly mapping; Z.ai 1302).
5. Cooldown and recovery timing; retries/backoff observed in log.
6. Log hygiene: grep logs/DB for prompt text and key patterns → must find none.
7. Cost guard: confirm a deliberately mispriced model is blocked by `max_budget: 0`.
8. rpm semantics: confirm rpm/rpd behavior (concurrency-derived cap vs true RPM) with 1 worker.
Acceptance criteria: every approved upstream has PASS direct test or a documented reason to exclude; failover works for each alias with ≥2 upstreams (test 3); zero paid spend (`cost_usd` = 0, provider dashboards show no charges); log has all whitelisted fields and no payload/secret/PII (test 6); no key value appears in any file, chat or report (secret-scan); results table contains no invented data (unknown = «нет данных»). Each upstream stays "UNVERIFIED" in the catalog until its row is PASS.

## 9. Open questions for Director
1. Secret storage: which store holds provider keys and router keys (env file with 600 perms on the shared box, vault, secret manager)? Who may read it?
2. Which agents connect to the router in the pilot (Orchestrator, Researcher, Prompt Engineer, Integration Developer, others)? One virtual key per agent OK?
3. Hosting: run LiteLLM + Postgres (Docker?) on the shared box, bound to localhost/private only? Is Docker available/allowed, and is Postgres acceptable (needed for virtual keys/budgets; without it budgets are not enforced)?
4. Paid use: **CLOSED — paid upstreams rejected permanently (Founder, 17.11; rules.md п.13).** **DECIDED (Director/Founder, 2026-11-17 13:25 ET): OpenRouter credits are NOT bought; plan only within `:free` limits (20 req/min, 50 req/day; `rpd` = 45).**
5. Data policy: confirm that anything with client PII never goes through free upstreams (Gemini free tier trains on content). **DECIDED (Director/Founder, 2026-11-17 13:25 ET): Gemini is enabled; calls go from the shared cloud box, no VPN needed. No client personal data or confidential client materials on the free tier.**
6. Mistral / Hugging Face / DeepSeek / Poe: docs show no free API access — exclude from registration list, or Founder decides on paying?
7. Qwen: sign-up needs "complete account information" (content «нет данных») and free quota lasts 90 days — proceed only if no phone/card/KYC is requested? **DECIDED (Director, 2026-11-17 13:32 ET): Qwen only with "Free Quota Only" ON in the console before the first call (otherwise auto-billing). Free quota removed for qwen-max/plus/turbo/flash and qwen3.6-plus; qwen3.7-max keeps its quota (only its snapshots `qwen3.7-max-*` lost it) → candidate model qwen3.7-max, confirm in console in Phase B.**
8. Where may usage logs/daily summaries live and who reads them? Retention 90 days OK?
9. **DECIDED (Director, 2026-11-17 13:32 ET):** ElevenLabs removed from the top-10 (ToS bars users from Russia; free tier non-commercial only); not registered.
10. **REJECTED permanently (Founder, 17.11; rules.md п.12–13):** paid Fable paths П1–П4 (OpenRouter, Poe API, uncensored.com API, Anthropic Claude.ai/Platform) are rejected; Fable stays out of the router (manual web final-review step only).
11. **Gemini model IDs (checked 2026-11-17, https://ai.google.dev/gemini-api/docs/deprecations, /docs/models):** `gemini-2.5-pro` is deprecated, API access limited to existing users who used it before; from 2026-12-01 all requests to it auto-route to `gemini-3.8-flash` and bill at 3.8 Flash rates → do not configure 2.5 Pro (or 2.5 Flash) for our new project. Use pinned stable model IDs only (read from `/v1/models` in Phase B); do not use hot-swapped `*-latest` aliases (e.g. `gemini-flash-latest`, 2-week email notice before swap).

12. **DECIDED (Founder, 17.11, rules.md п.13):** all work on free services only, spend = 0. Paid subscriptions (Founder's ChatGPT Plus, Director's subscription) are never router upstreams; manual checks only, via the Director.

## 10. Sources (all accessed 2026-11-17)
LiteLLM: https://docs.litellm.ai/docs/proxy/configs · /docs/routing · /docs/proxy/reliability · /docs/proxy/users · /docs/proxy/virtual_keys · /docs/proxy/cost_tracking · /docs/proxy/logging · /docs/observability/custom_callback
OpenRouter: https://openrouter.ai/docs/api-reference/limits · https://openrouter.ai/docs/quickstart
Groq: https://console.groq.com/docs/rate-limits · https://console.groq.com/docs/openai
Google: https://ai.google.dev/gemini-api/docs/openai · /docs/rate-limits · /docs/pricing
Mistral: https://docs.mistral.ai/admin/billing-usage/usage-limits · https://docs.mistral.ai/getting-started/models/ · https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them
Hugging Face: https://huggingface.co/docs/inference-providers/index · /pricing
DeepSeek: https://api-docs.deepseek.com/ · /quick_start/rate_limit
Alibaba Model Studio: https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen · https://docs.modelstudio.console.alibabacloud.com/en/model-studio/new-free-quota · https://www.alibabacloud.com/help/en/model-studio/new-free-quota-validity-adjustment · https://www.alibabacloud.com/help/en/model-studio/model-usage-statistics
Z.ai: https://docs.z.ai/guides/overview/quick-start · /guides/overview/pricing · /api-reference/api-code · /help/faq
Poe: https://creator.poe.com/docs/external-applications/openai-compatible-api
Unofficial (used only as flagged hints, not as facts): shahriarlabs.com Z.ai 1302 page, modelhubby.com Z.ai guide (1 concurrent request on free Flash models).

## Out of router: Fable (manual final-review step)
- Per Founder via Director (relayed by Orchestrator, 2026-11-17): every finished deliverable is reviewed and improved on "Claude Fable 5.x" at the end; it is never used to create from scratch.
- Reported availability: Arena.ai / DesignArena (web-only). Not verified by me; no API documented → NOT a router upstream. No API integration is designed for it.
- Process: router-produced result → human/agent pastes it into the web UI manually for the final review step.
- **Paid paths П1–П4 REJECTED permanently (Founder, 17.11; rules.md п.12–13).** Free final review only on web links whose ToS allow it (rules.md п.11–12: Arena manually, internal only; Design Arena / Poe / uncensored.com after ToS check). Paid subscriptions are for manual checks via the Director only; none of this is in the router.
