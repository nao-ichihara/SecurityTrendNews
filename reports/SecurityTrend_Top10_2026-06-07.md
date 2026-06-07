I'll search all 5 categories simultaneously to gather the latest security news.
# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月7日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVE-2026-20245** | Cisco Catalyst SD-WAN Managerに存在するCVSSスコア7.8の未パッチ・ゼロデイ脆弱性。攻撃者がroot権限で任意コマンドを実行可能で既に悪用が確認されている。 |
| 2 | **AIサイバークリアリングハウス** | トランプ大統領が署名したAI安全行政命令に基づく新設機関。フロンティアAIモデルを公開前30日間でセキュリティ評価し、脆弱性情報を業界と共有する仕組み。 |
| 3 | **DeFiブリッジ攻撃** | 2026年、クロスチェーンブリッジを狙った14件の大規模攻撃により累計3億4,070万ドルが流出。DeFiエコシステムで最も高リスクなインフラとして標的化が加速。 |
| 4 | **SECURE Data Act** | 米国下院で審議中の全国統一データプライバシー法案。州ごとに異なる規制の混乱解消を目指すが、強力な保護を持つ州の基準を引き下げるとして民主党が反発。 |
| 5 | **Shadow AI（シャドーAI）** | 企業公認外のAIツール・ブラウザ拡張・個人アカウントが静かに組織内に浸透する現象。LayerXレポートによると企業AI利用の大半がガバナンス管理外で発生している。 |

---

## 🔴 Cyber Security

### 1. Cisco SD-WAN Manager にゼロデイ脆弱性（CVE-2026-20245）— 未パッチで既に悪用中
**2026年6月5日**


Ciscoは、Cisco Catalyst SD-WAN Manager（旧SD-WAN vManage）に存在するゼロデイ脆弱性（CVE-2026-20245）について警告を発した。この高深刻度の欠陥は既に悪用が確認されており、root権限への特権昇格を可能にする。
影響範囲はオンプレミス・クラウド・政府（FedRAMP）など複数の展開形態に及び、認証済みローカル攻撃者が細工したファイルをアップロードすることでコマンドインジェクションが可能となる。パッチはまだ提供されておらず、緊急の対応が求められる。


🔗 [Cisco SD-WAN Zero-Day CVE-2026-20245 Actively Exploited](https://www.bleepingcomputer.com/news/security/)

---

### 2. WordPress プラグイン「Everest Forms Pro」に緊急RCE脆弱性（CVE-2026-3300）
**2026年6月上旬**


脅威アクターが、約4,000件のアクティブインストールを持つWordPressプラグイン「Everest Forms Pro」の深刻な脆弱性を悪用し、任意コードを実行してサイトを完全掌握する攻撃が進行中だ。問題の脆弱性はCVE-2026-3300（CVSSスコア：9.8）で、バージョン1.9.12以前の全バージョンに存在するリモートコード実行（RCE）バグである。
サイト運営者は直ちにプラグインのアップデートと侵害痕跡の確認を行う必要がある。

🔗 [Everest Forms Pro RCE CVE-2026-3300 Under Active Exploitation](https://thehackernews.com/)

---

### 3. Magecartキャンペーン — Stripe APIを悪用してカード情報を窃取
**2026年6月上旬**


新たなMagecartキャンペーンがStripeのAPIインフラを利用して、クレジットカード窃取ペイロードのホスティングおよびチェックアウトページからのデータ流出を行っていることが確認された。また、歯科医療給付管理会社DentaQuestでのデータ侵害により、260万件のアカウントの機密データが流出したとも報告されている。
サイバー犯罪グループはネットワークへ侵入後30秒以内に横展開を開始できるほど攻撃速度が向上しており、AI支援型攻撃の急増もセキュリティチームの対応を困難にしている。


🔗 [New Magecart Campaign Abuses Stripe API Infrastructure](https://www.bleepingcomputer.com/news/security/)

---

### 4. DentaQuest データ侵害 — 260万アカウントの個人情報が流出
**2026年6月上旬**


攻撃者はシニアエグゼクティブのメールアカウントに150日間アクセスし、数ヶ月にわたってデータを外部に持ち出していたことが判明した。
また、新たな積極的なサイバー恐喝グループ「Crimson Collective」が、通信プロバイダーBrightspeedに対するランサムウェア攻撃で100万人超の顧客データを窃取したと主張しており、ランサムウェアは依然として最も一般的なサイバー犯罪の形態の一つである。


🔗 [DentaQuest Data Breach Exposes 2.6 Million Accounts](https://www.bleepingcomputer.com/news/security/)

---

## 🟠 AI Risk

### 5. トランプ大統領がAIセキュリティ大統領令に署名 — フロンティアAIモデルの事前審査を義務化
**2026年6月3日**


トランプ大統領が署名した大統領令は、連邦機関に対してAIモデルのサイバー能力評価のためのベンチマーク開発、「AIサイバーセキュリティクリアリングハウス」の設置、政府のセキュリティ防衛強化を指示している。AI企業に対しては、最も強力なモデルを公開の30日前に政府のテストのために自発的に提出することを求めている。
この大統領令は、Anthropic社のClaude MythosモデルのプレビューがAIの新たなサイバー脆弱性特定・悪用能力において人間を大幅に上回ることを示したことへの対応として策定された。


🔗 [AI Executive Order Sets Stage for New Cybersecurity Directives](https://federalnewsnetwork.com/cybersecurity/2026/06/ai-executive-order-sets-stage-for-new-cybersecurity-directives/)

---

### 6. MIT/国際AI専門家272名が警告 — 情報・金融・安全保障分野で壊滅的リスク
**2026年6月3日**


MITフューチャーテックおよびクイーンズランド大学が37カ国272名の国際AI専門家を対象に実施した調査では、24のAIリスクカテゴリを横断的に検討した。専門家らは最も深刻な被害が生じる分野として情報、金融、国家安全保障を最も脆弱なセクターと判定した。
AIリスク軽減に最も責任を持つのは汎用AIの開発者と規制当局だが、「リスクを低減できる立場にある者が、その結果を最も被りやすい立場にはない」と研究者らは警鐘を鳴らしている。


🔗 [International AI Experts Warn of Potentially Catastrophic Risks from AI](https://www.globenewswire.com/news-release/2026/06/03/3305947/0/en/International-AI-experts-warn-of-potentially-catastrophic-risks-from-AI.html)

---

## 🟡 Data & Privacy

### 7. 米国SECURE Data Act審議 — 全国統一プライバシー法を巡り議会が対立
**2026年6月3日**


下院共和党が提出したデータプライバシー法案「SECURE Data Act」について、与野党の見解が対立している。共和党は「企業に明確性を提供し、全国民への統一的保護をもたらす」と主張する一方、民主党は「より強力なプライバシー法を持つ州の保護水準を引き下げ、プライバシー管理の負担を企業ではなく個人に転嫁する」と批判している。
法案は個人データの削除権、ターゲット広告のオプトアウト、データプロファイリングからのオプトアウトなどの消費者権利を新たに創設する内容となっている。


🔗 [Consent Questions Raised at Data Privacy Bill Hearing](https://rollcall.com/2026/06/03/consent-questions-raised-at-data-privacy-bill-hearing/)

---

### 8. 米国20州がプライバシー法を施行 — CCPA改訂・EU AI Act適用迫る
**2026年上半期（継続中）**


2026年3月時点で、米国20州が包括的プライバシー法を整備し、インディアナ・ケンタッキー・ロードアイランドが2026年に施行された。カリフォルニア・コネチカット・コロラド・メリーランド・ミネソタはリスク評価、プロファイリング、生体データ、オプトアウト手段、プライバシー通知の正確性の基準を引き上げている。
さらに、EU AI Actは2026年8月2日に完全適用される予定であり、企業にとってグローバルなコンプライアンス対応が急務となっている。


🔗 [2026 Data Security and Privacy Compliance Checklist](https://www.omm.com/insights/alerts-publications/2026-data-security-and-privacy-compliance-checklist-key-us-state-law-updates-ai-rules-coppa-changes-and-global-data-protection-risks/)

---

## 🟢 Security Governance

### 9. EU NIS2・DORA対応でEU組織がコンプライアンス圧力に苦しむ — ガバナンス再編が急務
**2026年6月1日**


EUにおけるサイバーセキュリティガバナンスは、NIS2やDORAなど拡大し続ける規制フレームワークの下で大きな変革を迫られており、AIが新たな問題を提起している。今後の展開は予測困難で、組織は適切な対処方法を模索し続けなければならない。
EU企業は増加する規制量に直面しており、GDPRとNIS2では対象データが異なるにもかかわらず相互補完的に機能すべきであるなど、「誰に何が適用され、なぜそうなのかを説明できる人が少ない」という複雑さが問題となっている。


🔗 [EU Organizations Buckle Under Rising Compliance Pressure](https://www.helpnetsecurity.com/2026/06/01/antonija-vojnovic-span-cybersecurity-governance-challenges/)

---

### 10. CMMC Phase 2施行迫る — DoD請負業者のサイバーセキュリティ認証が契約資格に直結
**2026年11月10日施行予定（準備期限迫る）**


CMMC Phase 2は2026年11月10日より、多くのDoD（米国防総省）請負業者に対してサードパーティ認証を契約資格の条件とする。32 CFR Part 170のPhase 2では、DoD が Level 2のC3PAO認証ステータスを適用可能な入札・契約の条件として要求できるようになり、FCI・CUI（管理された非機密情報）を扱う請負業者はセルフアセスメントを安全な選択肢として扱えなくなる。
条件付きLevel 2ステータスは180日後に失効する可能性があるため、早期の評価計画が不可欠だ。


🔗 [List of Recent Compliance News in 2026](https://www.brightdefense.com/resources/recent-compliance-news/)

---

## 🟣 Crypto Currency

### 🏆 DeFiブリッジへの集中攻