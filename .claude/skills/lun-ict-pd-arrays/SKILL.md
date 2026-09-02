---
name: lun-ict-pd-arrays
description: 按照交易倫（Alan / LunTrading）的教法定義同運用 ICT PD Array 全家族——Premium/Discount 50% 劃分、Order Block（訂單塊）、Breaker Block（破壞塊）、FVG/IFVG/隱藏 FVG、BPR（平衡價格區間）、拒絕塊、真空塊、補償塊、POI 極限位置——包括畫法、品質判斷（50% 回調規則、第一次觸碰最強、觸碰多次失效）、OB vs FVG 取捨、同「等結構轉換先入場」嘅確認紀律。Use when analysing PD Arrays / Order Blocks / FVG / fair value gaps / breaker blocks / premium-discount zones / POI the way 交易倫 teaches, or when marking 訂單塊/失衡區域/貴價區平價區 on a chart. 唔覆蓋流動性掃描理論、入場時機同出場管理（見 sibling skills）。
---

# lun-ict-pd-arrays：PD Array 詞彙與工具（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅詞彙地基。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。唔好摻入 corpus 以外嘅通用 ICT 理論。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 喺圖表上定義、畫出或驗證任何 PD Array 元素（OB / Breaker / FVG / IFVG / 隱藏 FVG / BPR / 拒絕塊 / 真空塊 / 補償塊）
- 判斷一個波段邊度係「貴」（Premium）邊度係「便宜」（Discount），過濾合理交易區
- 評估一個 Order Block 或 FVG 嘅品質同剩餘價值（第幾次觸碰、有冇失效）
- OB 同 FVG 同時存在時做取捨
- 檢查「碰到 PD Array 之後可唔可以做」嘅確認條件（結構轉換）

**唔應該用嘅情況**：

- 判斷流動性池位置、掃描/獵殺/假突破形態本身 → 用 `lun-liquidity-analysis`
- 回調入場嘅完整四步模型（掃描→動能→第三浪→共識）→ 用 `lun-ote-entry-model`
- 止盈投射、平價保護、分批出場 → 用 `lun-exit-management`
- 揀交易時段/週節奏 → 用 `lun-kill-zones-timing`；多時框分工流程 → 用 `lun-multi-timeframe-analysis`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答；唔可以摻入 corpus 以外嘅通用 ICT 理論（例如未經 corpus 教授嘅 Fibonacci OTE 62–79% 理論、標準 ICT 教科書定義）。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯**：讀逐字稿或引文前必須對照 `analysis/lun_trading_profile.md` §5 容錯表（FBG＝FVG、訂單快＝訂單塊、拒絕快＝拒絕塊、搶動能＝強動能、評價保護＝平價保護等）。
3. **Sibling 依賴**：本 skill 係詞彙地基，冇上游依賴；但完整交易決策需要 sibling skills 配合——流動性判斷（`lun-liquidity-analysis`）、入場模型（`lun-ote-entry-model`）、出場（`lun-exit-management`）、時機（`lun-kill-zones-timing`）、時框分工（`lun-multi-timeframe-analysis`）。其他 skill 引用 PD Array 元素時，以本 skill 定義為準（DRY）。
4. **核心詞彙速查表**（一行定義；全文原話引錄見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| PD Array | 「價格輸送的整個結構」；入場前用嘅判斷清單，唔係訊號 | tCfmxMX5WaU |
| Premium / Discount | 波段拉 50%：50% 以下＝便宜（搵多），50% 以上＝貴（搵空） | tCfmxMX5WaU, xwsyfVf2l0k |
| Order Block（訂單塊） | 大型機構出手區域＝強動能前最後一根反向 K 線，必須完全吞噬，由低引線畫到高引線；小時框要見失衡＋結構轉換 | tCfmxMX5WaU, xwsyfVf2l0k, ofQ--jkHTm4 |
| Breaker Block（破壞塊） | 反向主導嘅訂單塊：獵殺＋有效 OB 被收盤實體突破＋結構轉換後做反向操作 | tCfmxMX5WaU, xwsyfVf2l0k |
| FVG | 三根 K 線，中間必須大實體強動能，第一同第三根引線之間嘅空位（失衡區域），會被回補 | tCfmxMX5WaU, ofQ--jkHTm4, xwsyfVf2l0k |
| IFVG | 被破壞咗嘅 FVG，反向操作 | tCfmxMX5WaU |
| 隱藏 FVG | 前後引線重疊時，各取引線 50% 之間形成嘅區域 | tCfmxMX5WaU |
| BPR | 兩個反向 FVG 重疊結合嘅區域 | tCfmxMX5WaU |
| 拒絕塊 | 流動性掃描後嘅長引線，整條引線區域係入場參考 | tCfmxMX5WaU |
| 真空塊 | 收盤價同下一根開盤價之間嘅明顯跳空缺口，好可能被回補 | tCfmxMX5WaU |
| 補償塊 | 趨勢延伸失敗＋結構轉換嗰段區域，回碰後順新趨勢做 | tCfmxMX5WaU |
| POI / 極限位置 | POI＝FVG 或 Order Block；只做「極限的 POI」，中途位唔要 | ofQ--jkHTm4 |

## Workflow（分析流程）

對一張圖表做 PD Array 分析時，按次序行以下步驟：

**Step 1 — 劃區與過濾（先行）**

1. 揀定波段（腳到腳），拉 50%：上半＝Premium 搵空，下半＝Discount 搵多。
2. 執行 50% 紀律（硬規則）：「我希望可以在50%以下」去做多，「這個是我對自己很嚴格要求的一個部分」（tCfmxMX5WaU）；50% 以上嘅 FVG「我基本上會無視掉」（tCfmxMX5WaU）。
3. 冇碰到就走咗嘅兩個選項（tCfmxMX5WaU，兩者都係原話，唔好抹平）：
   - **允許追（結構破壞式）**：「那你可以追�你可以等破壞了�直接做多�或者是�你等未來碰到了�再做多�如果結構還沒有改變的話�再做多也可以」
   - **佢本人偏好（唔追）**：「對我來說�如果碰到了�還沒有碰到�價格就走了�那我就會去找�下一個機會�我不會去追」——預設跟呢個口徑，除非用家明確揀追嘅選項。

**Step 2 — 標記元素並過品質檢查**

Order Block 檢查清單（逐項核對，愈多愈高質）：

- [ ] 完全吞噬嘅最後一根反向 K 線（tCfmxMX5WaU）
- [ ] 小時框有失衡＋結構轉換（tCfmxMX5WaU）
- [ ] 50% 回調規則：「一個高質量的order block,一個有價值的order block,你會看到價格是不會回調超過一半的。」（xwsyfVf2l0k）
- [ ] 觸碰次數：「就是當它有強動能釋放之後,價格第一次回調到這個order block的時候,它的質量是最好的。」（xwsyfVf2l0k）；「當它觸碰太多次,它已經失去價值了之後,通常我就可以無視它了」（B7rumsOw6_U）
- [ ] 同 Breaker 重疊＝「非常高質量的交易區」（xwsyfVf2l0k）
- [ ] OB 價值要配合流動性睇：「你學會看流動性的時候你就知道哪一個order block是有價值Ｖ哪一個order block是沒有價值的」（yZoSW3DGRGI；流動性判斷本身歸 `lun-liquidity-analysis`）

FVG 檢查：

- [ ] 被碰過即失效：「這個FEG被碰到過了。」「對我來說沒有什麼價值了。」（7dDW8tF1cZo）
- [ ] 只用而家有效嘅：「但是現在已經沒有交易的價值�我們只看現在」（tCfmxMX5WaU）
- [ ] 前後引線已被觸碰過就唔算 FVG（tCfmxMX5WaU）

**Step 3 — 取捨**

- OB vs FVG：「我發現到有FVG,有order block的話,我都會選擇order block。」（xwsyfVf2l0k）
- POI 極限原則：「我們要價格到一個終極的 POI,極限的 POI,我們才來做交易」（ofQ--jkHTm4）
- 時框分工：「我們用兩個時空�大時空�找FBG�小時空�去找交易機會」（tCfmxMX5WaU；時空＝時框）

**Step 4 — 定確認層級（矛盾分層，唔好抹平）**

Corpus 內有三個唔同激進度嘅口徑，屬情境分層而非單一規則：

| 層級 | 規則 | 出處情境 |
|---|---|---|
| **保守（預設，佢嘅嚴格要求）** | 「不要一碰到就做交易」，要等結構轉換／結構破壞，「確認動能跟我們要交易的方向是一致性的時候」先入場；「沒有結構轉換」「不要做」 | tCfmxMX5WaU（OB/FVG 教學總綱；理由：喺 FVG 內直接做可能反覆被打，「所以等結構破壞了」「勝率會更高」） |
| **中性（觸發式掛單）** | 「我是等價格碰到了我的POI,我會射警報器在POI,動到了之後,我才掛單」（射警報器＝設警報器）——警報後見到反應先掛 | ofQ--jkHTm4（Order Flow 系統；前提係已有 BOS＋Accumulation 形態） |
| **激進（直接掛單）** | 「碰到了再做。或者是你要提前掛單也可以。」；拒絕塊 ICT 話可以直接做——「ICT是說你可以直接做空�但是對我來說的話�有其他的確認的共識工具�反倒會更好」 | 7dDW8tF1cZo（已有大級別掃描＋強動能結構破壞先行）；tCfmxMX5WaU（拒絕塊/真空塊例子直接入、抓 1比2） |

判斷原則：前置確認愈多（掃描、強動能結構破壞已發生），入場可以愈直接；PD Array 淨係一個位、冇任何結構訊號時，一定行保守層。

**Step 5 — 觸碰次數例外註記**

第一次觸碰最強係主規則，但唔係「第二次一定唔做」：WmW5fQjK5Qg 嘅 Russell 2000 例子，日線 OB「被觸碰了兩次。然後第二次呢,碰到了EMA50。」→「所以這個告訴我,反轉訊號非常強,非常漂亮」——第二次觸碰疊加其他共識（EMA50＋釘形）時仍可用。原則：次數遞減價值，共識可以補償；「觸碰太多次」（三次以上無明確數字）就無視。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅圖表判讀。一份完整嘅 PD-Array 分析回覆應包含以下四部分，每部分都要引用對應規則（附 video id）：

1. **區域清單**：波段 50% 線位置＋所有有效 PD Array 元素（元素類型、價格範圍、屬 Premium 定 Discount 區），逐個標明品質檢查結果（吞噬/失衡/結構轉換/觸碰次數/50% 回調）。
2. **方向偏好**：按 50% 劃分講明目前只可以搵邊個方向（50% 以下搵多、以上搵空，tCfmxMX5WaU）；OB 同 FVG 並存時聲明取 OB（xwsyfVf2l0k）。
3. **確認層級**：講明呢個情境應該用保守/中性/激進邊一層（按 Step 4 表），同埋仲欠咩前置確認（結構轉換未出現→唔做）。
4. **失效條件**：列明每個區域幾時作廢（FVG 被碰過、OB 觸碰太多次、前後引線已被觸碰、「我們只看現在」原則），同「冇碰到就唔追」嘅放棄條款（tCfmxMX5WaU）。

超出範圍嘅問題（流動性位置、入場時機、止盈）要明確轉介對應 sibling skill，唔好即場作答。

## 實例（corpus 內示範）

### 例一：黃金日線 FVG 嘅 50% 紀律（tCfmxMX5WaU）

黃金日線突破高位後留低 FVG。上半部分喺波段 50% 以上——「上面這一部分�FBG�上面這一部分�我基本上會無視掉�我會找下面這一部分」。結果價格冇跌入 50% 以下嘅 FVG 就走咗，佢認錯過——「我應該會錯過了這一筆交易」——但照樣唔追，因為 50% 以下先係佢嚴格要求。同片另一例：喺比較貴嘅 FVG 唔搵做多，「它就可以幫我們避免這邊有一個虧損的單子」；等結構轉換嘅例子做到「1比2�還是可以做得到的」。呢個例示範：規則嘅價值一半喺避開輸單。

### 例二：Russell 2000 日線 OB 做共識層（WmW5fQjK5Qg，2026-01-05 實盤，1:22.45）

週線結構破壞＋回調釘形支撐 → 日線：1月2號釘形「它是在日線圖一個order block,這一邊的位置形成了。被觸碰了兩次。然後第二次呢,碰到了EMA50。」→ 1小時假突破後回流 EMA50 兼支撐阻力轉換位做多——「滿滿的共識,滿滿的,就非常漂亮的位置」。目標參照包括「或者是這邊有一個小小的破壞塊」。呢筆最終 1:22.45。示範重點：PD Array 元素（OB、Breaker）喺實盤入面係共識拼圖之一，唔係孤立訊號；OB 被打破變破壞塊後可作目標參照（同類：zgVlK7UBNTY 原油例「上面這個order block被打破了,變成了破壞塊」）。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 流動性＝訂單嘅機制、流動性池位置清單（昨日/上週/上月/session 高低位）、掃描/獵殺/假突破三形態、「站得住」判斷 | `lun-liquidity-analysis` |
| OTE 四步入場模型、Fibonacci 50–79% 回調、第三浪、共識疊加入場流程 | `lun-ote-entry-model` |
| 止盈標準差投射、平價保護、分批、鎖利節奏 | `lun-exit-management` |
| 獵殺時段、Weekly Profile、數據日曆時機 | `lun-kill-zones-timing` |
| 日線→4H/1H→5分鐘三視角分工、A+ 篩選 | `lun-multi-timeframe-analysis` |
| BOS/CHoCH 結構判讀細則、K 線形態、EMA50/MACD 工具 | `lun-price-action-toolkit` |
| 倉位/風險%數字、盈虧比門檻分層 | `lun-risk-management` |

PD Array 元素被上述 skill 引用時（例如掃描目標、止盈障礙物），以本 skill 嘅定義為準（DRY：定義只寫喺度）。

## 侷限聲明

1. **ASR 來源**：所有引文出自本地 ASR 逐字稿，含系統性誤字（FBG＝FVG、訂單快＝訂單塊、拒絕快＝拒絕塊、搶動能＝強動能等）；引用時照錄原文，正字對照必查 profile §5。
2. **教學示範值，非驗證統計**：例子中嘅盈虧比（1比2、1比10、1:22.45）同「勝率會更高」等講法均為講者示範或自述，未經獨立對帳（profile §7.4）；1:22.45 該筆為講者公開實盤自述。
3. **內容有預告未教嘅部分**：tCfmxMX5WaU 片尾明言「之後我會分享完整的交易系統給大家」——本片只教元素判別，完整系統散見後續影片同付費班；動能回流完整清單唔喺公開 corpus（profile §7.1）。
4. **參數係示範口徑**：「觸碰太多次失效」無精確次數門檻；拒絕塊/真空塊例子嘅 1比2 目標係當場示範，非固定規則。實際使用前應按 `lun-backtesting-method` 做 100 筆級別驗證。
5. **隱藏 FVG／BPR／補償塊證據薄**：呢三個元素只有 tCfmxMX5WaU 一片定義＋少量例子，冇後續影片延伸；使用時降低信心權重。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 核心詞彙與定義全錄：每個 PD Array 元素嘅完整原話引文（verbatim＋video id），包括入場確認三層口徑同實例引文備份。呢個係 skill 本地、自足嘅證據檔。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（ASR 容錯對照表，讀任何引文/逐字稿必查）。
- **Contributing videos（18，per profile §6.1）**：tCfmxMX5WaU（總綱）、xwsyfVf2l0k、ofQ--jkHTm4、whJg0lgPbFo、7dDW8tF1cZo、3Kt_ruGepB4、Q371XdV3apE、RjNBnZ59c4U、kI5idYixD50、E0PF_0XLDGo、B7rumsOw6_U、WmW5fQjK5Qg、zgVlK7UBNTY、teVdcguZs_U、aSZzhnfOVkE、7yDxPi7Roh0、_TEaFyv7-ac、yZoSW3DGRGI（流動性課程，貢獻 FVG/OB 價值判斷引文）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim，whitespace-join 可）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `.claude/skills/` 嘅上兩層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
