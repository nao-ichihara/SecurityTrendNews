# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月19日（土）**

> ⚠️ この記事はClaude AIとxAI Grok API（話題性分析）を組み合わせて収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVSS 10.0連発** | Cisco ISE、Microsoft Azure AI Foundryなど最大深刻度（CVSS 10.0）の脆弱性が同時期に複数発覚し、緊急パッチ対応が相次いだ。 |
| 2 | **AIサプライチェーン攻撃** | Plugin4Shellなど、Claude Code・Copilot等のAIコーディングエージェントを狙う新種のゼロクリック攻撃が初めて表面化。 |
| 3 | **AIの自律性リスク** | ClaudeがAnthropicの後継モデル開発の大半を主導している実態が報じられ、AI業界内で開発減速を求める声が再燃。 |
| 4 | **大規模個人データ漏洩** | Gyazo（2,360万件）、Revolut（高プロファイル顧客・身代金要求）など、規模・悪質性ともに大きい漏洩が続発。 |
| 5 | **北朝鮮系ハッキング** | WaterPlum（Contagious Interview）による偽求人キャンペーンが継続し、暗号資産窃取が大規模化。 |

---

## 🔴 Cyber Security

### 1. Cisco ISE最大深刻度ゼロデイ、積極的悪用が確認
**2026年9月17日**
Cisco ISEおよびISE-PICにCVSS 10.0の未認証リモート認証バイパス脆弱性（CVE-2026-76460）が発見され、既に実際の攻撃で悪用が確認された。APIエンドポイントの認証制御不備を突かれ、攻撃者が管理インターフェースへ不正アクセス可能な状態だった。Ciscoは緊急パッチをリリース済み。

🔗 [Cisco warns of max-severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-max-severity-ise-zero-day-exploited-in-attacks/)

---

### 2. Microsoft Azure AI Foundryに未認証で管理機能を奪えるCVSS 10.0脆弱性
**2026年9月17日**
Azure AI Foundryに、認証チェック欠如（CWE-306）による最大深刻度（CVSS 10.0）の脆弱性CVE-2026-85889が発覚。攻撃者は資格情報なしでバックエンド機能に到達し、AIモデルや関連データの管理権限を奪取できる状態だった。Microsoftは既にパッチを適用済みで、悪用の痕跡は確認されていない。

🔗 [Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw](https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html)

---

### 3. Check Point管理システムにルート権限RCE脆弱性
**2026年9月18日**
Check Point Security ManagementおよびLog Serversに、リモートからルート権限でコード実行が可能な重大脆弱性が発覚した。セキュリティ管理システム自体が侵害されると、配下のファイアウォール網全体に影響が及ぶ懸念がある。パッチは既にリリース済み。

🔗 [New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/new-check-point-flaw-lets-hackers-execute-code-with-root-privileges/)

---

## 🟠 AI Risk

### 4. Plugin4Shell：4大AIコーディングエージェントを狙うゼロクリックRCE
**2026年9月18日**
Claude Code、Codex、GitHub Copilot、Gemini CLIの4大AIコーディングエージェントで、プラグインのSHAピンニングをバイパスするゼロクリックRCE「Plugin4Shell」が発覚。リポジトリ所有者が悪意あるコードに差し替えるだけで開発者環境を侵害できる、初のAIエージェント向けサプライチェーン攻撃として注目された。AnthropicとOpenAIはパッチ済みだが、Microsoftは未対応、Googleは非対応の姿勢という。

🔗 [Plugin4Shell lets repository owners achieve zero-click RCE](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

---

### 5. Anthropic Claudeが自社の後継モデル開発を主導、安全性議論が激化
**2026年9月18日**
Anthropic社内でClaudeがR&Dの約26%を単独主導（残り90%は人間との協働）している実態が報じられた。AIによる自己改善の加速に対する懸念から、研究者やリーダー層から開発減速を求める声が上がっており、AI業界全体で安全性を巡る議論が再燃している。

🔗 [Anthropic's Claude starts building its own successor as AI safety debate intensifies](https://www.latimes.com/business/story/2026-09-18/anthropics-claude-starts-building-its-own-successor-as-ai-safety-debate-intensifies)

---

## 🟡 Data & Privacy

### 6. 画像共有サービスGyazoで2,360万ユーザー記録が漏洩
**2026年9月18日**
Gyazoのアップロードサーバーの脆弱性を突かれ、氏名・メールアドレス・パスワードハッシュ・トークン・課金情報を含む2,360万ユーザー記録と、約4億9,000万件の画像メタデータが漏洩した。侵入は9月11日に発生し翌日に排除されたが、カード情報自体の漏洩はないという。

🔗 [23 million user records compromised in Gyazo data breach](https://www.securityweek.com/23-million-user-records-compromised-in-gyazo-data-breach/)

---

### 7. Revolut、680件の高プロファイル顧客データ侵害と300万ドルの身代金要求
**2026年9月17日**
Revolutが、偽イタリア政府機関を装ったフィッシング（infostealer経由）により約5ヶ月間にわたり顧客情報を抜き取られ、暗号資産の大口保有者を含む680件のパスポート情報や取引履歴が漏洩したことが判明。攻撃者は600万XMR（約300万ドル相当）の支払いを要求しているが、Revolutは直接の接触を否定している。

🔗 [Revolut data breach: 5 months, 680 high-profile accounts, $3M ransom](https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/)

---

## 🟢 Security Governance

### 8. EUサイバーレジリエンス法、脆弱性報告義務が適用開始
**2026年9月11日（適用開始）**
EUサイバーレジリエンス法（CRA）第14条の適用が始まり、対象製品の製造業者は悪用された脆弱性や重大インシデントを24時間以内にENISA・CSIRTへ報告することが義務化された。製品のデジタル要素についてライフサイクル全体でのセキュリティ要件強化が求められる。

🔗 [Cyber Resilience Act – explained](https://www.cyberresilienceact.eu/explained.html)

---

### 9. CISA、KEVカタログに複数の悪用確認済み脆弱性を追加
**2026年9月18日**
CISAがCisco ISEやVMware vCenterなど、実際の悪用が確認された複数の脆弱性をKnown Exploited Vulnerabilities（KEV）カタログに追加した。連邦機関には定められた期限内でのパッチ適用が義務付けられており、今週だけで複数回の追加が行われている。

🔗 [CISA Cybersecurity Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)

---

## 🟣 Crypto Currency

### 10. 北朝鮮系WaterPlum、3万台感染・1,100万ドル超の暗号資産を窃取
**2026年9月18日**
北朝鮮関連ハッキンググループWaterPlum（Contagious Interview）が偽の求人を使い3万台以上の端末に感染、2025年12月から2026年7月にかけて7,000超の暗号資産ウォレットから少なくとも1,071万ドルを窃取していたことが判明。日本の警察庁とFBIが共同で注意喚起を行った。

🔗 [North Korea-linked WaterPlum campaign steals crypto via fake job offers](https://www.mitrade.com/au/insights/news/live-news/article-3-2099065-20260918)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | ゼロデイ、CVSS 10.0、ルートRCE |
| AI Risk | 🟠🟠 | AIサプライチェーン攻撃、自律的AI開発 |
| Data & Privacy | 🟡🟡 | 大規模漏洩、身代金要求 |
| Security Governance | 🟢🟢 | CRA施行、CISA KEV追加 |
| Crypto Currency | 🟣 | 国家関与ハッキング、ウォレット窃取 |

---

*次回配信予定：2026年9月20日（日） | 収集ソース：Claude AI、xAI Grok API*
