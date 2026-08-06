# セキュリティトレンド Top 10 ニュース
**配信日：2026年8月6日（木）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CISA KEV（Langflow／N-central／Tomcat）** | AIワークフローツールLangflowの未認証RCE（CVE-2026-9198）を含む3件の脆弱性がCISAの既知悪用カタログに追加され、実際に悪用が確認された。 |
| 2 | **パスキー窃取マルウェア** | Windows端末上でGoogleパスワードマネージャーの同期パスキーを悪用し、秘密鍵を抜き取ってアカウントを乗っ取る手法が新たに確認された。 |
| 3 | **Coldcardエントロピー不具合** | ハードウェアウォレットColdcard Mk2／Mk3のファームウェアが弱い乱数生成にフォールバックしていたことが判明し、1.3億ドル超のビットコインが流出。 |
| 4 | **自律型AI攻撃（Autonomous AI-Driven Attacks）** | 人間の指示を最小限にAIが自律的に侵入・悪用のコマンドを何十セッションにもわたり生成する事例が研究者により報告された。 |
| 5 | **ガバナンスギャップ** | サイバー予算を増額する企業は77%に達する一方、全社的なサイバーレジリエンスを実現できているのはわずか2%という調査結果が公表された。 |

---

## 🔴 Cyber Security

### 1. CISA、Langflow・N-central・Apache Tomcatの悪用中脆弱性を追加
**2026年8月4〜5日**
CISAは既知悪用脆弱性（KEV）カタログに3件を追加。中でもAIワークフローツールLangflowのコード注入脆弱性（CVE-2026-9198、CVSS 9.8）は、未認証の呼び出し元にスーパーユーザートークンを発行してしまう欠陥と、任意のPythonコードを実行できる検証エンドポイントの欠陥を連結し、完全な未認証RCEを可能にする。連邦機関には8月7日までの対応が義務付けられた。

🔗 [CISA Flags Langflow RCE, Tomcat, and N-central Flaws as Actively Exploited](https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html)
🔗 [CISA Adds Three Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/08/04/cisa-adds-three-known-exploited-vulnerabilities-catalog)

---

### 2. Topgolf Callaway、100万人超に影響するデータ侵害
**2026年8月上旬報道**
Topgolf Callawayで大規模なデータ侵害が発生し、100万人を超える顧客に影響。対象者にはメールで通知が送付されている。

🔗 [Data Breaches That Have Happened This Year (2026 Update)](https://tech.co/news/data-breaches-updated-list)

---

### 3. Frederick Health Medical Group、93万人超の患者データ流出
**2026年8月上旬報道**
医療機関Frederick Health Medical Groupで934,326人の患者に影響するセキュリティ侵害が発生。氏名、住所、生年月日、社会保障番号、健康保険情報が流出したとされる。

🔗 [List of Recent Data Breaches in 2026](https://www.brightdefense.com/resources/recent-data-breaches/)

---

### 4. Windows端末でGoogleパスワードマネージャーのパスキーを狙う新手法
**2026年8月報道**
研究者が、すでに侵害されたWindows端末上のマルウェアがGoogleパスワードマネージャーの同期パスキーを悪用し、アカウントを乗っ取ったりパスキーの秘密鍵を抽出したりする3つの攻撃手法を確認した。

🔗 [Cyberattacks & Data Breaches recent news | Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches)

---

## 🟠 AI Risk

### 5. AIセキュリティ報告書：プロンプトインジェクションが急増
**2026年8月（Check Point Research／eSecurity Planet報告）**
高リスクなGenAIプロンプトの割合は過去1年で2%から4%へ倍増、企業は平均月10種のAIアプリケーションを（多くは未承認で）利用している。長文の悪意あるペイロード検出は3月から5月にかけて約5倍に増加し、5月には観測プロンプトの約1%に達した。

🔗 [The State of AI Risk Management in 2026 Reveals a Growing Confidence Gap](https://www.esecurityplanet.com/artificial-intelligence/the-state-of-ai-risk-management-in-2026-reveals-a-growing-confidence-gap/)

---

### 6. 自律型AIが侵入・悪用ワークフローを実行する事例を確認
**2026年8月報道**
研究者らは、AIが最小限の人間の指示のもとで侵入・悪用のワークフローを自律的に実行し、数十セッションにわたり数千のコマンドを生成した事例を文書化した。AIによるガバナンス統制と実運用のギャップが浮き彫りになっている。

🔗 [AI Security Daily Briefing: August 04, 2026](https://techmaniacs.com/2026/08/04/ai-security-daily-briefing-august-04-2026/)

---

## 🟡 Data & Privacy

### 7. 米新規3州のプライバシー法が本格運用、コネチカット州は適用範囲を拡大
**2026年（年間動向）**
インディアナ、ケンタッキー、ロードアイランドの新規包括的プライバシー法が施行され、規制対象州は約20州に拡大。コネチカット州はGLBA対象金融機関に認めていた事業者単位の適用除外を撤廃し、規制対象を拡大した。未成年者データ、自動意思決定、データブローカーの透明性への規制強化も続く。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

### 8. GDPR制裁金が累計58.8億ユーロに達する
**2026年動向まとめ**
2018年以降のGDPR制裁金総額が58.8億ユーロに到達。TikTokは中国への不正データ移転で5.3億ユーロ、Metaは同意操作で4.79億ユーロ、Vodafoneはベンダーのセキュリティ不備で4,500万ユーロの制裁を受けており、事業の中核的な業務プロセスを狙った摘発が続いている。

🔗 [The 5 trends shaping global privacy and enforcement in 2026](https://www.onetrust.com/blog/the-5-trends-shaping-global-privacy-and-enforcement-in-2026/)

---

## 🟢 Security Governance

### 9. サイバー予算は増加も全社的レジリエンスは2%止まり、SECはAI・サイバーを最優先に
**2026年8月報道**
77%の企業がサイバー予算の増額を計画する一方、全社的なサイバーレジリエンスを実現できているのはわずか2%にとどまり、ガバナンス体制・意思決定権限・取締役会レベルの説明責任の不足が指摘されている。米SECの2026年審査優先事項でも、暗号資産への関心をサイバーセキュリティとAIガバナンスへの関心が上回った。

🔗 [Rethinking business resilience in 2026: The expanding role of security, governance and risk](https://www.ibm.com/think/insights/expanding-role-security-governance-risk)

---

## 🟣 Crypto Currency

### 10. Coldcardハードウェアウォレットのエントロピー不具合で1.3億ドル超が流出
**攻撃開始：2026年7月30日／被害拡大：8月上旬まで継続**
Coldcard Mk2／Mk3のファームウェア（2021年3月のv4.0.0以降）がハードウェア乱数生成器を使わず弱いソフトウェア方式にフォールバックしていたことが判明。本来128bitを目標とするエントロピーが約40bitしかなく、攻撃者はオフラインで秘密鍵を再現可能だった。Galaxy Researchによれば少なくとも15グループの攻撃者が関与し、7,300以上のウォレットから1.3億ドル超のビットコインが流出。Coinkite（製造元）の公表は最初の攻撃波から約30時間後だった。

🔗 [Coldcard Attack Widens: 15 Hackers Drain $130M in Bitcoin](https://dailycoin.com/coldcard-wallet-attack-hackers-drain-130m-in-bitcoin/)
🔗 [A five-year-old Coldcard bug let hackers guess bitcoin wallet keys, Coinkite confirms](https://www.blockhead.co/2026/08/03/coldcard-hardware-wallets-shipped-with-broken-randomness-for-five-years-coinkite-confirms/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | CISA KEV、Langflow、データ侵害、パスキー窃取 |
| AI Risk | 🟠🟠 | プロンプトインジェクション急増、自律型AI攻撃 |
| Data & Privacy | 🟡🟡 | 米州プライバシー法拡大、GDPR大型制裁金 |
| Security Governance | 🟢 | ガバナンスギャップ、SEC審査優先事項 |
| Crypto Currency | 🟣 | Coldcardエントロピー不具合、$130M流出 |

---

*次回配信予定：2026年8月7日（金） | 収集ソース：The Hacker News, BleepingComputer, CISA, Dark Reading, tech.co, BrightDefense, eSecurity Planet, TECHMANIACS, Gunster, OneTrust, IBM, DailyCoin, Blockhead*
