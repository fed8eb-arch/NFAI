# AI Visibility Protocol — Module 02 (US pilot, Dallas, TX)
Version: v1.1 | Date: 2026-11-23 | Status: two frozen question sets (2A NFAI, 2B WireReady), protocol for review | Owner: Prompt Engineer | Reviewer: Бадди
Change log: v1.0 (2026-11-23) — from `../../ai-visibility-questions.md` v0.1: kept Q1–Q18 (unbranded), prefixed "In Dallas, TX,"; Q19–Q20 (branded) removed until the Founder confirms the brand name; added scoring instructions.
Change log: v1.1 (2026-11-23) — added section 2B: 18 unbranded B2B questions for WireReady (W01–W18), sourced from `competitors.md` v0.1 (commit 4f75121); section 2 renamed 2A (NFAI set unchanged).

## 1. Scope and limits
- Measures how often and how accurately AI assistants mention the measured brand for unbranded buyer questions.
- Measured brand: set by the Director before the run (field `BRAND`, plus aliases). Not fixed in this file.
- Engines: only approved official engines (ChatGPT, Gemini, Perplexity; Alice only if the property is in Yandex). Any substitute (for example LiteLLM `free-chat`) is labelled "substitute — not engine SoV" in every row.
- Intermediate metric only. No causal claim about leads, sales or profit (MISSION.md rule 8).
- No new accounts, spending or site changes without a Founder yes cited by ID.

## 2A. Frozen question set — NFAI (18, unbranded)
Source for all items: Prompt Engineer draft v0.1 (2026-11-23), written from the service category (AI growth / automation / lead conversion). Not yet validated against real sales calls or site-form questions — to be replaced or confirmed when those exist (training step 1).

| ID | Question (ask verbatim) |
|---|---|
| Q01 | In Dallas, TX, what are the best AI marketing agencies for small businesses? |
| Q02 | In Dallas, TX, which companies help small businesses use AI to get more leads? |
| Q03 | In Dallas, TX, who can set up an AI growth system for my business in 2027? |
| Q04 | In Dallas, TX, what is an "AI Growth OS" and which companies offer one? |
| Q05 | In Dallas, TX, what are the best done-for-you AI automation agencies for service businesses? |
| Q06 | In Dallas, TX, which are the top AI agencies that build custom AI agents for sales and marketing? |
| Q07 | In Dallas, TX, what are the best AI lead-conversion tools that integrate with a CRM for a small business? |
| Q08 | In Dallas, TX, which AI chatbots convert website visitors into booked calls best? |
| Q09 | In Dallas, TX, what are the alternatives to hiring a marketing agency — which AI services do growth for you? |
| Q10 | In Dallas, TX, what are the best AI tools to automate lead follow-up by email and SMS for local businesses? |
| Q11 | In Dallas, TX, how can a dental, law or real estate firm use AI to get more clients, and who can implement it? |
| Q12 | In Dallas, TX, who builds AI agents that answer leads 24/7 and book appointments? |
| Q13 | In Dallas, TX, which agencies help e-commerce brands increase conversions with AI? |
| Q14 | In Dallas, TX, what are the best AI content and SEO automation services for B2B companies? |
| Q15 | In Dallas, TX, who can help my business show up in ChatGPT and AI search answers? |
| Q16 | In Dallas, TX, how much does an AI automation agency cost per month? |
| Q17 | In Dallas, TX, what should I look for when choosing an AI agency, and which ones are reputable? |
| Q18 | In Dallas, TX, are there affordable AI growth agencies for startups with case studies? |

Note: this set fits an AI-services brand. If the measured brand is WireReady (Dallas data center electrical construction / apprenticeship prep), these questions do not match its category; a separate category-specific set is needed.

## 2B. Frozen question set — WireReady (18, unbranded, B2B)
Use when `BRAND` = WireReady (Dallas-area data center electrical construction, https://wireready-pilot.netlify.app).
Buyer personas: general contractors (GC) sourcing electrical subs, data center developers/owners, colocation operators' construction/procurement teams.
Source: `competitors.md` v0.1 (Researcher, 2026-11-23, commit 4f75121). "§2" = a real Google autocomplete suggestion (shows the query exists, not its volume; volume = no data). "§1" = a service competitors state on their own sites. "§3" = Researcher's hypothesis (GC, tenders, LinkedIn), not a fact.
**Assumption** = phrasing written by the Prompt Engineer, not observed in the data; validate against real RFQs/sales calls before relying on it.
No competitor names appear in questions (avoids leading the engine).

| ID | Question (ask verbatim) | Source | Assumption? |
|---|---|---|---|
| W01 | Who are the top data center electrical contractors in Texas? | §2 "top …", "… in texas" | no |
| W02 | Who are the largest data center electrical contractors in the Dallas–Fort Worth area? | §2 "largest …" | no (DFW geo added) |
| W03 | Which mission critical electrical contractors work on data center projects in Dallas, TX? | §2 "mission critical electrical contractors" | no |
| W04 | Which electrical subcontractors do general contractors use for data center builds in Dallas–Fort Worth? | §3 (GC channel) | **yes** |
| W05 | I'm a general contractor bidding a data center project in Dallas. Which electrical subcontractors should I invite to bid? | §3 (tenders) | **yes** |
| W06 | Which electrical contractors in Dallas do colocation fit-outs, including white space, PDUs and busway? | §1 (Allied, Blue Ridge) | no |
| W07 | Who can install UPS systems, generators and automatic transfer switches for a data center in Dallas, TX? | §1 (Allied, Walker) | no |
| W08 | Which electrical contractors in the Dallas area handle medium-voltage work for hyperscale data centers of 100 MW or more? | §1 (Oak Shield) | no |
| W09 | Who does data center electrical testing and commissioning in Dallas–Fort Worth? | §1 (Walker) | no |
| W10 | What are the electrical requirements for a new data center, and which Dallas contractors can build to them? | §2 "data center electrical requirements" | no (Dallas clause added) |
| W11 | Which electrical contractors in Dallas offer design-build for data centers? | §1 (FSG) | no |
| W12 | Who provides 24/7 emergency electrical service for data centers in Dallas? | §1 (FSG) | no |
| W13 | Which Dallas electrical contractors have data center case studies with major colocation or hyperscale clients? | §3 conclusion (case studies as key signal) | **yes** |
| W14 | Which licensed Texas electrical contractors (TECL) specialize in data centers in the Dallas area? | §1 (TECL numbers on sites) | no |
| W15 | Which data center electrical contractors in Dallas work in live facilities under MOPs and NFPA 70E? | §1 (Blue Ridge) | no |
| W16 | How should I prequalify an electrical contractor for a data center project in Texas, and who meets those criteria in Dallas? | — | **yes** |
| W17 | How much does data center electrical construction cost per MW in Dallas, TX? | — (prices: no data in §1) | **yes** |
| W18 | Which electrical contractors can quickly staff a large data center project in Dallas–Fort Worth with enough electricians? | — (labour capacity; GCATS "200+ technicians" claim in §1) | **yes** |

Counts: 12 grounded in data (§1/§2), 6 assumptions (W04, W05, W13, W16, W17, W18).
Not used: §2 "data center power dallas / … world power dallas 2026" (conference intent, not a purchase); "… in usa" (outside the local pilot).
Limits: autocomplete is US-wide, not Dallas-specific; no volume data, so the set is not weighted by demand. If the §3 hypothesis holds (demand comes via GC/tenders/LinkedIn), AI-answer visibility is a secondary channel for WireReady — report it as such.

## 3. Run procedure
1. New clean session per question (no memory, no custom instructions, logged out of personal history where possible). Record engine, model/mode shown in the UI, date-time (PT), location setting if shown.
2. Paste the question verbatim. Do not add follow-ups.
3. Save the full answer text and every cited URL verbatim (copy or export; screenshot as backup).
4. Repeats: R runs per question per engine. Record R. If R < 100, mark every rate "wide interval / indicative". A single pass is labelled "indicative, not a measurement".
5. Same list, same engines, repeat after 30 days for the before/after table.

## 4. Scoring each answer
Fill one row per answer:

| Field | Values / rule |
|---|---|
| run_id, engine, model_or_mode, datetime_pt, question_id, repeat_no | as recorded |
| mentioned | yes / no — brand name or any listed alias appears anywhere in the answer |
| position | 1..N = order of the brand among all named companies/products in the answer (first named = 1); "—" if not mentioned |
| total_named | number of distinct companies/products named |
| linked | yes / no — brand's own domain appears among cited URLs |
| sources | all cited URLs, verbatim; classify each: brand-owned / directory-review / media / competitor / other |
| competitors_named | list, verbatim names |
| accuracy | correct / partly wrong / wrong / n.a. — compare every brand claim (services, location, prices, contacts) with the brand's official site on the run date; quote each wrong claim verbatim |
| confusion | yes / no — brand confused with another company of a similar name |
| sentiment | positive / neutral / negative toward the brand; quote the sentence that decides it |
| notes | anything unusual (refusal, outdated info, hallucinated company) |

Rules:
- Every mention gets accuracy and sentiment tags (100%).
- A mention with a wrong or damaging statement counts as a failure, not a win.
- If there are zero mentions, state it explicitly.

## 5. Report
- Mention rate = answers with mentioned=yes / all answers, per engine and overall, with R stated.
- Average position (mentioned answers only); citation share of brand-owned URLs.
- Top cited domains and top competitors across all answers.
- At least three verbatim accuracy/sentiment examples, or "zero mentions".
- Engines actually used; any substitute labelled.
- Raw log (CSV/JSON) committed next to the report so every number can be recomputed.

## Language
Questions are asked in English (US market). Reports to the Founder are in Russian.
