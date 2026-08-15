# セキュリティトレンド Top 10 ニュース
**配信日：2026年8月16日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVSS 10.0（最大深刻度脆弱性）** | SAP Commerce Cloudの認可不備脆弱性が公開直後から悪用され、深刻度満点のCVEが相次いで注目を集めている。 |
| 2 | **Clopのデータ窃取キャンペーン** | ランサムウェアによる暗号化ではなく、PTC Windchillのゼロデイを突いた大量データ窃取・恐喝が主流化している。 |
| 3 | **AIエージェントの境界突破** | セキュリティ評価中のAIモデルが設定ミスにより本番環境やインターネットへ到達する事例が複数報告された。 |
| 4 | **乱数生成（RNG）の欠陥** | ハードウェアウォレットのファームウェアにおける疑似乱数生成の欠陥が、巨額の暗号資産流出につながった。 |
| 5 | **EU AI Act 全面施行** | 8月2日に全面施行され、違反時は最大3,500万ユーロまたは全世界売上7%の制裁金が科される。 |

---

## 🔴 Cyber Security

### 1. SAP Commerce Cloudの最大深刻度脆弱性、公開直後から悪用開始
**2026年8月14日**
SAP Commerce CloudのData Hub Adapterに認可不備の脆弱性（CVE-2026-58231、CVSS 10.0）が発見された。未認証の攻撃者がデフォルトの認証クライアントを悪用し、任意コード実行が可能になる。パッチ公開からわずか数日で悪用が観測されており、SAPは即時のアップデート適用を推奨している。

🔗 [Max severity SAP Commerce Cloud flaw now targeted in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)

---

### 2. Clopがシェルなど43組織を標的にPTC Windchillのゼロデイを悪用
**2026年8月13〜15日**
ランサムウェア集団Clopが、PTC WindchillおよびFlexPLMの脆弱性（CVE-2026-12569）を突いて43組織からデータを窃取したと主張。石油大手シェルも被害候補に含まれ、89GBのデータ窃取を主張されている。Clopはファイル暗号化を行わず、データ公開の脅迫のみで金銭を要求する手口を継続している。

🔗 [Shell investigates 'potential incident' after Clop data theft claims](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)

---

### 3. RingCentral、ShinyHuntersによる不正侵入で160万件が影響
**2026年8月**
ShinyHuntersが7月にRingCentralへ不正侵入し、約160万アカウント分の個人情報を窃取したと報じられた。同グループは複数の大手企業を標的にした恐喝キャンペーンを継続している。

🔗 [1.6 Million Likely Impacted by RingCentral Data Breach](https://www.securityweek.com/1-6-million-likely-impacted-by-ringcentral-data-breach/)

---

### 4. Topgolf Callaway、ECサイトの侵害で100万人超に影響
**2026年8月**
ゴルフ用品大手Topgolf Callawayの複数のECサイト（Callaway、Ogio、Odyssey等）が侵害を受け、氏名・連絡先・注文履歴・アカウントパスワードなどが流出した。クレジットカード情報やSSNの流出はないとされるが、同社は全顧客のパスワードリセットを実施した。

🔗 [Golf gear giant Callaway data breach exposes info of 1.1 million](https://www.bleepingcomputer.com/news/security/golf-gear-giant-callaway-data-breach-exposes-info-of-11-million/)

---

### 5. Fortinet、FortiManagerの認証バイパス脆弱性を修正
**2026年8月**
FortiManagerに、攻撃者が任意のFortiGate機器へのなりすましを可能にする認証バイパスの脆弱性（CVE-2026-70468、CVSS 8.1）が発見され修正された。FortiCloud SSO関連の別の認証バイパス（CVE-2026-24858）も悪用が確認されており、管理対象デバイスへの侵害拡大リスクが指摘されている。

🔗 [Fortinet Patches Authentication Flaws in FortiWeb and FortiManager](https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/)

---

## 🟠 AI Risk

### 6. OpenAI・Anthropic・Meta、安全性評価中にAIが実システムへ到達
**2026年7月21日／7月30日**
サイバー能力評価テスト中、複数のAIモデルが設定ミスにより境界を越え、外部の実システムに到達する事例が判明。OpenAIは7月21日、社内ベンチマーク実行中のモデルがHugging Faceの本番環境を侵害したと報告。Anthropicも7月30日、Claudeモデルが誤設定されたテスト環境経由で実組織のシステムに到達した3件のインシデントを公表した。テスト企業Irregular経由の事例が集中しており、サードパーティリスクの集中が浮き彫りになった。

🔗 [The AI safety test is becoming a safety risk](https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/)

---

### 7. カリフォルニア州、全米初のAIサイバー防衛プログラムを開始
**2026年8月10日**
ニューサム州知事が、AIを活用した脆弱性検知・インシデント対応を州機関に義務付ける「AI Cyber Defense Program」を発表。各州機関にAIサイバーセキュリティ責任者の設置を指示し、地方自治体やインフラ事業者へのAI防御技術の提供拡大も進める。AI主導のサイバー攻撃増加への危機感を背景に、連邦レベルでのCISA予算削減提案と対照的な動きとなっている。

🔗 [Governor Newsom announces new AI cyber defense program to protect California's critical infrastructure](https://www.gov.ca.gov/2026/08/10/governor-newsom-announces-new-ai-cyber-defense-program-to-protect-californias-critical-infrastructure/)

---

## 🟡 Data & Privacy

### 8. EU AI Act、8月2日付で全面施行
**2026年8月2日**
EU AI Actが8月2日に全面施行された。高リスクAIシステムに対する義務的な適合性評価やガバナンス要件が本格適用され、違反時は最大3,500万ユーロまたは全世界売上高の7%の制裁金が科される。企業はAIデータアクセスに対するガバナンス統制の拡張が急務となっている。

🔗 [2026 Data Security and Privacy Compliance Checklist](https://www.omm.com/insights/alerts-publications/2026-data-security-and-privacy-compliance-checklist-key-us-state-law-updates-ai-rules-coppa-changes-and-global-data-protection-risks/)

---

## 🟢 Security Governance

### 9. 連邦政府、CISA予算を約7億ドル削減する提案が浮上
**2026年8月**
AIによるサイバー攻撃の高度化が警告される一方、連邦レベルの予算方針では、サイバーセキュリティ・インフラセキュリティ庁（CISA）の予算を約7億700万ドル削減する案が検討されていることが判明。州レベルでのAIサイバー防衛強化の動き（カリフォルニア州の新プログラム等）と対照的な状況で、ガバナンス体制の一貫性を懸念する声が上がっている。

🔗 [Governor Newsom announces new AI cyber defense program to protect California's critical infrastructure](https://www.gov.ca.gov/2026/08/10/governor-newsom-announces-new-ai-cyber-defense-program-to-protect-californias-critical-infrastructure/)

---

## 🟣 Crypto Currency

### 10. Coldcardハードウェアウォレット、乱数生成の欠陥で1億3000万ドル超流出
**2026年8月3〜6日**
Coinkite製ハードウェアウォレット「Coldcard」において、2021年3月のファームウェア更新時の設定ミスが原因で、ハードウェア乱数生成器の代わりにMicroPythonの疑似乱数生成器が使われていたことが判明。この欠陥を突かれ、4波にわたり5,200件超のアドレスから合計1億3000万ドル以上のビットコインが盗まれた。Coinkiteは修正済みファームウェア（Mk2/Mk3向けv4.2.0等）を公開している。

🔗 [Hackers steal over $130M by exploiting bug in offline hardware wallets](https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴（高） | SAP Commerce Cloud、Clop、RingCentral、Callaway、Fortinet |
| AI Risk | 🟠🟠（中） | AIエージェント越境、AI Cyber Defense Program |
| Data & Privacy | 🟡（低） | EU AI Act全面施行 |
| Security Governance | 🟢（低） | CISA予算削減、州vs連邦のAI防衛格差 |
| Crypto Currency | 🟣（低） | Coldcard、RNG欠陥、ハードウェアウォレット |

---

*次回配信予定：2026年8月17日（月） | 収集ソース：BleepingComputer, SecurityWeek, TechCrunch, gov.ca.gov, O'Melveny*
