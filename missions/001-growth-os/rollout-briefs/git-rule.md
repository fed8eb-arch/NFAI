# Brief: Git rule for all agents (no bypass, own clone, plain push, push every step)
Version v1.5 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Changes:
- v1.0 → v1.1 (2026-11-23, Orchestrator's order): added rule 9 (Founder rule: a local commit without push does not count; push after every completed step). Listed the 9 app prompts' "Commit rule" line as a conflict.
- v1.1 → v1.2 (2026-11-23, Orchestrator's order):
  - the workspace is now **each agent's own fresh clone `/workspace/<agent>-clone`**. This replaces the per-agent worktree method of v1.0/v1.1 and the shared `/workspace/NFAI-mission-001`.
  - stated that the platform may replace the computer at any moment.
  - added section 10, "Prompt/profile updates".
  - Detection, deliverable and acceptance now refer to clones.
  - ГВБ's findings F1–F9 on v1.1 (`3346daf`, `clearance-git-rule.md`) are addressed: F1 effective date; F2 conflicts; F3 attribution; F4 lock check in own clone; F5 push only cleared work and only own commits; F6 branch moves; F7 who lifts a lock; F8 index check; F9 ГВБ deadline removed.

- v1.2 → v1.3 (2026-11-23): took in ГВБ's conditions on v1.2 (`2d3b238`, APPROVED WITH CONDITIONS). C1: what a rejected push means. C2: keep your files outside the repo when you stop at a lock. C3: `git-identity.md` is now v1.1, built on own clones.
- v1.3 → v1.4 (2026-11-23): made ГВБ's C1 and C2 explicit (`2d3b238`). A refusal by a hook, a permission or branch protection means STOP, report, never retry and never bypass. Named the durable folder for unpushed work (ГВБ named none; the folder is proposed, to verify). C3 was confirmed with no text change (`git-identity.md` v1.1 `94e7392` is built on own clones).
- v1.4 → v1.5 (2026-11-23): replaced the F5 pre-push clearance list with ГВБ's rule (relayed by the Orchestrator, 2026-11-23). Pre-push admission by ГВБ is needed only for prompts, the training corpus and public materials; ГВБ checks everything else after the push. v1.4 is APPROVED by ГВБ (`190f02e`); only rule 5 changed.

Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, `missions/001-growth-os/rollout-plan.md`, rows "Агентство: правило git (без обхода)" and "Агентство: отдельные git worktrees"). Context: Founder's order of 2026-11-23 17:28 PT (relayed): the WireReady pilot is paused; the priority is full agency rollout.
Times: America/Los_Angeles (PT). Repository: `fed8eb-arch/NFAI` (public), `https://github.com/fed8eb-arch/NFAI.git`.

## 1. Effective date
**This rule is mandatory for every agent that writes to the NFAI repository from the moment ГВБ clears it and the Orchestrator sends it out** (ГВБ F1). The task first named 2026-11-25; the Founder cancelled the deadlines, and a later date would leave a window for the 2026-11-23 incident to repeat. ГВБ has stated that the bans of rules 1–9 apply now, without waiting for this version to be cleared.
Executors are assigned only after Internal Security (ГВБ) clears this brief, and only through the Orchestrator.

## 2. Owners
| Part | Who |
|---|---|
| Brief text; prepared changes to prompts/profiles (section 10) | Prompt Engineer |
| Check of the brief; daily compliance check; violation log; clearance of prompt/profile changes | Head of Internal Security (ГВБ) |
| Reminder to agents; assignment; tracking; approval of prompt/profile changes | Orchestrator |
| Clone setup support; written check that every writing agent has its own clone | Integration Developer (Разработчик интеграций) |
| Acceptance of the rule; applying changed prompts to the bots | Director (Бадди) |
| Every writing agent | follows section 3 |

## 3. Rules (every agent)
0. **The machine is not durable.** The platform may replace the computer at any moment. Everything that is not pushed to origin is lost then: local commits, clones, worktrees and uncommitted files. Precedent: on 2026-11-23 at 17:42 PT the shared machine was replaced. The local `.git` of `/workspace/NFAI`, every linked worktree and every unpushed local commit were lost, including the Professor's commit `f712eb4`.
1. **Never bypass a lock.** A lock is anything that stops a write or a push:
   - a `remote.<name>.pushurl` set to a value that is not a URL (for example `DO-NOT-PUSH-UNTIL-APPROVED`);
   - a hook;
   - a `*.lock` file inside `.git/`;
   - a push refused by a hook, by missing permission, or by branch protection (ГВБ C1). A **non-fast-forward** rejection is not a lock: follow rule 6;
   - a written order to hold, which binds every clone even when your own config shows no lock.

   Banned in every form:
   - `git -c remote.<name>.pushurl=...`, `git -c remote.<name>.url=...`, `git -c url.<x>.insteadOf=...`, `git -c core.hooksPath=...`, and any other `git -c` that changes where or how a push goes;
   - `git push <URL>` (pushing to an explicit URL instead of `origin`) and `git push --no-verify`;
   - any edit of remote config (`git remote set-url`, `git remote add`, `git config remote.*`, `git config url.*`), of `pushurl`, of `core.hooksPath`, or of files in `.git/hooks/`, and editing `.git/config` by hand;
   - deleting another process's `*.lock` file in `.git/`;
   - cloning a second copy to get around a lock or a hold order. A fresh clone after a non-fast-forward rejection (rule 6) is not a bypass.

   **Who lifts a lock (ГВБ F7):** only the Director, or the Founder through the Director, in writing. An agent who set a lock may remove it only with their written consent. The Orchestrator keeps the list of hold orders in force. If you meet a lock: stop, leave your commit local, also copy your own changed files into your durable folder `/workspace/<agent>-unpushed/` (rule 9; ГВБ C2), and report it (section 6).
2. **No history rewriting and no hidden work.** Banned:
   - `git rebase`, including `git pull --rebase`;
   - `git stash` (any subcommand);
   - `git reset --hard` on a branch others use;
   - `git push --force`, `--force-with-lease` and `+refspec`;
   - `git commit --amend` of a pushed commit;
   - moving branches others use (ГВБ F6): `git branch -f`, `git checkout -B`, `git update-ref`, any `git reset` on a shared branch, and deleting another agent's branch or ref.
3. **Never resolve conflicts in other agents' files (ГВБ F2).** If a merge, pull or push shows a conflict in a file you do not own:
   - stop and leave the state as it is;
   - do not commit, and do not run `checkout`, `restore` or `merge --abort` on someone else's changes;
   - report to **the file's owner and the Orchestrator**: the file, the hashes and the time (PT).

   Never edit, check out, restore, delete or `git add` another agent's file.
4. **Own clone.** Each writing agent works only in its own fresh clone:
   `git clone --branch <branch> https://github.com/fed8eb-arch/NFAI.git /workspace/<agent>-clone`
   - `<agent>` is a short slug of your role, for example `pe`, `gvb`, `orch`, `prof`, `dev`. `<branch>` is the branch of your task, for example `mission-001` or `main`.
   - Do not work in `/workspace/NFAI`, in the shared `/workspace/NFAI-mission-001` or in any old worktree folder.
   - Never run `git init` over an old folder. Never touch another agent's clone.
   - Delete only your own clone, and only after everything in it is pushed.
   - If your clone is gone (for example after a machine replacement), clone again into the same path, or into `/workspace/<agent>-clone2` if the old folder still exists.
5. **Commit only your own paths, in one command, with a plain push:**
   `git add <own paths only> && git commit -m "<what>" && git push origin HEAD:<branch>`
   - No `git add -A`, no `git add .`, no `-c`, no force.
   - Before committing, run `git diff --cached --name-only` (ГВБ F8) and confirm that it lists only your paths.
   - **Attribution (ГВБ F3):** every commit message starts with your role, `<Role>: …` (for example `Prompt Engineer: …`), and every report with a hash carries the line `Agent: <role>`. When `git-identity.md` is in force, it is a mandatory addition to this rule: from then on a commit authored `NFAI Joker` is a violation.
   - **Push only your own commits (ГВБ F5):** before pushing, `git log origin/<branch>..HEAD --format='%h %s'` must list only your commits. Pushing other agents' commits is banned, including commits picked up "along the way" by a merge or rebase.
   - **Pre-push admission by ГВБ** (Internal Security rule, relayed by the Orchestrator, 2026-11-23; it replaces the v1.2–v1.4 F5 list) is required **only** for:
     1. prompts (agent app prompts and role profiles);
     2. the training corpus;
     3. public materials (anything published outside the repo).

     All other work is pushed straight away (rule 9), and ГВБ checks it **after the push**, in the daily check (step 2) or on request. Rule 8 still applies to every push: no secrets and no personal addresses. If you are unsure whether a file falls under items 1–3, treat it as needing admission and ask ГВБ.
   - Before pushing, run `git config --get-all remote.origin.pushurl` in your clone. If it prints anything, it is a lock: do not push (rule 1). Also check that no written hold order is in force.
6. **Rejected push: two cases (ГВБ C1).**
   - **Non-fast-forward** (`! [rejected] … (fetch first)` or `(non-fast-forward)`): someone pushed first. Do not rebase, merge or force. Instead:
     1. Make a fresh clone of the new remote head (for example `/workspace/<agent>-clone2`).
     2. Copy in only your own files.
     3. Commit them with the command in rule 5 and push again, once.

     If that push also fails, stop and report the exact error.
   - **Refusal by a hook, a missing permission, branch protection or a failed authentication** (for example `pre-receive hook declined`, `protected branch`, `Permission denied`, `403`, `Authentication failed`): this is a **lock**.
     - **STOP.** Do not retry, do not change the remote, credentials or config, and do not try another clone, URL or account. Never bypass it.
     - Copy your own changed files to `/workspace/<agent>-unpushed/` (rule 9).
     - Report the exact error text (without any token or URL credentials) to the Orchestrator and ГВБ the same hour.

7. **Verify every push.** `git ls-remote origin refs/heads/<branch>` must print the same hash as `git rev-parse HEAD`. Put both in your report. A commit without this check is not "saved" and not "done".
8. **No secrets and no personal addresses in commits** (existing rule). When pushing is allowed, ГВБ checks the diff of each push, per the plan.
9. **Push after every completed step (Founder rule, relayed by the Orchestrator, 2026-11-23).** A local commit without a push does not count: it is not saved, not "done" and not evidence.
   - Push your branch (`git push origin HEAD:<branch>`, then the `ls-remote` check of rule 7) after every completed step, not only at the end of a session (see rule 0).
   - If a lock stops the push (rule 1, rule 6), the step is not done. Report it, and copy your own changed files into **`/workspace/<agent>-unpushed/<YYYY-MM-DD>/`**. ГВБ named no folder, so this one is proposed, to verify with ГВБ.
     - The folder is outside any repo and has no `dist`, `build`, `out`, `coverage` or `target` path segment and no dot-folder (`.cache`, `.next` and the like).
     - It is not under `/tmp`, `/workspace/browser-cdp` or `/workspace/screenshots`. The platform wipes those on a machine replacement.
     - Even this folder is safer, not safe: only a push is durable.

## 4. Result / deliverable
- This rule is cleared by ГВБ and accepted by the Director. The Orchestrator sends it to every writing agent right after ГВБ clears it.
- From the date the rule is in force, every writing agent works in its own `/workspace/<agent>-clone`. By 2026-11-28 the Integration Developer confirms this in writing: one line per agent with the path, `git -C <path> remote -v` and the date.
- Prompt and profile changes are prepared as in section 10.
- ГВБ logs any violations (section 6).

## 5. Deadlines (PT)
The Director cancelled the writing deadlines for the briefs on 2026-11-23. Execution:
- the rule is in force from ГВБ's clearance and the Orchestrator's dispatch, then permanently (the plan says at least until 2026-12-05);
- own clones are confirmed by 2026-11-28 (plan);
- rule 9 applies at once.

## 6. Detection and escalation of violations
**Daily detection (ГВБ, inside daily check step 2, from the day the rule is in force; one line per day), run in each agent's clone listed by the Integration Developer:**
1. Remote config: `git -C <clone> config --show-origin --get-regexp '^(remote\..*\.(url|pushurl)|url\..*|core\.hookspath)$'`. Any change from the previous day's line is an issue unless a written order covers it.
2. Hooks: `ls <clone>/.git/hooks | grep -v '\.sample$'`. Any new file is an issue unless ordered.
3. Force push or rewrite: yesterday's recorded `ls-remote` hash of each branch must be an ancestor of today's: `git merge-base --is-ancestor <yesterday-hash> origin/<branch>` (exit 0 = OK).
4. Lock bypass: if a lock or a hold order was in force and `git ls-remote` shows that the branch moved during it, it is a bypass until proven otherwise.
5. Rebase and stash: `git -C <clone> stash list` must be empty, and `git -C <clone> reflog -n 100 | grep -E 'rebase|reset: moving'` must show nothing new.
6. Clones and paths: is the list of clones complete? For the new commits of the last 24h, `git log --since=24.hours --name-only --format='%h %an' origin/<branch>` must show that each author touched only their own paths. Author names become auditable after brief `git-identity.md`.

**Self-report:** an agent that breaks a rule or meets a lock reports it itself, the same hour, to the Orchestrator and ГВБ: the command, the time (PT), the hash, and what is affected.

**Escalation path:**
1. The agent reports to the Orchestrator and ГВБ the same hour.
2. ГВБ records it in the errors log (`_core/staff/errors-log.md`) and in the daily line.
3. The Orchestrator decides the fix.
4. The Director is involved if a lock, a force push or the Founder's domain is involved.
5. The Founder is reached only through the Director.

**Fixes:** never by force push or history rewrite. A wrong commit is undone only by a new commit, after ГВБ and the Orchestrator approve. Rewriting history needs an explicit "yes" from the Founder through the Director.

## 7. Acceptance criteria
1. ГВБ has written a decision (cleared / changes required) on this brief, with the date and a path or hash.
2. The Orchestrator's dispatch to all writing agents is recorded (date, list of agents).
3. From the date the rule is in force to 2026-12-05, ГВБ's daily line shows the six detection checks, and any issue has an errors-log entry and a decision.
4. By 2026-11-28 every writing agent has its own clone (Integration Developer's list), and no agent works in `/workspace/NFAI`, `/workspace/NFAI-mission-001` or an old worktree.
5. The errors log shows no new bypass, force push, rebase or stash after the rule is in force (plan acceptance: "в журнале ошибок нет новых обходов").
6. The section 10 changes went PE → ГВБ → Orchestrator → apply, and each step has a date and a hash.

## 8. Required proof
- The path of this brief and its commit hash on `origin/mission-001` = output of `git ls-remote origin refs/heads/mission-001`.
- ГВБ's decision: file path and commit hash (via `ls-remote`).
- Daily: ГВБ's check line with the results of the commands (no secrets).
- Integration Developer: the list of clones with the date (PT).

**"Done" only with proof.** A claim without a path and an `ls-remote`-verified hash is not done.

## 9. Conflicts with existing rules (for ГВБ and the Orchestrator)
- `AGENTS.md` ("Корень `/workspace/NFAI`"; section "Автосохранение", line 74 at `56b9067`) says `git add -A && git commit -m "<что сделано>" && git push`. That conflicts with rules 4 and 5. This brief does not edit `AGENTS.md`; its owner should align it (to verify who owns that file).
- `mission-001/briefs/talks-02-03.md` (section 4) uses `git pull --rebase` and the shared `/workspace/NFAI-mission-001`, which conflicts with rules 2 and 4. That task is finished; do not reuse that wording.
- `mission-001/briefs/w1-w4.md` uses the shared `/workspace/NFAI-mission-001`, which conflicts with rule 4. W1–W4 are paused; any new WireReady brief must use own clones.
- The 9 head app prompts v1.1 on `origin/main` (`_core/staff/app-prompts/*.md`, text `563faab`, Status line `a7e48cc`) conflict with rules 4 and 5. All 9 have a "Commit rule" line that says to commit in the shared `/workspace/NFAI-mission-001`. The prompts of hr-head, internal-security-head and professor also have "Mission work: /workspace/NFAI-mission-001". `app-prompts/training-briefs.md` cites the shared clone 12 times. They are handled through section 10.
- The rollout plan row "Агентство: отдельные git worktrees" expects worktrees. This brief replaces them with own clones, by the Orchestrator's order of 2026-11-23. The plan text is not changed here.
- `git-identity.md` v1.0 was built on worktrees. **v1.1 (`94e7392`) is built on own clones**: identity goes in the clone's local config; ГВБ's decisions are form B, the env-var fallback, and no `-c user.*` (ГВБ C3).

## 10. Prompt/profile updates
- **Affected:** every agent prompt or profile whose workspace line points to `/workspace/NFAI-mission-001`, `/workspace/NFAI` or a worktree. Found so far on `origin/main`:
  - the 9 head app prompts (their "Commit rule" lines, plus the "Mission work" lines of hr-head, internal-security-head and professor);
  - `app-prompts/training-briefs.md`;
  - `AGENTS.md`.

  Role cards in `_core/staff/` and the Director's, Orchestrator's and other agents' bot prompts are likely affected too; the full list is to verify.
- **New workspace line (proposed text for each affected prompt):** `Workspace: your own fresh clone /workspace/<agent>-clone (git clone --branch <branch> https://github.com/fed8eb-arch/NFAI.git /workspace/<agent>-clone); commit only own paths in one command; git push origin HEAD:<branch> after every completed step; verify with git ls-remote. Never use the shared /workspace/NFAI-mission-001. Follow missions/001-growth-os/rollout-briefs/git-rule.md.`
- **Order:** the Prompt Engineer prepares the change (new version, changelog) → ГВБ clears it → the Orchestrator approves → it is merged to `main` → the Director applies it to the bots. **No prompt or profile is edited before ГВБ's clearance.** This brief edits none.
- Deliverable: one change set with a version bump and changelog entries, plus intro ACK of the new version, as in `intro-ack-v1.1.md`.

## 11. To verify
- The full list of affected prompts and profiles.
- The exact list of writing agents. It depends on the approved roster; the "9 heads" list is the Founder's domain and is not decided here.
