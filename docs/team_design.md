# LunTrading Team Design：從逐字稿到 Skills + Subagent

> 目標交付物：9 個 `.claude/skills/<name>/SKILL.md`（逐一生成，每個經 dual-axis-skill-reviewer 把關 ≥90 分才生成下一個）＋ 1 個 `.claude/agents/lun-trading.md`（精簡人物設定＋決策框架＋skill routing table，深度知識放在 skills 裡）。
>
> 前例：`/Users/lui/workspace/Drmarkyang`（mark-yang-quant，33 部影片→單一 subagent，知識全部內嵌）。本專案的關鍵差異：57 部影片、知識拆分進 9 個 skills，subagent 只留 routing table，並多一層「逐一生成＋自動審查閘門」的循環。
>
> 本文件面向**執行方**（main session，具 Task tool 可 fan-out subagents）。所有角色都是 *main session 呼叫的 agent 類型*，不是新流程外的獨立系統。

---

## 0. 已確認的專案事實（設計依據）

- `analysis/NOTE_TEMPLATE.md` 已存在且已針對本專案調整過：分群欄位是 `ict_core / price_action / method / risk_management / prop_firm / psychology_habits`（6 類），Skill-cluster tags 欄位已預先列出 **9 個候選 skill 名稱**：
  `lun-ict-pd-arrays / lun-liquidity-analysis / lun-kill-zones-timing / lun-ote-entry-model / lun-price-action-toolkit / lun-risk-management / lun-prop-firm-playbook / lun-backtesting-method / lun-trading-psychology`。
  這 9 個名稱是 Phase 4 產出的「候選」，非鐵板——Phase 4 允許基於證據密度合併/新增/改名，但改動需在 profile 中寫明理由。
- Anti-hallucination 規則已寫死在模板：「沒有提到的欄位寫『未提及』，不要腦補。所有結論須可對應逐字稿內容。」——這是 Phase 3 QA 的檢查基準，不是建議，是硬性驗收條件。
- `scripts/check_integrity.py` 的通過條件：`missing == 0 and empty == 0`（exit code 0）；`chars/duration_sec < 1.0` 只標記為 `suspicious`（警告，不阻斷），但本設計把 suspicious 視為需人工確認才能進 Phase 3 的清單。
- `data/playlist.json` 是「哪些影片算 core」的 source of truth（`group != "excluded"`）；下游任何階段都不應重新判斷 excluded 與否。
- `dual-axis-skill-reviewer` 不是全自動黑盒：Step 1（腳本跑 auto-axis + 產生 LLM review prompt）→ Step 2（**需要一個 LLM/agent 讀 prompt 產出 review JSON**）→ Step 3（腳本合併 auto+LLM 兩軸，加權平均，預設 0.5/0.5）。所以審查閘門在本設計裡是「一個獨立 agent 實例扮演 reviewer 角色 + 跑腳本」，不是純腳本呼叫。

---

## 1. 團隊編制（Team Roster）

| # | 角色 | 執行的 agent 類型 | 輸入 | 輸出 | 驗收標準 |
|---|---|---|---|---|---|
| R1 | **Pipeline Operator**（Phase 1，進行中） | main session 直接跑既有 scripts（非 agent 委派，純腳本執行） | `data/playlist.json`, yt-dlp/mlx-whisper | `data/audio/<id>.m4a`, `data/transcripts/<id>.txt` | 見 R2 |
| R2 | **Integrity Gate** | main session 直接跑 `scripts/check_integrity.py` | `data/playlist.json`, `data/transcripts/*.txt` | 終端報告（ok/missing/empty/suspicious 計數） | `missing=0`, `empty=0`；`suspicious` 清單需人工聽前 60 秒確認後才放行進 Phase 3，否則該片標記 excluded 並記錄理由 |
| R3 | **Note Writer**（批次並行） | `general-purpose` subagent，波次 fan-out | 一批 3–4 部 `data/transcripts/<id>.txt` + `data/playlist.json`（取 title/upload_date）+ `analysis/NOTE_TEMPLATE.md` | 每部影片一份 `analysis/video_notes/<id>.md`（**每片一檔，不可合併輸出**） | 六大欄位齊全（未提及者寫「未提及」）；所有引語逐字可在原逐字稿找到；Skill-cluster tags 只能用模板列出的 9 個候選或附理由提議新 cluster |
| R4 | **Note QA Sampler** | `Explore` subagent（唯讀） | 該波次 15% 抽樣的 `<id>.md` + 對應 `<id>.txt` | 抽查報告（通過/退回清單＋理由） | 逐句核對抽樣引語是否存在於原文；核對「未提及」使用是否誠實（沒腦補）；不合格的送回 R3 單片重跑 |
| R5 | **Profile Synthesizer** | `general-purpose` subagent（單一實例，讀取量在其上下文預算內，見 §2） | 全部 57 份 `analysis/video_notes/*.md` | `analysis/lun_trading_profile.md`（人物特徵／能力／思維習性／ASR 容錯對照表／skill 分解圖含每個候選 skill 的證據密度） | 見 §3「Profile 驗收」 |
| R6 | **Skill Author**（每個 skill 一輪，循環 9 次） | `general-purpose` subagent，配備 skill-creator / skill-designer / superpowers:writing-skills | `analysis/lun_trading_profile.md`、該 cluster 標記到的 `video_notes/*.md`、`analysis/skill_boundary_ledger.md`（見 §4） | `.claude/skills/<name>/SKILL.md`（+ 必要的 `references/`、`scripts/`） | 通過 R7 審查閘門（≥90）才算完成 |
| R7 | **Skill Reviewer**（每輪，含修訂重審） | 獨立的 `general-purpose` subagent（**不可與 R6 同一實例**，避免自評偏誤）扮演 dual-axis 的 LLM-axis 角色 + 跑 `run_dual_axis_review.py` | 剛產出的 `SKILL.md`、`references/scoring_rubric.md`、`references/llm_review_schema.md` | `reports/skill_review_<name>_<ts>.{json,md}` | 加權後 final score ≥90 才放行；<90 附具體改進項回 R6 |
| R8 | **Agent Author** | `general-purpose` subagent（或 main session 直接寫） | `analysis/lun_trading_profile.md`、9 個已通過的 `SKILL.md` 的 frontmatter（name+description）、`Drmarkyang/.claude/agents/mark-yang-quant.md` 作結構參照 | `.claude/agents/lun-trading.md` | 見 §3「Agent 驗收」 |
| R9 | **Golden-Run Verifier** | `general-purpose` 或 `Explore` subagent | 安裝好的 `lun-trading` agent + 一組黃金測試提問 | 驗證報告（routing 正確率、人物設定一致性） | 見 §3「Golden-run 驗收」 |
| R10 | **Docs Writer** | `general-purpose` subagent（或 main session） | 以上所有產出 | `README.md`、研究文件（`analysis/lun_trading_profile.md` 已是研究文件本體，README 補管線說明＋侷限聲明） | 結構比照 `Drmarkyang/README.md`（核心交付物表、資料管線、完整性結果、目錄結構、侷限聲明） |

---

## 2. 各階段的協作模式（Orchestration Pattern）

### Phase 1（Pipeline，進行中）— 序列，不委派
`run_pipeline.sh` 本身是 resumable 序列腳本（download-archive + 可續跑轉錄），不需要 agent 化。main session 直接執行、等待完成。

### Phase 2（Integrity Gate）— 硬性檢查點，阻斷式
`check_integrity.py` exit code 非 0 即停止，不得跳過進 Phase 3。這是唯一「全體阻斷」的關卡；後續關卡都是「單片/單 skill 級」的局部重試，不阻斷整批。

### Phase 3（Note Writer 並行 fan-out）— 這是本設計的並行核心

**批次大小：每個 Note Writer agent 處理 3–4 部影片。**

理由：平均逐字稿 ~5,500 字元/片，批次 4 片 ≈ 22,000 字元（~6K tokens）輸入，加上模板與指令仍遠低於上下文上限；但真正的約束不是 token 預算，是**逐句引語核對的注意力密度**——批次越大，agent 對每片的逐字核對就越草率，anti-hallucination 風險上升。批次 3–4 是「還能對每片認真逐句核對」與「不會產生過多零碎 agent 實例」之間的平衡點。**不建議超過 6 片/agent。**

**波次併發：每波最多 8 個 Note Writer 同時跑。**

57 部 ÷ 4 片/agent ≈ 15 個 agent 實例 → 分 2 波（第一波 8 個、第二波 7 個）。8 是保守上限：M1 Mac mini 16GB 是本機硬體瓶頸（見 CLAUDE.md），且 main session 需要在每波之間收斂結果、指派 R4 抽查，過高併發會讓錯誤難以追蹤來源。

每個 Note Writer **輸出必須是每片一個檔案**（`analysis/video_notes/<id>.md`），即使一個 agent 處理 4 片也要寫 4 個檔，不可合併，以保持與驗收/重試粒度一致。

波次結束後立即跑 R4（Note QA Sampler）：**每波抽 15%（無條件進位，至少 1 篇）**，外加全部 57 篇跑完後再做一次跨波次分層抽樣（見 §3）。

### Phase 4（Profile Synthesizer）— 單一序列 agent

57 份 notes 總量估計 57 × ~2,000 字元（結構化筆記，含引語）≈ 114,000 字元（~30K tokens），單一 agent 一次讀完仍在合理預算內，**不需要拆成 cluster-summarizer 兩階段**。若之後發現筆記篇幅超預期（例如平均 >4,000 字元/篇）導致單一 agent 讀取吃力，才降級為「6 個分群 summarizer（依 NOTE_TEMPLATE 的 6 個分群各一個）→ 1 個 integrator」兩階段模式；預設方案是單一 agent。

### Phase 5（Skill Author + Reviewer 循環）— 嚴格序列，禁止並行

**逐一生成是硬性要求**，理由有二：(a) 審查閘門本身需要獨立於 author 之外的判斷，並行會讓「boundary ledger」的更新順序錯亂；(b) 9 個 skill 之間有內容邊界問題（例如風控概念會同時出現在 ote-entry-model 和 risk-management 筆記裡），序列生成才能讓後面的 skill author 看到「前面已經寫過什麼」而做交叉引用、避免重複。

**建議生成順序**（依 Phase 4 產出的證據密度，由核心技術到跨切面主題）：
1. `lun-ict-pd-arrays`
2. `lun-liquidity-analysis`
3. `lun-kill-zones-timing`
4. `lun-ote-entry-model`
5. `lun-price-action-toolkit`
6. `lun-backtesting-method`
7. `lun-prop-firm-playbook`
8. `lun-risk-management`
9. `lun-trading-psychology`

前 5 個是具體技術方法論（ICT 核心概念，彼此有依賴：liquidity/kill-zones/OTE 都建立在 PD Arrays 詞彙上，故 PD Arrays 必須第一個），第 6–7 個是應用層（回測方法、prop firm 規則），最後兩個（風控、心理）刻意放最後——它們天生跨切所有策略筆記，等前 7 個 skill 都定義好了邊界，風控/心理 skill 才能精準地「只講尚未被其他 skill 覆蓋的部分」並在 SKILL.md 裡交叉引用其他 8 個，而不是各自重複一份停損/心態論述。若 Phase 4 的證據密度數據顯示不同排序更合理，以 profile 數據為準，上述順序僅為預設 heuristic。

**單輪流程（每個 skill 重複）**：
1. R6 Skill Author 讀 `skill_boundary_ledger.md`（目前為空或已有 N 條）+ profile + 該 cluster 的 tagged notes → 寫 `SKILL.md`。
2. R7 Skill Reviewer（全新獨立 agent 實例）跑 `run_dual_axis_review.py --emit-llm-prompt` → 讀 prompt 產出 LLM review JSON → 跑 merge 步驟 → 產出 final score。
3. score ≥90 → 通過，把該 skill 的一句話邊界摘要追加進 `skill_boundary_ledger.md`，進下一個 skill。
4. score <90 → 把 improvement items 交還 R6（同一 skill，新一輪，non-adversarial 修訂），最多 **3 輪**。
5. 3 輪仍 <90 → 停止該 skill 的自動循環，上報使用者（附三輪分數與具體卡點），不得強行放行。

### Phase 6（Agent Author）— 單一 agent，序列
在全部 9 个 skill 通過後才開始（routing table 需要引用全部已確定的 skill name+description，不能邊生成邊寫)。

### Phase 7（Golden-run + 安裝 + 文件）— 序列
先跑 R9 驗證，通過才做全域安裝與 R10 文件撰寫；README 的「資料完整性」章節必須貼 Phase 2 的實際終端輸出（比照 Drmarkyang README 的做法），不可用估計數字代替。

---

## 3. 品質關卡（Quality Gates）細節

### 3.1 Integrity Gate（Phase 2，全體阻斷）
- 通過：`missing=0 and empty=0`。
- `suspicious`（chars/duration < 1.0 c/s）：人工聽該片前 60 秒確認是否為靜音/音樂/ASR 失敗；確認為有效內容但語速慢則放行，確認失敗則該 id 標記 excluded 並記錄於 README 侷限聲明，不重跑整條 pipeline 卡住其他 56 片。

### 3.2 Note 抽查協定（Phase 3，逐波 + 全corpus）
- **逐波抽查**：每波完成後，從該波產出中抽 15%（無條件進位，至少 1 篇），R4 逐句核對「引語是否存在於原逐字稿」「未提及欄位是否誠實」「Skill-cluster tags 是否落在允許清單或有理由的新提議」。
- **全 corpus 收斂抽查**：57 篇全部完成後，再做一次跨波次、跨 6 個分群類別分層抽樣，取 ~10 篇（~17%），確保沒有系統性偏差（例如某一分群集中出錯）。
- 不合格判定：任一引語查無出處、或欄位明顯腦補 → 該片退回 R3 用**單片**（非整批）重跑，最多 2 次重試；仍失敗則標記該片筆記為「人工待覆核」，Phase 4 引用時排除其證據，不阻斷整體進度。

### 3.3 Profile 驗收（Phase 4）
- 涵蓋全部 6 個分群類別且每類至少有具體引述佐證。
- Skill 分解圖：每個候選 skill 必須附「證據密度」（被幾篇 notes 標記該 tag）與至少 3 條直接引語佐證；若某候選 skill 密度過低（例如 <3 篇），需在 profile 中明寫是否合併進其他 skill 或降級為某 skill 的一個小節，而非硬湊成獨立 skill——**目標是 9 個左右，不是鐵定 9 個**，密度證據優先於預設數字。
- 隨機抽 5 條 profile 結論回頭核對其引用的 video_notes 是否確實支持。
- ASR 容錯對照表必須存在（比照 Drmarkyang 慣例，ICT 術語誤轉常見，例如「流動性」「訂單塊」「公允價值缺口」等術語的 ASR 誤字模式）。

### 3.4 Skill 審查閘門機制（Phase 5）
- 分數來源：`run_dual_axis_review.py` 的 auto-axis（metadata_use_case 20 / workflow_coverage 25 / execution_safety_reproducibility 25 / supporting_artifacts 10 / test_health 20）與 LLM-axis 加權合併（預設 0.5/0.5）。
- 生成前先判定該 skill 是否為 `knowledge_only`（無 `scripts/*.py`）——9 個候選多半是純知識型（ICT 概念、規則清單），若確定無需執行腳本，明確在 Skill Author 階段就以 knowledge_only 為目標形態，避免 Reviewer 誤判缺腳本而錯誤扣分（腳本本身有處理 knowledge_only 的邏輯，但仍要求清楚的 When to Use / Prerequisites / workflow 結構）。
- 通過線：≥90（比照 rubric 的 "production-ready baseline"）。
- 最多 3 修訂輪；3 輪後仍未達標 → 停止、上報使用者，附三輪的分數與 improvement items 軌跡，讓使用者決定降低標準／換人工介入／放棄該候選 skill 並回頭調整 profile 的分解圖。

### 3.5 Agent 驗收（Phase 6）
- Frontmatter 合規：`name` + `description`（+ 適當的 `tools`）齊全，YAML 可解析。
- Routing table 完整覆蓋全部 9 個已通過的 skill（逐一核對 name 是否都出現）。
- 人物設定與決策框架維持精簡（比照 mark-yang-quant.md 的「四大支柱＋編號決策框架」結構），深度知識**不得**內嵌回 agent 檔案本體——若發現大段技術細節被搬進 agent.md 而非留在對應 skill，視為結構違規，退回 R8 修正。

### 3.6 Golden-run 驗收（Phase 7）
- 準備 8–10 條代表性測試提問，需覆蓋：9 個 skill 各至少被觸發一次（驗證 routing）、1 條人物/哲學類問題（應由 agent 本體人物設定回答，不需觸發任何 skill）、1 條超出範疇的問題（應得體拒絕/轉介，不腦補）。
- 通過標準：routing 提問中 ≥90% 選對 skill；回答中的 ICT 術語與 profile 的「術語定義」一致，不與逐字稿內容矛盾；人物語氣與 `lun_trading_profile.md` 的思維習性/口頭禪一致。
- 未通過：定位是哪個 skill 或 routing table 條目的問題，做**局部修補**（改該 skill 或 routing table 一行），不重跑整條生成鏈。

---

## 4. 資料流契約（Data-Flow Contract）

```
data/playlist.json ─────────────┬─────────────────────────────────────────┐
                                 │                                         │
data/audio/<id>.m4a  (Phase 1)  │  ← 只有 Phase 1 的 ASR 步驟碰音檔        │
        │                       │     其他所有階段一律不讀 data/audio/*    │
        ▼                       │                                         │
data/transcripts/<id>.txt ──────┤                                         │
        │                       │                                         │
        ▼ (Phase 2 gate)        │                                         │
   [check_integrity.py]         │                                         │
        │ pass                  │                                         │
        ▼                       │                                         │
analysis/NOTE_TEMPLATE.md ──►  Note Writer (Phase 3) ──► analysis/video_notes/<id>.md
                                                                  │
                                                                  ▼ (全部 57 篇)
                                              Profile Synthesizer (Phase 4)
                                                                  │
                                                                  ▼
                                          analysis/lun_trading_profile.md
                                                                  │
                              ┌───────────────────────────────────┴───────────────────────────────────┐
                              ▼                                                                         │
              analysis/skill_boundary_ledger.md ◄────────────────┐                                     │
                              │  (逐輪讀寫，見下)                    │                                     │
                              ▼                                   │                                     │
              Skill Author (Phase 5, ×9 序列) ──► .claude/skills/<name>/SKILL.md                        │
                              │                                                                          │
                              ▼                                                                          │
              Skill Reviewer ──► reports/skill_review_<name>_<ts>.{json,md}                             │
                              │  score≥90 才回寫 ledger 並解鎖下一輪                                        │
                              ▼                                                                          │
                    （9 個 SKILL.md 全數通過）                                                              │
                              │                                                                          │
                              ▼                                                                          │
              Agent Author (Phase 6) ──► .claude/agents/lun-trading.md ◄──── Drmarkyang/mark-yang-quant.md（僅作結構參照，不讀取其內容作為知識來源）
                              │
                              ▼
              Golden-Run Verifier (Phase 7) ──► 驗證報告（不落檔於正式交付物，僅過程紀錄）
                              │
                              ▼
              Docs Writer ──► README.md ＋ analysis/lun_trading_profile.md（已是研究文件本體）
```

**新增檔案（本設計比 Drmarkyang 前例多出的協調用檔案）**：
- `analysis/skill_boundary_ledger.md`：每個 skill 通過審查後，追加一段「這個 skill 覆蓋了什麼、明確不覆蓋什麼（交給哪個其他 skill）」。Skill Author 在動筆前必讀，用來做 DRY 邊界判斷，避免 9 個 skill 互相抄一遍風控/心理段落。
- `reports/`：Reviewer 的所有中間產物（prompt、JSON、md 報告），僅供過程追蹤，不是正式交付物，不需要放進 README 的目錄結構表。

**契約重申**：Phase 3 之後的任何階段都不讀 `data/audio/*`；Phase 4 之後的任何階段都不直接讀 `data/transcripts/*`（一律透過 `video_notes/*.md` 這一層做為 canonical 摘要，避免重複逐字稿解讀導致 Phase 3 的抽查投資浪費）。

---

## 5. 失敗/重試策略（按階段）

| 階段 | 失敗態樣 | 重試單位 | 上限 | 上限後動作 |
|---|---|---|---|---|
| Phase 1 | yt-dlp/ASR 失敗、音檔缺漏 | 單片重跑（download-archive 本身就是 resumable） | 2 次 | 標記該片 excluded，寫入 README 侷限聲明，不阻斷其他片 |
| Phase 2 | integrity 不過 | 回到 Phase 1 補該片 | 依附 Phase 1 上限 | 同上 |
| Phase 3 | 筆記抽查不合格（引語查無出處/腦補） | 單片重跑（同一 Note Writer 角色，新 agent 實例） | 2 次 | 標記「人工待覆核」，Phase 4 排除其證據 |
| Phase 4 | Profile 驗收未過（覆蓋不全/引用對不上） | 整份 profile 一輪修訂（帶具體缺口清單） | 1 次自動修訂 | 仍不過 → 交還使用者決定是否補充來源或放寬標準 |
| Phase 5 | Skill 審查分數 <90 | 同一 skill 修訂（同一 SKILL.md，新 Author 輪次） | 3 輪 | 停止、上報使用者附三輪分數軌跡；不強行放行 |
| Phase 6 | Frontmatter 不合規/routing table 漏 skill | Agent 檔案局部修正 | 2 次 | 仍不過 → 交還使用者 |
| Phase 7 | Golden-run 未達 90% routing 正確率 | 定位問題 skill/routing 行，局部修補 | 2 次局部修補 | 仍不過 → 交還使用者，附失敗的具體提問與 agent 實際回覆 |

**通則**：越晚期的失敗，重試粒度越小（局部修補優先於整段重生成），因為晚期階段的重新生成成本（尤其 Phase 5 的審查輪）遠高於早期。任何階段連續失敗觸及上限，一律「上報使用者」而非自動降低驗收標準或跳過關卡。

---

## 6. 執行清單（Execution Checklist，main session 可逐條照做）

```
[ ] Phase 1  等待/確認 scripts/run_pipeline.sh 跑完 57 部 core 影片
[ ] Phase 2  跑 scripts/check_integrity.py
    [ ] missing=0, empty=0 → 繼續
    [ ] suspicious 清單 → 人工聽前 60 秒 → 放行或標記 excluded
[ ] Phase 3  Note Writer 波次 fan-out（batch=4, wave concurrency=8）
    [ ] Wave 1: 8 個 general-purpose agent，每個處理 4 部影片
    [ ] Wave 1 完成 → 抽 15% 跑 Note QA Sampler → 不合格單片重跑（≤2 次）
    [ ] Wave 2: 剩餘影片同上
    [ ] Wave 2 完成 → 抽 15% 跑 Note QA Sampler
    [ ] 全 corpus 收斂抽查：跨 6 分群分層抽 ~10 篇，複核
    [ ] 確認 analysis/video_notes/ 下恰有 57（扣除任何標記 excluded 的片數）份筆記
[ ] Phase 4  Profile Synthesizer 讀全部 video_notes → 寫 analysis/lun_trading_profile.md
    [ ] 驗收：6 分群覆蓋、skill 分解圖含證據密度、5 條隨機引用核對、ASR 容錯表
    [ ] 不過 → 1 輪修訂 → 仍不過 → 上報使用者
[ ] Phase 5  建立空的 analysis/skill_boundary_ledger.md
    對以下 9 個候選（依序，一次只做一個，禁止並行）：
    1. lun-ict-pd-arrays
    2. lun-liquidity-analysis
    3. lun-kill-zones-timing
    4. lun-ote-entry-model
    5. lun-price-action-toolkit
    6. lun-backtesting-method
    7. lun-prop-firm-playbook
    8. lun-risk-management
    9. lun-trading-psychology
    [ ] R6 Skill Author 寫 SKILL.md（讀 ledger + profile + 對應 tagged notes）
    [ ] R7 獨立 Skill Reviewer：跑 dual-axis Step1 → 產出 LLM review JSON → Step3 合併分數
    [ ] score ≥90 → 追加該 skill 邊界摘要進 ledger → 下一個候選
    [ ] score <90 → 回 R6 修訂（≤3 輪）→ 3 輪仍不過 → 上報使用者，跳過該候選或降規格，繼續下一個
[ ] Phase 6  9 個 SKILL.md 全數通過後，R8 寫 .claude/agents/lun-trading.md
    [ ] 驗收：frontmatter 合規、routing table 涵蓋全部已通過 skill、無深度知識誤內嵌
[ ] Phase 7
    [ ] 準備 8–10 條黃金提問（覆蓋 9 skill + 1 人物題 + 1 超綱題）
    [ ] R9 Golden-Run Verifier 跑驗證 → ≥90% routing 正確才過；未過→局部修補（≤2 次）
    [ ] 全域安裝（symlink 或依專案慣例）
    [ ] R10 撰寫 README.md（比照 Drmarkyang 結構：核心交付物表／使用方式／資料管線／資料完整性實際輸出／目錄結構／侷限聲明）
```
