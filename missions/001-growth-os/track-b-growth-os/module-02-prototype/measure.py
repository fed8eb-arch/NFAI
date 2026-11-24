#!/usr/bin/env python3
"""Query one LiteLLM model with buyer questions and record brand visibility.

This measures the model behind the local free-chat route only. It is not a
measurement of ChatGPT, Gemini, Perplexity, or any other consumer AI search
engine. Load the router key with:

    set -a; . ~/secrets/agency-llm.env; set +a

Never print or commit the key.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from detect import analyze_answer, summarize_run

ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG = ROOT / "config.wireready.json"
DEFAULT_OUT = ROOT / "output"


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def chat_completion(api_base: str, key: str, model: str, messages: list, timeout: int, max_tokens: int, temperature: float) -> dict:
    url = api_base.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
            return {"ok": True, "http_status": response.status, "body": body, "error": None}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        return {"ok": False, "http_status": exc.code, "body": None, "error": f"HTTP {exc.code}: {detail}"}
    except Exception as exc:  # noqa: BLE001 — record network failures in the run log
        return {"ok": False, "http_status": None, "body": None, "error": f"{type(exc).__name__}: {exc}"}


def extract_message(body: dict | None) -> tuple[str, str | None, dict | None]:
    if not body:
        return "", None, None
    choices = body.get("choices") or []
    content = ""
    if choices:
        message = choices[0].get("message") or {}
        content = message.get("content") or ""
    return content, body.get("model"), body.get("usage")


def flatten_row(row: dict) -> dict:
    mentioned = [item["name"] for item in row.get("competitors") or [] if item.get("mentioned")]
    cited = []
    for item in row.get("competitors") or []:
        cited.extend(item.get("cited_urls") or [])
    return {
        "question_id": row["question_id"],
        "category": row["category"],
        "question": row["question"],
        "ok": row["ok"],
        "http_status": row["http_status"],
        "latency_s": row["latency_s"],
        "returned_model": row["returned_model"],
        "brand_mentioned": row["brand_mentioned"],
        "brand_matched_names": " | ".join(row.get("brand_matched_names") or []),
        "brand_cited_urls": " | ".join(row.get("brand_cited_urls") or []),
        "competitors_mentioned": " | ".join(mentioned),
        "competitor_cited_urls": " | ".join(cited),
        "all_urls": " | ".join(row.get("urls") or []),
        "error": row.get("error") or "",
        "answer": row.get("answer") or "",
    }


def run(config_path: Path, out_dir: Path) -> Path:
    config = load_config(config_path)
    key = os.environ.get("LITELLM_MASTER_KEY", "").strip()
    if not key:
        sys.exit(
            "LITELLM_MASTER_KEY is not set. Load it with "
            "`set -a; . ~/secrets/agency-llm.env; set +a` and rerun. "
            "Do not paste the key into the command line or a file in this repo."
        )
    api_base = config.get("api_base") or "http://127.0.0.1:4000/v1"
    model = config.get("model") or "free-chat"
    timeout = int(config.get("timeout_s") or 90)
    max_tokens = int(config.get("max_tokens") or 800)
    temperature = float(config.get("temperature") if config.get("temperature") is not None else 0)
    pause = float(config.get("pause_s") or 0.4)
    system_prompt = config.get("system_prompt") or (
        "You are a helpful assistant answering a prospective buyer. "
        "Answer from what you know. If you mention organizations or websites, "
        "include URLs when you know them. If you are unsure, say so. "
        "Do not invent precise statistics."
    )
    brand = config["brand"]
    competitors = config.get("competitors") or []
    questions = config["questions"]

    started = datetime.now(timezone.utc)
    rows = []
    for item in questions:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": item["text"]},
        ]
        t0 = time.time()
        result = chat_completion(api_base, key, model, messages, timeout, max_tokens, temperature)
        latency = round(time.time() - t0, 3)
        answer, returned_model, usage = extract_message(result.get("body"))
        analysis = analyze_answer(answer, brand, competitors)
        rows.append(
            {
                "question_id": item["id"],
                "category": item.get("category") or "",
                "question": item["text"],
                "ok": result["ok"],
                "http_status": result["http_status"],
                "latency_s": latency,
                "requested_model": model,
                "returned_model": returned_model,
                "usage": usage,
                "error": result.get("error"),
                "answer": answer,
                **analysis,
            }
        )
        status = "ok" if result["ok"] else "FAIL"
        mentioned = "yes" if analysis["brand_mentioned"] else "no"
        print(
            f"{item['id']} {status} {latency}s brand_mentioned={mentioned} "
            f"model={returned_model or 'n/a'}",
            flush=True,
        )
        if pause:
            time.sleep(pause)

    ended = datetime.now(timezone.utc)
    summary = summarize_run(rows, competitors)
    returned_models = sorted({row.get("returned_model") or "" for row in rows if row.get("returned_model")})
    payload = {
        "measured_at_utc": started.isoformat(),
        "finished_at_utc": ended.isoformat(),
        "limitations": (
            "This run queried only the local LiteLLM route (default model free-chat). "
            "It is not a measurement of ChatGPT, Gemini, Perplexity, or other consumer "
            "AI search engines. Mention and citation flags are string matches in the "
            "model text; cited URLs are not fetched or verified here."
        ),
        "api_base": api_base,
        "requested_model": model,
        "returned_models": returned_models,
        "brand": brand,
        "competitors": [
            {"name": c["name"], "source_url": c.get("source_url"), "domains": c.get("domains")}
            for c in competitors
        ],
        "summary": summary,
        "questions": rows,
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = started.astimezone().strftime("%Y-%m-%d")
    brand_slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in brand.get("name", "brand")).strip("-")
    json_path = out_dir / f"run-{stamp}-{brand_slug}.json"
    csv_path = out_dir / f"run-{stamp}-{brand_slug}.csv"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fieldnames = list(flatten_row(rows[0]).keys()) if rows else []
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(flatten_row(row))
    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    print("summary:", json.dumps(summary, ensure_ascii=False))
    return json_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure brand mentions in one LiteLLM model.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    run(args.config, args.out)


if __name__ == "__main__":
    main()
