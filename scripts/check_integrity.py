#!/usr/bin/env python3
"""Data integrity check: every core (non-excluded) video has a sane transcript.

Checks: file exists, non-empty, chars-per-second ratio within plausible range
for Mandarin speech (flag < 1.0 c/s as suspicious — silence, music, or failed ASR).
"""
import json
import sys
from pathlib import Path

PLAYLIST = Path("data/playlist.json")
TRANSCRIPTS = Path("data/transcripts")

videos = [v for v in json.loads(PLAYLIST.read_text(encoding="utf-8"))
          if v["group"] != "excluded"]
missing, empty, suspicious, ok = [], [], [], []

for v in videos:
    vid, dur = v["id"], v["duration_sec"]
    f = TRANSCRIPTS / f"{vid}.txt"
    if not f.exists():
        missing.append(vid)
        continue
    n = len(f.read_text(encoding="utf-8").replace("\n", ""))
    if n == 0:
        empty.append(vid)
    elif n / dur < 1.0:
        suspicious.append((vid, n, dur, round(n / dur, 2)))
    else:
        ok.append((vid, n, dur))

print(f"core videos: {len(videos)}  ok: {len(ok)}  missing: {len(missing)}  "
      f"empty: {len(empty)}  suspicious: {len(suspicious)}")
for vid in missing:
    print(f"  MISSING    {vid}")
for vid in empty:
    print(f"  EMPTY      {vid}")
for vid, n, dur, r in suspicious:
    print(f"  SUSPICIOUS {vid}: {n} chars / {dur}s = {r} c/s")

total_chars = sum(n for _, n, _ in ok)
print(f"total transcript chars (ok files): {total_chars:,}")
sys.exit(0 if not missing and not empty else 1)
