I'll search all 5 categories simultaneously to collect the latest security news.
全カテゴリの情報が揃いました。レポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月19日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ShinyHunters** | 医療大手Abbottのがん診断部門（Exact Sciences）を標的とした恐喝グループ。30M行超の患者PII・医療情報の窃取を主張し、業界最注目の脅威アクターとなっている。 |
| 2 | **CMMC Phase II 停止** | 米国防総省が7月13日にCMMC第2フェーズの第三者審査要件を無期限停止。約12万社の防衛関連企業に影響し、コンプライアンス義務そのものは継続中。 |
| 3 | **WordPress RCE（CVE-2026-58644相当）** | WordPressコアに認証不要のリモートコード実行脆弱性が発覚。6.9系・7.0系全サイトが対象となり、強制アップデートで緊急対応済み。 |
| 4 | **AI脆弱性パッチ未適用問題** | AIパッケージを稼働させる企業の81%が既知の脆弱性を保持し、修正可能なアラートの99.9%が未対応のまま（Orca Security調査）。AI基盤のセキュリティ成熟度の遅れが露呈。 |
| 5 | **SEC「Regulation Crypto」規則制定** | 米SECが7月アジェンダに「レギュレーション・クリプト」の規則化を正式掲載。トークン販売のセーフハーバー創設で米国内暗号資産市場の合法的整備が進む見通し。 |

---

## 🔴 Cyber Security

### 1. Abbott（Exact Sciences）、ShinyHuntersによる二重インシデントを調査中
**2026年7月18日**


Abbott Laboratoriesは、がん診断事業における旧Exact Sciences社システムへの不正アクセスと、LabCentralポータルからのデータ窃取主張という2件のサイバーインシデントを調査中。
ShinyHuntersは3000万行超の顧客PII（氏名・メールアドレス・電話番号・生年月日・100万件超のSSN）を窃取したと主張。
同グループはMedtronic・OneMedical・AdaptHealthなど医療テクノロジー企業を連続標的にしており、医療業界への攻撃を激化させている。


🔗 [Abbott Laboratories probes two cyber incidents amid extortion claims](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)

---

### 2. Microsoft SharePoint Server にCVSS 9.8の深刻な脆弱性、CISAがFCEB機関に即時パッチ適用命令
**2026年7月17日**


CISAは、Microsoft SharePoint Serverに影響する新たに修正されたセキュリティ欠陥（CVE-2026-58644、CVSSスコア：9.8）をKnown Exploited Vulnerabilities（KEV）カタログに追加し、連邦機関に対して7月19日までのパッチ適用を義務付けた。これは信頼されていないデータのデシリアライゼーションを可能にするクリティカルな脆弱性。
Microsoftは「ネットワーク経由の攻撃において、サイトオーナー権限以上で認証された攻撃者がSharePointサーバー上で任意コードをリモート実行できる」と警告を発している。


🔗 [The Hacker News – SharePoint CVE-2026-58644 KEV追加](https://thehackernews.com/)

---

### 3. WordPressコアに認証不要のRCE脆弱性、1億超のサイトが危険に
**2026年7月17日**


この脆弱性はコア部分に存在するため、プラグインゼロの標準インストールでも悪用可能。6.9系・7.0系の全サイトが対象となり、WordPressは6.9.5および7.0.2を緊急リリースし、強制アップデート機能で対応した。
Assetnoteの研究者が発見したこの攻撃は「前提条件なしで匿名ユーザーが悪用できる」と説明されており、その危険性の高さが際立っている。


🔗 [The Hacker News – WordPress Pre-auth RCE](https://thehackernews.com/)

---

### 4. 欧州インフラへのサイバー攻撃が急増、イラン系ハッカーも米国を標的に
**2026年7月7日（TechCrunch まとめ）**


欧州の発電所・ダムなどのエネルギー・水道インフラを狙ったサイバー攻撃が相次ぎ、憂慮すべきトレンドを形成している。オープンソースの世界もほぼ毎週のように攻撃を受け、脆弱な標的であり続けている。
また、イスラエルとの紛争を背景に、イラン系ハッカーが米国の重要インフラ、特に基本的なサイバーセキュリティ対策が不十分な民間水道事業者を標的にしているとの警告が出ている。


🔗 [TechCrunch – The Worst Hacks and Breaches of 2026 So Far](https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/)

---

## 🟠 AI Risk

### 5. AIパッケージ稼働企業の81%に既知脆弱性、修正可能な99.9%が未対応
**2026年7月13日**


Orca Securityの「2026 State of AI Security Report」によると、組織はAIをクラウドで構築・展開・運用しているが、速度優先でサイバーセキュリティの基本が犠牲になっていることが多い。AI採用企業の56%がエージェントフレームワークを本番環境に展開しており、AIパッケージを稼働させる企業の81.2%が少なくとも1件の既知の脆弱性を保有し、修正可能なAI脆弱性アラートの99.9%が未対応のままになっている。
AIサービスは新たな認証情報漏洩のカテゴリを生み出しており、APIキーはAIモデルや企業データへのアクセスを可能にする魅力的な標的となっている。AI採用企業の約30%が少なくとも1つのAIキーを安全でない場所に保管している。


🔗 [Help Net Security – 99.9% of fixable AI vulnerabilities remain unpatched](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/)

---

### 6. AI支援ツールによる攻撃：AWSへの侵入からフル環境制圧まで72時間
**2026年7月13日**


Sygniaがサイバー攻撃調査の初期所見を公開。脅威アクターはAI支援ツールを使用し、AWS初期アクセスから環境全体の制圧まで約72時間で完了させた。AIツールにより複数のテクニックとアクセスキーの連鎖が容易になり、エージェント型自動化のリスクが明確に示された。
この事例は、LLM支援型の敵対的自動化の台頭とエンタープライズセキュリティアーキテクチャにおけるAI関連のブラインドスポットの拡大を示す典型例として注目を集めている。


🔗 [Enterprise Times – Security and AI news from the week beginning 6 July 2026](https://www.enterprisetimes.co.uk/2026/07/13/security-and-ai-news-from-the-week-beginning-6-july-2026/)

---

## 🟡 Data & Privacy

### 7. コネチカット州プライバシー法改正施行：LLMへの個人データ利用の開示義務が発動
**2026年7月1日施行**


2026年7月1日、コネチカット州のデータプライバシー法（CTDPA）改正が施行された。この改正により、データ管理者はプライバシーポリシーに、個人データをLLM（ChatGPT・Gemini・DeepSeek・Grokなどの広く知られたモデルを含む）の学習に使用・収集・販売しているかどうかを明確かつ目立つ形で開示することが義務付けられた。
また同改正では、神経データ（neural data）を「機密データ」の定義に含め、高度な保護とオプトイン同意を要求する規定も7月1日より施行されている。


🔗 [Shumaker – The Patchwork of Data Privacy Laws](https://www.shumaker.com/insight/the-patchwork-of-data-privacy-laws-recent-developments-and-implications/)

---

### 8. 米国で州プライバシー法が乱立、19州が包括的法律を施行済み・施行強化へ
**2026年7月（継続トレンド）**


2026年の米国プライバシー規制環境は3つの力によって形成されている：①新たな包括的州法、②既存法の大幅改正、③米国プライバシー史上最も積極的な執行環境。
アーカンソー州では2026年7月に新たなプライバシー法が発効し、未成年者データ、自動化意思決定、データブローカーの透明性への規制関心が高まっている。
連邦レベルの包括的プライバシー法が存在しない中、州レベルの規制が急増・強化される状況が続いており、複数州にまたがる企業にとって継続的なガバナンスが不可欠となっている。

🔗 [Smarsh – U.S. Data Privacy Laws and Regulations in 2026](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

## 🟢 Security Governance

### 9. DoD、CMMC第2フェーズを無期限停止──60日間の改革タスクフォースを発足
**2026年7月13日**


国防総省はCMMCの第三者評価要件のフェーズアップを停止し、CMMCプログラムの包括的な見直しを開始した。7月13日の発表で、国防総省は2026年11月10日に開始予定だった、機密非公開情報（CUI）を含む全契約に対する第三者サイバーセキュリティ評価要件の導入を停止することを表明した。
SBAの試算によれば、中小企業のCMMC認証コストは第三者評価が必要な企業で約59万3,800ドルに達し、Phase IIが予定通り実施されていれば12万社超のDIB中小企業が対応を迫られていたところだった。
なお、
CMMCプログラム自体や防衛受注業者に求められるサイバーセキュリティ要件は廃止されておらず、CUI保護に関する既存の契約義務・サイバーセキュリティ義務は変更なく継続する。


🔗 [Federal News Network – Pentagon suspends CMMC phase two requirements](https://federalnewsnetwork.com/cybersecurity/2026/07/pentagon-suspends-cmmc-phase-two-requirements-launches-review-of-program/)

---

## 🟣 Crypto Currency

### 10. 2026年上半期の暗号資産ハック件数が過去最多207件、総被害額は約10億ドル超
**2026年7月5〜17日（各社レポート集計）**


TRM Labsは2026年上半期に207件のクリプトハックを記録し、これは同社が観測した6か月間の最多件数となった。一方、損失額は9億7200万ドルに留まり、大半が少数の大規模な運用上の侵害に