# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月5日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **エージェント型AIのサイバーリスク** | 自律的に計画・実行するAIエージェントが攻撃・防御双方で存在感を増し、各国機関がガイダンス整備を急いでいる。 |
| 2 | **自律型AIサイバー攻撃** | AIモデル自身が標的探索からエクスプロイト実行までを行う攻撃キャンペーンが初めて具体的に報告された。 |
| 3 | **本人確認情報のダークウェブ流出** | 免許証など公的身分証のスキャン画像が大量に売買され、既存の本人確認システムを突破しうる脅威に。 |
| 4 | **身代金拒否後のデータリーク** | 企業が身代金支払いを拒否した結果、大規模な顧客データが公開される事案が相次いでいる。 |
| 5 | **暗号資産ウォレット窃取キャンペーン** | ブラウザ拡張機能やモバイルマルウェアを介した暗号資産窃取の手口が組織化・大規模化している。 |

---

## 🔴 Cyber Security

### 1. CISA、悪用が確認された脆弱性7件をKEVカタログに追加
**2026年9月2日**
米CISAは、実際の攻撃に悪用されていることが確認された脆弱性7件をKnown Exploited Vulnerabilities（KEV）カタログに追加した。対象にはSangoma Switchvox、Kestra OSS、LiteLLM、JFrog Artifactory、SonicWall SMA1000などが含まれる。攻撃者はリバースシェルの設置や暗号資産マイナーの展開に悪用しているという。

🔗 [CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html)

---

### 2. IDScan.net起点とみられる運転免許証1.53億件がダークウェブで販売
**2026年9月2〜3日**
米ルイジアナ州の本人確認企業IDScan.netを起点とみられる情報漏えいで、米国・カナダの運転免許証など1.53億件分のスキャン画像がダークウェブの識別情報販売サイト「Nexus」で発見された。赤外線・紫外線スキャンを含み、銀行などの本人確認システムを突破しうる。FBIが捜査を開始し、Nexusは報道後まもなく閉鎖された。

🔗 [153 Million Driver License Images Offered on Dark Web](https://www.securityweek.com/153-million-driver-license-images-offered-on-dark-web/)

---

### 3. マンチェスター空港グループ、身代金拒否後に880万人分のデータが流出
**2026年9月3〜4日**
英マンチェスター空港グループ（MAG）は、顧客エンゲージメント基盤Iterableの管理者キーがフロントエンドJavaScriptに露出していたことを突破口に侵入され、約549GB・880万人分の個人情報が窃取された。身代金支払いを拒否したため、攻撃グループFulcrumSecがデータをリークサイトで公開した。

🔗 [Manchester Airports Group Data on 8.8 Million People Leaked After Ransom Refusal](https://www.securityweek.com/manchester-airports-group-data-on-8-8-million-people-leaked-after-ransom-refusal/)

---

## 🟠 AI Risk

### 4. 中国系脅威アクター、DeepSeekとHermes Agentで自律型サイバー攻撃キャンペーンを実行
**2026年8月（Unit 42報告）**
Palo Alto Networks傘下のUnit 42は、中国語話者の脅威アクターがDeepSeekを推論エンジン、OSSのHermes Agentを実行基盤として用い、人手をほぼ介さず標的探索・エクスプロイト取得・攻撃実行を行う自律型キャンペーンを確認したと報告した。Hermesが自身のホームディレクトリからWebサーバーを誤って公開したことで攻撃者の環境が露呈し発覚。手動攻撃では460以上のシステムを標的にCitrix NetScalerの脆弱性（CVE-2026-3055）を悪用していた。

🔗 [Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)

---

### 5. OpenAI、サイバー防御に10億ドル投資──Astraがゼロデイ発見能力を獲得
**2026年9月4日**
OpenAIは自社のセキュリティモデルへの補助アクセスとして今後半年間で10億ドル相当を提供する「Daybreak」プログラムを発表した。同社は新モデルAstraが未知の脆弱性を自律的に発見し実働エクスプロイトを作成できると開示しており、重要インフラや政府機関、OSSメンテナーなどを優先的に支援する。

🔗 [OpenAI commits $1B in AI credits to frontline cyber defenders](https://www.theregister.com/security/2026/09/04/openai-commits-1b-in-ai-credits-to-frontline-cyber-defenders/)

---

### 6. 英NCSCなど各国機関、エージェント型AIのサイバーリスク管理ガイダンスを発表
**2026年8月20日（最新ブログ）**
英国家サイバーセキュリティセンター（NCSC）は、米CISA・NSAや豪加NZの機関と共同で、自律的に計画・判断・行動するエージェント型AIのリスク管理指針を公表した。サンドボックス化、厳格なアクセス制御、監査ログの整備、低リスク業務からの段階的導入などを推奨している。

🔗 [Managing the cyber risk of agentic AI](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)

---

## 🟡 Data & Privacy

### 7. EU「デジタル・オムニバス」、GDPR違反通知期限を72時間→96時間に延長提案
**2026年（審議継続中、直近の委員会修正は7月27日）**
欧州委員会が提案する「デジタル・オムニバス」法案は、GDPRに基づく監督当局への侵害通知期限を現行の72時間から96時間に延長し、報告閾値も「リスクがある」場合から「高リスクの可能性がある」場合へ引き上げる内容を含む。侵害報告を一元化する単一窓口の創設も盛り込まれるが、欧州議会では審議中で未成立。

🔗 [EU Digital Omnibus Seeks 96-Hour GDPR Breach Deadline](https://www.brightdefense.com/news/eu-digital-omnibus-seeks-96-hour-gdpr-breach-deadline/)

---

## 🟢 Security Governance

### 8. SEC「2026年審査優先事項」、暗号資産に代わりサイバー・AIガバナンスが最重要リスクに
**2025年12月公表（2026年の審査方針）**
米SECの検査部門が公表した2026年の審査優先事項では、過去5年間トップリスクだった暗号資産が単独項目として明記されなくなり、代わりにサイバーセキュリティとAIガバナンスが最重要領域に浮上した。ガバナンス体制、アクセス管理、AIを用いた投資助言の適正性などが重点審査対象となる。

🔗 [2026 SEC Exam Priorities for Registered Investment Advisers and Registered Investment Companies](https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-privateequity-pif-2026-sec-exam-priorities-for-registered-investment-advisers)

---

## 🟣 Crypto Currency

### 9. 偽Web3ウォレット拡張機能「Offside Wallet Theft Factory」、Firefoxストアで拡散
**2026年8月（活動は3月から、報告は8月）**
セキュリティ企業Socketは、OKXやRabby Wallet、TronLinkなどを装う悪性Firefox拡張機能群「Offside Wallet Theft Factory」を発見した。関連するアドオンIDは77件に上り、うち40件がシードフレーズや秘密鍵を窃取する機能を実装していた。Mozillaは該当拡張機能を削除し、ブロックリストに登録した。

🔗 [77 Firefox Extensions Linked to Crypto Wallet and Credential Theft](https://socket.dev/blog/firefox-crypto-wallet-theft)

---

### 10. Androidマルウェア「Manic」、ウクライナの銀行・暗号資産サービスを標的に
**2026年8月下旬〜9月初旬**
新種のAndroidマルウェア「Manic」が、ウクライナの銀行・政府系ID基盤・暗号資産サービスに加え、ロシアや欧州の金融機関を標的に確認された。銀行アプリや暗号資産ウォレット・取引所を含む169のアプリを監視し、PINコード窃取や画面オーバーレイによるフィッシングに加え、位置情報追跡やファイル窃取などのスパイウェア機能も備える。Wi-Fi DirectやBluetoothを使ったオフライン中継機能も特徴的。

🔗 [Manic Android Malware Exfiltrates Data From Offline Phones via Nearby Infected Devices](https://thehackernews.com/2026/08/manic-android-malware-exfiltrates-data.html)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | KEVカタログ、ダークウェブ流出、ランサムウェア |
| AI Risk | 🟠🟠🟠 | 自律型AI攻撃、エージェントAIガバナンス、AIセキュリティ投資 |
| Data & Privacy | 🟡 | GDPR、侵害通知期限、デジタル・オムニバス |
| Security Governance | 🟢 | SEC審査優先事項、AIガバナンス、コンプライアンス |
| Crypto Currency | 🟣🟣 | ウォレット窃取、ブラウザ拡張機能、モバイルマルウェア |

---

*次回配信予定：2026年9月6日（日） | 収集ソース：The Hacker News, SecurityWeek, Unit 42 (Palo Alto Networks), The Register, NCSC.gov.uk, BrightDefense, Goodwin Law, Socket.dev*
