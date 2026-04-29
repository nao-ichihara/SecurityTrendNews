I'll search for the latest security news across all 4 categories simultaneously!
# セキュリティトレンド Top 10 ニュース
**配信日：2026年4月29日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Agentic AI リスク** | AIエージェントが自律的にコード実行・システム操作を行う時代に突入し、過剰権限トークンや誤動作による本番データ消失など新種のリスクが顕在化 |
| 2 | **ShinyHunters** | Medtronic・ADTなど大手企業を次々と標的にしたサイバー犯罪グループ。ソーシャルエンジニアリングによるSalesforceデータ窃取など手口が高度化 |
| 3 | **SECURE Data Act** | 米共和党が提出した初の連邦包括プライバシー法案。州法の「パッチワーク」解消を目指す一方、Big Tech優遇との批判も集める注目の立法動向 |
| 4 | **VPN／リモートアクセス脆弱性** | CISAがFortinet・Microsoft・Adobeの6件の既知悪用脆弱性をKEVカタログに追加。AIが人間の対応時間を圧縮し、リモートアクセスが侵害の最短経路に |
| 5 | **EU AI Act 完全適用（8月）** | 2026年8月2日の完全施行を控え、AI意思決定の透明性・ガバナンス義務が企業コンプライアンスの最優先課題に浮上 |

---

## 🔴 Cyber Security

### 1. MedtronicへのShinyHunters侵害——900万件の個人情報が流出か
**2026年4月27〜28日 | SecurityWeek / DataBreachToday**


サイバー犯罪グループShinyHuntersがMedtronicから900万件の個人情報を窃取したと主張している。
Medtronicは連邦当局に対し、サイバー犯罪者が企業ITシステムに侵入したことを認めたが、医療機器製品・製造・流通業務への影響はなかったとしている。
医療機器大手への攻撃であり、患者データを含む可能性から影響範囲は広大。ランサム交渉の動向が引き続き注目される。

🔗 [ShinyHunters Claims Theft of 9 Million Medtronic Records](https://www.securityweek.com/)

---

### 2. ADT、顧客550万人分のデータ侵害——ShinyHuntersがSalesforce経由で窃取
**2026年4月27日 | GovInfoSecurity**


ホームセキュリティ大手ADTが、顧客の個人情報550万人分が流出したデータ侵害を受けたことが明らかになった。ShinyHuntersが犯行を主張しており、ADT社員へのソーシャルエンジニアリングを通じてSalesforceデータを窃取したとしている。
ソーシャルエンジニアリングを起点としたSaaSプラットフォーム侵害という手口は、あらゆる業界に刺さる教訓となる。

🔗 [ADT Data Breach Exposes 5.5 Million Customers](https://www.govinfosecurity.com/)

---

### 3. Windows Shellの高深刻度脆弱性CVE-2026-32202、野放し悪用を確認
**2026年4月28日 | The Hacker News**


Microsoftは月例パッチで修正済みのWindows Shellに影響する高深刻度脆弱性に関するアドバイザリを改訂し、この脆弱性（CVE-2026-32202、CVSSスコア4.3）が実際に野放しで悪用されていることを認めた。攻撃者が被害者に悪意あるファイルを送付・実行させることで、機密情報にアクセスできるスプーフィング脆弱性だ。
パッチ未適用環境には早急な対応が求められる。

🔗 [Microsoft Warns of Actively Exploited Windows Shell Vulnerability CVE-2026-32202](https://thehackernews.com/)

---

### 4. CISA、Fortinet・Microsoft・AdobeのKEVに6件を追加——FortiClientのSQLiはCVSS9.1
**2026年4月（月初） | The Hacker News**


CISAは月曜日、活発な悪用の証拠を理由に6件のセキュリティ欠陥をKnown Exploited Vulnerabilities（KEV）カタログに追加した。その中にはFortinet FortiClient EMSのSQLインジェクション脆弱性（CVE-2026-21643、CVSSスコア9.1）が含まれており、未認証の攻撃者が特定のHTTPリクエストで任意コードを実行できる。
先週、MicrosoftはStorm-1175と追跡する脅威アクターがCVE-2023-21529をMedusaランサムウェア配信に悪用していることを明らかにした。


🔗 [CISA Adds 6 Known Exploited Flaws in Fortinet, Microsoft, and Adobe Software](https://thehackernews.com/2026/04/cisa-adds-6-known-exploited-flaws-in.html)

---

### 5. 北朝鮮ハッカー、Calendly招待で仮想通貨狙いのソーシャルエンジニアリング攻撃
**2026年4月27日 | DataBreachToday**


北朝鮮のハッカーが仮想通貨業界の内部関係者を装い、CalendlyのカレンダーへのURLを承諾させる手口で標的を誘引している。このソーシャルエンジニアリング手法は、WindowsおよびmacOSシステムに暗号通貨スティーラーを感染させ、将来の囮に使うために実在人物の映像も収集することを目的としている。
信頼性の高いビジネスツールを悪用した多段攻撃に注意が必要。

🔗 [North Korean Hackers Use Calendly Invites for Crypto Theft](https://www.databreachtoday.com/)

---

## 🟠 AI Risk

### 6. Akamai調査：AI×APIリスクが急拡大——昨年のインシデント費用は平均70万ドル超
**2026年4月28日 | GlobeNewswire / Akamai**


Akamaiが新たな調査結果を発表し、各組織が十分なセキュリティやテストなしにAPIを急いで展開しており、リリース後の攻撃リスクにさらされていることが明らかになった。この「Akamai API Security Impact Survey」は1,840人のセキュリティ専門家を対象とした世界調査だ。
回答者の87%が過去1年間にAPIがらみのセキュリティインシデントを経験し、1件あたりの平均コストは70万ドルを超えた。
セキュリティチームはAI技術の保護を来年の最優先サイバーセキュリティ課題（38%）と位置づけている。


🔗 [Security Leaders Cite AI as a Risk Multiplier for APIs – Akamai Survey](https://www.globenewswire.com/news-release/2026/04/28/3282376/0/en/Security-Leaders-Cite-AI-as-a-Risk-Multiplier-for-APIs-in-New-Akamai-Survey.html)

---

### 7. AIガバナンスギャップ拡大——73%がAIツールを導入も実効ガバナンスは7%のみ
**2026年（最新調査） | Cybersecurity Insiders「AI Risk and Readiness Report 2026」**


調査対象組織の73%がAIツールを導入しているが、リアルタイムでセキュリティとポリシーを強制できるガバナンスが整っているのはわずか7%にとどまる。この66ポイントの構造的欠陥は、AI導入がコントロールの整備を上回るペースで続く中、拡大し続けている。
組織の90%がAIセキュリティ予算を増やしたにもかかわらず、29%は12ヵ月前より安全度が下がったと感じている。
予算拡大と現場のセキュリティ感覚の乖離が深刻な課題として浮かび上がっている。

🔗 [AI Risk and Readiness Report 2026 – Cybersecurity Insiders](https://www.cybersecurity-insiders.com/ai-risk-and-readiness-report-2026/)

---

### 8. CrowdStrike報告：AI悪用攻撃が89%増、平均ブレイクアウト時間は29分に短縮
**2026年4月 | Federal News Network / CrowdStrike Global Threat Report 2026**


CrowdStrikeの「2026 Global Threat Report」によると、AI活用型敵対者による攻撃は89%増加した。さらにAIが攻撃を加速させており、eCrimeの平均ブレイクアウト時間は29分まで短縮——2024年比で65%高速化されている。
防御側の対応時間が急速に失われており、AI活用型の自動防御への移行が急務となっている。

🔗 [Why DHS No Longer Has a Compliance Mindset for Cybersecurity](https://federalnewsnetwork.com/ask-the-cio/2026/04/why-dhs-no-longer-has-a-compliance-mindset-for-cybersecurity/)

---

## 🟡 Data & Privacy

### 9. 米共和党がSECURE Data Act提出——初の連邦包括プライバシー法案が議会に登場
**2026年4月22〜28日 | IAPP / The Hill**


2026年4月22日、下院エネルギー・商業委員会副委員長のジョン・ジョイス議員（共和党）が待望の包括的消費者プライバシー法案HR 8413を提出した。「SECURE Data Act」は2025年2月にブレット・ガスリー委員長が設立したPrivacy Working Groupの成果であり、第119議会における包括的消費者プライバシー規則の最初の試みだ。
連邦規制が存在しない中、数十の州法が空白を埋めようとしてきたが、テクノロジー業界は国内での事業運営に困難なルールの「パッチワーク」が生じると主張している。
民主党側からはBig Tech優遇との批判もあり、今後の審議が注目される。

🔗 [SECURE Data Act: Analysis of the New Federal Privacy Bill – IAPP](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill)

---

## 🟢 Security Governance

### 10. KPMG「Cybersecurity Considerations 2026」——非人間IDとサプライチェーンが最大優先事項に
**2026年4月24日 | Security MEA / KPMG**


機械ID・サービスアカウント・AIエージェントが人間ユーザーを数で上回り、攻撃対象領域を拡大させ、アイデンティティガバナンスを根本的に再定義しつつある。
KPMGの最新グローバルレポート「Cybersecurity Considerations 2026」によると、サイバーリスクはもはやITチームに限定された技術的問題ではなく、投資判断・規制コンプライアンス・長期競争力を左右するコアビジネス命題となっている。
サプライチェーンリスク・地政学的変化・非人間IDの管理がトップ優先事項として浮上しており、CISOの役割はビジネス戦略とサイバーセキュリティを整合させる前向きなリーダーへと拡張しつつある。


🔗 [KPMG Report: Eight Critical Cybersecurity Priorities Shaping 2026](https://securitymea.com/2026/04/24/kpmg-report-eight-critical-cybersecurity-priorities-shaping-2026/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | ShinyHunters, CVE-2026-32202, Fortinet KEV,