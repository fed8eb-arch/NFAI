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

