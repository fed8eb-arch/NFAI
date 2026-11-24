# Intro ACK v1.1 — results (9 head bots)
Version v1.0 | Date 2026-11-23 | Owner: Orchestrator | Brief: `intro-ack-v1.1.md` @08a58a6 (IS clearance 83531eb)
Requests sent by the Orchestrator 2026-11-23 ~17:52 PT; all replies arrived 17:53 PT.
Comparison against `git show a7e48cc:_core/staff/app-prompts/<file>` (L1 = line 1; other lines = grep of the same file).
`git ls-remote origin refs/heads/main` at comparison (17:56 PT) = `da84ceb77be887e0884f26ce3e4903d4e7db164f` (contains a7e48cc → 563faab).

| Bot | Reply PT | L1 = a7e48cc line 1 | Injection | Hard line (as in file) | Mission work (as in file) | Commit rule | Result | Ref hash |
|---|---|---|---|---|---|---|---|---|
| client-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| delivery-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| finance-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| hr-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| internal-security-head | 17:53 | yes | yes | yes (own wording, line 6) | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| legal-head | 17:53 | yes | yes | yes (lower-case "hard line:", line 6) | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| marketing-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| product-head | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |
| professor | 17:53 | yes | yes | yes | yes | yes | MATCH v1.1 | 563faab + a7e48cc |

Quoted L1 (identical in all 9 replies): `Version v1.1 | Date 2026-11-23 | Status: v1.1 cleared by Internal Security (eaebb4c) and Orchestrator, 2026-11-23 | Owner: Prompt Engineer`
All 9 replied `Prompt hash: "not in my prompt"`; none reported eaebb4c as its hash.

## Notes
1. Brief section 3 table is inaccurate: it says client/delivery/finance/legal/marketing/product have no Mission work line, and internal-security has no Hard line. The files at a7e48cc do contain them (grep, lines 6–11). Bots' replies match the files. → Prompt Engineer to fix the table.
2. Limit of proof: each bot quoted its agency role profile only (platform instructions not disclosed). The ACK proves the role profile carries v1.1 text, not the whole runtime prompt.
3. All 9 Commit rule / Mission work lines still point to the shared clone `/workspace/NFAI-mission-001`, which contradicts git-rule v1.3 (own clone). Needs prompts v1.2 (PE → IS → main → bots). Raised by IS-head too.
