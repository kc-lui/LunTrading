---
name: lun-backtesting-method
description: 按照交易倫（Alan / LunTrading）嘅回測與系統驗證方法測試同記錄交易系統——TradingView 回放（replay）bar-by-bar 手動回測、最少 100–200 單樣本、跟實際可交易時段模擬、截圖＋寫低原因（包括跳過嘅交易）、系統信心數據（預期回報 expectancy／預期連續虧損 consecutive losses／連續賺錢／Average RRR）、交易日記與每週/季度覆盤、模擬→小資金→大資金路徑、多系統框架與 100 筆交易挑戰。Use when 回測 backtest／backtesting, 驗證策略 validating a strategy, 複盤/復盤 review, 樣本 sample size, 100筆 100-trade challenge, 系統信心 system confidence data, 預期連敗 expected losing streak, 期望值 expectancy, 交易日記 trading journal, 多系統 multi-system framework the way 交易倫 teaches. 唔覆蓋心理習慣本身（trading-psychology）、具體策略規則（各策略 skill）、風險%（risk-management）。
---

# lun-backtesting-method：回測、記錄與系統驗證（交易倫版）

> 本 skill 係交易倫 11-skill 體系嘅「驗證」層——由「學完一套策略」到「敢用真錢執行」之間嘅全部工作：手動回測、樣本量、記錄、數據產出、日常覆盤、同埋用 100 筆挑戰揀系統。主教材係 RdnJw-mhwlE（跟我一起回測——實錄示範）；子節「多系統框架與 100 筆挑戰」吸收自 PypFn7GaVfE，另有 ≥14 片支撐素材（per profile §6.8）。**佢嘅方法係手動 TradingView 回放式回測**——corpus 冇教 walk-forward、Monte Carlo、程式化回測等教科書方法，一律唔准引入。所有引文照錄筆記/逐字稿原文（含 ASR 誤字；**「回撤」喺 RdnJw-mhwlE 全片＝回測**，正字對照見 `analysis/lun_trading_profile.md` §5）。核心宣言：「所以回撤就是可以让你在不需要」「浪费你的血汗钱的情况下」「去锻炼你的执行力」「去得到一些数据」「然后呢去测试这个系统」（RdnJw-mhwlE）。完整原話證據全錄喺 [references/evidence.md](references/evidence.md)。

## When to Use（何時使用）

用呢個 skill 當你需要：

- 為一套啱學完嘅策略設計回測計劃：工具（TradingView 回放）、樣本量（最少 100–200 單）、時段限制、記錄格式
- 執行 bar-by-bar 手動回測：唔睇後市、邊行邊講 thought process、心態同實倉一致
- 決定樣本量門檻：幾多筆先「夠扎實」、幾多筆先可以小資金實戰、幾多筆先可以考 prop firm 試
- 由回測/實倉數據整理「系統信心數據」：預期回報、預期連續虧損/連續賺錢單數、勝率、Average RRR、交易頻率、平均持倉時間
- 建立日常記錄制度：每筆（含跳過嘅）截圖＋原因、交易日記三階段情緒記錄、Excel/Tradezella
- 做每週/每月/季度覆盤：逐張截圖評價、季度指標（勝率/平均盈虧比/R 分佈/資金曲線健康度）、由最好 10 筆提煉入場標準
- 規劃實戰路徑：模擬→小資金→大資金；用刻意練習（千張截圖/搵 100 個機會）訓練眼同腦
- 揀系統/換系統：一個一個測試、100 筆交易挑戰、按性格配對、判斷「系統失效」定「市場節奏改變」

**唔應該用嘅情況**：

- 連虧時嘅情緒處理、對系統失去信心嘅心理機制本身 → 用 `lun-trading-psychology`（本 skill 只提供「用數據防跳系統」嘅論證同數據清單）
- 被回測嘅策略規則本身（Pivot+Price Action 示範規則、五套系統概觀、Wyckoff 四階段）→ 用 `lun-price-action-toolkit`；流動性系統定位 → `lun-liquidity-analysis`
- 每筆風險 %、等額風險、連虧降風險 → 用 `lun-risk-management`（回測期間落幾大唔係本 skill 管）
- prop firm 考試規則與考試場景執行 → 用 `lun-prop-firm-playbook`（本 skill 只管「考之前要有幾多筆數據」）
- 出場管理規則（回測中點止盈止損）→ `lun-exit-management`；時段時間表 → `lun-kill-zones-timing`

## Prerequisites（前置）

1. **Corpus grounding（硬規則）**：只可以用本 skill、references/evidence.md 同 `analysis/` 內嘅材料回答。教科書式回測方法論（walk-forward、Monte Carlo、in-sample/out-of-sample、overfitting 理論、程式化回測框架）corpus 冇教過，一律唔准引入。引用「」內文字必須照錄，唔可以改寫。
2. **ASR 容錯（本 skill 特別重要）**：**回撤＝回測**（RdnJw-mhwlE 全片）、复盘/副盤/付盤＝復盤、执行翼＝執行力、希望值＝期望值、投放系统＝跳換系統、Tradzilla＝疑為 Tradezella、大樹法則＝大數法則、100比教育＝100筆交易、教育＝交易。全表見 `analysis/lun_trading_profile.md` §5。
3. **TradingView 工具口徑**：corpus 內回測工具引用只限 RdnJw-mhwlE 所示——回放功能、付費用戶（「我用的回放的工具是来自TradingView的」「不要省掉TradingView的这个月费」）。TradingView 操作教學片（NqixhiGBt9E）唔喺 corpus 內，任何回放介面操作細節唔准補完。
4. **核心詞彙速查表**（一行定義；全文原話見 [references/evidence.md](references/evidence.md)）：

| 術語 | 一行定義（交易倫口徑） | 主要出處 |
|---|---|---|
| 回測（ASR「回撤」） | 用歷史價格回放執行系統：唔洗血汗錢、鍛煉執行力、得到數據、測試系統 | RdnJw-mhwlE |
| 樣本量門檻 | (transcript)「你最少要回撤100单交易」「200单的交易」……「才会够扎实」（呢個係其中一層口徑；10/50–100/100–200 分層見 Step 4，唔好合併做單一數字） | RdnJw-mhwlE |
| 樣本污染 | (transcript)「但是你的樣本呢,被污染了。」——情緒單令 100 筆數據失效 | 54WCm_VBYfY |
| 系統信心數據 | 預期回報＋預期連虧/連賺單數＋Average Risk Rewards Ratio | rLP-MPvGmDE |
| 交易日記 | 記錄進出場理由＋情緒變化，定期回顧搵 Pattern | oiMlx5UlRLQ, mDpbsw81ftI |
| 100 筆交易挑戰 | 用固定 100 筆樣本測邊套系統適合自己，再調規則迭代 | PypFn7GaVfE |

## Workflow（分析流程）

按佢嘅時間軸行：學完策略 → 回測 → 數據 → 實戰記錄 → 覆盤 → 揀系統迭代。

**Step 1 — 定位：學完策略嘅第一步係回測，唔係實戰**

- 「要做的第一个步骤」係「去回撤」「去复盘先」（RdnJw-mhwlE）；未回測過就實戰＝表現差嘅其中一個原因：「如果你没有回撤过」「这也许就是你在教育里面表现不好的其中一个原因」（教育＝交易）。
- 反跳系統：「傻傻的去跟着导师们去不断的投放系统啊」「这样子不行啊」（投放＝跳換）；揀系統前「你需要一个一个去测试」（VjSB-VRyxWI）；學人系統都要「去做一些復盤。看它到底適不適合你」（pK6S7CEqMAk）。

**Step 2 — 設置回測環境（貼近實盤先有效）**

- 工具：TradingView 回放功能（付費）——「我是TradingView的付费用户」「不要省掉TradingView的这个月费」（RdnJw-mhwlE，工具成本當必要投資）。
- **只回測自己實際可以交易嘅時段**：「我会尽可能的跟着我平时交易的时间」，半夜機會唔做（「我不再11点交易了」，推測 不在），因為「我也要尽量以最真实的情况去得到我需要的数据」（RdnJw-mhwlE）。
- bar-by-bar 唔睇後市（B7rumsOw6_U 全片示範；此描述屬筆記歸納非原話引文），掛單/撤單/時效條件照真實規則行（示範規則本身 → `lun-price-action-toolkit`）。
- 心態一致性警告：「回撤的表現是比較容易的」「你的表現可能會差一點」，但「如果你可以把回撤的心態跟你真實表現一致性的話」「你一定得到一樣的成果」（B7rumsOw6_U）。

**Step 3 — 執行與記錄（截圖＋解釋）**

- 每筆截圖＋解釋出場原因：「我会截图」「我会解释」「为什么我会出场」（RdnJw-mhwlE）；邊行邊講 thought process——「就是我在执行这个系统的时候」「我有什么样的想法」「我的决策的那个过程是什么」。
- **跳過嘅交易都要記**（90% 人唔願做嘅習慣）：「我選的�每一個交易機會�我都會做截圖」「我沒有做�我會寫下為什麼不做」（xmHaONnNrCw，考 FTMO 期間口徑）。
- 異常要歸因驗證：懷疑新聞插針就記低返去查（「之后找回去」「是否有新闻」RdnJw-mhwlE）；新聞打止損照記錄接受——「这种情况会发生」。

**Step 4 — 樣本量門檻（情境分層，唔係單一數字）**

| 門檻 | 用途 | 出處 |
|---|---|---|
| (transcript)「你最少要回撤100单交易」「200单的交易」……「才会够扎实」 | 回測基準樣本 | RdnJw-mhwlE |
| 「做10单做100单复盘了之后」「你才去用比较小之星去实战测试」（小之星：推測 小資金） | 復盤→小資金實戰 | RjNBnZ59c4U |
| 「你最少最少需要50到100筆交易」數據先可以評估系統／考機構試 | 考 prop firm 前 | rE21_onS0uo |
| 100 筆為單位評估、倉位不變先維持到概率模型（倉位規則 → `lun-risk-management`） | 概率模型 | 54WCm_VBYfY |

- 大數法則基礎：(transcript)「短期之內輸贏的分布是隨機的,但是樣本一到,概率就接管了。」（54WCm_VBYfY）
- **樣本純度**：100 筆入面 70 筆情緒單＝(transcript)「但是你的樣本呢,被污染了。」——唔跟計劃嘅單會令數據失去評估價值（54WCm_VBYfY）。

**Step 5 — 數據產出：系統信心數據**

回測/記錄完要答到呢啲問題（「你知道你的連續虧損是多少單嗎?」rE21_onS0uo）：

- 最大連續虧損單數——「你可以连续亏损多少单」「这个策略的连续亏损是」「3单」「5单」「10单」（RdnJw-mhwlE）
- 交易頻率＋平均持倉時間——「你可以知道你的交易频率有多少啊」「还有你平均要持上多久」（RdnJw-mhwlE）；勝率、平均盈虧比、持倉時間（rE21_onS0uo）
- 預期回報、預期連虧/連賺、Average RRR——(transcript)「你一定要知道這個系統,帶給你的預期,你的預期,回報是多少。」「會有多少比連續虧損的出現。多少比連續賺錢的出現。」「或者是你的Average,Risk Rewards Ratio,是多少。」（rLP-MPvGmDE；比＝筆）
- **期望值校準**：「你的希望值也会被调整」「调整到一个合理的期望值」，之後「你也可以更踏实的去做你的交易」（RdnJw-mhwlE；希望值＝期望值）
- 用途＝防連虧跳系統：(transcript)「最多的连续亏损是11单」但「这个系统一整年的回报是300」（RdnJw-mhwlE，佢舊系統實測；300 推測為 300%）——冇呢個數據，連虧一出現「你会开始觉得这个系统已经不行了」。連虧時嘅情緒處理 → `lun-trading-psychology`。

**Step 6 — 實倉延伸：交易日記與覆盤節奏**

- 交易日記內容：「在交易日記裡你需要記錄進場出場的理由」「結果情緒上面的變化」（mDpbsw81ftI）；情緒分三階段記錄（入場前/持倉中/出場後），甚至記生理反應（54WCm_VBYfY）；回顧搵「你犯錯的時候」「你的情緒是怎樣的?」嘅 Pattern（oiMlx5UlRLQ）。「這個無聊的習慣可以讓你資產翻十倍」（mDpbsw81ftI）。
- 工具：(transcript)「我會放在我自己的Excel,我會寫下來。我也會用交易記錄軟件,比如說Tradzilla等等。」（MjPZizFnX-E；Tradzilla 疑為 Tradezella）
- 覆盤節奏：**每週**逐張截圖「一張一張的去做評價」（xmHaONnNrCw）；佢自己「每周五我都會直播分享我這一周做的每一筆交易」（HeQiNekCZng 交易解剖）；**每月**最少檢討一次（mDpbsw81ftI）；**季度**覆盤——「你有做你的第一季度的交易表現回顧嗎?」（MjPZizFnX-E），指標：勝率、平均盈虧比、R 分佈、資金曲線健康度（(transcript)「太過山車的資金曲線呢,是非常不健康的。」）。
- 覆盤產出：由最好 10 筆交易搵共同點變入場清單（HeQiNekCZng）；搵出「什麼樣的策略,什麼樣的形態,在什麼樣的市場會變得特別的好用」（eIeYQStY5rI）；用數據發現剔走低質單可提升勝率（MjPZizFnX-E）。

**Step 7 — 實戰路徑與刻意練習**

- 路徑：「所以模拟小资金大资金」「这个才是最踏实的」；「如果你连小资金都没有办法赚钱了」「你在大资金也是亏钱了」（s4on4yJCLII）。新系統起步風險（0.25% 等數字）→ `lun-risk-management`。
- 刻意練習（佢自身標準，屬 preference 唔係入場門檻）：「你沒有花最少一萬個小時,我覺得你可能還是沒有練成」「我每天花16個小時來做學習,來做研究,來做复盤,來做截圖」「就單單只是頭肩型,我就拿了超過一千張的截圖」（T2Nk46EqAh4）；練眼訓練——「練習找出100個,」「確定了動能在入場的交易機會。」（rdXofMdxNEQ）。

## 子節：多系統框架與 100 筆挑戰（吸收自 lun-multi-system-framework，單源 PypFn7GaVfE）

- **點解要多系統**：單一系統會隨市場節奏改變而失效——失效時先問「是不是市場的節奏改變了」，唔好淨係怪執行力/心態；「一招打天下」最後只能「放寬規則」，之後「你勝率開始變低了」。工具-環境匹配：「你用錯市場結構」「你用錯節奏了」「還是要虧錢啦」。
- **同一框架五套系統**：「而是同一個框架」（動能釋放）「一棵樹長出來的5根樹枝」——動能回流/動能壓縮破壞/SBL/加倉/流動性（各系統概觀與 Wyckoff 四階段 → `lun-price-action-toolkit`；流動性系統定位 → `lun-liquidity-analysis`）。
- **100 筆交易挑戰（本子節嘅可操作核心）**：(transcript)「就是100筆交易挑戰」——用五套系統做 100 筆，「你基本上就更加了解哪一個系統是最適合你的」，之後「或者是你可以調整規則」「再繼續你的另外100筆交易」，最終「從我的框架上面去建立適合你節奏的交易系統」。理論根基係上集提過嘅「就是大樹法則」（推測 大數法則）。
- **按性格配對**（歸納自同片）：持倉能力好→動能回流；平時乜都唔做、時機到想盡情加倉→加倉系統；鍾意單一時框搵大動能釋放前入場→流動性系統；想乾淨明確唔使盯盤→SBL。
- **切換能力靠樣本**：「那是因為我看了幾百上千筆交易」「做了幾百上千筆交易」先有「很強的辨制能力」（辨制＝辨識）。
- **保留內容 flag（必須聲明）**：transcript 顯示 100 筆挑戰係佢付費班（輪交易班 7.0/8.0）嘅功課框架——(transcript)「你加入 輪交易班�7.0的線上課之後呢�你要開始做一件事�就是100筆交易挑戰」；五套系統嘅完整入場/出場規則明言留喺課程（profile §7.1.2–3），公開內容只有樣本方法本身＋系統定位。唔准用教科書補完五套系統規則。

## Output（輸出）

本 skill 嘅輸出係**對話式分析指引**——唔生成檔案，唔跑程式回測，只提供按交易倫口徑嘅回測/驗證判斷。一份完整回覆應包含以下部分（每部分附 video id）：

1. **回測計劃**：工具（TradingView 回放）、策略來源（route 去對應策略 skill）、時段限制（跟用戶實際可交易時間）、樣本目標（100–200 單，或按用途分層）。
2. **記錄格式**：每筆截圖＋出場解釋、跳過交易記錄、異常（新聞插針）歸因欄。
3. **數據清單**：最大連虧、連賺、勝率、平均 RRR、預期回報、頻率、平均持倉時間——並講明用途係期望值校準＋防跳系統。
4. **覆盤節奏**：每週逐張/每月檢討/季度指標（勝率、平均盈虧比、R 分佈、資金曲線）。
5. **實戰路徑**：模擬→小資金→大資金嘅過關條件；考機構試前嘅 50–100 筆門檻（考試本身 → `lun-prop-firm-playbook`）。
6. **行動銜接**：倉位/風險 → `lun-risk-management`；連虧情緒 → `lun-trading-psychology`；策略規則 → 對應策略 skill。

## 邊界（呢個 skill 唔覆蓋）

| 唔覆蓋 | 交畀 |
|---|---|
| 連虧心理、無偏差執行嘅心理修煉、五特質 | `lun-trading-psychology` |
| 被測策略嘅具體規則（Pivot+PA、五套系統、Wyckoff、動能） | `lun-price-action-toolkit`（流動性系統定位 → `lun-liquidity-analysis`） |
| 每筆風險 %、等額風險、回測/新系統起步倉位 | `lun-risk-management` |
| prop firm 考試規則、考試場景執行 | `lun-prop-firm-playbook` |
| 回測中嘅止損止盈擺位規則 | `lun-exit-management`；入場序列 → `lun-ote-entry-model` |
| 時段時間表（「跟平時交易時間」嘅時段點揀） | `lun-kill-zones-timing` |
| 多時框分工、A+ 機會過濾 | `lun-multi-timeframe-analysis` |

## 侷限聲明

1. **手動方法**：佢嘅回測係 TradingView 回放式手動執行＋人手記錄；corpus 冇 walk-forward/Monte Carlo/程式化回測/overfitting 理論，本 skill 唔准補。TradingView 操作教學片（NqixhiGBt9E）唔喺 corpus，介面細節唔准引用。
2. **多系統框架係單源**：PypFn7GaVfE 一片；100 筆挑戰嘅完整執行流程綁定付費班，五套系統規則未公開——使用時降權並聲明保留內容。
3. **數字紀律**：「回报是300」推測為 300%（ASR 無單位）；MjPZizFnX-E 嘅「勝率只有在40%」有分母口徑問題（19/47≈40.4% vs 19/(19+20)≈48.7%，8 筆疑為保本單，profile §7.3.3）——引用實績必附口徑警告。
4. **實績未經對帳**：連虧 11 單/年回報 300、FTMO 期間 1:5 起跳、Q1 79.69R 均為自述；佢本人警告「我公開的交易表現呢,不代表你們也能做到一樣的交易表現」（MjPZizFnX-E）。
5. **一萬小時/16 小時/千張截圖係佢個人強度自述**（T2Nk46EqAh4 單源），屬 preference/勵志基準，唔係規則門檻。
6. **多口徑平行**：樣本量 10/50/100/200 屬唔同用途分層（回測扎實 vs 小資金前 vs 考試前），唔好合併做單一數字。

## Resources（證據來源）

- **[references/evidence.md](references/evidence.md)** — 回測方法證據全錄：回測目的、環境設置、截圖記錄法、樣本量分層、系統信心數據、交易日記與覆盤節奏、實戰路徑、多系統框架與 100 筆挑戰、實績警告（verbatim＋video id；transcript 直接覆核嘅引文標註「(transcript)」）。
- **正字對照表**：`analysis/lun_trading_profile.md` §5（**回撤＝回測**、复盘＝復盤、希望值＝期望值、大樹法則＝大數法則等，讀任何引文/逐字稿必查）；矛盾處理依據 §7.3；實績警告依據 §7.4。
- **Contributing videos（16＋1，per profile §6.8）**：RdnJw-mhwlE（回測主教材）；PypFn7GaVfE（多系統子節）；B7rumsOw6_U（bar-by-bar 示範＋心態一致）、rLP-MPvGmDE（系統信心數據）、54WCm_VBYfY（大樣本/樣本污染）、MjPZizFnX-E（Excel/Tradezella＋季度覆盤）、rE21_onS0uo（50–100 筆門檻）、xmHaONnNrCw（截圖＋每週覆盤）、HeQiNekCZng（交易解剖＋最好 10 筆）、oiMlx5UlRLQ／eIeYQStY5rI（交易日記）、T2Nk46EqAh4（一萬小時）、rdXofMdxNEQ（搵 100 個練習）、RjNBnZ59c4U（10/100 單→小資金）、s4on4yJCLII（模擬→小→大）、VjSB-VRyxWI（逐一測試）、pK6S7CEqMAk（用前先復盤）；補充：mDpbsw81ftI（交易日記翻十倍）。
- **逐字稿**：`data/transcripts/<video_id>.txt`（引用必須 verbatim；本 skill 已覆核 RdnJw-mhwlE 100/200 單、連虧 11/300 段落，PypFn7GaVfE 100 筆挑戰＋付費班框架段落，54WCm_VBYfY 樣本污染句，MjPZizFnX-E Excel/資金曲線句，rLP-MPvGmDE 系統信心數據段落）。
- **路徑註記**：上面 `analysis/…` 同 `data/…` 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 `.claude/skills/` 嘅上兩層目錄）；如果本 skill 被安裝到全域位置，該啲證據仍然留喺該項目入面，skill 本地只保證 references/evidence.md 可用。
