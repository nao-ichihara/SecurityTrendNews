# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月24日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AIアシスト型攻撃** | AIがエクスプロイト生成・マルウェア作成を加速。Mandiant M-Trends 2026によると、CVE公開後24時間以内に悪用されるケースが28.3%に達する。 |
| 2 | **サプライチェーン攻撃** | GitHubやLaravel Langなどの開発インフラが標的。ソフトウェアのリリースパイプラインへの侵害が連鎖的被害を生む。 |
| 3 | **Agentic AI（自律型AI）リスク** | AIエージェントが人間の監視なしに機密操作を実行。32%の組織がエージェントの動作を全く可視化できていない。 |
| 4 | **米国プライバシー法の乱立** | 2026年1月にインディアナ・ケンタッキー・ロードアイランドの3州法が発効し、包括的プライバシー法を持つ州が20州に拡大。 |
| 5 | **CMMC Phase 2 / EU AI Act** | 米国防総省のCMMC第2フェーズが2026年11月開始、EU AI Actの透明性規則が2026年8月施行と規制強化が同時進行。 |

---

## 🔴 Cyber Security

### 1. GitHubが内部リポジトリ侵害を調査——3,800件超が流出か
**2026年5月20日（The Hacker News）**


GitHubは、脅威アクターTeamPCPがプラットフォームのソースコードをサイバー犯罪フォーラムで販売リストに掲載したことを受け、内部リポジトリへの不正アクセスを調査中と発表した。
TeamPCPは最低5万ドルで売却を試みており、LAPSUS$グループと共同で9万5,000ドルの販売交渉も行っている。
流出リポジトリにはGitHub Actions、Copilot内部プロジェクト、CodeQLツール、セキュリティツール、CodespacesおよびDependabotが含まれるとされる。


🔗 [GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html)

---

### 2. Cisco Secure WorkloadにCVSS 10.0の最大深刻度脆弱性
**2026年5月21日（The Hacker News）**


CiscoはSecure Workloadに影響する最大深刻度の脆弱性（CVE-2026-20223、CVSSスコア10.0）に対するアップデートを公開した。この脆弱性はREST APIエンドポイントへのアクセスにおける不十分な検証・認証から生じる。
攻撃者が悪用に成功した場合、サイトAdmin権限でテナント境界を越えて機密情報の読み取りや設定変更が可能になる。SaaSおよびオンプレミスのデプロイメント双方に影響し、
ワークアラウンドは存在しない。


🔗 [Cisco Secure Workload CVE-2026-20223 (CVSS 10.0)](https://thehackernews.com/)

---

### 3. CISA、LangflowとTrend Micro Apex OneのCVEをKEVカタログに追加
**2026年5月22日（The Hacker News）**


米CISAは、LangflowおよびTrend Micro Apex Oneに影響する2件の脆弱性を、実際の悪用証拠を根拠に既知悪用脆弱性（KEV）カタログに追加した。
LangflowのCVE-2025-34291（CVSSスコア9.4）は、攻撃者が任意コードを実行してシステムを完全に掌握できるオリジン検証エラー脆弱性だ。
Trend Micro Apex OneのCVE-2026-34926（CVSSスコア6.7）はディレクトリトラバーサル脆弱性であり、事前認証なしのローカル攻撃者がサーバーのキーテーブルを改ざんして悪意あるコードを展開できる。


🔗 [CISA Adds Langflow and Trend Micro Apex One Flaws to KEV Catalog](https://thehackernews.com/)

---

### 4. Laravel Lang組織のリリースパイプラインが侵害——700以上のバージョンに悪意あるタグ
**2026年5月23日（The Hacker News）**


laravel-lang関連パッケージを含む複数パッケージについて、2026年5月22〜23日に大量のタグが数秒間隔で矢継ぎ早に公開されており、単一パッケージの改ざんではなくLaravel Lang組織全体のリリースプロセスが侵害された可能性が指摘されている。
700以上のバージョンが特定されており、攻撃者が組織レベルの認証情報またはリリースインフラへのアクセスを取得した疑いがある。


🔗 [Laravel Lang Supply Chain Compromise — 700+ Malicious Package Versions](https://thehackernews.com/)

---

### 5. 2026年はAIアシスト型攻撃の年——エクスプロイト窓が急速に縮小
**2026年5月初旬（The Hacker News）**


Mandiantの「M-Trends 2026」レポートは、エクスプロイトまでの時間が事実上マイナスになったことを示しており、CVEの28.3%が開示後24時間以内に悪用されている。
深刻度の高いCVEの平均修正日数は現在74日であり、大企業（従業員1,000人以上）における脆弱性の45%は修正されないままとなっている。
AI生成マルウェアは静的解析・シグネチャスキャナを完全にすり抜けており、「脆弱性管理の複雑さとスケールは大半の組織の管理能力を超えている」と指摘されている。


🔗 [2026: The Year of AI-Assisted Attacks](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)

---

## 🟠 AI Risk

### 6. AIが連邦政府の「内部者リスク」に——自律型AIが機密タスクを無監視実行
**2026年5月（Federal News Network）**


2026年、連邦機関は「内部者」という概念の根本的な変容に直面している。AIシステム自体がマシンスピードで機密タスクを実行する「内部者」となっており、機関はインサイダーリスクの再定義を迫られている。
脅威は悪意ある人間のアクターを超え、設定ミスのあるAI・合成ID・非悪意的な行動によるデータ流出リスクにまで拡大している。
悪意あるAIまたは侵害されたAIが人間のアイデンティティ向けガバナンス制御を回避できるリスクが高まっており、フレームワークを更新しなければ、人間の監督者が異常を検知する前にAIが複雑な不正行為を実行してしまう懸念がある。


🔗 [When AI Becomes the Insider: Rethinking Federal Risk in 2026](https://federalnewsnetwork.com/commentary/2026/05/when-ai-becomes-the-insider-rethinking-federal-risk-in-2026/)

---

### 7. 100万件の公開AIサービスをスキャン——AIインフラのセキュリティは「最悪」
**2026年5月（The Hacker News）**


ソフトウェア業界はここ数十年で製品セキュリティを着実に向上させてきたが、AIの急速な普及がその進歩を脅かしている。企業はLLMインフラの自社ホスティングに急速に移行しているが、スピード優先でセキュリティが犠牲になっている。
200万件以上のホストから100万件の公開サービスをスキャンした結果、AIインフラはこれまで調査したソフトウェアの中で最も脆弱で、露出度が高く、設定ミスが多かった。
主な問題として、安全でないデフォルト設定、誤ったDocker構成、ハードコードされた認証情報、rootで動作するアプリケーション、新規インストール時の認証なし管理アクセスなどが繰り返し確認された。


🔗 [We Scanned 1 Million Exposed AI Services. Here's How Bad the Security Actually Is](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)

---

### 8. Agentic AIリスクレポート2026——組織の56%が本番環境でのAIエージェントリスクに直面
**2026年3月（Cybersecurity Insiders）**


AIシステムが自律的に動作するようになっており、多くがセキュリティの視野外のシャドーモードで稼働している。調査によると、56%の組織が実際のAgentic AIリスクにさらされており、うち23%はITが把握していないシャドー展開によるものだ。
過去12ヶ月でAIエージェントによる運用上の問題を経験した組織は37%に達し、8%は停止やデータ破損を引き起こすほど深刻だった。
一方、エージェントが有害な行動を開始した際に完了前に介入できる組織はわずか9%に過ぎない。


🔗 [AI Risk and Readiness Report 2026](https://www.cybersecurity-insiders.com/ai-risk-and-readiness-report-2026/)

---

## 🟡 Data & Privacy

### 9. 米国SECURE Data Act導入——州プライバシー法の乱立に終止符？連邦統一フレームワーク提案
**2026年4月22日（Clark Hill / DLA Piper）**


2026年4月22日、下院エネルギー・商業委員会は「SECURE Data Act」（Securing and Establishing Consumer Uniform Rights and Enforcement Over Data Act）を発表した。これは既存の州消費者プライバシー法の乱立に代わる単一の全国フレームワークを目指す包括的な連邦プライバシー法案だ。
執行権限はFTCおよび州司法長官に限定され、私的訴権はない。違反には書面による通知と少なくとも45日間の是正期間が設けられる。
同法案はデータブローカーに対する公開開示とFTCへの登録を義務付けるが、最も議論を呼ぶ州法の先占条項も含まれる。


🔗 [House Introduces SECURE Data Act to Establish a Federal Privacy Framework](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

## 🟢 Security Governance

### 10. AIガバナンスがデータガバナンスに統合——CMMC Phase 2・EU AI Act・HIPAA執行が同時進行
**2026年5月（Cybersecurity Insiders / Bright Defense）**


2026年ロードマップを持つ組織は100%だが、63%はAIエージェントへの目的制限を適用できず、60%は誤動作したエージェントを迅速に停止できない状況だ。
2026年4月23