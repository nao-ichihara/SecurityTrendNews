# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月30日（木）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ShinyHunters** | EY、RingCentral、Brinks Homeなど大手企業を次々とダークウェブ流出サイトに掲載する恐喝型ハッカー集団。7月下旬に活動が急拡大している。 |
| 2 | **ランサムウェアによるデータ窃取** | Coca-Cola傘下Fairlifeの事例のように、生産停止だけでなく機密データの窃取・公開を伴う二重恐喝が定着している。 |
| 3 | **AgentForger（AIエージェント乗っ取り）** | ChatGPTのWorkspace Agent Builderを悪用し、1本のフィッシングリンクだけで組織内に不正なAIエージェントを構築・常駐させる新種の攻撃手法。 |
| 4 | **サードパーティ・ベンダーリスク** | Craneware社の侵害のように、1社の医療系ベンダーが侵害されるだけで数千の病院・薬局に影響が波及する構造的リスクが顕在化。 |
| 5 | **DeFiブリッジ・鍵管理の脆弱性** | 2026年の暗号資産被害はスマートコントラクトのバグよりも秘密鍵・署名者・ガバナンスの不備に起因するケースが主流に。 |

---

## 🔴 Cyber Security

### 1. Coca-Cola、Fairlifeへのランサムウェア攻撃でデータ窃取を確認
**2026年7月28日**
Coca-Cola傘下の乳製品ブランドFairlifeは、7月16日に発生した侵害で米国内の生産が一時停止した後、Anubisランサムウェアグループが機密データ1テラバイトを窃取・暗号化したと主張していることを確認した。米生産拠点の大部分は稼働を再開している。

🔗 [Coca-Cola confirms hackers stole data in Fairlife ransomware attack](https://www.helpnetsecurity.com/2026/07/28/coca-cola-fairlife-dairy-subsidiary-ransomware-attack/)

---

### 2. 医療ベンダーCraneware、数千の病院・薬局に影響する情報漏えい
**2026年7月20日**
英国拠点の医療請求ソフト大手Cranewareが7月20日にサイバー攻撃を確認。同社は約2,000の米国病院と約1万の診療所・薬局に請求システムを提供しており、従業員データおよび顧客・パートナーの一部データが窃取された。第三者ベンダー経由の攻撃リスクを改めて浮き彫りにした。

🔗 [Hackers stole 'significant' amount of data from tech firm relied on by thousands of US hospitals](https://techcrunch.com/2026/07/20/hackers-stole-significant-amount-of-data-from-tech-firm-relied-on-by-thousands-of-us-hospitals-and-pharmacies/)

---

### 3. ShinyHunters、EY・RingCentral・Brinks Homeを流出サイトに追加
**2026年7月27日〜28日**
恐喝型ハッカー集団ShinyHuntersが、大手会計事務所EY、通信大手RingCentral、スマートホームセキュリティ企業Brinks Homeを相次いでダークウェブ流出サイトに掲載。Brinks Homeには「最終警告」として公開期限が設定されており、7月下旬の主要な脅威トレンドとなっている。

🔗 [ShinyHunters Adds EY, RingCentral, and Brinks Home to Data Leak Site](https://breachnews.com/breaches/shinyhunters-adds-ey-ringcentral-and-brinks-home-to-data-leak-site/)

---

### 4. ハッカーがルーマニアの土地登記データベースを全消去
**2026年7月21日**
ルーマニアの不動産登記機関ANCPIが、正規の認証情報を用いて侵入したハッカーにより登記データベース全体を消去され、不動産取引が完全に停止した。恐喝要求が拒否されたことへの報復とみられ、オフラインバックアップからの復旧が進められている。付加価値税の税率変更を控えた時期と重なり影響が拡大した。

🔗 [Hacker wipes European country's entire land registry database](https://cybernews.com/security/hacker-deletes-romanian-land-registry-database/)

---

## 🟠 AI Risk

### 5. ChatGPTの「AgentForger」脆弱性、1クリックで不正AIエージェントを組織内に展開
**2026年7月23日〜24日**
セキュリティ企業Zenity Labsが、OpenAIのChatGPT Workspace Agent Builderに存在するクロスサイト・リクエストフォージェリ型の脆弱性「AgentForger」を公表。ログイン済みユーザーが悪意あるリンクをクリックするだけで、既存の連携先すべてを引き継いだ自律型AIエージェントが自動生成され、書き込み承認設定も「常に確認」から「確認不要」に変更されてしまう。生成されたエージェントは5分おきに攻撃者の指示を受信するC2チャネルとして悪用され得た。OpenAIは既に修正済み。

🔗 [OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider](https://www.securityweek.com/openai-fixes-chatgpt-agent-flaw-that-could-let-attackers-forge-an-ai-insider/)

---

### 6. AIエージェントを狙う悪性プロンプトが急増、企業の未承認AI利用も課題に
**2026年7月**
Check Pointの「AI Security Report 2026」によると、悪意ある長文プロンプトの検出数は3月から5月の間に約5倍に増加し、高リスクなプロンプトの割合も2%から4%に倍増した。企業は平均月10種類のAIアプリケーションを利用しているが、その多くが正式な承認を経ておらず、シャドーAIによるデータ漏えいリスクが拡大している。

🔗 [AI Security Report 2026 - Check Point Research](https://research.checkpoint.com/2026/ai-security-report-2026/)

---

## 🟡 Data & Privacy

### 7. 米国州レベルのプライバシー規制、2026年に大幅拡大・罰則強化
**2026年**
インディアナ、ケンタッキー、ネブラスカ、ロードアイランドの4州で新たな包括的プライバシー法が施行される一方、カリフォルニア・コロラド・コネチカット・オレゴン・ユタは既存法を改正。カリフォルニアはCPRA違反の罰金を1件あたり7,988ドルに引き上げ、30日間の是正猶予も撤廃した。Global Privacy Control信号への対応を義務付ける州も8州に拡大している。

🔗 [New year, new rules: US state privacy requirements coming online as 2026 begins](https://iapp.org/news/a/new-year-new-rules-us-state-privacy-requirements-coming-online-as-2026-begins)

---

## 🟢 Security Governance

### 8. SEC、2026年の検査重点項目からサイバーとAIが暗号資産を上回る
**2026年（第4四半期に向けた方針）**
米証券取引委員会（SEC）が公表した2026年の検査重点項目では、サイバーセキュリティとAIガバナンスへの関心が暗号資産を初めて上回り、単独の暗号資産項目は姿を消した。検査ではガバナンス体制、データ損失防止、アクセス管理、ランサムウェア対応、AI主導の侵入への備えなどが重点的に評価される見通し。

🔗 [SEC's 2026 exam priorities: data privacy takes center stage as crypto is dropped](https://www.governance-intelligence.com/regulatory-compliance/secs-2026-exam-priorities-data-privacy-takes-center-stage-crypto-dropped)

---

## 🟣 Crypto Currency

### 9. 2026年の暗号資産被害額が約9.72億ドルに、鍵管理・ガバナンスの不備が主因
**2026年7月29日**
CoinDeskの分析によると、2026年の暗号資産盗難被害は累計で約9.72億ドルに達しており、その多くはスマートコントラクトのバグではなく秘密鍵・署名者・ガバナンスプロセスの不備が原因。直近1週間だけでもAFX Trade（約2,415万ドル）、Wanchain、Verusなどブリッジ関連の攻撃が相次ぎ、週間被害額は4,700万ドルを超えた。

🔗 [Crypto Long & Short: What this year's $972M crypto hacks actually tell us about security](https://www.coindesk.com/coindesk-indices/2026/07/29/crypto-long-and-short-what-this-year-s-usd972-million-crypto-hacks-actually-tell-us-about-security)

---

### 10. 暗号資産取引所BitMart、9年間の営業を終え撤退へ
**2026年7月**
暗号資産取引所BitMartが、新規登録・入金・注文を停止し、8月26日をもって現物・デリバティブ取引を全面終了すると発表。9年間続いた事業からの撤退となり、業界再編と規制強化の流れの中での動きとして注目されている。

🔗 [Crypto Market Update: BitMart Announces Exchange Shutdown](https://investingnews.com/cryptocurrency-market-recap/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | ランサムウェア、ShinyHunters、サードパーティリスク、データ破壊攻撃 |
| AI Risk | 🟠🟠🟠 | AIエージェント乗っ取り、AgentForger、シャドーAI |
| Data & Privacy | 🟡🟡 | 州プライバシー法、CPRA罰則強化 |
| Security Governance | 🟢🟢 | SEC検査重点項目、AIガバナンス格差 |
| Crypto Currency | 🟣🟣🟣 | DeFiブリッジ攻撃、鍵管理、取引所撤退 |

---

*次回配信予定：2026年7月31日（金） | 収集ソース：Help Net Security, TechCrunch, BreachNews, Cybernews, SecurityWeek, Check Point Research, IAPP, Governance Intelligence, CoinDesk, Investing News*
