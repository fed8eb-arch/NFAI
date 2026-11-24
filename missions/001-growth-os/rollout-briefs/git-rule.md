# Brief: Git rule for all agents (no bypass, own worktree, plain push)
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, `missions/001-growth-os/rollout-plan.md`, row "Агентство: правило git (без обхода)" and row "Агентство: отдельные git worktrees"). Context: Founder's order of 2026-11-23 17:28 PT (relayed): WireReady pilot paused; priority is full agency rollout.
Times: America/Los_Angeles (PT). Repository: `fed8eb-arch/NFAI` (public), local clone `/workspace/NFAI`.

## 1. Effective date
**This rule is mandatory for every agent that writes to the NFAI repository from 2026-11-25 00:00 PT.** Until then the bans already in force (do not bypass `pushurl`, commit only own paths, Orchestrator's orders of 2026-11-23) still apply, and agents are asked to follow this rule early.
Assignment to executors happens only after Internal Security (ГВБ) clears this brief, through the Orchestrator.

## 2. Owners
| Part | Who |
|---|---|
| Brief text | Prompt Engineer |
| Check of the brief; daily check of compliance; violation log | Head of Internal Security (ГВБ) |
| Reminder to agents; assignment; tracking | Orchestrator |
| Worktree setup support; verification that every writing agent has its own worktree | Integration Developer (Разработчик интеграций) |
| Acceptance of the rule | Director (Бадди) |
| Every writing agent | follows sections 3–5 |

## 3. Rules (every agent)
1. **Never bypass a lock.** A lock is any setting or state that stops a write or push: a `remote.<name>.pushurl` set to a non-URL value (for example `DO-NOT-PUSH-UNTIL-APPROVED`), a hook, a `*.lock` file inside `.git/`, a rejected push, or a written order to hold. Banned in every form:
   - `git -c remote.<name>.pushurl=...`, `git -c remote.<name>.url=...`, `git -c url.<x>.insteadOf=...`, `git -c core.hooksPath=...`, and any other `git -c` that changes where or how a push goes;
   - `git push <URL>` (pushing to an explicit URL instead of `origin`), `git push --no-verify`;
   - any edit of remote config (`git remote set-url`, `git remote add`, `git config remote.*`, `git config url.*`), of `pushurl`, of `core.hooksPath`, or of files in `.git/hooks/`; editing `.git/config` by hand;
   - deleting another process's `*.lock` file in `.git/`.
   A lock is lifted only by the person who ordered it, in writing (the Founder through the Director, or the Director). If you meet a lock: stop, leave your commit local, report (section 6).
2. **No history rewriting, no hidden work.** Banned: `git rebase` (including `git pull --rebase`), `git stash` (any subcommand; `refs/stash` is shared by all worktrees), `git reset --hard` on a branch others use, `git push --force` / `--force-with-lease` / `+refspec`, `git commit --amend` of a pushed commit.
3. **Never resolve conflicts in other agents' files.** If a merge, pull or push shows a conflict in a file you do not own, stop and report to the Orchestrator. Do not edit, check out, restore, delete or `git add` another agent's file.
4. **Own worktree.** Each writing agent works only in its own worktree, created with:
   `git -C /workspace/NFAI fetch origin && git -C /workspace/NFAI worktree add --detach /workspace/<agent>-wt origin/<branch>`
   `<agent>` is a short slug of your role (for example `pe`, `gvb`, `orch`, `prof`, `dev`); `<branch>` is the branch of your task (for example `mission-001` or `main`). Do not work in `/workspace/NFAI` or in the shared clone `/workspace/NFAI-mission-001`. Do not touch files in another agent's worktree. Remove only your own worktree (`git -C /workspace/NFAI worktree remove /workspace/<agent>-wt`), never another's.
5. **Commit only own paths, in one command, plain push:**
   `git add <own paths only> && git commit -m "<what>" && git push origin HEAD:<branch>`
   No `git add -A`, no `git add .`, no `-c`, no force. Before committing run `git status --short` and confirm the index holds only your paths. Before pushing run `git -C /workspace/NFAI config --get-all remote.origin.pushurl`: if it prints anything that is not the normal `origin` URL, it is a lock: do not push (rule 1).
6. **If the push is rejected** (non-fast-forward or any other reason): do not rebase, merge or force. Run `git -C /workspace/NFAI fetch origin`, create a fresh worktree from the new remote head (for example `/workspace/<agent>-wt2`), copy in only your own files, commit them with the command in rule 5, push again. If the second push also fails, stop and report the exact error.
7. **Verify every push:** `git ls-remote origin refs/heads/<branch>` must print the same hash as `git rev-parse HEAD`. Put both in your report. A local commit without this check is not "saved" and not "done".
8. **No secrets and no personal addresses in commits** (existing rule; ГВБ checks the diff of each push when pushing is allowed, per the plan).

## 4. Result / deliverable
- This rule cleared by ГВБ and accepted by the Director; the Orchestrator sends it to every writing agent before 2026-11-25 00:00 PT.
- From 2026-11-25: every writing agent has its own worktree (`git -C /workspace/NFAI worktree list` shows one path per agent); the Integration Developer confirms this in writing by 2026-11-28 (plan deadline for separate worktrees).
- Violations, if any, are logged by ГВБ (section 6).

## 5. Deadlines (PT)
| Item | Deadline |
|---|---|
| This brief to ГВБ for check | 2026-11-23 21:00 |
| ГВБ decision on this brief | to verify (ГВБ sets; proposed 2026-11-24 12:00) |
| Orchestrator sends the cleared rule to all writing agents | 2026-11-24 23:59 |
| Rule in force | 2026-11-25 00:00, then permanent (plan: at least until 2026-12-05) |
| Own worktree for every writing agent; Integration Developer's written confirmation | 2026-11-28 |

## 6. Detection and escalation of violations
**Daily detection (ГВБ, inside daily check step 2, from 2026-11-25; one line per day):**
1. Remote config: `git -C /workspace/NFAI config --show-origin --get-regexp '^(remote\..*\.(url|pushurl)|url\..*|core\.hookspath)$'` — any change from the previous day's line is an issue unless a written order covers it.
2. Hooks: `ls /workspace/NFAI/.git/hooks | grep -v '\.sample$'` — any new file is an issue unless ordered.
3. Force push / rewrite: yesterday's recorded `ls-remote` hash of each branch must be an ancestor of today's: `git merge-base --is-ancestor <yesterday-hash> origin/<branch>` (exit 0 = OK).
4. Lock bypass: if a lock was in force (rule 1) and `git ls-remote` shows the branch moved during the lock, it is a bypass until proven otherwise.
5. Rebase and stash: `git stash list` must be empty (or unchanged from the recorded baseline); `git -C <each worktree> reflog -n 100 | grep -E 'rebase|reset: moving'` must show nothing new.
6. Worktrees and paths: `git -C /workspace/NFAI worktree list`; for new commits of the last 24h, `git log --since=24.hours --name-only --format='%h %an' origin/<branch>` — each author touched only own paths (author names become auditable after brief `git-identity.md`).
**Self-report:** an agent that breaks a rule or meets a lock reports it itself, the same hour, to the Orchestrator and ГВБ: what command, when (PT), which hash, what is affected.
**Escalation path:** agent → Orchestrator and ГВБ (same hour) → ГВБ records it in the errors log (`_core/staff/errors-log.md`) and in the daily line → Orchestrator decides the fix → Director if a lock, a force push or the Founder's domain is involved → Founder only through the Director.
**Fixes:** never by force push or history rewrite. A wrong commit is undone only by a new commit, after ГВБ and Orchestrator approve. Rewriting history needs an explicit "yes" from the Founder through the Director.

## 7. Acceptance criteria
1. ГВБ has written a decision (cleared / changes required) on this brief, with date and path or hash.
2. The Orchestrator's dispatch to all writing agents is recorded (date, list of agents).
3. From 2026-11-25 to 2026-12-05, ГВБ's daily line shows the six detection checks; any issue has an errors-log entry and a decision.
4. By 2026-11-28, `git worktree list` shows one own worktree per writing agent, and no agent works in `/workspace/NFAI` or `/workspace/NFAI-mission-001`.
5. No new bypass, force push, rebase or stash after 2026-11-25 in the errors log (plan acceptance: "в журнале ошибок нет новых обходов").

## 8. Required proof
- Path of this brief and its commit hash on `origin/mission-001` = output of `git ls-remote origin refs/heads/mission-001`.
- ГВБ decision: file path and commit hash (via `ls-remote`).
- Daily: ГВБ's check line with the commands' results (no secrets).
- Integration Developer: output of `git -C /workspace/NFAI worktree list` with date (PT).
**"Done" only with proof.** A claim without a path and an `ls-remote`-verified hash is not done.

## 9. Conflicts with existing rules (for ГВБ and the Orchestrator)
- `AGENTS.md` (section "Автосохранение", line 74 at `56b9067`): `git add -A && git commit -m "<что сделано>" && git push` — conflicts with rule 5 (own paths only, `HEAD:<branch>`). This brief does not edit `AGENTS.md`; its owner should align it (to verify who owns that file).
- `mission-001/briefs/talks-02-03.md` (section 4): `git pull --rebase` and the shared worktree `/workspace/NFAI-mission-001` — conflict with rules 2 and 4. That task is finished; do not reuse that wording.
- `mission-001/briefs/w1-w4.md`: shared worktree `/workspace/NFAI-mission-001` — conflicts with rule 4. W1–W4 are paused; any new WireReady brief must use own worktrees.
- Plan deadlines differ: the rule takes effect 2026-11-25, the plan's deadline for separate worktrees is 2026-11-28. Until 2026-11-28 an agent without its own worktree creates it itself with the command in rule 4 before its first write; to verify with the Orchestrator.

## 10. To verify
- Who may legally lift a lock besides the Founder through the Director (this brief assumes: the person who set it, in writing).
- ГВБ's deadline for this check.
- The exact list of "writing agents" depends on the approved roster ("9 heads" list is the Founder's domain; not decided here).
