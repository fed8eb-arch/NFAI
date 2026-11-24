# NFAI offline task registry

Prototype for recording work and acceptance, using only Python's standard library.
It does not launch agents, synchronize GitHub, authenticate people, verify evidence,
or implement independent review: identities and evidence are operator assertions.
Use only on a private local database, outside the public repository. Do not enter
credentials, confidential information, or full transcripts.

```text
python registry.py --db private-tasks.sqlite add T1 "Review source" worker
python registry.py --db private-tasks.sqlite move T1 assigned --actor director --note assigned
python registry.py --db private-tasks.sqlite move T1 running --actor worker --note started
python registry.py --db private-tasks.sqlite move T1 review --actor worker --note submitted --evidence artifact-reference
python registry.py --db private-tasks.sqlite move T1 accepted --actor reviewer --note checked --evidence review-reference
python registry.py --db private-tasks.sqlite list
python -m unittest -v test_registry
```

Never interpret the event log as proof that a real independent person or agent
has reviewed an item. Back up and control access to the database separately.

## 2026-11-24 — claim and recovery safety

Only the recorded owner may transition an assigned task to running or submit it for review. Assignment requires an operator distinct from that owner. A blocked task requires explicit reassignment before retry; a review must be blocked and reassigned before rework. Accepted is terminal. SQLite BEGIN IMMEDIATE serializes transition and audit event across local writers. Two concurrent claims of one assigned task produce exactly one successful running transition. On interruption reconcile external side effects before authorizing another attempt; the registry cannot guarantee exactly-once external actions.

Native Python 3.13.5 / SQLite validation: 6/6 unit tests PASS, including two real concurrent connections to a temporary SQLite file, owner/duplicate rejection and reassignment recovery. Tested registry blob b996e9482548f58eac146d939c6042c2fde789ac (commit bff41f1bec395478a3ebba89b07dcee7fb716952), tests blob ec5da18c52cef9715a5a354c4eb405d437627389 (commit de6d6e0b257da628dc5afacd8c926e5408acd119); GitHub readback matched the locally tested blobs. This is still a local offline prototype, NOT deployed into Windows MCP or the private Bridge. Actor identifiers are operator assertions, not authenticated roles; a separate actor is not proof of authorization. Do not create a second agency source of truth or treat this test database as canonical. Next integrate with the existing private Bridge only after inspecting actual Windows MCP and identity/authority source; native ChatGPT events remain blocked.
