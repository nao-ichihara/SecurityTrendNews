# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月13日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ゼロデイ悪用（Zero-Day Exploitation）** | 未パッチの脆弱性を標的にする攻撃が急増。PeopleSoft CVE-2026-35273（CVSS 9.8）がShinyHuntersに悪用され、大学を中心に被害が拡大。発見から悪用までのタイムラインが急速に短縮している。 |
| 2 | **AIエージェントセキュリティ** | LLMを搭載した自律型AIエージェントが初めてライブ攻撃に使用された事例が確認された。人間の指示なしにAWSデータベースを1時間以内に侵害・流出させており、AI攻撃の自動化が新たな脅威段階に入った。 |
| 3 | **クロスチェーンブリッジ攻撃** | 2026年のDeFiハックの中心的手口。14件の攻撃で累計3.41億ドルが流出。Lazarus Groupの関与も確認され、スマートコントラクト以外にバリデーターやガバナンス系も標的に。 |
| 4 | **AIガバナンス規制** | コロラド州AI法（6月30日施行）、EUのAI法一般適用（8月2日）、米ホワイトハウスの大統領令と、AIリスク規制が世界規模で同時進行。企業のコンプライアンス対応が急務となっている。 |
| 5 | **CISA KEVカタログ強化** | CISAが連邦パッチ適用要件を刷新し、最高リスクの脆弱性を3日以内修正義務へ。SolarWinds Serv-Uの脆弱性もKEVに追加されるなど、積極的な悪用事例への対応スピードが求められている。 |

---

## 🔴 Cyber Security

### 1. ShinyHunters がOracle PeopleSoft ゼロデイ（CVE-2026-35273）を悪用、大学など多数の組織に侵入
**2026年6月9日**
ランサムウェア／恐喝グループのShinyHuntersが、5月27日〜6月9日にかけてOracle PeopleSoft Enterprise PeopleToolsの未パッチ脆弱性CVE-2026-35273（CVSS 9.8）を悪用。認証・ユーザー操作なしにHTTP経由でリモートコード実行が可能なこの脆弱性を使い、大学を中心とした企業システムからデータを窃取した。

🔗 [Hacked, leaked, and held for ransom: The worst breaches of 2026 so far | TechCrunch](https://techcrunch.com/2026/06/07/the-worst-hacks-and-breaches-of-2026-so-far/)

---

### 2. CISAがSolarWinds Serv-Uの高深刻度脆弱性（CVE-2026-28318）をKEVに追加
**2026年6月上旬**
CISAはSolarWinds Serv-Uマルチプロトコルファイルサーバーソフトウェアの高深刻度セキュリティ欠陥CVE-2026-28318をKnown Exploited Vulnerabilities（KEV）カタログに追加した。積極的な悪用の証拠が確認されており、連邦機関には期限内のパッチ適用が義務付けられる。

🔗 [Cybersecurity News, Insights and Analysis | SecurityWeek](https://www.securityweek.com/)

---

### 3. 2026年DBIR（Verizon）：攻撃者の侵入から横展開まで30秒未満のグループが出現
**2026年5〜6月**
Verizonが発表した2026年データ侵害調査レポート（DBIR）では、一部の脅威アクターがネットワーク侵入から横展開を30秒以内に開始する事例が報告された。AI支援攻撃の急増、フィッシング・ソーシャルエンジニアリング・認証情報窃取が引き続き主要な攻撃経路となっている。

🔗 [2026 Data Breach Investigations Report (DBIR) | Verizon](https://www.verizon.com/business/resources/reports/dbir/)

---

### 4. Stryker医療機器会社へのサイバー攻撃：イラン系ハクティビストグループが関与
**2026年3月（2026年上半期主要インシデント）**
医療技術大手Strykerがイラン系ハクティビストグループによる大規模サイバー攻撃を受けた。2026年上半期の主要インシデントの一つとして注目され、医療セクターへの国家支援型攻撃の脅威が改めて浮き彫りになった。

🔗 [The biggest cyber breaches of 2026 so far | ACI Learning](https://www.acilearning.com/blog/the-biggest-cybersecurity-breaches-of-2026-so-far-and-the-training-that-could-have-prevented-them/)

---

## 🟠 AI Risk

### 5. LLMエージェントが初のライブ攻撃に使用：BadHost脆弱性（CVE-2026-48710）でAWSデータベースを自律侵害
**2026年6月**
StarlettePythonフレームワークのクリティカルなホストヘッダーインジェクション脆弱性「BadHost」（CVE-2026-48710）が発見された。FastAPI・vLLM・LiteLLM・MCPサーバーなど数百万のAIエージェントが影響を受ける。セキュリティ企業Sysdigは、LLMエージェントが人間の指示なしに1時間以内でAWSデータベースを自律的に侵害・流出させた初のライブ攻撃事例を記録した。

🔗 [We Scanned 1 Million Exposed AI Services. Here's How Bad the Security Actually Is | The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)

---

### 6. ホワイトハウスがAIセキュリティ大統領令を発令：フロンティアAIの公開前リスク評価を義務化
**2026年6月**
ホワイトハウスはAIサイバーセキュリティ「クリアリングハウス」の設立と、高度フロンティアAIモデルの公開前サイバーセキュリティリスク評価の義務化を盛り込んだ大統領令を発令した。複数の連邦機関に対して新たなサイバーガイダンスの整備を指示している。

🔗 [White House Releases Executive Order on Advanced AI Innovation and Security | Global Policy Watch](https://www.globalpolicywatch.com/2026/06/white-house-releases-executive-order-on-advanced-ai-innovation-and-security/)

---

## 🟡 Data & Privacy

### 7. 米SECURE Data Act議会初公聴会：ビジネスフレンドリーとの批判も
**2026年6月3日**
下院エネルギー・商業委員会で共和党主導のSECURE Data Act（Securing and Establishing Consumer Uniform Rights and Enforcement over Data Act）の初公聴会が開かれた。消費者保護よりも企業の利便性を優先する内容との批判が上がり、包括的な連邦プライバシー法制定への道のりに課題が残る。

🔗 [Consent questions raised at data privacy bill hearing – Roll Call](https://rollcall.com/2026/06/03/consent-questions-raised-at-data-privacy-bill-hearing/)

---

### 8. ニューヨーク州が健康データプライバシー法案を可決：ワシントン州My Health My Data Actに続く動き
**2026年6月5日**
ニューヨーク州議会がS-9269（健康データプライバシー法案）を可決。ワシントン州が2023年に成立させた「My Health My Data Act」に倣い、消費者の健康データに対する同意・管理権を強化する内容。インディアナ・ケンタッキー・ロードアイランド州でも2026年に新たな包括的プライバシー法が施行される。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws | Gunster](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. コロラド州AI法施行（6/30）・EUのAI法適用（8/2）・FTC「TAKE IT DOWN Act」執行開始：AIガバナンス規制が同時多発
**2026年6月〜8月**
コロラド州AI法が6月30日、EUのAI法が8月2日に一般適用され、企業はハイリスクAIシステムへのコンプライアンス対応を迫られている。FTCは5月19日よりTAKE IT DOWN Actの第3条執行を開始し、AIが生成した非合意的親密画像のプラットフォームによる48時間以内の削除を義務付けた。

🔗 [How AI Governance Fits Into Cybersecurity Compliance: A Practical 2026 Guide | Secure Privacy](https://secureprivacy.ai/blog/how-ai-governance-fits-into-cybersecurity-compliance)

---

## 🟣 Crypto Currency

### 10. 2026年DeFiハック総額10億ドル超：KelpDAO $2.94億・Lazarus Groupが最大級被害に関与
**2026年上半期**
2026年のDeFi市場は深刻なセキュリティ危機に直面しており、45のプロトコルがハッキングされ損失は10億ドルを超えた。最大の事件はKelpDAOの$2.94億流出（rsETHブリッジコントラクトの悪用）で、北朝鮮系Lazarus Groupの関与が確認された。クロスチェーンブリッジへの14件の攻撃で累計$3.41億が流出しており、ブリッジがDeFiインフラの最大の弱点となっている。

🔗 [The Biggest Hack of 2026: What We Know About the $294M KelpDAO Exploit | CryptoPotato](https://cryptopotato.com/the-biggest-hack-of-2026-what-we-know-about-the-294m-kelpdao-exploit/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | ゼロデイ、PeopleSoft、SolarWinds、DBIR |
| AI Risk | 🟠🟠🟠🟠 | AIエージェント攻撃、BadHost、大統領令 |
| Data & Privacy | 🟡🟡🟡 | SECURE Data Act、健康データ、州法施行 |
| Security Governance | 🟢🟢🟢 | AIガバナンス、TAKE IT DOWN Act、EU AI法 |
| Crypto Currency | 🟣🟣🟣🟣 | DeFiハック、KelpDAO、Lazarus Group、ブリッジ攻撃 |

---

*次回配信予定：2026年6月14日（日） | 収集ソース：TechCrunch, SecurityWeek, The Hacker News, Verizon DBIR, Global Policy Watch, Roll Call, Gunster Law, CryptoPotato, Secure Privacy, ACI Learning*
