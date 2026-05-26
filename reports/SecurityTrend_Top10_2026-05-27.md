# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月27日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AI支援型攻撃（AI-Assisted Attack）** | 生成AIを活用して脆弱性探索・フィッシング・マルウェア生成を自動化する攻撃手法が急増。2026年を象徴するサイバー脅威トレンドとしてセキュリティ業界が警戒を強めている。 |
| 2 | **サプライチェーン攻撃（Supply Chain Attack）** | DAEMON Tools・Notepad++・CPUIDなど正規ソフトウェアインストーラへのマルウェア埋め込みが続発。100カ国以上に被害が及ぶ大規模キャンペーンに発展している。 |
| 3 | **ランサムウェア（Ransomware）** | GitHub・Foxconn・Instructureなど大企業を標的にした攻撃が激化。ShinyHunters・TeamPCP・Nitrogenなど新興グループが台頭し、データ窃取と二重脅迫型攻撃を組み合わせている。 |
| 4 | **ゼロデイ脆弱性（Zero-Day Vulnerability）** | Microsoft Exchange・SharePoint・NGINXなど広く使われるプラットフォームのゼロデイが相次いで実環境で悪用されている。CVSS 9.0以上の致命的なものが複数公開された。 |
| 5 | **ディープフェイク・ソーシャルエンジニアリング** | 幹部の音声・映像を模倣するディープフェイクが組織への不正アクセスや詐欺に悪用。2026年末までに最も一般的なソーシャルエンジニアリング手法になると予測されている。 |

---

## 🔴 Cyber Security

### 1. Canvas教育プラットフォーム大規模侵害：2億7500万人分のデータ流出危機
**2026年5月**
ShinyHuntersグループによるInstructure（Canvas LMS）への攻撃が深刻化。米国中の学校・大学約9,000機関の学生・教職員2億7500万人分のデータ流出が脅かされている。同グループは過去8カ月で少なくとも3回の侵害を実行しており、今回は段階的エスカレーションの一環とみられる。

🔗 [May 2026 Data Breaches: List Major Incidents & Latest Updates - SharkStriker](https://sharkstriker.com/blog/may-2026-data-breaches/)

---

### 2. GitHub社内リポジトリ3,800件が流出：TeamPCPによる攻撃
**2026年5月**
GitHubは社員デバイスへの侵入を通じた内部リポジトリ約3,800件の漏えいを公式確認した。攻撃の起点は悪意ある VS Code 拡張機能であり、サイバー犯罪グループ「TeamPCP」が実行した。ソフトウェア開発インフラへの攻撃という性質上、サプライチェーンリスクへの警戒が高まっている。

🔗 [GitHub Confirms Hack Impacting 3,800 Internal Repositories - SecurityWeek](https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/)

---

### 3. Foxconn北米拠点にランサムウェア攻撃：8TB・1,100万ファイル流出
**2026年5月**
台湾の電子機器大手Foxconnの北米拠点がNitrogenランサムウェアグループの攻撃を受け、8TB超・約1,100万件のファイルが窃取された。流出データには機密情報、内部プロジェクト文書、技術図面などが含まれており、製造業のサイバーセキュリティ脆弱性が改めて浮き彫りになった。

🔗 [Supply Chain Attacks, AI Security, and Major Breaches Define This Week in Cybersecurity in May 2026 - eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)

---

### 4. Microsoft Exchange Server ゼロデイ（CVE-2026-42897）が実環境で悪用
**2026年5月**
オンプレミス版Microsoft Exchange Serverに深刻な脆弱性（CVE-2026-42897、CVSSスコア：8.1）が開示され、すでに実環境での悪用が確認されている。また同時期にSharePointのゼロデイ（CVE-2026-32201）も発見・悪用が進行中。企業は緊急パッチ適用が求められている。

🔗 [On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email - The Hacker News](https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html)

---

### 5. DAEMON Toolsサプライチェーン攻撃：正規インストーラにマルウェア混入
**2026年5月**
人気の仮想ドライブソフト「DAEMON Tools」の公式インストーラがマルウェアに汚染されるサプライチェーン攻撃が発生。100カ国以上の数千件の感染試行が観測された。2026年前半だけでeScan・Notepad++・CPUIDなど複数の著名ソフトが同様の被害を受けており、ソフトウェア配布経路そのものへの信頼が問われている。

🔗 [DAEMON Tools Supply Chain Attack Compromises Official Installers with Malware - The Hacker News](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html)

---

## 🟠 AI Risk

### 6. 2026年：AI支援型攻撃の元年——脆弱性悪用が認証情報窃取を上回る
**2026年5月**
Verizon DBIRの最新版が、脆弱性悪用が初めて認証情報窃取を上回りインシデント起因の首位（31%）に立ったことを発表。生成AIによる攻撃自動化とサードパーティリスクの拡大が背景にあり、特に中小企業がランサムウェアの標的として急増している。組織の6件に1件の侵害にAIが関与しているとも報告されている。

🔗 [2026: The Year of AI-Assisted Attacks - The Hacker News](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
🔗 [AI-Driven Threats, Critical Vulnerabilities, and Supply Chain Breaches Define the Week in May 2026 - eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/ai-driven-threats-critical-vulnerabilities-and-supply-chain-breaches-define-the-week-in-may-2026/)

---

### 7. IMFが警告：AIがサイバー攻撃を増幅し金融システムを脅かす
**2026年5月**
IMFが、AIが防御側より攻撃側の能力を加速的に強化しているとする分析を公開。脆弱性の特定・悪用コストが劇的に低下し、複数の広く使われるシステムを同時に標的にするリスクが高まっている。AI技術の普及は金融安定性への脅威になりうるとして国際的な規制連携を訴えた。

🔗 [Financial Stability Risks Mount as Artificial Intelligence Fuels Cyberattacks - IMF](https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks)

---

### 8. AI自体が「内部脅威」に：連邦政府でのリスク再考
**2026年5月**
米連邦ニュースネットワークが、AIシステムそのものがマシンスピードで機密タスクを実行する「インサイダー脅威」化していると警告。ディープフェイクによる本人偽装やAI駆動のソーシャルエンジニアリングが高度化し、連邦職員が不正アクセスを許可させられるリスクが急上昇している。

🔗 [When AI becomes the insider: Rethinking federal risk in 2026 - Federal News Network](https://federalnewsnetwork.com/commentary/2026/05/when-ai-becomes-the-insider-rethinking-federal-risk-in-2026/)

---

## 🟡 Data & Privacy

### 9. GDPR施行10周年：EUがデータ削除権（忘れられる権利）の執行を最優先に
**2026年5月**
GDPR施行10年を迎え、欧州データ保護委員会（EDPB）が2026年の執行重点として第17条「忘れられる権利（削除権）」を指定した。累積制裁金は71億ユーロを超え、2025年だけで約12億ユーロが科された。また欧州委員会のDigital Omnibus提案により、中小企業向けのコンプライアンス簡素化が図られる見込みだが、個人の権利は維持される。

🔗 [Marking 10 years of the GDPR: the evolution of the European data protection landscape - EDPB](https://www.edpb.europa.eu/news/news/2026/marking-10-years-gdpr-evolution-european-data-protection-landscape_en)
🔗 [Data Privacy in 2026: How GDPR Compliance Landscape is Evolving - TJC Group](https://www.tjc-group.com/blogs/data-privacy-in-2026-how-gdpr-compliance-landscape-is-evolving/)

---

## 🟢 Security Governance

### 10. NISTがAIセキュリティフレームワーク整備を加速：CSF 2.0 + AI Cyber Profile
**2026年5月**
NISTは政府機関向けにNIST 800-53の全制御をレビューし、AIシステム保護に特化したオーバーレイ策定を進めている。Cybersecurity Framework（CSF）2.0をベースにした「Cyber AI Profile」は、AIがもたらすリスクと機会を体系化する指針として注目される。DORA（EU）やCMMC拡大（米）など国際的な規制強化とともに、継続的なセキュリティ検証が求められる時代が到来している。

🔗 [Here's how NIST is teeing up guidance for securing AI - Federal News Network](https://federalnewsnetwork.com/federal-insights/2026/05/heres-how-nist-is-teeing-up-guidance-for-securing-ai/)
🔗 [NIST Publishes Preliminary Draft of Cybersecurity Framework Profile for AI - Global Policy Watch](https://www.globalpolicywatch.com/2026/01/nist-publishes-preliminary-draft-of-cybersecurity-framework-profile-for-artificial-intelligence-for-public-comment/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | ランサムウェア、ゼロデイ、サプライチェーン、GitHub漏洩 |
| AI Risk | 🟠🟠🟠🟠 | AI支援型攻撃、ディープフェイク、脆弱性悪用増加 |
| Data & Privacy | 🟡🟡🟡 | GDPR10周年、忘れられる権利、EU AI Act |
| Security Governance | 🟢🟢🟢 | NIST CSF 2.0、DORA、CMMC、AI Cyber Profile |

---

*次回配信予定：2026年5月28日（木） | 収集ソース：The Hacker News、SecurityWeek、eSecurity Planet、SharkStriker、IMF Blog、Federal News Network、EDPB、GlobalPolicyWatch、Verizon DBIR*
