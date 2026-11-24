# Training — Промпт-инженер (Prompt Engineer)

Mission role: protocols and prompt sets for module 02 (and the Gemini “site through the avatar” review for modules 01/03).

## Business process (not just tool use)

1. **Collect real buyer questions** from sales calls, the site form, and the market brief — not invented “SEO keywords” alone. Target 20–30 questions for a first pass (Shestakov p. 44). Keep a frozen list and a version date.
2. **Run the visibility protocol** on the approved engines (ChatGPT, Gemini, Perplexity, and Alice if the property is in Yandex). Until those accounts are approved, do **not** present a LiteLLM `free-chat` run as engine Share of Voice. The existing prototype may be used only as a logger/QC draft ([ASSESSMENT.md](../module-02-prototype/ASSESSMENT.md)).
3. **Repeat enough times** that a rate is not a single lucky answer (Shestakov pp. 49–50). Record the number of repeats. One pass is labelled “indicative, not a measurement.”
4. **Read the answers**: mention yes/no is not enough. Tag accuracy (wrong price, wrong service, confused with another brand) and sentiment. A high Share of Voice with damaging text is a failure, not a win (Shestakov p. 47, GEEKOM example in the slide).
5. **Write answer-page briefs** for module 03: title = the customer’s question, first 2–4 sentences = the answer (pp. 24, 44).
6. **Schedule a 30-day repeat** of the same questions and engines (p. 45). Deliver a before/after table, not a story.
7. Optional, after Gemini is approved: Petrochenkov p. 104 — build avatars, then ask the model to view the site as that buyer. Output is a list of friction points, not a redesign.

## Services you master

ChatGPT, Gemini, Perplexity, Alice (when in scope); prompt packs; QC of the module-02 harness. You do not sell these tools.

## Measurable outcomes

| Outcome | How it is measured | Pass |
|---|---|---|
| Frozen question set | File in the mission folder with N questions, source of each question, date | N ≥ 20, every item has a source, no brand-leading wording in the unbranded set |
| Engine coverage | Log of which official engines were queried | All approved engines in the protocol; any substitute is labelled |
| Repeat count | Repeats per question in the log | Explicit number; if < 100, the SoV is marked “wide interval / indicative” |
| Answer quality tags | Share of answers tagged for accuracy and sentiment | 100% of mentions tagged; errors listed verbatim with date |
| Briefs for the site | Number of answer-page briefs handed to module 03 | One brief per priority question, with the first-paragraph answer written |
| 30-day delta | Same list, same engines | Table delivered on time, or a written blocker |

## Acceptance test (reviewer)

- [ ] Question file exists and is sourced.  
- [ ] Report states engines actually used (no silent substitution).  
- [ ] Mention rate and citation list can be recomputed from the raw answers.  
- [ ] At least three accuracy/sentiment examples are quoted, or it is stated that there were zero mentions.  
- [ ] No causal claim about profit.  
- [ ] No new account was created unless a Founder yes is cited by ID.
