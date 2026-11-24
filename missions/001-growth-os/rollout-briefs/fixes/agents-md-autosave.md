# Fix proposal: AGENTS.md "Автосохранение" — own paths instead of `git add -A`
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (conflict-fix package from ГВБ, item C1, most urgent). Basis: `missions/001-growth-os/rollout-briefs/git-rule.md` v1.5 (v1.4 APPROVED by ГВБ, `190f02e`), rules 4, 5, 7 and 9; ГВБ confirmed the conflict `AGENTS.md:74` in `clearance-git-rule.md`.
This file is only a proposal. `AGENTS.md` is not edited here: it is a shared root file (role and hierarchy text, Founder orders), and its owner applies the change after ГВБ admission and Orchestrator approval. Nothing in `AGENTS.md` other than the line below is touched.

## Why
`git add -A` stages every change in the working tree, including other agents' files and any stray file with secrets (`.env`, keydrop exports, tokens). The repo is public, so one such commit publishes the secret. This is the risk that ГВБ flagged. `git-rule.md` rule 5 already bans `git add -A` / `git add .`.

## Change (exact text)
File: `AGENTS.md`, section `## Автосохранение`, **line 74** (on `origin/mission-001` at `a430dee`; to verify the line number on `main` before applying).

**Old:**
```text
Вся работа сохраняется в публичный репозиторий https://github.com/fed8eb-arch/NFAI (ветка main); репозиторий остаётся публичным по приказу Основателя. После каждого шага: `git add -A && git commit -m "<что сделано>" && git push`. Ключи, пароли, keydrop и .env не коммитить.
```

**New:**
```text
Вся работа сохраняется в публичный репозиторий https://github.com/fed8eb-arch/NFAI; репозиторий остаётся публичным по приказу Основателя. Работай только в своём свежем клоне `/workspace/<agent>-clone` и по правилу `missions/001-growth-os/rollout-briefs/git-rule.md`. После каждого шага: `git add <только свои пути> && git commit -m "<Роль>: <что сделано>" && git push origin HEAD:<ветка>`, затем проверь, что `git ls-remote origin refs/heads/<ветка>` совпадает с `git rev-parse HEAD`. `git add -A` и `git add .` запрещены: они захватывают чужие файлы и могут затащить секреты. Без `-c`, force, rebase и stash. Локальный коммит без push не считается сохранённым. Ключи, пароли, keydrop и .env не коммитить.
```

Note: the old text says "(ветка main)". The new text names the branch per task (`<ветка>`), because mission work goes to `mission-001` and `main` gets changes only after admission. To verify with the Orchestrator: should "(ветка main)" stay as the default branch?

## Related, not changed by this proposal (for the owner)
- `AGENTS.md:3`: «Корень `/workspace/NFAI`». After the machine replacement of 2026-11-23 17:42 PT that folder is not a git repository, and `git-rule.md` bans working there. Proposed: «Корень — свой клон `/workspace/<agent>-clone`»; to verify.
- Other parts of `AGENTS.md` that may belong to findings F1/F2 are the Founder's domain. They are not quoted or changed here.

## Order
Prompt Engineer (this proposal) → ГВБ admission → Orchestrator approval → the owner of `AGENTS.md` applies the change on `main` in their own clone, one file, plain push → `ls-remote` check.

## Acceptance and proof
- `AGENTS.md` line in `## Автосохранение` equals the **New** text; `grep -c "git add -A" AGENTS.md` = 0.
- Commit hash = output of `git ls-remote origin refs/heads/main`.

**"Done" only with proof.**
