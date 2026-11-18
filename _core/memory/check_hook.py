"""Report memory graph validation failures after a Claude Code edit."""
import json
import os
from pathlib import Path
import sys

from query import ROOT, load_graph


def main():
    event = json.load(sys.stdin)
    tool_input = event.get("tool_input", {})
    name = tool_input.get("file_path")
    if not isinstance(name, str):
        return
    cwd = Path(event.get("cwd") or os.getcwd())
    edited = (cwd / name).resolve()
    if edited != ROOT / "_core/memory/graph.json":
        return
    try:
        nodes, edges = load_graph()
        message = f"NFAI memory graph validated: {len(nodes)} nodes and {len(edges)} edges."
    except (OSError, ValueError, KeyError, TypeError) as exc:
        message = f"NFAI memory graph failed validation: {exc}. Repair it before committing."
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": message,
    }}))


if __name__ == "__main__":
    main()
