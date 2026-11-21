# セキュリティトレンド Top 10 ニュース
**配信日：2026年11月22日（日）**

> ⚠️ この記事はClaude AIとxAI Grok API（話題性分析）を組み合わせて収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **自律型AIエージェント攻撃** | 中国系アクターがAIエージェントでMONAI Labelのゼロデイを約11分で発見・悪用。人間の介在なしに侵入まで完結する攻撃が実証された。 |
| 2 | **FBI NCIC侵害** | 全米の警察が使う犯罪情報データベースへの侵害疑い。9月の求人ポータル侵害に続き、FBIのシステムが再び標的に。 |
| 3 | **クラウドID基盤のAPI欠陥** | Microsoft Entra Connect HealthのAPI脆弱性が約4か月放置され、テナントのメタデータが読み出された。ID管理基盤の周辺サービスがリスクに。 |
| 4 | **Web/ベンダー経由サプライチェーン** | Optimizely経由で178組織のサイトにマルウェア注入、金融大手のベンダー侵害など、自社外の経路からの被害が続いている。 |
| 5 | **米サイバー政策の人事刷新** | 国家サイバー長官Cairncross氏が退任し、次期上院国土安全保障委員長はAI脅威を優先課題に掲げた。米国のサイバー政策の舵取りが変わりつつある。 |

---

## 🔴 Cyber Security

### 1. FBIの全米犯罪情報センター（NCIC）データベースに侵害の疑い
**2026年11月20〜21日**
CNNの報道によると、令状・犯罪歴・身元調査の情報を全米の法執行機関が共有するFBIのNCICが侵害された疑いがあります。9月の求人ポータル侵害に続く2度目の事案で、漏えいの範囲やデータの種類はまだ確認されておらず、調査が続いています。警察の日常業務を支える基盤だけに、政策面への波及も大きいとみられます。

🔗 [FBI's criminal information database hacked, CNN reports (Reuters)](https://www.reuters.com/world/us/fbis-criminal-information-database-hacked-cnn-reports-2026-11-21/)
🔗 [FBI hacked again, target crime database (CNN)](https://www.cnn.com/2026/11/20/politics/fbi-hacked-again-target-crime-database)

---

### 2. Microsoft Entra Connect HealthのAPI脆弱性が悪用され、テナント情報が漏えい
**2026年11月21日**
7月23日に入り込んだAPIの欠陥が悪用され、11月19日にサーバー側で修正されるまで、管理者・技術担当のメールアドレス、テナントID、ライセンス階層、同期状況などが読み出せる状態でした。読み取り専用で、パスワード・トークンの漏えいや設定変更は確認されていません。影響を受けたテナント数は公表されていません。

🔗 [Microsoft Entra Connect Health flaw exploited to steal tenant data (BleepingComputer)](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)

---

### 3. F5 BIG-IPにCVSS 9.8の重大脆弱性が複数、緊急ホットフィックスを公開
**2026年11月18〜20日**
F5はBIG-IP APMとiRulesのスタックバッファオーバーフロー脆弱性（認証なしでRCE・DoSが可能、CVSS 9.8）に対する緊急ホットフィックスを公開しました。悪用は現時点で確認されていませんが、回避策がなく、インターネットに露出した機器が多いため、早急な適用が推奨されます。

🔗 [F5 scrambles to fix more critical BIG-IP security flaws (Network World)](https://www.networkworld.com/article/4251676/f5-scrambles-to-fix-more-critical-big-ip-security-flaws.html)

---

## 🟠 AI Risk

### 4. 中国系攻撃者がAIエージェントでMONAI Labelのゼロデイを自律的に発見・悪用 — Amazonが報告
**2026年11月20〜21日**
Amazon Threat Intelligenceによると、中国系の脅威アクターがオープンソースのCairnフレームワーク上のAIエージェントを使い、医療画像ソフトMONAI Labelのパストラバーサル脆弱性（CVE-2026-133968、CVSS 9.8）を約11分で発見・悪用し、東アジアの大学サーバーでrootシェルを取得しました。認証が既定で無効だったことも被害を広げました。人間の介在なしにゼロデイ発見から侵入まで完結した事例として大きく注目されています。

🔗 [Amazon: China-linked hackers' AI agents exploited medical software zero-day (SecurityWeek)](https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/)
🔗 [China attackers deployed AI agents that autonomously found and exploited a 0-day (The Register)](https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382)
🔗 [Amazon uncovers AI agent campaign (The Hacker News)](https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html)

---

## 🟡 Data & Privacy

### 5. Optimizely経由のサプライチェーン攻撃、178組織のサイトで訪問者データが危険に
**2026年11月17日〜**
Optimizely Experimentationの登録フローの欠陥が悪用され、BBC・CNN・Salesforce・HSBC・Ledger・Zoomなど178組織のサイトに悪性コードが注入されました。カードスキミング、Cookieやスクリーンショットの窃取、暗号資産アドレスのすり替え、iOS向けエクスプロイトキットの配信が確認され、影響を受けた訪問は数百万〜数千万件と推定されています。

🔗 [Attackers used Optimizely to A/B test malware on top websites (Krebs on Security)](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/)
🔗 [Optimizely supply chain attack delivers malware to CNN, Fox News, BBC, Salesforce sites (BleepingComputer)](https://bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites)

---

### 6. JPMorgan・Visa・Mastercard、第三者ベンダー経由で顧客マーケティングデータが流出
**2026年11月19日**
恐喝グループn0nが第三者プロバイダーへの侵害を主張し、JPMorgan Reserveの顧客約1万6,000件のメールアドレスなどを公開しました。Visa・Mastercardも同様の被害を確認しています。各社の自社システムやカード番号への影響はないとしていますが、金融業界の第三者リスク管理が改めて問われています。

🔗 [JPMorgan says third-party vendors targeted in cyberattack (Reuters)](https://www.reuters.com/legal/government/jpmorgan-says-third-party-vendors-targeted-cyberattack-2026-11-19/)
🔗 [JPMorgan Chase cyberattack (The Verge)](https://www.theverge.com/tech/1037695/jpmorgan-chase-cyberattack)

---

## 🟢 Security Governance

### 7. ホワイトハウスの国家サイバー長官Sean Cairncross氏が退任、DoD CIOのDavies氏が代行
**2026年11月19〜20日**
政府システムの障害が続くなか、Cairncross国家サイバー長官が職を離れました（事実上の解任との報道もあります）。国防総省CIOのKirsten Davies氏が代行を務めます。トランプ政権のサイバー部門の人事刷新により、国家サイバー戦略の執行が停滞しないかが議論されています。

🔗 [National cyber director replaced: Sean Cairncross (CNN)](https://www.cnn.com/2026/11/19/politics/national-cyber-director-replaced-sean-cairncross)
🔗 [Sean Cairncross out as cyber director (Politico)](https://www.politico.com/news/2026/11/19/sean-cairncross-cyber-director-out-01177151)

---

### 8. 次期上院国土安全保障委員長のHassan議員、AIによる重要インフラへの脅威を優先課題に
**2026年11月21日**
次期委員長に就くMaggie Hassan上院議員が、AIが重要インフラにもたらす脅威を早期の優先課題に挙げました。CISA長官の指名公聴会とも連動する動きで、エージェント型攻撃の急増を受けて、AIセキュリティの立法・監督が加速する可能性があります。

🔗 [Inside Cybersecurity](https://insidecybersecurity.com/)
🔗 [The Record by Recorded Future](https://therecord.media/)

---

## 🟣 Crypto Currency

### 9. Binance 63億ドル流出事件、犯行グループが約5.94億ドル相当のETHを移動
**2026年11月19〜20日**
10月29日のBinanceホットウォレット侵害（北朝鮮系TraderTraitorによるとされる史上最大の流出）に関連するアドレスから、約5.94億ドル相当のETHが新しいウォレットへ移されました。THORChainなどを使ったクロスチェーンでの資金洗浄が続いており、FBIが警告したアドレスも含まれています。

🔗 [Binance hackers move $594 million in Ether via THORChain (CoinLaw)](https://coinlaw.io/binance-hackers-594-million-ether-thorchain/)
🔗 [RUNE token surges amid Binance hack laundering (Cointelegraph)](https://cointelegraph.com/news/rune-token-surges-binance-hack)

---

### 10. Ledger端末への通信インプラント問題、11月19日の更新で正規リセラー経由の被害地域が拡大
**2026年11月19〜20日（10月からの続報）**
10月に発覚した、リセラー経由のLedger端末にLTEモジュールが仕込まれ、セットアップ時に24語のシードフレーズが外部送信されていた問題の続報です。11月19日のLedgerの更新では、東南アジアに加えベルリンやドバイの販売経路でも改ざん端末が確認されました。被害額は報道によって約168万ドル〜最大8,600万ドル超と幅があり、「Genuine Check」でも検出できないため、購入経路の確認と、疑わしい端末で作ったシードの破棄が推奨されます。

🔗 [Ledger finds LTE implant that stole recovery phrases in suspected $86M drain (Decrypt)](https://decrypt.co/380826/ledger-finds-lte-implant-that-stole-recovery-phrases-in-suspected-86m-drain)
🔗 [Ledger asks sellers across Asia to halt sales after supply chain attack (BleepingComputer)](https://www.bleepingcomputer.com/news/security/ledger-asks-sellers-across-asia-to-halt-sales-after-supply-chain-attack/amp/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | FBI NCIC、Entra Connect Health、F5 BIG-IP |
| AI Risk | 🟠 | 自律型AIエージェント攻撃、MONAI Label、Cairn |
| Data & Privacy | 🟡🟡 | Optimizely、第三者ベンダー、n0n |
| Security Governance | 🟢🟢 | Cairncross退任、Hassan議員、AI安全 |
| Crypto Currency | 🟣🟣 | Binance資金洗浄、THORChain、Ledgerインプラント |

---

*次回配信予定：2026年11月23日（月） | 収集ソース：Reuters、CNN、BleepingComputer、SecurityWeek、The Register、The Hacker News、Network World、Krebs on Security、Politico、The Verge、CoinLaw、Cointelegraph、Decrypt、xAI Grok API*
