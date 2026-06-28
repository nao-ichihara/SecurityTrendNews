# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月29日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ShinyHunters / Oracle PeopleSoftゼロデイ** | 恐喝集団ShinyHuntersがPeopleSoftの未修正RCE（CVE-2026-35273）を悪用し、100以上の組織（多くが大学）から学生記録を窃取。 |
| 2 | **AI悪用型サイバー攻撃の加速** | Five Eyes（米英加豪NZ）が、AIモデルによる本格的なサイバー攻撃が「数か月以内」に到来すると共同警告。生成AIが攻撃速度を大幅に高めている。 |
| 3 | **ゼロデイ／緊急RCE脆弱性の連鎖** | PeopleSoft、PTC Windchill/FlexPLM、Amazon Q Developerなど主要製品で深刻なRCE脆弱性が相次いで悪用・公開された。 |
| 4 | **インフォスティーラー摘発（Operation Endgame）** | Microsoft・Europol主導の作戦でStealC/Amadeyのインフラを解体。2,560万件の認証情報と38.5万台の感染端末を確認。 |
| 5 | **取締役会のAIガバナンス・ギャップ** | 取締役の82%が業務でAIを利用する一方、69%は正式なAI利用ポリシーを持たず、機密情報の取扱いリスクが拡大。 |

---

## 🔴 Cyber Security

### 1. ShinyHunters、Oracle PeopleSoftのゼロデイを悪用し100超の組織から学生records窃取
**2026年6月26日**
恐喝集団ShinyHunters（Mandiant追跡名：UNC6240）が、Oracle PeopleSoft PeopleToolsの未認証RCEバグ（CVE-2026-35273、CVSS 9.8）を5月27日〜6月9日にゼロデイとして悪用。約300のPeopleSoftインスタンス、100以上の組織（68%が高等教育機関）から学生・卒業生の個人情報を窃取し、Nottingham大学など被害が確認されている。

🔗 [ShinyHunters Exploits Oracle PeopleSoft Zero-Day to Breach Universities](https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html)

---

### 2. Amazon Q DeveloperのMCP設定自動読込み脆弱性、クラウド認証情報を窃取可能
**2026年6月26日**
Wiz Researchが発見したCVE-2026-12957（CVSS 8.5）は、Amazon QがワークスペースのMCPサーバー設定（.amazonq/mcp.json）を確認なしに自動実行する欠陥。悪意あるリポジトリをクローン・開くだけでAWS認証情報などが流出する恐れがあり、Language Servers for AWS 1.69.0への更新が推奨されている。

🔗 [Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs](https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html)

---

### 3. PTC Windchill/FlexPLMの緊急RCE脆弱性、実環境での悪用を確認・CISA KEVに追加
**2026年6月27日**
CVE-2026-12569（CVSS 9.3）は、Windchill PDMLinkにおける未認証デシリアライゼーションRCE。攻撃者がJSP Webシェルを設置し永続的な遠隔操作とデータ持出しを行う実例が確認され、CISAは連邦機関に6月28日までの対応を義務化した。

🔗 [First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild](https://www.securityweek.com/first-ever-exploitation-of-ptc-windchill-vulnerability-discovered-in-the-wild/)

---

### 4. Linuxカーネルの新型LPE「DirtyClone」、実証エクスプロイトが公開
**2026年6月25日**
JFrog Security Researchが、CVE-2026-43503（CVSS 8.8、通称DirtyClone）の詳細なエクスプロイトチェーンを公開。ページキャッシュのクローン処理の欠陥を突き、ディスク変更なしに一般ユーザーがroot権限を取得可能で、ファイル整合性監視やログでも検知が困難。Debian/Fedoraは既定設定で影響を受ける。

🔗 [Dissecting and Exploiting Linux LPE Variant: DirtyClone](https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/)

---

### 5. Microsoft・Europol主導「Operation Endgame」、StealC/Amadeyインフラを摘発
**2026年6月24日**
Microsoft Digital Crimes UnitがEuropolや業界各社と連携し、情報窃取マルウェアStealCとローダーAmadeyのC2サーバー200台以上を解体。2,560万件の認証情報と38.5万台の感染システムが確認され、RICO法を用いた関係者の一括訴追という新しい手法も採られた。

🔗 [StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)

---

## 🟠 AI Risk

### 6. Five Eyes、AIによる大規模サイバー攻撃が「数か月以内」に到来と共同警告
**2026年6月23日**
米英加豪NZの情報機関連合（Five Eyes）が、フロンティアAIモデルが政府・企業の防御を突破できる攻撃能力を持つ日が「年単位ではなく月単位」で迫っていると共同声明。各国政府・企業トップに防御強化の即時対応を要請した。

🔗 [AI could breach government and business defenses in months](https://www.cnn.com/2026/06/23/world/ai-five-eyes-warning-cyber-threat-intl-hnk)

---

### 7. 米政府、AnthropicのMythosモデルの限定リリースを許可
**2026年6月26日**
国家安全保障上の懸念から輸出制限を受けていたAnthropicの最強モデル「Mythos」について、米政府がライセンス要件を見直し、サイバー防御担当者や重要インフラ事業者など一部組織への限定提供を許可。一方、軽量版「Fable」の提供は依然認められていない。

🔗 [US government allows Anthropic limited release of AI model that sparked cybersecurity concerns](https://www.cnn.com/2026/06/26/tech/anthropic-mythos-release)

---

## 🟡 Data & Privacy

### 8. 米下院、州法の分断を解消する連邦プライバシー法案「SECURE Data Act」を提出
**2026年4月22日（6月時点で継続協議）**
下院エネルギー・商業委員会が、19州に広がった州ごとの消費者プライバシー法の分断を一本化する連邦包括プライバシー枠組み「SECURE Data Act」を発表。データ訂正権やユニバーサル・オプトアウトなど消費者権利の統一化を目指す。

🔗 [House Introduces SECURE Data Act to Establish a Federal Privacy Framework](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

## 🟢 Security Governance

### 9. 取締役会のAI利用が急拡大も、69%が正式なAIポリシー未整備
**2026年6月（Diligent Institute調査）**
取締役の82%が取締役会業務に生成AIを活用（9か月前は66%）と急増する一方、69%の取締役会はAI利用を統制する正式ポリシーを持たない。30%は機密情報を含む取締役会資料の要約にAIを利用しており、ガバナンス整備の遅れがリスクとして指摘されている。

🔗 [As directors embrace GenAI use, robust governance must follow](https://www.diligent.com/resources/blog/as-directors-embrace-genai)

---

## 🟣 Crypto Currency

### 10. 2026年、暗号資産プロトコルから2週間で4.5億ドル超が流出
**2026年6月（TRM Labs/MEXCレポート）**
2026年に入り45のプロトコルから合計4.5億ドル超が流出。Dango・Silo V2ではスマートコントラクトの欠陥、Kraken・Zerionでは内部関係者・ソーシャルエンジニアリング、CoW Swap・Hyperbridgeではインフラ層の侵害が確認され、攻撃面が監査済みコードの外側にも拡大している実態が浮かんだ。

🔗 [Crypto Hacks in 2026: $450M Lost Across 45 Protocols in Two Weeks](https://www.mexc.com/news/1031060)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | ShinyHunters、ゼロデイRCE、DirtyClone、Operation Endgame |
| AI Risk | 🟠🟠 | Five Eyes警告、Anthropic Mythos |
| Data & Privacy | 🟡 | SECURE Data Act、連邦プライバシー法 |
| Security Governance | 🟢 | 取締役会AIガバナンス・ギャップ |
| Crypto Currency | 🟣 | プロトコル流出、スマートコントラクト欠陥 |

---

*次回配信予定：2026年6月30日（火） | 収集ソース：The Hacker News, SecurityWeek, CNN, JFrog Security Research, Microsoft Security Blog, Diligent, MEXC, Clark Hill*
