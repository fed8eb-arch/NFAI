#!/usr/bin/env python3
"""Transcribe a local audio or video file with faster-whisper on CPU."""
import argparse
import subprocess

import numpy as np
from faster_whisper import WhisperModel

parser = argparse.ArgumentParser()
parser.add_argument("audio")
parser.add_argument("--model", required=True)
parser.add_argument("--language", default="ru")
parser.add_argument("--srt-output", help="write SRT captions to a new file")
parser.add_argument("--word-captions", action="store_true", help="write one subtitle cue per recognized word")
args = parser.parse_args()
if args.word_captions and not args.srt_output:
    parser.error("--word-captions requires --srt-output")

raw = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", args.audio, "-f", "s16le",
     "-ac", "1", "-ar", "16000", "pipe:1"],
    check=True,
    capture_output=True,
).stdout
audio = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=4)
segments, _ = model.transcribe(audio, language=args.language, beam_size=1,
                               word_timestamps=args.word_captions)


def srt_time(seconds):
    total_ms = round(seconds * 1000)
    hours, remainder = divmod(total_ms, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


if args.srt_output:
    captions = []
    if args.word_captions:
        cues = (word for segment in segments for word in segment.words)
    else:
        cues = segments
    previous_end_ms = 0
    for cue in cues:
        text = (cue.word if args.word_captions else cue.text).strip()
        start_ms = round(cue.start * 1000)
        end_ms = round(cue.end * 1000)
        if args.word_captions:
            start_ms = max(start_ms, previous_end_ms)
            if not text or end_ms <= start_ms:
                continue
        captions.append(
            f"{len(captions) + 1}\n{srt_time(start_ms / 1000)} --> "
            f"{srt_time(end_ms / 1000)}\n{text}\n\n"
        )
        previous_end_ms = end_ms
    with open(args.srt_output, "x", encoding="utf-8") as output:
        output.writelines(captions)
else:
    for segment in segments:
        print(f"{segment.start:.2f}–{segment.end:.2f} {segment.text.strip()}")
