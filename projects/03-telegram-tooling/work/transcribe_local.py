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
for segment in segments:
    print(f"{segment.start:.2f}–{segment.end:.2f} {segment.text.strip()}")
