"""Create timestamped contact sheets from local videos for visual research review."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--columns", type=int, default=5)
    parser.add_argument("--rows", type=int, default=5)
    parser.add_argument("--width", type=int, default=480)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for video in sorted(args.input_dir.glob("*.mp4")):
        capture = cv2.VideoCapture(str(video))
        fps = capture.get(cv2.CAP_PROP_FPS) or 30.0
        total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total / fps
        frames = []
        timestamp = 0.0
        while timestamp <= duration:
            capture.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
            ok, frame = capture.read()
            if not ok:
                break
            height, width = frame.shape[:2]
            target_height = round(height * args.width / width)
            frame = cv2.resize(frame, (args.width, target_height))
            label = f"{int(timestamp) // 60:02d}:{int(timestamp) % 60:02d}"
            cv2.rectangle(frame, (0, 0), (92, 31), (0, 0, 0), -1)
            cv2.putText(frame, label, (7, 23), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            frames.append(frame)
            timestamp += args.interval
        capture.release()

        page_size = args.columns * args.rows
        blank = frames[0] * 0 if frames else None
        for page, start in enumerate(range(0, len(frames), page_size), 1):
            page_frames = frames[start : start + page_size]
            page_frames.extend([blank] * (page_size - len(page_frames)))
            rows = [cv2.hconcat(page_frames[i : i + args.columns]) for i in range(0, page_size, args.columns)]
            sheet = cv2.vconcat(rows)
            cv2.imwrite(str(args.output_dir / f"{video.stem}_sheet_{page:02d}.jpg"), sheet, [cv2.IMWRITE_JPEG_QUALITY, 90])


if __name__ == "__main__":
    main()
