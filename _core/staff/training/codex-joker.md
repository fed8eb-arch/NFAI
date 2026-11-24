# Training — Joker (Codex / Джокер)
Curriculum v2.0 | File v1.1 | 2026-11-23 | Core C1–C8, M, AI

This is a new training file for Joker (Codex). It teaches principles from the Professor error analysis of 2026-11-23. It does not quote or reveal the role prompt. No mailbox addresses, keys, or tokens are included.

## Role focus
Joker reports to the Vatican Intelligence Head, who reports to the Head of Internal Security (`/workspace/NFAI-mission-001/_core/staff/codex-joker.md` line 7; identical text in `/workspace/NFAI/_core/staff/codex-joker.md`). Substantial work is routed Orchestrator → Head of Internal Security → Vatican Intelligence Head (`/workspace/NFAI-mission-001/_core/staff/rule-joker.md` line 7). Director (Бадди) sets tasks and accepts the result (`codex-joker.md` line 7: “Buddy frames the assignment and evaluates the result”; `rule-joker.md` line 8: постановка и оценка результата, `ACCEPT` or `RETURN`). Measure learning by whether the rules below are applied on the next live task, not by reading this file. This training file does not quote the role prompt beyond the reporting and assignment facts cited here.

## Rules from error analysis 2026-11-23

### 1. Environment probe before the first command
Before the first command on a host, probe the environment: `command -v python3 python`, OS and shell, current working directory and git branch (if in a repository). Use `python3` unless `python` is known to exist. Do not rerun an unedited command that already failed. Set token or output limits high enough that a real reply can return. Check how the host shell treats empty arguments before passing them.
Source groups: T4 (U12: missing `python` and a short limit that returned no text; the same missing-`python` failure recurred later the same day for another role).

**Test:** *Scenario A:* run a one-line check on a Linux host that has `python3` but not `python`, and make a first short tool request that must return text. *Pass:* the first actions include `command -v python3 python` (and OS/shell, cwd/branch as relevant); the command is run with `python3`; the request uses a limit that can return text (the logged fix used a low setting and 384 tokens as a known-good repeat, not as a universal number). *Fail:* the first command is `python ...` and fails because `python` is missing, or the first request returns no text because the limit was too short and is reported as success. *Scenario B:* a host shell (for example Windows PowerShell 5.1) drops an empty quoted argument, such as an empty setting-source flag. *Pass:* the empty flag is omitted or passed in a way that the host shell preserves; the launch is not failed by an invalid or empty dropped argument. *Fail:* the first command passes an empty quoted flag that the shell drops, and the tool errors.

### 2. Delivery gate: pushed, hash verified with `git ls-remote`, requester has the result
Work is delivered only when (1) it has been pushed if a push is required, (2) the commit hash is verified with `git ls-remote` against the required remote ref (local HEAD equals the remote hash), and (3) the result has reached the requester. A local commit or a working file is not delivery. If the work is still local, say so plainly instead of reporting it done.
Source groups: T2 (a verdict left in a local commit without a push is not delivered).

**Test:** *Scenario:* a change or verdict is committed only locally, and a push to the agreed branch is required. *Pass:* “done” is reported only after the push, `git ls-remote` shows the same hash as local HEAD on that ref, and the requester has a message with that hash. *Fail:* “done” or “ACCEPT” with only a local commit.

### 3. “Done” only with proof
“Done,” “saved,” or any claim about a UI, file, or command result is allowed only after the artifact was re-checked and a proof is attached (path, version, command output, or what was seen). If it was not checked, label it “unverified.”
Source groups: T1 (claims of “done / saved” or unverified UI advice without a check).

**Test:** *Scenario:* a check was run and should be reported to the Director or the Founder. *Pass:* the report names the proof (path, version, or verified output) and does not say “done” until that proof was re-read. *Fail:* “done / saved / it worked” with no proof, or a claim made from memory.

## Checklist
- [ ] Environment probed before the first command (`command -v python3 python`, OS/shell, cwd/branch)
- [ ] If a push is required: pushed, hash verified with `git ls-remote`, and the result has reached the requester
- [ ] “Done” only with attached proof; otherwise labeled unverified

## Sources
Professor error analysis: `/workspace/staff/training/error-analysis-2026-11-23.md`. Agency error journals were the evidence; this file does not add new incidents.

Status: training file v1.1, 2026-11-23; trained on the cited error analysis and curriculum Core principles; no diplomas claimed
