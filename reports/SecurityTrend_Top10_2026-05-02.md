# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月2日（土）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **サプライチェーン攻撃** | npm等のオープンソースエコシステムやSaaS連携を狙った攻撃が急増。AIエージェント開発環境も標的となり、単一の侵害が広範な被害を引き起こす複合型脅威として定着しつつある。 |
| 2 | **AIソーシャルエンジニアリング** | 北朝鮮系ハッカーが生成AIやディープフェイク動画を悪用し、暗号資産企業幹部を狙うなど、AI活用型フィッシング・なりすまし攻撃が急速に高度化・量産化している。 |
| 3 | **ソースコード流出** | セキュリティベンダーTrellixがソースコードリポジトリへの不正アクセスを公表。セキュリティ製品自体のソースコードが狙われる事案は、二次的なゼロデイ攻撃リスクを孕むとして注目されている。 |
| 4 | **CIRCIA最終規則** | 米CISAが重要インフラへのサイバーインシデント報告を72時間以内に義務化する最終規則を2026年5月に公表予定。30万超の事業者に影響する歴史的規模のサイバーセキュリティ規制として注目が集まる。 |
| 5 | **EU AI Act施行** | 2026年8月2日に高リスクAIへの主要義務が全面適用となるEU AI Act。最大3,500万ユーロまたは年間売上高7%の制裁金を伴う執行権限が発動され、グローバル企業は対応を急いでいる。 |

---

## 🔴 Cyber Security

### 1. セキュリティ大手Trellixがソースコードリポジトリへの不正アクセスを公表
**2026年5月2日**

サイバーセキュリティ企業Trellixは、同社のソースコードリポジトリへの不正アクセスが発生したと発表した。同社は大手フォレンジック企業と連携して調査を開始し、法執行機関にも通報済み。現時点では「ソースコードのリリースや配布プロセスへの影響」および「ソースコードの悪用」の証拠は確認されていないとしているが、詳細の開示は調査進行に合わせて順次行う方針。セキュリティベンダー自身のソースコード流出は、未知の脆弱性発見や標的型攻撃への悪用につながるリスクが高く、業界全体が注視している。

🔗 [Trellix Confirms Source Code Breach With Unauthorized Repository Access - The Hacker News](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html)

---

### 2. Linuxの特権昇格脆弱性「Copy Fail」（CVE-2026-31431）が発覚、2017年以降ほぼ全ディストリビューションに影響
**2026年5月初旬**

CVSS 7.8の高深刻度脆弱性「CVE-2026-31431」（通称：Copy Fail）が公開された。非特権のローカルユーザーが732バイトのPythonスクリプトでsetuidバイナリを書き換えてroot権限を取得できる。2017年以降にリリースされたほぼ全てのLinuxディストリビューションが影響を受けるとされ、クラウドサーバーや組み込みシステムへの広範な被害が懸念される。早急なパッチ適用と権限管理の見直しが求められている。

🔗 [May 2026 Cyber Update - CyberNewsCenter](https://www.cybernewscentre.com/1st-may-2026-cyber-update-uk-survey-phishing-breach-economy/)

---

### 3. ADTがSalesforce/Okta SSO経由の侵害で550万人のデータ漏えいを確認
**2026年5月初旬**

ホームセキュリティ大手ADTが、Okta SSOを経由したSalesforceクラウドへの不正アクセスにより約550万人のユーザーデータが漏えいしたと発表した。2024年以来ADTにとって3度目の大規模侵害となり、SaaS連携のアイデンティティ管理における脆弱性が改めて浮き彫りとなった。クラウドSaaS経由のサプライチェーンリスクが高まる中、SSO・OAuth管理の強化とゼロトラスト導入の重要性が再認識されている。

🔗 [Supply Chain Attacks, AI Security, and Major Breaches - eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)

---

### 4. npmサプライチェーンワームがAIエージェント開発環境を標的に
**2026年4月〜5月**

AI企業Namastex Labsが管理する複数のnpmパッケージが自己複製型マルウェア「CanisterWorm」に感染。開発者環境内でシークレット情報や機密データを窃取しながら横展開することが確認された。AI開発エコシステムへのサプライチェーン攻撃は急増しており、オープンソース依存度の高いエンタープライズ環境では依存パッケージの継続的な監視とSBOM（ソフトウェア部品表）管理が不可欠となっている。

🔗 [Another npm Supply Chain Worm Hits Dev Environments - The Register](https://www.theregister.com/2026/04/22/another_npm_supply_chain_attack/)

---

### 5. 英国サイバーセキュリティ侵害調査：フィッシングが企業の38%・慈善団体の25%に影響
**2026年5月1日**

英国政府の2025/2026年度サイバーセキュリティ侵害調査によると、過去12ヶ月間にフィッシング攻撃を受けた企業は38%、慈善団体は25%に上ることが判明。フィッシングは最多かつ最も損害の大きいインシデント種別として引き続きトップを占めている。生成AIの活用によりフィッシングメールの精度が向上しており、従業員教育とメールセキュリティ対策の継続的な強化が喫緊の課題となっている。

🔗 [1st May 2026 Cyber Update: UK Survey Shows Phishing Still Owns the Breach Economy](https://www.cybernewscentre.com/1st-may-2026-cyber-update-uk-survey-phishing-breach-economy/)

---

## 🟠 AI Risk

### 6. 北朝鮮系ハッカーUNC1069がAI・ディープフェイクを駆使して暗号資産企業を攻撃、2026年は76%のクリプト被害を占める
**2026年5月**

北朝鮮と関連するハッカー集団UNC1069が、AIが生成したディープフェイク動画や偽Zoomミーティングを使った高度なソーシャルエンジニアリングで暗号資産企業の幹部を標的にしていることが明らかになった。2026年の暗号資産ハッキング被害のうち76%が北朝鮮系グループによるもので、2017年以来の累計被害は60億ドルを突破した。AIが言語バリアや偽人物の構築コストを劇的に低下させたことで、攻撃の精度と規模が急拡大している。

🔗 [North Korea-Linked UNC1069 Uses AI Lures to Attack Cryptocurrency Organizations - The Hacker News](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html)

🔗 [North Korea Linked to 76% Crypto Hacks in 2026 - Dark Reading](https://www.darkreading.com/cybersecurity-analytics/crypto-stolen-2026-north-korea)

---

### 7. Proofpoint調査：AI管理策を導入済みでも組織の半数がAIインシデントを経験
**2026年4月28日**

Proofpointが2026年AI・ヒューマンリスク状況報告書を公開。12ヵ国1,400人以上のセキュリティ専門家を対象とした調査によると、87%の組織がAIアシスタントを本番環境に展開済みであるにもかかわらず、AIセキュリティ管理策を導入している組織の52%は「それらが侵害を検知できるか自信がない」と回答。42%がAI関連の不審イベントまたはインシデントを経験しており、AI展開速度がセキュリティ成熟度を大きく上回っている実態が浮き彫りになった。

🔗 [Proofpoint Research Reveals Half of Global Organizations Experienced AI Incidents - Proofpoint](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-reveals-half-global-organizations-experienced-ai)

---

### 8. AIエージェントの急速普及でアイデンティティリスクが急拡大、Shadow AIが新たな盲点に
**2026年5月**

Grip Securityのレポートにより、AIエージェントの本番展開が加速する中でOAuthの乱用・非人間型アイデンティティ（NHI）の急増・サードパーティAIサプライチェーンリスクが主要な脅威として台頭していることが明らかになった。AIが生成したコードが安全でない実装を含む場合、そのまま本番環境への侵害経路となるリスクも指摘されている。AIレッドチーミングはニッチな研究領域から主流のエンタープライズセキュリティ機能へと移行しており、2028年までに需要が35%急増する見込み。

🔗 [Top AI Security Risks in 2026 - Grip Security](https://www.grip.security/blog/top-ai-security-risks-in-2026)

🔗 [The State of AI Risk Management in 2026 - eSecurity Planet](https://www.esecurityplanet.com/artificial-intelligence/the-state-of-ai-risk-management-in-2026-reveals-a-growing-confidence-gap/)

---

## 🟡 Data & Privacy

### 9. カリフォルニア州DELETE Actが2026年8月に施行、データブローカーへの一括削除請求が可能に
**2026年5月**

カリフォルニア州がDelete Actに基づいて設立するDROP（Delete Request and Opt-Out Platform）が2026年8月に正式ローンチする。消費者は単一のプラットフォームから全データブローカーへの一括削除リクエストを送信できるようになり、データブローカーはその処理が義務付けられる。米国では2026年にインディアナ・ケンタッキー・ロードアイランドで新たな包括的プライバシー法が施行され、19州が包括的なプライバシー法を有する状況となる。未成年者データ保護・自動意思決定規制・データブローカー透明性への規制強化が続く。

🔗 [Data Privacy Laws: What to Expect for 2026 - Ketch](https://www.ketch.com/blog/posts/us-privacy-laws-2026)

🔗 [U.S. Data Privacy Laws and Regulations in 2026 - Smarsh](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

## 🟢 Security Governance

### 10. CIRCIA最終規則が2026年5月公表予定、重要インフラに72時間以内のインシデント報告義務
**2026年5月**

米国土安全保障省CISAは、重要インフラ事業者にサイバーインシデント発生から72時間以内の報告とランサムウェア身代金支払いから24時間以内の報告を義務付けるCIRCIA（Cyber Incident Reporting for Critical Infrastructure Act）最終規則を2026年5月に公表する予定。16の重要インフラセクターで中小企業規模基準を超える30万超の事業者が対象となる。当初2025年10月が期限だったが、膨大なパブリックコメントの精査と他の連邦報告フレームワークとの整合性確保のため延期された経緯がある。

🔗 [CISA Pushes Final Cyber Incident Reporting Rule to May 2026 - CyberScoop](https://cyberscoop.com/cisa-pushes-final-cyber-incident-reporting-rule-to-may-2026/)

🔗 [CIRCIA FAQs - CISA](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/circia/faqs)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | ソースコード流出、特権昇格、サプライチェーン、フィッシング |
| AI Risk | 🟠🟠🟠🟠 | ディープフェイク、AIインシデント、Shadow AI、NHI |
| Data & Privacy | 🟡🟡🟡 | DELETE Act、データブローカー規制、未成年者保護 |
| Security Governance | 🟢🟢🟢🟢 | CIRCIA、72時間報告義務、EU AI Act施行 |

---

*次回配信予定：2026年5月3日（日） | 収集ソース：The Hacker News、Dark Reading、eSecurity Planet、Proofpoint、CyberScoop、The Register、Grip Security、Infosecurity Magazine、CISA*
