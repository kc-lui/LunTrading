#!/usr/bin/env python3
"""Verify every 「」-quoted phrase in video notes exists verbatim in its transcript.

Whitespace/newlines are stripped from both sides before matching, so quotes may
join transcript lines. 「」 is reserved for verbatim transcript text; writer
annotations belong outside the brackets.
"""
import re
import sys
from pathlib import Path

WHITELIST = {"未提及", "本片僅預告，未教"}


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


def main() -> int:
    failed_notes = 0
    for note in sorted(Path("analysis/video_notes").glob("*.md")):
        txt_path = Path(f"data/transcripts/{note.stem}.txt")
        if not txt_path.exists():
            print(f"{note.stem}: NO TRANSCRIPT")
            failed_notes += 1
            continue
        transcript = norm(txt_path.read_text(encoding="utf-8"))
        quotes = re.findall(r"「([^」]+)」", note.read_text(encoding="utf-8"))
        fails = [q for q in quotes
                 if norm(q) not in transcript and q not in WHITELIST
                 and len(norm(q)) > 2]
        if fails:
            failed_notes += 1
            print(f"{note.stem}: {len(fails)}/{len(quotes)} quotes FAILED")
            for f in fails:
                print(f"   ✗ {f[:80]}")
    if failed_notes == 0:
        print("ALL NOTES CLEAN")
    return 1 if failed_notes else 0


if __name__ == "__main__":
    sys.exit(main())
