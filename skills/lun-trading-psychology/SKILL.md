---
name: lun-trading-psychology
description: 按照交易倫（Alan / LunTrading）嘅交易心理與習慣體系做行為層分析——敵人係自己嘅大腦、三層 WHY 動機檢查（結果→過程→身份）、概率思維＋無偏差執行、五特質修煉（察覺/接受/負責任/一致性/耐心）、10 個習慣（2024/2026 兩版本平行呈現）、與情緒合作（情緒＝訊號、唔消滅）、FOMO／報復性交易／過度自信攔截、mental capital 情緒本金、行為金融實證（講者轉述 11 篇論文：95% 定律、profit paradox、情緒 5 天效應）、MBTI 交易員類型（NTJ 特質、F/P 型盲點）、7 個人生教訓（孤獨共存、問心無愧、遠離壓力源）。Use when 交易心理 trading psychology, 習慣 habits, 紀律 discipline, 情緒化交易 emotional trading, FOMO 害怕錯過, 報復性交易 revenge trading, 過度自信 overconfidence, 過度交易心理 overtrading psychology, 交易員類型 trader personality MBTI, 動機 WHY motivation, 教訓 lessons, 心態 mindset, 連虧後心態 losing streak mentality, burnout 交易倦怠 the way 交易倫 teaches. 唔覆蓋風險%數字（risk-management）、記錄工具方法（backtesting-method）、出場規則（exit-management）。
---

# lun-trading-psychology：交易心理與習慣（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅**最後一塊：心理/習慣/動機層**（27/57 份筆記）。佢嘅核心主張：「交易真正的敵人呢,就是你自己的大腦」（OnjOO0QyVUU）、「交易的成功,靠的不是方法,更多靠的是你的習慣」（eIeYQStY5rI）、「你有沒有想過問題可能不是策略罷了?」（HeQiNekCZng）。**本 skill 只持有行為/動機/人格層**——一切可量化規則（風險%、止損位、記錄工具、考試上限）已由 10 個 sibling skills 持有，一律路由（Step 0）；本 skill 同時係 `lun-risk-management` Step 8 錯誤目錄嘅指定接收方（F01–F03、E07/E10、M01–M03/M06，見 Step 9）。所有引文照錄筆記/逐字稿原文（含 ASR 誤字；正字對照見 `analysis/lun_trading_profile.md` §5）。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 診斷**行為根因**：表現差係策略問題定習慣/心理問題（「同樣的策略,不同的習慣,結果也是天差地別的」）
- 檢查**交易動機 WHY**：三層 WHY（結果→過程→身份）、5 Why 追問法、錢-WHY 點樣引致情緒化錯誤
- 建立**概率思維**：大數法則、獨立事件、樣本污染、賭徒謬誤、「無偏差執行」嘅修煉時間表
- 修煉**五特質**：察覺→接受→負責任→一致性→耐心嘅次序同各自練法
- 對照**10 個習慣**：2024 版同 2026 版兩份清單（平行呈現，唔合併）
- 處理**情緒事件**：FOMO、報復性交易、追單、連虧後心態、大賺後飄、mental capital 保護、幾時停手唔睇盤
- 引用**行為金融實證**：講者轉述嘅 11 篇論文結論（95% 定律、profit paradox、5 天效應、存活率漏斗、性別研究）
- 做**交易員類型/人格匹配**：MBTI 四維度、NTJ 成功特質、F 型/P 型盲點、人格可後天矯正
- 攞**人生教訓層**指引：孤獨共存、專注過程、問心無愧、學會防守心態、遠離壓力源、金繼修復觀

**唔應該用嘅情況（路由表，DRY 硬規則）**：

- 風險%數字、倉位公式、連虧降倉、停手線、**虧幾多、開幾大、幾時停** → `lun-risk-management`（本 skill 只持有背後嘅心理機制）
- 交易日記/截圖/覆盤嘅**記錄方法與工具**（Excel/Tradezella、每週覆盤流程、樣本量）→ `lun-backtesting-method`（本 skill 只持有三階段**情緒**記錄嘅內容維度）
- 止損止盈放置、提前出場、平價保護 → `lun-exit-management`（「該出場就出場」嘅情緒本金理由留本 skill）
- 出金後戒飄嘅 prop firm 場景規則、資金太細得失心重→考機構嘅路線 → `lun-prop-firm-playbook`（飄嘅心理循環本體留本 skill Step 8）
- A+ 挑剔過濾標準本體 → `lun-multi-timeframe-analysis`；時段紀律/Burn out 時間表 → `lun-kill-zones-timing`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答。教科書交易心理一律唔准補完：**Mark Douglas《Trading in the Zone》框架、通用 CBT/正念冥想療程、prospect theory/loss aversion 等行為經濟學術語（除非講者原話用過）、NLP 技巧——corpus 冇教，唔准引入**。講者引用過嘅書只有「Untreated Soul」（HeQiNekCZng，推測為 The Untethered Soul）——只可照錄佢嘅轉述，唔准補書本內容。
2. **研究轉述紀律**：OnjOO0QyVUU 嘅論文結論全部係**講者轉述研究，未核對原論文**——引用時必須帶此標記，唔准擅自補充原論文出處、作者全名或方法論細節（「Barber & Odin」照錄 ASR 誤字，推測為 Barber & Odean）。
3. **傳記影片禁區**：Kovner/Seykota/Marcus 等傳奇交易員故事影片喺 corpus 之外，唔准引用；**例外**：oiULdfvMlYY 片內提及嘅交易員 MBTI 名單（Soros/PTJ/Druckenmiller/Simons/Buffett/Richard Dennis）屬 in-corpus，只可喺 MBTI 語境用（Step 8）。
4. **ASR 容錯**：教育＝交易、Y＝WHY、任性＝韌性、希望值＝期望值、精氣＝金繼、指南症＝指南針、付盤＝復盤、比＝筆、過度之心＝過度自信、以其/抱負＝與其/暴富、feel of missing out＝fear of missing out、METR/Myersprick＝MBTI/Myers-Briggs、Paul Tudels-Jones＝Paul Tudor Jones、Stanley Drunken Miller＝Stanley Druckenmiller、Jim Simon＝Jim Simons、半小時＝絆腳石。全表見 `analysis/lun_trading_profile.md` §5。
5. **引用紀律**：「」內文字必須照錄筆記/逐字稿原文，**「」內禁止用「…」省略字詞**——要縮短就拆成兩個獨立「」span、用非引號文字連接；編輯標籤用粗體唔入「」；推論帶（推測）；單源子節帶（單源）；自述經歷帶「自述」；帶「(transcript)」者已直接覆核逐字稿。
6. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 無偏差執行 | 「紀律不是大部分時間做到就好,而是無偏差的去做到」 | 54WCm_VBYfY |
| 概率思維 | 認同大數法則：「短期之內輸贏的分布是隨機的,但是樣本一到,概率就接管了」 | 54WCm_VBYfY |
| 三層 WHY | 淺層（結果/錢）→中層（過程/策略）→深層（身份）；深層先畀到穩定 | ryv0CUgVZCM |
| 情緒＝訊號 | 「情緒永遠不是我們的敵人。它是一種訊號。」唔消滅、唔對抗 | HeQiNekCZng |
| mental capital | 情緒本金——該出場就出場以保住「你的情緒本金也會一直maintain著去」 | T2Nk46EqAh4（單源） |
| 樣本污染 | 100 筆中 70 筆情緒單→「你的樣本呢,被污染了」 | 54WCm_VBYfY |
| 金繼修復觀 | 失敗裂縫可以接返：「那個裂縫就會變成你的金線」 | 54WCm_VBYfY |

## Workflow（分析流程）

按行為診斷順序行：路由 → 定調 → WHY → 概率思維 → 五特質 → 習慣 → 情緒攔截 → 實證 → 人格 → 教訓 → 錯誤目錄。

**Step 0 — 路由檢查（先分流，後分析）**

問題係咪真係行為/動機層？數字規則 → `lun-risk-management`；記錄工具 → `lun-backtesting-method`；出場位 → `lun-exit-management`；考試場景 → `lun-prop-firm-playbook`。只有**點解會咁做、點樣改習慣、動機啱唔啱**留喺本 skill。

**Step 1 — 定調：敵人係自己，成敗靠習慣**

- 三句同構定調（三源互證）：(transcript)「交易真正的敵人呢,就是你自己的大腦」（OnjOO0QyVUU）；「交易裡面最大的敵人不是市場,而是你的內心」（eIeYQStY5rI）；「教育裡面最大的敵人是誰?你自己」（54WCm_VBYfY，教育＝交易）。
- 歸因於習慣而非策略：「你有沒有想過問題可能不是策略罷了?」（HeQiNekCZng）；「你才是最大的問題」、換 100 種策略都冇用（7yDxPi7Roh0）；三角缺一不可——技術＋風控＋情緒（H3OZxavXlsk；風控角本體 → `lun-risk-management`）。
- 平衡視角：系統失效都要先問「是不是市場的節奏改變了」（PypFn7GaVfE via profile §3.13）——唔好將一切歸咎心理。

**Step 2 — WHY 動機檢查（ryv0CUgVZCM，單源）**

- 三層 WHY：「小層的Y,就是更專注在結果」→「中層的Y,就是要把過程給做好」→「第三個Y,是跟你自己的身份有關的Y」；(transcript)「旁邊的Y,會給你方向。但是深層的Y,那種最深層的Y,會給你一個穩定。」（旁邊＝推測：表面/淺層）。
- 錢-WHY 危害：(transcript)「如果你的why是想要賺更多錢的話,那你很有可能會被市場教育的」；結果導向情緒化錯誤鏈——「你就會更容易追單,更容易報復,更容易加倉,然後太早進場,太晚出場」。
- 工具：5 Why 追問法——(transcript)「你要連續問自己5次」搵深層價值；由 WHY 倒推系統設計（穩定→固定時段系統）；WHY 每年演化要回顧。「Y不是心靈雞湯。它更多的是幫助你去培養更好的交易習慣」。

**Step 3 — 概率思維＋無偏差執行（54WCm_VBYfY 骨幹）**

- 大數法則：(transcript)「短期之內輸贏的分布是隨機的,但是樣本一到,概率就接管了」；「每一筆交易都是獨立事件」；「市場是沒有記憶的」；「不是運氣,而是數學」。
- 無偏差執行：(transcript)「紀律不是大部分時間做到就好,而是無偏差的去做到」；時間預期——「不是3個月,至少1年到2年的時間」；三個月挑戰「漏掉了,重新開始」。
- 行為病理：賭徒謬誤（連虧覺得下筆會贏）；樣本污染（70 筆情緒單）；最常見死法係「把一個有正期望值的系統給丟掉」；「不要對單一的數據點又哭有笑」。（期望值數學/樣本量 → `lun-backtesting-method`；等額風險 → `lun-risk-management`。）

**Step 4 — 五特質修煉（54WCm_VBYfY，有次序）**

1. **察覺 awareness**：三階段情緒記錄（入場前/持倉中/出場後，連生理反應）；前提誠實——「你要願意承認你是驕傲的,你要願意承認你是貪婪的」（日記工具方法 → `lun-backtesting-method`）。
2. **接受 acceptance**：預先接受風險/虧損/不確定性——(transcript)「所以你接受了,你就自由了」。
3. **負責任 responsibility**：「你沒有欠市場任何東西,市場也沒有欠你任何東西」；(transcript)「當你把專注力放在你可以控制的事情上面的話,你就不會再焦慮了」（54WCm_VBYfY）；「沒有人會幫你變得富有,你必須付出100%的責任」（T2Nk46EqAh4）。
4. **一致性 consistency**：頂尖運動員式固定流程、「最不能妥協的就是把你做的每一筆交易都記錄下來」。
5. **耐心 patience**：「耐心的過程是需要你不斷地去壓制你的欲望的」；比賽故事「前面45分鐘我們一單都沒有下」。
- 修煉觀：健身類比（心理肌肉未長出前犯錯唔好過度自責）；金繼修復（(transcript)「說到底,教育就是自我修行」）。

**Step 5 — 10 個習慣：兩版本平行呈現（唔合併）**

| # | **2024 版**（eIeYQStY5rI, 2024-08） | **2026 版**（HeQiNekCZng, 2026-01） |
|---|---|---|
| 1 | 專注交易質量而非數量 | 寧可錯過，也不要做錯 |
| 2 | 執行你的交易計劃 | 佈局（下單前寫計劃＋設警報器） |
| 3 | 良好的風險管理 | 嚴格執行風險管理 |
| 4 | 管理好你的情緒 | 學會與情緒合作 |
| 5 | 回顧與反省的習慣 | 回顧你的交易（每週交易解剖） |
| 6 | 耐心 | 培養耐心（等機會/持倉/帳戶增長三層面） |
| 7 | 合理的期望值 | 腳踏實地的目標（過程導向） |
| 8 | 一致性 | 堅持你的交易系統（一年內唔換） |
| 9 | 堅持 | 培養韌性（ASR「任性」；虧損係學費） |
| 10 | 平衡 | 維持生活平衡 |

- 兩版係**唔同清單**（約 6 項主題重疊：風控/情緒/回顧/耐心/堅持/平衡），相隔 17 個月，唔好合併成一份**佢嘅 10 習慣**；引用邊版必須註明年份。2026 版係後期口徑，佢自述憑呢啲習慣通過 FTMO 40 萬考試（自述；考試本體 → `lun-prop-firm-playbook`）。
- 習慣係後天可培養：「這些習慣呢,不是以生俱來的,是可以後天培養的」（eIeYQStY5rI）。

**Step 6 — 情緒管理與攔截機制**

- 與情緒合作（唔消滅、唔對抗）：(transcript)「情緒永遠不是我們的敵人。它是一種訊號。」「我們要訓練自己,什麼都不要去做。讓情緒自己離開就好。」（HeQiNekCZng）；「情緒是沒有辦法去消滅的,但是你要跟情緒共存」（54WCm_VBYfY）；「You don't have to react on your anger」（rLP-MPvGmDE）。
- 攔截規則（逐條附出處）：守不了規則就**停止交易**直到重新遵守為止（oiMlx5UlRLQ）；情緒唔好可以唔睇盤（ryv0CUgVZCM）；大賺大虧後停 3–5 天先返嚟（OnjOO0QyVUU）；主動休息兩星期至一個月去健身/做難事（oiMlx5UlRLQ）／放兩三個星期假充電（s4on4yJCLII）；(transcript) mental capital——該出場就出場保住「你的情緒本金也會一直maintain著去」（T2Nk46EqAh4，單源）。
- FOMO：「焦慮在於你害怕錯過機會。也就是我們常說的feel of missing out」（eIeYQStY5rI，＝fear of missing out）；解藥係「寧可錯過,也不要做錯」（HeQiNekCZng）。
- 報復性交易：成因係連虧後「变得很情绪化」「变得很不甘心」甚至潛意識想解脫，解法「那你就离开」（s4on4yJCLII）；「你覺得不甘心」「你想要報仇」（mDpbsw81ftI）。
- 過度盯盤：「只要我們沒有過度盯盤,我們就不會慌了」、(transcript)「The market is slower than you think.」（T2Nk46EqAh4）。
- 跟單＝心理卸責：「你跟著他們操作了,你虧錢了,你不會怪自己。你怪他們」（T2Nk46EqAh4）；處方「你應該要退出所有的群組」「不要去跟單」（rLP-MPvGmDE）；直覺＝「不去跟從你的交易系統走的一個藉口」（rLP-MPvGmDE）。
- **口徑分層（表面矛盾）**：「退出所有的群組」（rLP-MPvGmDE）vs「找 Trading Coach 與 Community」「你根本不需要孤軍作戰」（oiMlx5UlRLQ）vs「學會與寂寞共存」（0a4NrcfAPJU）——分層讀：跟單訊號群＝卸責要退出；向成功者/教練**學習**＝縮短學習曲線；交易執行本身＝孤獨要接受。三者唔衝突但引用時要指明層次（呢個分層本身屬推測性調和）。

**Step 7 — 行為金融實證（OnjOO0QyVUU，單源；講者轉述研究，未核對原論文）**

- 95% 定律：(transcript)「有95%的人在交易裡面是不賺錢的」；「Barber & Odin」（ASR，推測 Barber & Odean）研究 66,456 個家庭——「交易是有害財富的」。
- profit paradox：(transcript)「就是典型的過度之心」（＝過度自信）——贏錢後「他們未來賺錢的潛能就會大跌60%」。
- persistence of effect：(transcript) 每筆交易嘅情緒影響力「會持續大約5天左右」→ 佢嘅 3–5 天停手規則由此嚟（Step 6）。
- 後悔效應：「他們是不會再買回曾經虧過錢的股票」。
- 存活率漏斗：「75-80%的新手交易員會在2年內消失」→ 3 年剩 13% → 5 年剩 7% → 穩定獲利 3% →「真正賺大錢了吼,是1%」。
- 性別/行為差異：「男性交易員比女性交易員的交易量是多了45%」、(transcript)「女生會比男生平均一年少虧1%」；單身男人更傾向攞風險（「我覺得啦,最主要是單身的男生更想要證明自己」——講者個人解讀）；樂透頭獎超過 5 億台幣散戶交易量大跌 7%（賭性證據）。
- 總結：(transcript)「基本上有97%的人就是敗給人性」；贏家係「少數有紀律」「比較穩定,然後可以長期專注的人」。**所有數字照錄講者口述，唔准當已核實統計引用。**

**Step 8 — 交易員類型／MBTI（oiULdfvMlYY，單源）**

- 四維度：E/I（能量來源）、S/N（獲取信息：S 具體可量化 vs N 背後意義）、T/F（決定：理性 vs 感性）、J/P（計劃 vs 靈活）。
- 研究結論（講者自述「我就針對這方面去做了研究」，來源未列明）：「答案是N型」「頂尖交易員裡面N型的人占比率會比較高」；N/T/J 三特質「在交易成功啊它的相關度是非常高的」；片內傳奇交易員名單——Soros INTJ、Paul Tudor Jones（ASR「Paul Tudels-Jones」）ENTJ、Druckenmiller（ASR「Stanley Drunken Miller」）ENTJ、Jim Simons（逐字稿作「Jim Simon」）INTJ、(transcript)「巴菲特 INTJ」「有時候是ENTJ」「但取決他當下需要達到什麼樣的目的」、Richard Dennis ENTJ（in-corpus 例外，只限此語境）。
- 盲點對應：**F 型**——「該出場不出場」「該止損不止損」「因為會不甘心」、虧錢「怪市場」「怪策略」；**P 型**——「就會很容易出現沒有一致性的情況」，補救係「你要去學習培養那個紀律」。
- 人格可後天改變：(transcript) 講者自述「我是NFP型的」「是非常非常不適合做交易」→ 後天努力→(transcript)「我已經是一個NTJ型了」（oiULdfvMlYY）。**注意（講者自述前後不一）**：0a4NrcfAPJU（2024）另自報 (transcript)「那我的人格呢是ENFJ」——ENFJ 係 J 型，同 **NFP→NTJ** 敘事嘅 P 起點衝突；照 profile §1.3 處理，引用時並列兩次自報、唔裁決。
- 使用原則：「這個16個性格沒有好壞」「都有自己的盲點」、測試要對自己誠實；系統 80/20——「所有條件只佔了80%」「還有20%是主觀判斷的」（主觀判斷＝判斷要唔要更挑剔）。

**Step 9 — 人生教訓層（7 個教訓：0a4NrcfAPJU＋jlO3771JF1E 兩集，單源系列）**

1. 與孤獨共存——「其實你做交易的話,你一定是孤獨的」；接受後「你就再也不需要證明給任何一個人看」。
2. 分散但只做熟悉領域——「不熟,不做」（規則本體 → `lun-risk-management` Step 2）。
3. 專注過程唔專注結果——「過度的專注在結果上面,會讓你很痛苦」；「真正有價值的是,過程中的每一段學習」。
4. 搵自己嘅人生意義——人生羅盤比喻：「他們用著別人的羅盤來過自己的人生」。
5. 問心無愧——(transcript)「我从小到大都有一个原则,就是我要做到问心无愧」；拒絕割韭菜快錢；「守住自己的原则其实是无价」。
6. 學會防守——「很多人赚到钱后就飘了」（jlO3771JF1E）；承認運氣成分（「可能就只是纯粹运气好」jlO3771JF1E）；反面教材 8 個月蝕超過 80 萬美金（自述，jlO3771JF1E；資金防守規則 → `lun-risk-management`）。飄嘅循環：大出金→「過度興奮」→表現下滑→連虧→由最簡單步驟重建（mDpbsw81ftI 學員案例；出金後場景規則 → `lun-prop-firm-playbook`）。
7. 遠離人生壓力源——「不要听家人的意见」（唔係惡意，係「他们没有走过你要走的路」）；只跟該領域成功嘅人學習。
- 長期主義收束：「交易是馬拉松,不是短跑」（eIeYQStY5rI）；「你可以交易個10年,20年,30年這麼久」（H3OZxavXlsk）。

**Step 10 — 錯誤目錄承接（接收 `lun-risk-management` Step 8 路由）**

| 承接 id | 項目 | 心理機制（本 skill 持有） | 出處 |
|---|---|---|---|
| F01 | 冇主見（靠跟單） | 卸責機制：「你虧錢了,你不會怪自己。你怪他們」；退群、唔跟單 | T2Nk46EqAh4, rLP-MPvGmDE |
| F02 | 過度盯盤 | 盯盤→慌→情緒化；「The market is slower than you think」；分析麻痹（M04 關聯） | T2Nk46EqAh4, H3OZxavXlsk |
| F03 | 執行力差 | 無偏差執行修煉 1–2 年、三個月挑戰、心理肌肉觀 | 54WCm_VBYfY, T2Nk46EqAh4 |
| E07 | All-in | 報復/不甘心/想解脫嘅衝動；攔截＝離開市場 | s4on4yJCLII |
| E10 | 放棄太早 | 「交易是真的需要时间去锻炼的」；失敗當學費前提係有分析原因 | s4on4yJCLII, oiMlx5UlRLQ |
| M01–M03 | 捷徑/隨處可交易/當遊戲 | 成功沒有捷徑（16 小時×半年～1 年＋2 年情緒管理）；專注力要求；遊戲心態→賭性強 | H3OZxavXlsk |
| M06 | 天天賺錢幻想 | 「有賺錢,也會有賠錢」「這就是交易的本質嘛」；合理期望值（唔好 weekly/daily target） | H3OZxavXlsk, oiMlx5UlRLQ |

（M04 時間≠回報、M05 三角論嘅風控後果層 → `lun-risk-management` 持有，唔好搬返嚟。）

## Output（輸出）

本 skill 嘅輸出係**對話式行為分析指引**——唔生成檔案、唔畀投資建議、唔做臨床心理診斷。一份完整回覆應包含（每部分附 video id）：

1. **路由聲明**：邊部分屬行為層、邊部分已轉交邊個 sibling（尤其數字規則同記錄工具）。
2. **根因定位**：用 Step 1–2 判斷係動機（WHY）、思維（概率）、特質（五特質邊瓣）、定習慣缺口。
3. **對應機制**：引用具體攔截規則（停手/唔睇盤/3–5 天/休息充電）或習慣清單條目，註明 2024/2026 版本。
4. **實證支持**：如引 OnjOO0QyVUU 數字，必帶「講者轉述研究，未核對原論文」標記。
5. **人格匹配**（如適用）：MBTI 盲點對應＋（單源）標記＋自報不一 caveat。
6. **警告聲明**：單源標（單源）；自述經歷標「自述」；推測性調和（如 Step 6 群組口徑分層）標（推測）；教科書心理學概念一律拒絕補完並說明原因。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 風險%、倉位、連虧降倉、停手線、錯誤目錄 E01–E06/E08–E09/M04–M05/K01 | `lun-risk-management` |
| 交易日記工具、截圖覆盤流程、樣本量、100 筆挑戰 | `lun-backtesting-method` |
| 止損止盈放置、80% 提前出場規則本體 | `lun-exit-management` |
| 出金後戒飄嘅 prop firm 規則、資金細→考機構路線 | `lun-prop-firm-playbook` |
| A+ 挑剔四大標準、垃圾交易過濾 | `lun-multi-timeframe-analysis` |
| 時段揀選、Burn out 時間表、唔用手機交易嘅 routine | `lun-kill-zones-timing` |

## 侷限聲明

1. **單源子節多**：MBTI（oiULdfvMlYY）、11 篇論文（OnjOO0QyVUU）、三層 WHY（ryv0CUgVZCM）、mental capital（T2Nk46EqAh4）、6 迷思（H3OZxavXlsk）、5 妙招（oiMlx5UlRLQ）、5 秘訣（rLP-MPvGmDE）、7 教訓（兩集系列）各為單源，使用時聲明。
2. **研究未核對**：OnjOO0QyVUU 全部統計數字（95%/60%/5 天/45%/1%/2.2 兆/97%）係講者口述轉述，原論文未核對；「我看到的研究」（oiULdfvMlYY MBTI 相關度）來源未列明——一律唔可當已驗證統計。
3. **MBTI 自報不一**：ENFJ（0a4NrcfAPJU, 2024）vs **NFP→NTJ**（oiULdfvMlYY, 2026）——講者自述前後不一，corpus 冇解釋，並列唔裁決（profile §1.3）。
4. **10 習慣兩版未調和**：2024/2026 兩份清單唔同，corpus 冇講係演化定重寫，只可平行呈現（Step 5）。
5. **自述經歷未對帳**：80 萬美金虧損、輕生念頭後重建、FTMO 40 萬通過、學員案例（40 萬 funded 飄咗連虧五個月）均為自述。
6. **教科書禁區**：Mark Douglas、通用 CBT/正念、行為經濟學術語補完、傳記影片故事（corpus 外）——一律唔准引入；「Untreated Soul」只可照錄講者轉述。
7. **群組口徑分層屬推測**：Step 6 嘅**退群 vs 教練社群 vs 孤獨**三層調和係本 skill 嘅推測性讀法，corpus 冇明講三者關係。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 心理層證據全錄：定調三句、WHY 框架、概率思維、五特質、10 習慣兩版、情緒攔截規則、論文轉述數字、MBTI、7 教訓、錯誤目錄心理機制（verbatim＋video id）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5；MBTI 自報不一依據 §1.3；scope 依據 §6.11；歸因習性依據 §3.13–3.14。
- **Contributing videos（27，per profile §6.11；另 PypFn7GaVfE 只經 profile §3.13 引用一句平衡視角「是不是市場的節奏改變了」，非 contributing）**：骨幹——54WCm_VBYfY（概率思維＋五特質）、HeQiNekCZng（2026 版 10 習慣）、eIeYQStY5rI（2024 版 10 習慣）、ryv0CUgVZCM（WHY）、OnjOO0QyVUU（11 論文）、oiULdfvMlYY（MBTI）、0a4NrcfAPJU＋jlO3771JF1E（7 教訓）、rLP-MPvGmDE（5 秘訣）、oiMlx5UlRLQ（5 妙招）、H3OZxavXlsk（6 迷思）、T2Nk46EqAh4（mental capital＋3 致命失誤）、s4on4yJCLII（報復/放棄）、mDpbsw81ftI（飄嘅循環）、7yDxPi7Roh0（歸因自己）；其餘（48pCaOfGGmA、91Hpt_LyJSE、nzZ5oqmLjhM、CJi1ltRQnys、E0PF_0XLDGo、GINdJCIIEvw、hkCvRoLc3Nk、RdnJw-mhwlE、rE21_onS0uo、teVdcguZs_U、xmHaONnNrCw、zgVlK7UBNTY）主要貢獻已由 sibling skills 持有，本 skill 只作行為語境銜接。
- **逐字稿**：`data/transcripts/<video_id>.txt`（標「(transcript)」者為直接覆核；本 skill 已覆核 54WCm_VBYfY 紀律/接受/大數法則/控制/自我修行句、HeQiNekCZng 情緒訊號/寧可錯過/讓情緒離開句、eIeYQStY5rI 靠習慣/馬拉松句、OnjOO0QyVUU 大腦/95%/5天/paradox/少虧1%/97% 句、ryv0CUgVZCM why-錢/5次句、oiULdfvMlYY NFP/NTJ 句、oiMlx5UlRLQ 停止交易句、T2Nk46EqAh4 slower/mental capital 句、jlO3771JF1E 问心无愧句、0a4NrcfAPJU 寂寞共存/ENFJ 句）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `skills/` 嘅上一層目錄）；skill-relative 寫法即 `../../analysis/lun_trading_profile.md`、`../../data/transcripts/<video_id>.txt`；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
