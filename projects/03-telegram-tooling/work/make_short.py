#!/usr/bin/env python3
"""Create a captioned vertical clip from checked subtitles and a search phrase."""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from check_short_captions import validate
from clip_captions import clip_captions
from find_clip_candidates import find_candidates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("captions", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--phrase", required=True)
    parser.add_argument("--context-seconds", type=float, default=5)
    parser.add_argument("--match", type=int, default=1, help="1-based matching occurrence")
    args = parser.parse_args()
    try:
        video = args.video.resolve(strict=True)
        captions = args.captions.resolve(strict=True)
        output_dir = args.output_dir.absolute()
        if args.match < 1:
            raise ValueError("match must be at least 1")
        candidates = find_candidates(captions, video, args.phrase, args.context_seconds)
        if args.match > len(candidates):
            raise ValueError(f"match {args.match} unavailable; found {len(candidates)}")
        selected = candidates[args.match - 1]
        start, end = selected["clip_start_ms"], selected["clip_end_ms"]
        result = clip_captions(captions, start, end)
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".nfai-short-", dir=output_dir.parent) as temp:
            temp_dir = Path(temp)
            (temp_dir / "captions.srt").write_text(result, encoding="utf-8")
            subprocess.run([
                "ffmpeg", "-nostdin", "-v", "error", "-n", "-ss", f"{start / 1000:.3f}",
                "-i", str(video), "-t", f"{(end - start) / 1000:.3f}", "-map", "0:v:0",
                "-map", "0:a?", "-vf",
                "scale=360:640:force_original_aspect_ratio=increase,crop=360:640,setsar=1,subtitles=captions.srt",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", "clip.mp4",
            ], cwd=temp_dir, check=True)
            count, duration = validate(temp_dir / "captions.srt", temp_dir / "clip.mp4")
            # Reserving the directory ensures existing results are never overwritten.
            output_dir.mkdir()
            try:
                os.replace(temp_dir / "captions.srt", output_dir / "captions.srt")
                os.replace(temp_dir / "clip.mp4", output_dir / "clip.mp4")
            except OSError:
                shutil.rmtree(output_dir)
                raise
        print(f"OK: {count} cues, {duration / 1000:.3f}s; clip {start / 1000:.3f}–{end / 1000:.3f}s")
        print("Review the subtitles against audio, especially cues cut at clip boundaries.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"FAILED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
