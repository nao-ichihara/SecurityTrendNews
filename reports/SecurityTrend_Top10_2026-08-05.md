I'll search all 5 categories simultaneously to gather the latest security news.
Now let me search for a few more specific stories to fill in the details:
以上の検索結果をもとに、Markdownレポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年8月5日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **サプライチェーン攻撃** | 広告テックや製薬業界のサードパーティクラウドを経由した攻撃が急増。間接的な侵害経路がセキュリティの最大の死角に。 |
| 2 | **EU AI Act 完全施行** | 2026年8月2日にEU AI法が全面執行フェーズへ移行。GPAIモデルへの罰則権限が発動し、グローバル企業に対応が迫られる。 |
| 3 | **CVE-2026-18577（認証バイパス）** | N-able N-centralの深刻な脆弱性がCISAのKEVカタログに追加。パッチバイパスで野放しの悪用が継続中。 |
| 4 | **クリプトクリッパーマルウェア** | ウォレットアドレスをリアルタイムで書き換えるマルウェアが拡散。Adform事案や$130M規模のColdcardハックで被害が顕在化。 |
| 5 | **ヘルスケア・クラウド侵害** | AmgenやAbbottなど医療・製薬企業でサードパーティクラウドからのPHI漏えいが連続発生。業界全体のリスクが急上昇。 |

---

## 🔴 Cyber Security

### 1. 英国警察データベース（PNLD）が侵害──10万人超の警察官情報がダークウェブに流出

**2026年7月26日（発覚）/ 8月5日時点 調査継続中**


英国の警察専用法律データベース（PNLD）へのサイバー攻撃により、10万人超の警察官・刑事司法関係者の連絡先情報が侵害された。侵入は7月26日（日）に検知され、データ恐喝グループ「ExfilSquad」が犯行を主張し、135,000件の連絡先レコードを窃取したと主張している。
パスワードは流出していないが、漏えいした情報によってフィッシングや標的型攻撃のリスクが高まっており、セキュリティ会社はMicrosoft Power Pagesポータルの設定ミスとの関連を示唆している。
本件は、政府機関を狙った一連の侵害を受け、英国公共部門ITシステムのセキュリティに対する懸念を新たに高めている。


🔗 [ExfilSquad hackers leak info of over 100,000 UK police officers, staff](https://www.bleepingcomputer.com/news/security/exfilsquad-hackers-leak-info-of-over-100-000-uk-police-officers-staff/)

---

### 2. 製薬大手Amgen、サードパーティクラウドから患者PHIと企業機密データが流出

**2026年7月31日（SEC 8-K 開示）**


製薬大手Amgenは、サードパーティのクラウドサービス事業者が運営する複数のクラウドシステムに脅威アクターが侵入し、企業データおよび患者情報が窃取されたと発表した。同社は2026年7月に不正活動を検知し対応を開始した。
調査の結果、機密企業データ・患者の保護健康情報（PHI）・その他のデータがクラウド環境から外部に持ち出されたことが判明し、7月29日にSECへ重要事案として報告された。
本件は、2026年を通じて製薬・医療セクターを標的としたサードパーティクラウド攻撃の広範なパターンの一部と位置付けられている。


🔗 [Amgen says cloud data breach exposed patient health, proprietary info](https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/)

---

### 3. CISAがN-able N-central認証バイパス脆弱性（CVE-2026-18577）をKEVに追加──INC ランサムウェアが積極悪用

**2026年8月4日**


米国CISAは、N-able N-centralに影響する高深刻度のセキュリティ欠陥をKnown Exploited Vulnerabilities（KEV）カタログに追加した。この脆弱性（CVE-2026-18577、CVSSスコア：8.2）は、以前のパッチ（CVE-2026-18556）の不完全な修正であり、認証バイパスおよびアカウント乗っ取りを可能にする。
CISAによると、脆弱なN-centralサーバーへのリモート管理者アクセスが可能となり、組み込みの「Take Control」機能を悪用して管理対象エンドポイントに侵入し、永続化機構を展開することができる。
INCランサムウェアグループが脆弱なSMA1000アプライアンスを標的にroot権限取得と横断的移動を行っていることも報告されている。


🔗 [CISA Warns of Actively Exploited N-central Vulnerability CVE-2026-18577](https://thehackernews.com/)

---

### 4. Coldcardハードウェアウォレットの脆弱性悪用で1億3,000万ドル超が窃取

**2026年8月4日**


暗号資産ハードウェアウォレット「Coldcard」のセキュリティ脆弱性が悪用され、ハッカーが被害者のウォレットから暗号資産を流出させている。ブロックチェーン監視会社によると、総被害額は1億3,000万ドルを超える。
オフラインで安全とされるハードウェアウォレットを狙った大規模窃盗が進行中であり、少なくとも12の異なるハッカーグループがCoinkite社製のColdcardユーザーを標的にしているとされ、背後には複数のグループの関与が示唆されている。


🔗 [Hackers steal over $130M by exploiting bug in offline hardware wallets](https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/)

---

## 🟠 AI Risk

### 5. Check Pointレポート：間接プロンプトインジェクションが急増──AIへの攻撃が「運用上のリスク」に

**2026年7月〜8月（レポート公開）**


間接プロンプトインジェクションの検知が急増しており、より長い悪意あるペイロードの検知数は2026年3月〜5月の間に約5倍に増加し、5月には観測されたプロンプトの1%近くに達した。
エンタープライズにおけるGenAIを通じたデータ漏洩は持続的かつ拡大するリスクとなっており、高リスクなプロンプトは昨年比で2%から4%へと倍増した。一方、組織は月平均10のAIアプリを使用しており、その多くは正式な承認なしに運用されている。
ビジネスサービス部門では高リスクGenAIプロンプトの発生率が5.91%と最も高く、約17回に1回のAIインタラクションで機密データ漏洩リスクが発生していることを意味する。


🔗 [AI Security Report 2026 - Check Point Research](https://research.checkpoint.com/2026/ai-security-report-2026/)

---

### 6. AIリスク管理の「自信ギャップ」が拡大──企業の90%がAIセキュリティ強化に期待、実装可能は8%のみ

**2026年（レポート公開）**


エンタープライズでのAI採用が加速する中、新たなレポートは、組織がAIリスクの管理について自己認識よりはるかに準備が不足している可能性を警告している。「State of AI Risk Management 2026」レポートは、AI システムをエンタープライズ規模で管理するためのガバナンスに重大なギャップがあることを示している。
ゾーホーの調査では、90%の組織がAIによってセキュリティ対策が強化されると考えているにもかかわらず、AIを活用したセキュリティツールを実際に展開できる体制が整っているのはわずか8%であることが明らかになった。


🔗 [The State of AI Risk Management in 2026 Reveals a Growing Confidence Gap](https://www.esecurityplanet.com/artificial-intelligence/the-state-of-ai-risk-management-in-2026-reveals-a-growing-confidence-gap/)

---

## 🟡 Data & Privacy

### 7. EU AI法（AI Act）が8月2日に全面施行──高リスクAIシステムへの厳格義務とGPAI罰則権限が始動

**2026年8月2日（施行日）**


2026年8月2日より、特定のAIシステムの提供者および展開者はEU AI法第50条の透明性義務を遵守しなければならない。欧州委員会は7月20日にこれらの義務に関するガイドラインを採択しており、違反した場合は最大1,500万ユーロまたは世界年間売上高の3%の罰金が科される。
GPAIモデルプロバイダーに対する欧州委員会の監督・執行権限が2026年8月2日に初めて発動する。
ハイリスクAIシステム（重要インフラ、医療、雇用、教育、法執行機関、移民で使用）はリスク管理、データガバナンス、技術文書、人間による監視、サイバーセキュリティに関する厳格な義務への準拠が求められる。


🔗 [EU AI Act: Transparency Obligations Take Effect 2 August 2026](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026)

---

### 8. 米国プライバシー規制が加速──20州が包括的データプライバシー法を施行、コネチカット州がニューラルデータを追加

**2026年（年間動向）**


2026年1月1日時点で、インディアナ州・ケンタッキー州・ロードアイランド州を直近として、米国20州が包括的消費者プライバシー法を施行している。
コネチカット州は2026年7月1日に「ニューラルデータ」を機密カテゴリに追加した。
米国のプライバシー規制の状況は、（1）新しい包括的州プライバシー法、（2）既存法の大幅改正、（3）米国史上最も積極的な執行環境という3つの力によって形成されている。


🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 9. SEC開示義務が「コンプライアンスの試金石」に──企業のサイバーインシデント報告が2025年比で増加傾向

**2026年（年間動向）**


SECへのサイバーインシデント開示（Form 8-K）は2025年のペースを上回って推移しており、重要性（マテリアリティ）評価のタイミング・根拠・証拠保全が問われている。SECのルールは、重要なサイバーインシデントを重要性判断後4営業日以内に開示することを求めており、法務・財務・セキュリティ・取締役会報告のワークフローに大きな圧力をかけている。