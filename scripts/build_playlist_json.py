#!/usr/bin/env python3
"""Build data/playlist.json from data/playlist_meta.txt with topic groups.

Group "excluded" = low-signal videos (biographies, desk tour, tool tutorial,
meditation, day-in-life, motivational) that are neither downloaded nor
transcribed. This file is the single source of truth for the exclusion list.
"""
import json
from pathlib import Path

GROUPS = {
    "ict_core": [  # ICT/聰明錢核心概念：流動性、PD Array、Kill Zone、入場模型
        "yZoSW3DGRGI", "xwsyfVf2l0k", "Q371XdV3apE", "3Kt_ruGepB4",
        "CJi1ltRQnys", "7dDW8tF1cZo", "E0PF_0XLDGo", "whJg0lgPbFo",
        "tCfmxMX5WaU", "ofQ--jkHTm4", "_TEaFyv7-ac", "aSZzhnfOVkE",
        "RjNBnZ59c4U",
    ],
    "price_action": [  # 價格行為/破位/形態/動能/多時框策略
        "JtPN1rBq5h0", "QZNzq-BunA4", "zgVlK7UBNTY", "fTRv2HhTJUk",
        "7yDxPi7Roh0", "qWMKL-p1MPE", "GINdJCIIEvw", "WmW5fQjK5Qg",
        "hmpAys3lJEo", "kI5idYixD50", "fLN20X1dP48", "YeGLUuh3eCg",
        "6_5DVT6uS9E", "teVdcguZs_U", "VjSB-VRyxWI", "pK6S7CEqMAk",
        "OANImZtkkeM", "rdXofMdxNEQ", "B7rumsOw6_U",
    ],
    "method": [  # 交易方法論：多系統框架、回測
        "PypFn7GaVfE", "RdnJw-mhwlE",
    ],
    "risk_management": [  # 止損止盈、資金管理、常見錯誤
        "hkCvRoLc3Nk", "k0ESC6XYz50", "48pCaOfGGmA", "T2Nk46EqAh4",
        "s4on4yJCLII",
    ],
    "prop_firm": [  # 資金盤挑戰、帳戶增長藍圖、績效回顧
        "xmHaONnNrCw", "nzZ5oqmLjhM", "91Hpt_LyJSE", "rE21_onS0uo",
        "7j7_mhfda38", "mDpbsw81ftI", "MjPZizFnX-E",
    ],
    "psychology_habits": [  # 交易心理、習慣、教訓
        "54WCm_VBYfY", "HeQiNekCZng", "eIeYQStY5rI", "oiULdfvMlYY",
        "ryv0CUgVZCM", "OnjOO0QyVUU", "rLP-MPvGmDE", "oiMlx5UlRLQ",
        "H3OZxavXlsk", "jlO3771JF1E", "0a4NrcfAPJU",
    ],
    "excluded": [  # 低訊號：傳記×4、Desk Tour、TradingView 教學、冥想、日常、勵志
        "kSJRzrZE6E8", "Cpn7fBwmLzE", "Zqq0HJJAffk", "N9TmkW8x2gs",
        "GZPC9J7RIWo", "NqixhiGBt9E", "X07s48_tn40", "VTnY5yGAc7M",
        "BThilOfKSGQ",
    ],
}
GROUP_OF = {vid: g for g, vids in GROUPS.items() for vid in vids}

rows = []
for line in Path("data/playlist_meta.txt").read_text().splitlines():
    # Titles may themselves contain "|": id is the first field, the last three
    # are date/duration/views, and the title is everything in between.
    parts = line.split("|")
    vid, upload_date, duration, views = parts[0], *parts[-3:]
    title = "|".join(parts[1:-3])
    rows.append({
        "id": vid,
        "title": " ".join(title.split()),
        "upload_date": upload_date,
        "duration_sec": int(duration),
        "view_count": int(views),
        "group": GROUP_OF.get(vid, "ungrouped"),
    })

rows.sort(key=lambda r: r["upload_date"])
Path("data/playlist.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

ungrouped = [r["id"] for r in rows if r["group"] == "ungrouped"]
core = [r for r in rows if r["group"] not in ("ungrouped", "excluded")]
total_h = sum(r["duration_sec"] for r in core) / 3600
print(f"{len(rows)} videos, core: {len(core)} ({total_h:.1f}h), "
      f"excluded: {len(rows) - len(core) - len(ungrouped)}, "
      f"ungrouped: {ungrouped or 'none'}")
