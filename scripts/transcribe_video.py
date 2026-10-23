"""Transcribe a local research video to timestamped text on stdout."""

from __future__ import annotations

import argparse

from faster_whisper import WhisperModel


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--model", default="small")
    parser.add_argument("--language", default="zh")
    args = parser.parse_args()

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(
        args.video,
        language=args.language,
        vad_filter=True,
        beam_size=5,
    )
    for segment in segments:
        text = segment.text.strip()
        print(f"[{segment.start:07.2f}-{segment.end:07.2f}] {text}", flush=True)


if __name__ == "__main__":
    main()
