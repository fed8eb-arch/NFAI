"""Check for performance regressions between comparable Lighthouse navigation reports."""

import argparse
import json
import math
from pathlib import Path
import sys
from urllib.parse import urlsplit


METRICS = (
    ("LCP", "largest-contentful-paint", "millisecond", "ms"),
    ("CLS", "cumulative-layout-shift", "unitless", ""),
    ("TBT", "total-blocking-time", "millisecond", "ms"),
)
PROFILE_FIELDS = ("formFactor", "throttlingMethod", "throttling", "screenEmulation")


def read_report(path):
    report = json.loads(path.read_text(encoding="utf-8"))
    settings = report["configSettings"]
    if report.get("runtimeError") or report.get("gatherMode", settings.get("gatherMode", "navigation")) != "navigation":
        raise ValueError("A successful Lighthouse navigation report is required")
    route = urlsplit(report["requestedUrl"])
    final_url = report.get("finalDisplayedUrl") or report.get("finalUrl")
    destination = None
    if final_url:
        final_route = urlsplit(final_url)
        if final_route.netloc != route.netloc:
            raise ValueError("Report redirects to a different host")
        destination = (final_route.path or "/", final_route.query)
    profile = (
        route.path or "/",
        route.query,
        destination,
        report["lighthouseVersion"],
        *(settings[field] for field in PROFILE_FIELDS),
    )
    values = []
    for label, audit_id, unit, _ in METRICS:
        audit = report["audits"][audit_id]
        value = audit.get("numericValue")
        if (
            audit.get("scoreDisplayMode") == "error"
            or audit.get("numericUnit") != unit
            or type(value) not in (int, float)
            or not math.isfinite(value)
            or value < 0
        ):
            raise ValueError(f"Missing or invalid {label} measurement")
        values.append(value)
    return profile, values


def nonnegative(value):
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise argparse.ArgumentTypeError("Expected a finite non-negative number")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--allow-time-ms", type=nonnegative, default=0, help="Allowed increase for LCP and TBT")
    parser.add_argument("--allow-cls", type=nonnegative, default=0, help="Allowed increase for CLS")
    args = parser.parse_args()
    try:
        baseline_profile, baseline = read_report(args.baseline)
        candidate_profile, candidate = read_report(args.candidate)
        if baseline_profile != candidate_profile:
            raise ValueError("Reports must use the same requested and final route, Lighthouse version and measurement profile")
    except (OSError, AttributeError, KeyError, TypeError, ValueError) as error:
        print(f"Cannot compare reports: {error}", file=sys.stderr)
        return 2

    regressed = False
    for (label, _, unit, suffix), before, after in zip(METRICS, baseline, candidate):
        allowance = args.allow_cls if unit == "unitless" else args.allow_time_ms
        limit = before + allowance
        passed = after <= limit or math.isclose(after, limit, rel_tol=0, abs_tol=1e-9)
        regressed |= not passed
        outcome = "OK" if passed else "REGRESSION"
        print(f"{label}: {before:g} -> {after:g} {suffix} (allowance {allowance:g}) {outcome}".replace("  ", " "))
    return int(regressed)


if __name__ == "__main__":
    sys.exit(main())
