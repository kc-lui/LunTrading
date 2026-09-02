---
name: lun-ote-entry-model
description: 按照交易倫（Alan / LunTrading）的 OTE（Optimal Trade Entry / 最佳入場點）入場模型做完整入場執行——四招順序（流動性掃描→強動能釋放/結構破壞確認→唔做第一浪、等回調 50%–79% 抓第三浪→Fib×OB/FVG 共識疊加）、Fibonacci 回調口徑對照（50–79%／61.8 以上／50–61.8／50% 以下便宜區／38.2–78.6 揀共識）、掛單 vs 觸發確認雙選項、止損止盈初設（127.2/161.8 延伸）、首次失敗後再入場規則。Use when executing a pullback entry（回調入場/Fib 回調）, applying the OTE entry model（入場模型）, deciding 「喺邊入場」「掛單定等確認」「回調到幾多先入」 the way 交易倫 teaches. 唔覆蓋流動性掃描機制、PD Array 定義、多時框偏向判斷、出場管理（見 sibling skills）。
---

# lun-ote-entry-model：OTE 入場模型——完整入場執行（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅「入場執行」層——由 setup（流動性掃描）到 trigger（強動能確認＋回調到位）到 order placement（掛單/觸發、止損止盈初設）嘅**順序化流程**。主教材係 3Kt_ruGepB4（ICT#8 OTE 完整教學）同 7dDW8tF1cZo（ICT#5 完整入場模型），另有 7 片同源素材（per profile §6.5）。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。**佢嘅 OTE 回調區口徑係「(transcript)『我們需要價格回調到第一浪的50%以上到50-79%以上』」（3Kt_ruGepB4）——唔係教科書 ICT 嘅 62%–79% Fib 帶，嚴禁用教科書口徑覆蓋**。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。佢嘅一句總定調：「OTE入場模型。就是強動能破壞。結構破壞。回調」（hmpAys3lJEo）。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 由頭到尾行一次 OTE 四招入場流程（掃描→確認→定浪拉 Fib→共識入場）
- 決定回調要去到邊先算「到位」：對照 corpus 內幾套 Fib 回調口徑（唔合併）
- 解釋點解唔喺前高前低直接入場（「這根本就是垃圾交易來的」）、點解唔做第一浪
- 揀落單方式：提前掛單 vs 等價格碰到/反轉先入（雙選項＋佢嘅示範偏好）
- 設初始止損（離開 FVG/OB/整個結構＋5–10 點緩衝）同初始止盈框（127.2/161.8 延伸、對面流動性位）
- 處理第一筆入場失敗之後嘅保守再入場
- 追溯佢入場模型嘅演化族譜（Base Zone→ICI Fib→動能 Fib→完整入場模型→OTE 四招→Fib ABC）

**唔應該用嘅情況**：

- 流動性池喺邊、掃描/獵殺機制、真假突破「站得住」測試 → 用 `lun-liquidity-analysis`（本 skill 只當 Step 1 係前置訊號）
- OB/FVG/IFVG/破壞塊定義、品質檢查、觸碰衰減、**PD-Array 區內三層入場確認口徑** → 用 `lun-ict-pd-arrays`（DRY：本 skill 持有順序，區內確認分層由該 skill 持有）
- 強動能 K 線力度判讀、吞噬/釘形/圖形本身、破位 vs 破位回調 → 用 `lun-price-action-toolkit`
- 日線/週線偏向、幾多個時框要同向（OTE 嘅「獨家秘訣」多時框同向歸邊）→ 用 `lun-multi-timeframe-analysis`
- 幾時交易（時段/週節奏/數據日曆）→ 用 `lun-kill-zones-timing`；入場後嘅移動止損/平價保護/鎖利節奏 → 用 `lun-exit-management`；倉位/單筆風險 → 用 `lun-risk-management`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答。**最重要嘅 fence：教科書 ICT 嘅 OTE＝62%（0.618）–79%（0.786）Fib 帶、OTE sweet spot 70.5% 等講法，corpus 冇教過，一律唔准引入**——佢教嘅係「50%以上到50-79%以上」（3Kt_ruGepB4，transcript 覆核）同下表幾套平行口徑。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯**：讀逐字稿或引文前必須對照 `analysis/lun_trading_profile.md` §5（低浪＝第一浪、聰明前＝聰明錢、贏盔比/盈潰比＝盈虧比、指引點/直升點＝止盈點/止損點、FEG/FBG＝FVG、定型＝釘形、菲波納吉＝Fibonacci、少掉＝掃掉、實況/時光＝時框）。
3. **前置路由**：本 skill 假設偏向已定（`lun-multi-timeframe-analysis`）、時段已揀（`lun-kill-zones-timing`）。OTE 係順勢模型——「我們確認我們是順趨勢走的,我們是跟著動能走的」（3Kt_ruGepB4）；冇偏向就唔好嚟到呢層。
4. **入場確認分層唔好重複**：價格入到 Fib×OB/FVG 疊加區之後「等唔等 K 線確認、追唔追」嘅三層口徑表由 `lun-ict-pd-arrays` 持有——本 skill 只喺 Step 5 畀落單雙選項，唔重抄該表。
5. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| OTE | 「全名呢叫做Optimal Trade Entry」「最佳入場點」；順勢回調入場模型 | 3Kt_ruGepB4 |
| 一句版定義 | 「OTE入場模型。就是強動能破壞。結構破壞。回調」 | hmpAys3lJEo |
| 第一浪／低浪 | 掃描反轉後嘅第一波動能釋放；「我們不要做低浪」（低浪＝第一浪，推測正字） | 3Kt_ruGepB4 |
| 第三浪 | 回調完成後嘅順勢延伸；(transcript)「注意,第三浪呢,一定是最長的」 | 3Kt_ruGepB4 |
| OTE 回調區 | (transcript)「回調到第一浪的50%以上到50-79%以上」（筆記推測＝50%–79% 回調區） | 3Kt_ruGepB4 |
| 便宜價格 | 「就是50%以下,就是大約這邊以下」（折扣半區；劃分紀律→`lun-ict-pd-arrays`） | 7dDW8tF1cZo |
| 共識 | 「第四招就是共識」＝Fib 區×第一浪內 OB/FVG 疊加 | 3Kt_ruGepB4 |

## Workflow（分析流程）

按四招原始次序行（次序本身係規則——每一招都係為咗「讓質量變高」3Kt_ruGepB4）：

**Step 0 — 前置檢查（路由）**：偏向與多時框同向已成立（→`lun-multi-timeframe-analysis`；OTE 片尾「獨家秘訣」＝「我們永遠是做多時框同向的交易機會」，內容歸該 skill）；時段已揀（→`lun-kill-zones-timing`）。

**Step 1 — 第一招：流動性掃描（setup）**

「而第一招呢,就是流動性掃描」——需要價格喺**關鍵位置**出現假突破/掃掉：「昨日的前高位」「上週的前高位,或是前低位。上個月的高低位。或是亞洲盤的高低位。」或紐約盤高低位（3Kt_ruGepB4）。關鍵位必須大級別：「它一定要是大石框的高地位。」「不可以是,喔!是一根K線,這個4小時K線的高地位。」（7dDW8tF1cZo；大石框＝大時框、高地位＝高低位）。掃描機制、池位置清單、點解止損單＝燃料 → 全部轉介 `lun-liquidity-analysis`；本 skill 只收「見到掃描先開始計」呢個 gate。

**Step 2 — 第二招：強動能釋放／結構破壞確認（trigger 之一）**

「第二招就是我們需要確認動能釋放」尤其強動能——**唔准喺高低位直接入**：(transcript)「這樣子的質量非常的低的。」「這根本就是垃圾交易來的。」「因為不是每次,價格碰到了前高位,或是前低位。就會反轉」（3Kt_ruGepB4）。確認標準＝反轉後有強動能釋放／強動能結構破壞：「這個結構破壞呢,我們需要它是以強動能去做破壞的。」「如果它是低動能破壞的話,它其實價值沒有太大。」（7dDW8tF1cZo）。背後邏輯：(transcript)「我們先讓大資金進來先。」「確認我們跟聰明前是同利陣線了之後。」「我們在等待回調,抓順勢交易的機會。」（3Kt_ruGepB4；聰明前＝聰明錢）。K 線力度點判讀（強/弱/組合）→ `lun-price-action-toolkit`。

**Step 3 — 第三招：唔做第一浪，拉 Fib 等回調（trigger 之二）**

(transcript)「重點來了,我們不要做低浪。」「我們不要做,我們讓聰明前或是大資金去做。」回調預期：(transcript)「通常出現低浪反轉之後呢,市場會有80%的機會被看到回調的」（3Kt_ruGepB4；80% 係經驗值無樣本出處，_TEaFyv7-ac 同樣講「有80%的機率」——唔可以當已驗證統計）。目標係第三浪：(transcript)「注意,第三浪呢,一定是最長的。」用 Fibonacci Retracement 由第一浪起點拉到終點（rdXofMdxNEQ：「來從最低位拉到最高位。」）。**回調到位口徑對照表（平行照錄，唔准合併成單一數字帶）**：

| 口徑 | 原話 | 出處／情境 |
|---|---|---|
| 50%–79%（主口徑） | (transcript)「回調到第一浪的50%以上到50-79%以上」（措辭含糊，筆記推測＝50–79% 區） | 3Kt_ruGepB4 OTE 主教材 |
| 61.8 以上 | (transcript)「出現在61.8以上的回調。這個也是OTE的入場模型」 | 3Kt_ruGepB4 例二 |
| 50–61.8 甚至更低 | 「價格回調到我們的Fibonacci,50到61.8,甚至更低些都OK」 | xwsyfVf2l0k 策略一 |
| 50% 以下便宜區 | (transcript)「就是50%以下,就是大約這邊以下」（成個折扣半區搵 FVG/OB） | 7dDW8tF1cZo |
| 38.2/50/61.8/78.6 揀共識 | 「382、50、618、786都可以。我個人喜歡是最多共識的位置」 | 7yDxPi7Roh0 Fib ABC |
| Base Zone 中間線 | 「我Prefer的交易點,其實是Base Zone的中間線,就是一半」 | _TEaFyv7-ac 早期版（單源） |

共同錨係 50% 中線（過咗一半＝夠平），闊窄按片有異——回答時按用戶引用嘅版本對答，預設用主口徑並列明其他口徑存在。反面規則：唔好見 38.2% 就入——「這個時候你不要冒冒然的」「我們要做的是找到confluence」（OANImZtkkeM）。失效條件：「在沒有趨勢的情況下。在市場震盪的情況下。千萬不要用這個策略。完全沒有用的」（7yDxPi7Roh0）。

**Step 4 — 第四招：共識疊加（zone selection）**

(transcript)「第四招就是共識。我們需要找更多的共識,包括了order block,或者是FVG。」條件係**第一浪入面、50% 以內**嘅 OB/FVG/IFVG 同 Fib 區疊埋：(transcript)「然後呢,我們需要50%裡面的。這些疊在一起的話,這個時候配合動能回調到50%裡面。」「那這個時候呢,就是我們的最佳入場時機了。」（3Kt_ruGepB4）。xwsyfVf2l0k 版本：「不管是order block還是FVG,它需要跟其中一個Fibonacci的區間是有重疊。」揀區規則歸 `lun-ict-pd-arrays`（OB 優先於 FVG、觸碰衰減——3Kt_ruGepB4 例一都示範：FVG「已經被觸碰過一次了」就寧願等 OB）；ICI 版本用支撐/主力點/供應需求區代替 OB/FVG 做 confluence（OANImZtkkeM，單源）。**價格入到區之後等唔等確認、追唔追 → 直接引用 `lun-ict-pd-arrays` 嘅三層入場確認口徑表，本 skill 唔重抄。**

**Step 5 — 落單：掛單 vs 觸發確認（order placement，雙選項）**

兩種都係佢畀嘅**permission**：「你要做多?你要在哪裡做?就是在FEG做。」「碰到了再做。或者是你要提前掛單也可以。」／「第一,直接掛單。」「第二,等價格碰到了,再入場。」（7dDW8tF1cZo；FEG＝FVG。同一段引文亦係 lun-ict-pd-arrays 三層確認口徑嘅進取層依據——嗰邊管「等唔等確認先入區」，呢邊管「用邊種單入」，係同一 permission 嘅兩個切面，唔係兩條獨立規則）。佢示範中嘅**preference**：「那我就等價格碰到先。」（7dDW8tF1cZo）；反轉確認後亦可即掛：(transcript)「跌進來之後如果有反轉的話,我們就可以直接掛單。進場。」（3Kt_ruGepB4）。入場 K 線偏好：「我最喜歡的K線形態,就是吞噬形態。」（xwsyfVf2l0k）；ICI 版「只要出現了一根Bullish Candle」（OANImZtkkeM）；早期版可用 Sell Limit 掛 Base Zone 中線，且**入場位由 RR 反推**：「因為如果我在這裡賣的話,那我的Risk Reward Ratio 就沒有一對一了」「所以我就必須把我的Entry拉高」（_TEaFyv7-ac，單源低信心）。

**Step 6 — 止損／止盈初設（本 skill 只設初值，管理歸 exit）**

- **止損**（三個檔位，全部 permission）：「止损點可以離開FEG,離開你的order block都可以。」「或者是直接離開整個U轉的地位都沒有問題。」緩衝示範 5–10 點：「就是我會離開5個點離開這個order block。」「大約10個點左右。」（7dDW8tF1cZo）；避開整數關口（hmpAys3lJEo）；止損太大就棄做該筆（hmpAys3lJEo）。
- **止盈**（初框）：(transcript)「指引點可以在我們的Fibonacci,就是Fibonacci工具的127.2延長。」「甚至你要拉的更高。比如說161.8也是可以。」（3Kt_ruGepB4；指引點＝止盈點）；或對面大級別流動性位——「那我就放昨日的高位作為止盈點。」（7dDW8tF1cZo）；ICI 版「-0.272 或者是叫127%的一個Fibonacci extension」（OANImZtkkeM，單源）。深回調例外（單例推測規則）：(transcript)「因為是會調到78.6。我們直接把指引點拉低一點。拉在0%就好。」（3Kt_ruGepB4——回調越深，目標越保守）。盈虧比預期：「所以我們贏盔比要做超過1比3,其實很容易的」（3Kt_ruGepB4）；示範例 1:3～1:9。移動止損/鎖利/平價保護 → `lun-exit-management`。
- **每筆風險％/倉位** → `lun-risk-management`（本 skill 唔持有）。

**Step 7 — 失敗管理：第一次虧、第二次保守再入**

個別虧損照收：(transcript)「那這一筆虧掉了,沒關係。」（3Kt_ruGepB4）。再入場條件＝偏向未變、結構未破：(transcript)「只要價格沒有打破高位,或者是高時框都有一樣的偏向的話,我們也是可以等待回調。」「這邊可能會是我們第一次入場的位置。可能會失敗。但是第二次入場的話,我們會在這邊。」（3Kt_ruGepB4）；「第一次失敗,第二次還是可以入場」「因為我們偏向是走多」（zgVlK7UBNTY）；「所以第一次可能失敗。沒關係。再進多一次就好」（7yDxPi7Roh0）。注意：呢條唔係無限加注許可——corpus 只示範「再入一次」，冇教第三次。

## 入場模型族譜（演化對照，唔好混用版本）

| 年份 | 版本 | 核心差異 | 出處 |
|---|---|---|---|
| 2023-12 | 動能 Fib 回調 | 動能確認→Fib 由低拉到高等回調（無掃描前置） | rdXofMdxNEQ |
| 2024-01 | ICI Fib 進場 | 趨勢線突破＋Fib×支撐/主力點 confluence；只拿第二三波段 | OANImZtkkeM（單源） |
| 2024-04 | Base Zone 三招 | 假突破→換手（CHoCH）→回 Base Zone 中線；RR 反推 Entry | _TEaFyv7-ac（單源） |
| 2025-08 | 完整入場模型 | 掃描→強動能結構破壞→回調 50% 以下便宜區 FVG/OB | 7dDW8tF1cZo |
| 2025-10 | **OTE 四招（主口徑）** | ＋唔做第一浪/抓第三浪＋50–79% 區＋共識疊加＋多時框秘訣 | 3Kt_ruGepB4 |
| 2026 | Fib ABC／策略一 | 38.2–78.6 揀最多共識位；50–61.8 版 | 7yDxPi7Roh0, xwsyfVf2l0k |

全部同構（掃描/確認→回調→共識入場），但數字口徑同觸發細節唔同——引用邊個版本就用返嗰個版本嘅數字。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅入場執行判斷。一份完整嘅 OTE 入場分析回覆應包含以下六部分，每部分引用對應規則（附 video id）：

1. **前置宣告**：偏向/多時框/時段由邊個 sibling 判定咗、結論係乜（fail 就直接停，唔好硬跑四招）。
2. **四招逐項核對**：掃描（乜位被掃）→ 強動能確認（有/冇，冇就等）→ 回調到位（用邊套口徑、而家喺幾多 %）→ 共識（Fib×邊個 OB/FVG；區內確認轉介 `lun-ict-pd-arrays`）。
3. **落單方案**：掛單定等觸發（列明雙選項＋佢嘅示範偏好）、入場 K 線要求。
4. **止損止盈初設**：三檔止損位＋緩衝、TP 初框（127.2/161.8/對面流動性位）、粗略盈虧比 vs 1:3 門檻；78.6 深回調就縮目標。
5. **失敗預案**：第一次失敗嘅再入條件（偏向未變、高位未破）；震盪市即棄用。
6. **行動銜接**：講明下一步轉介邊個 sibling（入場後管理→exit、倉位→risk），唔好即場代答超範圍問題。

## 實例（corpus 內示範）

### 例一：黃金 5 分鐘 OTE 全流程（3Kt_ruGepB4）

昨日紐約盤低位被打掉→下跌反轉→(transcript)「我們等待價格回調到50%裡面。去找我們要的FVG。」→反轉後直接掛單，止損離開 FVG，止盈揀昨日高位（「黃金大偏向都是做多嘛」），沿途鎖利做到約 1:9。示範重點：四招齊行＋TP 揀對面流動性位而非機械拉 127.2。

### 例二：S&P500 OTE（hmpAys3lJEo，錯過嘅機會）

「就是價格在輸走線上面了之後。EMA50上面了之後。加上趨勢線破壞了之後」——OTE 條件（強動能破壞→結構破壞→回調）疊 EMA50/趨勢線過濾，理論 1:5。示範重點：OTE 可以同 price-action 過濾器（→`lun-price-action-toolkit`）並用；錯過就認——「算是错过了」。

### 例三：比特幣 IFVG 揀區＋兩段抓回調（3Kt_ruGepB4）

第一浪後揀 IFVG（因為佢將 FVG/OB 重疊晒）入場，價格跌穿 161.8 後再回調——高位未破、高時框同向就可以再抓；第二段回調到 78.6，TP 縮到 0%，約 1:3。示範重點：Step 7 再入場規則＋深回調縮目標嘅單例出處。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 流動性池位置/掃描獵殺機制/真假突破測試 | `lun-liquidity-analysis` |
| OB/FVG/IFVG 定義、品質、觸碰衰減、區內三層入場確認口徑 | `lun-ict-pd-arrays`（DRY anchor） |
| 強動能 K 線判讀、吞噬/釘形/圖形、破位策略、ICI 形態本身 | `lun-price-action-toolkit` |
| 偏向/多時框同向/A+ 篩選（OTE 片尾秘訣內容） | `lun-multi-timeframe-analysis` |
| 時段/週節奏/數據日曆 | `lun-kill-zones-timing` |
| 移動止損、平價保護、鎖利節奏、持倉管理 | `lun-exit-management` |
| 每筆風險％、倉位、頻率風控 | `lun-risk-management` |

## 侷限聲明

1. **口徑非教科書（最重要）**：OTE 回調區以 corpus 原話為準——「50%以上到50-79%以上」措辭本身含糊，「50%–79% 回調區」係筆記**推測**整理；教科書 ICT 62–79% 帶唔准引入或「修正」佢嘅數字。
2. **多口徑照錄**：回調深度六套口徑（見 Step 3 表）平行存在，唔裁決邊套「啱」；共識數量參照 `lun-price-action-toolkit`（2–3 底線/3–5 理想，profile §7.3.1）。
3. **經驗值非統計**：「80% 機會回調」（3Kt_ruGepB4, _TEaFyv7-ac）、ICI「成功的機會大概有50-60%」（OANImZtkkeM）均無樣本出處（profile §7.4）；引用時要註明係講者經驗值。
4. **單源低信心**：Base Zone 中線＋RR 反推 Entry（_TEaFyv7-ac）、ICI Fib 進場與 -0.272 止盈（OANImZtkkeM）、78.6 深回調縮 TP（3Kt_ruGepB4 單例）各只有一片/一例來源；使用時降權，建議按 `lun-backtesting-method` 驗證。
5. **推測標註**：「低浪＝第一浪」「聰明前＝聰明錢」「指引點/直升點＝止盈/止損點」等正字全屬 ASR 推測修正；「回調越深目標越保守」係由 78.6 單例歸納嘅**推測規則**，講者冇明講通則。
6. **實績未經對帳**：示範盈虧比 1:5/1:6.2/1:9（3Kt_ruGepB4）、1:8（7dDW8tF1cZo）等全部係覆盤示範或自述；佢本人警告「我公開的交易表現呢,不代表你們也能做到一樣的交易表現」（MjPZizFnX-E）。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — OTE 入場模型證據全錄：四招原話、回調口徑對照、落單雙選項、止損止盈初設、失敗再入場、族譜各版本嘅完整原話引文（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（ASR 容錯對照表，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3；經驗值警告依據 §7.4。
- **Contributing videos（9，per profile §6.5）**：3Kt_ruGepB4（OTE 四招主教材）、7dDW8tF1cZo（完整入場模型）、xwsyfVf2l0k（策略一 50–61.8 版）、hmpAys3lJEo（一句版定義＋實戰）、zgVlK7UBNTY（OTE 成立實例＋再入場）、7yDxPi7Roh0（Fib ABC 38.2–78.6）、rdXofMdxNEQ（動能 Fib 早期版）、OANImZtkkeM（ICI Fib 進場）、_TEaFyv7-ac（Base Zone 早期版）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim，whitespace-join 可；本 skill 已覆核 3Kt_ruGepB4 全片四招/50–79%/127.2/78.6/再入場段落、7dDW8tF1cZo 便宜區/掛單雙選項/止損三檔段落）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `.claude/skills/` 嘅上兩層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
