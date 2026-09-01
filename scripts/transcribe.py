#!/usr/bin/env python3
"""Transcribe all audio in data/audio/ to data/transcripts/<id>.txt.

Resumable: skips videos whose transcript already exists and is non-empty.
Skips videos marked group="excluded" in data/playlist.json.
Uses mlx-whisper (Apple Silicon) with whisper-large-v3-turbo.
"""
import json
import sys
import time
from pathlib import Path

import mlx_whisper

AUDIO_DIR = Path("data/audio")
OUT_DIR = Path("data/transcripts")
PLAYLIST = Path("data/playlist.json")
MODEL = "mlx-community/whisper-large-v3-turbo"
# LANGUAGE decided by the pre-batch probe (zh vs yue on the shortest video).
LANGUAGE = "zh"
PROMPT = ("以下是中文的外匯、黃金與指數交易教學影片，講者是全職交易員交易倫，"
          "內容包括 ICT、聰明錢、流動性 Liquidity、Order Block、公允價值缺口 FVG、"
          "Kill Zone、OTE 入場模型、多時間框架分析、價格行為、破位交易、"
          "供應需求、FTMO 資金盤挑戰、止損止盈、盈虧比、回測。")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    excluded = {v["id"] for v in json.loads(PLAYLIST.read_text(encoding="utf-8"))
                if v["group"] == "excluded"}
    audio_files = sorted(AUDIO_DIR.glob("*.m4a")) + sorted(AUDIO_DIR.glob("*.webm"))
    audio_files = [p for p in audio_files if p.stem not in excluded]
    if not audio_files:
        print("ERROR: no audio files in", AUDIO_DIR)
        return 1

    # Smallest files first so early failures surface fast and progress is visible
    audio_files.sort(key=lambda p: p.stat().st_size)

    for i, audio in enumerate(audio_files, 1):
        vid = audio.stem
        out = OUT_DIR / f"{vid}.txt"
        if out.exists() and out.stat().st_size > 0:
            print(f"[{i}/{len(audio_files)}] {vid}: skip (exists)", flush=True)
            continue
        t0 = time.time()
        print(f"[{i}/{len(audio_files)}] {vid}: transcribing "
              f"({audio.stat().st_size / 1e6:.1f} MB)...", flush=True)
        try:
            result = mlx_whisper.transcribe(
                str(audio),
                path_or_hf_repo=MODEL,
                language=LANGUAGE,
                initial_prompt=PROMPT,
            )
        except Exception as e:  # keep pipeline going; integrity check catches gaps
            print(f"[{i}/{len(audio_files)}] {vid}: FAILED {e!r}", flush=True)
            continue
        segments = result.get("segments", [])
        lines = [seg["text"].strip() for seg in segments if seg["text"].strip()]
        out.write_text("\n".join(lines), encoding="utf-8")
        dt = time.time() - t0
        print(f"[{i}/{len(audio_files)}] {vid}: done {len(lines)} lines, "
              f"{out.stat().st_size} bytes, {dt:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
