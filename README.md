# LunTrading — 交易倫 YouTube 頻道蒸餾專案

將 [@LunTrading](https://www.youtube.com/@LunTrading)（交易倫 Alan，全職交易員、World Trading Tournament 亞軍）嘅 57 條核心教學影片，蒸餾成 **11 個 Claude Code Agent Skills ＋ 1 個 subagent**。

同前例 [Drmarkyang](../Drmarkyang) 嘅關鍵分別：知識唔再 inline 喺 agent md，而係**逐一（one by one）生成為獨立 skills**，每個經自動雙軸審查 gate（≥90 分）先算通過；agent md 保持精簡（persona＋決策框架＋skill 路由表），符合 Claude Code subagent 公開規範。

## 核心交付物

| 交付物 | 位置 | 審查分數 |
|---|---|---|
| `lun-ict-pd-arrays` | `.claude/skills/` | 90（auto 80 / LLM 96） |
| `lun-price-action-toolkit` | `.claude/skills/` | 90（auto 80 / LLM 96） |
| `lun-liquidity-analysis` | `.claude/skills/` | 90（auto 80 / LLM 96，first pass） |
| `lun-kill-zones-timing` | `.claude/skills/` | 90（auto 80 / LLM 96，first pass） |
| `lun-multi-timeframe-analysis` | `.claude/skills/` | 90（auto 80 / LLM 96，first pass） |
| `lun-ote-entry-model` | `.claude/skills/` | 91（auto 80 / LLM 97，first pass） |
| `lun-exit-management` | `.claude/skills/` | 90（auto 80 / LLM 96，first pass） |
| `lun-backtesting-method` | `.claude/skills/` | 90（auto 80 / LLM 96，first pass） |
| `lun-prop-firm-playbook` | `.claude/skills/` | 90（auto 80 / LLM 96） |
| `lun-risk-management` | `.claude/skills/` | 90（auto 80 / LLM 96） |
| `lun-trading-psychology` | `.claude/skills/` | 91（auto 80 / LLM 97） |
| `lun-trading` agent | `.claude/agents/lun-trading.md` | spec 驗證＋golden run |

每個 skill：`SKILL.md`（Agent Skills 規範 frontmatter：name + description）＋ `references/evidence.md`（全量 verbatim 引文證據，附 video id 同 "(transcript)" 覆核標記）。審查工具：[dual-axis-skill-reviewer](~/.claude/skills/dual-axis-skill-reviewer)，knowledge_only 權重 0.35 auto / 0.65 LLM（理據見 `docs/team_design.md` §3.4），閘門 ≥90，author 同 reviewer 必須係唔同 agent 實例。

## 資料管線（可重跑）

```
scripts/fetch_meta.sh          # 頻道 metadata → data/playlist_meta.txt
scripts/build_playlist_json.py # 人工分群（66 → 57 core + 9 excluded）→ data/playlist.json
scripts/run_pipeline.sh        # yt-dlp 下載 m4a → mlx-whisper 轉錄（resumable）
scripts/check_integrity.py     # 完整性 gate
scripts/check_quotes.py        # 筆記引文 verbatim 驗證 gate
```

- ASR：`mlx-community/whisper-large-v3-turbo`，`language="zh"`（語言探測：講者為華語（馬來西亞口音），zh 優於 yue），M1 上 ~5x realtime。
- 排除 9 條低訊號影片：4 條交易員傳記、Desk Tour、TradingView 教學、冥想練習、日常 vlog、勵志清單。

## 資料完整性（實際輸出）

```
core videos: 57  ok: 57  missing: 0  empty: 0  suspicious: 0
total transcript chars (ok files): 335,622
```

筆記層：57 份結構化筆記（`analysis/video_notes/`），全部通過 `check_quotes.py`（每個「」引文 verbatim 對應逐字稿）＋ 兩輪抽樣稽核（Wave 1: 5/5 PASS 321/321 引文；跨分群 7 篇：7/7 PASS，0 捏造）。

## 方法論（四階段漏斗）

1. **管線**：metadata → 下載 → ASR → 完整性 gate（硬性檢查點）
2. **筆記**：15 個並行 note-writer agents，逐片一份筆記，反幻覺模板（未提及唔腦補、引文 verbatim）＋抽樣稽核
3. **綜合**：57 筆記 → `analysis/lun_trading_profile.md`（人物、思維習性、ASR 容錯對照表、skill 分解圖連證據密度）
4. **Skills 逐一生成**：嚴格順序（詞彙地基先行、跨切面殿後），每個 skill 經獨立 reviewer 雙軸審查 ≥90 先開始下一個；`analysis/skill_boundary_ledger.md` 記錄每個通過 skill 嘅邊界，保證 DRY

團隊設計（agent-organizer 產出）：`docs/team_design.md`。研究文檔：`docs/research.md`。

## 使用

```bash
# 喺任何 project 用（已安裝到 global）
# subagent：Claude Code 內 "use the lun-trading agent to ..."
# skills：/lun-ict-pd-arrays 等，或由 lun-trading agent 自動路由
```

Agent 驗證樣本（golden run）：`analysis/agent_verification_sample.md`。

## 目錄結構

```
.claude/agents/lun-trading.md    # subagent（精簡核心＋路由表）
.claude/skills/lun-*/            # 11 個 skills（SKILL.md + references/evidence.md）
analysis/video_notes/<id>.md     # 57 份逐片筆記（證據層）
analysis/lun_trading_profile.md  # 綜合檔案（研究文檔本體）
analysis/skill_boundary_ledger.md# skill 邊界帳（DRY 契約）
analysis/NOTE_TEMPLATE.md        # 筆記模板（反幻覺規則）
data/transcripts/<id>.txt        # 57 份 ASR 逐字稿
data/playlist.json               # 影片清單＋分群（exclusion source of truth）
docs/team_design.md              # agent-organizer 團隊設計
docs/research.md                 # 方法論研究文檔
reports/                         # 全部審查報告（審計軌跡）
scripts/                         # 可重跑管線
```

## 侷限聲明

- **ASR 來源**：全部知識出自機器逐字稿，有系統性誤字（對照表見 profile §5）；引文照錄原文。
- **示範參數非驗證統計**：影片中嘅盈虧比/勝率/時段參數係教學樣本，使用前必須自行回測校準。
- **付費內容邊界**：動能回流完整規則、100 筆挑戰細節等明示留喺付費班，skills 只錄公開骨架，唔准補完。
- **推廣合作**：Axi Select 相關內容係贊助導流，相關規則帶【推廣合作】標記且有時效性。
- **口徑矛盾照錄**：風險% 三口徑、confluence 2-3/3-5、RR 門檻分層等，全部平行呈現唔裁決。
- 蒸餾日期：2026-09-02/03；影片範圍 2023-07-20 至 2026-08-28。

## 來源與版權聲明

本專案嘅所有知識內容蒸餾自 [@LunTrading](https://www.youtube.com/@LunTrading)（交易倫 Alan）公開發佈嘅 YouTube 教學影片。版權屬原作者所有。

- `data/transcripts/` 係機器轉錄（ASR）嘅逐字稿，`analysis/` 同 `.claude/skills/*/references/` 含逐字引文，一律用於**研究、學習與方法論示範**目的，並全程標註來源 video id 以便追溯原片。
- 本倉庫**唔係**原作者授權或背書嘅產物，亦唔包含佢付費課程嘅內容（corpus 中明示留喺付費班嘅規則已明確標記為未公開且禁止補完）。
- 所有交易規則、參數、盈虧比同勝率數字均為影片教學示範，**唔構成投資建議**；實際使用前必須自行回測驗證。
- 如原作者希望移除本倉庫任何內容，請開 issue，我會即時處理。
