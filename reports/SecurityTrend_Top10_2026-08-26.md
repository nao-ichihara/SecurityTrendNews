# セキュリティトレンド Top 10 ニュース
**配信日：2026年8月26日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CISAの3日パッチ義務（BOD 26-04）** | AIによる悪用高速化を理由に、CISAは重大脆弱性の連邦機関対応期限を3日に短縮。Oracle・Zimbraへの相次ぐ緊急指令が象徴。 |
| 2 | **OAuth／認証フロー悪用** | 正規のログイン・デバイス連携機能を悪用して多要素認証を回避する攻撃が国家支援型アクターで急増。 |
| 3 | **インフィニットミント（無制限発行）攻撃** | ブリッジやクロスチェーン機構の欠陥を突き、トークンを無制限発行して価格を暴落させるDeFi攻撃が8月に多発。 |
| 4 | **プロンプトインジェクション増加** | 悪意あるペイロードの検知が3月〜5月で約5倍に増加し、企業のAI利用リスクも拡大している。 |
| 5 | **露出したクラウド認証情報** | GitやDockerイメージ、CI/CDログに残る古いAWSキーが今も有効で、企業クラウドの乗っ取りリスクとして再注目。 |

---

## 🔴 Cyber Security

### 1. Oracle WebLogic/HTTP Serverの最大深刻度の脆弱性が実際に悪用、CISAが緊急指令
**2026年8月24日〜25日**
CVSS 10.0のCVE-2026-21962（Oracle HTTP ServerとWebLogic Server Proxy Plug-inの認証不要のアクセス制御不備）がCISAのKEVカタログに追加された。連邦機関には8月27日までの対応が義務付けられている。パッチ自体は今年1月に提供済みだったが、パッチ未適用環境が標的になっている。

🔗 [U.S. CISA adds maximum-severity Oracle flaw to its Known Exploited Vulnerabilities catalog](https://securityaffairs.com/197801/security/u-s-cisa-adds-maximum-severity-oracle-flaw-to-its-known-exploited-vulnerabilities-catalog.html)

---

### 2. Zimbra Collaboration Suiteの実悪用脆弱性、CISAが3日以内の対応を指示
**2026年8月21日〜24日**
CVE-2026-73570（SNMP通知が有効な環境で任意コマンド実行が可能）がKEVカタログに追加され、CISAは連邦機関に8月24日までの緩和策実施か利用停止を要求した。パッチはバージョン10.1.20（7月20日リリース）で提供済み。今年6月から適用されている「3日以内対応」の新方針(BOD 26-04)の一環。

🔗 [CISA orders urgent patching of actively exploited Zimbra flaw](https://www.bleepingcomputer.com/news/security/cisa-orders-urgent-patching-of-actively-exploited-zimbra-flaw/)

---

### 3. WordPressプラグイン「Everest Forms」の脆弱性で10万サイト超が乗っ取りリスクに
**2026年8月**
CVSS 9.8のCVE-2026-19598は、ファイルアップロード処理の検証不備によりPHPウェブシェルの設置を許す。認証不要で悪用可能で、バージョン3.0.9.5未満が影響を受ける。管理者は直ちにアップデートするか、公開フォームを一時停止する必要がある。

🔗 [WordPress Plugin Vulnerability Exposes 100,000 Sites to Complete Site Takeover Attacks](https://cybersecuritynews.com/wordpress-everest-forms-plugin-flaw/)

---

### 4. Googleがロシア系スパイ活動クラスターによるOAuth・WhatsApp連携悪用を報告
**2026年8月20日〜21日**
Google Threat Intelligence Groupは、UNC6293・UNC7005・UNC5976の3クラスターが、正規のOAuth認可フロー、アプリパスワード窃取、デバイスコード連携などを悪用し、多要素認証を回避してアカウントを乗っ取っていると発表。標的は欧米の防衛・政府・学術・シンクタンク関係者。

🔗 [Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts](https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html)

---

### 5. 漏洩した企業向けAWSキー768件が依然として管理者権限で有効
**2026年8月10日調査公表**
Truffle Securityが2022年〜2026年にGit履歴・Dockerイメージ・Hugging Faceデータセットなどから収集した1万件超のAWS認証情報を再検証したところ、88%が今も認証に成功。うち768件は企業関連で、526件がルートアクセスキー、242件が管理者権限付きIAMユーザーだった。

🔗 [768 Leaked Corporate AWS Keys Remain Active With Full Administrator Access](https://cybersecuritynews.com/768-leaked-corporate-aws-keys-remain-active/)

---

## 🟠 AI Risk

### 6. Ollama「Bleeding Llama」脆弱性、世界30万台のサーバーに影響の恐れ
**2026年8月**
CVE-2026-7482（CVSS 9.1）はOllamaのモデル量子化パイプラインにおけるヒープ範囲外読み取りの欠陥で、認証不要のままプロセスメモリ（システムプロンプトやユーザーメッセージ、環境変数）を漏洩させる。Ollamaはローカル利用前提のため認証機能を持たない設計が背景にある。加えてNVIDIA NemoClaw環境でも、悪意あるWebページ経由でローカルのOllamaサーバーを不正操作されうる別の欠陥が報告された。修正版0.17.1へのアップデートと、外部公開の禁止・認証プロキシの導入が推奨される。

🔗 [Ollama vulnerability highlights danger of AI frameworks with unrestricted access](https://www.csoonline.com/article/4168584/ollama-vulnerability-highlights-danger-of-ai-frameworks-with-unrestricted-access.html)

---

### 7. 間接的プロンプトインジェクションの検知が3〜5月で約5倍に急増
**2026年8月**
週次動向レポートによると、悪意あるペイロードを含む長文の間接プロンプトインジェクション検知が3月から5月にかけて約5倍に増加し、観測プロンプトの約1%に達した。あわせて、機密データ漏洩につながる高リスクなAI利用も1年で2%から4%へ倍増しており、組織が平均10種類のAIアプリを未承認のまま利用している実態も浮き彫りになった。

🔗 [AI Security Failures, Active Exploits, and Breaches Define the Week in August 2026](https://www.esecurityplanet.com/weekly-roundup/ai-security-failures-active-exploits-and-breaches-define-the-week-in-august-2026/)

---

## 🟡 Data & Privacy

### 8. EDPB、GDPR「削除権」監査結果を公表し2026年は透明性義務へ重点シフト
**2026年2月18日公表／継続的注目**
欧州データ保護会議（EDPB）は32カ国764組織を対象にした過去最大規模の「削除権」（GDPR第17条）協調執行結果を公表。バックアップ削除の不備や内部手続きの欠如など、全体的なコンプライアンスは「平均的」と評価された。2026年の協調執行フォーカス（CEF）は、削除権から一転し、GDPR第12〜14条が定める透明性・情報提供義務に重点が移る。

🔗 [GDPR Article 17 Right to Erasure: EDPB Audit Findings and 7 Compliance Fixes](https://secureprivacy.ai/blog/gdpr-article-17-right-to-erasure-edpb-audit-findings-and-7-compliance-fixes)

---

## 🟢 Security Governance

### 9. SEC、2026年審査重点方針から暗号資産を外しサイバーセキュリティとAIを最優先に
**2026年12月発表分の継続報道**
米証券取引委員会（SEC）の2026年examination prioritiesでは、過去5年間主要テーマだった暗号資産を単独項目から外し、サイバーセキュリティとAIガバナンスを最重点分野に格上げ。データ損失防止やアクセス管理、ランサムウェア対応体制、AI活用時のガバナンス・顧客説明の適切性などが審査対象となる。

🔗 [SEC drops crypto from 2026 exam priorities while emphasizing AI, cybersecurity and new rules](https://www.pionline.com/rules-regulations/government-politics/pi-sec-exams-cybersecurity-ai-crypto/)

---

## 🟣 Crypto Currency

### 10. ブリッジ・クロスチェーン基盤を狙った「無制限発行」攻撃が8月に相次ぐ
**2026年8月**
Oraichain（EVMクロスチェーン転送経路の欠陥で不正発行、8月9日からネットワーク停止）、Harmony Protocol（ONEトークン約40億枚を不正発行、総供給の約26%相当）、The Sandbox（SANDの無制限発行懸念で売り圧殺到）、MAP Protocol（Butter Bridge V3.1の欠陥で約1千兆枚の偽MAPOトークンを発行）など、ガバナンス不備やプロトコルバグに起因する「インフィニットミント」型攻撃が同時多発し、攻撃対象の広がりを示した。

🔗 [August 2026's Exploit Wave: Governance Failures, Protocol Bugs, And A Widening Attack Surface](https://mpost.io/august-2026s-exploit-wave-governance-failures-protocol-bugs-and-a-widening-attack-surface/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | CISA KEV、3日パッチ義務、OAuth悪用、認証情報漏洩 |
| AI Risk | 🟠🟠 | Ollama脆弱性、プロンプトインジェクション |
| Data & Privacy | 🟡 | GDPR第17条、EDPB、透明性義務 |
| Security Governance | 🟢 | SEC審査方針、AIガバナンス |
| Crypto Currency | 🟣 | インフィニットミント、ブリッジ攻撃 |

---

*次回配信予定：2026年8月27日（木） | 収集ソース：CISA、SecurityAffairs、BleepingComputer、CyberSecurityNews、TheHackerNews、CSO Online、eSecurity Planet、Secure Privacy、Pensions & Investments、Metaverse Post*
