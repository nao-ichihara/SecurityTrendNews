I'll search all 5 categories simultaneously to collect the latest security news!
収集完了。各カテゴリのデータを分析・選定してレポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月21日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **FortiBleed** | ロシア語圏の脅威アクターによるFortinetファイアウォール大規模侵害キャンペーン。194カ国・86,000台超が被害を受けた前代未聞のグローバル規模の攻撃。 |
| 2 | **AIフロンティアモデル規制** | ホワイトハウスが署名したAIセキュリティ大統領令で、政府がリリース前30日間にわたりフロンティアAIモデルの評価を行う任意枠組みを構築。 |
| 3 | **ShinyHunters** | Oracle PeopleSoftのゼロデイ（CVE-2026-35273）を悪用し、世界100以上の組織・大学を標的にした恐喝グループ。Salesforce/Klue経由の侵害にも関与。 |
| 4 | **北朝鮮DPRKクリプト窃盗** | 2025年に約20億ドル相当の仮想通貨を窃取し、全サービス侵害の76%を占めるとされる国家支援グループ。2026年も継続的に脅威。 |
| 5 | **米国州プライバシー法ラッシュ** | インディアナ、ケンタッキー、ロードアイランドで2026年1月1日から包括的プライバシー法が施行。米国の包括的プライバシー法保有州が計20州に拡大。 |

---

## 🔴 Cyber Security

### 1. FortiBleed：Fortinet大規模侵害キャンペーン — 194カ国8.6万台超が被害
**2026年6月17〜19日**


「FortiBleed」と命名されたサイバースパイキャンペーンが、194カ国にわたり73,932件以上のFortinetファイアウォールURLを静かに侵害した。
脅威アクターは32万台超のFortiGateターゲットに対して推定11.6億回のクレデンシャルベース攻撃を実行し、さらに16万台超のMSSQLサーバーに21億回のブルートフォース攻撃を行い、21,632件のユニークドメインを侵害した。
CISAはFortinet顧客に対してFortiGateデバイスの即時保護措置を求める緊急勧告を発令。この大規模キャンペーンはロシア語圏の脅威アクターによるものとされている。


🔗 [FortiBleed - 70,000+ Fortinet Firewalls Compromised in Massive Exploitation Attack](https://cybersecuritynews.com/fortibleed-fortinet-firewalls-compromised/)

---

### 2. Salesforce/Klue インシデント：恐喝グループIcarusが顧客データを侵害
**2026年6月19日**


Salesforceはセキュリティインシデントを受けてKlue Battlecardsアプリの連携を無効化したと発表した。Salesforceは今週公開したアラートで、アプリ経由で顧客データへの不正アクセスが発生した可能性があることを認めた。
恐喝グループ「Icarus」がKlueの顧客データを侵害・流出させており、被害にはサイバーセキュリティ企業HuntressやRecorded Futureも含まれる。
Salesforceプラットフォーム自体の脆弱性ではなく、サードパーティのアプリ連携経由という点で、サプライチェーンリスクの深刻さを改めて示す事例となった。

🔗 [The Hacker News - Klue/Salesforce Security Incident](https://thehackernews.com/)

---

### 3. ShinyHunters、Oracle PeopleSoftゼロデイ悪用（CVE-2026-35273）で100以上の大学・組織を侵害
**2026年6月11〜12日**


ShinyHuntersの恐喝グループは、Oracle PeopleSoftの未パッチ脆弱性を悪用して企業システムに侵入しデータを窃取。このキャンペーンは大学を最も多く標的とし、GoogleのMandiantはこの活動をUNC6240として追跡、5月27日〜6月9日の間の活動と特定している。
Mandiantおよびグーグル脅威インテリジェンスグループの研究者によれば、ShinyHuntersは世界100以上の組織を侵害し、大学・高等教育機関が確認済み標的の大多数を占める恐喝キャンペーンを実施した。


🔗 [WIU CyberNews - ShinyHunters Exploits Oracle PeopleSoft Zero-Day](https://www.wiu.edu/cybersecuritycenter/cybernews.php)

---

### 4. Microsoft DefenderのPoC公開：SYSTEMコマンドプロンプトを起動可能なレースコンディション脆弱性
**2026年6月19日**


公開されたPoC（実証コード）は、Microsoft Defenderのレースコンディションを悪用してSYSTEM権限のコマンドプロンプトを起動するものだ。
CISAは連邦機関に対して、未認証リモートコード実行が可能な CVE-2026-20253 を3日以内にパッチするよう指示した。
エンドポイントセキュリティ製品そのものに権限昇格の弱点があることが露呈した形で、パッチ適用の優先度が特に高い案件として注目される。

🔗 [SecurityWeek - Microsoft Defender PoC / CVE-2026-20253](https://www.securityweek.com/)

---

## 🟠 AI Risk

### 5. ホワイトハウス「AIイノベーションとセキュリティの推進」大統領令：フロンティアモデル事前評価の任意枠組みを構築
**2026年6月2日署名**


2026年6月2日、ホワイトハウスは「AIイノベーションとセキュリティの推進」と題した大統領令を発令。米国のAIリーダーシップ推進と、高度化するAIシステムに伴う安全保障リスクへの対処が目的で、①政府・民間のサイバー防御強化、②フロンティアAIモデルの安全な開発・公開のための任意ベンチマーク・審査枠組みの構築、という2つのアプローチを概説している。
この大統領令は、Anthropic Claude Mythosモデルがサイバー脆弱性の特定・悪用において人間を大幅に凌駕する能力を示したことを受けて発出された。


🔗 [White House EO - Promoting Advanced AI Innovation and Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

---

### 6. 国際AIセーフティレポート2026：能力向上が新たな攻撃経路を拡大、AIサイバー作戦利用の証拠も
**2026年6月（最新レポート）**


サイバーリスクはAI自律性リスクの中心に位置する。同レポートは実際のサイバー作戦でAIが使用されているという強化された証拠を示しており、サイバーベンチマークでの急速な性能向上も指摘している。防御側はスピードを得る一方、攻撃側は規模を得るという「デュアルシグナル」として捉えるべきだと強調している。
プロンプトインジェクションの成功率が主要リリース全体で依然として高い水準にあり、ツール利用型AIエージェントは新たな攻撃対象領域を生み出している。


🔗 [The Hill - AI Safety Report 2026 Highlights](https://thehill.com/opinion/technology/5924895-ai-safety-report-2026-highlights/)

---

## 🟡 Data & Privacy

### 7. 米国プライバシー規制ラッシュ：20州が包括的プライバシー法を保有、FTC・州AG執行が激化
**2026年6月（継続トレンド）**


インディアナ、ケンタッキー、ロードアイランドの包括的プライバシー法が2026年1月1日に施行され、包括的消費者プライバシー法を持つ州の総数が20州に達した。
2026年4月にはハウス共和党が「SECURE Data Act」を提出。連邦レベルで消費者のアクセス権・削除権・特定処理のオプトアウト権を確立し、州法を先取りする内容だが、
米国のプライバシー規制環境は2026年に、①新たな包括的州法、②既存法の大幅改正、③米国史上最も攻撃的な執行状況、の3つの力によって形成されている。


🔗 [Morgan Lewis - Hot Privacy and Data Security Issues on the Hill for 2026](https://www.morganlewis.com/pubs/2026/06/hot-privacy-and-data-security-issues-on-the-hill-for-2026)

---

### 8. EU AI法、2026年8月2日に完全適用開始：AI意思決定の説明義務が企業に課される
**2026年6月〜8月（予定）**


EU AI法は2026年8月2日に完全施行され、企業は消費者に影響するAI主導の意思決定を説明することが義務付けられる。この法律は欧州委員会のデジタルオムニバス規制提案によって大幅な変更を受ける可能性があり、組織は透明性・ガバナンス・容認できないリスクを巡る不確実性と監視強化に備えるべきだ。
このAI法の完全適用（一部高リスク製品については2027年まで延長）は、AI利活用において企業の法的・コンプライアンス負担を大幅に増大させる。


🔗 [Complete Discovery Source - Global Data Privacy Laws 2026](https://cdslegal.com/insights/global-data-privacy-laws-the-current-environment-and-what-to-look-for-in-2026/)

---

## 🟢 Security Governance

### 9. トランプ大統領、国家安全保障システムのサイバーガバナンス覚書に署名：NSAを国家管理者に指定
**2026年6月12日**


トランプ大統領は6月12日、連邦機関が使用する国家安全保障システムに関するサイバーセキュリティガバナンス覚書に署名。この覚書は「国家安全保障システム委員会（CNSS）」を再設立し、NSA長官を国家管理者として任命するもので、国家管理者は新興脅威の特定、CINSSへの助言、緊急指令の発令を担う。
さらに、CMMC（サイバーセキュリティ成熟度モデル認証）Phase 2が2026年11月10日より開始予定で、多くのDoD請負業者に対してサードパーティ認証が契約受注条件となる。


🔗 [AHA News - Administration releases memo on cybersecurity governance for national security systems](https://www.aha.org/news/headline/2026-06-15-administration-releases-memo-cybersecurity-governance-national-security-systems)

---

## 🟣 Crypto Currency

### 10a. 米議会、「連邦仮想通貨窃盗執行・調整法案」提出：DOJ主導のクリプトハック対策タスクフォース設立へ
**2026年6月11日**


2026年6月11日、米国下院議員2名が「連邦仮想通貨窃盗執行・調整法（Federal Cryptocurrency Theft Enforcement and Coordination Act）」を提出。政府横断的なタスクフォースを設置し、暗号資産ハック・悪用・詐欺の