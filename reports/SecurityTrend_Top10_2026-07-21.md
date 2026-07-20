# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月21日（火）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **SonicWall SMA1000ゼロデイ** | VPNアプライアンスの2つの脆弱性（CVSS 10.0 / 7.2）がゼロデイ攻撃で悪用され、連邦機関に緊急対応期限が課された。 |
| 2 | **間接的プロンプトインジェクション** | 悪意あるコンテンツを外部データ経由でAIエージェントに読み込ませる攻撃が前年比340%増と急拡大している。 |
| 3 | **ランサムウェア寡占化** | Qilin・LockBit・The Gentlemenなど少数グループへの攻撃集中が進み、業界全体の被害の4割超を占める。 |
| 4 | **npm/GitHubサプライチェーン侵害** | 正規開発者アカウント乗っ取りによるパッケージ改ざんで、暗号資産ウォレットの秘密鍵窃取を狙う手口が拡大。 |
| 5 | **侵害の透明性問題** | インシデントを当局へ報告せず内密処理するよう指示された組織が過半数に上り、ガバナンス上の課題として浮上。 |

---

## 🔴 Cyber Security

### 1. SonicWall SMA1000シリーズにゼロデイ脆弱性、連邦機関に緊急パッチ期限
**2026年7月14日〜20日**
SonicWallのSMA1000シリーズVPNアプライアンスに存在する2つの脆弱性（CVE-2026-15409：CVSS 10.0のSSRF、CVE-2026-15410：CVSS 7.2の認証後コマンド実行）が、公開前からゼロデイとして悪用されていたことが判明。両者を連鎖させることで未認証のまま任意コマンド実行が可能となる。Inc ランサムウェアによる悪用も確認されており、米連邦機関には7月17日までの対応期限（BOD 26-04）が課された。

🔗 [Two SonicWall SMA 1000 Zero-Days Exploited, One Could Enable Admin Commands](https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html)

---

### 2. ServiceNow、未認証APIエンドポイントの脆弱性による情報流出インシデントを開示
**2026年6月上旬（継続対応中）**
ServiceNowは、ホスト型顧客インスタンスで使用されるAPIエンドポイント（`requires_authentication=false`設定の不備）が悪用され、未認証の第三者が顧客テーブルのデータを照会できた問題を開示。6月2〜3日に不正アクセスが発生し、6月5日にセキュリティ更新を適用済み。ITサポートチケットや従業員記録などの機密データが対象となった可能性がある。

🔗 [ServiceNow discloses security incident exposing customer data](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/)

---

### 3. ランサムウェア集団Qilin、米広告大手PP+Kへの攻撃を主張
**2026年7月19日**
ランサムウェアグループQilinが、米広告代理店PP+Kへのサイバー攻撃を主張し、交渉に応じなければ機密データを公開すると脅迫。Qilinは2026年第1四半期に338件の被害を計上し、業界最大手の座を維持している。同日前後にはCAFAR（アルゼンチン）やCentre for Newcomers（カナダ）など複数組織もInterlock・The Gentlemen・LockBitなどによる侵害を受けたと報告された。

🔗 [Qilin ransomware surges into 2026](https://blog.barracuda.com/2026/01/15/qilin-ransomware-surges-into-2026)

---

### 4. 欧州の重要インフラへのサイバー攻撃が拡大、ロシア関与が疑われる
**2026年7月（継続中）**
ポーランドの電力網やスウェーデンの熱供給プラント、ノルウェーのダムなど、欧州各国の民間エネルギー・水道インフラを狙ったサイバー攻撃が相次いでいる。一部はロシアの関与が疑われており、実社会への被害リスクが高まっている。ポーランドでは水処理施設も標的となった。

🔗 [Hacked, leaked, and held for ransom: The worst breaches of 2026 so far](https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/)

---

## 🟠 AI Risk

### 5. 間接的プロンプトインジェクション攻撃が前年比340%増、OWASP最重要脅威に
**2026年7月（最新統計）**
OWASPの2026年LLMセキュリティレポートによると、プロンプトインジェクション攻撃は前年比340%増と、サイバー攻撃カテゴリの中で最も急成長している。Webページやメール、カレンダー招待などの第三者データにマルウェアを仕込みAIエージェントに読み込ませる手口が急増しており、Unit 42の調査では侵害事案の18%が認証情報や決済データの露出に関連していた。ある金融事案では約25万ドルの不正送金被害も報告された。

🔗 [Indirect prompt injection is taking hold in the wild](https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)

---

### 6. Five Eyes情報機関、AIによる大規模サイバー攻撃能力は「数か月以内」と警告
**2026年6月23日**
米国とその情報同盟国（Five Eyes）は、政府・企業の防御網を突破しうるAIモデルの登場が「数年ではなく数か月」の単位で迫っていると共同警告を発表。AIモデルが脆弱性発見を劇的に加速させており、既に逼迫しているセキュリティチームの負荷がさらに増す懸念がある。

🔗 [AI could breach government and business defenses in months, US and its intelligence partners warn](https://www.cnn.com/2026/06/23/world/ai-five-eyes-warning-cyber-threat-intl-hnk)

---

## 🟡 Data & Privacy

### 7. コネチカット州プライバシー法改正、LLM学習利用の開示義務とニューラルデータ規制が発効
**2026年7月1日**
コネチカット州データプライバシー法（CTDPA）の改正が7月1日付で発効し、対象企業は個人データが大規模言語モデル（LLM）の学習に利用されているか開示する義務を負う。あわせて「機微データ」の定義にニューラルデータが追加され、規制対象が拡大した。米国では現在ほぼ20州がデータプライバシー法を有しており、2026年は執行が最も厳格化する年になると見られている。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

### 8. 欧州委員会、MetaのFacebook/Instagramの「中毒性デザイン」がDSA違反と予備認定
**2026年7月（予備調査結果）**
欧州委員会は予備調査の結果、MetaのFacebookおよびInstagramに実装された「中毒性のある設計」がデジタルサービス法（DSA）に違反するとの見解を示した。若年層保護や依存性を助長するUI設計への規制圧力が強まっており、今後正式な措置や制裁につながる可能性がある。

🔗 [Global Data Privacy Laws in 2026: Mid-Year Update](https://cdslegal.com/insights/global-data-privacy-laws-in-2026-mid-year-update/)

---

## 🟢 Security Governance

### 9. 侵害の半数超が当局未報告のまま「内密扱い」に、透明性がガバナンス最大の課題に
**2026年7月**
過去12か月にセキュリティインシデントや侵害を経験した組織のうち55.2%が、本来当局へ報告すべきと考えながらも機密扱いにするよう指示されていたことが調査で判明。AI活用の進展とともにガバナンス・コンプライアンス体制の整備が追いついていないとの指摘があり、侵害の透明性確保が業界共通の課題として浮上している。

🔗 [Breach Transparency Remains Cybersecurity's Toughest Governance Problem](https://thehackernews.com/expert-insights/2026/07/breach-transparency-remains.html)

---

## 🟣 Crypto Currency

### 10. Injective LabsのGitHub/npmが侵害、暗号資産ウォレット秘密鍵を狙う攻撃発生
**2026年7月9日〜10日**
Injective Labsの正規コントリビューターのGitHubアカウントが乗っ取られ、週50,000ダウンロードの`@injectivelabs/sdk-ts`を含む18個のnpmパッケージに悪意あるバージョン（1.20.21）が公開された。開発者がウォレット鍵を生成・インポートする際にニーモニックフレーズと秘密鍵を窃取し、外部サーバーへ送信する仕組み。Socket、Ox Security、StepSecurityが検知し、Injective側は迅速に修正版を公開した。

🔗 [Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Packages](https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | SonicWallゼロデイ、ServiceNow、ランサムウェア、重要インフラ攻撃 |
| AI Risk | 🟠🟠 | プロンプトインジェクション、AI脅威の加速 |
| Data & Privacy | 🟡🟡 | CTDPA改正、DSA違反、ニューラルデータ |
| Security Governance | 🟢 | 侵害透明性、AIガバナンス |
| Crypto Currency | 🟣 | npmサプライチェーン攻撃、ウォレット秘密鍵窃取 |

---

*次回配信予定：2026年7月22日（水） | 収集ソース：The Hacker News, BleepingComputer, TechCrunch, Dark Reading, CNN, Help Net Security, SecurityWeek, Gunster, CDS Legal*
