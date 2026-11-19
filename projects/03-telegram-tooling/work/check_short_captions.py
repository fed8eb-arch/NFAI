#!/usr/bin/env python3
"""Check an SRT subtitle file against a finished video using ffprobe."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TIME = re.compile(r'^(\d{2,}):(\d{2}):(\d{2}),(\d{3})$')


def milliseconds(value):
    match = TIME.fullmatch(value.strip())
    if not match:
        raise ValueError(f'invalid timestamp: {value}')
    hours, minutes, seconds, millis = map(int, match.groups())
    if minutes >= 60 or seconds >= 60:
        raise ValueError(f'invalid timestamp: {value}')
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis


def validate(srt_path, video_path):
    probe = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(video_path)],
        text=True, capture_output=True, check=True,
    )
    duration = round(float(json.loads(probe.stdout)['format']['duration']) * 1000)
    content = srt_path.read_text(encoding='utf-8-sig').replace('\r\n', '\n').strip()
    if not content:
        raise ValueError('subtitle file is empty')
    previous_end = 0
    count = 0
    for block in re.split(r'\n\s*\n', content):
        lines = block.splitlines()
        if len(lines) < 3 or not lines[0].strip().isdigit() or '-->' not in lines[1]:
            raise ValueError(f'invalid subtitle block: {block[:60]}')
        start_text, end_text = lines[1].split('-->', 1)
        start, end = milliseconds(start_text), milliseconds(end_text)
        if start >= end:
            raise ValueError(f'cue {lines[0]} has non-positive duration')
        if start < previous_end:
            raise ValueError(f'cue {lines[0]} overlaps the preceding cue')
        if end > duration:
            raise ValueError(f'cue {lines[0]} ends after the video')
        if not any(line.strip() for line in lines[2:]):
            raise ValueError(f'cue {lines[0]} has no text')
        previous_end = end
        count += 1
    return count, duration


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('srt', type=Path)
    parser.add_argument('video', type=Path)
    args = parser.parse_args()
    try:
        count, duration = validate(args.srt, args.video)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f'FAILED: {error}', file=sys.stderr)
        return 1
    print(f'OK: {count} cues, video duration {duration / 1000:.3f}s')
    return 0


if __name__ == '__main__':
    sys.exit(main())
