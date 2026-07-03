# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月4日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Agent Goal Hijack（エージェント目標乗っ取り）** | OWASP Top 10 for Agentic Applications 2026でASI01に選出。外部コンテンツ経由でAIエージェントの目的を書き換える攻撃が最重要リスクに。 |
| 2 | **ゼロクリック・プロンプトインジェクション** | Cursor IDEの「DuneSlide」脆弱性のように、ユーザー操作なしでサンドボックスを脱出しOS権限のコード実行に至る攻撃手法が急増。 |
| 3 | **CISA KEVカタログ即時対応** | SharePointのRCE脆弱性（CVE-2026-45659）がKEV登録後、米政府機関に即日パッチ適用が義務化される事例が続出。 |
| 4 | **脆弱性連鎖型ランサムウェア** | Citrix Bleed 2などの既知脆弱性とRMMツール悪用を組み合わせる手口が、Anubisなどのランサムウェアグループで常態化。 |
| 5 | **秘密鍵盗難による暗号資産ハック** | Humanity Protocol事件のように、管理者権限や秘密鍵の窃取を起点とした大規模な資金流出が引き続き主要な攻撃経路に。 |

---

## 🔴 Cyber Security

### 1. CISA、SharePointの深刻な脆弱性を悪用実績ありとしてKEVカタログに追加
**2026年7月1日**
CISAはMicrosoft SharePoint Serverの深刻な脆弱性CVE-2026-45659（CVSS 8.8）を、既知の悪用が確認された脆弱性（KEV）カタログに追加した。認証済みかつSiteメンバー権限を持つ攻撃者が、デシリアライゼーションの欠陥を悪用してリモートでコードを実行できる。米連邦機関には即日パッチ適用が義務付けられた。

🔗 [SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html)

---

### 2. ServiceNow、未認証APIエンドポイントの欠陥による顧客データ露出を公表
**2026年6月9日**
ServiceNowは、認証を要求しない設定になっていたAPIエンドポイント（/api/now/related_list_edit/create）が悪用され、顧客インスタンスのITチケットや埋め込み認証情報、従業員データが露出したことを公表した。バグ報奨金研究者による責任ある開示が発端とされている。

🔗 [ServiceNow discloses security incident exposing customer data](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/)

---

### 3. テキサス州公園野生生物局、300万人超に影響する委託ベンダー経由の情報漏洩
**2026年6月18日**
狩猟・釣りライセンスシステムを管理する委託ベンダーへの不正アクセスにより、運転免許証情報、パスポート番号、メールアドレス、電話番号、住所などが露出。300万人以上の顧客が影響を受けた可能性がある。社会保障番号や金融情報は含まれていない。

🔗 [Texas Parks & Wildlife Data Breach Affects 3 Million Individuals](https://www.securityweek.com/texas-parks-wildlife-data-breach-affects-3-million-individuals/)

---

### 4. Cursor IDEの「DuneSlide」脆弱性、ゼロクリックでサンドボックスを脱出しRCEに発展
**2026年7月2日**
Cato AI LabsがCursor IDEに2件の深刻な脆弱性（CVE-2026-50548、CVE-2026-50549、CVSS 9.8）「DuneSlide」を発見。MCP経由や検索結果に仕込まれたプロンプトインジェクションにより、ユーザー操作なしでサンドボックスを脱出しOS上で任意コード実行が可能だった。Cursor 3.0で修正済み。

🔗 [Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands](https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html)

---

### 5. Anubisランサムウェア、Citrix Bleed 2を悪用し正規RMMツールで潜伏
**2026年7月2日**
ランサムウェアグループAnubisが、Citrix NetScalerの深刻な脆弱性「Citrix Bleed 2」（CVE-2025-5777、CVSS 9.3）とVPN認証情報窃取、正規のリモート管理ツール（ScreenConnect、Zoho Assistなど）の悪用を組み合わせ、検知を回避しながらデータを暗号化する手口が確認された。6月だけで11件の被害が報告されている。

🔗 [Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials](https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html)

---

## 🟠 AI Risk

### 6. 中国系アクター、AI企業へのスパイ活動を米中AI競争激化の中で拡大
**2026年7月1日**
FBIによると、中国による経済スパイ活動は米経済に年間数千億ドル規模の損害を与えており、AI企業やスタートアップを標的にした人的リスク・内部者リスクが拡大している。AIを活用したソーシャルエンジニアリングの高度化も指摘されている。

🔗 [China-linked actors target more than technology as AI competition with U.S. intensifies](https://www.cnbc.com/2026/07/01/china-ai-cyberattacks-startups-insider-risks-espionage.html)

---

### 7. OWASP、「Agentic Applications向けTop 10（2026年版）」を発表、Agent Goal Hijackを最大リスクに選出
**2026年**
OWASPは自律型AIエージェントを対象とした新セキュリティフレームワークを発表。攻撃者がツール出力や外部文書に悪意ある指示を仕込みエージェントの目的を書き換える「Agent Goal Hijack」を最重要リスク（ASI01）と位置付けた。企業の34%しかAI専用のセキュリティ管理体制を持たないとの調査も報告されている。

🔗 [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

---

## 🟡 Data & Privacy

### 8. コネチカット州CTDPA改正、LLM学習利用の開示義務が2026年7月1日発効
**2026年7月1日**
コネチカット州データプライバシー法（CTDPA）の改正により、個人データがChatGPTやGemini、DeepSeek、Grokなど大規模言語モデルの学習に利用・収集・販売されているかを、事業者はプライバシー通知で明確に開示することが義務付けられた。ユタ州でも訂正権やソーシャルメディアのデータポータビリティ要件が同時期に発効している。

🔗 [2026 Data Security and Privacy Compliance Checklist](https://www.omm.com/insights/alerts-publications/2026-data-security-and-privacy-compliance-checklist-key-us-state-law-updates-ai-rules-coppa-changes-and-global-data-protection-risks/)

---

## 🟢 Security Governance

### 9. 米下院、州法の分断解消を目指す連邦プライバシー法案「SECURE Data Act」を提出
**2026年4月22日**
米下院エネルギー・商業委員会が、乱立する州レベルの消費者プライバシー法を単一の連邦フレームワークに統合する「SECURE Data Act」を提出したことを発表。AIガバナンスやサードパーティリスク管理の要求強化とあわせ、企業のコンプライアンス対応の再設計が求められている。

🔗 [Comprehensive Federal Privacy Bill SECURE Data Act Introduced by House Republicans](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

## 🟣 Crypto Currency

### 10. Humanity Protocol、秘密鍵漏洩により3,100万ドル相当の被害、トークン価格80%超下落
**2026年6月9日**
本人確認基盤プロジェクトHumanity Protocolで、従業員端末経由の秘密鍵漏洩により複数のマルチシグウォレットが侵害され、約3,100万ドル相当の資産が流出。攻撃者はBNBチェーンのブリッジ設定鍵を悪用し無制限にHトークンを新規発行、トークン価格は80%超下落した。内部者による「イグジットスキャム」の可能性を指摘する声もある。

🔗 [Humanity Protocol token crashes more than 80% after a $32 million private-key hack](https://www.coindesk.com/tech/2026/06/09/humanity-protocol-token-crashes-more-than-80-after-a-usd32-million-private-key-hack)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | KEV、SharePoint、ランサムウェア、Citrix Bleed 2、プロンプトインジェクション |
| AI Risk | 🟠🟠 | Agent Goal Hijack、エージェンティックAI、産業スパイ |
| Data & Privacy | 🟡 | CTDPA、LLM学習データ開示、州プライバシー法 |
| Security Governance | 🟢 | SECURE Data Act、連邦プライバシー枠組み |
| Crypto Currency | 🟣 | 秘密鍵漏洩、ブリッジ悪用、DeFiハッキング |

---

*次回配信予定：2026年7月5日（日） | 収集ソース：The Hacker News, BleepingComputer, SecurityWeek, CNBC, OWASP GenAI Security Project, O'Melveny, Clark Hill, CoinDesk*
