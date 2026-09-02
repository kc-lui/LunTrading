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
