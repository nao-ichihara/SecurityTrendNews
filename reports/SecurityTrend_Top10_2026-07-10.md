I'll search all 5 categories simultaneously to gather the latest security news.
収集完了。全カテゴリのデータを統合し、Top10レポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月10日（金）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AIエージェント攻撃（JADEPUFFER）** | 
セキュリティ企業Sysdigが、AIエージェント「JADEPUFFER」が侵入から恐喝まで全プロセスをエンドツーエンドで自動実行したランサムウェア攻撃事例を報告。
マシンスピードのサイバー攻撃時代の到来を告げる。 |
| 2 | **BlueHammer / CVE-2026-33825** | 
CISAがMicrosoft Defenderの脆弱性「BlueHammer（CVE-2026-33825）」がランサムウェア攻撃に悪用されたと確認。2026年4月にゼロデイとして初めて公開された。
 |
| 3 | **Claude Codeバックドア疑惑** | 
中国がAnthropicのAIコーディングツール「Claude Code」にバックドアリスクがあると警告。アリババは7月10日付で従業員のAnthropicツール使用を禁止した。
 |
| 4 | **SECクリプト規制案（Regulation Crypto）** | 
SECが2026年7月に大規模な暗号資産ルール改定を発表。「Regulation Crypto」として登録免除や発行体向けセーフハーバーの新設などが含まれる可能性がある。
 |
| 5 | **米国州プライバシー法ラッシュ（20州体制）** | 
2026年3月時点でアメリカの20州が包括的プライバシー法を有し、インディアナ・ケンタッキー・ロードアイランドの3州が2026年に施行開始。
企業のマルチ管轄コンプライアンス負担が急増している。 |

---

## 🔴 Cyber Security

### 1. Microsoft SharePoint RCE脆弱性（CVE-2026-45659）がCISA KEVに追加され積極悪用が進行中

**2026年7月9日 | SecurityWeek / The Hacker News**


CISAが、Microsoft SharePoint Serverに影響する高重大度の脆弱性「CVE-2026-45659」（CVSSスコア8.8）を既知悪用脆弱性（KEV）カタログに追加した。この脆弱性は、非信頼データのデシリアライズに起因するリモートコード実行の問題である。
認証済み攻撃者であれば管理者権限なしでも発動でき、最小限のサイトメンバー権限でSharePointサーバー上でリモートコードを実行できる。
一連の攻撃の一部はStorm-2603によるものと帰属され、同グループはWarlock ransomwareを展開することで知られる。


🔗 [SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html)

---

### 2. Linuxカーネルに2011年以降の全主要ディストリビューションに影響するroot権限取得脆弱性

**2026年7月9日 | SecurityWeek**


2011年以降のすべての主要Linuxディストリビューションに影響するLinuxカーネル脆弱性が確認されており、攻撃者がroot権限を取得できる状態にある。
「Bad Epoll（CVE-2026-46242）」と呼ばれるこの欠陥は、特別なアクセス権を持たない一般ユーザーがマシンをroot権限で完全に掌握することを可能にし、Linuxデスクトップ・サーバー・Androidに影響する。
特権を持たない攻撃者が、カーネルの欠陥を通じてLinuxやAndroidシステムを完全なroot制御に昇格させ、マルチテナントワークロードの完全侵害につながるおそれがある。


🔗 [Weekly Threat Intelligence: The July 2026 Breaches](https://securityonline.info/weekly-threat-intelligence-july-2026/)

---

### 3. FBI監視システムに中国スパイが侵入―「重大サイバーインシデント」を宣言

**2026年7月7日 | TechCrunch**


米連邦捜査局（FBI）は、監視システムの1つが侵害されたことを確認し「重大サイバーインシデント」を宣言、議会への法的開示義務を果たした。この侵害では捜査員の盗聴対象者の電話番号が漏えいした可能性があり、中国のスパイが非機密ネットワークに不正アクセスしたと非難されている。
この侵害は米国の国家安全保障に対する「実証可能な損害」の基準に達したとみられる。


🔗 [The Worst Hacks and Breaches of 2026 So Far](https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/)

---

### 4. CISA、Adobe ColdFusion・LangflowほかKEV脆弱性4件をリスト追加―連邦機関に7月10日までパッチ適用命令

**2026年7月 | SecurityWeek / SecurityOnline**


Adobe ColdFusionおよびLangflowの重大な脆弱性2件が、Joomlaの拡張機能の欠陥2件とともにCISAの既知悪用脆弱性カタログに追加され、連邦機関には7月10日までのパッチ適用が義務付けられた。
Adobe ColdFusionはすでに大規模な悪用に直面しており、重大なパストラバーサル欠陥（CVE-2026-48282）がハッカーにシステムへの深いアクセスを許している。
また、IBM Langflow OSSには深刻なシークレット読み取り脆弱性（CVE-2026-10134）が存在し、攻撃者はすべてのアクティブプロセスシークレットを読み取り、AIワークフローを無制限に変更できる状態にある。


🔗 [SecurityWeek - Cybersecurity News](https://www.securityweek.com/)

---

## 🟠 AI Risk

### 5. 中国、Anthropic「Claude Code」のバックドアリスクを警告―アリババが7月10日付で使用禁止

**2026年7月8〜9日 | CNBC**


中国は、米国のAI企業AnthropicのAIコーディングツール「Claude Code」に「バックドア」セキュリティリスクがあると警告した。これは米中ハイテク競争が激化するなかで発生しており、Anthropicは先月、中国のAlibabaが自社AIの能力を不正に抽出しようとしたと非難していた。
中国の工業・情報化省はサイバーセキュリティ脅威プラットフォームが「Claude Codeには深刻な脅威をもたらすバックドア脆弱性が含まれている」と認定したと発表した。
なお、アリババは同日付けで全従業員へのAnthropicツール利用停止を通達した。

🔗 [China warns about AI risks with Anthropic's Claude Code](https://www.cnbc.com/2026/07/08/china-anthropic-ai-claude-code-backdoor-security-threat.html)

---

### 6. EU、医療・銀行・電力網を対象にAIサイバーセキュリティ試験プラットフォームを発表

**2026年7月7日 | 欧州委員会**


欧州委員会は、サイバーセキュリティにおける先進AIのリスクに対処し機会を活用するための計画を発表した。AIはセキュリティを向上させる一方で、脆弱性の特定や攻撃の自動化・規模拡大にも悪用されうると指摘し、EU加盟国・産業・EU機関が連携して対策を強化する方針を示した。
EUサイバーセキュリティ機関（ENISA）と欧州委員会の共同研究センター（JRC）は、模擬環境も活用しながらAIをサイバーセキュリティ用途でテストするためのセキュアなプラットフォームを構築予定で、重要インフラ事業者へのAI安全活用ノウハウを提供する。


🔗 [New EU plan to address the risks and opportunities of advanced AI for cybersecurity](https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en)

---

## 🟡 Data & Privacy

### 7. 米国20州体制が完成―アーカンソー新法も7月施行、AI・未成年データへの規制が強化

**2026年7月 | Smarsh / Secure Privacy / MultiState**


2026年、米国では約20州が独自の包括的プライバシー法を導入しており、組織はかつてカリフォルニアのCCPA/CPRAが中心だった時代よりはるかに広範な規制環境への対応を迫られている。
アーカンソー州では2026年7月に新たなプライバシー法が施行され、未成年のデータ・自動意思決定・データブローカーの透明性に対する規制の強化が図られる。
また、コネチカット州は7月1日付でニューラルデータを機微情報カテゴリに追加し、EUのAI法は2026年8月2日に完全施行を迎える。


🔗 [U.S. Data Privacy Laws and Regulations in 2026](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

### 8. Bitdefender調査：侵害を経験した企業の55%が当局報告を抑制―ガバナンス危機が浮き彫りに

**2026年7月 | The Hacker News / Bitdefender**


セキュリティインシデントや侵害を経験した回答者の55.2%が、当局に報告すべきと自覚しながらも機密扱いにするよう指示されたと回答。米国では68.6%と最も高く、ドイツ・英国が57.2%で続いた。
これらの調査結果は、組織がインシデント発生時にどう対応し、どれだけ透明性を持てるか、そして内部文化がコンプライアンス・説明責任・信頼を支えているかという、より広いガバナンス課題を示している。


🔗 [Breach Transparency Remains Cybersecurity's Toughest Governance Problem](https://thehackernews.com/expert-insights/2026/07/breach-transparency-remains.html)

---

## 🟢 Security Governance

### 9. 企業の55%がAIを導入するも、ガバナンスフレームワークが整備されているのはわずか26%

**2026年7月8日 | Corporate Compliance Insights**


SmarshとFTIコンサルティングの新たな調査によると、企業の55%がAIを積極的に導入している一方、ガバナンスフレームワークが導入ペースと完全に整合していると回答した企業はわずか26%にとどまった。
「AIの活用が進むにつれ、個々の従業員は独自にスキルアップを図るようになる。一部の組織では、シャドーITアプリや教育不足による利用、ハルシネーションが引き起こす誤った成果物が