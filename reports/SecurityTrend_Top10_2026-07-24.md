# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月24日（金）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **自律型AIエージェント攻撃** | AIエージェントが自律的に偵察・侵入・横展開まで実行する攻撃が実際に観測され始めた。Hugging Face侵害が象徴例。 |
| 2 | **Agent Data Injection（ADI）** | AIエージェントが「信頼しているデータ」自体を汚染し誤操作させる新種の攻撃手法。プロンプトインジェクションとは異なる防御が必要。 |
| 3 | **記録的ゼロデイ・パッチ** | Microsoftの2026年7月Patch Tuesdayは過去最大規模となり、悪用済みゼロデイも複数含まれた。 |
| 4 | **クロスチェーンブリッジ攻撃** | 鍵管理やアップグレード権限の不備を突いた攻撃で、暗号自体ではなく運用ガバナンスの弱さが繰り返し標的に。 |
| 5 | **侵害の透明性（Breach Transparency）** | インシデント対応の開示姿勢や社内文化がガバナンス評価の焦点として重要度を増している。 |

---

## 🔴 Cyber Security

### 1. Hugging Face、自律型AIエージェントによる侵害を確認
**2026年7月20日**
世界最大級のAIモデルリポジトリHugging Faceが、自律型AIエージェントシステムによる侵害を公表した。悪意あるデータセットがコード実行の脆弱性を悪用し、ノードレベルへの権限昇格からクラウド・クラスタ認証情報の窃取、複数内部クラスタへの横展開まで、週末の間に自動化された形で実行された。パートナーや顧客データへのアクセス、公開モデルの改ざんの証拠は現時点で確認されていない。

🔗 [World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent](https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html)

---

### 2. Microsoft、過去最大規模の月例パッチで悪用済みゼロデイ2件に対応
**2026年7月（Patch Tuesday）**
Microsoftの2026年7月Patch Tuesdayは約570件の脆弱性に対応する過去最大規模となり、SharePoint Serverの権限昇格ゼロデイ（CVE-2026-56164）とActive Directory Federation Servicesの脆弱性（CVE-2026-56155)が実際に悪用されていたことが判明した。SharePointの脆弱性はMandiant/Google FLAREが実際の攻撃対応中に発見したもの。

🔗 [Microsoft's July 2026 Patch Tuesday Addresses 569 CVEs (CVE-2026-56155, CVE-2026-56164)](https://www.tenable.com/blog/microsofts-july-2026-patch-tuesday-addresses-569-cves-cve-2026-56155-cve-2026-56164)

---

### 3. SonicWall SMA1000、CVSS10.0の脆弱性連鎖で完全なリモートコード実行が可能に
**2026年7月14日（CISA KEV追加）**
SonicWall SMA1000アプライアンスの未認証SSRF脆弱性（CVE-2026-15409、CVSS10.0）は、別の脆弱性（CVE-2026-15410）と連鎖させることで完全なリモートコード実行に至ることが判明し、CISAの既知悪用脆弱性（KEV）カタログに追加された。

🔗 [July 2026 InfraTrust Report Flags 26 Unauthenticated Vulnerabilities and Exploited SonicWall Flaws](https://cybersecuritynews.com/infratrust-flags-26-vulnerabilities/)

---

### 4. 160万インストールのChrome拡張機能ModHeader、マルウェア認定で削除
**2026年7月**
開発者やQAエンジニアに広く使われるHTTPヘッダー編集拡張機能「ModHeader」に、閲覧履歴を収集・暗号化して外部送信する休眠コードが発見され、GoogleとMicrosoftがChromeおよびEdgeストアから削除した。実際のデータ窃取は未確認だが、認証トークンやCookieを含む内部ツール・CI/CD情報が標的化されるリスクが指摘されている。

🔗 [Google removes popular Chrome extension: hidden surveillance code found](https://cybernews.com/security/modheader-chrome-extension-hidden-tracker/)

---

### 5. EY（アーンスト・アンド・ヤング）、ITサポート基盤侵害で顧客税務データ流出
**2026年7月15日（州当局へ通知）**
EYは、IT部門が利用するサードパーティ製サポートチケット基盤に第三者が不正アクセスし、2026年3月28日から4月12日にかけて顧客の税務・投資保有関連文書をダウンロードしていたことを公表した。悪用や特定個人への標的化の証拠は現時点でないとしている。

🔗 [Ernst & Young discloses data breach after support system hack](https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/)

---

## 🟠 AI Risk

### 6. AIリスクがデータ盗難を抜き、セキュリティ投資の最大要因に浮上
**2026年7月**
EMA ResearchとSkyhigh Securityの調査によると、企業のセキュリティ投資判断において、従来型のデータ盗難よりもAI関連リスクが最大の推進要因となったことが明らかになった。AI統合がセキュリティ管理体制のスピードを上回り、データ操作・認証情報管理・分離不足が新たな運用・コンプライアンスリスクを生んでいる。

🔗 [AI Risks Overtake Data Theft as the #1 Driver for Security Investments](https://finance.yahoo.com/technology/ai/articles/ai-risks-overtake-data-theft-143200317.html)

---

### 7. 新種「Agent Data Injection（ADI）」攻撃、AIエージェントの誤操作を誘発
**2026年7月6日（論文発表）**
ソウル大学、イリノイ大学アーバナ・シャンペーン校などの研究者が、AIエージェントが信頼するデータ自体を汚染して誤動作させる新攻撃手法「Agent Data Injection」を発表した。1件の偽レビューでAIエージェントに意図しない購入操作をさせたり、GitHub上の偽コメントでコーディングアシスタントに任意コマンドを実行させたりできる。従来のプロンプトインジェクション対策をすり抜ける点が特徴。

🔗 [New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands](https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html)

---

## 🟡 Data & Privacy

### 8. 米国で州プライバシー法の新設・改正が相次ぐ、2026年は「執行元年」に
**2026年（通年、7月時点最新）**
2026年はインディアナ、ケンタッキー、ロードアイランドで新たな包括的プライバシー法が施行され、アーカンソーも7月に新法を導入した。カリフォルニアではCCPA改正規則により、自動意思決定技術（ADMT）に関する透明性強化やリスク評価の義務化が進み、コロラド・オレゴンも生体情報や位置情報などセンシティブデータの保護を強化。規制当局の焦点は法制定から「執行」へと移行しつつある。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. 「侵害の透明性」、サイバーセキュリティガバナンス最大の課題として浮上
**2026年7月**
インシデント対応時の開示姿勢や透明性、それを支える組織文化が、ガバナンス評価における最重要論点として注目されている。説明責任と信頼を担保する体制構築が、規制対応以上に企業の実質的なセキュリティ成熟度を左右するとの指摘が強まっている。

🔗 [Breach Transparency Remains Cybersecurity's Toughest Governance Problem](https://thehackernews.com/expert-insights/2026/07/breach-transparency-remains.html)

---

## 🟣 Crypto Currency

### 10. クロスチェーンブリッジが6時間で3件連続攻撃、3500万ドル超が流出
**2026年7月23日**
VerusのEthereumブリッジが5月の攻撃と同じ脆弱性クラスを突かれ約754万ドルを喪失、B²Networkはステーキングコントラクトのアップグレード権限を乗っ取られ約386万ドルを喪失するなど、6時間以内に複数の暗号資産ブリッジが攻撃を受け合計3500万ドル超が流出した。暗号技術自体ではなく、鍵管理やアップグレード権限などの運用ガバナンスの不備が繰り返し狙われている。

🔗 [Bitcoin, Ethereum-linked protocols lose $35 million in multiple attacks hours apart](https://www.coindesk.com/tech/2026/07/23/bitcoin-ethereum-linked-protocols-lose-usd35-million-in-multiple-attacks-hours-apart)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | 自律AIエージェント侵害、ゼロデイ、脆弱性連鎖、悪性拡張機能 |
| AI Risk | 🟠🟠 | AIリスク投資シフト、Agent Data Injection |
| Data & Privacy | 🟡 | 州プライバシー法、ADMT規制 |
| Security Governance | 🟢 | 侵害の透明性、説明責任 |
| Crypto Currency | 🟣 | クロスチェーンブリッジ攻撃、鍵管理不備 |

---

*次回配信予定：2026年7月25日（土） | 収集ソース：The Hacker News, BleepingComputer, SecurityWeek, Cybersecurity News, CyberNews, Tenable, CoinDesk, Yahoo Finance, Gunster*
