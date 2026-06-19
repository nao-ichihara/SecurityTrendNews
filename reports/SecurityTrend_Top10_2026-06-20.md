# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月20日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **RoguePlanet（CVE-2026-50656）** | Microsoft Defender自体のマルウェア検査エンジンに存在するTOCTOU型の権限昇格脆弱性。検出機能が攻撃面になるという逆説的なケースで、パッチ未提供のまま注目を集めている。 |
| 2 | **Icarus（新興恐喝グループ）** | 2026年4月から活動する新興ランサム/恐喝集団。KlueのOAuthトークンを窃取してSalesforceデータを抜き出すサプライチェーン型攻撃を展開し、Huntressなど複数のセキュリティ企業を巻き込んだ。 |
| 3 | **CVE-2026-41940（cPanel/WHM認証バイパス）** | CVSS 9.8の重大な認証バイパス。約150万台のインターネット公開cPanelサーバーに影響し、2月下旬から悪用が続いている。 |
| 4 | **Fable 5 / Mythos 5（AIモデル提供停止）** | 米商務省の指令によりAnthropicが最新モデルへのアクセスを停止。AIモデルのジェイルブレイク手法が国家安全保障上の懸念とされた異例の事例。 |
| 5 | **False Claims Act × サイバー自己評価** | 国防関連企業が虚偽のサイバーセキュリティ自己評価スコアを申告したとして摘発・罰金が相次ぐ。NIST SP 800-171／CMMC対応の実態と申告の食い違いが規制執行の焦点に。 |

---

## 🔴 Cyber Security

### 1. Klue経由のサプライチェーン攻撃でHuntress含む複数企業のSalesforceデータが流出
**2026年6月18日〜19日**
新興恐喝グループ「Icarus」が、営業支援ツールKlueの長期間使われていなかったAPI認証情報を悪用してバックエンドに侵入。OAuthトークンを窃取し、HuntressなどのSalesforce/Gongデータ（商談情報、見積もり、営業メールなど）を抜き出した。Salesforceは影響を抑えるためKlueアプリとの連携を無効化した。

🔗 [Klue OAuth breach linked to 'Icarus' Salesforce data theft attacks](https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/)

---

### 2. cPanel/WHMの認証バイパス（CVE-2026-41940）が約150万台で悪用継続
**2026年4月30日判明、現在も活発に悪用**
CRLFインジェクションによりセッションクッキーの暗号化処理を回避できる重大な脆弱性（CVSS 9.8）。2月23日から悪用が始まっていたとみられ、ホスティング事業者やWeb管理者は至急パッチ適用が必要。

🔗 [CVE-2026-41940 Explained: The cPanel & WHM Authentication Bypass That Hit 1.5M Servers](https://www.picussecurity.com/resource/blog/cve-2026-41940-explained-cpanel-whm-authentication-bypass-hit-1-5m-servers)

---

### 3. Microsoft Defenderにゼロデイ「RoguePlanet」、パッチ未提供
**2026年6月16日公開（CVE-2026-50656）**
Defenderのマルウェア検査エンジン内のTOCTOU（Time-of-Check to Time-of-Use）競合状態を突き、ファイル検査の隙にマルウェアを差し替えて権限昇格を行う。エクスプロイトコードは6月10日にGitHubで公開済み。Microsoftは修正パッチを開発中と表明。

🔗 [Microsoft working on patch for RoguePlanet Defender zero-day](https://www.helpnetsecurity.com/2026/06/17/rogueplanet-zero-day-cve-2026-50656/)

---

### 4. Splunk・AtlassianがAI関連ツールや依存パッケージの脆弱性を一斉修正
**2026年6月18日**
SplunkはAI Toolkit内のOSコマンドインジェクション脆弱性を修正。Atlassianも複数製品でサードパーティ依存パッケージの脆弱性数十件にパッチを適用した。AI機能拡張に伴う攻撃対象領域の拡大が背景にある。

🔗 [Cyber Security News Today - Latest Updates & Research](https://cybernews.com/)

---

### 5. AI支援型サイバー攻撃が急増、ゼロデイ悪用の高速化が顕著
**2026年6月時点の動向**
CrowdStrikeの分析では、AIを活用した攻撃者の攻撃件数が前年比89％増加。脆弱性が攻撃者によってパッチ適用前に悪用されるスピードがこれまでより速まっており、防御側の対応力が追いついていない状況が指摘されている。

🔗 [AI helps speed cybercrime, and other cybersecurity news](https://www.weforum.org/stories/2026/06/ai-cybercrime-and-other-cybersecurity-news/)

---

## 🟠 AI Risk

### 6. 米政府の指令でAnthropicがFable 5・Mythos 5へのアクセスを停止
**2026年6月12日〜13日**
米商務省（Lutnick長官）の指令により、AnthropicはAIモデルFable 5とMythos 5への全アクセスを外国籍ユーザーに対し停止。背景は「ジェイルブレイク」手法の発見とされるが、Anthropicは既知の軽微な脆弱性に過ぎず過剰反応だと反論している。業界全体のモデル提供姿勢に影響を与える可能性がある異例の規制介入。

🔗 [Anthropic suspends all access to Mythos model after US government bans foreign nationals use](https://www.cnn.com/2026/06/13/business/anthropic-mythos-model-national-security)

---

### 7. CISAがAIを踏まえ「最高リスク」脆弱性へのパッチ対応を優先する指令を発表
**2026年6月**
新型AIモデルが脆弱性の発見・悪用を加速させているとの分析を踏まえ、CISAは連邦機関に対し最高リスクの脆弱性へパッチ適用を集中させる指令を発出。AIが攻守両面のスピードを変えている現状を象徴する動き。

🔗 [AI directive focuses patching efforts on 'highest risk' vulnerabilities](https://federalnewsnetwork.com/cybersecurity/2026/06/ai-directive-focuses-patching-efforts-on-highest-risk-vulnerabilities/)

---

## 🟡 Data & Privacy

### 8. 米国で新たな州データプライバシー法が続々施行、EU AI Actも8月に全面適用へ
**2026年内施行**
インディアナ州・ケンタッキー州・ロードアイランド州で新たな包括的データプライバシー法が施行予定。カリフォルニア・コロラド・コネチカット・オレゴン・ユタの各州も既存法を改正し、自動意思決定技術（ADMT）の透明性強化やリスクアセスメント義務化が進む。EUでは2026年8月2日にAI Actが原則全面適用となる。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. 国防関連企業LOGZONE、虚偽のサイバー自己評価で50万ドル超の和解金
**2026年6月18日**
LOGZONE社は2021年に自己評価スコア「110点（満点）」を提出していたが、2024年のDIBCAC審査で実際は「マイナス170点」と判明。NIST SP 800-171対応を欠いたまま政府契約の支払いを受けていたとして、虚偽請求防止法（False Claims Act）に基づき507,144ドルの支払いで和解した。サイバー自己申告と実態の齟齬に対する執行強化の一例。

🔗 [Defense contractor settles cybersecurity False Claims Act allegations](https://defensescoop.com/2026/06/18/defense-contractor-settles-cybersecurity-false-claims-act-allegations/)

---

## 🟣 Crypto Currency

### 10. 暗号資産業界のハッキング被害額が大幅減少、一方でUSB経由のウォレット狙いマルウェアも発見
**2026年2月時点データ／2026年6月報告**
2026年2月の暗号資産業界の被害額は15件・約2,650万ドルで、前年同期比98.2％減と大幅改善。ブリッジ攻撃の比率も2022年の73％から2025年は3％に低下するなど、業界全体の防御強化が進む。一方Microsoftは、USBメモリ経由で拡散し暗号資産ウォレットを乗っ取るマルウェアを発見しており、新たな攻撃ベクトルへの警戒も必要。

🔗 [If You Want to Secure Your Crypto in 2026, Do This](https://www.ibtimes.com/if-you-want-secure-your-crypto-2026-do-this-3803841)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | Icarus, RoguePlanet, CVE-2026-41940, サプライチェーン攻撃 |
| AI Risk | 🟠🟠 | Fable 5/Mythos 5, CISA AI指令, AI支援型攻撃 |
| Data & Privacy | 🟡 | 州プライバシー法, EU AI Act, ADMT |
| Security Governance | 🟢 | False Claims Act, NIST SP 800-171, CMMC |
| Crypto Currency | 🟣 | DeFi被害減少, ウォレット狙いマルウェア |

---

*次回配信予定：2026年6月21日（日） | 収集ソース：BleepingComputer、Help Net Security、The Hacker News、SecurityWeek、Picus Security、CNN、DefenseScoop、WEF、Gunster、IBTimes ほか*
