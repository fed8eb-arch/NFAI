# Brief: Daily checks — who, what, when (PT), what proof
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`; the rows "Оркестратор", "Промпт-инженер", "Профессор", "ГВБ", "Глава клиентского отдела" and "Агентство: волна специалистов"). The plan says: "Цикл `daily-checks.md` (13 шагов) не исполнялся: журнала результатов, golden-set, журнала допусков и реестра доступа не найдено". Base: the registry `/workspace/staff/daily-checks.md` v1.0 (2026-11-17), identical to `_core/staff/daily-checks.md` on `mission-001`. Times: America/Los_Angeles (PT).

## 1. Rule (from the registry, unchanged)
- Every periodic check runs **daily**, in a fixed order. **Step 1 is always the Prompt Engineer check** (Founder, 2026-11-17).
- A daily check is incremental: what changed in the last 24h, plus a small rotating sample.
- A check only finds and reports. Fixes follow the normal path: Prompt Engineer → ГВБ → Orchestrator.
- Result format: one line per check, either `OK` or `issue: what / who / deadline`. Issues go to the Orchestrator; systemic issues also go to the Professor.
- The cycle finishes before the Director's short daily report to the Founder (Mon–Sat, "~20:00 Krasnoyarsk" per the registry).

## 2. Timing (PT)
Krasnoyarsk time is UTC+7, so 20:00 there is 05:00 PST, during US winter time (**to verify** with the Director: is the report still tied to 20:00 Krasnoyarsk?). Proposed daily windows:
| Time PT | What |
|---|---|
| 00:30 | Orchestrator opens the cycle (one message to the owners of steps 1–13) |
| by 01:30 | Step 1 — Prompt Engineer line pushed |
| by 03:30 | Steps 2–13 — each owner's line pushed (in registry order; a step may run in parallel with others, but is not reported before step 1) |
| by 04:15 | Orchestrator's summary pushed |
| ~05:00 | Director's short report to the Founder (Mon–Sat); Sunday: the weekly detailed report, unchanged |
How the cycle is triggered (a scheduled routine, or the Orchestrator's message) is **to verify** with the Orchestrator. Agents do not run on their own clock.

## 3. Who checks what (13 steps; scope = last 24h unless stated)
| # | Owner | What | Daily scope | Note for the rollout period (from the plan) |
|---|---|---|---|---|
| 1 | **Prompt Engineer** | prompts: version and date match the changelog; reporting lines mirror on both sides; no contradictions; header present; golden-set re-run for prompts changed in the last 24h; the Director's brief template matches the Orchestrator's intake fields | changed prompts + 5 rotating unchanged + the template | the golden set does not exist yet (plan: by 2026-11-29); see section 5 |
| 2 | Head of Internal Security | clearance log: every Prompt Engineer action has a logged clearance; graded intelligence (source, date, reliability); **plus the 6 git-rule detections** (`git-rule.md` v1.2 section 6) | entries of the last 24h | the clearance log is not found yet (plan: in the cycle by 2026-11-29) |
| 3 | Head of Internal Security (store owned by DevOps) | access audit of the secret store and the access register | changes + 1 sampled account | register not found (plan); values are never written into the line |
| 4 | Counterintelligence | exposure scan of public materials | new public posts, ads, job posts | the public repo counts as a public material |
| 5 | Professor | training spot-check: 3 roles sampled; error log → lessons; 1 rotating training file + 5 curriculum links; 1 Tier F question | 3 roles/day | plan: daily 24–29.11 |
| 6 | Orchestrator, with the Professor | cross-department error review (blameless, root cause) | `_core/staff/errors-log.md` entries of the last 24h | |
| 7 | DevOps Engineer, with Head of Delivery | last backup succeeded; smoke-restore of 1 file, checksum | last backup + 1 sample | DevOps runs inside the Head of Delivery bot; whether a scheduled backup exists is to verify. The 23.11 machine replacement is the case this step must catch |
| 8 | Head of Delivery, Delivery Support | uptime and incidents; status updates for client-facing incidents are current | last 24h | "no live client service" is a valid `OK (nothing in scope)` |
| 9 | Cost Controller | spend vs yesterday and vs the 7-day average; new recurring cost; unused subscriptions | last 24h | budget is $0 (plan); any new cost is an issue |
| 10 | Billing, Financial Analyst | receivables aging; forecast vs actual on live projects | changes | WireReady is paused; to verify which projects are live |
| 11 | Ads Specialist | CPL vs target; the pause rule; decisions logged | live campaigns | no live campaigns known: `OK (nothing in scope)` |
| 12 | Head of Client Relations, Product Manager | client health; first-reply SLA (4 business hours); backlog priorities | last 24h | working hours and time zone are not approved: report the SLA but promise nothing to clients (plan) |
| 13 | Director, with Business Angel and AI Mentor | strategic decisions of the last 24h get a council read | decisions of the last 24h; skipped when there are none | |

The exceptions table of the registry (monthly or quarterly deep checks) is unchanged. Its line "all 38 training files" is outdated: the corpus has 41 role files and 44 top-level files (`training-corpus-to-git.md`). Correcting the registry is for its owner, the Orchestrator.

## 4. Proof (every step, every day)
- **Line file:** each owner pushes its own file `missions/001-growth-os/daily-checks/<YYYY-MM-DD>/<NN>-<role>.md` (proposed path; to verify with the Orchestrator). One file per owner means no shared file and no conflicts (`git-rule.md` rule 3).
- **Content:** the step number, owner, time PT, scope actually covered, and the result line (`OK` / `issue: what / who / deadline`). Add the commands or sources used and the hashes or paths checked. No secrets, no personal addresses, no values from the secret store.
- **Push:** own clone, own path, plain push, `ls-remote` = HEAD (`git-rule.md` v1.2); commit prefix `<Role>: daily check <date> step <NN>`; identity per `git-identity.md`.
- **Summary:** the Orchestrator pushes `missions/001-growth-os/daily-checks/<YYYY-MM-DD>/summary.md`. It has 13 rows (step, owner, result, hash of the line file) and lists missing steps as `NOT RUN`. The Director's report quotes the summary hash.
- A step that cannot run (no data, or the owner is unavailable) is reported as `NOT RUN: reason`, never left out.

## 5. The Prompt Engineer's first daily check (step 1)
**When:** the first cycle after ГВБ clears this brief. **Output:** `missions/001-growth-os/daily-checks/<date>/01-prompt-engineer.md`.
**(a) Prompts changed in the last 24h.** These are the 9 head app prompts v1.1 on `origin/main` (`_core/staff/app-prompts/*.md`; text `563faab`, Status line `a7e48cc`):
1. Header present, with Version v1.1 and Date 2026-11-23, and matching `_core/staff/prompts-changelog.md` on `origin/main` (entries "2026-11-23 — app-промпты 9 глав v1.0 → v1.1" and "… v1.1: строка Status").
2. Reporting lines mirror: each prompt says "Reports to: the Orchestrator". The other side, `AGENTS.md` ("Оркестратору подчиняются главы …") and `_core/staff/orchestrator.md`, must list that head.
3. Contradictions. Known items to log as issues:
   - the "Commit rule" and "Mission work" lines point to the shared `/workspace/NFAI-mission-001`, which contradicts `git-rule.md` v1.2 (owner: Prompt Engineer; fix: prompts v1.2 through ГВБ);
   - ГВБ's two open notes for v1.2: the branch name in Mission work; Legal's hard-line wording.
4. Golden-set re-run: **no golden set exists**, so log `issue: golden set missing / Prompt Engineer / 2026-11-29 (plan)`.
5. Intro ACK status of the 9 bots (`intro-ack-v1.1.md`): record the result, or `pending`.

**(a) 5 sampled unchanged prompts.** The rotation is alphabetical through the role cards in `_core/staff/`. Day 1: `account-manager.md`, `ads-specialist.md`, `ai-certified-mentor.md`, `architect.md`, `billing.md`. Check the header, the changelog match, mirrored reporting lines, and no contradiction with `git-rule.md` v1.2.
**(b) Brief template.** Compare the Director's brief template (the brief format in `_core/staff/rule-joker.md`: Plan, Task ID, Owner and department, Goal, Context and input paths, Constraints and approval references, Acceptance checks, Deadline, Budget, Output path and report format, Mentor note) with the Orchestrator's intake fields (`_core/staff/orchestrator.md` Inputs: goal, context, constraints, success criteria, deadline, budget, report format). Record the differences, for example that the Task ID, owner and output path have no intake field (to verify).
**Known contradiction to log:** `orchestrator.md` Inputs says "no separate prompt engineer sits between the Director …". That contradicts the current rule that the Prompt Engineer writes all briefs and ГВБ checks them (Founder's order relayed on 2026-11-23). This brief does not edit `orchestrator.md`. The fix goes through the prompt/profile order (`git-rule.md` v1.2 section 10).

## 6. Owners of this brief
| Part | Who |
|---|---|
| Brief text; step 1 | Prompt Engineer |
| Check of the brief; steps 2–3 | ГВБ |
| Runs the cycle; summary; registry text | Orchestrator |
| Steps 4–13 | as in the table in section 3 |
| Reads the summary; acceptance | Director (Бадди) |

## 7. Result / deliverable
From the first cycle after clearance until at least 2026-12-05 (plan), the repo holds every day a folder with 13 line files (or `NOT RUN` rows) and the Orchestrator's summary, all pushed and verified.

## 8. Deadline (PT)
The Director cancelled the writing deadlines for these briefs on 2026-11-23. Execution: the first cycle runs after ГВБ clears this brief. The plan has the daily cycle running 24–29.11, with the golden set and the clearance log in the cycle by 2026-11-29.

## 9. Acceptance criterion
1. Every day: a summary with 13 rows, step 1 first, each row with a result and the hash of its line file.
2. Every `issue` has an owner and a deadline, and appears in the next day's summary until it is closed.
3. No secret or personal data in any line file (ГВБ spot-check in step 2).
4. The Director's daily report cites the summary hash.

## 10. Required proof
The path of each line file and summary, with the commit hash = output of `git ls-remote origin refs/heads/mission-001`.
**"Done" only with proof.** A local commit without push does not count.

## 11. Escalation
- A step not run by its window → the Orchestrator asks the owner once, then records `NOT RUN` in the summary.
- An issue that blocks clients, money or security → the Orchestrator and the Director at once, without waiting for the summary.
- Systemic issues → the Professor (error flag path).
- The Founder is reached only through the Director.

## 12. To verify / conflicts
- The PT time of the Director's daily report (05:00 PT = 20:00 Krasnoyarsk in winter).
- How the cycle is triggered: a routine or a message.
- The repo path for the daily files.
- Whether a scheduled backup exists (step 7).
- Which projects are live (steps 10–12).
- Conflicts: the registry's "38 training files"; `orchestrator.md` "no separate prompt engineer"; the commit and workspace lines of the 9 prompts vs `git-rule.md` v1.2.
