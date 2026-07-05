# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月6日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **FortiBleed** | Fortinet FortiGate機器を狙った大規模な認証情報窃取キャンペーン。世界430,000台に影響し、INC・Lynxランサムウェアへの侵入経路として悪用されている。 |
| 2 | **CVE-2026-45659（SharePoint RCE）** | Microsoft SharePoint Serverのリモートコード実行脆弱性。CISAがKEVカタログに追加し、連邦機関に7月4日までの修正適用を義務付けた。 |
| 3 | **Avalon / CrownX** | フィッシング経由で拡散する新型モジュール型マルウェア。資格情報窃取から横展開、ランサムウェア実行までを一括で担う。 |
| 4 | **AIリスクの投資シフト** | AIリスクがデータ盗難を上回り、企業のセキュリティ投資における最大の動機に。エージェントAIセキュリティ市場は2032年に135億ドル規模へ拡大予測。 |
| 5 | **北朝鮮の暗号資産窃取** | 北朝鮮関連アクターが2026年上半期だけで6.43億ドル相当の暗号資産を窃取し、世界の暗号資産犯罪をリード。 |

---

## 🔴 Cyber Security

### 1. SharePoint RCE「CVE-2026-45659」がCISAのKEVカタログに追加、悪用が活発化
**2026年7月3日**
Microsoft SharePoint Serverの深刻なリモートコード実行脆弱性（CVSS 8.8）が、信頼できないデータのデシリアライズに起因することが判明。CISAは実際の悪用を確認し、既知悪用脆弱性（KEV）カタログに追加した。連邦機関には7月4日までの修正適用が義務付けられている。

🔗 [SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html)

---

### 2. 「FortiBleed」キャンペーンで430,000台のFortiGateが影響、ランサムウェアと直結
**2026年7月5日**
Fortinet FortiGateファイアウォールを狙った大規模な認証情報窃取キャンペーン「FortiBleed」が、INCおよびLynxランサムウェアの侵入経路として使われていたことが判明。1.1億件超の認証情報が窃取され、少なくとも12件のランサムウェア展開に直結した。

🔗 [FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations](https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html)

---

### 3. Oracle E-Business Suiteの重大脆弱性が悪用継続、950台超が公開状態
**2026年6月30日**
Oracle Paymentsモジュールの権限管理・認証不備の脆弱性「CVE-2026-46817」（CVSS 9.8）が、5月のパッチ公開後も未パッチ環境で悪用されている。攻撃者は認証なしでリモートから侵害可能で、公開されたままの950台超のインスタンスが標的となっている。

🔗 [Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild](https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html)

---

### 4. Progress Kemp LoadMasterの事前認証RCE脆弱性、悪用試行を確認
**2026年7月2日**
ロードバランサー製品Kemp LoadMasterのOSコマンドインジェクション脆弱性「CVE-2026-8037」（CVSS 9.6）で、6月29日から悪用試行が観測された。escape_quotes()関数のヒープ境界外読み取りに起因し、API機能を有効化した機器が標的となる。

🔗 [Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts](https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html)

---

### 5. 新型モジュール型マルウェア「Avalon」、ランサムウェア「CrownX」を内包
**2026年7月3日**
フィッシングメールを起点とする多段階攻撃で拡散する新種マルウェアフレームワーク「Avalon」が発見された。資格情報窃取・横展開・遠隔操作・復旧妨害・ランサムウェア実行を一つに統合し、主要EDR製品の検知回避機能も備える。

🔗 [New Avalon Malware Framework Packs CrownX Ransomware Capabilities](https://thehackernews.com/2026/07/new-avalon-malware-framework-packs.html)

---

## 🟠 AI Risk

### 6. AIリスクがデータ盗難を上回り、セキュリティ投資の最大動機に
**2026年7月1日**
最新調査により、企業のセキュリティ投資判断における最大の動機が従来のデータ盗難からAIリスクへ移行したことが明らかになった。エージェント型AIセキュリティ市場は2026年の16.5億ドルから2032年には135.2億ドルへ拡大すると予測されている。

🔗 [AI Risks Overtake Data Theft as the #1 Driver for Security Investments](https://www.globenewswire.com/news-release/2026/07/01/3320801/0/en/ai-risks-overtake-data-theft-as-the-1-driver-for-security-investments.html)

---

### 7. CISA、AI悪用を見据えた「高リスク脆弱性」優先パッチ指令を発令
**2026年6月30日**
AIモデルの進化により攻撃者がソフトウェアの脆弱性をより迅速に特定・悪用できるようになっていることを受け、CISAは高リスク脆弱性のパッチ適用を優先する拘束力のある運用指令を発出した。

🔗 [AI directive focuses patching efforts on 'highest risk' vulnerabilities](https://federalnewsnetwork.com/cybersecurity/2026/06/ai-directive-focuses-patching-efforts-on-highest-risk-vulnerabilities/)

---

## 🟡 Data & Privacy

### 8. 米国各州のプライバシー法が続々施行、アーカンソー州は7月から新法適用
**2026年7月1日**
2026年は米国で約20州が独自のデータプライバシー規制を持つに至り、カリフォルニア・コネチカット・オレゴン・ユタ各州で規制が更新されたほか、アーカンソー州で新たなプライバシー法が7月に施行された。未成年者データや自動意思決定、データブローカーの透明性への規制強化が焦点となっている。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. 政権、国家安全保障システム向けサイバーセキュリティ統治に関する覚書を発出
**2026年6月12日**
米政権は国家安全保障システムのサイバーセキュリティ統治に関する覚書を発出し、国家安全保障局（NSA）長官が国家管理者を務める「国家安全保障システム委員会（CNSS）」を再設置した。連邦機関のガバナンス体制見直しにつながる動きとして注目されている。

🔗 [Administration releases memo on cybersecurity governance for national security systems](https://www.aha.org/news/headline/2026-06-15-administration-releases-memo-cybersecurity-governance-national-security-systems)

---

## 🟣 Crypto Currency

### 10. 北朝鮮関連アクター、2026年上半期だけで6.43億ドル相当の暗号資産を窃取
**2026年7月2日**
北朝鮮関連のサイバー犯罪グループが2026年上半期に6.43億ドル相当の暗号資産を窃取し、世界の暗号資産犯罪をリードしていることが判明した。6月だけでもDeFiプラットフォームやクロスチェーンブリッジを狙った40件の重大な侵害で7,587万ドルの損失が発生しており、鍵管理の不備が主要因の一つとされる。

🔗 [North Korea leads global crypto crime with theft of $643M in first half of 2026](https://www.nknews.org/2026/07/north-korea-leads-global-crypto-crime-with-theft-of-643m-in-first-half-of-2026/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | FortiBleed, SharePoint RCE, Oracle EBS, Kemp LoadMaster, Avalon |
| AI Risk | 🟠🟠 | AIリスク投資シフト, CISA AI指令 |
| Data & Privacy | 🟡 | 米国州プライバシー法, アーカンソー州 |
| Security Governance | 🟢 | CNSS再設置, 国家安全保障システム統治 |
| Crypto Currency | 🟣 | 北朝鮮, 暗号資産窃取, 鍵管理不備 |

---

*次回配信予定：2026年7月7日（火） | 収集ソース：The Hacker News, Federal News Network, GlobeNewswire, Gunster, AHA News, NK News*
