# Skill Boundary Ledger

> 每個 skill 通過 dual-axis 審查（≥90）後，喺呢度追加一段：呢個 skill 覆蓋咗乜、明確唔覆蓋乜（交畀邊個其他 skill）。
> 後續 skill author 動筆前必讀，用嚟做 DRY 邊界判斷，避免 skills 之間重複風控/心理/MTF 論述。

## 生成次序

1. lun-ict-pd-arrays
2. lun-price-action-toolkit
3. lun-liquidity-analysis
4. lun-kill-zones-timing
5. lun-multi-timeframe-analysis
6. lun-ote-entry-model
7. lun-exit-management
8. lun-backtesting-method
9. lun-prop-firm-playbook
10. lun-risk-management
11. lun-trading-psychology

## 已通過 skills 邊界摘要

### 1. lun-ict-pd-arrays ✅ 90/100（2026-09-02，auto 80 / LLM 96）
- **覆蓋**：PD Array 詞彙地基 — Order Block、Breaker Block、FVG、IFVG/隱藏FVG、BPR、拒絕塊/真空塊/補償塊、50% premium/discount 劃分紀律、區域品質檢查清單、入場確認三層口徑（追/唔追雙選項）、觸碰次數衰減規則。
- **唔覆蓋**：流動性掃蕩理論（→ lun-liquidity-analysis）、OTE 入場步驟（→ lun-ote-entry-model）、時段選擇（→ lun-kill-zones-timing）、多時框串聯（→ lun-multi-timeframe-analysis）、出場管理（→ lun-exit-management）、倉位風險（→ lun-risk-management）。
- **DRY anchor**：所有 sibling skills 引用 PD Array 詞彙時一律指向本 skill，唔好重新定義。

### 2. lun-price-action-toolkit ✅ 90/100（2026-09-02，auto 80 / LLM 96）
- **覆蓋**：14 種價格行為策略索引、市場階段判斷、偏向兩步法、K 線力度三分法/時鐘法、破位 vs 破位回調雙選項、供應需求六招（衝停衝 base 規則）、動能兩階段、Turtle Soup、諧波三形態（Bat/Butterfly/Gartley XABCD，單源低信心子節）、ICI 自創形態、confluence 分層（2–3 底線/3–5 理想）、均線口徑演化（100日→EMA50→21/50/200）。
- **唔覆蓋**：PD Array 詞彙（→ lun-ict-pd-arrays）、假突破背後訂單博弈（→ lun-liquidity-analysis）、HTF→LTF 完整分工（→ lun-multi-timeframe-analysis）、Fib 回調入場執行（→ lun-ote-entry-model）、出場（→ lun-exit-management）、時段（→ lun-kill-zones-timing）。
- **DRY anchor**：策略嘅「入場模式」層由本 skill 持有；sibling 講到具體策略名（破位清單、動能、S&D、諧波、ICI、Turtle Soup）一律指向本 skill。

### 3. lun-liquidity-analysis ✅ 90/100（2026-09-02，auto 80 / LLM 96，first pass）
- **覆蓋**：訂單博弈機制層 — 三種訂單類型、止損單＝突破單燃料、流動性池地圖（高低壓、internal/external）、三種流動性形態 vs 三種池行為（平行框架，唔好合併）、獵殺/sweep 循環、真假突破嘅「站得住」機制測試、先佈局 vs 等確認雙口徑、Daily Bias 應用鏈、進階工具（Heatmap 盲點等，單源）。
- **唔覆蓋**：PD Array 詞彙（→ lun-ict-pd-arrays）、破位策略執行/K線收盤紀律（→ lun-price-action-toolkit）、時段（→ lun-kill-zones-timing）、MTF 分工（→ lun-multi-timeframe-analysis）、入場執行（→ lun-ote-entry-model）、出場（→ lun-exit-management）。
- **DRY anchor**：流動性池位置、掃蕩機制、真假突破機制測試由本 skill 持有；「掃描流動性」相關一律指向本 skill。

### 4. lun-kill-zones-timing ✅ 90/100（2026-09-02，auto 80 / LLM 96，first pass）
- **覆蓋**：「幾時交易」決策層 — Kill Zone 時間表（亞洲/倫敦/紐約，含 NY 雙口徑平行呈現）、時段揀選與品種配對、時段紀律清單、個人 routine、Weekly Market Profile 子節（單源）、數據日曆/新聞 timing 子節（單源）、時區口徑規則（紐約時間 vs 美國時間 vs 馬來西亞時間）。
- **唔覆蓋**：倫敦破位策略執行（→ lun-price-action-toolkit）、時段內流動性行為（→ lun-liquidity-analysis）、入場模型（→ lun-ote-entry-model）、MTF 分工（→ lun-multi-timeframe-analysis）。ICT 銀彈策略＝僅預告未教，唔准由教科書補完。
- **DRY anchor**：一切時間表/時段/日曆判斷指向本 skill。

### 5. lun-multi-timeframe-analysis ✅ 90/100（2026-09-02，auto 80 / LLM 96，first pass）
- **覆蓋**：時框分工路由層 — 7-row 時框組合對照表（主流 D1→4H/1H→5m、圖形 15m/5m、四層版、五時框版等，平行照錄唔合併）、一票否決順序（B7rumsOw6_U）、動能回流公開骨架（大時框止盈＋小時框入場；完整 1234 招明示留付費班，禁止補完）、A+ 交易四大標準過濾器（k0ESC6XYz50，單源）、鬧鐘/切換 routine。
- **唔覆蓋**：各時框內用乜工具判斷（→ 對應 sibling）、時段（→ lun-kill-zones-timing）、入場觸發（→ lun-ote-entry-model）、圖形庫（→ lun-price-action-toolkit）。
- **DRY anchor**：HTF→LTF 分工、時框組合揀選、動能回流骨架、A+ 過濾清單由本 skill 持有。

### 6. lun-ote-entry-model ✅ 91/100（2026-09-02，auto 80 / LLM 97，first pass）
- **覆蓋**：入場執行序列層 — Step 0-7 完整入場工作流（路由→流動性掃描→強動能→定浪拉 Fib→共識疊加→掛單/觸發雙選項→SL/TP 初設→失敗再入場）、OTE 口徑 50%–79%（講者原話，教科書 62-79% 明令禁止）、六口徑回調對照表（平行照錄）、入場模型族譜 2023-2026 六版演化、入場 K 線偏好（吞噬形態）。
- **唔覆蓋**：PD Array 區域確認三層口徑（→ lun-ict-pd-arrays，引用唔重複）、掃蕩機制（→ lun-liquidity-analysis）、MTF 秘訣（→ lun-multi-timeframe-analysis）、出場管理細節（→ lun-exit-management）。
- **DRY anchor**：入場「序列」（setup→trigger→order placement）由本 skill 持有。

### 7. lun-exit-management ✅ 90/100（2026-09-02，auto 80 / LLM 96，first pass）
- **覆蓋**：出場管理層 — 止損三法（結構位/POI 後面/呼吸空間）、止盈三套（下一個主力區/標準差投射（單源）/EMA50 追蹤）、三層管理（消除風險→利潤最大化→鎖住利潤）、80% 提前出場雙口徑、平價保護鐵律、分批（-2 出一半，單源）、RR↔勝率取捨、RR 門檻 1:1/1:2/1:3 分層、寬窄止損兩層悖論。RdnJw-mhwlE Pivot 句永久存疑標記。
- **唔覆蓋**：倉位 sizing/風險%（→ lun-risk-management）、時段性出場時間表（→ lun-kill-zones-timing）、入場序列中嘅 SL/TP 初設（→ lun-ote-entry-model）。
- **DRY anchor**：一切「止損放邊/止盈點邊度/幾時提前走」由本 skill 持有。

### 8. lun-backtesting-method ✅ 90/100（2026-09-02，auto 80 / LLM 96，first pass）
- **覆蓋**：手動 TradingView-replay 式回測方法 — 樣本量分層（10/50–100/100–200，按用途，唔合併）、截圖＋解釋記錄法、bar-by-bar 唔睇後市、系統信心數據（expected return/預期連敗/連勝/平均 RRR）、日記與覆盤節奏、多系統框架與 100 筆挑戰（單源；挑戰本體係付費班功課，只錄公開部分）。教科書方法論（walk-forward/Monte Carlo/overfitting）明令禁止補完；NqixhiGBt9E 出 corpus 外，唔准引用。
- **唔覆蓋**：五大系統具體規則（→ lun-price-action-toolkit / lun-liquidity-analysis）、風險%（→ lun-risk-management）、考試應用（→ lun-prop-firm-playbook）、出場（→ lun-exit-management）。
- **DRY anchor**：「點樣驗證一個系統」由本 skill 持有。

### 9. lun-prop-firm-playbook ✅ 90/100（2026-09-02，auto 80 / LLM 96，round 2）
- **覆蓋**：資金盤/機構考試層 — 資金問題診斷（識交易但本金細）、數據門檻（先有回測數據先好考）、兩條路線對照（FTMO 倒推計劃 vs Axi Select【推廣合作】隔離區）、考試用短線系統背景、prop firm 風險上限（考試 1%、撥資 ≤1%、起步 0.25%、絕不過夜——情緒理由為原話，考試保護框架屬推測）、增長藍圖（講者藍圖非驗證統計）、出金後戒飄。Axi 規則帶時效性 caveat；MjPZizFnX-E 引用必帶分母 caveat。
- **唔覆蓋**：一般風險%（→ lun-risk-management）、考試系統規則本體（→ lun-price-action-toolkit）、TP/SL 放置（→ lun-exit-management）、時段（→ lun-kill-zones-timing）。
- **DRY anchor**：考試規則、資金盤路線比較、贊助內容隔離規範由本 skill 持有。

### 10. lun-risk-management ✅ 90/100（2026-09-02，auto 80 / LLM 96，round 2）
- **覆蓋**：資金/風險層 — 防守哲學、倉位公式（資金×風險%÷止損點數）、單筆風險三口徑平行呈現（教學 1–2% / 自用 <0.25% / 實盤 1R=1%，Tier 1a+1b 唔裁決、必須一齊報）、等額風險鐵律＋大回撤唯一例外、連虧降倉、30% 停手出金、本金 10–30% 配置、「不熟,不做」、頻率即風控（月 3–5 筆）、大盈虧比連虧保險數學、錯誤目錄 E/F/M/K 帶逐項路由。教科書公式（Kelly/VaR/ATR sizing）ban-fenced。
- **唔覆蓋**：SL/TP 放置（→ lun-exit-management）、prop firm 情境上限（→ lun-prop-firm-playbook）、RR 門檻分層（→ lun-exit-management，侷限聲明 7 已披露同 profile §6.10 嘅偏離）、心理項目（→ lun-trading-psychology）。
- **DRY anchor**：「虧幾多、開幾大、幾時停」由本 skill 持有。

