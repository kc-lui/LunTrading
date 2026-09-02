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
