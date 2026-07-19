# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月20日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **ゼロデイ悪用の連鎖** | SharePoint、SonicWall SMA、Oracle PeopleSoftなど、複数ベンダーの重大脆弱性が公開前後に相次いで実攻撃に悪用され、CISAのKEVカタログへの追加ペースが加速している。 |
| 2 | **AIセキュリティ成熟度のギャップ** | AIの本番導入が急拡大する一方、81.2%の企業がAIパッケージに既知の脆弱性を抱え、修正可能な脆弱性の99.9%が未対応というレポートが公表された。 |
| 3 | **OSS/npmサプライチェーン攻撃** | 正規の開発者アカウント経由でGitHubリポジトリが侵害され、npm経由でウォレット秘密鍵を窃取するマルウェアが配布される事例が続発。 |
| 4 | **侵害の透明性・報告義務** | 侵害を経験した専門家の55.2%が「報告すべきと思ったが箝口令を敷かれた」と回答し、インシデント対応ガバナンスの課題が浮き彫りに。 |
| 5 | **連邦データプライバシー法の統一化** | 州ごとに分断された米国のプライバシー規制を一本化する「SECURE Data Act」が下院で審議中で、企業のコンプライアンス対応に影響を与える可能性。 |

---

## 🔴 Cyber Security

### 1. CISA、Microsoft SharePointの重大脆弱性（CVSS9.8）をKEVカタログに追加
**2026年7月16日**
CISAはMicrosoft SharePoint Serverの深刻な逆シリアル化脆弱性CVE-2026-58644（CVSSスコア9.8）を既知悪用脆弱性（KEV）カタログに追加した。オンプレミス版SharePointの全サポートバージョンが影響を受け、攻撃者はIISマシンキーの窃取や持続的アクセスの確立に悪用している。連邦政府機関には7月19日までの対応が義務付けられた。

🔗 [CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV](https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html)

---

### 2. SonicWall SMA 1000のゼロデイ2件をInc Ransomwareが悪用
**2026年7月14日**
SonicWallのSMA 1000シリーズに存在するCVE-2026-15409とCVE-2026-15410が、Inc Ransomware関連の攻撃者によりゼロデイとして悪用された。2つの脆弱性を連鎖させることで、未認証の攻撃者がリモートコード実行からルート権限奪取まで到達可能。SonicWallは緊急ホットフィックスを公開している。

🔗 [Inc Ransomware Exploits SonicWall SMA Zero-Days](https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days)

---

### 3. ServiceNow、未認証APIエンドポイントの不備による顧客データ露出を公表
**2026年6月2日（発生）**
ServiceNowは、Scripted REST Resourceの設定ミス（requires_authentication=falseの誤設定）により、未認証のリクエストが顧客インスタンスのデータにアクセス可能だったインシデントを公表した。ITチケットや従業員情報など機微な企業データが影響範囲に含まれる可能性がある。

🔗 [ServiceNow discloses security incident exposing customer data](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/)

---

### 4. ShinyHunters、Oracle PeopleSoftのゼロデイで100超の組織を侵害
**2026年6月10日**
ShinyHuntersはOracle PeopleSoftの未認証RCEゼロデイ（CVE-2026-35273）を悪用し、5月27日から6月9日にかけて300インスタンス・100組織超を侵害した。被害の3分の2以上が大学で、氏名・住所・GPA・学籍番号などを含む学生記録が大量流出。Oracleの公式アドバイザリはShinyHuntersのデータ公開後に公表された。

🔗 [ShinyHunters linked to exploitation of critical flaw in Oracle PeopleSoft](https://www.cybersecuritydive.com/news/shinyhunters-exploitation-critical-flaw-oracle-peoplesoft/822796/)

---

### 5. テキサス州パークス&ワイルドライフ局、狩猟・釣り免許顧客300万人超の情報漏えい
**2026年6月18日**
免許システムの委託ベンダーが侵害され、運転免許証情報やパスポート番号、メールアドレス、住所など300万人超の顧客データが影響を受けた可能性がある。社会保障番号やクレジットカード情報は含まれていないとされ、影響を受けた顧客にはKroll社経由の信用監視サービスが提供される。

🔗 [Texas Parks & Wildlife Data Breach Affects 3 Million Individuals](https://www.securityweek.com/texas-parks-wildlife-data-breach-affects-3-million-individuals/)

---

## 🟠 AI Risk

### 6. Five Eyes、「AIによる大規模サイバー攻撃は数か月以内」と警告
**2026年6月23日**
米・英・加・豪・NZの情報機関連合Five Eyesは、政府・企業の防御網を圧倒しうるAIモデルの登場が「年単位ではなく月単位」で迫っていると共同警告を発表した。AIは脆弱性特定やフィッシング作成、マルウェア生成を自動化し攻撃の速度と複雑さを増大させるとし、特に中小企業のリスクが高いと指摘している。

🔗 [AI on pace to bypass cybersecurity systems in months, not years, "Five Eyes" spy partners warn](https://www.cbsnews.com/news/ai-bypass-cybersecurity-systems-months-not-years-five-eyes/)

---

### 7. Orca Security調査：修正可能なAI脆弱性の99.9%が未対応
**2026年7月13日**
Orca Securityの「2026 State of AI Security Report」（1,200組織超のテレメトリを分析）によると、AIパッケージを実行する企業の81.2%が既知の脆弱性を抱え、修正パッチが存在するAI脆弱性の99.9%が未適用のまま放置されている。AIが本番インフラ化する速度にセキュリティ対応が追いついていない実態が浮き彫りになった。

🔗 [99.9% of fixable AI vulnerabilities remain unpatched](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/)

---

## 🟡 Data & Privacy

### 8. 米下院、州法の分断を解消する連邦プライバシー法案「SECURE Data Act」を提出
**2026年4月22日**
下院エネルギー・商業委員会と金融サービス委員会は、州ごとに乱立するプライバシー法を一本化する「SECURE Data Act」を発表した。個人データへのアクセス・削除権、ターゲティング広告のオプトアウト、未成年データの保護強化などを規定し、FTCを執行機関とする一方、州法を優先的に無効化（プリエンプション）する内容も含む。

🔗 [Committees on Energy and Commerce and Financial Services Introduce Pair of Privacy Bills](https://energycommerce.house.gov/posts/committees-on-energy-and-commerce-and-financial-services-introduce-pair-of-privacy-bills-to-establish-comprehensive-data-protections-for-all-americans)

---

## 🟢 Security Governance

### 9. セキュリティ専門家の55.2%、「報告すべき侵害」を隠蔽するよう指示された経験
**2026年7月（Bitdefender 2026 Cybersecurity Assessment）**
6カ国1,200人のIT・セキュリティ専門家を対象にした調査で、過去12か月に侵害を経験した回答者の55.2%が「当局に報告すべきと考えたが、箝口令を敷かれた」と回答した。米国が68.6%と最も高く、インシデント対応における透明性の欠如が組織統治上の課題として指摘されている。

🔗 [Breach Transparency Remains Cybersecurity's Toughest Governance Problem](https://thehackernews.com/expert-insights/2026/07/breach-transparency-remains.html)

---

## 🟣 Crypto Currency

### 10. Injective Labs、GitHub侵害経由でウォレット秘密鍵窃取npmパッケージが拡散
**2026年7月8日**
攻撃者はInjective Labs SDKプロジェクトの正規開発者アカウントを通じてGitHubリポジトリに不正コードをコミットし、`@injectivelabs/sdk-ts@1.20.21`としてnpmに公開した。ウォレットキー生成・インポート関数の呼び出し時にシードフレーズと秘密鍵を窃取し外部サーバーへ送信する仕組みで、週間5万ダウンロードの人気パッケージを起点に17の関連パッケージにも波及した。

🔗 [Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Packages](https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | ゼロデイ、KEV、ランサムウェア、データ侵害 |
| AI Risk | 🟠🟠🟠 | AIガバナンス、脆弱性未対応、Five Eyes警告 |
| Data & Privacy | 🟡🟡 | 連邦プライバシー法、SECURE Data Act |
| Security Governance | 🟢🟢 | 侵害の透明性、インシデント報告義務 |
| Crypto Currency | 🟣🟣 | サプライチェーン攻撃、ウォレット窃取 |

---

*次回配信予定：2026年7月21日（火） | 収集ソース：The Hacker News, BleepingComputer, Dark Reading, SecurityWeek, CBS News, Cybersecurity Dive, Help Net Security, CISA, energycommerce.house.gov*
