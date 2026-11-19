#!/usr/bin/env python3
"""Find occurrences of a phrase in checked SRT captions and propose clip intervals."""

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

from check_short_captions import milliseconds, validate


def find_candidates(srt_path, video_path, phrase, context_seconds):
    if not phrase.strip():
        raise ValueError("search phrase is empty")
    if not math.isfinite(context_seconds) or context_seconds < 0:
        raise ValueError("context must be a finite non-negative number")

    _, duration_ms = validate(srt_path, video_path)
    content = srt_path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
    transcript = ""
    spans = []
    for block in re.split(r"\n\s*\n", content):
        lines = block.splitlines()
        start_text, end_text = lines[1].split("-->", 1)
        cue_text = " ".join(" ".join(lines[2:]).split()).casefold()
        if transcript:
            transcript += " "
        start_index = len(transcript)
        transcript += cue_text
        spans.append((start_index, len(transcript), milliseconds(start_text), milliseconds(end_text)))

    query = " ".join(phrase.split()).casefold()
    context_ms = round(context_seconds * 1000)
    candidates = []
    for match in re.finditer(re.escape(query), transcript):
        matching_cues = [span for span in spans if span[0] < match.end() and span[1] > match.start()]
        start_ms = matching_cues[0][2]
        end_ms = matching_cues[-1][3]
        candidates.append({
            "match_start_ms": start_ms,
            "match_end_ms": end_ms,
            "clip_start_ms": max(0, start_ms - context_ms),
            "clip_end_ms": min(duration_ms, end_ms + context_ms),
        })
    return candidates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("srt", type=Path)
    parser.add_argument("video", type=Path)
    parser.add_argument("--phrase", required=True)
    parser.add_argument("--context-seconds", type=float, default=5)
    args = parser.parse_args()
    try:
        candidates = find_candidates(args.srt, args.video, args.phrase, args.context_seconds)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"FAILED: {error}", file=sys.stderr)
        return 2
    print(json.dumps(candidates, ensure_ascii=False, indent=2))
    return 0 if candidates else 1


if __name__ == "__main__":
    sys.exit(main())
