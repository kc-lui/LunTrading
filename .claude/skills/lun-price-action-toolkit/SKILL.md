---
name: lun-price-action-toolkit
description: 按照交易倫（Alan / LunTrading）的教法運用價格行為（price action）工具箱——K 線力度三分法、動能兩階段（積累/釋放）、圖形庫（頭肩形/旗形/三角形/通道/矩形/雙頂雙底）、時鐘法趨勢強度、BOS/CHoCH 結構判讀、EMA50/RSI/MACD/Pivot 過濾、13+ 種策略總綱（趨勢線破壞、Triple Test、破位/破位回調、倫敦破位、海龜湯 turtle soup、ICI）、Supply & Demand（供應需求）六招，以及進階諧波形態（harmonic patterns：蝙蝠/蝴蝶/Gartley XABCD 比例）。Use when reading candlestick momentum, chart patterns, 破位/breakout vs 假突破/fakeout, 供應需求/supply & demand zones, 動能/momentum phases, 諧波/harmonics, or picking a price-action strategy the way 交易倫 teaches. 唔覆蓋 PD Array 詞彙定義、流動性掃蕩機制、多時框分工、OTE 入場步驟同出場管理（見 sibling skills）。
---

# lun-price-action-toolkit：價格行為工具箱（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅第二層詞彙——形態、動能、結構與指標工具。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。唔好摻入 corpus 以外嘅通用價格行為教科書理論。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。佢嘅總定調：「其實我是動能交易。OK,我不太在乎趨勢,但是動能對我來說很重要」（qWMKL-p1MPE）。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 判讀 K 線動能強弱（力度三分法、強動能 K 線、Pin Bar／吞噬／晨星夜星）
- 判斷市場處於動能積累定動能釋放階段，決定可唔可以交易
- 識別同運用圖形（頭肩、旗形、三角形、通道、矩形、雙頂雙底、海龜湯 W/M、ICI）
- 判斷突破 vs 假突破（第一次破位懷疑、站得住、實體收盤規則）
- 用 EMA50／RSI／MACD／Pivot Point 做方向與動能過濾
- 由 13+ 策略總綱揀一套策略、決定破位定破位回調入場模式
- 執行 Supply & Demand 六招或（進階）諧波形態 XABCD 比例分析

**唔應該用嘅情況**：

- 定義 Order Block／FVG／Premium-Discount 等 PD Array 元素 → 用 `lun-ict-pd-arrays`（DRY：詞彙以該 skill 為準，唔好喺度重新定義）
- 流動性池位置、掃蕩/獵殺機制、「止損單＝聰明錢燃料」理論 → 用 `lun-liquidity-analysis`
- 日線→4H/1H→5分鐘三視角分工、A+ 四大標準篩選 → 用 `lun-multi-timeframe-analysis`
- Fibonacci 50–79% 回調入場四步驟 → 用 `lun-ote-entry-model`
- 止損擺法、止盈投射、平價保護、鎖利 → 用 `lun-exit-management`；倉位/風險% → 用 `lun-risk-management`
- 時段選擇（倫敦/紐約、10 點停手等） → 用 `lun-kill-zones-timing`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答；唔可以摻入 corpus 以外嘅通用價格行為理論（例如講者未教過嘅標準教科書形態統計、其他導師嘅 harmonic 比例變體）。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯**：讀逐字稿或引文前必須對照 `analysis/lun_trading_profile.md` §5 容錯表（搶動能＝強動能、Pinball/PIN吧＝Pin Bar、成星＝晨星、頭間形＝頭肩形、時光/實況/直框＝時框、OVERSOT＝Overbought/Oversold、Gutly/Gardly＝Gartley、輸走點＝樞軸點等）。
3. **Sibling 依賴**：PD Array 元素（OB/FVG/Breaker 等）作為 confluence 或目標時，定義一律引用 `lun-ict-pd-arrays`。本 skill 嘅策略幾乎全部內嵌「HTF 偏向→LTF 入場」流程——完整多時框分工歸 `lun-multi-timeframe-analysis`，此處只保留各策略指明嘅時框配置。
4. **策略索引表**（詳細規則見 evidence.md 對應節）：

| 策略/工具 | 一句定位 | 主要出處 |
|---|---|---|
| 動能兩階段框架 | 避開積累期、等強動能 K 線確認邊個控盤先入場 | rdXofMdxNEQ |
| 13/14 種策略總綱 | 趨勢線破壞、第三次觸碰、Triple Test、Divergence、London Breakout、多時框 Pin Bar、hit and run 等 | VjSB-VRyxWI |
| 8 個中長線策略 | 均線反轉、趨勢/籌碼消耗、通道、形態突破、動能持續、趨勢線破壞、Fibonacci ABC | 7yDxPi7Roh0 |
| 完整版四部分系統 | 日線 bias → 4H/1H 圖形 → 15m/5m 趨勢入場＋時鐘法 | pK6S7CEqMAk |
| 破位交易清單 | 偏向→回調（RSI 唔破 50）→再突破（RSI 近 70/30） | fTRv2HhTJUk |
| 突破/假突破判斷 | 第一次破位懷疑＋站得住 | JtPN1rBq5h0, yZoSW3DGRGI |
| 改良版倫敦破位 | 亞洲盤區間窄→破位；區間闊→假突破反做 | QZNzq-BunA4 |
| Pivot Point 系統 | daily/traditional、S3/R3 夠、碰 Pivot 有 rejection 先做 | 7j7_mhfda38 |
| Supply & Demand 六招 | 衝停衝 base、首次回踩、形態確認、confluence | teVdcguZs_U |
| 海龜湯（現代版） | 假突破前高/前低嘅 W/M 形態，5 分鐘入場 | qWMKL-p1MPE |
| ICI（自創） | Impulse-Correction-Impulse 三階段，只拿第二三波段 | OANImZtkkeM |
| 1H＋5M EMA 三線系統 | EMA 21/50/200 排列＋強動能推開＋RSI 過濾 | fLN20X1dP48 |
| Harmonic Patterns（進階） | 蝙蝠/蝴蝶/Gartley XABCD Fibonacci 比例 | 6_5DVT6uS9E（單源） |

## Workflow（分析流程）

分析一張圖表或者揀策略時，跟講者嘅決策鏈行：「就是你了解整体故事了之后」「你再找到你的偏向」「你才来找你的策略」「你才来找你的入场位置在哪里」（VjSB-VRyxWI）。

**Step 1 — 判斷市場階段（可唔可以交易）**

1. 動能兩階段：「市場動能主要分成兩個階段。」「動能釋放,以及動能積累。」（rdXofMdxNEQ）；積累期「波動是相當不穩定的,是非常沒有規律的」——「避開沒有動能的階段」。
2. 時鐘法量化趨勢強度（pK6S7CEqMAk transcript）：一點鐘＝破位交易「非常的賺錢」且止損唔使大；兩點鐘＝回撤力度大，止損要大啲、止盈唔好太大；**三點鐘＝橫盤，「所有的交易策略,所有的K線圖,所有的圖形都會失效」——暫時唔交易**；四點鐘＝初跌，止損保守啲；五點鐘＝強跌，止損唔使大。
3. Wyckoff 節奏交叉檢查（PypFn7GaVfE）：市場有四個循環（吸筹/拉升/派發/下跌），「價格行為的模式是完全不一樣的」——「你用錯市場結構」「你用錯節奏了」「還是要虧錢啦」。趨勢第五波段之後唔再做趨勢交易（s4on4yJCLII）。

**Step 2 — 定方向偏向（兩步法）**

- 「第一步就是你要判斷動能」→ 第二步「我們去用EMA50來判斷我們的趨勢」；「最好做的是,就是強動能突破加上EMA都一致性的話,這個機會就很完美了」（YeGLUuh3eCg）。方向唔一致或者唔清晰→跳過（「我們不要做」B7rumsOw6_U）。
- 均線參數係演化口徑（唔好抹平）：2023 年教 100 日平均線（rdXofMdxNEQ）→ 2025 起統一 EMA50——中長線「50天是非常有效率的...200天就太長,20天就太短」（7yDxPi7Roh0）、日內「其實EMA50來做日內交易是最適合不過的」（B7rumsOw6_U）；另有 5 分鐘 EMA 21/50/200 三線排列系統（fLN20X1dP48）。**預設用 EMA50（後期統一口徑），標註早期版本存在。**

**Step 3 — 讀 K 線與圖形（位置優先）**

1. 力度三分法：收盤價喺整根 K 線上三分之一＝強、中間＝neutral、底三分之一＝「非常弱的牛市K線」，特定條件下「我甚至可以把它當成是一根熊市的」K線（pK6S7CEqMAk transcript）；動能＝「當開盤架和收盤架的距離越遠的時候,動能就越強」。
2. 形態庫（每個形態＝一個動能故事）：頭肩形「所有圖形裡面最強的圖形」；Flag＝「動能累積」「趨勢繼續的一個休息站」；三角形＝「破位回調交易的最佳形態」；Channel＝「動能耗盡的一種表現」；Rectangle＝動能累積（pK6S7CEqMAk）。反轉 K 線：Pin Bar、吞噬（佢最喜歡嘅確認 K 線，xwsyfVf2l0k）、晨星夜星＝「動能轉換的形態」。
3. 鐵律：「重要的不是形態,重要的是這個形態在哪裡出現」（pK6S7CEqMAk）——形態必須出現喺關鍵位置（往左搵歷史主力區、支撐阻力、趨勢線、Pivot、PD Array 元素→定義見 `lun-ict-pd-arrays`）。
4. 結構判讀：上漲趨勢＝HH+HL，「價格永遠不可以打掉Higher Low」（ofQ--jkHTm4）；BOS＝「原本控盤的那一方還在控盤」；CHoCH＝「可能會出現一個反轉訊號。注意是可能。」（xwsyfVf2l0k）；有效突破要「實體是收盤在突破的外面」。

**Step 4 — 揀策略同進場模式**

1. 每個形態都有兩種進場（並列口徑，唔好抹平）：**直接破位**（止損較大但唔錯過）vs **破位回調**（止損較好、勝率較好但「有20%的机会价格是不做任何回调」）；講者現時個人偏向破位回調（VjSB-VRyxWI）——預設跟呢個偏好，除非用家接受錯過風險。
2. 破位交易必查清單（fTRv2HhTJUk）：①確認偏向（動能釋放＋EMA50）→②「一定要有回調」且回調動能唔可以強（做多 RSI「是不可以跌超過50的」、回調唔超過 EMA50）→③回調後再突破先入場（RSI 靠近 70/做空靠近 30）。失敗後第二次回調一樣冇碰 50 可以「給它多一個機會」。
3. 突破真假判斷：「第一次破位永遠不要直接判斷他是真實突破。」（JtPN1rBq5h0）；兩個條件——係咪「搶動能K線破壞」＋「它是否站得住」（yZoSW3DGRGI）；站唔住→反向交易；站得住→等新動能落細時框做順向破位。K 線收盤紀律：「我至少要等這一根K線收盤先」（B7rumsOw6_U；有經驗者可當收盤直接入場，QZNzq-BunA4）。
4. 承認主觀成分：「所有的交易策略都有80%的規則」「20%你需要主觀判斷」（QZNzq-BunA4）。

**Step 5 — 疊 confluence（分層口徑，唔好抹平）**

- 同一片內兩個數字都係原話：「最少有3到5個共識是跟我們交易的方向是一致性的」同「那我們最少需要2到3個拼圖都指著同一個方向」（teVdcguZs_U）。**按 profile §7.3.1 處理：2–3 為底線、3–5 為理想，並註明出處矛盾。**
- Confluence 素材清單（teVdcguZs_U）：圖形破壞、pivot、強動能 K 線、EMA 上下方、divergence、RSI 跌破 50；PD Array 元素亦可疊（→ `lun-ict-pd-arrays`）。
- 容錯：「如果有一兩個指標或者是圖形呢,是跟你想要交易的方向是相反的話,不要擔心。這並不夠讓你去停止交易。」（teVdcguZs_U）。
- 最低盈虧比門檻係情境分層（profile §7.3.2）：harmonic 1:1「有1比1其实就已经OK了」（6_5DVT6uS9E）／日內基準 1:2「因为我做不到一对二」「所以根本没有任何的意义」（RdnJw-mhwlE）／聰明錢框架偏好 1:3（xwsyfVf2l0k）。門檻揀邊層按策略類型講明；倉位數字歸 `lun-risk-management`。

**Step 6 — 檢查失效條件**

- 三點鐘橫盤＝全部工具失效（pK6S7CEqMAk）；「在沒有趨勢的情況下。在市場震盪的情況下。千萬不要用這個策略。完全沒有用的」（7yDxPi7Roh0，指 Fibonacci/圖形）；平衡區域「任何技術指標,均線還是RSI這些都是完全沒有什麼意義的」（xwsyfVf2l0k）。
- 觸碰遞減：「它觸碰的次數越多,它就會變得越弱」（xwsyfVf2l0k）；S&D「我們只做首次回踩的交易」（teVdcguZs_U）。
- 掛單時效示範口徑：「条件是6-8根K线里面」價格要碰到 Entry Line，否則撤單（RdnJw-mhwlE）。

### 進階子節：Supply & Demand 六招（teVdcguZs_U）

①趨勢反轉後**首次**形成嘅供應/需求區域→②辨認「衝停衝的停,也就是base,是最有交易價值的」並畫 base→③「耐心等待價格回踩」→④區內「等待一個形態出現」（佢最喜歡「突進破壞」＝圖形破壞）→⑤搵 confluence（見 Step 5 分層）→⑥「我們只做首次回踩的交易」。核心精神：「找到大訂單都藏在哪裡」；同 ICT「同根同源」。後備入場：止損太大做唔到一對二時，可遲啲喺右肩（FVG/OB 位）等 K 線確認再做——「會更安全」。

### 進階子節：Harmonic Patterns（6_5DVT6uS9E；單一影片來源，低信心）

> ⚠️ 全 corpus 只有一片教 harmonic，冇後續延伸；勝率宣稱（「勝率都有超過50%」）無樣本出處。使用前應按 `lun-backtesting-method` 驗證。定位：「你確實只能夠用Fibonacci去衡量，去判斷，到底哪裡可以入場，其他位置都不能入場」。

| 形態 | B 點（A→B 回調） | D 點（入場位） | 性格配對（講者口徑） |
|---|---|---|---|
| 蝙蝠 Bat | 50%，「可以超過50%，但是不可以碰到61.8%」（同片另有更嚴格 B 點口徑，全文見 references/evidence.md） | X→A 嘅 88.6——「價格一定要回測到88.6」 | 「蝙蝠形态的胜率会比较高」，適合保守交易員 |
| 蝴蝶 Butterfly | 「它直接去到了78.6」 | A→B 嘅 127.2 extension，「D点是超过X点的」 | 盈虧比最高、勝率可能最低、「最激进」（直接喺 D 位做） |
| Gartley | 「一定要回调到61.8」「不可以碰到78.6」 | A→B 嘅 127.2（B→C 回調亦要 61.8） | 「它的盈亏比都还不错」 |

通則：B→C 最少回調 38.2 且「不可以打破高位」（唔可以超過 A 點）；先要有動能釋放形成 X→A；**D 點必須實際觸及先入場——「不可以提早」**；止損放 X 點外；止盈 A→D 嘅 61.8（或 38.2）；盈虧比下限 1:1（呢個係 harmonic 情境嘅特例層，見 Step 5）。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅價格行為判讀。一份完整回覆應包含以下五部分，每部分引用對應規則（附 video id）：

1. **市場階段判定**：動能積累定釋放、時鐘方向（幾點鐘）、Wyckoff 節奏，同明確講可唔可以交易（三點鐘/震盪→唔做）。
2. **偏向**：動能＋EMA50 兩步法結論（做多/做空/冇方向唔做），註明用邊個均線口徑。
3. **形態與位置**：識別到嘅 K 線/圖形、力度評級（三分法）、以及**佢出現喺咩位置**（位置優先原則）；PD Array 元素只引用唔重定義。
4. **策略建議**：由索引表揀策略、講明進場模式（破位 vs 破位回調，預設佢偏好嘅後者）、confluence 清單（2–3 底線/3–5 理想）同適用嘅最低盈虧比層級。
5. **失效與轉介**：列明幾時作廢（觸碰次數、震盪、掛單時效），超出範圍嘅問題（流動性位置、時框分工、入場步驟、出場、倉位、時段）明確轉介對應 sibling skill，唔好即場作答。

## 實例（corpus 內示範）

### 例一：Russell 2000 1:22.45（WmW5fQjK5Qg，2026-01-05 實盤自述）

週線結構破壞＋回調釘形支撐 → 日線 1 月 2 號釘形喺 OB＋第二次觸碰 EMA50——「反轉訊號非常強,非常漂亮」→ 1 小時假突破後「搶動輪回流,回流到1小時的EMA50」兼支撐阻力轉換位做多——「滿滿的共識,滿滿的,就非常漂亮的位置」。示範重點：形態（釘形/假突破）×位置（OB/EMA50/SR轉換）×confluence 疊加，正係 Step 3–5 嘅完整鏈。

### 例二：黃金 Pivot 三步清單（7j7_mhfda38）

「因為第一步,我們有下跌的趨勢。第二步,價格現在在pivot以下。第三步,我們有假突破出現。」——趨勢＋位置＋觸發三步齊先入場；「當價格沒有在任何一個Pivot裡面的話,我們就不交易。」示範重點：檢查清單化決策，冇觸發條件＝唔做。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| OB/FVG/Breaker/Premium-Discount 等 PD Array 元素定義與品質檢查 | `lun-ict-pd-arrays`（DRY anchor） |
| 流動性池位置清單、掃蕩/獵殺機制、假突破背後嘅訂單博弈理論 | `lun-liquidity-analysis` |
| 三視角時框分工、A+ 四大標準（多時框同向/第三浪/高RR/催化劑）篩選 | `lun-multi-timeframe-analysis` |
| OTE 四步入場、Fibonacci 回調位執行細節 | `lun-ote-entry-model` |
| 止損三擺法、止盈兩法、80% 規則、平價保護、鎖利節奏 | `lun-exit-management` |
| 倉位公式、風險%、連虧降倉、止損 30 點上限 | `lun-risk-management` |
| 倫敦/紐約時段規則、10 點停手、數據日曆 | `lun-kill-zones-timing` |
| 100 筆挑戰、回測流程、策略逐一測試方法 | `lun-backtesting-method` |

## 侷限聲明

1. **ASR 來源**：所有引文出自本地 ASR 逐字稿，含系統性誤字（搶動能＝強動能、Gutly＝Gartley、頭間形＝頭肩形等）；引用照錄原文，正字對照必查 profile §5。fTRv2HhTJUk 中後段逐字稿碎片化嚴重（「!」分隔）。
2. **教學示範值，非驗證統計**：所有盈虧比例子（1對4.8、一對七、1:22.45 等）同勝率宣稱（harmonic >50%、ICI 50-60%、「80%的機會回調」，以及最大宣稱 Triple Test 「一对二十」/VjSB-VRyxWI）均為講者示範或自述經驗值，無樣本出處，未經獨立對帳（profile §7.4）。
3. **矛盾口徑照錄**：confluence 2–3 vs 3–5（同片）、最低盈虧比 1:1/1:2/1:3、均線 100日→EMA50→21/50/200、破位 vs 破位回調——全部按情境分層呈現，唔好將任何一層當成唯一規則。
4. **Harmonic 單源**：6_5DVT6uS9E 係唯一來源，冇後續影片延伸，信心權重最低；ICI 係自創形態，同樣只有單片完整教學（OANImZtkkeM，另 7yDxPi7Roh0 有 ASR 疑似「ICI模型」＝Fibonacci ABC 嘅重述）。
5. **筆記覆蓋警告**：per profile §7.2，量化等待時間同例外規則（等幾多根 K 線等）筆記捕捉不足；已知嘅有 6-8 根 K 線掛單時效（RdnJw-mhwlE），其他需要精確數字時應回讀 `data/transcripts/` 覆核。
6. **動能回流完整清單唔喺公開 corpus**：WmW5fQjK5Qg 明言「細節我就不多講了,有興趣可以直接進入交易輪交易班去學習」——本 skill 只覆蓋公開嘅價格行為工具，動能回流公開骨架歸 `lun-multi-timeframe-analysis`。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 價格行為工具箱證據全錄：動能兩階段、K 線力度、圖形庫、結構/時鐘法、指標、破位/假突破、策略總綱、S&D 六招、海龜湯、ICI、Harmonic、Wyckoff、失效條件與矛盾口徑嘅完整原話引文（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（ASR 容錯對照表，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3。
- **Contributing videos（29＋1，per profile §6.3）**：pK6S7CEqMAk（主幹）、VjSB-VRyxWI（策略總綱）、7yDxPi7Roh0（8 個中長線策略）、teVdcguZs_U（S&D）、OANImZtkkeM（ICI）、qWMKL-p1MPE（海龜湯）、QZNzq-BunA4（倫敦破位）、fTRv2HhTJUk（破位清單）、rdXofMdxNEQ（動能）、fLN20X1dP48、YeGLUuh3eCg、B7rumsOw6_U、GINdJCIIEvw、hmpAys3lJEo、JtPN1rBq5h0、WmW5fQjK5Qg、zgVlK7UBNTY、xwsyfVf2l0k、tCfmxMX5WaU、ofQ--jkHTm4、RdnJw-mhwlE、s4on4yJCLII、T2Nk46EqAh4、hkCvRoLc3Nk、7j7_mhfda38、k0ESC6XYz50、PypFn7GaVfE（Wyckoff 交叉引用）、yZoSW3DGRGI、6_5DVT6uS9E（harmonic 子節，+1 吸收自 lun-harmonic-patterns 提議）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim，whitespace-join 可；本 skill 已覆核 pK6S7CEqMAk 嘅時鐘法與力度三分法段落）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `.claude/skills/` 嘅上兩層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
