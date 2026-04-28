# セキュリティトレンド Top 10 ニュース
**配信日：2026年4月28日（火）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Agentic AI（エージェント型AI）** | 自律的にタスクを実行するAIエージェントが企業ネットワークに急増し、サイバーインシデントの新たな温床となっている。CSAレポートが警鐘を鳴らす。 |
| 2 | **サプライチェーン攻撃** | BitwardenやLMDeployなどの信頼されたOSSライブラリを狙った攻撃が連鎖的に拡大。AIフレームワークも標的に。 |
| 3 | **SECURE Data Act** | 米国下院共和党が提出した連邦レベルの包括的データプライバシー法案。州法の乱立に終止符を打つ可能性がある注目立法。 |
| 4 | **MCP（Model Context Protocol）脆弱性** | AnthropicのAI統合SDKに設計上の欠陥。7,000以上のサーバー・1億5,000万DL超に影響するAIサプライチェーンリスク。 |
| 5 | **COPPA改正コンプライアンス期限** | 2026年4月22日を期限とするFTC改正COPPAルールが発効。子どものプライバシー保護で企業に新たな対応義務。 |

---

## 🔴 Cyber Security

### 1. Bitwarden CLIがサプライチェーン攻撃で侵害 ─ Checkmarxキャンペーンの一環
**2026年4月28日（直近）**


パスワードマネージャーBitwardenのコマンドラインインターフェース（CLI）が、JFrogとSocketの調査によりCheckmarxサプライチェーンキャンペーンの一環として侵害されたことが判明した。
影響を受けたバージョンは`@bitwarden/cli@2026.4.0`で、悪意あるコードがパッケージ内の`bw1.js`ファイルに埋め込まれていた。
開発者・企業のCI/CDパイプラインへの広範な影響が懸念される深刻インシデント。

🔗 [The Hacker News – Bitwarden CLI Supply Chain Compromise](https://thehackernews.com/)

---

### 2. LMDeployのSSRF脆弱性（CVE-2026-33626）─ 公開後13時間以内に実被害
**2026年4月（直近）**


LLM向けオープンソースツールキット「LMDeploy」に高深刻度のSSRF脆弱性（CVE-2026-33626、CVSSスコア7.5）が発見され、公開からわずか13時間以内に実際の攻撃が確認された。
脆弱な`load_image()`関数が任意URLを検証なしに取得し、攻撃者がクラウドメタデータサービスや内部ネットワークにアクセス可能となる。
バージョン0.12.0以前の全ビジョン言語サポート版が影響を受ける。


🔗 [The Hacker News – LMDeploy SSRF Vulnerability](https://thehackernews.com/)

---

### 3. CISA KEVカタログ更新 ─ Microsoft Office Excel RCEなど期限付き対応要求
**2026年4月28日（期限日）**


CISAの既知悪用脆弱性（KEV）カタログに、Microsoft Office ExcelのRCE脆弱性（CVE-2026-32201）が掲載され、2026年4月28日が対応期限に設定された。特別に細工されたExcelファイルを開くことで攻撃者がシステムを完全制御できる。
さらに
JetBrains TeamCityの相対パストラバーサル脆弱性も同カタログに追加され、限定的な管理者操作が実行可能になるリスクがある。


🔗 [CISA – Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### 4. 米国大手銀行2行がサイバー攻撃被害 ─ Citizens Bank・Frost Bankが侵害確認
**2026年4月23日**


米国の主要銀行2行、Citizens BankとFrost Bankがデータ侵害を確認したと報じられた（4月23日）。
また、別のインシデントでは攻撃者がMFAを欠くアカウントへの侵入後、APIキーを悪用して1,858件のネットワーク機器と2,600台以上のデバイスを掌握。12.6GBのデータ（平文認証情報・取引記録・監視カメラアクセスを含む）が流出した。


🔗 [Cybernews – US Banks Breach](https://cybernews.com/)

---

### 5. CPUID公式サイトが侵害 ─ STX RATをCPU-Z・HWMonitorに仕込んで配布
**2026年4月12日**


人気ハードウェアモニタリングツール「CPU-Z」「HWMonitor」などを配布するCPUIDの公式サイトが不明の脅威アクターに侵害され、正規ソフトウェアにリモートアクセス型トロイの木馬「STX RAT」を仕込んだ悪意ある実行ファイルが配布された。インシデントは4月9日15:00 UTCから翌10日10:00 UTCにかけて約19時間継続した。


🔗 [WIU Cybersecurity Center – CPUID Breach](https://www.wiu.edu/cybersecuritycenter/cybernews.php)

---

## 🟠 AI Risk

### 6. AnthropicのMCP SDKに設計上の欠陥 ─ AIサプライチェーン全体に波及するRCEリスク
**2026年4月（直近）**


脆弱性はAnthropicの公式MCP SDKに組み込まれており、Python・TypeScript・Java・Rustなど全サポート言語に影響。7,000以上の公開サーバーと1億5,000万ダウンロード超のソフトウェアパッケージに影響が及ぶ。
LiteLLM・LangChain・LangFlow・Flowise・LettaAI・LangBotなど人気プロジェクトを含む10件の脆弱性が発見された。
Anthropicはプロトコル設計の変更を拒否しており、一部ベンダーがパッチを発行しているものの、開発者がコード実行リスクを引き継ぐ状況が続いている。


🔗 [The Hacker News – Anthropic MCP RCE Vulnerability](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)

---

### 7. CSAレポート：企業の3分の2でAIエージェントがセキュリティインシデントを引き起こす
**2026年4月21日**


Cloud Security Alliance（CSA）がToken Securityと共同で発表したレポート「Autonomous but Not Controlled」（4月21日公開）によると、企業ネットワーク上で制御されていないAIエージェントがデータ露出・業務停止・財務損失などの被害を引き起こしていることが明らかになった。
回答者の68%がAIエージェントの可視性に自信を持つと答えた一方、82%が過去1年間に未知のエージェントを発見した経験があると回答しており、認識と実態の乖離が浮き彫りになっている。


🔗 [Infosecurity Magazine – AI Agents Cause Incidents at Two Thirds of Firms](https://www.infosecurity-magazine.com/news/unchecked-ai-agents-cause/)

---

### 8. AI攻撃ツール化が加速 ─ HiddenLayerが2026年AIスレットランドスケープレポートを公開
**2026年3月（直近参照）**


HiddenLayerの調査によると、エージェント型AIは企業導入の初期段階にあるにもかかわらず、すでにリスクが顕在化しており、企業のAI侵害の8社に1社はエージェントシステムに起因している。
「エージェントがWebブラウジング・コード実行・実世界のワークフロー操作が可能になると、プロンプトインジェクションは単なるモデルの欠陥ではなく、システム侵害への直接経路を持つ運用上のセキュリティリスクになる」と警告している。


🔗 [Business Journal Daily – HiddenLayer 2026 AI Threat Report](https://businessjournaldaily.com/ai-security-company-releases-2026-threat-report/)

---

## 🟡 Data & Privacy

### 9. 米下院共和党が連邦データプライバシー法案「SECURE Data Act」を提出
**2026年4月22日**


2026年4月22日、下院エネルギー商業委員会副委員長のJohn Joyce議員（共和・ペンシルバニア州）が、包括的消費者プライバシー法案HR 8413「SECURE Data Act」を提出。同法案は第119議会における初の包括的連邦消費者プライバシー規制の試みとなる。
連邦規制の不在により、数十の州法が乱立しており、テクノロジー業界は州をまたいだ運用における複雑な規制対応を問題視している。


🔗 [IAPP – SECURE Data Act Analysis](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill)

---

## 🟢 Security Governance

### 10. KPMGが「2026年サイバーセキュリティ考慮事項」レポートを公開 ─ 非人間IDとサプライチェーンリスクがトップ優先事項に
**2026年4月24日**


KPMGのレポートによると、エージェント型AIのセキュリティ業務活用、非人間ID（NHI）の増加、地政学的変化、コンプライアンス要件の複雑化がCISOの役割を拡大させており、サプライチェーンリスク・地政学・非人間IDの管理がトップ優先事項に浮上している。
機械ID・サービスアカウント・AIエージェントが人間ユーザーを凌駕する勢いで増加し、IT/OT/AIの融合が重要インフラ全体のサイバーリスクを高めており、ゼロトラスト型のセキュリティアーキテクチャの必要性が高まっている。


🔗 [Security MEA – KPMG Cybersecurity Priorities 2026](https://securitymea.com/2026/04/24/kpmg-report-eight-critical-cybersecurity-priorities-shaping-2026/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | サプライチェーン攻撃、SSRF、KEV、ランサムウェア |
| AI Risk | 🟠🟠🟠🟠 | MCP脆弱性、AIエージェント、プロンプトインジェクション |
| Data & Privacy | 🟡🟡🟡 | SECURE Data Act、COPPA改正、州法乱立 |
| Security Governance | 🟢🟢🟢 | 非人間ID、KPMG報告、ゼロトラスト |

---

*次回配信予定：2026年4月29日（水） | 収集ソース：The Hacker News、CISA、Cybernews、Infosecurity Magazine、Security MEA、IAPP、Business Journal Daily、WIU Cybersecurity Center、SharkStriker、Morgan Lewis*