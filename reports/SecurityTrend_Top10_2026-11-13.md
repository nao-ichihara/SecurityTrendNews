# セキュリティトレンド Top 10 ニュース
**配信日：2026年11月13日（金）**

> ⚠️ この記事はClaude AIとxAI Grok API（話題性分析）を組み合わせて収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **エージェント型AI攻撃ツール（ARTEX / AntiFox）** | オープンソースのAIペンテスト基盤が国家系・犯罪グループに転用され、14カ国200超の組織で数分〜数時間の特権奪取を実現。「AIが攻撃を回す」段階が実戦で常態化しつつある。 |
| 2 | **PHP2Shell** | Check Pointゲートウェイで権限昇格バグと連鎖悪用され、root奪取→VMware ESXiへのワイパー展開へ。境界装置の侵害が破壊型攻撃の入口になる典型例。 |
| 3 | **AIサプライチェーン侵害（Fireworks AI）** | AI推論基盤の侵害がNotionのチャット記録、Uberドライバーの免許情報へと波及。AIベンダーが新たな「第三者リスク」の焦点に。 |
| 4 | **KEV / BOD 26-04** | CISAがCheck Point・UnrealIRCdの脆弱性を追加し、連邦機関に短期のパッチ・フォレンジックを要求。週内に複数回のKEV追加が続いている。 |
| 5 | **ハードウェアインプラント** | Trezor Safe 5の一部個体に、リカバリフレーズを携帯網経由で送る物理改造を確認。正規品でも流通経路が攻撃面になる。 |

---

## 🔴 Cyber Security

### 1. Check PointゲートウェイがPHP2Shell連鎖で乗っ取られ、VMware ESXiにワイパー展開
**2026年11月13日**
Check Point Security GatewayでPHP2Shellと新たなGaia OS権限昇格バグ（CVE-2026-123039）が連鎖悪用され、root権限取得後にバックドアを設置、さらに内部のVMware ESXiホストへデータワイパーを展開する攻撃が確認された。10月末にイスラエルで始まり複数国へ拡大、数十社の被害が報告されている。CISAは同日、当該脆弱性をKEVに追加した。

🔗 [Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper（BleepingComputer）](https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/)
🔗 [Chinese hackers used VMware ESX zero-day; PHP2Shell and Fragnesia chained to root firewalls（Help Net Security）](https://www.helpnetsecurity.com/?p=389707)

---

### 2. Microsoft 365で世界規模の大規模障害、Outlook・Teams・Copilotが停止
**2026年11月12〜13日**
11月12日からOutlook、Teams、SharePoint、Copilotなどが世界的に利用困難となり、復旧は13日まで長引いた。Microsoftはネットワーク変更が原因でサイバー攻撃ではないと説明しているが、政府・警察・医療機関の業務にも影響。障害に便乗した「復旧案内」型フィッシングの増加に注意が必要。

🔗 [Microsoft struggles to restore email and other services in a global outage（SecurityWeek）](https://www.securityweek.com/microsoft-struggles-to-restore-email-and-other-services-in-a-global-outage/)
🔗 [Massive Microsoft 365 outage disrupts Outlook, Teams, Copilot worldwide（BleepingComputer）](https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-disrupts-outlook-teams-copilot-worldwide/)

---

### 3. 「セキュリティ監査」を装う悪性GitHub Actionsワークフロー、数万リポジトリに混入
**2026年11月13日**
Socketの調査によると、2つのアカウントが「security audit」を装ったワークフローを大量のリポジトリへプッシュし、Actionsシークレットや Git履歴内の認証情報を収集していた。前日報じられたGitHubアカウント悪用型の窃取キャンペーンに続き、CI/CDを狙うサプライチェーン攻撃が相次いでいる。

🔗 [Supply chain attack hits thousands of repositories（Infosecurity Magazine）](https://www.infosecurity-magazine.com/news/supply-chain-attack-thousands/)

---

## 🟠 AI Risk

### 4. AIペンテスト基盤「ARTEX」とフォーク「AntiFox」が実攻撃で拡散、200超の組織が標的に
**2026年11月10〜13日**
オープンソースのエージェント型AIペンテストフレームワークARTEXが、中国系とされるStorm-0940などに悪用され、14カ国200以上の組織を標的化。ConnectWise経由のサプライチェーン侵入やAWSシークレット窃取を、数分〜数時間で特権アクセスまで自動化していた。SophosやSentinelOneが相次いで分析を公表した。

🔗 [ARTEX AI pen test tool becomes hackers' weapon（Dark Reading）](https://www.darkreading.com/cyberattacks-data-breaches/artex-ai-pen-test-tool-hackers-weapon)
🔗 [ARTEX unmasked: the rise of AI-powered ARTEX in cybercrime & espionage（SentinelOne）](https://www.sentinelone.com/blog/artex-unmasked-the-rise-of-ai-powered-artex-in-cybercrime-espionage/)
🔗 [Attackers are using agentic AI offensive tools to automate intrusions（Security Boulevard）](https://securityboulevard.com/2026/11/attackers-are-using-agentic-ai-offensive-tools-to-automate-intrusions/)

---

### 5. OpenAIが「Daybreak」でAIセキュリティ製品に参入、攻撃能力と防御販売の利益相反が議論に
**2026年11月13日**
OpenAIがGPT-6 Cyberモデルを用いた脆弱性テスト「Daybreak Red Team」と自動パッチ「Defense Factory」を発表。一方で、フロンティアモデルの攻撃能力を警告する同社自身が防御製品を販売する構図に、調達・ガバナンス面での利益相反を指摘する声が上がっている。前日のフロンティアAI開発凍結訴訟とあわせ、AIベンダーの責任論が強まっている。

🔗 [OpenAI's AI security products create a vendor conflict of interest problem（AI Governance）](https://aigovernance.com/news/openais-ai-security-products-create-a-vendor-conflict-of-interest-problem)

---

## 🟡 Data & Privacy

### 6. ニトリ、最大3,762万件の顧客情報が流出した可能性を公表
**2026年11月13日**
家具大手ニトリが、不正アクセスにより最大3,762万件の顧客記録が窃取された可能性があると発表した。ログ上は10月中旬〜下旬からアクセスがあり、11月6日に遮断。パスワードやクレジットカード情報は含まれていないとしている。国内小売として最大級の規模で、フィッシングへの二次悪用に警戒が必要。

🔗 [Japanese furniture giant Nitori says hackers stole 37.6M customer records（BleepingComputer）](https://www.bleepingcomputer.com/news/security/japanese-furniture-giant-nitori-says-hackers-stole-376m-customer-records/)
🔗 [Top 10 Breaches of the Week（Security Boulevard）](https://securityboulevard.com/2026/11/top-10-breaches-of-the-week-16/)

---

### 7. Fireworks AI侵害がUberにも波及、ドライバー数千人分の運転免許情報が流出
**2026年11月13日**
Uberは州司法長官への通知で、10月9日に第三者ベンダーから侵入と認証情報窃取の連絡を受けたと説明。TechCrunchはこのベンダーをAI推論基盤のFireworks AIと特定した。マサチューセッツ2,567人、サウスカロライナ3,430人、ロードアイランド1,873人の免許情報が影響を受け、総数は未公表。前日判明したNotion顧客のAIチャット記録流出に続く被害で、AIベンダー経由の第三者リスクが顕在化している。

🔗 [Uber confirms hackers stole thousands of drivers' license information in data breach（TechCrunch）](https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/)
🔗 [Cyberattack on Fireworks AI allowed hackers to access Notion customers' chat transcripts（TechCrunch）](https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/)

---

### 8. フィリピンで政府機関の情報漏えいが連鎖、NPCが少なくとも10機関の侵害を確認
**2026年11月12日**
フィリピン国家プライバシー委員会（NPC）が、少なくとも10の政府機関から侵害通知を受けたと確認した。調査団体の集計では23機関で漏えいが主張され、労働雇用省（DOLE）1,920万件、物流大手LBC Expressの配送ログ2,090万件などのデータセットが出回っているとされる（件数の多くは攻撃者側の主張）。

🔗 [NPC confirms data breach in 10 government agencies（Philstar）](https://www.philstar.com/headlines/2026/11/12/2569565/npc-confirms-data-breach-10-government-agencies/amp/)

---

## 🟢 Security Governance

### 9. CISAがCheck Point・UnrealIRCdの脆弱性をKEVに追加、CIRCIA最終規則は依然審査中
**2026年11月13日**
CISAはCheck Point（CVE-2026-123039）とUnrealIRCd（CVE-2026-114713）の脆弱性をKEVカタログに追加し、BOD 26-04に基づき連邦民間機関に11月16日までのパッチ適用とフォレンジック調査を求めた。週初のOpenSSH「SSHole」等に続く短期期限の追加が続く。一方、重要インフラ向け72時間報告義務を定めるCIRCIA最終規則は10月からOMB審査で止まったままで、CISAは任意報告フォームの改修で当座をしのいでいる。

🔗 [CISA adds two known exploited vulnerabilities to catalog（CISA）](https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog)
🔗 [CISA updates cyber reporting form as broader incident mandate awaits approval（Nextgov/FCW）](https://www.nextgov.com/cybersecurity/2026/11/cisa-updates-cyber-reporting-form-broader-incident-mandate-awaits-approval/417130/)

---

## 🟣 Crypto Currency

### 10. Trezor、Safe 5の3台で暗号資産窃取用ハードウェアインプラントを確認、修正ファームを配布（続報）
**2026年11月13日**
Trezorは東南アジアの販売代理店CryptoBilis経由で流通したSafe 5の3台に、画面に表示されたリカバリフレーズを携帯電話網経由で外部送信する悪意ある改造を確認したと公表。11月11日のファームウェア2.13.1でインプラントを無効化し、資金被害の報告はないという。同社はリセラー網を約8割削減する方針で、ハードウェアウォレットの購入経路の重要性が改めて浮き彫りになった。

🔗 [Trezor confirms crypto-stealing implants in three wallets, releases fix（BleepingComputer）](https://www.bleepingcomputer.com/news/cryptocurrency/trezor-confirms-crypto-stealing-implants-in-three-wallets-releases-fix/)
🔗 [Trezor confirms hidden hardware implant（The Hacker News）](https://thehackernews.com/2026/11/trezor-confirms-hidden-hardware.html)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | PHP2Shell、ESXiワイパー、M365障害、GitHub Actions |
| AI Risk | 🟠🟠 | ARTEX / AntiFox、エージェント型攻撃、OpenAI Daybreak |
| Data & Privacy | 🟡🟡🟡 | ニトリ3,762万件、Fireworks AI / Uber、フィリピン政府機関 |
| Security Governance | 🟢 | KEV / BOD 26-04、CIRCIA |
| Crypto Currency | 🟣 | Trezor Safe 5、ハードウェアインプラント |

---

*次回配信予定：2026年11月14日（土） | 収集ソース：BleepingComputer、Help Net Security、SecurityWeek、Infosecurity Magazine、Dark Reading、SentinelOne、Security Boulevard、AI Governance、TechCrunch、Philstar、CISA、Nextgov/FCW、The Hacker News、xAI Grok API*
