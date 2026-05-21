# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月21日（木）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **サプライチェーン攻撃** | 
第三者関与の侵害が60%増加し、全侵害の48%を占めるまでに拡大。
ソフトウェアやnpmパッケージを経由した攻撃が相次いでいる。 |
| 2 | **AIによる脆弱性悪用加速** | 
AIが脅威アクターによって既知の脆弱性の悪用時間を短縮し、防御のウィンドウが数ヶ月から数時間に縮小している。
 |
| 3 | **Shadow AI（シャドーAI）** | 
未承認のAIツールを職場で使用する従業員が増加し、シャドーAIはデータ漏洩関連の第3位のリスク活動に。使用率は1年で15%から45%に急増している。
 |
| 4 | **SECURE Data Act** | 
2026年4月22日、下院エネルギー・商業委員会が、現在の州ごとのプライバシー法の乱立を単一の国家フレームワークに置き換えることを目的とした包括的連邦プライバシー法案を提出した。
 |
| 5 | **AIガバナンスギャップ** | 
調査によれば、100%の組織が2026年のロードマップにAIを盛り込んでいる一方、63%はAIエージェントへの目的制限を強制できず、60%は誤動作するAIを迅速に停止できない。
 |

---

## 🔴 Cyber Security

### 1. GitHub内部リポジトリ侵害 — 3,800件超が流出、従業員デバイス経由の攻撃
**2026年5月20日**


GitHubは、悪意のあるVisual Studio Code拡張機能を通じて従業員デバイスが侵害され、内部リポジトリへの不正アクセスが確認されたことを公式に発表した。Microsoftが所有するこのプラットフォームは、拡張機能の毒入れによって従業員のエンドポイントが侵害されたと説明した。
 
脅威アクターTeamPCPがGitHubのソースコードをサイバー犯罪フォーラムに売りに出しており、LAPSUS$グループとの共同売却価格は95,000ドルとされている。
 
漏洩したリポジトリにはGitHub Actions、Copilot関連プロジェクト、CodeQLツール、内部インフラなどが含まれるとされる。


🔗 [GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html)

---

### 2. Verizon DBIR 2026：脆弱性悪用が19年間で初めて盗用認証情報を抜きトップに
**2026年5月19日**


脆弱性の悪用が、攻撃者がターゲットネットワークへの初期アクセスを得る最も一般的な手法として盗用認証情報を超えた。DBIRの19年の歴史で初めて認証情報の盗用がトップから陥落した。
 
ランサムウェアは全侵害の48%に増加（前年比44%）。一方で被害者の69%は身代金を支払っておらず、支払額は減少傾向にある。


🔗 [Verizon DBIR: Vulnerability exploitation is the dominant initial access vector](https://www.helpnetsecurity.com/2026/05/20/verizon-2026-dbir-findings/)

---

### 3. Cisco SD-WAN ゼロデイ (CVE-2026-20182)：2026年で6件目の悪用済み脆弱性
**2026年5月15日頃**


Ciscoはまた別のSD-WANのクリティカルなゼロデイ脆弱性にパッチを適用した。これは2026年に悪用が判明した6件目のSD-WANの欠陥である。このゼロデイ(CVE-2026-20182)は、高度な脅威アクターUAT-8616による標的型攻撃で悪用された。
 
この脆弱性は認証バイパスの脆弱性として説明されており、リモートの攻撃者が特別に細工されたパケットを通じて対象システム上の管理者権限を取得できる。
 
CISAはCVE-2026-20182をKEVカタログに追加し、連邦機関に3日以内の対応を指示した。


🔗 [Cisco Patches Another SD-WAN Zero-Day, the Sixth Exploited in 2026](https://www.securityweek.com/cisco-patches-another-sd-wan-zero-day-the-sixth-exploited-in-2026/)

---

### 4. Webworm（中国系）がDiscord・MS Graph APIを悪用した新型バックドアを展開
**2026年5月20日**


サイバーセキュリティ研究者は、中国と関連する脅威アクター「Webworm」による新たな活動を確認した。Discord及びMicrosoft Graph APIをC2通信に利用するカスタムバックドアを展開している。Webwormは少なくとも2022年から活動し、政府機関を標的にしていると評価されている。
 今回新たに「EchoCreep」「GraphWorm」という2種のバックドアが使用されたことが判明した。

🔗 [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://www.wiu.edu/cybersecuritycenter/cybernews.php)

---

### 5. NGINX CVE-2026-42945 (CVSS 9.2) がワイルドで悪用、RCEリスク
**2026年5月17日**


NGINX PlusおよびNGINX Openに影響を与える新たなセキュリティ欠陥が、公開からわずか数日で実際に悪用されていることが確認された。CVE-2026-42945（CVSSスコア：9.2）として追跡されるこの脆弱性は、NGINXバージョン0.6.27から1.30.0に影響するヒープバッファオーバーフローである。


🔗 [NGINX CVE-2026-42945 Exploited in the Wild, Causing Worker Crashes and Possible RCE](https://www.wiu.edu/cybersecuritycenter/cybernews.php)

---

## 🟠 AI Risk

### 6. Verizon DBIR 2026：AIが防御ウィンドウを「数ヶ月から数時間」に縮小
**2026年5月19日**


DBIRは、AIが加速させるソフトウェアの欠陥識別への増大するパッチ対応、「セキュア・バイ・デザイン」フレームワークへのAI統合、そして総攻撃面を最小化するための防御的AI活用など、今日のAI環境を踏まえた勧告を提供している。このレポートは2025年データを使用しているが、傾向は明確でありAIはサイバーセキュリティ業界を根本的に再形成している。
 
CrowdStrikeの今年初めのグローバル脅威レポートでは、2025年に「AIを活用した攻撃者が前年比89%増加した」と記録されている。


🔗 [Verizon's 2026 Breach Report: AI Shrinks Defense Time to Hours](https://www.technology.org/2026/05/20/verizon-dbir-2026-ai-vulnerability-breaches/)

---

### 7. Proofpoint調査：世界の組織の半数がAIセキュリティ管理があるにも関わらずAIインシデントを経験
**2026年4月28日**


Proofpointの「2026 AI and Human Risk Landscape」レポートの主要な知見によると、AIの導入はガバナンスフレームワークの成熟より速く進んでいる。87%の組織がAIアシスタントをパイロット段階を超えて展開しているが、半数以上がセキュリティ対応を「追いついていない、一貫性がない、または後手に回っている」と認識している。
 
42%がAI関連のインシデントを経験済みと報告しており、実運用環境でのリスクはすでに顕在化している。


🔗 [Proofpoint Research Reveals Half of Global Organizations Experienced AI Incidents](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-reveals-half-global-organizations-experienced-ai)

---

### 8. IMF警告：AIが金融システムへのサイバー攻撃を加速、マクロ金融ショックのリスク
**2026年5月7日**


高度なAIモデルは、脆弱性の特定と悪用に必要な時間とコストを劇的に削減し、広く使用されているシステムの欠陥を同時に発見・標的化する可能性を高めている。その結果、サイバーリスクは金融仲介、決済、信頼をシステムレベルで混乱させる可能性のある相関的障害の問題になりつつある。
 
AIは単一の脆弱性が多くの機関に波及するリスク集中をさらに高める恐れがある。少数のソフトウェアプラットフォームやクラウドプロバイダーへの依存が単一の悪用された脆弱性の影響を増大させ、潜在的なマクロ金融ショックへのリスクを高めている。


🔗 [Financial Stability Risks Mount as Artificial Intelligence Fuels Cyberattacks](https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks)

---

## 🟡 Data & Privacy

### 9. SECURE Data Act：連邦プライバシー統一法案を下院提出、州法の"上書き"で波紋
**2026年4月22日（継続審議中）**


2026年4月22日、下院エネルギー・商業委員会は「SECURE Data Act」を提出した。現在のバラバラな州のプライバシー法を単一の国家フレームワークに置き換えることを目的とした包括的な連邦プライバシー提案である。この法案の重要性は、それが創出する権利よりも規制の景観をどう再構築するかにある。
 
この法案は数百にわたる州のプライバシー保護を無効化する可能性があり、消費者が自らの権利を守るための訴訟を提起すること（プライベート・ライト・オブ・アクション）を認めない点が最大の問題として挙げられている。


🔗 [The SECURE Data Act is Not a Serious Piece of Privacy Legislation | EFF](https://www.eff.org/deeplinks/2026/05/secure-data-act-not-serious-piece-privacy-legislation)

---

## 🟢 Security Governance

### 10. AIガバナンスがデータガバナンスと一体化：「ガバナンスvs封じ込めギャップ」の現実
**2026年5月21日**


調査データは深刻な実態を明らかにしている。100%の組織がAIをロードマップに組み込んでいる一方で、63%はAIエージェントへの目的制限を強制できず、60%は誤動作するAIを迅速に停止させられない。
 
組織はAIの行動を監視することには投資してきたが、停止させることには投資してこなかった。目的拘束、キルスイッチ、ネットワーク分離などの封じ込め制御は、監視制御より