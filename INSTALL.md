# 安裝指南

本倉庫同時係一個 **Claude Code plugin** 同埋佢自己嘅 **marketplace**，所以唔使手動 copy 檔案。

交付內容：11 個 skills（`skills/`）＋ 1 個 subagent（`agents/lun-trading.md`）。

---

## 方法一：Plugin 安裝（建議）

喺 Claude Code 入面執行：

```
/plugin marketplace add kc-lui/LunTrading
/plugin install lun-trading@luntrading
```

完成後重開 session。驗證：

```
/plugin                      # 應見 lun-trading 已安裝
```

更新到最新版：

```
/plugin marketplace update luntrading
```

移除：

```
/plugin uninstall lun-trading@luntrading
/plugin marketplace remove luntrading
```

### 用 CLI 安裝（唔入互動模式）

```bash
claude plugin marketplace add kc-lui/LunTrading
claude plugin install lun-trading@luntrading
```

---

## 方法二：手動安裝到全域

適合想自行改內容、或者唔想經 plugin 系統嘅人。

```bash
git clone https://github.com/kc-lui/LunTrading.git
cd LunTrading

mkdir -p ~/.claude/skills ~/.claude/agents
cp -R skills/lun-* ~/.claude/skills/
cp agents/lun-trading.md ~/.claude/agents/
```

想跟住上游更新，用 symlink 代替 copy：

```bash
for d in "$PWD"/skills/lun-*; do ln -sfn "$d" ~/.claude/skills/; done
ln -sfn "$PWD/agents/lun-trading.md" ~/.claude/agents/lun-trading.md
```

之後 `git pull` 就自動生效。

---

## 方法三：淨係喺單一專案用

```bash
cd /path/to/your-project
mkdir -p .claude
git clone https://github.com/kc-lui/LunTrading.git /tmp/luntrading
cp -R /tmp/luntrading/skills .claude/skills
cp -R /tmp/luntrading/agents .claude/agents
```

`.claude/skills/` 同 `.claude/agents/` 只會喺該專案生效。

---

## 驗證安裝

重開 Claude Code session 後：

```
# 1. Subagent 應該出現
用 lun-trading agent 分析：黃金日線上升趨勢、4小時回調緊，紐約時段點搵多單位？

# 2. 單一 skill 直接調用
/lun-liquidity-analysis
```

Agent 正常運作嘅話，會按決策框架逐層調用對應 skill（時段 → 多時框 → 流動性 → PD Array → 入場 → 出場風控），輸出分五段：結論／分層分析／矛盾與口徑／風控與失效條件／侷限。

超綱問題（例如頻道冇教嘅加密長線囤幣）佢應該直接講「頻道未教」而唔係作嘢 — 呢個係刻意設計嘅行為，見 `analysis/agent_verification_sample.md`。

---

## 系統需求

- **安裝同使用 skills / agent**：淨係要 Claude Code，冇其他依賴（全部係 Markdown 知識檔，無 scripts、無 MCP server、無 API key）。
- **重跑資料管線**（只有想自己由頻道重新蒸餾先需要）：Python 3.9+、`yt-dlp`、`mlx-whisper`（Apple Silicon）、`static-ffmpeg`。見 README「資料管線」一節。

---

## 常見問題

**Q：安裝完 `/lun-*` 冇反應？**
重開 session。Plugin 同 skills 喺 session 啟動時載入。

**Q：Plugin 版同手動版會唔會撞？**
會。如果 `~/.claude/skills/lun-*` 已經有手動裝嘅版本，再裝 plugin 會有兩份。揀一種，刪另一種。

**Q：Skills 入面提到嘅 `analysis/…`、`data/transcripts/…` 路徑點樣解？**
嗰啲係指返本倉庫嘅證據層（逐片筆記同逐字稿），俾你追溯每條規則嘅原始出處。安裝到全域之後嗰啲檔案唔會跟住過去；skill 本身自帶 `references/evidence.md`，已經包含全部 verbatim 引文，唔影響使用。想要完整證據鏈就 clone 本倉庫。

**Q：可唔可以淨係裝其中幾個 skill？**
可以，用方法二手動 copy 你要嘅 `skills/lun-xxx` 就得。但留意 skills 之間有 DRY 邊界（例如 `lun-ote-entry-model` 唔重複定義 PD Array，會轉介 `lun-ict-pd-arrays`），邊界關係見 `analysis/skill_boundary_ledger.md`。
