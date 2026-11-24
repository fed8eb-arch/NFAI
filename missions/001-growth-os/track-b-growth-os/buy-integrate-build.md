# Buy vs Integrate vs Build — six modules of NFAI AI Growth OS

Date: 2026-11-23, America/Los_Angeles.  
Rule (t458u): **BUY + INTEGRATE + BUILD**. Adopt the best ready services (including those named by Rush Conf speakers), integrate them into the OS, and build NFAI’s own components where they are needed for integration, quality control, cost, vendor independence, or a competitive edge. **NFAI is not a reseller** of Rush Analytics, Semrush, a CRM, or any other vendor product.

Service names and PDF pages: [Track A catalog](../track-a-rush-conf/services.md). Speaker result claims stay under Track A statuses in [claims.md](../track-a-rush-conf/claims.md) until independently verified. Signups, payments, and production changes need the Founder’s explicit yes. Current budget: zero new spend.

Criteria used below: quality of the outcome for a US test, cost (now and later), limits, security / ToS / data, operational efficiency, and a recommendation.

## How the three options are used together

| Option | Meaning for NFAI |
|---|---|
| Buy | Pay for or subscribe to a ready service and **operate it** as part of a client system (not resell the vendor’s license as “NFAI’s product”). |
| Integrate | Connect a service NFAI already may use, or a free official product, into the module’s workflow, data, and checks. |
| Build | Write NFAI-owned process, harness, prompts, QC, data model, or glue. Build when a vendor would lock NFAI in, hide the method, or charge for something we can do better as an agency OS. |

## Module 01 — Market Intelligence

Purpose: sourced picture of market, demand, audience, and competitors, so later modules do not guess.

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | Ahrefs or Semrush (named/cited in Shestakov’s deck for citation and query research). | High coverage of search and backlink data if the plan fits the market. | Paid. Official pricing pages exist ([ahrefs.com/pricing](https://ahrefs.com/pricing), [semrush.com/pricing](https://www.semrush.com/pricing/)); exact plan amounts were not extracted from JS-heavy pages on 2026-11-23. Needs Founder yes. | Data is vendor-defined; RU-only sources (Wordstat, etc.) are a poor fit for a US pilot if bought instead of US tools. | Official accounts only; no scraping of closed databases (NFAI OSINT rule). | Fast secondary research once licensed. | **Later, optional**, after a written gap: what public sources cannot answer. |
| Integrate | Public official sites, search, maps listings, company pages; LiteLLM `free-chat` only for summarization of already-collected public text; existing role Исследователь рынка + ОСИНТ. | Quality equals source discipline (URL, date, reliability). | $0 with current stack. | Incomplete market-size figures; no invented TAM. | Public sources only; no keys in the public repo. | Already how NFAI research works. | **Do now.** |
| Build | Research brief schema, evidence log, competitor watch list, question set for module 02, report format tied to business metrics. | Determines whether later work is usable. | Time only. | Does not replace a data vendor. | Keep client and secrets out of public git. | Reusable across pilots. | **Do now** (process and templates, not a new scraper). |

**Recommendation:** Integrate public research + build the brief/evidence format now. Do not buy Ahrefs/Semrush until the Founder approves a named plan. Do not build a search-index clone.

## Module 02 — AI Visibility Engine

Purpose: measure whether named AI systems mention and accurately represent the brand, and whether that later coincides with qualified demand. Intermediate metric only.

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | Rush Analytics AI Results Tracker (listed on [rush-analytics.com](https://rush-analytics.com/), homepage 2026-11-23: first 7 days free, no credit card); or Surfer / Semrush AI visibility suites. Rush Agency “AI diagnosis” is a **service**, not a platform to resell (Shestakov p. 55). | A mature tracker may already do multi-engine collection and repeats. Quality still depends on question design and human reading of answers. | Trial may be free; paid after that. No signup in this pass. | Vendor method may be opaque. Buying a tracker does not make NFAI’s product “Rush Analytics”. | Vendor ToS; no client confidential prompts in a trial without approval. | Faster scale than manual queries. | **Optional later**, as a tool NFAI operates, not a white-label offer. |
| Integrate | ChatGPT, Gemini, Perplexity, Alice — the measurement set on Shestakov p. 44. Webmaster «Видимость сайта в Алисе AI» for properties in Yandex. | This is the only way to claim engine-specific visibility. | Consumer or API plans. Official ChatGPT pricing page: [chatgpt.com/pricing](https://chatgpt.com/pricing/) (HTTP 200, a Free plan is named; paid amounts not extracted here). Other paid amounts similarly not invented. Needs yes. | Alice / Yandex are weak or irrelevant for a US-only property; still useful if NFAI also measures RU brands. Rate limits, ToS on automation. | Use official apps/APIs; do not scrape logged-in sessions. | Manual first (20–30 questions), then automation only if ToS and approval allow. | **Primary path**, after account approval. |
| Build | The existing [module-02 prototype](module-02-prototype/ASSESSMENT.md): question runner, logs, mention/citation detection, tests. Later: multi-run statistics, accuracy/sentiment review, 30-day repeat, comparison of vendor exports vs NFAI logs. | Good as QC and evidence store; **poor as a stand-in for the four engines**. The 2026-11-23 run was 0/10 mentions on `free-chat` only. | $0 on the recorded run (`cost: 0`). | One model, one pass, no sentiment. | Key already stays in `~/secrets`; never committed. | Cheap regression tests. | **Keep and use as the NFAI layer.** Do not extend until the assessment is accepted. Do not publish its numbers as ChatGPT/Gemini/Perplexity/Alice SoV. |

**Recommendation:** Integrate the real engines (with Founder yes). Build/keep the harness and QC so NFAI is not a reseller and can check a vendor. Buy a tracker only if manual+harness cannot scale.

## Module 03 — Website Growth Engine

Purpose: site and content that can be crawled, cited, and converted (SEO, GEO, UX/UI, CRO, schema, analytics, lead capture).

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | Tilda or Webflow as a CMS (named on Shestakov p. 40 as typical comparison queries); Surfer as a content assistant. Tilda official prices read 2026-11-23 from [tilda.cc/pricing](https://tilda.cc/pricing/): Free; Personal $10/month with annual payment or $15/month; Business $20/month annual or $25/month (5 sites, code export). | Fine for new sites; the US pilot already has a live Next.js/Netlify property (WireReady) if that pilot is accepted. | See above; Webflow amounts not extracted (JS). | Switching a live site needs Founder/owner yes. | Hosting ToS, form PII. | High if starting from zero. | Buy a CMS **only** for a new property, not to rebuild a working one. |
| Integrate | Google Analytics 4 ([marketing page](https://marketingplatform.google.com/about/analytics/)); Google Business Profile ([US listing page](https://business.google.com/us/business-profile/)); Search Console; Lighthouse / Playwright already in NFAI; maps/listings where relevant. Yandex Metrica is documented as a free analytics product on [b2b.yandex.ru/adv/metrika](https://b2b.yandex.ru/adv/metrika) — useful for RU, not the default for a US-only site. | Matches Shestakov’s “technical foundation” and “maps card” steps (pp. 26, 45). | Standard GA4 and Business Profile are official free products; no new paid SKU proposed now. | WireReady homepage HTML fetched 2026-11-23 had no JSON-LD, no Plausible script, no gtag in the document (observation, not a full audit). Privacy policy on that site mentions Plausible “when configured”. | Analytics and form data: minimize PII; no keys in git. | Uses tools the team already knows. | **Do after a written audit and Founder yes for any live change.** |
| Build | Answer-page pattern (question in the title, answer in the first sentences — Shestakov pp. 24, 44); `robots.txt` policy for `OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`; no-JS content check; CRO tests with a pre-registered metric. Official bot docs: OpenAI crawlers [developers.openai.com/api/docs/bots](https://developers.openai.com/api/docs/bots); Perplexity crawlers [docs.perplexity.ai/docs/resources/perplexity-crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) (`PerplexityBot` confirmed in that page); Claude-SearchBot: [support.claude.com/en/articles/8896518](https://support.claude.com/en/articles/8896518). | This is the method, not a vendor feature. | Time only. | Does not replace hosting or a design system. | robots.txt changes are production — need yes. | Repeatable across clients. | **Build the checks and the content method.** Do not build a new CMS. |

**Recommendation:** Build the GEO/SEO method and technical checks; integrate free Google properties; do not migrate a live site onto Tilda/Webflow without a separate decision.

## Module 04 — AI Conversion Engine

Purpose: take an inquiry to a qualified conversation and, where appropriate, a sale — with attribution.

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | amoCRM (RU: [amocrm.ru/buy](https://www.amocrm.ru/buy/); international product at the same vendor family is Kommo, [kommo.com](https://www.kommo.com/buy/tariff/)); Bitrix24 ([bitrix24.com/prices](https://www.bitrix24.com/prices/)). Both appear in speaker slides as CRM examples, not as a mandatory stack. Rick.ai ([rick.ai](https://rick.ai/), “Try for free” on the homepage 2026-11-23) is Krasinsky’s attribution product. | A real CRM beats a spreadsheet once volume exists. | Paid or freemium; amounts not extracted. Needs yes. | amoCRM.ru is the RU product; a US pilot should not assume it is the right legal/hosting choice. | PII, CRM ToS, DPA; NFAI rule: no client PII to unapproved models (including some free Gemini use). | Fast once chosen. | **Choose one CRM after the Founder names it.** Do not resell CRM seats as “NFAI CRM”. |
| Integrate | Existing site forms (WireReady project inquiry is a public form); LiteLLM or an approved model for **non-PII** drafts; calendar later; “how did you hear about us?” in the form (Shestakov p. 50). Draft requirements already in [crm-lead-module-requirements.md](../crm-lead-module-requirements.md) — that draft predates the Product C naming in t452u and describes module 04, not the Growth Agent Team. | Quality = speed of first reply + qualification accuracy + no lost leads. | $0 until a CRM/email provider is approved. | WireReady privacy policy says Resend/Supabase apply “when configured”; this assessment did not verify that delivery is live. | CAN-SPAM / TCPA if email/SMS; no confidential drawings in forms (already on the public WireReady form copy). | Start with a human SLA and a logged form. | **Integrate attribution and a logged intake now (process); wire a CRM after approval.** |
| Build | Lead record schema, deduping, qualification rubric, handoff rules, fallback when the model fails, audit log. | This is NFAI’s conversion layer and QC. | Time. | Do not build a full CRM. | Store PII off the public repo. | Prevents vendor lock-in of the process. | **Build the process and glue, not a CRM clone.** |

**Recommendation:** Build the qualification/attribution layer; integrate one approved CRM and the site form; buy Rick.ai only if channel ROMI cannot be seen otherwise.

## Module 05 — Growth Analytics

Purpose: one view of visibility, traffic, leads, sales, CAC, margin, and incremental effect. Business metrics are primary.

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | Rick.ai or a paid analytics suite. | Can speed multi-channel attribution if the implementation is honest. | Paid; needs yes. | Still cannot turn SoV into profit without a causal design. | Data processing agreements. | High if already in the stack. | Optional later. |
| Integrate | GA4, ad accounts (only if used), CRM stages, form/call source field, spreadsheet or Looker Studio-class free dashboard if available. | Sufficient for a first pilot if definitions are written down. | $0 if we stay on free official tools. | Shestakov p. 50: AI-influenced visits may appear as Direct. | Access control on analytics properties. | Immediate. | **Do now, as a definition + collection plan** (implementation on a live property needs yes). |
| Build | Metric dictionary (primary vs intermediate); incrementality rules (holdout, geo split, or pre-post with a control; limits). Methods with URLs: Google’s geo-experiment paper [research.google/pubs/measuring-ad-effectiveness-using-geo-experiments](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/); GeoLift methodology [facebookincubator.github.io/GeoLift/docs/Methodology](https://facebookincubator.github.io/GeoLift/docs/Methodology/); trustworthy experiments [experimentguide.com](https://experimentguide.com/). | This is the anti-reseller, anti-hype core of the OS. | Time. | A US site with little traffic cannot run a powerful geo test; that limit must be stated, not hidden. | No fabricated lift. | Reusable for every client. | **Build the metric and causality rules now.** |

**Recommendation:** Build the KPI and causality model first. Integrate free analytics and lead-source questions. No causal GEO→profit claim without a design that fits the traffic you actually have.

## Module 06 — Autonomous Agent Operations

Purpose: specialized agents do real work, hand off evidence, and pass independent review.

| Option | What | Quality | Cost | Limits | Security | Efficiency | Recommendation |
|---|---|---|---|---|---|---|---|
| Buy | A third-party “AI agency OS”. Not required. Speaker gifts (Metastabilnost diagnosis, Rush diagnosis) are optional inputs, not the OS. | Would make NFAI look like a reseller or a clone. | Paid or lead-gen. | Conflicts with the “do not copy Rush Agency” rule. | Third-party sees process data. | False shortcut. | **Do not buy a substitute for NFAI’s own operations.** |
| Integrate | Existing NFAI agents, memory graph, LiteLLM, OmniRoute, local Claude Code (box + PC), Codex, Brain Bridge, staff profiles. Already checked in [INFRA.md](../INFRA.md). Claude Code and OpenAI Codex are what Gurbanov p. 46 tells teams to learn — NFAI already runs both under current authorizations. | Quality = clear owner, deadline, evidence, independent QA (Tester / mentors). | $0 new if we stay inside approved tools. Codex uses the existing ChatGPT allowance (remaining quota is not visible in the CLI). | Box Claude Code: one task at a time on ports 11435/20129. Brain Bridge is async, not a live bus. | Public repo: no secrets. | This is the current operating system. | **Integrate and tighten** existing operations. |
| Build | Playbooks, TASKS journal, acceptance tests, handoff format, stop rules (captcha, payment, production). Product C (Growth Agent Team) must **map existing roles**, not duplicate them. | This is NFAI’s edge. | Time. | Roles without a human reviewer will drift. | Merit registry stays out of the public repo. | Parallel work already expected (PC + box Claude Code). | **Build playbooks and gates.** |

**Recommendation:** Build and integrate NFAI operations. Do not purchase another company’s operating system. Use Claude Code / Codex as tools, not as a product we resell.

## Cross-cutting recommendation

1. **Now ($0, no production change):** public research, metric dictionary, prototype kept as QC harness, training playbooks, audit *plans* for the chosen pilot.  
2. **After Founder yes:** accounts for the four visibility engines and (if needed) one CRM, one analytics property, one tracker.  
3. **Never:** sell a vendor login as an NFAI product; claim engine SoV from the LiteLLM run; claim profit lift from GEO without a valid design.
