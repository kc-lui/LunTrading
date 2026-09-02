# 研究文檔：YouTube 頻道 → Skills-first Agent 蒸餾方法論

本文檔記錄 LunTrading 專案嘅方法論決策、量化結果同可重用經驗，供下一個同類專案（頻道蒸餾）參考。前例：Drmarkyang（單一 agent、知識 inline）；本專案係第二代方法（skills-first、逐一生成、自動審查 gate）。

## 1. 架構決策：點解拆做 skills

| 維度 | Drmarkyang（inline agent） | LunTrading（skills-first） |
|---|---|---|
| 知識載體 | 單一 agent md（92 行，全 inline） | 11 個 skills（SKILL.md ~150-200 行 + evidence.md）＋精簡 agent（70 行） |
| Context 成本 | agent 一載入就全量佔用 | 按需載入（progressive disclosure），routing 表先行 |
| 可審查性 | 整體一次過 | 逐 skill 獨立審查、獨立分數、獨立 commit |
| 可重用性 | 綁定單一 agent | skills 可被任何 agent/session 單獨調用 |
| DRY | 唔適用 | boundary ledger 契約，11 個 skill 零重複定義 |

## 2. 管線量化結果

- 66 條影片 → 人工分群排除 9 條低訊號 → **57 條核心（15.5h）**
- 語言探測（batch 前必做）：同一短片以 zh/yue 各轉一次人工比對 → zh 勝（1920 vs 1731 chars，錯字更少）
- ASR：mlx-whisper large-v3-turbo，M1 16GB ~5x realtime，總轉錄 ~3h（背景跑，中斷三次全部 resume 成功）
- 完整性：57/57 ok，0 missing / 0 empty / 0 suspicious，335,622 chars
- 筆記：15 agents 兩波並行（batch 3-4 片/agent），~1.5h；引文驗證 `check_quotes.py` 全綠
- Skills：11 個，嚴格順序生成；6 個 first-pass 過 gate，5 個一輪修訂過；全部 ≥90

## 3. 反幻覺體系（本專案最重要嘅工程）

四層防線，每層都實際攔到嘢：

1. **筆記模板規則**（未提及唔腦補、引文 verbatim）——寫入 NOTE_TEMPLATE.md，agents 自發加咗程式化驗證。
2. **確定性驗證** `scripts/check_quotes.py`——攔到 35 個非 verbatim 引文（多為 writer 註解誤入「」、分段符錯位），全部修復。
3. **抽樣稽核（判斷層）**——攔到 quote-checker 攔唔到嘅問題：僅預告當已教、覆蓋缺口（例外規則/量化等候時間系統性漏抄）、tag 唔一致。
4. **獨立 LLM 審查（逐 skill）**——攔到最隱蔽嘅：CTA 引文張冠李戴（sponsored 判定嘅 load-bearing 證據錯 source）、H-score 晉級規則同 transcript 相反、「…」省略號靜默刪字、核心發現被自己張表推翻（風險% 第三口徑）。

經驗：**author 同 reviewer 必須係唔同 agent 實例**；reviewer 用到第 6 個 skill 後 context 過大，輪換新 reviewer 反而提高咗嚴格度（新 reviewer 即刻抓到舊 reviewer 冇抓到嘅 HIGH）。

## 4. 審查 gate 校準

dual-axis-skill-reviewer 對 knowledge_only skills 嘅 auto axis 有結構性封頂（exec 14/25、test 12/20 → auto ceiling ≈ 80-82）。0.5/0.5 權重下 90 分閘門數學上不可達；依工具自身文檔嘅權重旋鈕改為 **0.35/0.65**，閘門維持 90（auto 80 時要求 LLM ≥ 95.4——仍然嚴格：三個 skill 首輪唔過）。

結構契約（過 auto axis 嘅充分條件）：`references/*.md` 存在＋無 `scripts/`（→ knowledge_only 判定）；五個規範 H2（When to Use / Prerequisites / Workflow / Output / Resources，容許中文後綴）；無絕對路徑/username。

## 5. 逐步固化嘅內容公約（審查迭代出嚟，寫入後續 author prompt）

1. 「」只放 corpus verbatim 文字；編輯標籤用粗體；「…」省略號禁止
2. 每個引文 inline 附 video id；transcript 直接覆核者標 "(transcript)"
3. 矛盾口徑平行分層唔裁決；permission 同 preference 分開呈現
4. 單源元素逐個標「單源低信心」；推論標「推測」
5. 贊助內容結構性隔離（【推廣合作】banner + CTA 引文做證據）＋時效性 caveat
6. 路徑用自我定位錨（「本 skill 所在 .claude/skills/ 嘅上兩層」）＋ ../../../ 雙形式

## 6. 團隊協作模式（實際 vs 設計）

按 `docs/team_design.md` 執行，實際偏差：
- agent-organizer 只做設計文檔（its tools 冇 Task/Bash），實際 orchestration 由 main session 用 Agent tool 做——同設計一致
- Note QA 由「每波 15% 抽查」實做為「自動 quote-checker 全量 + 判斷層抽查 5+7 篇」——上位替代
- Session limit 三次中斷（notes wave 2、skill 3 author、skill 7 reviewer、skill 11 author）——SendMessage resume 全部無損恢復；nohup + Monitor 令 ASR 管線唔受 session 中斷影響
- Reviewer 換人一次（context 膨脹）——見 §3

## 7. 已知未解問題

- 筆記層系統性覆蓋缺口（例外規則、量化等候時間、輸單示範）只喺 7 篇抽查樣本確認；其餘 50 篇未逐一補抄。skills 經 transcript 直接覆核已部分補救，但唔完整。
- excluded 9 條片（傳記/工具教學）或含 persona 素材，本輪未用。
- Golden run 只覆蓋 4 條代表性問題；11 skills 全路由覆蓋測試未做。
- 頻道持續更新；新影片需重跑管線增量處理（腳本已 resumable，只需重跑 fetch_meta → build_playlist_json 加分群 → run_pipeline）。
