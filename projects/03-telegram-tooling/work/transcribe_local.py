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
args = parser.parse_args()

raw = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", args.audio, "-f", "s16le",
     "-ac", "1", "-ar", "16000", "pipe:1"],
    check=True,
    capture_output=True,
).stdout
audio = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=4)
segments, _ = model.transcribe(audio, language=args.language, beam_size=1)
def srt_time(seconds):
    total_ms = round(seconds * 1000)
    hours, remainder = divmod(total_ms, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


if args.srt_output:
    captions = []
    for index, segment in enumerate(segments, 1):
        captions.append(
            f"{index}\n{srt_time(segment.start)} --> {srt_time(segment.end)}\n"
            f"{segment.text.strip()}\n\n"
        )
    with open(args.srt_output, "x", encoding="utf-8") as output:
        output.writelines(captions)
else:
    for segment in segments:
        print(f"{segment.start:.2f}–{segment.end:.2f} {segment.text.strip()}")
