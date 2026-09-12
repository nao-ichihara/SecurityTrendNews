# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月13日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **GitLab CVE-2026-85706（CVSS 10.0）** | パストラバーサルにより認証なしで任意ファイル読み取りが可能な最高深刻度の脆弱性。CISAがKEVカタログに追加し、連邦機関に9月14日までの対応を要求。 |
| 2 | **Anthropic脅威インテリジェンスレポート** | 2025年12月〜2026年8月にClaudeが悪用された7つの被害領域（サイバー攻撃・監視・詐欺など）を公表。国家関連アクターによるエージェント型攻撃の広がりが焦点。 |
| 3 | **ShinyHunters** | Syrian政府7百万件、VK.com、Berkadiaなど複数組織への攻撃・データ流出を継続する恐喝グループ。9月に入り新たなリークサイトも展開。 |
| 4 | **Liquid Networkハック（ホワイトハット）** | ビットコインのサイドチェーンから3.2億ドル相当が流出。攻撃者は「ホワイトハット」を自称し大半を返還したが、約15%を保持する異例の展開に。 |
| 5 | **インフォスティーラー経由のAIトークン窃取** | Lumma/Vidar等のインフォスティーラーが窃取したJWTトークンにより、MFAを回避してClaude・ChatGPT・Gemini等のアカウントに不正アクセス可能な実態が判明。 |

---

## 🔴 Cyber Security

### 1. GitLab、CVSS 10.0の重大パストラバーサル脆弱性が悪用され緊急対応
**2026年9月11日**
CISAはGitLab Community/Enterprise Editionに存在するパストラバーサル脆弱性（CVE-2026-85706）をKnown Exploited Vulnerabilitiesカタログに追加。認証なしの攻撃者がリポジトリコミットAPIの不備を突き、サーバー上の任意ファイルを読み取れる状態にあった。連邦機関には9月14日までの対応期限とフォレンジック調査（BOD 26-04）が課された。

🔗 [GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html)
🔗 [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog)

---

### 2. Adobe、BPO委託先経由の侵害で1300万件のサポートチケット流出か
**2026年9月（報道時点、Adobe未確認）**
「Mr. Raccoon」を名乗る攻撃者が、Adobeが契約するインドのBPO業者の従業員端末にRATを仕込み侵入。1300万件のサポートチケット、1万5000件の従業員記録、HackerOneの未公開脆弱性報告一式を窃取したと主張している。Adobeは公式な確認をしていないが、マルウェア解析コミュニティは流出サンプルを「信憑性が高い」と評価している。

🔗 [Adobe Breach - Threat Actor Allegedly Claims Leak of 13 Million Support Tickets and Employee Records](https://cybersecuritynews.com/adobe-breach/)

---

### 3. Clopがランサムウェア化、PTC Windchill脆弱性を悪用し継続的にデータ窃取
**2026年6月の脆弱性公開以降、9月時点も攻撃継続**
Clop（Cl0p）がPTC Windchill/FlexPLMのリモートコード実行脆弱性（CVE-2026-12569、CVSS 9.3）を悪用し、専用に開発したJSP Webシェルを設置。認証情報の復号やファイルリポジトリの列挙機能を備え、製造業の設計データなど機密情報を窃取する二重恐喝キャンペーンを展開している。

🔗 [Clop created custom web shell for Windchill data theft attacks](https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/)
🔗 [CISA Adds Exploited PTC Windchill RCE Flaw to KEV as Web Shell Attacks Continue](https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html)

---

## 🟠 AI Risk

### 4. Anthropic、Claude悪用に関する脅威インテリジェンスレポートを公表
**2026年9月10日**
Anthropicは2025年12月〜2026年8月にかけて検知・遮断したClaude悪用事例を、サイバー攻撃・影響工作・監視・詐欺・生物兵器関連・通常兵器開発・蒸留の7領域にわたって報告。フーシ派関連グループによる誘導兵器コード生成の試みやイラン関連グループによる監視目的利用、中国系ラボによる大量クエリを用いたモデル蒸留など、エージェント型AIの悪用が単なるプロンプト支援から実行フェーズへ拡大している実態が明らかになった。

🔗 [Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)
🔗 [Anthropic Details Disrupted Claude Misuse Across Seven Harm Areas](https://www.unite.ai/anthropic-details-disrupted-claude-misuse-across-seven-harm-areas/)

---

### 5. インフォスティーラーが窃取したAIトークンでMFAを回避しアカウント乗っ取り
**2026年9月9日**
Telegramで公開された7GB分のインフォスティーラーログ（162カ国・5,871台の感染端末由来）を分析した結果、Google・Anthropic・Microsoft・OpenAI関連サービスなどの未失効認証トークンが多数含まれていたことが判明。有効なJWTを再利用されるとパスワードやMFAをバイパスして直接アカウントへアクセスされる恐れがあり、Claude・Cursor・ChatGPT・Geminiへのアクセス権が闇市場で売買されている実態も確認された。

🔗 [Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA](https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html)

---

## 🟡 Data & Privacy

### 6. Alipay、8.2億ユーザーの情報漏えいが疑われるとダークウェブで主張
**2026年9月9日**
ダークウェブ上で、攻撃者がAlipay（Ant Group傘下）の8.2億ユーザー分の氏名・電話番号・メールアドレス等を含むとするデータベースを販売用に投稿。Alipay側からの独立した確認は取れておらず、件数には重複データの可能性も指摘されているが、真正であれば中国国内最大級の漏えい事案となる。

🔗 [Hacker puts data of 820 million Alipay users up for sale](https://www.escudodigital.com/en/cybersecurity/hacker-puts-data-of-820-million-alipay-users-up-for-sale.html)

---

### 7. ShinyHunters、シリア政府7百万件やVK.comなど複数組織から相次ぎ情報流出
**2026年9月9日**
恐喝グループShinyHunstersが、シリア政府関連の700万件の個人情報記録やロシアのSNS大手VK.com（Vkontakte）の過去データなどをリークフォーラムに相次いで投稿。同グループは新たなリーク基盤も展開しており、テイクダウンを受けても窃取データを恒久的に公開し続ける姿勢を示している。

🔗 [ShinyHunters rolls out new leak infrastructure, vows stolen data will stay online forever](https://cybernews.com/cybercrime/shinyhunters-expands-leak-operation-survives-takedowns/)

---

## 🟢 Security Governance

### 8. 金融安定理事会（FSB)、フロンティアAIのサイバーリスクをG20に警告
**2026年8月28日付け書簡（9月上旬に報道）**
FSB議長のAndrew Bailey氏が、フロンティアAIモデルがサイバー攻撃の速度・規模・経済性を根本的に変え、金融システム全体の信頼を揺るがしかねないとG20財務相・中央銀行総裁宛に警告。集中度の高いサードパーティ技術プロバイダーへの依存が複数機関にまたがる障害波及リスクを高めるとし、モデルの安全なリリースと金融機関側の脆弱性管理・復旧能力強化を求めた。

🔗 [FSB Chair warns of risks arising from frontier Artificial Intelligence (AI) models](https://www.fsb.org/2026/08/fsb-chair-warns-of-risks-arising-from-frontier-artificial-intelligence-ai-models/)
🔗 [Financial Stability Board Sounds the Alarm Over Frontier AI Risks](https://www.infosecurity-magazine.com/news/financial-stability-board-alarm/)

---

## 🟣 Crypto Currency

### 9. Liquid Networkから3.2億ドル流出、「ホワイトハット」が大半を返還する異例の展開
**2026年9月7日〜8日**
BitcoinサイドチェーンLiquid Networkの連邦ウォレットからBTC約4,000枚（約3.2億ドル相当、保有量の約95%）が流出。運営元Blockstreamは鍵の漏えいではなくElementsのソフトウェアバグが原因とし、認証済み引き出しプラットフォームSideSwapを通じて不正に生成されたL-BTCが換金されたと説明。攻撃者はOP_RETURNを使った取引メッセージで「ホワイトハット」を自称し、24時間以内にBTC3,400枚（85%）を返還、598.5枚（約15%）を報酬として保持した。

🔗 [$320 million bitcoin exploit hits Liquid Network. Hacker makes conditional offer](https://www.coindesk.com/markets/2026/09/07/bitcoin-network-used-by-exchanges-hit-by-usd320-million-exploit-hackers-claim-they-re-the-good-guys)
🔗 [Liquid Network hack: Whitehats return 3,400 BTC](https://www.coindesk.com/markets/2026/09/08/white-hat-hackers-return-most-of-usd320m-bitcoin-taken-from-liquid-network)

---

### 10. ウォレットドレイナー詐欺が拡大、偽IRS通知やディープフェイク投資勧誘も横行
**2026年9月（月間まとめ）**
2026年9月は偽の米国内国歳入庁（IRS）通知から架空の「デジタル資産コンプライアンスポータル」へ誘導する詐欺や、AIディープフェイクを使った投資勧誘、ウォレットドレイナーリンク、承認フィッシングなどが活発化。悪意あるスマートコントラクト承認に署名させ資産を吸い上げる手口が主流で、直近ではCrypto.com関連の貸付プラットフォームから約600万ドルが抜き取られる事案も発生した。

🔗 [Crypto Scams September 2026: The Complete Active Threats List](https://www.coingabbar.com/en/crypto-blogs-details/crypto-scam-alert-list-active-fraud-schemes-2026)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | GitLab, Adobe, Clop, Windchill |
| AI Risk | 🟠🟠 | Anthropic脅威レポート, インフォスティーラー, AIトークン窃取 |
| Data & Privacy | 🟡🟡 | Alipay, ShinyHunters, 大規模漏えい |
| Security Governance | 🟢 | FSB, フロンティアAI, G20 |
| Crypto Currency | 🟣🟣 | Liquid Network, ホワイトハット, ウォレットドレイナー |

---

*次回配信予定：2026年9月14日（月） | 収集ソース：The Hacker News, BleepingComputer, CISA, Anthropic公式, CoinDesk, cybersecuritynews.com ほか（Grok連携：XAI_API_KEYは設定済みだが、このセッションのネットワーク制限によりapi.x.aiへの接続がブロックされたためスキップ。通常のWeb検索のみでレポートを生成）*
