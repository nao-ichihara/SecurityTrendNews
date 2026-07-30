# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月31日（金）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AIワーム（プロンプトインジェクション伝播）** | Microsoft Copilot for Wordで、文書に隠されたプロンプトが編集を通じて他の文書へ自己増殖する新種の攻撃手法が確認された。 |
| 2 | **wp2shell** | WordPress Coreの2つの脆弱性（CVE-2026-63030／CVE-2026-60137）を連結し、未認証のまま管理者権限でコード実行を可能にする攻撃チェーン。既に悪用が確認されている。 |
| 3 | **EU AI Act 第50条（透明性義務）** | 2026年8月2日からチャットボット等のAI利用開示・ディープフェイク表示義務が施行され、汎用AIモデル提供者への執行権限も発動する。 |
| 4 | **x402（エージェント決済プロトコル）** | Coinbase等が採用するAIエージェント向け決済規格「x402」で31件の脆弱性が発覚し、資産窃取や無料購入などのリスクが指摘された。 |
| 5 | **侵害の透明性（Breach Transparency）** | インシデント発生時の開示姿勢や説明責任が、ガバナンス上の最大の課題として改めて浮き彫りになっている。 |

---

## 🔴 Cyber Security

### 1. WordPress Core「wp2shell」pre-auth RCEチェーンが実際に悪用
**2026年7月17日開示／7月18〜20日に悪用確認**
WordPress Core 6.9系・7.0系に存在する2つの脆弱性（REST APIバッチルートの混同とSQLインジェクション）を連結し、認証なしで管理者アカウントを偽装、サーバー上で任意コードを実行できる。PoCが公開され、複数のセキュリティ企業が実環境での悪用を確認。7.0.2／6.9.5／6.8.6へのアップデートが必須。

🔗 [New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)
🔗 [WordPress Core Pre-Auth RCE Chain Exploited in the Wild](https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/)

---

### 2. Microsoft Copilot for Wordに自己増殖するAIワーム脆弱性
**2026年7月28〜29日報道（開示は3月、7月28日時点も攻撃手法が再現）**
文書内に隠されたJSON形式のプロンプトをCopilotが解釈し、編集済み文書が新たな攻撃媒体となって他の文書へ自己増殖する「AIワーム」が確認された。Microsoftは複数回の緩和策を実施したが、改変版のペイロードは7月28日時点でも同種の攻撃を再現できている。外部由来文書はCopilot利用前に信頼できないものとして扱うことが推奨される。

🔗 [Hidden prompt turns Microsoft Copilot into an AI worm](https://www.malwarebytes.com/blog/ai/2026/07/hidden-microsoft-copilot-ai-worm)
🔗 [Word worm crawls into Copilot, spreads chaos](https://www.theregister.com/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588)

---

### 3. Revolut、7,500万件の顧客データ流出疑惑
**2026年7月29日**
ダークウェブのフォーラムに、Revolutの顧客7,500万人分とされるデータベース（カード情報・氏名・メール・電話番号・住所・デバイス情報・ハッシュ化認証情報を含む）がわずか500ドルで売りに出された。Revolutは社内監視で不正アクセスの兆候はないとして調査中。研究者は7,500万件という規模を検証できておらず、複数ソースの混在データの可能性を指摘している。

🔗 [75 million Revolut records allegedly for sale: here's what our researchers found](https://cybernews.com/security/revolut-data-breach-75-million-records/)

---

### 4. ランサムウェア集団、脆弱なファイアウォールを標的に
**2026年7月（週次まとめ）**
INCランサムウェアなど複数の攻撃者グループが、パッチ未適用のファイアウォール機器を標的にした侵入を続けている。AIを活用したマルウェアやガードレールのないAIモデルがサイバー犯罪の高速化・自動化を後押ししているとの指摘もある。

🔗 [AI Agents, Trust Abuse, and Breaches Define Cybersecurity News this Week of July 2026](https://www.esecurityplanet.com/weekly-roundup/ai-agents-trust-abuse-and-breaches-define-cybersecurity-news-this-week-of-july-2026/)

---

## 🟠 AI Risk

### 5. OpenAI ChatGPT Workspace Agentsに「AgentForger」脆弱性
**開示：Zenity Labs（修正は6月8日時点で完了）**
フィッシングリンク経由で組織内に自律型AIエージェントを展開できてしまう重大な脆弱性が、ChatGPT Workspace Agentsで確認された。OpenAIは既に対応済みだが、AIエージェントが企業内で権限を持つことに伴うリスクとして注目されている。

🔗 [AI Security Daily Briefing: July 27, 2026](https://techmaniacs.com/2026/07/27/ai-security-daily-briefing-july-27-2026/)

---

### 6. AIエージェントへのデータ汚染・注入攻撃が拡大
**2026年7月時点のトレンド**
偽の商品レビューでAIエージェントに「購入」操作をさせたり、偽のGitHubコメントでコーディング支援AIに攻撃者のコマンドを実行させるなど、データポイズニングによるAIエージェント操作が顕在化。エンタープライズでのAI導入がセキュリティ統制の整備を上回っている状況が指摘されている。

🔗 [AI Agents, Trust Abuse, and Breaches Define Cybersecurity News this Week of July 2026](https://www.esecurityplanet.com/weekly-roundup/ai-agents-trust-abuse-and-breaches-define-cybersecurity-news-this-week-of-july-2026/)

---

## 🟡 Data & Privacy

### 7. EU AI Act 第50条の透明性義務が2026年8月2日に施行
**施行日：2026年8月2日**
チャットボット等のAI対話は「AIと会話している」旨の開示、合成コンテンツ・ディープフェイクの表示義務が発効。同日、汎用AI（GPAI）モデル提供者に対する欧州委員会の監督・執行権限も発動する。違反時は最大3,500万ユーロまたは全世界年間売上高7%の制裁金。

🔗 [The EU AI Act – when does it become enforceable now?](https://www.dataprotectionreport.com/2026/07/the-eu-ai-act-when-does-it-become-enforceable-now/)
🔗 [EU AI Act Enforcement: What Aug 2, 2026 Means](https://olakai.ai/blog/eu-ai-act-enforcement-august-2026/)

---

### 8. 米国州プライバシー法が2026年後半も拡大続く
**2026年7月時点**
カリフォルニア、コネチカット、オレゴン、ユタ各州で規制が発効し、アーカンソー州も7月に新法を施行。未成年者データ、自動意思決定、データブローカーの透明性への規制強化に加え、ユニバーサルオプトアウトの義務化が進む。カリフォルニアはサイバーセキュリティ監査要件とプライバシーリスク評価も拡充。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. 「侵害の透明性」が依然としてガバナンス最大の課題
**2026年7月**
2026年版Bitdefenderサイバーセキュリティ評価は、インシデント発生時の対応姿勢・透明性・説明責任の文化が組織のガバナンス力を左右すると指摘。侵害報告義務は認識されつつも、事案を公表しない圧力が依然として存在するという。米SECの2026年審査優先事項でも、暗号資産よりサイバー・AIガバナンスへの関心が上回った。

🔗 [Breach Transparency Remains Cybersecurity's Toughest Governance Problem](https://thehackernews.com/expert-insights/2026/07/breach-transparency-remains.html)

---

## 🟣 Crypto Currency

### 10. AIエージェント決済「x402」に31件の脆弱性
**開示：2026年7月21日**
Coinbase、Stripe、Cloudflare等が採用する取引全体の99%を扱う15のx402決済ファシリテーターを調査した結果、資産窃取・無料購入・サービス妨害・ガス代の不正転嫁につながる31件の脆弱性が発覚。全ファシリテーターで何らかの違反が確認され、Coinbaseを含む各社が修正対応を開始した。

🔗 [31 newly discovered vulnerabilities expose 99% of x402 crypto payments to asset theft and free shopping](https://cryptoslate.com/31-newly-discovered-vulnerabilities-expose-99-of-x402-crypto-payments-to-asset-theft-and-free-shopping/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | wp2shell、AIワーム、データ漏えい、ランサムウェア |
| AI Risk | 🟠🟠 | AgentForger、データポイズニング、エージェント統制 |
| Data & Privacy | 🟡🟡 | EU AI Act第50条、米国州プライバシー法 |
| Security Governance | 🟢 | 侵害の透明性、SEC審査優先事項 |
| Crypto Currency | 🟣 | x402、決済ファシリテーター脆弱性 |

---

*次回配信予定：2026年8月1日（土） | 収集ソース：The Hacker News, BleepingComputer, Cybernews, eSecurity Planet, Malwarebytes, The Register, Data Protection Report, Olakai, Gunster, CryptoSlate, CoinDesk*
