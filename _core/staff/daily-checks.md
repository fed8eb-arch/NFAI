# Daily Checks Registry (Ежедневные проверки)
Version: v1.0 | Date: 2026-11-17 | Status: new, by order of the Founder (Peter, 2026-11-17: «Все проверки проводи ежедневно и промт инженер в первую очередь»)
Owner: Orchestrator (runs the cycle) | Reads: Director (Buddy)

## Rule
- Every periodic check, review, or audit runs DAILY. The cycle finishes before the Director's short daily report to the Founder (Mon–Sat ~20:00 Krasnoyarsk; the Sunday weekly detailed report is unchanged).
- **Order is fixed. Step 1 is always the Prompt Engineer check.** The next steps follow the list below.
- **Daily = incremental.** To stay budget-friendly, a daily check covers what changed in the last 24 hours plus a small rotating sample. A deep full pass happens only where the table says so.
- A check only finds and reports. Any fix goes through the normal path (Prompt Engineer changes: Internal Security clearance, then Orchestrator approval).
- Result format: one line per check: OK / issue found (what, who, deadline). Issues go to the Orchestrator; systemic issues also to the Professor's flag path.
- Founder reports are NOT checks and keep their cadence: daily short, weekly detailed (Sunday). Other periodic outputs (weekly cost report, monthly financial pack, quarterly letter and client business review) are reports and keep their cadence; the checks that feed them are daily.

## Order of the daily cycle
| # | Check | Owner | Daily scope | Was |
|---|---|---|---|---|
| 1 | **Prompt Engineer check (FIRST):** (a) agent prompts: version and date match the changelog, reporting lines and handoffs mirror on both sides, no contradictions, header present; golden-set re-run for any prompt changed in the last 24h; (b) the Director's brief template: still matches the Orchestrator's intake fields | Prompt Engineer | all changed prompts + 5 sampled unchanged ones (rotating) + brief template | monthly brief-template review; prompt version audit (monthly) |
| 2 | Clearance log and intelligence report grading: every Prompt Engineer action has a logged clearance; every accepted report has source, date, reliability | Head of Internal Security | entries of the last 24h | continuous / weekly summary |
| 3 | Access audit of the secret store and access register (least privilege, time-boxed access, offboarding done same day) | Head of Internal Security (store owned by DevOps) | changes in the last 24h + 1 sampled account | "periodic" / monthly access review |
| 4 | Exposure scan of public materials (footprint of the agency, clients, stack) | Counterintelligence | new public posts, ads, job posts | monthly footprint scan |
| 5 | Training spot-check: sample of recent work against role checklists; error log → lessons; one rotating role's training file and 5 curriculum links re-checked; one rotating Tier F self-check question put to a sampled role | Professor | 3 roles sampled per day; rotating link sample | monthly sampling; first review was due 2026-12-17 |
| 6 | Cross-department error review (blameless, root cause) | Orchestrator, with the Professor | errors logged in the last 24h | monthly error review; weekly error log review |
| 7 | Backup check: last scheduled backup succeeded; **lightweight restore smoke test** (restore one sampled file or database table, verify checksum) | DevOps Engineer, with Head of Delivery | last backup + 1 sample | monthly restore test |
| 8 | Uptime and incident check; client-facing incident status updates are current (critical daily, others every 2 business days) | Head of Delivery, Delivery Support | last 24h | monthly uptime summary |
| 9 | Cost check: spend vs yesterday and vs 7-day average; any new recurring cost; unused or duplicate subscriptions | Cost Controller | last 24h | weekly (alert at +20% week over week) |
| 10 | Finance checks: receivables aging, forecast vs actual variance on live projects | Billing, Financial Analyst | changes in the last 24h | weekly aging; monthly variance |
| 11 | Marketing checks: ad campaign CPL vs target (pause rule: CPL more than 50% over target after 3 full days or the test budget); campaign decisions logged | Ads Specialist | live campaigns | weekly error review |
| 12 | Client and product checks: client health score, first-reply SLA (4 business hours), backlog priorities | Head of Client Relations, Product Manager | last 24h | weekly |
| 13 | Strategic decision review: any strategic decision taken in the last 24h gets a Business Angel (council) read | Director with Business Angel and AI Mentor | decisions of the last 24h; skipped when none | monthly |

## Exceptions (cannot or should not be fully daily)
| Deep check | Cadence | Why (one line) |
|---|---|---|
| Full backup restore test (whole environment, time-to-restore recorded) | monthly | A full restore costs hours of compute and can load production; the daily smoke test (step 7) catches broken backups in 24h. |
| Incident-response drill (playbook tested end to end) | quarterly | A real drill needs several agents and a simulated incident; the daily check (step 3) confirms the playbook and contacts are current. |
| Full re-validation of all curriculum links and all 38 training files | monthly | A full pass duplicates the daily rotating sample and burns tokens; the daily sample covers every file within about two weeks. |
| Spaced-review intervals of lessons (1 week, 1 month, 1 quarter) | unchanged | These are learning intervals, not checks; shortening them to a day defeats spaced repetition. |
| Quarterly letter to the Founder; quarterly client business review; monthly financial pack | unchanged | These are reports and client meetings, not checks; the daily checks feed them. |
