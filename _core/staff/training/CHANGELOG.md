# Training Curriculum — Changelog
Owner: Professor. Rule: every curriculum change gets a version, a date, what changed, and why.

## v1.0 — 2026-11-17
**Why:** the Founder (Peter) ordered training for the whole agency under the mentor-council methodology, with no topic limits within each role's mission and explicit cross-disciplinary learning.

**Added**
- `curriculum.md`: Module 0 Core (C1–C8: first principles, error reviews, testing on data, customer value, cost and cash discipline, speed under uncertainty, small elite team and automation, agency operating rules); Module M Multimodal (M1–M6); Module AI (LLM and agent work for every role); 14 specialty tracks (T-LEAD, T-START, T-PROD, T-ENG, T-DES, T-CLI, T-FIN, T-MKT, T-SEC, T-INT, T-LEG, T-HR, T-EDU, T-CAP); 14 cross-disciplinary modules (X1–X14); role → modules map; source list.
- `director.md`: course completion notes for the Director (Buddy): lenses, cadence, decision checklist, health metrics, cases.
- 38 role training files (`<slug>.md`, same slug as the prompt file), each with core applied, specialty principles, 2–3 X modules, a checklist, 2 practice cases, and sources.

**Link check (2026-11-17)**
- All links are HTTP 200 except three marked *[bot-blocked, open manually]*: Columbia Heilbrunn Center, OHCHR Berkeley Protocol, RBC Tinkov profile.
- Replaced: HBS MBA case-method page (404) → HBS teaching case-method page; datajournalism.com Verification Handbook 3 (404) → verificationhandbook.com.
- Dropped: FTC advertising guidance (404), Facebook Business Learn (400), Zendesk Help (403, not essential).
- Raw check results are in `_linkcheck/`.

**Next review:** 2026-12-17. The Professor samples work against the checklists, updates cases from the error log, and re-runs the link check.

## v1.1 — 2026-11-17
**Why:** the Founder (Peter) asked to add a technologically trained member to the Mentor Council and to formalize how the Director turns council opinions into briefs for the Orchestrator.

**Added**
- `ai-certified-mentor.md`: study plan for the AI Mentor built on five public program curricula (Anthropic Claude Certified Architect – Foundations, GitHub Foundations, Google AI Essentials, AWS Certified AI Practitioner, IBM Generative AI Engineering Professional Certificate): 9 modules, practice tasks, self-checks, and official URLs.

**Changed**
- `director.md` (notes v1.1): sections 8–9: council → decision → brief workflow, unified brief template, reporting cadence (daily Mon–Sat ~20:00, weekly Sunday ~19:00 Krasnoyarsk).

**Link check (2026-11-17):** all five program pages HTTP 200 (Google's skills.google.com path returned 403 to bots and was not used). Prices and domain weights come from the official pages; third-party figures are marked unverified in the file.

**Next review:** 2026-12-17.

## v2.0 — 2026-11-17
**Why:** the Founder (Peter) ordered (1) all checks, reviews, and audits to run daily with the Prompt Engineer first, and (2) the training to move from basic to fundamental level with business programs of Harvard, Yale, and British schools.

**Added**
- `curriculum.md` v2.0: **Tier F — Business & Management Fundamentals**: 11 modules (F1 Strategy, F2 Corporate finance, F3 Accounting, F4 Economics, F5 Negotiation, F6 Leadership and organizations, F7 Operations, F8 Marketing, F9 Entrepreneurship and innovation, F10 Data and decision-making, F11 Ethics and governance), each with verified source URLs, a classic reading list, agency case tasks, and a self-check; school table (HBS and Harvard wider, Yale SOM and Open Yale Courses, Oxford Saïd, Cambridge Judge, LBS, LSE, plus INSEAD, Wharton, Stanford GSB, MIT OCW, IMD); role → modules map; honest research finding on "closed" UK schools. v1.0 content is kept unchanged as the foundation (backup of v1.0: `_linkcheck/curriculum-v1.0.bak.md`).
- Wording rule: agents are "trained on public curricula and open materials of" these schools; no degrees or diplomas are held or claimed.
- A **Tier F pointer** (required modules, plus daily check duty where the role has one) appended to all 40 role training files, with their headers moved to Curriculum v2.0.
- `/workspace/staff/daily-checks.md` v1.0: the registry of daily checks and their fixed order (Prompt Engineer first).

**Changed (cadence moved to daily)**
- `curriculum.md`: Professor samples work daily (was monthly); full link/file re-validation stays monthly.
- `director.md` (notes v1.2): daily error review, strategic decision review, training-gap check, prompt version audit; new section 10 (fundamentals tier).
- Checklists: product-manager (backlog), ads-specialist (error review), financial-analyst (forecast vs actual), cost-controller (cost check), billing (aging), client-head (health score), counterintelligence (footprint scan), internal-security-head (access register, playbook readiness), devops-engineer and delivery-head (restore smoke test daily), architect, prompt-engineer, professor, market-competitor-researcher, intelligence-head-vatican.
- Exceptions kept deep-and-rare with a daily lightweight check: full backup restore test (monthly), incident-response drill (quarterly), full link and file re-validation (monthly). Spaced-review intervals of lessons are learning intervals, not checks, and stay unchanged. Reports (weekly cost report, monthly financial pack, quarterly letter and client business review, the Founder's daily and weekly reports) are not checks and stay unchanged.

**Link check (2026-11-17):** about 100 URLs checked. All Tier F URLs returned HTTP 200 except Oxford Saïd pages (403 to the bot, confirmed live via web search, marked [bot-blocked]) and INSEAD's own site (403, not used). Replaced after 404: several MIT OCW slugs, HBS required-curriculum page, Yale SOM integrated-core page; dropped MIT 15.812 archive (404). Raw results: `_linkcheck/results_v2.txt`, `_linkcheck/results_v2b.txt`; final re-check of all 75 Tier F URLs: `_linkcheck/results_v2_final.txt` (72 × 200, 3 Oxford × 403).

**Next review:** daily from 2026-11-18 (Professor, step 5 of the daily cycle); full re-validation monthly (next 2026-12-17).

## 2026-11-17 — обучение по программе v2.0 (приказ основателя: «Пусть обучится по 2.0 все»)
- Во все 40 файлов обучения (39 ролей + director.md) добавлен раздел «## Усвоено по программе v2.0 (2026-11-17)»: конспект на английском по обязательным модулям роли (Core/M/AI, треки, нужные модули Tier F), 3 контрольных вопроса с эталонными ответами по роли, строка статуса «trained on curriculum v2.0 public materials; no diplomas claimed».
- Полный F1–F11: director, orchestrator, business-angel, ai-certified-mentor и 9 глав отделов (13 файлов). У ai-certified-mentor дополнительно сжаты его модули M1–M9. У остальных 27 ролей — только их модули Tier F по таблице curriculum.md.
- Источники — только curriculum.md v2.0 и общеизвестные фреймворки; цифр и цитат не добавлялось; дипломы не заявляются.
- Пропущенных ролей нет. Это обучение на открытых материалах (конспект в файле), а не подтверждённая проверка навыков: проверку по живым задачам делает Профессор в ежедневном цикле.
- Резервные копии изменённых файлов: /workspace/v2build/backup/.

## 2026-11-17 — director.md v1.3: модуль «Управление командой в бизнес-процессах» (приказ основателя, t316u; правило t317u)
- `director.md` (notes v1.2 → v1.3): новый раздел 11: роль Директора (что/зачем/когда), постоянное правило Основателя «сначала справка Совета менторов, потом исполнение» + шаблон справки (11.1а), делегирование через бриф, RACI, управление по отклонениям и пороги эскалации, постоянные одобрения, стоп/HOLD с границами, проверка памяти, дисциплина доставки, разбор 6 ошибок дня, чек-лист из 10 пунктов, самопроверка. Основа: делегирование, RACI, management by exception, OKR/бриф, High Output Management (Andy Grove); без цитат и цифр.
- Бэкап предыдущей версии: `/workspace/staff/training/_backup/director.v1.2.md`.
- Предложение правила (не применено): `/workspace/pilot/proposals/standing-approvals.md` v0.1 (п. 26–29 для rules.md); решение за Директором.
- Системные промпты и роль-файлы не менялись.

## 2026-11-17 — director.md v1.4: раздел 12 «Прибыль и бонусы» (приказ основателя, t337u)
- `director.md` (notes v1.3 → v1.4): новый раздел 12: что такое прибыль (выручка − затраты, валовая и чистая, маржа), ради чего она добывается (выживание, реинвестирование, рост, отдача владельцу, миссия), стартап с нулевой выручкой (бесплатные ресурсы как реальная экономия), правила (не отказываться от бесплатного и не отзывать без справки Совета; всегда искать бонусы при регистрации; вопрос «повышает ли это прибыль или снижает затраты?»), чек-лист из 5 пунктов, самопроверка. Основа: общие темы курсов финансов и управленческой экономики (Harvard/Yale/LBS) только в общем виде; цитат и выдуманных цифр нет.
- Справка Совета: `/workspace/pilot/mentor-notes/2026-11-17-bonuses-profit.md` (процесс поиска бонусов, чек-лист, программы со ссылками, UNVERIFIED помечены).
- Бэкап предыдущей версии: `/workspace/staff/training/_backup/director.v1.3.md`.
- Системные промпты и роль-файлы не менялись.

## 2026-11-23 — orchestrator.md and devops-engineer.md file v2.1 (error analysis follow-up)
- **Files:** `orchestrator.md` and `devops-engineer.md` (Curriculum v2.0, file version bumped to v2.1).
- **What changed:** added a delivery gate (work is delivered only when, if a push is required, it has been pushed and the hash is verified with `git ls-remote`, and the result has reached the requester) and an environment probe before the first command (`command -v python3 python`, OS/shell, cwd/branch). Each rule has one measurable test (scenario + pass criterion). Checklist items added; existing text kept.
- **Why:** Professor error analysis `/workspace/staff/training/error-analysis-2026-11-23.md`, recurring groups T2 (delivery treated as done before the requester has the result, including a local ACCEPT left unpushed) and T4 (environment or shell assumed, not probed: missing `python` used twice; later a host shell dropped an empty argument). Orchestrator-approved training follow-up (first pass: orchestrator and devops only). A same-day plan change then added `director.md` v1.6 and new `codex-joker.md` v1.0 (see the entries below). Role prompts were not edited.

## 2026-11-23 — director.md notes v1.6 (assignment/brief rules + delivery/proof/env-probe; labelling corrected in v1.7)
- **File:** `director.md` (notes v1.5 → v1.6). Nothing deleted; section 14 appended.
- **What changed:** two rules, each with a measurable test: (1) the Director only assigns tasks and accepts work (never executes, including via own helpers); (2) all prompts and task briefs for agents are written by the Prompt Engineer. These were first written as “Founder rules dated 2026-11-23”; that labelling is corrected in notes v1.7 — they are paraphrases relayed by the Director, not a verbatim Founder record. Sources: (1) `/workspace/NFAI-mission-001/errors-log.md` line 2 (2026-11-23 16:48 PT, «далее только распределение и приёмка»); (2) relayed by Бадди to the Prompt Engineer on 23.11, secondary reference `/workspace/pilot/status.md` lines 184 and 198. No primary record of the Founder’s words for these two rules was found in `/workspace`. Also added Director-relevant items from the error analysis: delivery gate (push if required, hash verified with `git ls-remote`, result reaches the Founder), “done” only with proof, and environment probe before the first command — each with a test.
- **Why:** Orchestrator plan change after the error analysis `/workspace/staff/training/error-analysis-2026-11-23.md`, groups T3 (role boundary; U16 recurrence), and T1/T2/T4. For review by the Prompt Engineer and Internal Security; role prompts were not edited.

## 2026-11-23 — codex-joker.md v1.0 (new training file for Джокер / Codex)
- **File:** `codex-joker.md` created (Curriculum v2.0, file v1.0, 2026-11-23). No prior training file existed for this role under `/workspace/staff/training/`.
- **What changed:** three rules from the error analysis, each with a measurable test: environment probe before the first command; delivery gate (push if required, hash verified with `git ls-remote`, result reaches the requester); “done” only with proof. Checklist included. No prompt text and no secrets.
- **Why:** Orchestrator plan change; error analysis groups T4 (U12), T2, and T1. For review by the Prompt Engineer and Internal Security; the Joker/Codex role prompt was not edited.

## 2026-11-23 — Prompt Engineer review fixes: director.md v1.7, orchestrator.md v2.2, devops-engineer.md v2.2, codex-joker.md v1.1
- **Why:** Prompt Engineer review of the five training files on 2026-11-23 (hashes matched the submitted set; verdict not clean OK). Role prompts were not edited. `curriculum.md` was not updated. This pass covers error-analysis types T1–T4; T6 is not covered. A T5/U13a case was added only in `orchestrator.md` (supported by `/workspace/staff/errors-log.md` line 25).
- **director.md (notes v1.6 → v1.7):** §14.1 and §14.2 are no longer labelled verbatim “Founder rule”; both are marked “paraphrase, relayed by Director,” with the sources above. §14.2 now states that it supersedes §8.4, §11.1 / 11.1a / 11.2, and the brief-writing lines in `AGENTS.md` and `rule-joker.md` (cited by path and line; those files were not edited): the Director sets goal, constraints, deadline, and acceptance criterion; the Prompt Engineer writes the brief/prompt text. Header line 2 now includes section 13 (added v1.5) in the version history. The §14.1 test no longer says the Director “writes assignments”: the Director sets parameters, requests the brief from the Prompt Engineer, then assigns and accepts. Nothing deleted.
- **director.md v1.5 backup status:** the exact pre-edit notes v1.5 text was **not recovered**. Searched `git log --all -- '*director.md'` in `/workspace/NFAI` and `/workspace/NFAI-mission-001` (no matches), `/workspace/staff/training/_backup/` (v1.2, v1.3, v1.4 only), `/workspace/v2build/backup/train-director.md` (v1.2), and editor/tool snapshot paths; no byte-exact v1.5 file was found. No `director.v1.5.md` was fabricated. Current notes v1.6 (before this v1.7 edit) was saved as `/workspace/staff/training/_backup/director.v1.6.md`.
- **orchestrator.md (file v2.1 → v2.2):** added the empty-shell-arguments sentence to the environment-probe rule, same wording as devops/joker: “Check how the host shell treats empty arguments before passing them.” Added measurable test 3 for T5/U13a (“No credit card required” is not a card request), citing `errors-log.md` line 25.
- **devops-engineer.md (file v2.1 → v2.2):** extended environment-probe test 2 with Scenario B, where the host shell drops an empty argument, plus a pass/fail criterion.
- **codex-joker.md (file v1.0 → v1.1):** Sources path is `/workspace/staff/training/error-analysis-2026-11-23.md` only. Role-focus line no longer says “technical work with the Director”; it cites `codex-joker.md` line 7 and `rule-joker.md` lines 7–8: Joker reports to the Vatican Intelligence Head, who reports to the Head of Internal Security; the Director (Бадди) sets tasks and accepts. Environment-probe test gained an empty-argument case. **Note:** Joker (Codex / Джокер) is absent from `/workspace/staff/training/curriculum.md` v2.0 (role → modules map and elsewhere) and from `/workspace/staff/full-roster.md`; those files were not updated in this pass.

## 2026-11-23 — director.md v1.7 → v1.7.1 (Orchestrator decision, option a)
- **What changed:** §14.2 heading now reads "(paraphrase, relayed by Director; primary source pending)"; header version line updated. No other text changed; nothing deleted. Backup of v1.7: `_backup/director.v1.7.md`.
- **Why:** Orchestrator decision 2026-11-23 ~17:19 PT: keep files as accepted by the Prompt Engineer; §14.1 has a primary record (`/workspace/NFAI-mission-001/errors-log.md` line 2); §14.2 has only a relayed/secondary source, so it is marked pending until the Director supplies a primary record. If none is supplied and the Director rules it cannot stay, §14.2 moves to an "awaiting primary source" block in a later version.

## 2026-11-23 — director.md v1.7.1 → v1.7.2 (Internal Security review)
- **What changed:** lines 190 and 208 (§13 error review): the Founder's personal sign-in address and its local part were replaced with "адрес ChatGPT Основателя на домене агентства [скрыт]" / "адрес ChatGPT Основателя [скрыт]"; header lines 2–3 updated to v1.7.2. Nothing else changed; nothing deleted. Backup of v1.7.1: `_backup/director.v1.7.1.md` (local only, not for the public repo).
- **Why:** Internal Security review 2026-11-23: personal data must not go into the public repository (blocker). Non-blocking IS note on §14.2 wording ("supersedes" vs rules.md) is recorded for the next revision.

## 2026-11-23 — director.md v1.7.2 → v1.7.3 (§14.2 source label)
- **What changed:** §14.2 heading: "primary source pending" replaced with the Founder chat message to Бадди (2026-11-23 ~16:55 PT, verbatim quote) and the 2026-11-17 call on the PE role (relayed by Director); the quote was supplied by the Director via the Orchestrator and not independently verified by the Professor. The §14.2 source bullet updated to match. Rule meaning unchanged; header lines 2–3 updated. Backup: `_backup/director.v1.7.2.md` (local only).
- **Why:** Orchestrator message 2026-11-23 ~17:22 PT relaying the Director's primary source.
