# W2 — Consent / privacy text for the WireReady project-inquiry form (Legal)

- **Date:** 2026-11-23 (PT)
- **Author:** Head of Legal (agent). Model: Grok Bot (executor subagent); effort: standard.
- **Brief:** `mission-001/briefs/w1-w4.md` @ 4858ba3, section «W2. GA4 + «How did you hear about us» field», step 2; «Open questions and risks», item 7.
- **Sources read (2026-11-23, read-only):**
  - https://wireready-pilot.netlify.app/contact (curl): fields `name`, `company`, `email` ("Work email"), `location`, `phase`, `message`, honeypot `website`; notice "We use these details to respond to your inquiry. See our privacy notice."; no checkbox; no `gtag` / `googletagmanager` string in HTML.
  - https://wireready-pilot.netlify.app/privacy (curl): Resend forwards inquiries "when delivery is configured"; Supabase / Plausible "when configured"; "WireReady is not yet connected to a production service"; owner "must add a support contact". No contact, no legal entity, no retention period, no sale/share statement, no GA mention. The page mostly describes an apprenticeship-assessment MVP (account, veteran status, scores) — see gaps.
  - Cal. Civ. Code §1798.100, §1798.140, §1798.145 (leginfo.legislature.ca.gov); CPPA threshold page https://cppa.ca.gov/regulations/cpi_adjustment.html.
  - Tex. Bus. & Com. Code ch. 541 (statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm).
  - 15 U.S.C. §7702, §7704 (law.cornell.edu).
  - Google Analytics Terms of Service (US), §7 "Privacy", last updated May 15, 2023 (marketingplatform.google.com/about/analytics/terms/us/).
  - GA Help: "IP masking in Universal Analytics" (answer 2763052), "Data retention" (answer 7667196).

> **Status:** agent opinion, not a conclusion of a licensed attorney. Recommendation only — not an agency sign-off. The Founder approves. Applies to the **Netlify preview** only until the gaps in §5 are closed.

---

## 1. Ready-to-paste form text (English)

### 1a. Notice at collection — place directly above the submit button (replaces the current one-liner)

> We use the details you submit (name, company, work email, project location, phase, how you heard about us, and your message) to respond to your inquiry. We also use Google Analytics, which relies on cookies and similar technologies, to measure how visitors find and use this site. [We do not sell or share your personal information.]¹ See our [Privacy Notice](/privacy) for details, including how to request access to or deletion of your information by contacting [CONTACT EMAIL].

¹ **Fact to confirm before use.** Keep the bracketed sentence only if (a) no form data is sold or disclosed to third parties for their own purposes and (b) GA4 is configured with Google signals OFF and no Google Ads / advertising linking (otherwise GA data could fall under "share" = cross-context behavioral advertising, Cal. Civ. Code §1798.140(ah)). If unconfirmed, **delete the sentence** — do not publish an unverified statement.

Preview fallback if `[CONTACT EMAIL]` is still unknown at preview time: end the paragraph at "…for details." and keep the placeholder visible in the PR description as an open item. Do **not** promote to production without a real contact.

### 1b. Short analytics/cookie notice (option, for footer or a small banner — no consent gate)

> This site uses Google Analytics cookies to understand how visitors find and use it. No information you type into our forms is sent to Google Analytics. Learn more in our [Privacy Notice](/privacy) and in [How Google uses information from sites or apps that use our services](https://www.google.com/policies/privacy/partners/).

### 1c. Checkbox decision

- **No checkbox required (recommendation).** Reasons: US B2B project inquiry; data used only to answer the request the visitor initiated and for site analytics; no marketing email (W4 forbids outreach). CCPA §1798.100(a) requires *notice* at or before collection, not consent; TDPSA requires consent only for sensitive data (§541.101(b)(4) — not collected here) and, for small businesses, for *sale* of sensitive data (§541.107). A notice next to the button is the proportionate control.
- **Never a pre-ticked box.** (A pre-ticked box is not an "affirmative act"; cf. "consent" definition, Tex. Bus. & Com. Code §541.001(6).)
- **No marketing opt-in checkbox in W2.** Not included because W4 forbids outreach; adding an unused opt-in would collect consent for a purpose we do not have. If marketing email is planned later, add an *unticked, optional* opt-in then and apply CAN-SPAM (§3c).

### 1d. GA4 configuration requirements (for the Integration Developer; settings, not text)

| Setting | Requirement | Basis |
|---|---|---|
| IP addresses | No action needed: GA4 does not log or store IP addresses | GA Help answer 2763052 (verified) |
| Data retention | Set user/event data retention to **2 months** for the pilot (options: 2 or 14 months) | GA Help answer 7667196 (verified); data minimisation, §1798.100(c) |
| Google signals | **OFF** | keeps "no share" statement accurate (§1798.140(ah)) |
| Google Ads / advertising linking, ads personalization | **OFF / not linked** | same |
| PII in events, URLs, page titles | **Prohibited**: never send name, email, company, message, or the free-text "Other" answer to GA; form must POST (not GET) so values never appear in URLs; the source-field *option value* (e.g. `search`, `linkedin`) may be sent as an event parameter, free text may not | GA ToS §7, first sentence (verified) |
| Consent Mode | Optional for a US-only pilot; required in practice only if EEA/UK traffic is targeted (see §3e) | «не проверено» for EEA mechanics |
| Property owner | GA property must be created under the **client's** account, not an agency account (also: any Google sign-in = STOP per brief) | brief W2 step 4 |

---

## 2. Suggested additions to `/privacy` (list only — the site is not edited by Legal)

1. **Who we are:** [LEGAL ENTITY] (WireReady brand — pending Founder confirmation), [POSTAL ADDRESS], [CONTACT EMAIL].
2. **Separate "Project inquiries" section** listing: categories (name, company, work email, project city/state, phase, how you heard about us, message); purpose (respond to the inquiry; measure which channels bring inquiries); recipients/processors ([PROCESSORS], e.g. Resend for delivery, Netlify for hosting — **confirm which are actually live**).
3. **Analytics section:** "We use Google Analytics …" + cookies/similar technologies + link to https://www.google.com/policies/privacy/partners/ (GA ToS §7 requires disclosure of GA use, cookies, and how GA collects/processes data). Replace/clarify the current Plausible statement if Plausible is not used.
4. **Retention:** inquiry data kept for [RETENTION PERIOD] or criteria (CCPA §1798.100(a)(3)); GA retention 2 months.
5. **Sale/share statement:** "We do not sell or share personal information" — only if confirmed (see ¹).
6. **Your rights / how to request:** access, deletion, correction; at least two methods (e.g. email + web form) — TDPSA §541.055(a) if TDPSA applies; appeal process §541.102(a)(3) if applicable.
7. **Remove "not yet connected to a production service"** and add the support contact before production; otherwise the notice is inaccurate once the form goes live.
8. **Scope note:** the current notice mostly describes an apprenticeship-assessment app (accounts, veteran status, scores). Either confirm that this product is part of the same site/entity or split notices. Out of W2 scope, flagged.
9. **"Effective date"** line.

---

## 3. Applicability analysis

### 3a. California — CCPA as amended by CPRA (Cal. Civ. Code §1798.100 et seq.)
- **Notice at collection:** §1798.100(a) — at or before collection, inform of categories, purposes, whether sold or shared, and retention period. *Verified (leginfo).* Text 1a + privacy additions cover this.
- **"Business" thresholds:** §1798.140(d)(1): for-profit, does business in CA, and (A) annual gross revenue > $25,000,000 as CPI-adjusted (**$26,625,000** effective 2025-01-01, CPPA page), or (B) buys/sells/shares PI of ≥100,000 consumers/households, or (C) ≥50% revenue from selling/sharing PI. *Verified.* WireReady's revenue and CA nexus: **нет данных**. A Dallas contractor may fall below — then CCPA does not apply, but the text is still good practice.
- **B2B exemption:** §1798.145(n) (communications with an employee/owner of a company in a B2B context) is **inoperative since 2023-01-01** ("Subdivisions (m) and (n) inoperative January 1, 2023, by their own provisions"). *Verified.* So business-contact data is covered if WireReady is a "business".
- **Consumer** = natural person who is a CA resident, §1798.140(i) — includes B2B contacts. *Verified.*
- **Share:** §1798.140(ah) — disclosure for cross-context behavioral advertising. *Verified.* Drives the GA settings above.

### 3b. Texas — Data Privacy and Security Act (Tex. Bus. & Com. Code ch. 541)
- **Applicability:** §541.002(a) — conducts business in TX, processes personal data, and **is not a small business as defined by the U.S. SBA** (except §541.107). *Verified.* SBA size status of WireReady: **нет данных** (SBA size standard for electrical contractors: «не проверено»).
- **Consumer** = TX resident acting only in an individual or household context; **excludes an individual acting in a commercial or employment context**, §541.001(7). *Verified.* Inquiries via "Work email" for a commercial project are therefore largely outside TDPSA even if the chapter applies.
- **If applicable:** privacy notice content §541.102(a); ≥2 request methods §541.055(a). Enforcement only by the AG (§541.151), 30-day cure notice (§541.154), civil penalty up to $7,500 per violation (§541.155). *Verified.*
- **Small business:** §541.107 — may not sell sensitive data without prior consent. Not relevant (no sensitive data, no sale).

### 3c. CAN-SPAM Act (15 U.S.C. §7701 et seq.)
- Applies to **commercial electronic mail messages** (§7704(a)(5): identification as ad, opt-out notice, postal address). *Verified (Cornell LII).* A reply to an inquiry the person sent is not a marketing campaign; W2/W4 send no marketing email → **not triggered now**. Becomes relevant if Resend "early-access emails" (mentioned on /privacy) or any follow-up marketing is sent.

### 3d. Google Analytics Terms of Service (US), §7 "Privacy" (last updated 2023-05-15) — *verified*
- No PII passed to Google (first sentence).
- "You must post a Privacy Policy and that Privacy Policy must provide notice of Your use of cookies … or similar technology used to collect data. You must disclose the use of Google Analytics, and how it collects and processes data" — may be done by a prominent link to www.google.com/policies/privacy/partners/.
- Cookie consent "where … required by law".
- Current /privacy does **not** mention GA → must be added before GA runs on production (on preview: recommended).

### 3e. Google EU user consent policy / GDPR / EEA
- Only if EEA/UK visitors are targeted or GA Ads features are used. WireReady targets Texas/US data-center projects → treated as **not applicable** for the pilot. Text of the EU user consent policy and GDPR Art. 3(2) territorial scope: **не проверено** in this review.

### 3f. Other US states
- Other state comprehensive privacy laws (e.g. Virginia, Colorado): **не проверено**; most exclude B2B/employment-context individuals similarly to Texas — **не проверено**, do not rely on.

---

## 4. Residual risk (after text 1a + GA settings 1d)

| Area | Rating | Reason |
|---|---|---|
| Preview only (not public traffic), test data | **Low** | No real visitors' data; text present. |
| Production with 1a but **without** contact email / entity on /privacy | **Medium** | Notice at collection incomplete (no request route); /privacy says "not connected to a production service" — inaccurate once live. |
| CCPA overall | **Low** | Probably below thresholds (нет данных); text meets §1798.100(a) if retention and contact are filled. |
| TDPSA | **Low** | Commercial-context individuals excluded (§541.001(7)); possible SBA small-business exemption. |
| GA ToS §7 | **Medium → Low** | Medium until /privacy discloses GA + link; Low after addition. |
| "We do not sell or share" statement | **Medium** if published unverified; **Low** if confirmed or removed | Misstatement risk. |
| PII leaking into GA (free text, URLs) | **Medium → Low** | Low only if 1d rules are implemented and checked in GA DebugView. |
| CAN-SPAM | **Low** | No commercial email sent. |
| PII in public NFAI repo (item 7) | **Medium** | Public repo + test submissions/screenshots/logs; mitigated by §6 rules. |

---

## 5. Gaps (facts Legal needs — not invented)

1. **[LEGAL ENTITY]** — legal name, state of formation, address.
2. **Brand** — Founder confirmation of "WireReady".
3. **[CONTACT EMAIL]** — privacy/support contact (public notice states it is not yet added).
4. Whether inquiry data is **actually stored**, and where (Resend only? Supabase? Netlify Forms? sales inbox provider?).
5. **[PROCESSORS]** — list of live providers and whether their DPAs/terms were accepted by the site owner.
6. **[RETENTION PERIOD]** for inquiries and email.
7. Whether any data is **sold or shared** (incl. GA Google signals / Ads linking).
8. WireReady **revenue / CA business activity** (CCPA threshold) and **SBA small-business status** (TDPSA).
9. Whether **EEA/UK** visitors are targeted.
10. Whether Plausible is used at all (current notice) vs. GA4.
11. Whether the apprenticeship-assessment app described on /privacy is the same entity/site (scope of the notice).

---

## 6. Item 7 — PII in the public NFAI repo (rules)

1. **Test leads only with obviously fake data:** e.g. name `Test Lead W2`, company `Example Co (TEST)`, email `test+w2@example.com` (RFC 2606 reserved domain), city `Testville, TX`, message starting with `TEST — W2 preview, ignore`. Never a real person's or client's data, never team members' personal emails/phones.
2. **Screenshots:** crop to the form/field; redact (solid box, not blur) any email, name, phone, IP, account IDs, tokens, GA measurement/property IDs if not needed; store only under `pilot/evidence/w2/`; check EXIF/metadata is stripped.
3. **Logs:** no worker/Netlify/Resend logs with real submissions in the repo; commit only aggregated counts or synthetic payloads; keys/tokens by name only.
4. **Form-notification IDs** may be cited; contents may not.
5. **If real PII lands in the repo:** (a) stop committing to the path; (b) remove the file in a new commit immediately; (c) notify the Orchestrator and Бадди the same day (what, which commit, since when public); (d) **history rewrite / force-push only with Founder approval** (destructive, affects all agents' clones); (e) if third-party data of a real person — Founder decides on notifying that person / the client; check whether breach-notification laws apply («не проверено»); (f) rotate any exposed secret regardless.
6. Pre-commit self-check: `git diff --cached` scan for `@` (other than example.com), phone patterns, and tokens before every push.

---

## 7. Disclaimer

Agent opinion, not a licensed attorney's legal conclusion. Recommendation only, not an agency sign-off. Citations above were opened and read on 2026-11-23 unless marked «не проверено» / «нет данных». The Founder approves the final text before any production use.
