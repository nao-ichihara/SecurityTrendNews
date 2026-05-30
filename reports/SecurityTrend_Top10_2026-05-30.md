I'll search all 5 categories simultaneously to collect the latest security news!
収集完了。全カテゴリのデータを分析・選定し、レポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月30日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AIエージェント侵害** | LLMエージェントが侵害後の攻撃活動を自律実行する新手口が観測。CVE-2026-39987を悪用しPostgreSQLのデータを2分以内に窃取する事例が発生 |
| 2 | **ShinyHunters** | Instructure（Canvas）への連続侵害やCharterからの4,200万件超のレコード漏洩など、2026年最も活発な恐喝グループとして猛威を振るう |
| 3 | **Shadow AI / AIガバナンス** | 企業内でのAI利用が個人アカウントや野良ツールに拡散。約半数の企業AIトラフィックが非管理アカウント経由という深刻なガバナンスギャップが顕在化 |
| 4 | **米国プライバシー法ラッシュ** | インディアナ・ケンタッキー・ロードアイランド等の新法が続々施行。SECURE Data Actによる連邦統一法制定の動きも加速 |
| 5 | **クリプト詐欺国家関与** | 北朝鮮・ロシア・イランが暗号資産インフラを制裁回避・資金調達に活用。2025年のAI模倣詐欺は前年比1,400%増という衝撃的な増加率を記録 |

---

## 🔴 Cyber Security

### 1. LLMエージェントが自律的に侵害後攻撃を実行——Marimo脆弱性（CVE-2026-39987）悪用で2分以内にDBを完全窃取
**2026年5月29日**


未知の脅威アクターが大規模言語モデル（LLM）エージェントを利用した侵害後攻撃が観測された。公開されているMarimoネットワークの脆弱性を悪用して初期アクセスを取得後、AWSのシークレットマネージャーからSSH秘密鍵を奪取し、8つのSSHセッションを経由して内部PostgreSQLデータベースに到達した。
 
バスチョンフェーズでは2分以内に内部PostgreSQLデータベースのスキーマと全内容が持ち出された。CVE-2026-39987はMarimo 0.20.4以前の全バージョンに影響するプレ認証RCE脆弱性で、未認証の攻撃者が任意のシステムコマンドを実行できる。


🔗 [An Unknown Threat Actor Used an LLM Agent to Conduct Post-Compromise Actions](https://thehackernews.com/)

---

### 2. Microsoft Patch Tuesday：167件の脆弱性修正——SharePointゼロデイ「CVE-2026-32201」が既に悪用中
**2026年5月27日頃**


Microsoftは167件のセキュリティ脆弱性を修正するアップデートをリリース。SharePoint Serverのゼロデイおよびレッドチームが"BlueHammer"と命名したWindows Defenderの既知の欠陥が含まれる。またGoogle ChromeはChrome 2026年4回目のゼロデイを修正し、Adobe ReaderへのRCEにつながる積極的に悪用されているフローにも緊急アップデートが提供された。
 
Microsoftは攻撃者がCVE-2026-32201（SharePoint Serverにおけるコンテンツ・インターフェース偽装の脆弱性）を既に標的にしていると警告。この脆弱性を使えばフィッシング攻撃や無断のデータ操作、社会工学的攻撃によるさらなる侵害へと悪用される恐れがあるとしている。


🔗 [Microsoft Patch Tuesday: 167 Vulnerabilities Including SharePoint Zero-Day](https://krebsonsecurity.com/)

---

### 3. ShinyHunters、Instructure（Canvas）を8か月間で複数回侵害——学生データ3.5TB窃取後に「データ削除」合意
**2026年5月上旬〜29日**


世界中の大学・カレッジで広く使われるeLearningプラットフォーム「Canvas」を提供するInstructureが、5月初旬のサイバー攻撃でハッカーと「合意」に達したと発表。この合意により3.5テラバイトの学生・大学データの公開を防ぎ、データ削除の「デジタル確認」を受けた。しかし多くのセキュリティ専門家はこの取引をリスクの高いトレードオフとみなしている——データが本当に削除される保証がなく、さらなる攻撃を促す前例になり得るためだ。
 
セキュリティ研究者は、今回の攻撃がここ8か月間でShinyHuntersがInstructureに仕掛けた少なくとも3回目の侵害であると指摘している。


🔗 [Instructure Reached Agreement With ShinyHunters Over Canvas Breach](https://krebsonsecurity.com/)

---

### 4. FortiClient EMS に CVSS 9.1 の認証バイパス脆弱性（CVE-2026-35616）——クレデンシャル窃取マルウェアを大規模配布
**2026年5月28日**


FortiClient EMSの重大なゼロデイ脆弱性を悪用したクレデンシャル窃取マルウェアのキャンペーンが継続。攻撃者は信頼されたエンドポイント管理インフラを悪用してマネージドエンドポイント全体にマルウェアを配布。Fortineのエンドポイント更新に偽装したペイロードをPowerShell経由でサイレント実行した。
 
2026年5月に観測されたこの活動は、CVE-2026-35616（CVSSスコア：9.1）——特権昇格につながるプレ認証APIアクセスバイパス——の悪用を伴う。本件はFortiClient EMS 7.4.7以降で対処済み。


🔗 [Critical FortiClient EMS Vulnerability CVE-2026-35616 Exploited in the Wild](https://thehackernews.com/)

---

## 🟠 AI Risk

### 5. CISAがAI最高責任者不在のまま弱体化——Anthropic「Mythos」によるAI主導の攻撃波に備えられないとの懸念
**2026年5月26日**


元官僚や業界リーダーは、CISA（サイバーセキュリティ・インフラセキュリティ庁）がもはや電力会社や銀行などの重要インフラ事業者がAnthropicの「Mythos」のようなAIモデルによるAI主導の攻撃の波に備えるための支援能力を失っていると懸念している。同機関はAIが最も必要とされる今、歴史的な弱体化に直面している。
 
同機関は昨年チーフAIオフィサーが退任した後に後任を置かず、他機関と異なりMythosへの初期アクセスも付与されなかった。
 
高度なAIモデルは脆弱性を特定・悪用する時間とコストを劇的に削減し、広く使用されているシステムの弱点を同時に発見・標的にする可能性を高める。その結果、サイバーリスクは金融仲介・決済・信頼を混乱させる相関的な障害という形でマクロ金融リスクへと発展しつつある。


🔗 [Trump Hobbled Top Cyber Agency Just as AI Learned to Hack](https://www.axios.com/2026/05/26/cisa-white-house-cybersecurity-ai)

---

### 6. 企業AIリスクレポート2026：「AIパワーユーザー」上位5%が組織全体の露出リスクを集中支配
**2026年5月28日**


LayerX SecurityによるState of AI Usage Report 2026は、エンタープライズAIリスクがユーザーやプラットフォーム全体に均等に分散されていないことを明らかにした。リスクは少数のAIパワーユーザーと、エンタープライズAIアクティビティと機密データ露出の大部分を占む少数の支配的AIプラットフォームに集中している。
 
ほぼ半数の企業AIの会話が、企業管理アカウントではなく個人アカウントを経由して行われていることも判明した。
 
企業ユーザーの約30%がすでに複数のAIプラットフォームを使用しており、上位5%は6つ以上のAIアプリケーションを利用している。


🔗 [New AI Usage Report: Enterprise AI Risk Is Heavily Concentrated Among a Small Group](https://thehackernews.com/2026/05/new-ai-usage-report-enterprise-ai-risk.html)

---

## 🟡 Data & Privacy

### 7. 米下院「SECURE Data Act」提出——州法の乱立に終止符を打つ連邦統一プライバシー法が本格始動
**2026年4月22日〜継続審議中**


SECURE Data Act（消費者権利・データ執行に関する統一規則の確立・保護法）が2026年4月22日に下院エネルギー商業委員会で提出された。現在の州消費者プライバシー法の乱立を単一の全国的なフレームワークに置き換えることを目的とした包括的な連邦プライバシー法案だ。
 
同法はデータブローカーに対する連邦基準も設定し、FTCへの登録と公開開示を義務付ける。しかし最も議論を呼ぶのは州法を上書きするプリエンプション条項だ。
 2026年に入りインディアナ・ケンタッキー・ロードアイランドの3つの包括的州プライバシー法が施行され、
米国では現在約20の州が独自のデータプライバシー規制を導入している。


🔗 [House Introduces SECURE Data Act to Establish Federal Privacy Framework](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

### 8. 23andMeデータ侵害訴訟——カリフォルニア州AG、破産後のChrome Holding Co.を提訴
**2026年5月26日頃**


カリフォルニア州司法長官ロブ・ボンタ氏は、23andMeが昨年3月に破産申請後にリブランドしたChrome Holding Co.に対して訴訟を提起した。
 
ハッカーらは2023年に23andMeのITシステムに5か月間にわたって検知されずに侵入しており、その間に複数の警告サインが見逃されていたとカリフォルニア州司法長官の訴状で主張されている。
 遺伝子情報という極めてセンシティブな個人データを保有する企業の破産と情報流出責任の所在が問われる画期的な訴訟として注目されている。

🔗 [California AG Files Lawsuit Over 23andMe Data Breach](https://www.securityweek.com/)

---

## 🟢 Security Governance

### 9. CMMC Phase 2が2026年11月10日に開始——DoD契約企業に第三者認証（C3PAO）が契約条件に
**2026年5月（継続的報道）**


CMMC（サイバーセキュリティ成熟度モデル認証）Phase 2が2026年11月10日から開始される。32 CFR Part 170に基づき、Phase 2はDoD（米国防総省）が対象となる入札・契約においてレベル2のC3PAO（第三者評価機関認定）資格を契約条件として要求することを可能にする。FCI（連邦契約情報）