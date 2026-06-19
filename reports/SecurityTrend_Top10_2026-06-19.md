# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月19日（金）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **FortiBleed** | 約75,000台のFortinet FortiGateファイアウォールの管理者認証情報が流出した大規模キャンペーン。194カ国・政府機関・大手企業を直撃し、進行中の攻撃として最大級の脅威となっている。 |
| 2 | **RoguePlanet（CVE-2026-50656）** | Microsoft Defenderのゼロデイ特権昇格脆弱性。完全パッチ済みのWindows 10/11でもSYSTEM権限を奪取可能で、パッチ未提供のまま公開PoC（概念実証コード）が出回っている。 |
| 3 | **AI駆動型サイバー攻撃** | Verizon 2026 DBIRで脆弱性悪用が初めて最大の侵害経路（31%）となり、AIが攻撃速度を「数ヶ月」から「数時間」に短縮していることが確認された。 |
| 4 | **サプライチェーン攻撃** | JetBrainsマーケットプレイスの不正プラグイン（約7万インストール）やNintendoのサードパーティHRシステム侵害など、供給チェーン経由の攻撃が急増・多様化している。 |
| 5 | **米国暗号資産犯罪対策タスクフォース法案** | FBI記録で2025年に米国民が暗号資産詐欺で110億ドル超の被害を受けた背景に、DOJ主導の新たな連邦タスクフォース設立法案が超党派で提出された。 |

---

## 🔴 Cyber Security

### 1. 「FortiBleed」―75,000台のFortinet FireGateの管理者パスワードが流出・進行中の攻撃
**2026年6月18日（木）**


新たに発覚した「FortiBleed」と呼ばれるサイバー犯罪キャンペーンにより、約75,000台のFortinet FortiGateファイアウォールの管理者認証情報が流出し、世界中の企業ネットワークへの直接アクセスを攻撃者に与える可能性がある。
流出データは194カ国に及ぶ組織に影響しており、大手企業・政府機関・重要インフラの事業者の有効な認証情報が含まれている。
データにはOracle、Chevron、Lenovo、FedEx、Foxconn、Samsung、Comcast、Siemens、PwC、Accentureなどの名前が含まれ、研究者はこのキャンペーンをロシア語話者グループに帰属させている。
脅威インテリジェンス企業SOCRadarは、攻撃者のインフラが現在も稼働中であり、新たな被害組織が追加され続けている「進行中のキャンペーン」と警告している。


🔗 [FortiBleed campaign exposes 75,000 Fortinet firewalls worldwide](https://www.csoonline.com/article/4186790/fortibleed-campaign-exposes-75000-fortinet-firewalls-worldwide.html)

---

### 2. Microsoft Defender ゼロデイ「RoguePlanet」（CVE-2026-50656）―パッチなしで公開PoC出回る
**2026年6月16〜17日（火・水）**


Microsoftは、「RoguePlanet」と呼ばれるMicrosoft Defenderの重大なゼロデイ脆弱性を正式に認め、セキュリティパッチを開発中と発表した。CVE-2026-50656として追跡され、CVSS 3.1スコア7.8（重要）が付与されている。
この脆弱性はDefenderのリアルタイムスキャンエンジン内のTOCTOU（Time-of-Check/Time-of-Use）競合状態を悪用し、成功すると最高権限であるNT AUTHORITY\SYSTEMでコマンドプロンプトが起動される。
この脆弱性は2026年6月の累積アップデートを適用済みのWindows 10およびWindows 11にも影響する。
RoguePlanetはMicrosoftとの確執から2026年3月以降Microsoft製品のゼロデイを公開し続けている「Nightmare Eclipse」という研究者がリリースしたエクスプロイトの一つとされている。


🔗 [Microsoft Confirms Defender RoguePlanet 0-Day Exploit and Working to Release Patch](https://cybersecuritynews.com/defender-rogueplanet-0-day-exploit-patch/)

---

### 3. Nintendo 従業員データ侵害―ShadowByte$が200万ドルの身代金要求
**2026年6月13〜16日（金〜火）**


サイバー犯罪グループ「ShadowByte$」がNintendoの社内ネットワークへの侵害と称し、200万ドルの身代金を要求した。
主張によると、従業員名・メールアドレス・アンケート・分析レポート・銀行明細・W-9フォーム・職場フィードバックなどを含む約859MBのデータがHRプラットフォーム「TINYpulse」から搾取されたという。
Nintendoが支払いを拒否したため、犯罪グループはTinyPulse社に直接要求先を変更したと報じられている。
Nintendoは「Nintendo of Americaの一部の従業員の内部アンケートに限定されたもので、顧客データや財務データへのアクセスはない」と声明を出した。


🔗 [Hackers demand $2M from Nintendo over alleged data breach](https://cybernews.com/security/nintendo-employee-data-ransom-claim/)

---

### 4. ServiceNow APIゼロ認証脆弱性―顧客データが不正アクセスに晒される
**2026年6月5〜9日（金〜火）**


ServiceNowの侵害は、認証不要に設定されたScripted REST Resourceを攻撃者が悪用したもので、2026年6月2〜3日の間、顧客インスタンスのITチケット・従業員記録・資産一覧・埋め込み認証情報が単一の有効な認証情報なしに抽出された。
ServiceNowが静かにパッチを適用した6月5日から6月9日の公開開示まで4日間のギャップがあり、この間組織は発生した侵害を監査できなかった。
さらに、あるセキュリティチームが約4月7日にServiceNowへ脆弱性を報告しており、6月5日のパッチまでの約2ヶ月間、社内で問題を把握していた可能性が指摘されている。


🔗 [ServiceNow data breach: security issue gives attacker access](https://cybernews.com/security/servicenow-confirms-security-incident-data-breach/)

---

## 🟠 AI Risk

### 5. JetBrains Marketplace 不正プラグイン―AIのAPIキーを70,000回以上盗むサプライチェーン攻撃
**2026年6月16〜17日（火・水）**


JetBrains Marketplace上で15本の悪意あるプラグインによる「協調マルウェアキャンペーン」が確認された。すべてのプラグインがDeepSeekなどの大規模言語モデルを基盤にしたAIコーディングアシスタントを装っていた。
7つのベンダーアカウント下でリリースされたこれらのプラグインは合計約70,000回インストールされ、最新版は2026年6月10日まで公開されており、ユーザーが設定に入力したAI APIキーを攻撃者のサーバーに密かに送信していた。
主なターゲットはOpenAI・DeepSeek・SiliconFlowなどのAIプロバイダーのAPIキーであった。
JetBrainsは6月16日に報告を受け、問題のプラグインをマーケットプレイスから削除し、関連する発行者アカウントをブロック、バックエンドシステムを通じてインストール済みIDEでも無効化した。


🔗 [Malicious JetBrains Marketplace plugins steal AI API keys from developers](https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/)

---

### 6. Verizon 2026 DBIR―脆弱性悪用がはじめて最大の侵害起点に、AIが攻撃速度を劇的加速
**2026年5月〜6月（継続注目）**


Verizonの2026 DBIRによると、ソフトウェアの欠陥を使用した脆弱性悪用（31%）が、はじめて盗まれた認証情報を上回り最大の初期侵害起点となった。AIが攻撃を数ヶ月から数時間へ加速させている。
従業員による未承認の「シャドーAI」ツール利用は前年比3倍の45%に急増してデータ漏洩リスクを高め、サードパーティのサプライチェーン侵害は60%増加して全体の48%を占めるに至った。
DBIRはAIの主な影響は既存のサイバー攻撃を自動化・拡大することであり、熟練度の低い攻撃者でも以前は高度な技術を要した攻撃を実行できるようになっていると結論づけている。


🔗 [Verizon DBIR: Enterprises Face a Dangerous Vulnerability Glut](https://www.darkreading.com/threat-intelligence/verizon-dbir-enterprises-vulnerability-glut)

---

## 🟡 Data & Privacy

### 7. EU AI法（EU AI Act）、2026年8月2日に完全適用へ―企業対応の最終局面
**2026年6月（継続注目）**


EU AI Actは2026年8月2日に完全効力を持ち、企業には消費者に影響を与えるAI主導の意思決定を説明することが求められる。
また米国のカリフォルニアでは、改訂されたCCPA（カリフォルニア州消費者プライバシー法）規制に基づき、強化されたサイバーセキュリティ対策・正式なリスク評価・自動意思決定技術（ADMT）の透明性の確保が義務化される。
2026年の米国のプライバシー規制環境は、新たな包括的州プライバシー法・既存法の大幅改正・米国プライバシー史上最も積極的な執行という3つの力によって形成されている。


🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

### 8. 米国データプライバシー規制の拡大―約20州が包括的法律を施行、州司法長官が執行前面に
**2026年6月（最新動向）**


2026年時点で、米国のおよそ19州が包括的な消費者プライバシー法を有している。
法律の新規制定ペースは落ち着いているが、データプライバシーリスクは拡大し、州規制当局はデジタルトラッキング技術・健康関連データ・オプトアウト要件・オンライン同意メカニズムを標的に執行を強化している。
監査・リスク評価・開示義務の重複管理が中心的な運営課題となっており、2