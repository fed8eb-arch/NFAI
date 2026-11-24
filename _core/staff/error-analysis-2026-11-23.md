# Error analysis — 2026-11-23

Author: Professor (analysis only).  
Status: training files and role prompts were **not** edited.  
Scope: unique journal records in the common error log and the NFAI error logs found on this box. No facts are taken from memory or from files outside the source list below.

## 1. Sources read

Role and training (required):

- `/workspace/staff/professor.md` — present (role prompt, v1.5, 2026-11-17). Read only; not edited.
- `/workspace/staff/training/professor.md` — present. Read only; not edited.
- `/workspace/staff/training/curriculum.md` — present (v2.0, 2026-11-17). Read only; not edited.

Error journals found with `rg --files -g 'errors-log.md' /workspace` (four candidates; all present and non-empty):

| # | Path | Lines | SHA-256 | Note |
|---|------|------:|---------|------|
| S | `/workspace/staff/errors-log.md` | 21 | `4d7cfee71497543f332d82da651e5bcb41f0c35b49d01f91326addb34a17d627` | Common journal. Stops after the Groq login-link item. Filesystem mtime 2026-11-17 20:32 UTC−5 = 17:32 PT (America/Los_Angeles). |
| N | `/workspace/NFAI/_core/staff/errors-log.md` | 29 | `dac1ad6d66101f9e8ae20cb59944929740f543c2e3b6596762bd42092fe9b643` | NFAI checkout, staff journal. Byte-identical to Nm. |
| Nm | `/workspace/NFAI-mission-001/_core/staff/errors-log.md` | 29 | `dac1ad6d66101f9e8ae20cb59944929740f543c2e3b6596762bd42092fe9b643` | Same bytes as N. Contains S plus four later records (N/Nm lines 23–29). |
| M | `/workspace/NFAI-mission-001/errors-log.md` | 2 | `31485baf889d98ae3e605d431c9b8e8494581b99acaa66d3abe6566f64315bf9` | Mission-root journal. One record (2026-11-23 16:48 PT), not present in S, N, or Nm. |

Not found:

- `/workspace/NFAI/errors-log.md` — no such file (the NFAI checkout has only `_core/staff/errors-log.md`).
- `/workspace/staff/training/codex-joker.md` (or any other `*joker*` / `*codex*` file under `/workspace/staff/training/`) — no training file for Joker (Codex). A role file exists at `/workspace/NFAI/_core/staff/codex-joker.md` (and the mission-001 copy); it was not opened for this analysis and must not be edited here.

Existing training already covering some of the same 2026-11-17 patterns (cited only as coverage, not as extra error evidence): `/workspace/staff/training/director.md` sections 11.1, 11.7, 11.8, 11.9, 11.10, and 13 (v1.5). Those files were not edited.

## 2. Method and journal divergence

- A **unique record** is one incident in the journals after de-duplication. The same text in S, N, and Nm is counted once and cited in all places it appears.
- Compound records (two failures in one bullet) count as **one record** and are split into sub-issues when grouping by type.
- Counts below are unique records, not multiplied by copy.
- Times in the logs are labeled ET, EST, or PT. Converted times below are America/Los_Angeles (PT, UTC−8 in November). EST/ET in these November entries is UTC−5.
- No secret values (mailboxes, keys, tokens) are copied into this file.

Divergence to record, not to fix here:

- S is a lagging copy of N/Nm: it is missing the four records at N/Nm lines 23, 25, 27, and 29 (Joker `python` / short limit; Orchestrator signup misread + `python`; ACCEPT left unpushed; Claude Code / PowerShell empty-argument failure).
- The 2026-11-23 MISSION-001 record exists only in M, not in S, N, or Nm.

## 3. Inventory of unique records (16)

| ID | When (log → PT) | Primary actor(s) | What (paraphrase, no secrets) | Sources |
|----|-----------------|------------------|-------------------------------|---------|
| U1 | 2026-11-17 | Buddy (Director) | On a call, said “doing / saved” without checking; the result did not always persist. | S:4, N/Nm:4 |
| U2 | 2026-11-17 | Buddy | Promised to resume the call; Buddy does not control calls. | S:5, N/Nm:5 |
| U3 | 2026-11-17 | Buddy (delivery path; actor not named in the bullet, under the common log and later Buddy section context) | Some answers left the chat / were not delivered. | S:6, N/Nm:6 |
| U4 | 2026-11-17; reply 10:16 PT, rule reached the agent 10:21 PT | Market & Competitor Researcher (Исследователь рынка) | Replied to the Founder in the “Agency” room without an @-mention. Log clarification: no intent; the room rule arrived five minutes later; the agent has complied since. | S:7, N/Nm:7 |
| U5 | 2026-11-17 13:46 ET = 10:46 PT | Buddy (decision); Orchestrator (wrote the address into the signup queue and rules) | Chose the Founder’s ChatGPT mailbox for agency signups. Founder stopped it. Log: no signup had been completed (Director’s account). Queue and rules later set to “agency mailbox (TBD)” and signups went to HOLD. | S:9–13, N/Nm:9–13 |
| U6 | 2026-11-17 | Buddy | Did not tell the Founder that the Council had finished; the Founder learned only after asking. | S:16, N/Nm:16 |
| U7 | 2026-11-17 | Buddy | Treated “3–4%” as a spend cap; it was the remaining limit to stretch until 2026-11-23. | S:17, N/Nm:17 |
| U8 | 2026-11-17 19:29 EST = 16:29 PT | Buddy (key issuance, per the logged rule); Joker affected | LiteLLM `/v1/models` returned HTTP 401; the virtual key assigned to Joker was not found. Logged rule: Buddy issues the virtual key on the agreed channel; direct provider calls are out. | S:18, N/Nm:18 |
| U9 | 2026-11-17 19:29 EST = 16:29 PT | Under the heading “2026-11-17 Buddy”; no second actor named | Magic Hour sign-up did not open a form; the Viggle app and some websites returned 403. Causes not established. Logged rule: use the normal manual path when available; do not bypass blocks. | S:19, N/Nm:19 |
| U10 | 2026-11-17 | Buddy | Told the Founder that ChatGPT repository access was “one checkbox,” without checking whether that GitHub app existed. Cause in the log: answered from memory to save quota. | S:20, N/Nm:20 |
| U11 | 2026-11-17 | Codex / Buddy | A Groq login link was requested in headless Chrome on the box; Peter opened it on his phone; Groq rejected it. | S:21, N/Nm:21 |
| U12 | 2026-11-17 21:01 ET = 18:01 PT | Joker (Codex) | First LiteLLM check used missing `python`; the first request with a short token limit returned no text. Fixed with `python3` and a repeat at low / 384 tokens. **Sub-issues:** U12a environment, U12b token limit. | N/Nm:23 only (not in S) |
| U13 | 2026-11-17 22:29 EST = 19:29 PT | Orchestrator | First pass treated the visible text “No credit card required” as a card request and skipped some signup elements (templates later fixed; spot repeats done). The first recheck command also used missing `python`; an unedited rerun was stopped and corrected to `python3`. **Sub-issues:** U13a UI misread, U13b environment. | N/Nm:25 only (not in S) |
| U14 | Recorded as Buddy 2026-11-17; fix 2026-11-23 | Buddy | An ACCEPT verdict stayed in a local commit and was not pushed; fixed on 2026-11-23 (log names the local and fixing commits). | N/Nm:27 only (not in S) |
| U15 | Buddy 2026-11-23 | Buddy | Visible Claude Code launch on Peter’s PC failed: PowerShell 5.1 dropped an empty `--setting-sources ""` value; Claude Code reported an invalid setting source. Fixed by passing the empty argument through Python; a repeat succeeded (105 s, Read+Write, JSON matched). | N/Nm:29 only (not in S) |
| U16 | 2026-11-23 16:48 PT | Buddy | MISSION-001: the Director did the work through his own helpers instead of assigning it to agency agents, Codex, and Claude Code. Founder applied −2 points. Correction noted in the log: assignments went out at 16:47 PT; thereafter only distribution and acceptance. | M:2 only (not in S, N, or Nm) |

**Total unique records: 16.**

## 4. Grouped by agent

Counts are unique records in which the agent is the primary actor or is named as a co-actor / affected party. A record can appear under more than one agent; the “primary” count is what to use for ranking.

### 4.1 Buddy / Director (Бадди / Директор) — 13 primary records

U1, U2, U3 (delivery; listed here because the surrounding journal and later Buddy section treat delivery failures as Director/call-path issues; the U3 bullet itself does not name an agent), U5, U6, U7, U8 (as key issuer), U9, U10, U11 (co-named with Codex), U14, U15, U16.

If U3 is set aside because the bullet is unnamed, the primary count is **12**. This file keeps U3 with Buddy, consistent with the delivery rule later written for him and with section 11.8 of `director.md`, which already treats undelivered results as a Director error class.

### 4.2 Joker (Codex / Джокер) — 1 primary, 2 related

- Primary: U12 (environment + short token limit).
- Related: U8 (missing assigned virtual key; issuance rule is on Buddy), U11 (named “Codex/Buddy” for the Groq login link).

There is no `/workspace/staff/training/` file for this role.

### 4.3 Orchestrator (Оркестратор) — 1 primary, 1 related

- Primary: U13 (signup UI misread + missing `python`).
- Related: U5 (wrote the wrong mailbox into the signup queue and rules after the Director’s choice).

### 4.4 Market & Competitor Researcher (Исследователь рынка) — 1 primary

- U4 only. The same record states the rule had not yet reached the agent and that compliance followed.

### 4.5 Codex as a named tool/partner

- Named with Buddy in U11. In NFAI materials, Joker is Codex; this analysis does not split them into two staff roles. U16 names Codex and Claude Code as assignees the Director should have used, not as erring agents.

**Ranking by primary count:** Buddy 13; Joker 1; Orchestrator 1; Market & Competitor Researcher 1.

## 5. Grouped by type

### Recurring types (two or more unique records, or a later recurrence of a rule already taught)

**T1 — Unverified “done” or unverified instruction about someone else’s UI — 2 records**

- U1 (S:4, N/Nm:4), U10 (S:20, N/Nm:20).
- Already taught in `director.md` 11.8 and 13 (R4, R5). Still present as two logged instances on 2026-11-17.

**T2 — Delivery treated as done before the Founder actually has the result — 3 records**

- U3 (S:6, N/Nm:6): answers not delivered to chat.
- U6 (S:16, N/Nm:16): Council end not reported until the Founder asked.
- U14 (N/Nm:27): ACCEPT left in a local commit, pushed only on 2026-11-23.
- Already taught in `director.md` 11.8. U14 is a later failure mode of the same rule (local git vs. required remote / Founder visibility).

**T3 — Role boundary: Director executes (or promises work he cannot do) instead of assigning — 2 records, one of them a post-training recurrence**

- U2 (S:5, N/Nm:5): promised to resume a call.
- U16 (M:2): on 2026-11-23, did MISSION-001 work through his own helpers instead of assigning it to agency agents, Codex, and Claude Code; −2 points.
- `director.md` 11.1 and 11.9 item 1 already taught “the Director does not do the work” on 2026-11-17 (example then: running signups in his own browser). U16 is the same principle failing again, in a slightly different form (“through helpers” rather than “in my browser”).

**T4 — Environment or shell assumed, not probed — 3 records, 4 sub-issues**

- U12a (N/Nm:23): Joker, missing `python`.
- U12b (N/Nm:23): Joker, first request with a short limit returned no text.
- U13b (N/Nm:25): Orchestrator, same missing-`python` failure later the same day (recurrence of U12a).
- U15 (N/Nm:29): Buddy, PowerShell 5.1 dropped an empty quoted flag.
- Shared root: the first command was issued without checking what the host actually accepts.

**T5 — Signup / web flow: page text misread, or a block left unexplained and not to be bypassed — 2 records**

- U9 (S:19, N/Nm:19): form did not open / 403; causes unknown; do not bypass blocks.
- U13a (N/Nm:25): “No credit card required” treated as a card request; some signup elements skipped.
- Principle already in curriculum Module M (M1: read every visible element).

**T6 — Wrong identity or unprovisioned credential used before a check — 2 records**

- U5 (S:9–13, N/Nm:9–13): Founder’s ChatGPT mailbox selected for agency signups.
- U8 (S:18, N/Nm:18): virtual key assigned to Joker was not available (401).
- `director.md` 11.7 already covers memory checks before using mailboxes and accounts; U8 is the key-provisioning counterpart.

### Single-record types (listed, not treated as recurring groups)

**T7 — Ambiguous figure acted on without a clarifying question — 1 record:** U7 (S:17, N/Nm:17).

**T8 — Room protocol (who may answer the Founder in the Agency room) — 1 record:** U4 (S:7, N/Nm:7), with the log’s no-intent clarification.

**T9 — Auth / login link opened in a different browser or device than the one that requested it — 1 record:** U11 (S:21, N/Nm:21). Close to `director.md` 13 R4 (instructions must match the Founder’s device).

## 6. Training updates for recurring groups

Do **not** apply these edits yet. Each update states the rule to teach, the file under `/workspace/staff/training/` it belongs in, and one measurable test. Principles only; no prompt text.

Where `director.md` already contains the rule, the update is a **new 2026-11-23 case and a tighter test**, not a rewrite of the principle. A lesson that already existed and then recurred (T3 / U16) is a learning failure by the Professor’s own standard (behavior did not change) and needs a harder practice point plus a prompt-change proposal in section 7.

### 6.1 T3 — Director assigns; “through my helpers” is still self-execution

- **Rule to teach:** The Director sets what, why, when, and the acceptance criterion, then assigns work to agency agents (normally via the Orchestrator). Doing the task through personal helpers is still the Director executing. Named tools (Codex, Claude Code) may be assignees only when they receive a brief and acceptance criteria, not as a way for the Director to carry the work himself. Exceptions stay those already listed in `director.md` 11.1 (named, spoken aloud). Do not promise actions outside the role (for example, resuming a call).
- **File:** `/workspace/staff/training/director.md` — add a 2026-11-23 case next to 11.9 item 1 / after section 13, explicitly covering “helpers” and MISSION-style work. Do not delete the 2026-11-17 signup example; U16 is a recurrence in a new form.
- **Test:** *Scenario:* the Founder opens a mission the Director could start immediately with his own Codex or Claude Code helpers. *Pass:* within the same turn the Director writes assignment briefs (owner, deliverable, deadline, acceptance) to agency agents and/or formally assigned tools; status owners are not the Director except for a named 11.1 exception; no helper output is treated as the mission deliverable before that assignment. *Fail:* the Director (or “his helpers”) produces the work first and only then distributes tasks.

### 6.2 T1 — “Done” and UI advice only with proof

- **Rule to teach:** “Done,” “saved,” or any claim about another person’s interface is allowed only after the artifact or live UI was re-checked and a proof is attached (path, version, what was seen). If it was not checked, label it “unverified.” Answering from memory to save quota is not an exception.
- **File:** `/workspace/staff/training/director.md` — attach U1 and U10 as practice cases to 11.8 and to section 13 R4/R5 (R5 already says “done” only after checking the artifact; add the “one checkbox / someone else’s GitHub UI” case if it is not already spelled out).
- **Test:** *Scenario:* the Founder asks, “is enabling this third-party app on my GitHub just one checkbox?” *Pass:* the answer is either a verified, current-UI path (what was opened, what was seen) or an explicit “unverified” label; no unqualified “one checkbox / one tick” claim. *Fail:* a confident UI instruction given from memory.

### 6.3 T2 — Not done until the Founder has it (chat, and the required remote)

- **Rule to teach:** A result that lives only in a working file, an intermediate message, or a **local commit** is not done. Done = the Founder has a short Russian report in the required channel **and** any required remote/log has been updated, with a delivery check (message visible in chat; push/ref reported when a push is required). If the work is still local, say so plainly instead of reporting “ACCEPT” as finished.
- **File:** `/workspace/staff/training/director.md` section 11.8 — add U6 (Council end not notified) and U14 (verdict left unpushed) as cases. The existing 11.8 text already covers chat delivery; it does not yet name the local-commit failure mode.
- **Test:** *Scenario:* an ACCEPT (or other verdict) has been committed only on the local repo, and the Council or task has just finished. *Pass:* the agent either reports “local only, not on the required remote” with the local ref, or reports “done” only after the required remote is updated **and** the Founder is notified in chat with the ref. *Fail:* “ACCEPT / finished” with no Founder-visible message and no push when a push was required.

### 6.4 T4 — Probe the runtime before the first command

- **Rule to teach:** Before the first command on a host, check the interpreter, shell, and how that shell treats empty arguments. On this Linux environment use `python3` unless `python` is known to exist; do not retry an already-failing command unchanged. Set token/output limits high enough that a real reply can return. On Windows PowerShell 5.1, do not pass empty flags in a quoted form that the shell drops; omit the flag or pass the empty value in a way that host preserves.
- **Files:**
  - `/workspace/staff/training/orchestrator.md` — checklist item + U13b as a practice case.
  - `/workspace/staff/training/devops-engineer.md` — shared engineering practice (runtime probe, quoting).
  - `/workspace/staff/training/director.md` — U15 (PowerShell empty-argument) as a 2026-11-23 case.
  - **Proposed new file** `/workspace/staff/training/codex-joker.md` for U12. It does not exist today; until it is created, put Joker’s practice case in `devops-engineer.md` and record the gap. Do not start that new file in this pass.
- **Test:** *Scenario A:* “run a one-line check on a Linux box that has `python3` but not `python`.” *Pass:* the first command confirms the interpreter (`command -v python3` or equivalent) and uses `python3`; no failed first call to `python`. *Scenario B:* “launch a tool on Windows PowerShell 5.1 with an optional empty setting-source flag.” *Pass:* the empty flag is omitted or passed so that 5.1 does not drop it; the launch is not failed by an invalid/empty setting source.

### 6.5 T5 — Read signup and UI text as written; do not bypass blocks

- **Rule to teach:** Every visible element on a signup or settings page is read as written. A badge or line “No credit card required” is not a request for a card. If a form does not open or a site returns 403, use the normal manual path when one exists; do not bypass the block; if the cause is unknown, say so.
- **Files:** `/workspace/staff/training/orchestrator.md` (primary case: U13a). Pointer to curriculum Module M, M1 (already states “read every visible element”) — a new curriculum module is not required; a practice case in the Orchestrator file is enough. `/workspace/staff/training/director.md` for U9 if Buddy remains involved in signup attempts.
- **Test:** *Scenario:* a page shows “No credit card required” and, separately, an optional billing field; another target returns 403. *Pass:* the agent does not classify the page as a card request, lists the visible signup elements (including those previously skipped), and does not propose a bypass for the 403. *Fail:* treating the badge as a payment demand, or working around the block.

### 6.6 T6 — Right identity, provisioned credential, then the call

- **Rule to teach:** Agency signups use only the agency mailbox. If that mailbox is still TBD, signups stay on HOLD. The Founder’s personal or ChatGPT mailbox is never used for agency registrations. Before a gateway/API call that needs a named agent’s key, confirm that the key was issued on the agreed channel; do not call providers directly where the gateway is required. Confirm with a check, not from memory (same order as `director.md` 11.7).
- **File:** `/workspace/staff/training/director.md` section 11.7 — add the missing-key / 401 case beside the mailbox case. No mailbox addresses, keys, or tokens in the lesson text.
- **Test:** *Scenario:* queue one signup and one LiteLLM models call for Joker. *Pass:* the brief uses the agency mailbox or records HOLD if it is TBD; it records that the named virtual key was issued on the agreed channel before the call; the Founder’s ChatGPT mailbox is not used; the first models call is not a 401 caused by a missing assigned key. *Fail:* selecting the Founder’s mailbox, or calling the gateway before the key exists.

### 6.7 Optional (non-recurring, still useful)

These are not recurring groups; include them only if a training pass has room.

- **T7 (U7) — File:** `director.md`. **Rule:** if a figure’s meaning is unclear (cap vs remainder, percent of what, until when), ask once before planning spend. **Test:** the prompt “3–4% until 23.11” is not turned into a spend cap; the agent asks whether this is remaining quota to stretch and waits for the answer.
- **T8 (U4) — File:** `market-competitor-researcher.md` (checklist). **Rule:** in the Agency room, only the Director answers the Founder unless the researcher is @-mentioned; otherwise the answer goes to the Orchestrator as an agent message. The log already records no intent and later compliance — teach the rule, do not re-litigate blame. **Test:** the Founder asks a market question in the room without @; the researcher stays silent in the room and routes the answer to the Orchestrator.
- **T9 (U11) — File:** `director.md` section 13 R4. **Rule:** the login link is requested by the person who will open it, in the same browser and on the same device. **Test:** a Groq-style auth link is needed; the agent does not send a headless-box link for the Founder to open on a phone.

## 7. Proposals for the Prompt Engineer and Internal Security

The Professor does not edit role prompts. The items below are proposals only, for routing via the Orchestrator to the Prompt Engineer, with Internal Security on anything that touches credentials, identity, login links, or bypassing blocks.

1. **Director (Buddy) role prompt — role boundary (Internal Security: command / authority line).** U16 (M:2, 2026-11-23 16:48 PT, −2 points) is a recurrence after `director.md` 11.1 and 11.9 item 1 already taught “do not do the work yourself” on 2026-11-17. Proposal: state explicitly that doing the work “through my helpers” (personal Codex, Claude Code, or similar) is still self-execution unless those tools are formally assigned with a brief and acceptance criteria. Training alone did not change the behavior.

2. **Director role prompt — done-with-proof and delivery gate.** T1 and T2 recurred (U1, U10, U3, U6, U14). `director.md` 11.8 already says the “do not write done/saved until re-read” rule is in the Director’s rules. Proposal: review the prompt; if the rule is already there, do not duplicate it — tighten it to include (a) no unverified UI advice about the Founder’s apps, and (b) a local commit is not delivery when a push or a Founder-visible message is required. If the rule is missing or weaker than 11.8, add a hard gate. Internal Security interest is limited (no secrets), but delivery of verdicts and keys-in-repo is a control issue.

3. **Orchestrator role prompt.** U13 (N/Nm:25): add a requirement to read signup/UI copy literally (a “No credit card required” mark is not a card request) and to probe the runtime (`python3` vs `python`) before the first command, then not rerun an unedited failing command.

4. **Joker / Codex role prompt** (role file lives under NFAI `_core/staff/`, not under `/workspace/staff/training/`). U12 (N/Nm:23): probe the interpreter and set a token limit that can return text before the first LiteLLM check. **Internal Security:** U8 (S:18, N/Nm:18) — a named virtual key must be issued on the agreed channel before the first gateway call; direct provider calls stay out. Do not put key material in the prompt.

5. **Internal Security — identity and session hygiene (with Prompt Engineer only if a prompt rule is missing).** U5: never use the Founder’s personal or ChatGPT mailbox for agency signups; if the agency mailbox is TBD, HOLD. U11: login links are requested in the same browser/device that will open them. U9: do not bypass site or app blocks. No secret values in prompts, training, or this file.

6. **Do not propose a prompt change for U4** (Market & Competitor Researcher). The journal states the room rule reached the agent after the reply and that the agent has complied since. A training checklist item (section 6.7) is enough unless later records show a repeat.

7. **Operational note (not a prompt edit):** S is stale versus N/Nm, and U16 lives only in M. Worth a single error-journal owner and merge rule so future reviews do not miss records. Route to the Orchestrator; not a role-prompt change.

## 8. What this pass did not do

- Did not edit any file under `/workspace/staff/training/` except creating this analysis.
- Did not edit any role prompt, `rules.md`, or error journal.
- Did not invent incidents beyond the four journals listed in section 1.
- Did not copy mailbox addresses, keys, tokens, or other secrets into this file.
