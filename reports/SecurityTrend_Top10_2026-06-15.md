# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月15日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Agentjacking** | AIコーディングエージェント（Claude Code、Cursorなど）をハイジャックし、悪意あるコードを開発者マシンで実行させる新攻撃クラス。Sentryのエラー追跡機能を悪用する手口が確認された。 |
| 2 | **ゼロデイRCE** | Oracle PeopleSoftの未パッチ脆弱性（CVE-2026-35273）がShinyHuntersに悪用され、100以上の組織が被害を受けた。認証不要で遠隔からサーバーを完全掌握できる危険度9.8の重大脆弱性。 |
| 3 | **AI Executive Order** | トランプ大統領が署名したAIセキュリティ大統領令「Promoting Advanced AI Innovation and Security」。フロンティアAIモデルの事前評価義務化やAIサイバーセキュリティ・クリアリングハウスの設立を指示。 |
| 4 | **DeFi Bridge Exploit** | クロスチェーンブリッジを狙うDeFiハックが2026年に急増。KelpDAOの2億9200万ドル流出をはじめ、14件のブリッジ攻撃で3億4000万ドル以上が失われた。 |
| 5 | **二重脅迫ランサムウェア** | データ暗号化と情報窃取を同時に行う「二重脅迫モデル」がヘルスケア分野で96%に達する。Akira、Qilin、BianLianなど主要グループがAI活用で攻撃を高速化・精度向上。 |

---

## 🔴 Cyber Security

### 1. Oracle PeopleSoftのゼロデイRCE脆弱性をShinyHuntersが悪用、100以上の組織に被害
**2026年6月11日〜12日**

Oracle PeopleSoft Enterprise PeopleToolsに重大な認証不要のリモートコード実行脆弱性（CVE-2026-35273、CVSS 9.8）が発見され、ハッキンググループShinyHunters（UNC6240）が大学を中心に100以上の組織を侵害した。被害組織の68%が高等教育機関。攻撃はOracle公式アドバイザリ発出前の5月27日〜6月9日の間に行われており、真のゼロデイ攻撃となった。Oracleはまだパッチを発布しておらず、緊急の緩和策適用を求めている。

🔗 [ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities](https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html)

---

### 2. 「Agentjacking」攻撃：AIコーディングエージェントを狙う新たな脅威
**2026年6月**

セキュリティ研究者がAIコーディングエージェント（Claude Code、Cursorなど）をハイジャックする新攻撃クラス「Agentjacking」を公開した。Sentryのエラー追跡プラットフォームを悪用して偽のエラーレポートを生成し、エージェントに任意のコードを実行させる手口。環境変数、Gitクレデンシャル、プライベートリポジトリURLなどの機密情報が漏洩する危険性がある。

🔗 [Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html)

---

### 3. ランサムウェアがヘルスケア・重要インフラを直撃、Q1だけで1,300件超
**2026年第1四半期**

2026年第1四半期だけで1,305件のサイバーインシデントが記録され、そのうち1,138件がランサムウェア攻撃として公表された。ヘルスケア分野のランサムウェア攻撃の96%が「二重脅迫モデル」（データ暗号化＋情報窃取）を採用。AIを活用した攻撃高速化により、一部グループはネットワーク侵入から横展開開始まで30秒以内という記録も。前FBI幹部はホスピタルを標的とするランサムウェアグループをテロ組織に指定する提案を行った。

🔗 [Ransomware in Healthcare: A Life-Critical Business Priority for 2026](https://www.morphisec.com/blog/ransomware-in-healthcare-a-life-critical-business-priority-for-2026/)

---

## 🟠 AI Risk

### 4. トランプ大統領がAIセキュリティ大統領令に署名、フロンティアモデルの事前評価を義務化
**2026年6月2日**

トランプ大統領が「Promoting Advanced AI Innovation and Security」と題した大統領令に署名。主な内容は：①フロンティアAIモデルのサイバーセキュリティリスク事前評価の義務化（自発的フレームワーク）、②CISAへのAI活用防御ツール拡充指示、③財務省主導のAIサイバーセキュリティ・クリアリングハウス設立。CISAは近日中に連邦機関向けに大規模言語モデルのセキュリティ確保を求める拘束的運用指令（BOD）を発出する見通し。

🔗 [AI executive order sets stage for new cybersecurity directives](https://federalnewsnetwork.com/cybersecurity/2026/06/ai-executive-order-sets-stage-for-new-cybersecurity-directives/)

---

### 5. LangGraphに重大脆弱性チェーン、自己ホスト型AIエージェントが完全乗っ取りリスク
**2026年6月**

人気のAIエージェントフレームワーク「LangGraph」（LangChain開発）に3つの重大脆弱性が発見された（CVE-2025-67644: SQLインジェクション、CVE-2026-28277: 安全でないmsgpackデシリアライゼーション、CVE-2026-27022: RedisクエリインジェクションのRCEチェーン）。SQLiteまたはRedisチェックポインタを使用する自己ホスト型デプロイメントで完全なサーバー制御奪取が可能。いずれもパッチ適用済みだが、自己ホスト環境でのアップデート対応が急務。

🔗 [LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)

---

## 🟡 Data & Privacy

### 6. GDPR罰金累計71億ユーロ突破、2026年の執行は「能動的調査」に移行
**2026年6月**

2018年5月以降のGDPR罰金累計が71億ユーロを超えた（2025年12月時点で2,679件、67億ユーロ）。アイルランドのデータ保護委員会はBig Techへの大型罰金で40億4000万ユーロを占める。2026年の特徴的変化として、規制当局が苦情待ちから「能動的調査」（ウェブサイトの積極的テスト等）に転換。金融・ヘルスケア・通信・公共機関が重点ターゲットに。また欧州委員会の「Digital Omnibus」提案がGDPR義務の一部簡素化を検討中。

🔗 [GDPR Fines Hit €7.1 Billion: Data Privacy Enforcement Trends in 2026](https://www.kiteworks.com/gdpr-compliance/gdpr-fines-data-privacy-enforcement-2026/)

---

## 🟢 Security Governance

### 7. コロラド州AI法が大幅改定、施行日を2027年1月1日に延期
**2026年5月14日**

コロラド州知事がSB 189に署名し、2024年に制定されたコロラドAI法（SB 24-205）を大幅改定。当初2026年6月30日とされた施行日が2027年1月1日に延期された。リスク管理プログラム・年次影響評価・アルゴリズム差別禁止などの包括的要件を撤廃し、AIが重要な意思決定に影響する場合の消費者通知・透明性確保を中心とした軽量フレームワークに変更。ホワイトハウスの圧力もあり、EUモデルからの転換を図った形。

🔗 [Colorado AI Act Amended and Effective Date Delayed](https://www.hunton.com/privacy-and-cybersecurity-law-blog/colorado-ai-act-amended-and-effective-date-delayed)

---

### 8. CISAが連邦パッチ適用要件を刷新、AI脅威時代対応のリスクマトリクス方式を採用
**2026年6月**

CISAが連邦機関向けのパッチ適用義務規制を大幅改定し、脆弱性の危険度に応じたリスクマトリクスアプローチを採用。最高危険度の脆弱性は3日以内の対処を義務化する一方、低リスク案件は正式に延期を許容する柔軟な枠組みに転換。このほかSP 800-230（コメント期間6月12日終了）、SP 800-133r3（6月16日終了）など複数のNIST文書も更新中。

🔗 [CISA Rewrites Federal Patching Requirements for AI Threat Era](https://www.darkreading.com/cyber-risk/cisa-rewrites-federal-patching-requirements-ai-threat-era)

---

## 🟣 Crypto Currency

### 9. KelpDAO 2億9200万ドル流出、2026年最大のDeFiハック——犯人はLazarusグループ
**2026年4月18日〜継続**

液体リステーキングプロトコルKelpDAOのLayerZeroブリッジが侵害され、116,500 rsETH（約2億9200万ドル、流通量の18%）が20チェーン以上で流出。2026年最大のDeFi被害。スマートコントラクトのバグではなく、オフチェーンインフラへの高度な攻撃で、北朝鮮のLazarusグループが内部RPCノードを侵害し外部ノードをDDoS攻撃して1-of-1検証ネットワークへ偽データを送り込んだ。Aave・SparkLend・FluidがrsETH関連市場を一時凍結。

🔗 [Kelp DAO exploited for $292 million with wrapped ether stranded across 20 chains](https://www.coindesk.com/tech/2026/04/19/2026-s-biggest-crypto-exploit-kelp-dao-hit-for-usd292-million-with-wrapped-ether-stranded-across-20-chains)

---

### 10. Europol、ランサムウェアグループが利用する暗号資産ロンダリングサービスAudiA6を摘発
**2026年6月12日**

Europolが暗号資産ロンダリングサービス「AudiA6」を摘発。同サービスはランサムウェアグループやサイバー犯罪ネットワークが身代金の資金洗浄に使用していた。2026年には45以上のプロトコルがハッキングされ累計4億5000万ドル以上が失われており、クロスチェーンブリッジへの攻撃（14件・3億4000万ドル）が特に深刻。Chainalysisの2026年暗号犯罪レポートはブリッジへのインフラ攻撃とガバナンス攻撃の増加を警告している。

🔗 [2026 Crypto Crime Report – Illicit Crypto Trends & Typologies](https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | PeopleSoft ゼロデイ, Agentjacking, ランサムウェア |
| AI Risk | 🟠🟠🟠 | AI大統領令, LangGraph RCE, AIエージェント乗っ取り |
| Data & Privacy | 🟡🟡 | GDPR 71億ユーロ, 能動的執行, Digital Omnibus |
| Security Governance | 🟢🟢 | コロラドAI法改定, CISA BOD, NISTリスクマトリクス |
| Crypto Currency | 🟣🟣 | KelpDAO 2.92億ドル, AudiA6摘発, DeFiブリッジ攻撃 |

---

*次回配信予定：2026年6月16日（火） | 収集ソース：The Hacker News, SecurityWeek, Dark Reading, BleepingComputer, CoinDesk, Chainalysis, Federal News Network, Hunton Privacy Blog*
