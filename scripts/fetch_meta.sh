#!/bin/zsh
# Fetch per-video metadata for the whole channel into data/playlist_meta.txt.
set -u
cd "$(dirname "$0")/.."

CHANNEL="https://www.youtube.com/@LunTrading/videos"

.venv/bin/yt-dlp --js-runtimes node --skip-download --ignore-errors \
  --sleep-requests 1.0 \
  --print "%(id)s|%(title)s|%(upload_date)s|%(duration)s|%(view_count)s" \
  "$CHANNEL" > data/playlist_meta.txt

echo "videos: $(wc -l < data/playlist_meta.txt)"
