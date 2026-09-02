---
name: lun-liquidity-analysis
description: 按照交易倫（Alan / LunTrading）的教法做流動性分析——三種訂單與止損單＝突破單的訂單博弈機制（「你的止損點是我的入場點」）、BSL/SSL 流動性池位置清單（昨日/上週/上月/session 高低位、支撐阻力、轉折點）、內外部與高低壓力流動性、三種流動性形態（獵殺/假突破/突破）與「站得住」機制判斷、掃描後的銜接與進階工具（Order Flow/Volume Profile/Heatmap）。Use when analysing liquidity / liquidity pools（流動性池）/ stop hunt（止損獵殺）/ sweep（流動性掃描）/ 假突破 fakeout mechanics / buy-side & sell-side liquidity / equal highs-lows（重疊流動性；alias，非講者用語）the way 交易倫 teaches, or answering 「流動性在哪裡」「點解一入場就被掃損」. 唔覆蓋 PD Array 詞彙、策略入場模式、OTE 步驟、時段與出場管理（見 sibling skills）。
---

# lun-liquidity-analysis：流動性分析（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅訂單博弈/流動性機制層——佢比賽奪亞嘅招牌能力。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。唔好摻入 corpus 以外嘅通用 ICT 流動性理論。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。佢嘅總定調：所有工具「都是在回答一件事情Ｖ流動性在哪裡」（yZoSW3DGRGI）。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 解釋「點解一入場就被掃損／方向啱都先虧錢」——訂單匹配、止損單＝突破單、聰明錢燃料嘅機制
- 喺圖表上標記流動性池（BSL/SSL、昨日/上週/上月高低位、session 高低位、支撐阻力、轉折點、重疊位）
- 判斷價格下一步去向（高流動性→低流動性、內部→外部、低壓力位遲早被掃）
- 判別三種流動性形態（獵殺/假突破/突破）同用「站得住」做真假突破嘅機制判斷
- 解釋假突破背後嘅訂單博弈（`lun-price-action-toolkit` 對呢層明確轉介到本 skill）
- 評估進階工具（Order Flow / Volume Profile / Footprint / Heatmap）可以答咩、答唔到咩

**唔應該用嘅情況**：

- 定義 OB/FVG/Premium-Discount 等 PD Array 元素 → 用 `lun-ict-pd-arrays`（DRY：掃描目標涉及 PD Array 時只引用唔重定義）
- 突破/假突破嘅策略執行（破位清單、K 線收盤紀律、海龜湯/S&D 入場模式）→ 用 `lun-price-action-toolkit`
- 掃描後嘅完整入場四步（回調 50–79%、第三浪、共識疊加）→ 用 `lun-ote-entry-model`
- 獵殺時段、Weekly Profile 週節奏、數據日曆佈局 → 用 `lun-kill-zones-timing`
- 止盈標準差投射、平價保護、分批 → 用 `lun-exit-management`；時框分工 → 用 `lun-multi-timeframe-analysis`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答；唔可以摻入 corpus 以外嘅通用 ICT 流動性理論（例如講者未教過嘅 equal highs 專門術語、draw on liquidity 教科書講法、SMT divergence）。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯**：讀逐字稿或引文前必須對照 `analysis/lun_trading_profile.md` §5 容錯表（裂殺/列殺/劣殺＝獵殺、聰明前＝聰明錢、高地位＝高低位、少掉＝掃掉、扭動性＝流動性、紙銀/紫銀＝止盈、出发＝觸發、被焊了/被控到＝被 hunt 到）。
3. **Sibling 依賴**：本 skill 係「價格會去邊、幾時唔好信破位」嘅機制層；掃描確認後嘅執行全部轉介 sibling（POI 定義→`lun-ict-pd-arrays`、入場→`lun-ote-entry-model`、出場→`lun-exit-management`）。Sibling 講到「流動性掃描」「獵殺」「止損獵殺位」時，以本 skill 定義為準（DRY）。
4. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 流動性 | 「買家跟賣家之間的博弈」；「流動性就是訂單」；能否喺最短時間成交 | aSZzhnfOVkE, xwsyfVf2l0k, yZoSW3DGRGI |
| 三種訂單 | 市價單／限價單（保證價格唔保證成交）／突破單（Stop Order，觸發前唔喺賬本） | whJg0lgPbFo, yZoSW3DGRGI |
| 止損單＝突破單 | 「止损单其实就是一个突破单」；止盈用限價單、止損用 Stop Order | whJg0lgPbFo, yZoSW3DGRGI |
| BSL / SSL | 聚集喺高位上方外面嘅 Buy Stop 單／低位下方嘅賣方流動區 | yZoSW3DGRGI, whJg0lgPbFo, 7dDW8tF1cZo |
| 流動性池位置 | 支撐阻力位、轉折點、昨日/上週/上月高低位、亞洲/倫敦/紐約盤高低位 | yZoSW3DGRGI, aSZzhnfOVkE, whJg0lgPbFo |
| 內部/外部流動性 | 「內部的流動性被裂殺掉Ｖ價格就會前往外部的流動性」（單源低信心） | yZoSW3DGRGI |
| 高低壓力流動性 | 價格由高壓力（已掃）流動性去低壓力（未掃）流動性；低壓力位「迟早被扫到」 | whJg0lgPbFo, yZoSW3DGRGI |
| 三種流動性形態 | 獵殺（一根K線/長引線急衝急回）／假突破（徘徊 2-3 根K線先跌回）／突破（Liquidity run） | yZoSW3DGRGI |
| 站得住 | 破位後反向動能壓唔低太多＝真突破；等新動能確認延續 | yZoSW3DGRGI, JtPN1rBq5h0 |
| 流動性掃描（sweep） | 關鍵高低位被掃走止損單嘅假突破動作；掃描＋反轉＝最好時機 | xwsyfVf2l0k, whJg0lgPbFo, E0PF_0XLDGo |
| 獵殺（stop hunt） | 「就是我們所謂的直勝獵殺」＝止損獵殺；早期版叫 Liquidity Hunting——「就是假突破的一種形態」 | kI5idYixD50, _TEaFyv7-ac |
| Engineered Liquidity | ＝Accumulation Zone 動能累積形態，「其實是一樣的東西」（單源低信心） | ofQ--jkHTm4 |

## Workflow（分析流程）

對一張圖表做流動性分析時，按次序行以下步驟：

**Step 1 — 由訂單機制起步（點解會有掃損）**

理解基礎：「你们一定要搞懂订单是怎么样子去匹配的」（whJg0lgPbFo）。散戶止損集中喺同一啲位（「基本上大家止损点其实都会放在同一个位置」），而止損單本質係突破單——所以「我们的止损点其实就是聪明前的进场燃料」（whJg0lgPbFo）。呢個唔係陰謀：「這並不是什麽陰謀�而是�不到單子�最多的地方�他們沒有辦法建立」佢哋需要嘅倉位（yZoSW3DGRGI）。分析語氣保持市場中性——「它只是一台會利用人性的機器。」（xwsyfVf2l0k）。

**Step 2 — 標記流動性池（地圖）**

逐項標記（愈大級別愈有價值）：

- [ ] 明顯支撐阻力位＋每個轉折點（Swing High/Low）（yZoSW3DGRGI）
- [ ] 昨日／上週／上月高低位（yZoSW3DGRGI, aSZzhnfOVkE；7dDW8tF1cZo 建議用 Hilo Yesterday/Last Week/Last Month 指標）
- [ ] 亞洲盤／倫敦盤／紐約盤高低位（whJg0lgPbFo, aSZzhnfOVkE；session 具體時間歸 `lun-kill-zones-timing`）
- [ ] 支撐阻力轉換位（JtPN1rBq5h0）
- [ ] 級別過濾：「它一定要是大石框的高地位。」單一 4 小時 K 線嘅高低位唔算（7dDW8tF1cZo）
- [ ] 重疊優先：「那这些重叠的位置」「迟早会被扫到」（whJg0lgPbFo）；重疊位「強動能釋放一來的時候呢,全部都會被掃完的」（zgVlK7UBNTY）

**Step 3 — 分類與去向判斷（價格要去哪裡）**

核心規律：「價格會從高流動性去Ｖ低流動性的位置」（yZoSW3DGRGI）；已掃＝高壓力、未掃＝低壓力，「这些低压力的位置」「迟早被扫到」（whJg0lgPbFo）。內部流動性被掃→前往外部流動性（yZoSW3DGRGI，單源低信心）。呢條規律唔分時框、唔分品種：「不管什麼图表�就算是指數Ｖ也是一樣的」（yZoSW3DGRGI, transcript）。分析時模仿佢嘅自問自答：「價格要去哪裡」→「它就要去找低流動性的區域」。破位可靠性推理：「價格從高流動性。去另外一個高流動性。中間呢。通常都是流動性比較低的。所以這個時候的破壞交易是比較可靠的。」（JtPN1rBq5h0）。

**Step 4 — 判別形態（價格到達流動性池後發生咩事）**

兩套口徑並列（同源但切面唔同，唔好合併抹平）：

| 口徑 | 內容 | 出處 |
|---|---|---|
| 三種流動性形態 | ①獵殺：一根K線/長引線急衝急回（有內部結構獵殺 vs 外部結構獵殺之分）②假突破：突破後徘徊 2-3 根K線先加速跌回 ③突破（Liquidity run） | yZoSW3DGRGI |
| 池上三種行為 | ①假突破 ②暫時停留喺流動性池 ③直接突破流動性池；「最好的時機就是我們可以看到流動性掃描出現的時候。」 | xwsyfVf2l0k |

真假突破機制檢查（兩條件，yZoSW3DGRGI）：①「它是否是搶動能K線破壞」；②「它是否站得住」——真突破係「它破壞了之後Ｖ熊市K線Ｖ並沒有很長」而順向動能較強 (transcript)；相反「牛市動能Ｖ跟熊市的動能都一樣強Ｖ它就只是一個Ｖ假突破的前兆」(transcript)；「真正的突破�它一定是加速離開的Ｖ非常強大」(transcript)。JtPN1rBq5h0 同口徑：站得住＝反向強動能「壓不了太多」，等新動能確認延續。反應判讀三情境（aSZzhnfOVkE）：強力壓回＝該邊賣家強、跌破後徘徊＝反手搵對向機會、完全唔回頭＝「這個時候做的破壞交易就特別的有效」。決策鐵律（執行細節歸 `lun-price-action-toolkit`）：「第一次破位永遠不要直接判斷他是真實突破。」（JtPN1rBq5h0）。

**Step 5 — 佈局定等待（兩個口徑並列，唔好抹平）**

- **先佈局（允許）**：「我们就可以提前去做布局」，等掃描出現後跟掃描方向走（whJg0lgPbFo）
- **等確認（冇判斷時嘅預設）**：「那如果没有这样子的判断的话」「那我们可以等」「等多几根配线」（whJg0lgPbFo）；用警報器代替盯盤——價格碰到先睇、等 K 線收盤先決定（yZoSW3DGRGI）

主次判斷：「最重要的其实是这两个」——上下方流動性＋流動性掃描；其他概念「其实这一些还好」（whJg0lgPbFo）。

日常應用形態（Daily Bias，RjNBnZ59c4U）：本 skill 嘅機制層日日重用——「只是Daily Bias比较注重是高地位」「然后流动性扫描」「然后再去低死矿找结构破坏」「然后再做FEG那边入场」（低死矿＝低時框、FEG＝FVG）；而且偏向會隨新掃描反轉：「如果有流动性扫描的话那我的偏向会重做多变成做空就这么简单」。唔對稱優勢：「但是如果你的偏向错了」「入场条件没有满足的话」「你不会亏」。

**Step 6 — 掃描確認後嘅銜接（全部轉介）**

掃描＋結構轉換出現後：落更低時框（4H/30m→15m 級別）搵 FVG/Order Block 做 POI（whJg0lgPbFo；元素定義→`lun-ict-pd-arrays`；四步入場→`lun-ote-entry-model`）；止盈方向「在下一个流动性区域就好了」（whJg0lgPbFo），投射錨一定係「掃描的那一個角」（Q371XdV3apE；標準差投射→`lun-exit-management`）；入場後出現反向掃描必須平價保護（xwsyfVf2l0k→`lun-exit-management`）。OB 價值必須配合流動性睇——就算 OB 出現喺前高位，「不重要的Ｖ價格還是一樣會流動性掃描」（yZoSW3DGRGI, transcript）。

**Step 7 — 進階工具（單源低信心，選修）**

Order Flow（睇邊個價位成交量最高）、Value Area High/Low（只睇已形成嘅 profile，「我們不會看Ｖ當下的Volume Profile」）、Footprint、Liquidity Heatmap（睇過去限價單掛喺邊；限制：「價格是看不到止损單的」）——全部只有 yZoSW3DGRGI 一片教授。定位警告照錄：「但是它會給到你絕對的優勢嗎�不會」；「主要的還是你的整個交易思路Ｖ你的交易框架�還有你的執行力」。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅流動性判讀。一份完整嘅流動性分析回覆應包含以下五部分，每部分引用對應規則（附 video id）：

1. **流動性地圖**：已標記嘅流動性池清單（類型、價格範圍、級別、係咪重疊位），並講明邊啲已被掃（高壓力）、邊啲未被掃（低壓力）。
2. **去向判斷**：按「高流動性→低流動性」規律講價格最可能被吸引去邊個池，附推理（內部→外部、低壓力遲早被掃）。
3. **形態判定**：目前係咪已出現獵殺/假突破/突破；真假突破用兩條件（強動能破壞＋站得住）逐項核對，講明仲欠咩確認（例如等反向動能測試）。
4. **行動銜接**：講明下一步應該轉介邊個 sibling skill（掃描確認→OTE 入場、目標→出場管理、時段→kill zones），唔好即場代答超範圍問題。
5. **警告與失效**：提醒「就算你的偏向是對的,你還是會先虧錢先」嘅時機風險（aSZzhnfOVkE）、第一次破位懷疑鐵律、以及冇掃描就冇高質量確認（「沒有掃描,沒有交易」E0PF_0XLDGo）。

## 實例（corpus 內示範）

### 例一：昨日高位反應判讀（aSZzhnfOVkE）

標記昨日高低位後觀察觸及反應：「價格其實碰到了昨日的高位之後,馬上被強動能壓下來」→ 結論「我們可以知道這一邊是充滿著大量非常強的賣家」→ 偏空搵入場；隔天價格重返同一位置再被推低——「這邊的流動性還沒有被清除了。所以價格又被推下來了」。示範重點：流動性位＋觸及反應＝買賣家強弱結論，之後「你只需要跟著你原本的交易體系去做一個調整」。

### 例二：黃金 30 分鐘真假突破（JtPN1rBq5h0）

30 分鐘圖見破位 → 唔即入（「第一次破位永遠不要直接判斷他是真實突破。」）→ 自問「流動性在哪裡。昨日的高低位。還有嗎?或許是支撐阻力轉換。」→ 睇站唔站得住：「看到它站不住了之後。那我們可以做反向交易。或者是它站得住。那我們等待破壞。然後我們直接抓下一波動能。」→ 站得住就落 5 分鐘搵順向破位（30m→5m、1h→15m 比例），目標下一個流動性位，「你就抓一個1比2就好。」示範重點：本 skill 嘅機制判斷點樣直接餵入策略執行層。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| OB/FVG/Breaker/Premium-Discount 定義與品質檢查 | `lun-ict-pd-arrays`（DRY anchor） |
| 破位清單、海龜湯、S&D 等策略入場模式；K 線收盤/實體突破紀律 | `lun-price-action-toolkit` |
| 掃描後回調 50–79%、第三浪、共識疊加嘅入場四步 | `lun-ote-entry-model` |
| 獵殺時段時間表、Weekly Profile 三形態、數據日曆佈局 | `lun-kill-zones-timing` |
| 標準差投射、平價保護、分批、鎖利 | `lun-exit-management` |
| 三視角時框分工、A+ 篩選 | `lun-multi-timeframe-analysis` |
| 倉位/風險%、盈虧比門檻總表 | `lun-risk-management` |

## 侷限聲明

1. **ASR 來源**：所有引文出自本地 ASR 逐字稿，含系統性誤字（裂殺＝獵殺、聰明前＝聰明錢、高地位＝高低位等）；yZoSW3DGRGI 逐字稿夾雜「�」「Ｖ」雜訊分隔符，引用照錄原文，正字對照必查 profile §5。
2. **比賽亞軍流動性系統規則未公開**：PypFn7GaVfE 同 aSZzhnfOVkE 只講定位（「這就是我去參加比賽用的一個主要框架」），具體入場/出場規則留喺交易班（profile §7.1）——本 skill 只覆蓋公開嘅機制層，唔好扮演已知完整系統。
3. **單源低信心元素**（每項只有一片來源，使用時降權）：內部/外部流動性（yZoSW3DGRGI）；Engineered Liquidity＝Accumulation（ofQ--jkHTm4）；進階工具四件套連 Heatmap 限制（yZoSW3DGRGI）；三種反應判讀嘅完整三分法（aSZzhnfOVkE；xwsyfVf2l0k 嘅池上三行為屬近義旁證）；Weekly「沒有掃描,沒有交易」（E0PF_0XLDGo，主體歸 `lun-kill-zones-timing`）。
4. **教學示範值，非驗證統計**：所有盈虧比例子（1比2、1比3、1比7 等）同「你的勝率會提高」「勝率就會變得比較高了」等講法均為講者示範或自述，無樣本出處，未經獨立對帳（profile §7.4）。
5. **矛盾/多口徑照錄**：三種流動性形態（yZoSW3DGRGI）vs 池上三行為（xwsyfVf2l0k）係兩個切面，唔好合併；先佈局 vs 等確認兩個口徑並列；盈虧比 1:2（流動性/破位語境）vs 1:3（聰明錢框架偏好）按情境分層（profile §7.3.2）。
6. **筆記覆蓋警告**：per profile §7.2，「徘徊幾多根 K 線先算假突破」等量化門檻筆記捕捉不足（yZoSW3DGRGI 只講「可分 2-3 根 K 線發生」）；需要精確數字時應回讀 `data/transcripts/` 覆核，並按 `lun-backtesting-method` 做樣本驗證。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 流動性分析證據全錄：訂單機制、止損＝燃料、BSL/SSL 與位置清單、內外部/高低壓力、三形態與站得住、池上行為判讀、掃描銜接、Engineered Liquidity、進階工具、佈局口徑、盈虧比情境層、心態去陰謀論、比賽系統定位嘅完整原話引文（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（ASR 容錯對照表，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3；比賽系統未公開邊界依據 §7.1。
- **Contributing videos（20，per profile §6.2）**：yZoSW3DGRGI（完整課程，2026-08-28 壓軸教材）、whJg0lgPbFo（訂單機制）、aSZzhnfOVkE（博弈入門）、JtPN1rBq5h0（突破/假突破）、xwsyfVf2l0k（聰明錢完整版）、_TEaFyv7-ac（stop hunting 早期版）、qWMKL-p1MPE（獵殺實戰應用）、E0PF_0XLDGo、RjNBnZ59c4U、kI5idYixD50、3Kt_ruGepB4、7dDW8tF1cZo、fTRv2HhTJUk、ofQ--jkHTm4、Q371XdV3apE、tCfmxMX5WaU、teVdcguZs_U、PypFn7GaVfE、WmW5fQjK5Qg、zgVlK7UBNTY。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim，whitespace-join 可；本 skill 已覆核 yZoSW3DGRGI 嘅訂單類型、BSL、三形態、站得住段落）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `.claude/skills/` 嘅上兩層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
