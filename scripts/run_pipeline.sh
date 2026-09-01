#!/bin/zsh
# Download core-video audio then transcribe. Resumable end-to-end.
# Requires data/playlist.json (run fetch_meta.sh + build_playlist_json.py first)
# — it is the source of truth for which videos are excluded.
set -u
cd "$(dirname "$0")/.."

FFDIR=$(.venv/bin/python -c "import static_ffmpeg.run as r; print(r.get_platform_dir())")
export PATH="$FFDIR:$PATH"

CORE_IDS=$(.venv/bin/python - <<'EOF'
import json
for v in json.load(open("data/playlist.json")):
    if v["group"] != "excluded":
        print(v["id"])
EOF
)

echo "=== Step 1: download audio ($(echo "$CORE_IDS" | wc -l | tr -d ' ') core videos) ==="
echo "$CORE_IDS" | .venv/bin/yt-dlp --js-runtimes node \
  -f "bestaudio[ext=m4a]/bestaudio" \
  --ignore-errors --no-overwrites \
  --sleep-requests 1.5 \
  --download-archive data/audio_archive.txt \
  -o "data/audio/%(id)s.%(ext)s" \
  --batch-file -
echo "audio files: $(ls data/audio | wc -l)"

echo "=== Step 2: transcribe ==="
.venv/bin/python scripts/transcribe.py
echo "=== pipeline done ==="
