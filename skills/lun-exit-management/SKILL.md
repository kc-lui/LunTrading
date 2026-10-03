---
name: lun-exit-management
description: 按照交易倫（Alan / LunTrading）的出場管理體系管理已入場嘅倉位——三種止損擺法（遠離 Swing Structure／兩個 Technical Barrier 以外／離開入場 K 線）、呼吸空間 vs 盈虧比取捨、兩種止盈法（固定盈虧比／HTF 主力區）、標準差投射（Standard Deviation Projection，掃描腳拉 -1/-2/-2.5/-4 揀共識級）、三層交易管理（消除風險→利潤最大化→鎖住利潤）、平價保護鐵律、80% 提前出場、EMA50 移動止損、-2 出一半分批、持倉時間規則。Use when deciding 止盈 take profit targets, 止損 stop loss placement, 出場 exit timing, 移動止損 trailing stop, 平價保護 breakeven protection, 分批 partial exit, 鎖利 locking profits the way 交易倫 teaches. 唔覆蓋倉位大小/風險%（risk-management）、入場序列（ote-entry-model）、PD Array 定義（ict-pd-arrays）。
---

# lun-exit-management：出場管理——止損擺位、止盈投射與三層持倉管理（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅「出場執行」層——由入場單成立嗰一刻開始，到平倉為止嘅全部決策：止損擺喺邊、止盈點點定、幾時保本、幾時鎖利、幾時提早走。主教材係 hkCvRoLc3Nk（止損止盈完整攻略）同 Q371XdV3apE（ICT#9 日內止盈：標準差投射），另有 ≥8 片支撐素材（per profile §6.7）。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5——**止盈/止損係全 corpus ASR 誤認最多嘅兩個詞**）。三層管理總綱：「第一個任務就是要消除風險。」「第二個就是我們要利潤最大化。」「第三呢,我們就要鎖住利潤。」（GINdJCIIEvw）。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 為一筆已規劃/已成立嘅入場單擺止損：三檔擺法（保守→激進）、緩衝與整數關口、止損太大點處理
- 定止盈目標：固定盈虧比 vs HTF 主力區 vs 標準差投射（-1/-2/-2.5/-4 揀共識級）三套方法對照
- 入場後管理：幾時消除風險（平價保護）、幾時開始鎖利、用乜做移動止損參照（EMA50/結構/樞軸）
- 判斷提早出場：80% 到止盈規則（兩口徑）、candle close 反轉、徘徊太久、接近止盈未觸及
- 分批決策：-1 保本、-2 出一半、剩低追 -4；平價保護後再入場
- 處理持倉時間：>1:6 可持過一週、兩日未到止盈平保出場
- 解釋 RR↔勝率 tradeoff（1:10+ 要接受勝率 <30%）同「唔好鎖太多利潤」嘅回報最大化節奏

**唔應該用嘅情況**：

- 倉位大小、每筆風險 %、連虧降倉、風險暴露上限 → 用 `lun-risk-management`（本 skill 只管「單入咗場之後點行」，唔管「落幾大」）
- 入場序列（掃描→確認→回調→落單）、止損止盈**初設**嘅 127.2/161.8 延伸框 → 用 `lun-ote-entry-model`（該 skill 設初值，本 skill 接手管理）
- OB/FVG/破壞塊/高低位定義與品質（止盈共識疊嘅「障礙物」係乜）→ 用 `lun-ict-pd-arrays`
- 流動性池喺邊、掃蕩機制（標準差投射嘅「基準腳」點認、反向掃描點判定）→ 用 `lun-liquidity-analysis`
- 大時框搵止盈嘅時框分工本身（動能回流骨架「大時框止盈＋小時框入場」）→ 用 `lun-multi-timeframe-analysis`（該 skill 持有分工，本 skill 持有止盈點嘅具體定法）
- 硬性時段出場時間表（唔過夜、收市前/11–12 點出場、時段停手）→ 用 `lun-kill-zones-timing`；prop firm 考試場景嘅帳戶保護 → `lun-prop-firm-playbook`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答。教科書式出場方法（ATR 止損、Chandelier、R-multiple ladder 等）corpus 冇教過，一律唔准引入。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯（本 skill 特別重要）**：止盈＝直銀/紙銀/指引點/直营点/零点…；止損＝止损點/直送點/止筍/子孫/十頓點/支撐點/直瞬點…（20+ 變體）；盈虧比＝盈盔比/盈窥比/盈盈比/incred比…；**平價保護＝評價保護/平保**（保本/breakeven）。全表見 `analysis/lun_trading_profile.md` §5。同一句內「止损点」可能實指止盈點（見 Step 2 嘅 RdnJw-mhwlE 備註）。
3. **前置路由**：本 skill 假設入場已由 `lun-ote-entry-model`（或其他策略 skill）完成、倉位已由 `lun-risk-management` 計好。佢嘅思路係**入場前已預判出場**——「所以呢,已經知道在哪裡出場。」（qWMKL-p1MPE）；動能回流「第一步通常是要找價格可能會去到哪裡?」（zgVlK7UBNTY）——即止盈規劃先於入場，唔係入咗場先諗。
4. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 三層管理 | 消除風險→利潤最大化→鎖住利潤 | GINdJCIIEvw |
| 平價保護 | 止損推到入場價保本（ASR 常作「評價保護」）；「就是没有亏钱也没有赚钱」 | hmpAys3lJEo |
| 標準差投射 | (transcript)「叫做 Standard Deviation Projection，就是標準差投射」——掃描腳拉 Fib 負延伸定止盈 | Q371XdV3apE |
| Technical Barrier | 止損要放喺「最少兩個Technical Barrier以外」嘅參照物（趨勢線/抵抗位等） | hkCvRoLc3Nk |
| 呼吸空間 | 止損要「讓價格有足夠的呼吸空間去波動一段時間才出現Commitment」 | hkCvRoLc3Nk |
| 80% 規則 | (transcript)「80%到我的止盈點了,我就會提早出場」（另有條件版口徑，兩口徑見 Step 6） | hkCvRoLc3Nk |

## Workflow（分析流程）

按三層管理嘅時間軸行：擺位（入場時）→ 消除風險 → 利潤最大化 → 鎖住利潤 → 出場。

**Step 1 — 止損擺位（三法，由保守到激進，全部 permission）**

1. **遠離 Swing Structure**：「就是遠離前高位,或者是遠離前低位。這是最保守的。」（hkCvRoLc3Nk）——止損最大。
2. **最少兩個 Technical Barrier 以外**（佢個人偏好）：「我會把我的止损點設置在最少兩個Technical Barrier以外」「因為,價格必須突破兩個不一樣的Barrier,才會到達我的止损點」（hkCvRoLc3Nk）。
3. **直接離開入場 K 線**：「這是最激進的方法」，要「跟著K線的形態來做判斷」（hkCvRoLc3Nk）。

輔助規則：離開結構/POI——「只順便離開，離開遠一點」（Q371XdV3apE；只順便＝止損點）、「盡量離開所有的這些位置。就是所有這些關鍵的一些POI」（T2Nk46EqAh4）、離開 order block／EMA50（GINdJCIIEvw, B7rumsOw6_U, zgVlK7UBNTY）；**避開整數關口**——「通常,我都會盡量離開0.66這種整數」（hmpAys3lJEo）；止損太大就棄做該筆——「只顺点对我来说太大了」「所以我就」「没有去进场」（hmpAys3lJEo）。

**寬窄取捨（字面矛盾，實為兩層——profile §7.3.8）**：太窄唔得——(transcript)「用太窄的止损點,就代表你的Timing要非常的準確」，要呼吸空間（hkCvRoLc3Nk；xwsyfVf2l0k 同）；太大又「會影響到你的盈窥比了」（hkCvRoLc3Nk）。同時「用5分鐘去做入場的話呢,我們的止损可以非常的窄」（B7rumsOw6_U）——**解法係入場時框內留空間、靠降時框縮絕對距離**，唔係喺同一時框收窄。

**Step 2 — 止盈設定（三套方法；「三套」屬本 skill 編輯歸納：hkCvRoLc3Nk 教頭兩套成對，第三套出自另一單源影片，平行照錄）**

| 方法 | 規則 | 出處／適用 |
|---|---|---|
| 固定盈虧比 | 「第一種止盈的方法,就是固定盈亏比」「一對二,或是一對三的盈亏比就夠了」；適合初學者 | hkCvRoLc3Nk |
| HTF 主力區 | 「我會直接在高時框,比如說日線圖,或者4小時圖,來找一個主力支撐區域」；首選支撐阻力轉換位（hmpAys3lJEo） | hkCvRoLc3Nk |
| 標準差投射 | 見下段 | Q371XdV3apE（單源） |

**標準差投射（Standard Deviation Projection）**：基準腳**一定要係掃描/假突破嗰隻腳**——(transcript)「它一定要是，掃描的那一個角，就是掃描掉，突然間衝破的這一個」「或者是做假突破的那一個角，從它的高度到前低度」（角＝腳）；用 Fib 負延伸 (transcript)「我們用-1-2-2-2.5-4」（推測＝-1/-2/-2.5/-4）；**揀級唔係隨便揀**——(transcript)「不是隨便去選一個號碼」「選你喜歡的號碼」（否定句），而係揀最多共識/最多障礙物嗰級——「它就變成了很強的阻力,所以價格要繼續下跌的話,它就會遇到障礙物」；冇障礙物先拉遠——「是完全空空，沒有任何障礙物，我們就可以拉得更遠」；入場門檻——(transcript)「最少要有1比1的盈亏比，這樣子，這筆交易就可以做」（由入場到 -1 計）。障礙物（OB/FVG/破壞塊/高低位/樞軸線/收盤價）嘅定義 → `lun-ict-pd-arrays`；基準腳嘅掃描判定 → `lun-liquidity-analysis`。

相鄰口徑：下一個結構就好（「直銀呢,到下一個結構就好」B7rumsOw6_U，直銀＝止盈）、下一個 Pivot／主力區（7j7_mhfda38：「指引點呢,在下一個pivot。」）。**RdnJw-mhwlE 備註（存疑，唔好斷言）**：該片 (transcript)「止损点呢在下一个Pivot或者是下一个主力区那就ok了一对二就做到了」——筆記備註指由「一对二就做到了」上下文同 hkCvRoLc3Nk 嘅 HTF 主力區止盈講法推測，呢句應指**止盈目標**，「止损点」疑係 ASR 誤認或口誤；引用時必須帶住呢個 ambiguity，唔可以靜靜當止損或止盈規則用。

**Step 3 — 管理第一層：消除風險（平價保護）**

- **鐵律（觸發式）**：「你入場了,然後價格出現了流動性掃描,你一定要做評價保護。這是一個很重要的規則。」（xwsyfVf2l0k，transcript 覆核；評價保護＝平價保護）——反向流動性掃描出現即保本。
- 強動能離開即拉：「基本上只要價格離開了之後,尤其是搶動了離開了之後,我會盡快把我的止损點,拉去我的入場位置。」（GINdJCIIEvw；搶動＝強動能）
- 里程碑式：到標準差 -1 即保本——(transcript)「因為價格到了這一邊，我們就評價保護」（Q371XdV3apE）；或到止盈一半位——「就是在價格的一半的位置。就碰到這裡之後,我就開始break even的平價保護」（T2Nk46EqAh4，可設警報器）；突破阻力後——「其實我們就可以去做評價保護了」之後「你就沒有風險了」「你就讓他去跑」（zgVlK7UBNTY）。
- 保本都算好結果：「至少没有亏钱」（hmpAys3lJEo）；佢實盤大量「評價保護的階段」單（MjPZizFnX-E）。

**Step 4 — 管理第二層：利潤最大化（唔好鎖太多）**

- 節奏原則：「就是你盡可能的不要鎖住太多利潤,因為我們要回報最大化」（zgVlK7UBNTY，transcript 覆核）；風險消除後「我們就繼續持場」。
- 鎖利要有代價意識：「因為我們要鎖住利潤。所以鎖住利潤的話,我們沒有辦法,我們需要有一個犧牲。」（GINdJCIIEvw）——鎖得越貼，越易被震走。
- 實例節奏：1:22 持倉中鎖 1:16——「拉到這一邊,就是鎖定了1比16的盈虧比」「鎖定這麼多的利潤,然後給市場多一點空間去給我更大的利潤」（WmW5fQjK5Qg）。
- 鬆緊係個人選擇（permission）：「有時候你可以管理的更輕鬆一些,有時候你可以管理的更激進一些。看你想要什麼?你想要的是鎖住利潤呢?還是你想要的是回報最大化?」（GINdJCIIEvw）

**Step 5 — 管理第三層：鎖住利潤（移動止損）**

- **EMA50 追蹤法**：「隨著價格動能釋放離開了,推開了EMA50,我都會把我的止损點放在EMA50後面。慢慢的鎖住利潤。只要EMA51移開,我就繼續放在它後面。直到我被打掉為止。」（GINdJCIIEvw，transcript 覆核首句；EMA51移開＝EMA50一移開）；低時框版「你可以5分鐘EMA50後面做管理」（B7rumsOw6_U）。
- 結構/樞軸逐級鎖：到位「我們就一定要鎖住利潤」「你要鎖住一個R也可以」，破位後「那我們就要積極地鎖得更高一些」（B7rumsOw6_U）；突破高位先鎖——「只要價格繼續衝破高位,」「我們再去鎖定利潤就好。」（zgVlK7UBNTY）。

**Step 6 — 提前出場規則（觸發式，任一命中即考慮手動出）**

| 觸發 | 規則原話 | 出處 |
|---|---|---|
| 80% 到止盈（無條件版） | (transcript)「當我看到我的單子已經差不多要80%到我的止盈點了,我就會提早出場」 | hkCvRoLc3Nk |
| 80% ＋反轉形態（條件版） | (transcript)「當價格到了我的止盈點80%位置的時候,出現了反轉形態。這個時候我會選擇手動出場」 | T2Nk46EqAh4 |
| Candle close 反轉 | 急速反轉「等到candle close了,我們可以直接出場」，唔使等返轉方向，「直接找下一個交易機會,更有效」 | hkCvRoLc3Nk |
| 好近止盈但唔掂 | 「通常這種時候我會直接手動出場」（xwsyfVf2l0k）；「那通常這種時候,我就會選擇提早出場」「我不會吃太久。」（qWMKL-p1MPE） | xwsyfVf2l0k, qWMKL-p1MPE |
| 徘徊太久 | 「如果价格徘徊太久」「我可能会出场」（「通常半夜都会徘徊」） | RdnJw-mhwlE |
| 數據動能耗盡 | 「大数据带来的动能很快就会被消耗完了」所以「不要持太久」「千万不要贪心」 | kI5idYixD50（數據交易場景） |

兩個 80% 口徑（無條件 vs 要反轉形態）屬唔同時期版本，平行照錄唔裁決。背後係期望值思維：「我們在用著這一部分的回報,來parget我們想要的預期的這一小部分的回報,值得嗎?」（hkCvRoLc3Nk；parget＝target）、「去追求還沒有確認的200美金」（T2Nk46EqAh4，否定用 800 博 200）——同埋防「把我們的利潤還回給市場而變得很情緒化」（hkCvRoLc3Nk）。

**Step 7 — 分批、再入場與持倉時間**

- **分批（標準差投射版，單源）**：(transcript)「然後你甚至可以選擇到了減2，你出一半，剩下就讓它，看能不能去到減4」（Q371XdV3apE）——-1 保本、-2 出一半、餘倉追 -4。
- **平價保護後再入場**：「評價保護了之後,我再找第二個入場機會這一邊,再入場多一次,這樣子。」（GINdJCIIEvw 德指例）——再入場嘅序列執行 → `lun-ote-entry-model` Step 7。
- **持倉時間規則**：大 RR 可持過週末——「因為超過1比6的盈虧比」「我們可以持過一周」（zgVlK7UBNTY，transcript 覆核）；兩日未到止盈平保出場——「我们就有平保出场」「什么都没赚」（RdnJw-mhwlE）；日內短線系統絕不過夜——「我們不要hold overnight」（7j7_mhfda38，時間表細節 → `lun-kill-zones-timing`／`lun-prop-firm-playbook`）。

## RR↔勝率取捨與門檻（矛盾分層，per profile §7.3.2）

- **Tradeoff 定律**：(transcript)「當你的盈盔比變大,你要知道你的勝率就會變少」「當你喜歡超過一對十的盈盔比,你就要可以接受勝率低過30%」（hkCvRoLc3Nk；盈盔比＝盈虧比）——同時要「接受連續虧損的情況出現,還有連續Break Even的單子出現」。補償數學：「我只需要有一單盈利。基本上就可以把我所有的Losses cover掉」（hkCvRoLc3Nk）。
- **最低 RR 門檻係情境分層，唔係單一數字**：1:1（標準差投射到 -1 嘅入場門檻 Q371XdV3apE；harmonic 6_5DVT6uS9E）｜1:2（54WCm_VBYfY、RdnJw-mhwlE 示範口徑；7j7_mhfda38 不足 1:2 可掛低啲/拉高止盈湊）｜1:3（FTMO 考試場景 xmHaONnNrCw；xwsyfVf2l0k 基本設定）。回答時必須先問情境，唔准報單一數字。門檻背後嘅倉位/連虧數學 → `lun-risk-management`。
- **降低犧牲嘅方法**：「其實你可以做多一步,就是確保你盈亏比大的同時,勝率也不會低到哪裡去的。」——盡快移除風險＋只抓高質量機會（GINdJCIIEvw；質量篩選 → `lun-multi-timeframe-analysis`）。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅出場管理判斷。一份完整嘅出場管理回覆應包含以下六部分，每部分引用對應規則（附 video id）：

1. **前置宣告**：入場依據（邊個 sibling）、倉位已定（→`lun-risk-management`）、入場前止盈預判係乜。
2. **止損方案**：三法揀邊檔＋理由、參照物（結構/Barrier/K 線/POI）、整數關口檢查、寬窄層次（時框）；止損太大→建議棄做。
3. **止盈方案**：三套方法揀邊套；用標準差投射就列基準腳、四級障礙物盤點、揀級理由、-1 是否 ≥1:1。
4. **管理計劃**：平價保護觸發清單（反向掃描/強動能離開/-1/一半位）、鎖利參照（EMA50/結構）、鬆緊取態（鎖利 vs 回報最大化，講明係用戶選擇）。
5. **提前出場監察**：80% 位、candle close 反轉、徘徊時限、持倉時間規則邊條適用。
6. **行動銜接**：再入場→`lun-ote-entry-model`；下一筆倉位→`lun-risk-management`；情緒（唔忿出場/見錢興奮）→`lun-trading-psychology`。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 倉位公式、每筆風險 %、連虧降倉、頻率風控 | `lun-risk-management` |
| 入場序列、SL/TP 初設（127.2/161.8 框）、失敗再入場執行 | `lun-ote-entry-model` |
| OB/FVG/破壞塊/高低位/樞軸（止盈「障礙物」）定義與品質 | `lun-ict-pd-arrays` |
| 流動性池位置、掃蕩/假突破判定（投射基準腳、反向掃描） | `lun-liquidity-analysis` |
| 大時框止盈＋小時框入場嘅時框分工（動能回流骨架） | `lun-multi-timeframe-analysis` |
| 時段出場時間表、唔過夜/收市前出場、數據日曆 timing | `lun-kill-zones-timing` |
| 考試帳戶保護場景 | `lun-prop-firm-playbook` |
| 見錢興奮/唔捨得出場嘅情緒管理 | `lun-trading-psychology` |

## 侷限聲明

1. **標準差投射係單源**：完整方法只有 Q371XdV3apE 一片（-1/-2/-2.5/-4 級別數字亦係由 (transcript)「-1-2-2-2.5-4」推測還原）；分批「-2 出一半」同屬單例。使用時降權，建議按 `lun-backtesting-method` 驗證。
2. **RdnJw-mhwlE「止损点呢在下一个Pivot」存疑**：按上下文推測應指止盈目標，但無法排除口誤/ASR 以外嘅可能——引用必須照錄並帶備註，唔准淨引半句當規則。
3. **多口徑平行**：80% 規則兩版本（無條件/要反轉形態）、最低 RR 三檔（1:1/1:2/1:3 按情境）、鎖利鬆緊（permission 唔係規則）——一律照錄唔裁決。
4. **推測標註**：「評價保護＝平價保護」「只順便/十頓點/子孫＝止損點」「直銀/指引點＝止盈點」等正字全屬 ASR 推測修正；kI5idYixD50 出場規則碎片化嚴重（「止顺点拉开、指令点一样在上面」原文如此）。
5. **實績未經對帳**：1:16（GINdJCIIEvw 銀例）、1:22.45（WmW5fQjK5Qg）、1:5（hmpAys3lJEo）、Q1 79.69R（MjPZizFnX-E）均為覆盤示範或自述；佢本人警告「我公開的交易表現呢,不代表你們也能做到一樣的交易表現」（MjPZizFnX-E）。
6. **勝率口徑不明**：MjPZizFnX-E 嘅 40% 勝率有兩種分母算法（19/47 vs 19/39，profile §7.3.3），引用實績時要附口徑警告。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 出場管理證據全錄：止損三法、呼吸空間取捨、止盈三套方法、標準差投射全段、三層管理、平價保護鐵律、移動止損、提前出場、分批持倉、RR↔勝率（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（止盈/止損/盈虧比/平價保護誤認變體，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3；經驗值與實績警告依據 §7.4。
- **Contributing videos（核心 2＋支撐 8，per profile §6.7）**：hkCvRoLc3Nk（止損止盈完整攻略）、Q371XdV3apE（標準差投射）；GINdJCIIEvw（三層管理＋EMA50 追蹤）、T2Nk46EqAh4（80% 條件版＋半途保本）、B7rumsOw6_U（結構鎖利＋5分鐘 EMA50）、xwsyfVf2l0k（平價保護鐵律）、zgVlK7UBNTY（鎖利節奏＋持過一週）、RdnJw-mhwlE（徘徊/兩日平保出場；Pivot 句存疑）、7j7_mhfda38（下一個 Pivot 止盈＋唔過夜）、qWMKL-p1MPE／hmpAys3lJEo／WmW5fQjK5Qg／kI5idYixD50／MjPZizFnX-E（提早出場/整數關口/鎖 1:16/數據動能/實盤佐證）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim；本 skill 已覆核 hkCvRoLc3Nk 三法/80%/勝率30%段落、Q371XdV3apE 基準腳/級別/揀級/1:1/-1保本/出一半段落、xwsyfVf2l0k 鐵律句、GINdJCIIEvw 三層句、zgVlK7UBNTY 鎖利節奏句、RdnJw-mhwlE Pivot 句、T2Nk46EqAh4 80% 句）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `skills/` 嘅上一層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
