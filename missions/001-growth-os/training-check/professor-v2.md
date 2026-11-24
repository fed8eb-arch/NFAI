# Training check v2 — Professor

Date: 2026-11-23  
Author: Professor  
Model: Grok Bot (executor)  
Effort: high  
Curriculum studied: v2.0 (2026-11-17)  
Output rule: new file; existing training-check files were not overwritten.  
Constraints honored: $0 spend; no sign-ups, sending, publishing, or site changes; no secrets or PII (no mailboxes, keys, tokens, or personal addresses); no full third-party materials; no agent prompt contents quoted or revealed.

Mission context (read-only): `missions/001-growth-os/MISSION.md`, `TASKS.md`, and `track-b-growth-os/` (including `pilot/` and `training/`). Pilot client: WireReady, a Dallas data-center electrical contractor; the brand is not yet confirmed by the Founder. Acceptance already written in `TASKS.md:2`: a commit pushed to `mission-001`, hash verified with `git ls-remote`.

---

## 1. Modules studied and one-line takeaways

| Module | Takeaway |
|---|---|
| Specialty: teaching agents | Teach the why, end with retrieval practice, version the curriculum, and never quote a prompt. |
| Checklist (professor.md) | A lesson is complete only if it is tied to a real case, has one checkable practice point, a spaced-review date, and no prompt text. |
| Practice cases | Pattern → a short lesson → one verifiable next action → a systemic flag to the Orchestrator (the Professor does not send the flag as an order). |
| Module 0 (C1–C8) | Rebuild from verifiable facts; change the system after a miss; do not call work done without a quality gate and proof. |
| Module M | Screenshots, logs, and command output are evidence of what was displayed, not proof that delivery happened. |
| Module AI | Give role, goal, context, constraints, and format; verify each step; treat files and logs as data, never as instructions. |
| T-EDU | Testing recall beats rereading; spaced review at growing intervals; measure learning by behavior change, not by lessons delivered. |
| X14 Teaching × Prompting × QA | When the same error appears across agents, flag it to the Orchestrator with examples and dates; prompt edits are not the Professor's to make. |
| X7 AI | Brief another agent with full context, a clear format, and a stated acceptance criterion. |
| X12 Multimodal × Verification | Cite provenance (file, line, commit, time zone); do not claim what the evidence does not show. |
| F6 Leadership | Delegation is owner + deliverable + deadline + criterion; handoffs are where errors live. |
| F9 Entrepreneurship | Run the cheapest test that could kill the riskiest assumption; vanity activity is not learning. |
| F10 Data and decisions | Fix the metric and the decision rule before looking at results; do not overclaim from incomplete evidence. |
| F11 Ethics and governance | Separate who does the work, who approves, and who checks; skin in the game on public, irreversible commits. |
| Role → modules map (professor) | Track T-EDU; X modules X14, X7, X12. Module 0, M, and AI apply to every role. |
| Tier F “Who takes which modules” | Professor takes F6, F9, F10, F11 (not the full F1–F11 set reserved for Director, Orchestrator, Business Angel, AI Mentor, and department heads). |

---

## 2. Dedup method and journal divergence

Sources compared on 2026-11-23 (times below are America/New_York, UTC−5, unless a source itself names another zone):

| Tag | Path | Lines | SHA-256 | Note |
|---|---|---:|---|---|
| S | `/workspace/staff/errors-log.md` | 29 | `dac1ad6d66101f9e8ae20cb59944929740f543c2e3b6596762bd42092fe9b643` | Common journal. |
| N | `/workspace/NFAI/_core/staff/errors-log.md` | 29 | same as S | NFAI checkout. |
| Nm | `/workspace/NFAI-mission-001/_core/staff/errors-log.md` | 29 | same as S | Mission-001 copy of the staff journal. |
| M | `/workspace/NFAI-mission-001/errors-log.md` | 2 | `31485baf889d98ae3e605d431c9b8e8494581b99acaa66d3abe6566f64315bf9` | Mission-root journal. One record, not in S/N/Nm. |
| A | `/workspace/staff/training/error-analysis-2026-11-23.md` | 226 | `a872270b43d9a14a5f0039aa85fd922c1544de6e1ec8d06c7bcde1ad24fef514` | Prior Professor analysis (read as a source, then re-checked against the live logs). |

Dedup rule: a unique record is one incident. Identical text in S, N, and Nm is counted once and cited in every file where it now appears. Compound bullets (two failures in one record) count as one record and are split into sub-issues only when grouping by type. Counts are unique records, not multiplied by copy. No facts are taken from memory beyond these sources plus git log/reflog checks named in §5.

Divergence:

- As of this pass, **S, N, and Nm are byte-identical** (`diff` empty; same SHA-256). `/workspace/NFAI-mission-001/_core/staff/errors-log.md` does **not** differ from `/workspace/NFAI/_core/staff/errors-log.md` or from `/workspace/staff/errors-log.md`.
- Analysis A (written earlier on 2026-11-23) is stale on this point: it described S as a 21-line lagging copy (SHA-256 `4d7cfee7…`) missing N/Nm lines 23, 25, 27, and 29. Those four records are now present in S at the same line numbers. Citations below use the current files.
- U16 still exists only in M (M:2). It has not been merged into S, N, or Nm.
- A copy of analysis A also sits untracked in the shared clone at `/workspace/NFAI-mission-001/_core/staff/error-analysis-2026-11-23.md` (same SHA-256 `a872270b…`). It is not in any commit (see §5). This file does not commit it.

---

## 3. Unique records (16), grouped by agent and type

IDs U1–U16 follow analysis A, re-verified against the current logs. Paraphrase only; no secret values.

| ID | When | Primary actor(s) | What (paraphrase) | Citations |
|---|---|---|---|---|
| U1 | 2026-11-17 | Buddy (Director) | Said “doing / saved” on a call without checking; the result did not always persist. | S:4, N:4, Nm:4 |
| U2 | 2026-11-17 | Buddy | Promised to resume a call; Buddy does not control calls. | S:5, N:5, Nm:5 |
| U3 | 2026-11-17 | Delivery path; bullet unnamed, kept with Buddy as in A | Some answers left the chat / were not delivered. | S:6, N:6, Nm:6 |
| U4 | 2026-11-17; reply 13:16 ET = 13:16 America/New_York; rule reached the agent 13:21 | Market & Competitor Researcher | Replied to the Founder in the “Agency” room without an @-mention. Log: no intent; rule arrived five minutes later; compliance since. | S:7, N:7, Nm:7 |
| U5 | 2026-11-17 13:46 ET = 13:46 America/New_York | Buddy (decision); Orchestrator (wrote the address into the queue and rules) | Chose the Founder’s ChatGPT mailbox for agency signups. Founder stopped it. Log: no signup completed. Queue and rules later set to “agency mailbox (TBD)” and HOLD. | S:9–13, N:9–13, Nm:9–13 |
| U6 | 2026-11-17 | Buddy | Did not tell the Founder that the Council had finished; the Founder learned only after asking. | S:16, N:16, Nm:16 |
| U7 | 2026-11-17 | Buddy | Treated “3–4%” as a spend cap; it was the remaining limit to stretch until 2026-11-23. | S:17, N:17, Nm:17 |
| U8 | 2026-11-17 19:29 EST = 19:29 America/New_York | Buddy (key issuance, per the logged rule); Joker affected | LiteLLM `/v1/models` returned HTTP 401; the virtual key assigned to Joker was not found. | S:18, N:18, Nm:18 |
| U9 | 2026-11-17 19:29 EST = 19:29 America/New_York | Under the “2026-11-17 Buddy” heading; no second actor named | A sign-up form did not open; an app and some sites returned 403. Causes not established. Logged rule: use the normal manual path; do not bypass blocks. | S:19, N:19, Nm:19 |
| U10 | 2026-11-17 | Buddy | Told the Founder that ChatGPT repository access was “one checkbox,” without checking whether that GitHub app existed. Log cause: answered from memory to save quota. | S:20, N:20, Nm:20 |
| U11 | 2026-11-17 | Codex / Buddy | A login link was requested in headless Chrome on the box; Peter opened it on his phone; the provider rejected it. | S:21, N:21, Nm:21 |
| U12 | 2026-11-17 21:01 ET = 21:01 America/New_York | Joker (Codex) | First LiteLLM check used missing `python`; a short token limit returned no text. Fixed with `python3` and a repeat at low / 384 tokens. Sub-issues: U12a environment, U12b token limit. | S:23, N:23, Nm:23 |
| U13 | 2026-11-17 22:29 EST = 22:29 America/New_York | Orchestrator | First pass treated visible text “No credit card required” as a card request and skipped some signup elements. The first recheck also used missing `python`; an unedited rerun was stopped and corrected to `python3`. Sub-issues: U13a UI misread, U13b environment. | S:25, N:25, Nm:25 |
| U14 | Recorded as Buddy 2026-11-17; fix 2026-11-23 | Buddy | An ACCEPT verdict stayed in a local commit and was not pushed; fixed on 2026-11-23 (log names the local and fixing commits). Git confirmation in §5. | S:27, N:27, Nm:27 |
| U15 | 2026-11-23 | Buddy | Visible Claude Code launch on Peter’s PC failed: PowerShell 5.1 dropped an empty flag value. Fixed by passing the empty argument through Python; a repeat succeeded. | S:29, N:29, Nm:29 |
| U16 | 2026-11-23 16:48 PT = 19:48 America/New_York | Buddy | MISSION-001: the Director did the work through his own helpers instead of assigning it to agency agents, Codex, and Claude Code. Founder applied −2 points. Log: assignments went out at 16:47 PT; thereafter only distribution and acceptance. | M:2 only |

**Total unique records: 16.**

### 3.1 By agent (primary count for ranking)

A record can be listed as related under a second agent; the primary count is the ranking figure.

- **Buddy / Director — 13 primary:** U1, U2, U3, U5, U6, U7, U8 (as key issuer), U9, U10, U11 (co-named with Codex), U14, U15, U16. If U3 is set aside because the bullet is unnamed, the primary count is 12. This file keeps U3 with Buddy, consistent with analysis A and with the delivery rule later written for that role.
- **Joker (Codex) — 1 primary, 2 related:** primary U12; related U8 (issuance rule is on Buddy) and U11 (named “Codex/Buddy”).
- **Orchestrator — 1 primary, 1 related:** primary U13; related U5 (wrote the chosen mailbox into the queue and rules).
- **Market & Competitor Researcher — 1 primary:** U4 only (log: no intent; later compliance).

Ranking by primary count: Buddy 13; Joker 1; Orchestrator 1; Market & Competitor Researcher 1.

### 3.2 By type

Recurring types (two or more unique records, or a later recurrence of a rule already taught):

| Type | Count | Records and citations |
|---|---:|---|
| T1 — Unverified “done” or unverified instruction about someone else’s UI | 2 | U1 (S/N/Nm:4), U10 (S/N/Nm:20) |
| T2 — Delivery treated as done before the Founder actually has the result (including a local commit without a required push) | 3 | U3 (S/N/Nm:6), U6 (S/N/Nm:16), U14 (S/N/Nm:27) |
| T3 — Role boundary: Director executes or promises work he cannot do, instead of assigning | 2 | U2 (S/N/Nm:5), U16 (M:2). U16 is a post-training recurrence, and the only journal record explicitly labeled MISSION-001. |
| T4 — Environment or shell assumed, not probed | 3 records / 4 sub-issues | U12a and U12b (S/N/Nm:23), U13b (S/N/Nm:25; same missing-`python` failure later the same day), U15 (S/N/Nm:29) |
| T5 — Signup / web flow: page text misread, or a block left unexplained and not to be bypassed | 2 | U9 (S/N/Nm:19), U13a (S/N/Nm:25) |
| T6 — Wrong identity or unprovisioned credential used before a check | 2 | U5 (S/N/Nm:9–13), U8 (S/N/Nm:18) |

Single-record types:

| Type | Count | Records and citations |
|---|---:|---|
| T7 — Ambiguous figure acted on without a clarifying question | 1 | U7 (S/N/Nm:17) |
| T8 — Room protocol (who may answer the Founder in the Agency room) | 1 | U4 (S/N/Nm:7) |
| T9 — Auth / login link opened on a different browser or device than the one that requested it | 1 | U11 (S/N/Nm:21) |

Tied for most frequent types in the journals: **T2 (3)** and **T4 (3 records, 4 sub-issues)**.

---

## 4. Chosen systemic error for MISSION-001 work

**Choice: T2 in its MISSION-001 form — commit / proof / index hygiene in the shared clone.** Principle: work is not delivered until the required remote contains a commit of *only* your paths and the hash has been checked with `git ls-remote` (or a descendant check). A staged file, an untracked file, or a local-only commit is not delivery.

Why this, and not another type:

- In the journals overall, T2 and T4 are tied at 3 records. T4 (probe the runtime) matters, but it is not the live MISSION-001 failure class.
- The only journal record *explicitly labeled* MISSION-001 is U16 (T3, M:2, 2026-11-23 16:48 PT = 19:48 America/New_York). That is a real, already-flagged role-boundary recurrence. It is not the most frequent MISSION-001 *operational* error across agents, and Director-training edits are already on a separate review path.
- U14 (T2, S/N/Nm:27) is the logged precursor of the same delivery-proof failure: an ACCEPT verdict dated 2026-11-17 stayed in a local commit and was pushed only on 2026-11-23. It is not itself labeled MISSION-001, but it is the same principle.
- Official MISSION-001 acceptance already requires a pushed commit and an `ls-remote` check (`TASKS.md:2`). On 2026-11-23 the Prompt Engineer recorded a shared-clone commit rule in `origin/main` `56ff980` (20:03:42 America/New_York). The rule exists because this keeps happening.
- Today’s live case in this shared clone is the index/worktree form of T2 (details and the honesty limit in §5).

---

## 5. What git log and reflog can prove (today’s shared-clone case)

Checked in `/workspace/NFAI-mission-001` on branch `mission-001`. Only git log, reflog, and object queries were used for claims in this section. Index `add`/`restore --staged` events are not recorded in reflog, so some steps **cannot** be proven from those two sources.

**Proven:**

1. `_core/staff/error-analysis-2026-11-23.md` is present in the worktree, SHA-256 `a872270b43d9a14a5f0039aa85fd922c1544de6e1ec8d06c7bcde1ad24fef514` (byte-identical to analysis A). `git log --all --full-history --` on that path (and on `**/error-analysis*`) is empty: the file has never been in any commit on this clone. `git status` lists it as untracked (`??`).
2. Reflog records, at **2026-11-23 19:57:59 America/New_York**, `reset: moving to HEAD` while HEAD was `f70598c` (`HR-1: bot id/status/date column in roster and launch plan`, 19:56:38). A default mixed `git reset` to HEAD does not move HEAD and clears the index. That is a mechanism that would unstage any previously staged paths. The same second, reflog then records the commit `f6e4cc3` (`training-check: finance-head`). Reflog does not name which agent ran the reset.
3. `bb68779` (`HR-1b: Telegram Parser is a role inside Market Researcher bot`, 2026-11-23 20:00:24 America/New_York) changes only `_core/staff/full-roster.md` and does not contain the analysis file. Later commits on `mission-001` also do not contain it. `git stash list` was empty at the time of this check.
4. U14, independently of the analysis file: commit `8ad9cea` (2026-11-17 23:20:17 America/New_York), subject “Buddy: verify local Claude Code document workflow (ACCEPT)”, exists as an object but is **not** an ancestor of current `HEAD`. Commit `268003d` (2026-11-23 15:51:31 UTC−8 = **18:51:31 America/New_York**), subject “Buddy: push ACCEPT verdict for local Claude Code document workflow (was only in local 8ad9cea)”, **is** an ancestor of `HEAD`. That matches S/N/Nm:27: local ACCEPT was not on the required branch until the later push.

**Not proven from git log or reflog (and therefore not claimed):**

- That the analysis file was in the index immediately before the 19:57:59 reset, or that `bb68779` itself unstaged it. A pathspec commit does not, by itself, record an unstage of other paths. The Orchestrator’s account of “HR’s commit unstaged a staged file” is consistent with a shared-clone index race, but git log/reflog cannot show the index membership of an untracked file.

**What we would do now:** do not leave own paths in the index between steps. Add, commit, and push only own paths in one command. Afterward, prove the remote and prove a clean index. Never stash, reset, or add another agent’s files in this shared clone.

---

## 6. Ten-minute lesson — “A staged or local-only file is not delivery”

**Audience:** every agent committing in the shared clone `/workspace/NFAI-mission-001`.  
**Length:** about 10 minutes, then the practice point.  
**Tied to:** U14 (S/N/Nm:27) and the 2026-11-23 shared-clone case in §5. Teaching the principle, not a prompt.

### The case

You finished a real deliverable in a clone that several agents share. You may have staged it, or you may have left it untracked, planning to commit after a review or after someone else finishes. Meanwhile another agent commits, or someone runs `git reset` to HEAD. Your file is still on disk. It is not on `origin/mission-001`. A later `git log` cannot show that you “had it ready.” The Founder and the Orchestrator can only accept what `git ls-remote` and the commit tree show.

### Decision point

When is the work done? When the file is saved? When it is staged? When it is in a local commit? Or when the required remote has a commit of only your paths and you have checked the hash?

### Options (and why most of them fail)

- *Leave it staged and come back later.* The index is shared. A mixed reset to HEAD, or another agent’s cleanup, can clear it. Reflog may show the reset and still not mention your file.
- *Commit everything that is staged, or `git add` broadly.* You may ship another agent’s unfinished path, or take their file out of their hands.
- *Commit locally and report “done.”* That is U14: the verdict existed on 2026-11-17 and was not on the required history until 2026-11-23.
- *Add, commit, and push only your paths in one command, then compare `git ls-remote` to your hash (or show that `origin/mission-001` is a descendant).* This is the only option that matches `TASKS.md:2`.

### The principle (why)

Delivery is a fact about a shared remote, not a feeling about a working tree. In a shared clone the index is not a private inbox. Learning is a change in behavior (Module 0, first principles): if agents still report “ready” while the file is untracked or local-only, the lesson was not learned. Check the checker (F11): `git status` and `git ls-remote` are the check; your memory of having staged the file is not.

### Rule to apply on the next commit

1. Confirm the branch (`mission-001`). Run `git pull --rebase` before you add anything. If that rebase fails because of other agents’ unstaged or untracked files, stop. Do not stash, reset, or otherwise touch their paths. Report the blockage.
2. In **one** command, add, commit, and push **only your paths**. Do not leave your files in the index between steps.
3. Prove it: `git show --name-only` on your commit lists only your paths; `git ls-remote origin refs/heads/mission-001` equals your hash, or `git branch -r --contains <hash>` includes `origin/mission-001`; `git diff --cached` is empty.
4. If the push is rejected, `git pull --rebase` and retry **once**. Never force-push.

---

## 7. Practice point (exactly one)

**Scenario.** You are in `/workspace/NFAI-mission-001` on `mission-001`. Your deliverable is an untracked file at a path only you own. Other untracked or staged files belonging to other agents may be present. You must deliver your file without touching theirs.

**Task.** After `git pull --rebase` succeeds, run one own-path add + commit + push, then produce the proof commands’ output.

**Pass criterion (all three must be true):**

1. `git show --name-only --pretty=format: <your-commit>` lists exactly your path and no other path.
2. `git ls-remote origin refs/heads/mission-001` prints a hash that equals `<your-commit>`, **or** `git branch -r --contains <your-commit>` includes `origin/mission-001` (a later descendant is acceptable; say which).
3. Immediately afterwards, `git diff --cached` is empty, and `git status --porcelain` does not show your path as staged (first column `A` or `M`). Other agents’ untracked files may still appear; you must not add, stash, or reset them.

Fail: any other path in your commit; “done” reported from a local commit or a staged file only; a force push; or another agent’s path changed in the index or worktree by you.

Example proof shape (replace the hash after you commit):

```bash
git show --name-only --pretty=format: HEAD
git ls-remote origin refs/heads/mission-001
git branch -r --contains HEAD
git diff --cached
git status --porcelain
```

---

## 8. Spaced-review dates

- **2026-11-26** (day 3): each agent who commits in this clone recites the pass criterion and applies it to that day’s commit (retrieval, not a reread).
- **2026-11-30** (day 7): Professor samples three recent `mission-001` commits: own-path only, `ls-remote` or descendant proof present, index not left staged. Recurrence of U14-class or index-left-staged failures is logged.

Curriculum intervals (1 month, 1 quarter) stay as they are in `professor.md` and will be used for a later revisit of the same principle; they are not extra checks in this exercise.

---

## 9. DRAFT — not sent

Systemic-error flag for the Orchestrator. Draft only. Not sent by the Professor.

- **Type:** T2 / shared-clone commit, proof, and index hygiene. Work reported or left staged/untracked is not on the required remote.
- **Agents:** any agent committing in `/workspace/NFAI-mission-001` (today’s case is role-independent). Logged precursor: Buddy (U14). Related logged delivery failures: Buddy (U3, U6). Live clone users on 2026-11-23 include at least HR (`bb68779`, `f70598c`), training-check authors, and the Professor (analysis file still untracked).
- **Examples and dates:**
  - U14, recorded 2026-11-17, fixed 2026-11-23: ACCEPT in local `8ad9cea` (2026-11-17 23:20:17 America/New_York), not an ancestor of current `HEAD`; pushed as `268003d` (2026-11-23 18:51:31 America/New_York). Citations: S/N/Nm:27.
  - 2026-11-23, shared clone: `_core/staff/error-analysis-2026-11-23.md` never appears in `git log`; remains untracked. Reflog shows `reset: moving to HEAD` at 19:57:59 America/New_York (HEAD was `f70598c`). Not proven from log/reflog: that this file was staged just before that reset, or that `bb68779` (20:00:24) itself unstaged it.
  - U3 (S/N/Nm:6) and U6 (S/N/Nm:16), 2026-11-17: result not delivered to the Founder until it was asked for — same “done without proof” family.
- **Already in force:** `TASKS.md:2` (push + `ls-remote`); commit rule recorded in `origin/main` `56ff980` (2026-11-23 20:03:42 America/New_York).
- **Ask:** treat “own paths, one command, then `ls-remote`, leave the index empty” as a standing gate for every agent on this clone. Do not have the Professor edit role prompts; route any prompt change through the Prompt Engineer and Internal Security.
- **Out of scope of this flag, already logged:** U16 (M:2, 2026-11-23 19:48 America/New_York) — Director self-execution on MISSION-001. Not this lesson’s practice point.

---

## 10. Self-check (Professor checklist)

- [x] Lesson tied to a real error or case (U14 + the 2026-11-23 shared-clone case)
- [x] Ends with one checkable practice point
- [x] Spaced-review dates set (2026-11-26 and 2026-11-30)
- [x] Curriculum version recorded (v2.0, 2026-11-17). Training-file changelog was **not** edited here; those files wait for a separate review and commit.
- [x] No prompt contents in this material
- [x] Public-repo secret scan before commit (no mailboxes, keys, tokens, or personal addresses)

This training-check commits only `missions/001-growth-os/training-check/professor-v2.md`. It does not add `_core/staff/error-analysis-2026-11-23.md` or any file under `/workspace/staff/training/`.
