#!/usr/bin/env python3
"""Retimestamp a UTF-8 SRT file for a selected clip of the source video."""
import argparse
import re
import sys
from pathlib import Path

from check_short_captions import milliseconds


def timestamp(value):
    hours, value = divmod(value, 3600000)
    minutes, value = divmod(value, 60000)
    seconds, millis = divmod(value, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def clip_captions(source, clip_start, clip_end):
    content = source.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
    if not content:
        raise ValueError("subtitle file is empty")
    result = []
    previous_end = 0
    for block in re.split(r"\n\s*\n", content):
        lines = block.splitlines()
        if len(lines) < 3 or not lines[0].strip().isdigit() or "-->" not in lines[1]:
            raise ValueError(f"invalid subtitle block: {block[:60]}")
        start_text, end_text = lines[1].split("-->", 1)
        start, end = milliseconds(start_text), milliseconds(end_text)
        if start >= end or start < previous_end:
            raise ValueError(f"invalid or overlapping interval in cue {lines[0]}")
        if not any(line.strip() for line in lines[2:]):
            raise ValueError(f"cue {lines[0]} has no text")
        previous_end = end
        start = max(start, clip_start)
        end = min(end, clip_end)
        if start < end:
            result.append((start - clip_start, end - clip_start, "\n".join(lines[2:])))
    if not result:
        raise ValueError("no subtitle cues in selected clip")
    return "".join(
        f"{number}\n{timestamp(start)} --> {timestamp(end)}\n{text}\n\n"
        for number, (start, end, text) in enumerate(result, 1)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--start", required=True, help="clip start in SRT timestamp format")
    parser.add_argument("--end", required=True, help="clip end in SRT timestamp format")
    args = parser.parse_args()
    try:
        start, end = milliseconds(args.start), milliseconds(args.end)
        if start >= end:
            raise ValueError("clip end must be after clip start")
        content = clip_captions(args.source, start, end)
        with args.destination.open("x", encoding="utf-8", newline="\n") as output:
            output.write(content)
    except (OSError, ValueError) as error:
        print(f"FAILED: {error}", file=sys.stderr)
        return 1
    print(f"OK: wrote {args.destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
