---
name: lun-risk-management
description: 按照交易倫（Alan / LunTrading）嘅風險管理體系做資金與風險層分析——防守哲學（保護資金＋保護心態、「活下去你就有機會」）、倉位計算公式（資金×風險%÷止損點數）、單筆風險多口徑（教學 1%–2% vs 自用 <0.25% vs 實盤覆盤 1%，平行呈現唔裁決）、等額風險鐵律與大回撤唯一例外、連虧降倉（0.5%–0.25%）、最大風險暴露、虧 30% 停手出金、本金只用虧得起嘅 10–30%、「不熟,不做」、交易頻率即風控（月 3–5 筆）、大盈虧比作連虧保險嘅數學、常見錯誤目錄（10 錯誤／3 致命失誤／6 迷思）。Use when 風險管理 risk management, 倉位 position sizing 倉位計算, 每筆風險% risk per trade, 回撤 drawdown 連虧 losing streak, 資金管理 capital management money management, 爆倉 blow up, 保護本金 capital preservation, 風險暴露 risk exposure, 停手規則 stop-trading rules, 過度交易 overtrading, 常見錯誤 common trading mistakes the way 交易倫 teaches. 唔覆蓋止損/止盈放置（exit-management）、prop firm 特定上限（prop-firm-playbook）、RR 門檻分層（exit-management）、A+ 交易過濾（multi-timeframe-analysis）。
---

# lun-risk-management：風險管理（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅**跨切資本/風險規則層**——覆蓋率全 corpus 最高（31/57 份筆記）。佢嘅風控唔係一條公式，而係一套防守哲學：「風險管理其實是交易的命脈。」（rLP-MPvGmDE）、「良好的風險管理是讓你不爆倉的最主要原因。活下去你就有機會。」（eIeYQStY5rI）。**本 skill 嘅核心發現**：佢嘅教學口徑（1%–2%）同佢自述最低嘅自用口徑（<0.25%，2025-10）相差 4–8 倍，而最近一次實盤覆盤（MjPZizFnX-E，2026-04）自報用嘅係固定 1%——多個口徑喺 corpus 內並存，必須平行呈現，唔可以合併、唔裁決邊個先係佢真正嘅取態（見 Workflow Step 3）。因為 9 個 sibling skills 已各自持有本域，本 skill 只持有**資本層**規則，其餘一律路由（見 Step 0）。所有引文照錄筆記/逐字稿原文（含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 建立或審視**資本保護哲學**：點解防守先於進攻、保護資金同保護心態係同一件事
- 計**倉位大小**：資金 × 風險% ÷ 止損點數嘅公式應用
- 決定**單筆風險 %**：理解教學口徑（1%–2%）同自用口徑（<0.25%）嘅差異同各自適用場景
- 執行**等額風險鐵律**：點解每筆風險必須一樣、唯一例外（大回撤主動降風險）幾時觸發
- 應對**連虧／回撤**：降倉規則（0.5%–0.25%）、同形態連虧兩單停手、虧 30% 停手出金、大盈虧比作連虧緩衝嘅數學
- 管理**總風險暴露**：唔好同時全開多單、日內止損 30 點上限（單源）
- 規劃**本金配置**：只用虧得起嘅 10–30%、「不熟,不做」、守住本金與累積觀
- 用**交易頻率做風控**：月 3–5 筆高質量交易勝過頻繁交易、識別垃圾交易同過度交易
- 對照**常見錯誤目錄**：10 個錯誤／3 個致命失誤／6 個迷思嘅風控相關條目

**唔應該用嘅情況（路由表，DRY 硬規則）**：

- 止損放邊／止盈點邊度／保本／分批／幾時提前走 → `lun-exit-management`（本 skill 只持有**止損 30 點上限**呢個風險 cap，唔持有放置方法）
- RR 門檻分層（1:1／1:2／1:3 按情境）同 RR↔勝率取捨規則本體 → `lun-exit-management`（本 skill 只引用大盈虧比嘅**連虧保險數學**）
- Prop firm／考試場景嘅**應用**（考試 1%、撥資機構 ≤1%、連虧 5 單砍半、唔過夜、考試倒推計劃）→ `lun-prop-firm-playbook`；注意：0.25%→1% 嘅漸進 baseline（rE21_onS0uo）**留喺本 skill**（Step 3 口徑 #3），prop-firm skill 只持有佢喺考試/撥資場景嘅落地
- 交易質量過濾（A+ 四大標準：多時框同向／第三浪／高RR／催化劑）→ `lun-multi-timeframe-analysis`（本 skill 只持有**頻率即風控**呢一層）
- 系統信心數據（預期連敗／樣本量／回測驗證）→ `lun-backtesting-method`
- 時段紀律（晚上 10 點後不開新單等時間規則）→ `lun-kill-zones-timing`
- 情緒機制本身（FOMO／報復交易／mental capital／過度盯盤嘅心理成因）→ lun-trading-psychology（生成中）

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答。教科書風控方法一律唔准補完：**Kelly criterion、VaR、fixed-fractional／fixed-ratio 理論、ATR-based sizing、portfolio heat、相關性對沖、Monte Carlo 回撤模擬——corpus 全部冇教，唔准引入**。組合/相關性管理 corpus 只有一句「不熟,不做」嘅配置原則（profile §7.1.5）。
2. **多口徑紀律（本 skill 核心硬規則）**：單筆風險 % 必須以**教學口徑 vs 自用口徑 vs 實盤口徑**平行呈現（Step 3），唔可以合併成單一建議數字，唔可以話佢教 1–2% 所以照用 1–2% 而唔披露自用/實盤口徑，亦唔可以話佢實際用 <0.25% 而唔披露最近實盤覆盤係 1%。
3. **ASR 容錯**：盈盔比/盈窥比/盈盈比/盈益比/銀規比＝盈虧比、止损點/直送點/殖存点/支撐點（語境）＝止損點、比＝筆、巴仙＝percent、過利＝獲利、賭信＝賭性、評價保護＝平價保護、希望值＝期望值、教育＝交易、Pore to those zones＝Paul Tudor Jones。全表見 `analysis/lun_trading_profile.md` §5。
4. **引用紀律**：「」內文字必須照錄筆記/逐字稿原文；編輯標籤（如**教學口徑**／**自用口徑**）用粗體唔入「」；一切推論帶（推測）標記；單源子節帶（單源）標記；自述績效帶「自述，未對帳」。
5. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 倉位計算 Formula | 資金 × 風險%（0.01/0.02）＝可虧金額，再 ÷ 止損點數得出 Lot Size | hkCvRoLc3Nk |
| 等額風險 | 「每一筆風險的大小要一樣」，否則概率模型毀掉 | 54WCm_VBYfY |
| Risk Exposure | 同時開倉嘅總風險上限，要預先自定 | rE21_onS0uo, rLP-MPvGmDE |
| 連虧降倉 | 連續虧損後強行拉低倉位至 0.5%–0.25% | HeQiNekCZng |
| 停手線 | 自有資金虧 30% 即出金停手休息 | rE21_onS0uo |
| 垃圾交易 | 「基本上沒有催化劑的交易,都是垃圾交易」（過濾標準本體 → `lun-multi-timeframe-analysis`） | k0ESC6XYz50 |
| 防守 | 「保护自己的资金,保护自己的心态」 | jlO3771JF1E |

## Workflow（分析流程）

按資本層決策順序行：路由檢查 → 哲學定調 → 本金配置 → 風險% → 倉位公式 → 等額鐵律 → 連虧應對 → 暴露與頻率 → 錯誤對照。

**Step 0 — 路由檢查（先分流，後分析）**

問題係咪真係資本層？止損放置／出場 → `lun-exit-management`；考試規則 → `lun-prop-firm-playbook`；做唔做呢筆 → `lun-multi-timeframe-analysis`；情緒本身 → lun-trading-psychology（生成中）。只有**虧幾多、開幾大、幾時停**留喺本 skill。

**Step 1 — 防守哲學定調**

- 命脈觀：(transcript)「風險管理其實是交易的命脈。」「你沒有資金你就出局了,」（rLP-MPvGmDE）；(transcript)「活下去你就有機會。」「如果你在90天內就爆倉了,那你就出局了」（eIeYQStY5rI）。
- 雙重保護：「你要做到保护自己的资金,保护自己的心态」（jlO3771JF1E）——資金同心態係同一條防線；反面教材係佢本人「我损失了超过80万美金,用个8个月的时间」（jlO3771JF1E，自述）。
- 核心心法（引 Paul Tudor Jones，ASR 作「Pore to those zones」）：(transcript)「不要專注在賺錢,我們要專注在保護我們已經擁有的」（HeQiNekCZng）。
- 三角缺一不可：「如果你有很好的策略,但是你的風險管理不好,你還是會虧錢啊」；反之技術差但風控情緒好「至少還是在一個不賺不賠的情況」（H3OZxavXlsk）。

**Step 2 — 本金配置：只用虧得起嘅錢**

- 上限：「不要把全部东西都压在交易里面」，本金用「可能10-30%」你虧得起嘅錢（s4on4yJCLII，單源數字）；「交易是个双刃剑」。
- 練習路徑：「所以模拟小资金大资金」「这个才是最踏实的」（s4on4yJCLII；系統驗證方法 → `lun-backtesting-method`；由零三步框架 → `lun-prop-firm-playbook`）。
- 配置原則：「你要分散投資,但是你要做你熟悉的領域」「不熟,不做」（0a4NrcfAPJU，單源）——反面教材係佢重倉不熟領域「因為這一個投資我損失了大部分的財富」（自述）。
- 守本金與累積：「財富的秘訣是什麼?是累積」「那些失敗的,都是守不住本金的人」；反賭博鐵律「不要逃避,不要把交易變成賭博,想要靠賭來翻身」（48pCaOfGGmA）。

**Step 3 — 單筆風險 %：雙口徑平行呈現（本 skill 核心發現）**

| 口徑 | 數字 | 原話 | 出處 |
|---|---|---|---|
| **教學口徑** | 1%–2%（一處放寬到 3%） | (transcript)「每一筆就是1%到2%的風險」(transcript)「我不管你用1%還是2%,記住,定了,就不要再改」 | HeQiNekCZng（2026-01）；hkCvRoLc3Nk（2024-06）；(transcript)「單比風險你可以用1%或者是2%、3%都OK。」fLN20X1dP48（2025-03） |
| **自用口徑** | <0.25% | (transcript)「我每天每一單的風險其實少過0.25%的」 | ryv0CUgVZCM（2025-10）；另過去自述「我過去交易的單比風險都是控制在2%以內」OANImZtkkeM |
| **漸進口徑** | 0.25% → 1% | 新系統起步 (transcript)「如果你的單比風險是0.25%的話」可收集 40 筆數據，有信心先加大到 1%（**本 skill 持有**呢個 baseline；佢喺考試/撥資場景嘅落地 → `lun-prop-firm-playbook`） | rE21_onS0uo（2025-08） |
| **實盤口徑** | 固定 1%（1R＝1%） | (transcript)「今天這支影片我們會用R來代替,一個R代表1%」（Q1 實績覆盤；自述，未對帳；分母 caveat 見侷限聲明 4） | MjPZizFnX-E（2026-04） |

- **教學 vs 自用（Tier 1a）**：兩個口徑同期並存（HeQiNekCZng 2026-01 教 1–2%；ryv0CUgVZCM 2025-10 自報 <0.25%），差距 4–8 倍，**唔係演化係分層**——唔可以合併，唔可以只引其一。
- **自用 vs 實盤（Tier 1b）**：<0.25%（ryv0CUgVZCM，2025-10）同固定 1%（MjPZizFnX-E，2026-04）**同屬自述**、相隔約 6 個月、相差 4 倍——corpus 冇解釋係口徑收窄定場景唔同（推測：可能係唔同帳戶/資金規模嘅唔同設定），**平行呈現唔裁決**；引述佢本人實際用幾多時，兩個數字必須一齊報。
- （推測）教學/自用差異嘅可能解釋：佢管理嘅資金規模大（prop firm 放大後 0.25% 絕對金額已經可觀），且 rE21_onS0uo 明示新系統/新環境起步就係 0.25%——教學嘅 1–2% 係畀已驗證系統嘅一般散戶口徑。呢個調和係推測，corpus 冇明講。
- 定咗就唔好改：「記住,定了,就不要再改」（HeQiNekCZng）——permission 層面佢容許 1%、2% 甚至 3%（fLN20X1dP48），preference 層面佢本人揀極低風險＋穩定：「那種短期的暴利其實對我來說真的沒有意義」（ryv0CUgVZCM）。
- Prop firm 場景嘅特定上限（考試 1%、撥資 ≤1%）→ `lun-prop-firm-playbook`；本 skill 只述 baseline。

**Step 4 — 倉位計算公式（hkCvRoLc3Nk）**

- (transcript)「那個Formula,就是你的資金再乘以0.01,0.01就是你的風險,那如果你的風險是2%的話,那就0.02」→ 得出可虧金額；(transcript)「你就要用你可以虧損的金額,再除以你的止损點」（止损點＝止損點數）→ 得出 Lot Size。
- 行為警告：由公式可見收窄止損可以開大倉——「這樣一來,你可以交易的Lot Size,就會更大」——呢個正係貪婪收窄止損嘅誘因（hkCvRoLc3Nk；止損寬窄悖論本體 → `lun-exit-management`）。

**Step 5 — 等額風險鐵律＋唯一例外**

- 鐵律：(transcript)「每一筆風險的大小要一樣」；信心爆棚加倉、驚錯過縮倉、報復性重倉都會令 (transcript)「只仓位的大小不一樣,整個概率模型就毀掉了」（54WCm_VBYfY；「只」疑為「只要」）。旁證：「你的單比風險都是一致的」（teVdcguZs_U）、「我都會固定我的倉位大小」（HeQiNekCZng）。
- 有信心都唔加：「就算你再有信心,不要加大風險,跟著你計劃去做」（54WCm_VBYfY）。
- **唯一例外**：(transcript)「如果你面對比較大的回撤的時候,你可以降低,主動去降低風險」，回返原本資金水平先用返原本風險（54WCm_VBYfY）——只准向下調，永遠唔准向上調。

**Step 6 — 連虧／回撤應對**

- 連虧降倉：(transcript)「連續虧損過後,我一定要強行拉低我的倉位」，此時 (transcript)「我的風險是0.5%到0.25%罷了」（HeQiNekCZng）；機制解讀：「當你在連續虧損的情況,就代表這個市場已經沒有那麼好做了。」降風險慢慢 cover，市場轉好先恢復（rLP-MPvGmDE）。（考試場景嘅**連虧 5 單砍半**規則 → `lun-prop-firm-playbook`。）
- 停手規則：同形態連虧兩單停手（QZNzq-BunA4，筆記歸納，單源）；自有資金虧 30% 停手——(transcript)「通常我會定給自己最多30%」，1 萬虧剩 7000 就出金、休息、回顧再重來（rE21_onS0uo，單源）。
- 大盈虧比作連虧保險嘅數學：(transcript)「我要連虧22單,我才會回到原點」(transcript)「要連虧22單,幾乎不可能」（WmW5fQjK5Qg）；(transcript)「我只需要有一單盈利。」(transcript)「基本上就可以把我所有的Losses cover掉」（hkCvRoLc3Nk）；實盤「我最大回撤,是6單連續虧損」「我只需要一單,我就可以把全部虧損都追回來」（MjPZizFnX-E，自述）。連虧現實提醒：「虽然它的胜率高」「不代表它不会连续亏损」（6_5DVT6uS9E）。（RR 門檻幾多先夠 → `lun-exit-management`。）

**Step 7 — 風險暴露與頻率**

- 最大風險暴露要預先自定：「最多的風險暴露是多少?」唔好同時全開 5 單各 2%（rE21_onS0uo）；「最多你的Risk Exposure到底有多少%?」（rLP-MPvGmDE）。
- 日內止損 30 點上限（單源）：(transcript)「我們盡量把我們的止損維持在30點以內。」「任何超過30點的話。在日內交易都是非常沒有勝算」（QZNzq-BunA4；放置方法 → `lun-exit-management`）。
- 頻率即風控（口徑演化，profile §7.3.6）：早期「每一个星期不一定要做很多比交易的」「3到5比」（hmpAys3lJEo，2025-09，每週）→ 後期「專注一個月做3-5筆高質量的交易」（k0ESC6XYz50，2025-10，每月）。以後期口徑為主，註明演化；佢實盤都話「我的交易量會越變越少」（MjPZizFnX-E）。
- 垃圾交易警示：「基本上沒有催化劑的交易,都是垃圾交易」、月 3 筆高質量「勝過一百筆的垃圾交易」（k0ESC6XYz50；四大過濾標準本體 → `lun-multi-timeframe-analysis`）。

**Step 8 — 常見錯誤目錄（跨片彙整，逐項附 id 同去向）**

| id | 錯誤 | 出處 | 風控歸屬／路由 |
|---|---|---|---|
| E01–E02 | 太晚入場；抄底摸頂做英雄 | s4on4yJCLII | 入場紀律 → `lun-price-action-toolkit` |
| E03 | 唔設止損——「沒有設置支撐點就代表你的風險是無限大的」（支撐點＝止損點） | s4on4yJCLII | 本 skill（必設止損）；放邊 → `lun-exit-management` |
| E04 | 壓太多資金——本金超過虧得起嘅 10–30% | s4on4yJCLII | 本 skill Step 2 |
| E05–E06 | 指標過多；頻繁換策略 | s4on4yJCLII | → `lun-backtesting-method`（一套系統練到底） |
| E07 | All-in——「All-in这个行为是非常危险的」 | s4on4yJCLII | 本 skill；報復心理成因 → lun-trading-psychology（生成中） |
| E08 | 唔做模擬直上實盤 | s4on4yJCLII | → `lun-backtesting-method` |
| E09 | 盈虧比錯（未夠 1:2 就想出場） | s4on4yJCLII | → `lun-exit-management` |
| E10 | 放棄太早 | s4on4yJCLII | → lun-trading-psychology（生成中） |
| F01–F03 | 三大致命失誤：冇主見（靠跟單）／過度盯盤／執行力差 | T2Nk46EqAh4（單源） | 全部 → lun-trading-psychology（生成中）；本 skill 只留**過度盯盤→過度交易**呢層風險後果 |
| M01–M06 | 六迷思：賺錢捷徑／隨處可交易／當遊戲／時間＝回報／全靠技術／天天賺錢 | H3OZxavXlsk（單源） | M04（時間≠回報→過度交易）、M05（技術+風控+情緒三角）留本 skill；其餘 → lun-trading-psychology（生成中） |
| K01 | 垃圾交易／過度交易（週 20–30 筆） | k0ESC6XYz50 | 本 skill Step 7；過濾標準 → `lun-multi-timeframe-analysis` |

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案、唔畀具體投資建議。一份完整回覆應包含（每部分附 video id）：

1. **路由聲明**：邊部分屬本 skill、邊部分已轉交邊個 sibling。
2. **防守定調**：相關哲學原則（命脈／活下去／雙重保護）。
3. **數字規則**：風險 % 必以雙口徑平行呈現（教學 1–2% vs 自用 <0.25% vs 漸進 0.25%→1%）；倉位公式運算示範；連虧降倉／停手線／暴露上限；每個數字附出處。
4. **permission vs preference**：邊啲係佢容許嘅範圍（1–3% 都 OK）、邊啲係佢本人嘅取態（極低風險＋低頻），分開講。
5. **錯誤對照**：如用戶行為觸及 E/F/M/K 目錄，指出對應條目同引文。
6. **警告聲明**：單源規則標（單源）；自述績效標（自述，未對帳）；推論標（推測）；教科書風控概念一律拒絕補完並說明原因。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 止損三法／止盈三套／平價保護／分批／80% 提前出場 | `lun-exit-management` |
| RR 門檻分層（1:1／1:2／1:3）、RR↔勝率取捨規則本體 | `lun-exit-management` |
| 考試 1%／撥資 ≤1% 上限、連虧 5 單砍半、唔過夜、增長藍圖等 prop firm 場景應用（0.25%→1% 漸進 baseline 本體**留喺本 skill** Step 3 口徑 #3） | `lun-prop-firm-playbook` |
| A+ 四大標準過濾（做唔做呢筆） | `lun-multi-timeframe-analysis` |
| 樣本量、預期連敗數據、系統驗證 | `lun-backtesting-method` |
| 時段紀律（晚上 10 點後不開新單、亞洲盤前平倉） | `lun-kill-zones-timing` |
| FOMO／報復交易／mental capital／過度盯盤心理機制、10 習慣全表 | lun-trading-psychology（生成中） |

## 侷限聲明

1. **多口徑未調和**：教學 1–2% vs 自用 <0.25% 嘅差距 corpus 冇解釋，本 skill 嘅調和屬（推測）；而自用 <0.25%（2025-10）同最近實盤覆盤固定 1%（MjPZizFnX-E，2026-04）同屬自述、相隔約 6 個月、相差 4 倍，corpus 同樣冇解釋——引用時所有口徑必須並列，唔裁決（profile §7.3.9；Step 3 Tier 1a/1b）。
2. **單源規則**：止損 30 點上限＋同形態連虧兩單停手（QZNzq-BunA4）、本金 10–30%（s4on4yJCLII）、30% 停手線＋最大暴露（rE21_onS0uo）、「不熟,不做」（0a4NrcfAPJU）、連虧 22 單數學（WmW5fQjK5Qg）、3 失誤（T2Nk46EqAh4）、6 迷思（H3OZxavXlsk）各為單源，使用時聲明。
3. **頻率口徑演化**：週 3–5 筆 vs 月 3–5 筆屬時期差異，以後期為主但必須註明（profile §7.3.6）。
4. **自述績效未對帳**：連虧 22 單數學、6 連虧最大回撤、80 萬美金虧損教訓、Q1 實績均為自述；引 MjPZizFnX-E 數字必附分母 caveat——「勝率只有在40%」存在 19/47≈40.4% vs 19/(19+20)≈48.7% 兩種算法、8 筆保本單去向未說明（profile §7.3.3）。
5. **教科書禁區**：Kelly、VaR、fixed-fractional、ATR sizing、組合相關性模型——corpus 冇教，唔准補完；等額風險嘅「概率模型」論述係佢嘅大數法則口徑，唔好擅自升級成統計學証明。
6. **未觸及**：對沖、多帳戶資金分配、稅務、槓桿倍數選擇——corpus 冇教。
7. **同 profile §6.10 嘅刻意偏離**：profile §6.10 名義上將最低盈虧比門檻（1:1/1:2/1:3 按情境）同 prop firm ≤1% 劃入本 skill scope，但 `analysis/skill_boundary_ledger.md` 第 7、9 條已分別將佢哋判畀 `lun-exit-management` 同 `lun-prop-firm-playbook`（兩者先通過審查）——本 skill 跟 ledger 行，ledger 係 DRY 最終依據；後續作者對照 profile 時唔好將呢兩項還原返嚟。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 風險管理證據全錄：防守哲學、雙口徑風險%、倉位公式、等額鐵律、連虧與回撤規則、大盈虧比數學、暴露與頻率、本金配置、錯誤目錄、矛盾與警告（verbatim＋video id）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（盈盔比＝盈虧比、比＝筆、賭信＝賭性、評價保護＝平價保護等）；雙口徑依據 §7.3.9；頻率演化依據 §7.3.6；勝率分母警告依據 §7.3.3。
- **Contributing videos（31，per profile §6.10）**：核心——hkCvRoLc3Nk（倉位公式＋1–2%）、ryv0CUgVZCM（<0.25% 自用）、HeQiNekCZng（1–2% 鐵律＋連虧降倉）、54WCm_VBYfY（等額風險＋唯一例外）、rE21_onS0uo（0.25% 漸進＋暴露＋30% 停手）、rLP-MPvGmDE（命脈觀＋連虧降風險）、WmW5fQjK5Qg（連虧 22 單數學）、QZNzq-BunA4（30 點上限）、k0ESC6XYz50（頻率即風控）、s4on4yJCLII（10 錯誤）、T2Nk46EqAh4（3 失誤）、H3OZxavXlsk（6 迷思）、eIeYQStY5rI（活下去）、jlO3771JF1E（防守觀）、0a4NrcfAPJU（不熟不做）、48pCaOfGGmA（守本金）、MjPZizFnX-E（1R 實盤）、OANImZtkkeM（2% 以內）、fLN20X1dP48（1–3%＋prop 銜接）、teVdcguZs_U（等額旁證）、6_5DVT6uS9E（連虧現實）、hmpAys3lJEo（週 3–5）；其餘（GINdJCIIEvw、xmHaONnNrCw、mDpbsw81ftI、91Hpt_LyJSE、xwsyfVf2l0k、zgVlK7UBNTY、fTRv2HhTJUk、qWMKL-p1MPE、7j7_mhfda38）主要貢獻已由 sibling skills 持有，本 skill 只作銜接引用。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim；標「(transcript)」者為直接覆核；本 skill 已覆核 ryv0CUgVZCM <0.25% 句、HeQiNekCZng 1–2%/唔好改/0.5%–0.25%/PTJ 句、fLN20X1dP48 1%–3% 句、hkCvRoLc3Nk 公式兩句＋一單 cover 句、WmW5fQjK5Qg 連虧 22 單兩句、54WCm_VBYfY 等額/概率模型/大回撤例外句、rE21_onS0uo 0.25% 起步/30% 停手句、QZNzq-BunA4 30 點句、MjPZizFnX-E 1R＝1% 句、rLP-MPvGmDE 命脈句、eIeYQStY5rI 活下去句）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `skills/` 嘅上一層目錄）；skill-relative 寫法即 `../../analysis/lun_trading_profile.md`、`../../data/transcripts/<video_id>.txt`；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
