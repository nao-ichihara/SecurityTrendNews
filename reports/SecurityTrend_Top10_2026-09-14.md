# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月14日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **StyleSmuggler** | Magento/Adobe Commerceの未認証RCEゼロデイ（CVE-2026-75650）の通称。パッチ適用済み環境でも侵害例が報告された。 |
| 2 | **ShinyHunters** | McKesson等の大規模データ窃取・恐喝事件の背後にいるとされる攻撃グループ。医療・ヘルスケア業界を狙う事例が続く。 |
| 3 | **CISA KEV** | GitLabのCVE-2026-85706が公開から1日で悪用され、CISAの「既知の悪用脆弱性」カタログに追加・対応期限が設定された。 |
| 4 | **AIオーケストレーション型攻撃** | AnthropicのAI脅威レポートが指摘した、AIモデルを多段階攻撃チェーンの実行ノードとして悪用する手口。 |
| 5 | **EU AI Act施行** | 2026年8月2日から欧州委員会AI Officeが透明性義務等の本格執行を開始し、違反時は巨額の制裁金が科され得る。 |

---

## 🔴 Cyber Security

### 1. GitLabの最大深刻度パス・トラバーサル脆弱性、CISA KEVに追加され悪用進行中
**2026年9月11日**
GitLabのリポジトリcommits APIに存在するCVE-2026-85706（CVSS 10.0）が公開から1日で実際に悪用され、CISAが既知の悪用脆弱性（KEV）カタログに追加した。未認証の攻撃者が単一のHTTPリクエストでSSH鍵やDB認証情報などの機微な設定情報を読み取れる。対応期限は9月14日に設定されている。

🔗 [GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html)
🔗 [GitLab urges users to patch max severity path traversal flaw](https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/)

---

### 2. Magento/Adobe Commerceの「StyleSmuggler」ゼロデイ、パッチ済み環境でも侵害
**2026年9月7日**
Sansecが発見した未認証RCEゼロデイ（CVE-2026-75650、CVSS 10.0）が9月4日から悪用され、テンプレート機能を悪用したPHPコード注入でRust製Linuxバックドアやウェブシェルが設置される事例が確認された。2026年7〜8月分のセキュリティ更新を適用済みの環境でも侵害が報告されている。Adobeは9月7日に緊急パッチを公開した。

🔗 [Adobe fixes critical Magento zero-day exploited to backdoor servers](https://www.bleepingcomputer.com/news/security/adobe-fixes-critical-magento-zero-day-exploited-to-backdoor-servers/)
🔗 [Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell](https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html)

---

### 3. 医薬品卸大手McKesson、ShinyHuntersによる2.84億件データ窃取主張と巨額の身代金要求
**2026年8月31日〜9月上旬**
McKessonは8月25日に第三者アプリケーション経由の不正アクセスとデータ窃取を確認した。ShinyHuntersは氏名・住所・社会保障番号に加え診断・投薬歴などの医療情報を含む2.84億件の記録窃取を主張し、約5,500万ドルを要求している。McKessonは信用監視サービスの提供と情報提供窓口の設置で対応している。

🔗 [McKesson Confirms Data Breach as Attacker Deadline Looms](https://www.securityweek.com/mckesson-confirms-data-breach-as-attacker-deadline-looms/)
🔗 [Hackers claim millions of patient records stolen during data breach at healthcare giant McKesson](https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/)

---

## 🟠 AI Risk

### 4. Anthropic、AIをオーケストレーション役に使う多段階攻撃チェーンを報告
**2026年9月11日**
Anthropicの脅威インテリジェンスレポート（2025年12月〜2026年8月分）は、国家支援組織や金銭目的の犯罪集団がClaudeを多段階攻撃フレームワーク内の実行ノードとして悪用する事例を開示した。ロシア関連とされる「Midnight Blizzard（GTG-20006）」は130日間で27組織中24組織へ侵入し、ウクライナの国防関連機関等を標的とした。盗まれたAI APIキー・セッショントークン自体が転売対象になっている点も指摘されている。

🔗 [Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

### 5. Azure OpenAIの重大SSRF脆弱性（CVSS 9.9）、権限昇格を許す設計不備
**公開：2026年7月2日／継続的注目**
CVE-2026-45499はAzure OpenAIにおけるサーバーサイドリクエストフォージェリ（SSRF）の脆弱性で、認証済み攻撃者が内部ネットワークエンドポイントへのリクエストを介して権限を昇格できる不備だった。Microsoftはクラウド側で既に完全に修正済みで顧客側の対応は不要だが、AIサービス特有の権限設計リスクの事例として引き続き参照されている。

🔗 [CVE-2026-45499 - Security Update Guide - Microsoft](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45499)

---

### 6. 「未承認AIアプリ」利用の拡大とリスクプロンプトの倍増が浮き彫りに
**2026年9月（Check Point AI Security Report 2026）**
組織は平均して月10種類のAIアプリケーションを利用しているが、その多くが正式な承認プロセスを経ていない。高リスクなプロンプトの割合は過去1年で2%から4%へ倍増し、AI用APIキーやエージェント連携用トークンを本番環境の認証情報と同等の重要度で扱うべきだとする指摘が強まっている。

🔗 [AI Security Report 2026 - Check Point Research](https://research.checkpoint.com/2026/ai-security-report-2026/)

---

## 🟡 Data & Privacy

### 7. Alipay利用者8.2億件分とされるデータがダークウェブで販売主張（未確認）
**2026年9月上旬**
攻撃者を名乗る人物が、氏名・電話番号・メールアドレスなどを含むAlipayユーザー8.2億件分のデータベースを保有していると主張し、闇市場での販売を持ちかけた。Alipay側からの侵害確認や情報流出元の特定はできておらず、重複データや他ソースとの混在の可能性も指摘されており、現時点では未確認情報として扱われている。

🔗 [Hacker puts data of 820 million Alipay users up for sale](https://www.escudodigital.com/en/cybersecurity/hacker-puts-data-of-820-million-alipay-users-up-for-sale.html)

---

### 8. ベトナム関連APIS（渡航者事前情報システム）から2.2億件のパスポート・搭乗記録が公開状態に
**発見：2026年6月3日／報道：2026年9月**
Kinryū Labsが、2017年〜2026年4月分の渡航者・乗員記録約2.2億件を含むElasticsearchクラスタが、認証不備とデフォルト認証情報の残存という2つの設定不備により誰でもアクセス可能な状態だったと報告した。6月8日に閉鎖されたが、閉鎖前にデータが窃取・転売されたかどうかは確認されていない。

🔗 [220 million traveler records exposed in Vietnam-linked APIS leak](https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/)

---

## 🟢 Security Governance

### 9. EU AI Act、透明性義務の本格執行がスタート
**施行：2026年8月2日／9月時点で運用継続中**
欧州委員会AI Officeと各国当局が8月2日からAI Actの本格的な執行を開始した。チャットボットの自動応答明示義務、ディープフェイクへのラベル付与、AI生成コンテンツへの機械可読な表示義務などが対象で、違反時は最大1,500万ユーロまたは全世界年間売上高の3%のいずれか高い方の制裁金が科され得る。金融安定理事会（FSB）もG20に対しフロンティアAIのサイバーリスクについて警告している。

🔗 [Commission starts enforcing AI Act rules and new transparency requirements on 2 August](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
🔗 [EU begins enforcing AI Act, putting AI models under the microscope](https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/)

---

## 🟣 Crypto Currency

### 10. Bitcoinサイドチェーン「Liquid Network」から3.2億ドル流出、「ホワイトハット」を名乗り大半を返還
**2026年9月6日〜8日**
Blockstreamが運営するBitcoinサイドチェーンLiquid Networkの連合ウォレットから約4,000BTC（3.2億ドル相当）が流出した。Blockstreamは鍵漏洩ではなくElementsのソフトウェアバグが原因と説明している。攻撃者はOP_RETURNを使った取引メッセージでBlockstreamと交渉し、9月8日までに3,400BTCを返還、約598.5BTC（引き出し額の約15%）を「手数料」として保持した。

🔗 [$320 million bitcoin exploit hits Liquid Network. Hacker makes conditional offer](https://www.coindesk.com/markets/2026/09/07/bitcoin-network-used-by-exchanges-hit-by-usd320-million-exploit-hackers-claim-they-re-the-good-guys)
🔗 [Liquid Network hack: Whitehats return 3,400 BTC](https://www.coindesk.com/markets/2026/09/08/white-hat-hackers-return-most-of-usd320m-bitcoin-taken-from-liquid-network)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | GitLab CVE-2026-85706, StyleSmuggler, ShinyHunters |
| AI Risk | 🟠🟠🟠 | Anthropic脅威レポート, Azure OpenAI SSRF, 未承認AIアプリ |
| Data & Privacy | 🟡🟡 | Alipay（未確認）, APIS 2.2億件流出 |
| Security Governance | 🟢 | EU AI Act施行, FSB |
| Crypto Currency | 🟣 | Liquid Network, ホワイトハット |

---

*次回配信予定：2026年9月15日（火） | 収集ソース：SecurityWeek、BleepingComputer、The Hacker News、TechCrunch、CoinDesk、Anthropic公式、欧州委員会 ほか*
