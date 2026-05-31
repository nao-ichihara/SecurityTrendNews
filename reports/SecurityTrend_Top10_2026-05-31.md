# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月31日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ChatGPhish** | ChatGPTのMarkdownレンダラーを悪用したプロンプトインジェクション攻撃手法。AIアシスタントへの新たなフィッシングベクターとして注目される。 |
| 2 | **AIパワーユーザーリスク** | 企業内AI利用リスクが少数の「ヘビーユーザー」に集中している実態が判明。AIガバナンスの死角として急浮上中。 |
| 3 | **SECURE Data Act** | 米国初の包括的連邦プライバシー法案。乱立する州法を統一する連邦フレームワーク構築を目指す重大立法動向。 |
| 4 | **CMMC Phase 2** | 米国防総省のサイバーセキュリティ認証制度フェーズ2が2026年11月より開始。DoD契約企業にとって入札条件に直結する重要施策。 |
| 5 | **北朝鮮国家ハッカー** | DPRKに連動したグループが2025年に20億ドルのクリプト窃取を記録。2026年も同規模攻撃の警戒が続く。 |

---

## 🔴 Cyber Security

### 1. GitHub内部リポジトリ侵害：3,800件以上のソースコードが流出危機
**2026年5月中旬**


GitHubは、悪名高い脅威アクター「TeamPCP」がプラットフォームのソースコードと内部組織をサイバー犯罪フォーラムで販売するリストに掲載した後、内部リポジトリへの不正アクセスを調査中であると発表した。
 
さらに、LAPSUSもTeamPCPと提携し、GitHubのリポジトリを9万5,000ドルで共同販売しようとしていることが明らかになった。
 
流出リポジトリにはGitHub Actions、Copilot内部プロジェクト、CodeQLツール、内部インフラ、セキュリティツールなどが含まれているとされる。


🔗 [GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html)

---

### 2. FortiClient EMSの重大脆弱性（CVSS 9.1）が野放し搾取中
**2026年5月**


脅威アクターが、FortiClient EMSの重大なセキュリティ欠陥を悪用して資格情報窃取マルウェアを配信し続けている。このキャンペーンは「信頼できるエンドポイント管理インフラを悪用してマルウェアを展開」し、攻撃者はFortinet製エンドポイントの正規アップデートに偽装した形でペイロードをPowerShell経由でサイレント実行させた。
 
2026年5月に観測されたこの活動は、CVE-2026-35616（CVSSスコア9.1）という認証前APIアクセスバイパスの脆弱性を悪用しており、FortiClient EMS 7.4.7以降で修正済み。


🔗 [The Hacker News – FortiClient EMS Critical Vulnerability](https://thehackernews.com/)

---

### 3. ShinyHuntersがCharterから4,200万件以上のレコードを流出
**2026年5月29日**


悪名高い恐喝グループ「ShinyHunters」が、4月にCharterから盗んだとされる4,200万件以上のレコードを流出させた。
 また同時期には、
Trump Mobileによる顧客データの漏洩や、2026 FIFAワールドカップを標的にしたフィッシャーの活動、さらにCISAによるサプライチェーン攻撃への対応も注目を集めている。
 
Verizonの2026 DBIRレポートでは、依然としてソーシャルエンジニアリング、フィッシング、認証情報の窃取、ランサムウェアが主要な侵害原因であると報告されている。


🔗 [SecurityWeek – ShinyHunters Charter Breach](https://www.securityweek.com/)

---

### 4. Kimsuky（北朝鮮）が韓国軍・企業を標的に新キャンペーン展開
**2026年3〜4月（5月末報告）**


北朝鮮国家支援型の脅威アクター「Kimsuky（別名 Velvet Chollima）」が、2026年3〜4月にかけて韓国の軍と企業体を標的にした新たなサイバー攻撃を実施。セキュリティソフトのインストールページや偽のWebexミーティングページへの誘導など、巧妙なソーシャルエンジニアリング戦術を駆使した。
 
攻撃では韓国製セキュリティソフトのインストーラーに偽装した「HTTPSpy」マルウェアの亜種が使用されており、2023年から一貫した手口として確認されている。


🔗 [The Hacker News – Kimsuky Campaign](https://thehackernews.com/)

---

## 🟠 AI Risk

### 5. ChatGPhish：ChatGPTのMarkdownを悪用した新型フィッシング攻撃が登場
**2026年5月29日**


ChatGPTのMarkdownリンクや画像への暗黙の信頼を利用してプロンプトインジェクションを引き起こし、フィッシング攻撃への扉を開く脆弱性の詳細が公開された。この手法はPermiso Securityによって「ChatGPhish」と命名されている。
 
研究者によると、「chatgpt.comのレスポンスレンダラーはサードパーティのページから生成されたMarkdownリンクやMarkdown画像URLを信頼し、それらの画像を自動取得して、信頼できるアシスタントUIの内部にライブでクリック可能な要素として表示する」という。


🔗 [The Hacker News – ChatGPhish Vulnerability](https://thehackernews.com/)

---

### 6. IMF警告：AI支援型サイバー攻撃が金融安定を脅かす「マクロ経済ショック」に
**2026年5月7日**


高度なAIモデルは脆弱性の特定と悪用に必要な時間とコストを劇的に削減し、広く使用されているシステムの弱点を同時に発見・標的にする可能性を高めている。その結果、サイバーリスクは金融仲介、決済、信頼をシステムレベルで混乱させる可能性のある相関的障害に関するものになりつつある。
 
Anthropicの高度AIモデル「Claude Mythos Preview」は、非専門家でも利用可能な形で主要なOSとWebブラウザの脆弱性を発見・悪用できることが示されており、AIリスクの急速な増大を浮き彫りにしている。


🔗 [IMF – Financial Stability Risks Mount as AI Fuels Cyberattacks](https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks)

---

## 🟡 Data & Privacy

### 7. 米国SECURE Data Act：連邦統一プライバシー法案が下院エネルギー商業委員会に提出
**2026年4月22日**


2026年4月22日、下院エネルギー商業委員会が「SECURE Data Act（Securing and Establishing Consumer Uniform Rights and Enforcement Over Data Act）」の導入を発表した。これは乱立する州ごとの消費者プライバシー法に代わる単一の国家的フレームワークを目的とした包括的な連邦プライバシー法案である。
 
この法案は統一的な連邦データプライバシーフレームワークを創設し、州法を無効化し、国境を越えたデータフローを規制するものであり、執行はFTCおよび各州司法長官に限定され、私的訴権は認めない。


🔗 [Clark Hill – House Introduces SECURE Data Act](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

### 8. 米国内で2026年初から州プライバシー法が続々施行：20州超が規制競争に突入
**2026年1月〜施行中**


インディアナ州、ケンタッキー州、ロードアイランド州の3つの包括的プライバシー法が2026年1月1日に施行され、消費者データ権利、センシティブデータ、オプトアウトメカニズムを規制する州の数が拡大した。
 
2026年現在、米国ではほぼ20の州が独自の規制を導入しており、企業は拡大する州プライバシー法の複雑な環境をナビゲートすることを余儀なくされている。
 
連邦プライバシー法が存在しない状況下で、各州がギャップを埋めており、新法、青少年安全法、影響力の大きい執行措置を通じてプライバシー規制を牽引し続けている。


🔗 [Ketch – Data Privacy Laws: What to Expect for 2026](https://www.ketch.com/blog/posts/us-privacy-laws-2026)

---

## 🟢 Security Governance

### 9. CMMC Phase 2始動：DoD調達の入札条件がサイバー認証に直結
**2026年11月10日施行予定（現在準備フェーズ）**


CMMC（サイバーセキュリティ成熟度モデル認証）フェーズ2は、2026年11月10日より多くのDoD請負業者にとって第三者認証が契約資格要件となる。32 CFR Part 170のフェーズ2では、DoD が適用可能な募集・契約にレベル2のC3PAO認証ステータスを義務付けることができるようになる。
 
また、HHS OCRは2026年4月23日に合計116万5,000ドルのHIPAAランサムウェア和解を発表しており、4件のランサムウェア事件で42万7,000人以上が影響を受けた医療機関への厳格な規制対応が続いている。


🔗 [Bright Defense – Recent Compliance News 2026](https://www.brightdefense.com/resources/recent-compliance-news/)

---

## 🟣 Crypto Currency

### 10. 国際的クリプト詐欺撲滅作戦：276人逮捕・9拠点閉鎖・7億1,000万ドル押収
**2026年5月（The Hacker News報告）**


国際的な一斉摘発でクリプト詐欺に関わる276人の容疑者が逮捕された。FBI主導の「Operation Level Up」は2024年1月に開始され、2026年4月時点でほぼ9,000人の被害者に通知し、推定5億6,200万ドルの被害を防いだとされている。
 
DoJはまた、ミャンマーの「Shundaスキャムコンパウンド」を運営していた中国人2名を起訴。被告らはカンボジアに第2の詐欺センターを開設しようとしていたとされる。


🔗 [The Hacker News – Global Crackdown: 276 Arrested, 9 Crypto Scam Centers Shut](https://thehackernews.com/2026/05/global-crackdown-arrests-276-shuts-9.html)

---

### Bonus. Chainalysis報告：2025年の不正クリプト流入が1,540億ドル（前年比+162%）
**2026年初頭〜継続分析**

