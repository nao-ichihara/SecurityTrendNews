# セキュリティトレンド Top 10 ニュース
**配信日：2026年8月13日（木）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **プロンプトインジェクション** | AIアシスタントに悪意ある指示を埋め込み、権限内のデータを外部に送信させる攻撃手法。AtlassianのRovoなど企業向けAIエージェントで相次いで報告されている。 |
| 2 | **Lazarus Group（北朝鮮系）** | Windowsゼロデイの悪用や暗号資産取引所への攻撃で今週最も名前が挙がった国家関与型ハッカー集団。ForestTigerバックドアや大型crypto流出の背後で確認された。 |
| 3 | **EU AI Act 本格施行** | 8月2日からEUのAI規制法の執行が開始。チャットボットのAI利用表示やディープフェイクのラベル付けが義務化され、違反時は世界売上高の最大3%の制裁金が科される。 |
| 4 | **ハードウェアウォレット脆弱性** | Coldcardの5年越しのファームウェア不備によりシード生成が弱い乱数に依存していたことが判明し、1億ドルを超えるビットコインが流出。自己管理型資産の安全神話が揺らいでいる。 |
| 5 | **サプライチェーン攻撃** | 開発者エコシステムやロジスティクス企業（Ceva）など、直接の標的以外に被害が連鎖的に波及する攻撃が今週の共通テーマとして浮上。 |

---

## 🔴 Cyber Security

### 1. Ceva Logisticsで大規模データ侵害、欧州の銀行・小売・Steamユーザーにまで波及
**2026年8月11日**
物流大手Ceva Logistics（CMA CGM傘下）の欧州8拠点の倉庫システムが7月29日〜8月1日にかけて侵害され、氏名・住所・電話番号・注文データなどが流出。ValveのSteamハードウェア購入者を含む多数の企業顧客に影響が波及し、オランダのデータ保護当局には10社から届出があった。

🔗 [A data breach at shipping giant Ceva Logistics is rippling across banks, retailers, Steam gamers, and beyond](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)

---

### 2. Lazarus GroupがWindowsゼロデイ（CVE-2026-68820）を悪用しForestTigerバックドアを展開
**2026年8月12日**
北朝鮮系Lazarus Groupが偽の求人オファーを介して欧州・インドの防衛関連（航空宇宙）企業を標的に攻撃。Windowsのafd.sysに存在するuse-after-free脆弱性（CVE-2026-68820）を突いてSYSTEM権限を奪取し、長期潜伏型のForestTigerバックドアを展開した。侵害されたWordPress/SharePoint/Roundcubeサーバーが C2 基盤として悪用されている。Microsoftは8月11日のPatch Tuesdayで修正済み。

🔗 [Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html)

---

### 3. Intelが8月Patch Tuesdayで8件の脆弱性を公表、高深刻度の権限昇格を複数含む
**2026年8月11日**
Intelは8月11日、CPUマイクロコード更新（20260811）を公開し、Xeon 6やIntel Core Ultraなど広範な世代に影響する高深刻度の権限昇格脆弱性（INTEL-SA-01379、01428、01435、01442など）と情報漏えい脆弱性を修正した。AMDと合わせ、両社で計70件超の脆弱性が今回のPatch Tuesdayで対応された。

🔗 [Chipmaker Patch Tuesday: Intel and AMD Patch 70 Vulnerabilities](https://www.securityweek.com/chipmaker-patch-tuesday-intel-and-amd-patch-70-vulnerabilities/)

---

### 4. ランサムウェア被害が「高水準の新常態」として定着、2026年通年で高止まり
**2026年8月上旬**
業界レポートによると、2026年に入ってもランサムウェアの攻撃件数は減少せず、高水準の「新常態」として定着しつつある。攻撃者はデータ窃取と暗号化を組み合わせた二重恐喝を継続しており、組織のベースラインリスク想定の見直しを迫っている。

🔗 [Ransomware reaches elevated 'new normal' as attack volumes hold steady into 2026](https://industrialcyber.co/reports/ransomware-reaches-elevated-new-normal-as-attack-volumes-hold-steady-into-2026-reshape-baseline-risk-expectations/)

---

## 🟠 AI Risk

### 5. Atlassian Rovoに「RovoBlast」プロンプトインジェクション脆弱性、企業データ窃取のおそれ
**2026年8月11日**
Atlassianの AI アシスタント「Rovo」に、ログイン済みユーザーが悪意あるリンクをクリックするだけでJira/Confluence等のアクセス権限内データを外部サーバーへ送信させられる脆弱性「RovoBlast」が発見された。研究者PromptArmorは5月23日に報告済みだが、複数回のフォローアップ後も十分な対応がないまま脆弱な状態が続いていると指摘している。

🔗 [One-click flaw in Atlassian Rovo exposed enterprise data via prompt injection attack](https://www.csoonline.com/article/4207306/one-click-flaw-in-atlassian-rovo-exposed-enterprise-data-via-prompt-injection-attack.html)

---

### 6. AIリスク管理に「認識と対応」の乖離拡大、新調査で判明
**2026年8月**
最新の調査によると、多くの組織はAI活用に伴うリスクの存在自体は認識しているものの、実際の対応スピードが脅威の拡大に追いついていないことが明らかになった。AIがより自律的かつ業務に深く組み込まれるにつれ、このギャップを埋められるかどうかはガバナンスモデルの適応速度に懸かっているとされる。

🔗 [The State of AI Risk Management in 2026 Reveals a Growing Confidence Gap](https://www.esecurityplanet.com/artificial-intelligence/the-state-of-ai-risk-management-in-2026-reveals-a-growing-confidence-gap/)

---

## 🟡 Data & Privacy

### 7. EU AI Actの透明性義務が8月2日から本格施行
**2026年8月2日**
欧州委員会のAI Officeと加盟国当局によるAI Actの本格的な執行が8月2日に開始。チャットボット等の対話型AIシステムはAIであることをユーザーに明示する義務を負い、ディープフェイクにはラベル付けが必須となった。AI生成・加工コンテンツには機械可読な識別情報の付与も求められる。違反時の制裁金は世界売上高の最大3%。

🔗 [Commission starts enforcing AI Act rules and new transparency requirements on 2 August](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714)

---

## 🟢 Security Governance

### 8. SEC、2026年examination prioritiesで暗号資産からサイバー・AIへ重点をシフト
**2026年8月**
米SECの2026年検査重点項目では、過去5年間にわたり主要テーマだった暗号資産関連リスクに代わり、サイバーセキュリティとAIガバナンスが業界の中心的関心事として浮上。暗号資産関連リスクは単独カテゴリではなく、カストディ・開示・不正防止といった既存の枠組みに統合される形となった。

🔗 [SEC's 2026 exam priorities: data privacy takes center stage as crypto is dropped](https://www.governance-intelligence.com/regulatory-compliance/secs-2026-exam-priorities-data-privacy-takes-center-stage-crypto-dropped)

---

## 🟣 Crypto Currency

### 9. Coldcardハードウェアウォレットの脆弱性で1億3000万ドル超のBTCが流出
**2026年8月10日**
Coinkite社のハードウェアウォレット「Coldcard」において、2021年3月のファームウェアに起因するビルド設定の不備でシード生成が弱いソフトウェア乱数に依存していたことが判明。7月30日以降、攻撃者が体系的にビットコインを窃取し、初動の41分間だけで約1,082BTC（約7,000万ドル）が流出、被害総額は最終的に1億3,000万ドルを超えた。同期間にシードを生成したユーザーは移行が推奨されている。

🔗 [Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 Minutes](https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html)

---

### 10. Blockaid調査：2026年上半期の暗号資産ハッキング被害が過去最高の11億ドル超
**2026年7月29日**
セキュリティ企業Blockaidの調査によると、2026年上半期の暗号資産関連ハッキング被害額は212件の検証済みインシデントで合計約11億ドルに達し、上半期として過去最高を記録。KelpDAO（2.92億ドル）、Drift Protocol（2.85億ドル）など上位4件で全体の約64%を占め、北朝鮮系Lazarus Group傘下のTraderTraitorが被害額の過半（約55%）に関与したと分析されている。

🔗 [Crypto hacks hit record high in H1 2026 as losses top $1 billion, Blockaid says](https://www.theblock.co/post/409944/crypto-hacks-hit-record-high-in-h1-2026-as-losses-top-1-billion-blockaid-says)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | サプライチェーン侵害、ゼロデイ、Patch Tuesday、ランサムウェア |
| AI Risk | 🟠🟠 | プロンプトインジェクション、AIガバナンス格差 |
| Data & Privacy | 🟡 | EU AI Act、透明性義務 |
| Security Governance | 🟢 | SEC examination priorities、規制シフト |
| Crypto Currency | 🟣🟣 | ハードウェアウォレット、Lazarus Group、H1被害額最高 |

---

*次回配信予定：2026年8月14日（金） | 収集ソース：TechCrunch, The Hacker News, SecurityWeek, CSO Online, eSecurity Planet, European Commission, Governance Intelligence, The Block, Industrial Cyber*
