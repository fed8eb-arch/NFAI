# NFAI Professor exercises

Exercise version 1.0 · 18 November 2026

Run the following Python 3 standard-library script. It uses only synthetic fixtures. The checks require no account, external request, model, or package installation.

```python
import json
from statistics import mean

# Harness² practice: use a fixed answer key to compare two instructions.
claims = [
    {"source": True, "test": False},
    {"source": True, "test": True},
    {"source": False, "test": False},
    {"source": True, "test": True},
]
expected_decisions = [False, True, False, True]
baseline = [claim["source"] for claim in claims]
candidate = [claim["source"] and claim["test"] for claim in claims]
scores = [
    sum(decision == expected for decision, expected in zip(answers, expected_decisions))
    for answers in (baseline, candidate)
]
assert scores == [3, 4], scores
print(f"Evidence gate: {scores[0]}/4 -> {scores[1]}/4")

# Forecasting practice: compare held-out one-step forecasts against baselines.
series = [20 + (index % 4) * 3 for index in range(24)]
origins = range(8, len(series))
last_value_mae = mean(abs(series[index] - series[index - 1]) for index in origins)
seasonal_mae = mean(abs(series[index] - series[index - 4]) for index in origins)
assert (len(origins), last_value_mae, seasonal_mae) == (16, 4.5, 0)
print(f"Forecast baselines: {len(origins)} steps, MAE {last_value_mae} / {seasonal_mae}")

# Code Mode practice: return only the fields needed for a read-only decision.
records = [
    {"id": index, "finished": index % 4 == 0, "owner": "fictional", "detail": "padding " * 24}
    for index in range(32)
]
full = json.dumps(records, separators=(",", ":")).encode("utf-8")
selected = json.dumps(
    [record["id"] for record in records if record["finished"]],
    separators=(",", ":"),
).encode("utf-8")
expected_ids = [0, 4, 8, 12, 16, 20, 24, 28]
assert json.loads(selected) == expected_ids
assert (len(full), len(selected)) == (8015, 22)
print(f"Read-only projection: {len(expected_ids)} IDs, {len(full)} -> {len(selected)} bytes")
```

Expected output

```text
Evidence gate: 3/4 -> 4/4
Forecast baselines: 16 steps, MAE 4.5 / 0
Read-only projection: 8 IDs, 8015 -> 22 bytes
```

To pass, reproduce all three lines and explain one evidence boundary per exercise. The first comparison uses deterministic rules on a fixed fixture, the second measures simple synthetic baselines, and the third measures JSON bytes. Harness², TimesFM and the Cloudflare runtime are outside these checks. Vendor benchmark numbers, real forecast accuracy, and model token savings remain unmeasured.
