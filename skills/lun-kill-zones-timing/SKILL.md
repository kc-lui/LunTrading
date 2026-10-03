---
name: lun-kill-zones-timing
description: 按照交易倫（Alan / LunTrading）的教法決定「幾時交易」——三大交易時段（亞洲盤/倫敦盤/紐約盤 session）與黃金獵殺時段（Kill Zone）具體時間表（紐約時間）、時段配品種、9點半規則、每小時檢查一次的時段紀律、時間出場規則（10點停手/絕不過夜/凌晨5點前平倉）、Weekly Market Profile 三種週節奏形態（「沒有掃描,沒有交易」）、同 Forex Factory 紅色新聞數據日曆佈局（只要時間日期、唔猜結果）。Use when choosing trading sessions / kill zones（獵殺時段）/ timing filters, planning weekly rhythm（週節奏）or news-event（新聞事件/數據公布）timing the way 交易倫 teaches, or answering 「幾時先應該交易」「邊個時段做邊啲品種」「數據公布點佈局」. 唔覆蓋時段內嘅入場模型、流動性掃描機制、出場管理（見 sibling skills）。
---

# lun-kill-zones-timing：交易時機——時段／週節奏／數據日曆（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅「幾時交易」決策層——由日內 Kill Zone、週節奏（Weekly Profile）到數據日曆，三層時間邏輯合成一個 skill（per profile §6.0 合併決定）。所有規則同引文均出自佢 YouTube 影片嘅 ASR 逐字稿與筆記（引文照錄原文，含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。唔好摻入 corpus 以外嘅通用 ICT kill zone 時間表或教科書 session 時間。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。佢嘅總定調：「很多教育員都沒有搞懂市場的運作是有時間邏輯的」（E0PF_0XLDGo；教育員＝交易員）。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 決定應該喺邊個時段交易、每個時段配咩品種（時段配品種表＋9點半規則）
- 解釋 Kill Zone 係咩、點解喺獵殺時段入場盈虧比同勝率會更好
- 設計時段紀律（每小時檢查一次、幾點停手、幾點前平倉、絕不過夜）而唔使全日坐盤
- 用 Weekly Profile 三形態判斷一週節奏（週幾可能出現該週高低點、週一應唔應該交易）
- 圍繞 Forex Factory 紅色數據做成週佈局（週日排程、只取時間日期、數據後等獵殺）
- 判斷某筆交易機會係咪「超出時段」應該放棄

**唔應該用嘅情況**：

- 時段內嘅具體入場觸發（掃描→結構破壞→回調入場）→ 用 `lun-ote-entry-model`
- 流動性池位置、掃描/獵殺機制、真假突破判斷 → 用 `lun-liquidity-analysis`（DRY：session 高低位＝流動性位，機制層以該 skill 為準）
- London Breakout／倫敦破位策略嘅執行細節（區間闊窄判別、破位入場）→ 用 `lun-price-action-toolkit`（策略入場模式由該 skill 持有）
- OB/FVG/PD array 定義 → 用 `lun-ict-pd-arrays`；出場/平價保護/標準差投射 → 用 `lun-exit-management`
- 時框分工（HTF→LTF）→ 用 `lun-multi-timeframe-analysis`；倉位/風險% → 用 `lun-risk-management`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答；唔可以摻入講者未教過嘅通用 ICT kill zone 講法（例如佢冇講過嘅 midnight open、CBDR、silver bullet 時間窗——tCfmxMX5WaU 只預告過「ICT 時段/銀彈策略」但**僅預告未教**）。引用「」內文字必須照錄，唔可以改寫。
2. **時區口徑**：Kill Zone 時間表全部係**紐約時間**（CJi1ltRQnys 明言，並教用時間轉換器換算本地時間）；但 QZNzq-BunA4 用「美國時間」講全 session、用「我們的時間」（講者身處馬來西亞）講亞洲盤換盤——引用時必須保留原語境，唔好自行換算後當引文。
3. **ASR 容錯**：讀逐字稿或引文前必須對照 `analysis/lun_trading_profile.md` §5 容錯表（獵莎/裂殺＝獵殺、梅子＝美指、教育＝交易、專友們＝戰友們、紅盤＝橫盤、少掉＝掃掉、實況＝時框、評價保護＝平價保護、隱窺比＝盈虧比）。
4. **Sibling 依賴**：本 skill 答「幾時」；「喺邊」（流動性位）→`lun-liquidity-analysis`、「點入」→`lun-ote-entry-model`、「點出」→`lun-exit-management`。Sibling 講到「獵殺時段」「session 時間」「週節奏」「數據日曆」時，以本 skill 為準（DRY anchor）。
5. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 三大時段 | 亞洲盤/倫敦盤/紐約盤；日線 K 線由三時段波動形成；倫敦交易量最大 | CJi1ltRQnys, QZNzq-BunA4 |
| 黃金獵殺時段（Kill Zone） | 「出現的該日最高價,或者是該日最低價的機率是最高的」時間段 | CJi1ltRQnys |
| 9點半規則 | 美指等 9:30 之後先做——「因為9點半以前,很多獵殺的情況出現」 | CJi1ltRQnys, hmpAys3lJEo |
| Session 高低位 | 三時段各自嘅高低位＝流動性參考位（機制歸 lun-liquidity-analysis） | aSZzhnfOVkE, 7dDW8tF1cZo, RjNBnZ59c4U |
| Weekly Profile | 週節奏三形態：經典擴張/週中反轉/橫盤震盪（單源低信心） | E0PF_0XLDGo |
| 紅色數據 | Forex Factory 上「最有價值的波動力是最大的」數據（單源低信心） | kI5idYixD50 |

## Workflow（分析流程）

回答「幾時交易」相關問題時，按次序行以下步驟：

**Step 1 — 定位時間層（日內 / 週 / 事件）**

先分清問緊邊層：日內時段選擇→Step 2–4；週節奏→Step 5；數據事件→Step 6。三層可以疊加（例如：紅色數據日＋獵殺時段內＝雙重過濾）。前提認知：識三個時段本身冇用——「你真正要懂的是,到底有沒有一個特定的時間段,是很值得讓你去做交易的」(transcript, CJi1ltRQnys)。

**Step 2 — 套用黃金獵殺時段時間表（全部紐約時間）**

| 時段 | 黃金獵殺時段 | 品種（CJi1ltRQnys 單源） |
|---|---|---|
| 亞洲盤 | 「晚上8點到凌晨12點」 | 日圓/澳幣/紐西蘭相關；指數 AUS200、JPN225 |
| 倫敦盤 | 「凌晨2點到凌晨5點」 | 歐元/英鎊相關（EURUSD、GPUSD〔推測 GBPUSD〕）；指數 DAX、FPSC100〔推測 FTSE100〕 |
| 紐約盤 | 「早上8點到早上11點」 | 美元相關；指數 SP500、DAOJONS30〔推測 Dow Jones 30〕、NAS100；美指等 9:30 後先做 |

原理：Kill Zone 內「出現的該日最高價,或者是該日最低價的機率是最高的」，喺極值位入場「那你的盈虧比不是變高了嗎?同時你的勝率也會更好」（CJi1ltRQnys）——但「雖然不是每一天都這樣」(transcript)，係機率唔係保證。紐約盤兩個口徑並列（唔好抹平）：口播版 8am–11am（CJi1ltRQnys）vs ICT Killzone and Pivot 指標設定「Killzone是9點半開始到11點」而佢本人「我會從8點就開始看盤了」(transcript, 7dDW8tF1cZo)。特例：黃金三個盤「其實都可以做」；虛擬貨幣異常波動難做、「週末去抓虛擬貨幣的話反而會比較容易」但佢照跟自己獵殺時段規則做（CJi1ltRQnys——例外情況照跟主規則嘅示範）。

**Step 3 — 揀適合自己嘅時段（唔係全部都做）**

「答案是選擇適合你的獵殺時段」——揀「你可以在電腦面前很有精神,很有活力,充滿幹勁」嘅時段；「你是不需要每一個時段都做,這樣子你很快會心很累」「你會Burn out」（CJi1ltRQnys）。Permission vs preference 並列：佢全職「其實三個時段都可以做的」但「我盡量專注在紐約盤跟倫敦盤罷了」(transcript)。唔活躍時段唔做：「在不活躍的時段做交易其實沒有太大的意義,利潤空間也不大」（CJi1ltRQnys）；「聰明人你一定會發現,倫敦盤跟紐約盤的動能一定是最大的」（QZNzq-BunA4）。

**Step 4 — 執行時段紀律（時間規則清單）**

- [ ] **每小時檢查一次**，唔使四個鐘坐盤：「可能我每一個小時會看你吃盤」，只睇有冇交易機會＋倉位管理（CJi1ltRQnys；Buffet 比喻——長坐盤「你很容易變得情緒化」）
- [ ] **參考 routine**（佢個人版，時間口徑推測為紐約時間——與同片 KZ 時間表一致，非原話明示）：2點開始每小時睇到5點→停→8點重新每小時睇→「到10點我就決定要不要出場,還是我要評價保護」（CJi1ltRQnys）
- [ ] **停手/平倉時間規則**（情境分層，唔好合併成一條）：晚上10點後唔開新單（QZNzq-BunA4）；日內系統 11–12 點出場、「我們不要hold overnight」（7j7_mhfda38 考試系統）；持倉過亞洲盤開市前要平倉避點差——「萬一點差變大的時候。你可能會被提早掃出去」（QZNzq-BunA4）
- [ ] **持倉係選項唔係義務**：「你可以選擇去持艙,或者是獵殺時段結束後,你想要出場,其實都ok的」（CJi1ltRQnys；permission）
- [ ] **超出時段就放棄該筆**，偏向可以留低：「所以這一筆加就算了,」「不過偏向之後還是會繼續做空」（Q371XdV3apE）
- [ ] **錯過就等聽日**：「錯過了,就沒關係,我就去等第二天這樣子」（CJi1ltRQnys）

**Step 5 — 子節：Weekly Profile 三形態〔單源低信心：E0PF_0XLDGo 一片〕**

總邏輯：「市場呢,要嘛就創造流動性,要嘛去尋找流動性,掃描流動性,或者是失衡了之後,要回到平衡點,找回平衡」。三形態（紅盤＝橫盤）：

| 形態 | 節奏 | 交易含義 |
|---|---|---|
| 經典擴張 | 週一動能累積/去 HTF PD array→週二掃週一高低位、「價格會創該週最高點,或者是最低點」→週二至四釋放→週五回調找平衡 | 掃描＋反轉後入場；保守版等打破高位先入 |
| 週中反轉 | 週一二無動能橫盤，「到了星期三才少掉了週一的低位」先反轉，週三至五釋放 | 等週三掃描 |
| 橫盤震盪 | 週一二三橫盤，週四先掃週一二高低位 | 較少見；「週一,週二,週三,都在橫盤的話」就唔做 |

鐵律：「沒有掃描,沒有交易」；連續動能釋放無掃描都唔做；用此方法「你週一呢,是不用交易的」（週一要交易須用 Daily Bias——`lun-liquidity-analysis` 覆蓋）。時框：最低 15 分鐘、日線/4H/1H 睇節奏、1 小時入場已夠。出場：「到了下一個PD array,其實你就可以出場了」、唔使持到週四五——「你越想要持越久,你很快就失敗了」。實戰旁證：hmpAys3lJEo 用「周三價格打破了周二跟周一的高位」推「那周四周五可能都會下跌」。

**Step 6 — 子節：數據日曆佈局〔單源低信心：kI5idYixD50 一片〕**

三招成週佈局：①**週日篩選**——開 Forex Factory 漏斗「只打勾紅色跟灰色的數據罷了」（紅色＝波動最大、灰色＝銀行假期），核心原則「我們只需要知道數據公布的時間還有日期就夠。數據的結果不重要。」唔猜方向；邊隻貨幣有紅色數據就專注該貨幣相關品種。②**等待獵殺**——「等待那些品種在數據公布之後出現流動性掃描」（機制→`lun-liquidity-analysis`）。③**入場模型**——「跟ICT第五集分享的是一樣的」，結構轉換後喺 FVG/OB 入（執行→`lun-ote-entry-model`）。明確否定跨式雙向掛單：「它長期下來是不會幫你賺到錢的」「很多時候兩單都會被觸發到,然後兩單都會虧」。出場配合動能壽命：「大数据带来的动能很快就会被消耗完了」，唔好持太久，穩定「1比3 1比4」好過硬追 1比10。第一次激進入場失敗，第二次「我都会等一个结构破坏啊还是什么在进」。

**Step 7 — 同 sibling 整合（時段＝過濾器）**

時段層嘅輸出係一個 yes/no 過濾器＋品種清單：獵殺時段內（Q371XdV3apE 用「獵殺時段」做入場過濾）＋session 高低位做流動性錨（「這三個階段的高地位,都可以是我們的BuySight或是小Sight,Liquidity」transcript, 7dDW8tF1cZo→機制歸 `lun-liquidity-analysis`）→ 之後嘅入場/出場全部轉介 sibling。London Breakout／倫敦破位策略嘅執行歸 `lun-price-action-toolkit`（本 skill 只持有其時段依據：「因为伦敦开市之后」「所有的Transaction是最高的」VjSB-VRyxWI）。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔落單，只提供按交易倫口徑嘅時機判斷。一份完整嘅 timing 分析回覆應包含以下五部分，每部分引用對應規則（附 video id）：

1. **時段判定**：而家/目標時間屬邊個時段、係咪黃金獵殺時段內（紐約時間換算講清楚）、該時段配咩品種，唔匹配就講明「唔活躍唔做」。
2. **週節奏定位**（如適用）：本週行到邊個 Weekly Profile 形態、週一高低位掃咗未、「沒有掃描,沒有交易」檢查結果——並標明呢層係單源低信心。
3. **事件檢查**（如適用）：本週紅色數據時間表、目標品種有冇受影響、數據前後嘅等獵殺安排——並標明單源低信心。
4. **紀律清單**：適用嘅時間規則（每小時檢查、10點停手、過夜與否、亞洲盤開市前平倉）逐項核對。
5. **行動銜接**：講明下一步轉介邊個 sibling skill（流動性錨→liquidity、入場→ote、出場→exit），唔好即場代答超範圍問題。

## 實例（corpus 內示範）

### 例一：一週實戰嘅時段紀律（hmpAys3lJEo）

交易解剖示範點樣將時段規則織入實戰：「我通常早上不看盤。那我是等到倫敦時段」先開始搵機會；做指數「我通常是9點半才會入場」（9:30 規則嘅實戰版）；偏向判斷用週節奏——「你看,周三價格打破了周二跟周一的高位」做假突破，推論「那周四周五可能都會下跌」（Weekly Profile 思路嘅應用旁證）。示範重點：時段層先過濾「幾時睇盤/幾時入場」，之後嘅觸發同管理交返俾策略層。

### 例二：亞洲盤區間決定倫敦盤點做（QZNzq-BunA4）

Session 結構直接餵入策略選擇：第一步「我們一定要確認亞洲盤的高位跟亞洲盤的低位」→ 區間窄（無動能釋放）做倫敦破位、區間闊（「相差一段距離就代表亞洲盤其實有動能釋放」）等倫敦假突破反做（判別與入場執行→`lun-price-action-toolkit`）。時間紀律收尾：假突破出現「已經超過了10點。晚上10點。基本上我就已經再不做交易了」；持倉「你要在凌晨5點之前就是收盤之前出場」避點差。示範重點：本 skill 嘅時段錨（亞洲盤高低位＋時間規則）點樣包住一套完整策略嘅頭尾。

### 例三：獵殺時段作放棄準則（Q371XdV3apE）

止盈教學片入面，一個交易機會因為超出獵殺時段被直接放棄：「所以這一筆加就算了,」「我們就不要做先,不過偏向之後還是會繼續做空」——時段唔啱，偏向保留，等下一個時段內嘅機會。示範重點：時段係一票否決嘅過濾器，唔係加分項。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 流動性池/掃描/獵殺機制、真假突破 | `lun-liquidity-analysis`（DRY anchor） |
| 倫敦破位/假突破策略執行、London Breakout 入場細節 | `lun-price-action-toolkit` |
| 掃描後入場四步、FVG/OB 掛單 | `lun-ote-entry-model`；元素定義→`lun-ict-pd-arrays` |
| 平價保護、標準差投射、分批鎖利 | `lun-exit-management` |
| HTF→LTF 分工、A+ 篩選 | `lun-multi-timeframe-analysis` |
| 風險%、止損30點上限、頻率風控 | `lun-risk-management`；防 Burn out 心理層→`lun-trading-psychology` |

## 侷限聲明

1. **單源低信心（顯著）**：Weekly Profile 成個子節只有 E0PF_0XLDGo 一片（hmpAys3lJEo 僅一次實戰旁證）；數據日曆佈局成個子節只有 kI5idYixD50 一片；時段配品種表、每小時檢查一次、亞洲盤開市前平倉避點差各只有一片來源。使用時降權，並建議按 `lun-backtesting-method` 做樣本驗證。
2. **時間表雙源但有口徑差**：Kill Zone 時間 CJi1ltRQnys＋7dDW8tF1cZo 雙源互證，但紐約盤「8–11am 口播」vs「指標 9:30–11:00」兩口徑並列（見 Step 2），唔好合併成單一數字。
3. **僅預告未教**：tCfmxMX5WaU 預告過 ICT 時段/銀彈（silver bullet）策略但冇教學內容——唔可以引用該片充當時段規則來源，亦唔好用通用 ICT 銀彈時間窗補完。
4. **矛盾/多口徑照錄**：全 session 時間（QZNzq-BunA4，「美國時間」/「我們的時間」）vs Kill Zone（紐約時間）係兩個概念層；亞洲盤取態三口徑（CJi1ltRQnys 可做配品種／7j7_mhfda38 考試系統關掉唔做／RjNBnZ59c4U 波動率高執行唔嚟就用 4H/1H）屬情境差異；數據入場用 1/3/5 分鐘（kI5idYixD50）vs「低过5分钟我个人非常不认同」（RjNBnZ59c4U）——per profile §7.3.5 照錄唔裁決；交易頻率週 3-5 筆 vs 月 3-5 筆以後期口徑為主（profile §7.3.6，主體歸 `lun-risk-management`）。
5. **教學示範值，非驗證統計**：「機率是最高的」「盈虧比不是變高了嗎」同所有盈虧比例子（1比2/1比3/1比10）均為講者經驗值/示範，無樣本出處，未經獨立對帳（profile §7.4）。
6. **ASR 來源**：所有引文出自 ASR 逐字稿，含系統性誤字（獵莎＝獵殺、梅子＝美指、專友們＝戰友們、紅盤＝橫盤）；品種名 GPUSD/FPSC100/DAOJONS30 等為 ASR 變體，正字屬推測，引用照錄原文。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 交易時機證據全錄：三大時段與 Kill Zone 定義、時間表（雙源互證＋指標設定版）、時段配品種、揀時段原則與紀律 routine、時間出場規則、session 高低位＝流動性錨、Weekly Profile 三形態、數據日曆三招、心態時段語境嘅完整原話引文（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（ASR 容錯對照表，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3；未教邊界依據 §7.1。
- **Contributing videos（10＋2 子節，per profile §6.6）**：CJi1ltRQnys（Kill Zone 主教材）、7dDW8tF1cZo（時間表指標設定＋session 高低位）、QZNzq-BunA4（session 定義＋時間出場規則）、7j7_mhfda38（倫敦紐約硬過濾＋絕不過夜）、hmpAys3lJEo（個人時段紀律＋9點半旁證）、Q371XdV3apE（時段作入場過濾）、RjNBnZ59c4U（session 指標＋亞洲盤執行難度）、aSZzhnfOVkE（session 高低位＝流動性）、VjSB-VRyxWI（London Breakout 時段依據）、E0PF_0XLDGo（Weekly Profile 子節，單源）、kI5idYixD50（數據日曆子節，單源）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim，whitespace-join 可；本 skill 已覆核 CJi1ltRQnys 全文時間表/routine 段落同 7dDW8tF1cZo 嘅 Killzone 指標設定段落）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `skills/` 嘅上一層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
