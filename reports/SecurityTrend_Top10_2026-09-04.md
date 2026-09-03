# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月4日（金）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **エージェンティックAIリスク** | AIエージェントが人の介入なしに攻撃・業務を自律実行するリスクが顕在化。NCSCの国際ガイドラインとUnit 42の自律型攻撃事例が同時に公表された。 |
| 2 | **認証バイパス（Auth Bypass）** | JFrog ArtifactoryとMicrosoft SharePointで相次いで認証バイパスの脆弱性が悪用され、管理者権限奪取や連鎖的RCEにつながっている。 |
| 3 | **サードパーティ／サプライチェーン侵害** | Thomson Reutersの裁判所向けシステムC-Trackが侵害され、米加の複数の裁判所データが漏えい。委託先経由の被害拡大が続く。 |
| 4 | **データブローカー規制強化** | CalPrivacyがデータブローカーへの摘発を継続。EUもDigital Omnibusで違反通知期限の見直しを提案し、規制の再編が進む。 |
| 5 | **重要インフラ（OT/PLC）攻撃** | 水道・エネルギー分野でPLC機器を狙った攻撃が拡大し、FBIが警告を発出。物理システムへの実害リスクが増している。 |

---

## 🔴 Cyber Security

### 1. Thomson Reutersの裁判所システムC-Track、米加で情報漏えい
**2026年9月3日**
Thomson Reutersの裁判記録管理ソフト「C-Track」が侵害され、米国11州・カナダ・米領ヴァージン諸島の裁判所データが影響を受けた。攻撃者は2026年3月にファイルを窃取していたが、発覚は6月30日だった。氏名等の個人情報に加え、一部の機密・封印記録も流出した可能性がある。

🔗 [Thomson Reuters Court Software Breach May Have Exposed SSNs and Sealed Data](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)
🔗 [US and Canadian Court Records Breached Following Thomson Reuters Incident](https://www.infosecurity-magazine.com/news/us-canada-court-breach-thomson/)

---

### 2. JFrog Artifactoryの認証バイパス脆弱性、公開直後に悪用開始
**2026年9月1日〜**
CVSS 9.8の重大な認証バイパス脆弱性CVE-2026-82329が、8月28日の修正公開からわずか数日で悪用され始めた。攻撃者は管理者トークンを不正発行し、ユーザーや権限情報を偵察している。自己ホスト型インスタンスが対象で、JFrogのSaaS版は影響を受けない。

🔗 [Attackers Exploit Critical JFrog Artifactory Flaw to Mint Admin Tokens Days After Disclosure](https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html)
🔗 [Hackers exploit critical JFrog Artifactory flaw to forge admin tokens](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/)

---

### 3. SharePointのJWT認証バイパス、RCEへ連鎖する攻撃が継続
**2026年8月〜9月**
7月のPatch Tuesdayで修正されたCVE-2026-55040（JWTトークン検証の複数の欠陥）を突くPoC公開後、攻撃者による不正なJWT偽造とサイト管理者へのなりすましが確認されている。さらにCVE-2026-63520と連鎖させることでリモートコード実行が可能となる。

🔗 [Attackers Exploit SharePoint Authentication Bypass After Public PoC Release](https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html)
🔗 [CVE-2026-55040: Microsoft SharePoint JWT Token Authentication Bypass](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/)

---

### 4. 水道・エネルギー分野のPLC機器を狙う攻撃が拡大、FBIが警告
**2026年8月（継続中）**
7月27日以降、少なくとも7州の水道・下水処理事業者がFBIにインシデントを報告。Rockwell Automation/Allen-BradleyのPLC（MicroLogix 1100/1400）がインターネット露出のまま狙われ、一部で運用障害が発生した。攻撃はエネルギー・化学・商業施設分野にも及ぶ。

🔗 [Malicious Cyber Actors Targeting Water and Wastewater Sector PLCs](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)
🔗 [Rising Cyberattacks on U.S. Water Infrastructure](https://foleyhoag.com/news-and-insights/blogs/energy-and-climate-counsel/2026/august/rising-cyberattacks-on-u-s-water-infrastructure-federal-guidance-and-next-steps-for-operators/)

---

## 🟠 AI Risk

### 5. NCSCとFive Eyes、エージェンティックAIのサイバーリスク管理指針を公表
**2026年8月20日**
英国NCSCが米加豪NZの当局と共同で、自律的に計画・判断・行動するAIエージェント特有のリスクに対応する国際ガイドラインを発表。最小権限の徹底、長期認証情報の排除、サンドボックス化、行動監視などを推奨している。

🔗 [NCSC Publishes Guidance on Securing Agentic AI Use](https://www.infosecurity-magazine.com/news/ncsc-publishes-guidance-securing/)
🔗 [Managing the cyber risk of agentic AI | NCSC](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)

---

### 6. 中国拠点の攻撃者、DeepSeek×Hermes Agentで自律型サイバー攻撃を実行
**2026年8月**
Palo Alto Networks Unit 42が、DeepSeekを推論エンジンとするオープンソースAIフレームワーク「Hermes Agent」を用いた自律攻撃キャンペーンを確認。460以上の標的に対し、人手を介さずFOFAでの標的探索から攻撃コード実行までを自動化していた。Citrix NetScaler等での情報窃取も確認された。

🔗 [Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)
🔗 [Hacker uses DeepSeek AI to autonomously attack vulnerable servers](https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/)

---

## 🟡 Data & Privacy

### 7. CalPrivacy、データブローカーSalesIntelに3.64万ドルの制裁金
**2026年9月1日**
カリフォルニア州プライバシー保護局（CPPA）が、データブローカー登録の遅延を理由にバージニア州のSalesIntel Researchへ制裁金36,400ドルを科した。同社は2億件超の企業連絡先情報を扱う。CalPrivacyによる摘発は今回で3社目となり「取り締まりの波」が続いている。

🔗 [CalPrivacy Continues Enforcement Blitz with Action Against Virginia Data Broker](https://privacy.ca.gov/2026/09/calprivacy-continues-enforcement-blitz-with-action-against-virginia-data-broker/)

---

### 8. EU、GDPR違反通知期限を72時間→96時間へ延長する改正案
**2026年（審議中、7月27日委員会修正記録）**
欧州委員会の「Digital Omnibus」提案が、GDPRの侵害通知期限を72時間から96時間へ延長し、報告基準も「リスク」から「高リスク」へ引き上げる内容を含む。複数の通知義務を一本化する「単一窓口」創設も盛り込まれている。

🔗 [EU Digital Omnibus Seeks 96-Hour GDPR Breach Deadline](https://www.brightdefense.com/news/eu-digital-omnibus-seeks-96-hour-gdpr-breach-deadline/)

---

## 🟢 Security Governance

### 9. 取締役会のサイバーリスク説明責任が拡大、NISTがAI向けフレームワークを整備
**2026年（進行中）**
SECの開示規則によりサイバーインシデントは取締役会レベルの説明責任事項となり、NISTは「AI向けサイバーセキュリティフレームワーク・プロファイル」の草案を公表。企業のAI導入速度がセキュリティ対応を上回る中、CISOのボード参画やサードパーティリスク開示の拡充が進んでいる。

🔗 [Cyber Risk Is Enterprise Risk: What That Means for Board Oversight in 2026](https://huntscanlon.com/cyber-risk-is-enterprise-risk-what-that-means-for-board-oversight-in-2026/)
🔗 [2026 Director's Handbook on Cyber-Risk | NACD](https://www.nacdonline.org/all-governance/governance-resources/governance-research/director-handbooks/2026-cyber-risk-oversight/)

---

## 🟣 Crypto Currency

### 10. Ledgerに5億ドル規模の集団訴訟、過去の情報漏えい放置を主張
**2026年8月27日提訴（9月3日報道）**
ニューヨーク州南部地区連邦裁判所に、Ledgerを相手取った集団訴訟が提起された。2020年の顧客270万件超の漏えいや2026年2月のフィッシング詐欺を放置したとして、少なくとも5億ドルの損害賠償を求めている。原告は詐欺師になりすまされ約195万ドルの暗号資産を窃取されたと主張。

🔗 [Ledger Data Breach Lawsuit Seeks $500 Million in Damages](https://en.cryptonomist.ch/2026/09/03/ledger-data-breach-lawsuit/)
🔗 [Ledger sued for $500M over alleged data breach and crypto theft](https://crypto.news/ledger-sued-for-500m-over-alleged-data-breach-and-crypto-theft/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | 認証バイパス、サードパーティ侵害、OT/PLC攻撃 |
| AI Risk | 🟠🟠 | エージェンティックAI、自律型攻撃、Five Eyesガイダンス |
| Data & Privacy | 🟡🟡 | データブローカー規制、GDPR改正 |
| Security Governance | 🟢 | 取締役会責任、NIST AIフレームワーク |
| Crypto Currency | 🟣 | 集団訴訟、ウォレットセキュリティ |

---

*次回配信予定：2026年9月5日（土） | 収集ソース：The Hacker News, BleepingComputer, SecurityWeek, Infosecurity Magazine, Unit 42 (Palo Alto Networks), NCSC, FBI, Bright Defense, NACD, crypto.news, Cryptonomist*
