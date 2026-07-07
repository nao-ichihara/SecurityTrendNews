I'll search all 5 categories simultaneously to gather the latest security news!
収集完了。全カテゴリのデータを統合してTop10レポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月7日（火）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVE-2026-45659 (SharePoint RCE)** | CISAがKEVカタログに追加したMicrosoft SharePointの高危険度RCE脆弱性。認証済み攻撃者がリモートコード実行可能で、連邦機関へのパッチ適用が緊急命令されている。 |
| 2 | **AIガバナンス（Agentic AI）** | 国連が7月6〜7日にジュネーブで初のAIガバナンス対話を開催。企業・政府レベルのAIエージェント管理とリスク統制が最重要テーマに浮上。 |
| 3 | **FortiBleed / FortiGate クレデンシャル窃取** | 数十万台のFortiGateファイアウォールから盗まれた認証情報が、INC・Lynxランサムウェアグループの次の侵入に悪用されると警告。 |
| 4 | **米国プライバシー法ラッシュ（State Privacy Laws）** | 2026年7月より、アーカンソー州・コネチカット州（ニューラルデータ含む）などで新たなプライバシー法が施行。米国全20州に広がる複雑なコンプライアンス対応が必至。 |
| 5 | **暗号詐欺AI化（AI-Enabled Crypto Fraud）** | 2025年のChainalysis報告によるとAIなりすまし詐欺が前年比1,400%増。2026年も手口がさらに高度化し、deepfakeを用いたソーシャルエンジニアリングが主要脅威となっている。 |

---

## 🔴 Cyber Security

### 1. CISAがSharePoint RCEをKEVに追加——Storm-2603ランサムウェアとの関連も浮上
**2026年7月2日（BleepingComputer / The Hacker News）**


CISAは、Microsoft SharePoint Serverに影響する高危険度の脆弱性（CVE-2026-45659、CVSSスコア8.8）を既知悪用脆弱性（KEV）カタログに追加した。この脆弱性は、信頼されていないデータのデシリアライズに起因するリモートコード実行の欠陥だ。
 
Microsoftによれば、認証済みの攻撃者であれば管理者権限なしでも悪用可能であり、最低限のサイトメンバー権限でSharePoint Server上でコードをリモート実行できる。
 
また先月、Microsoftはルーティンなランサムウェア調査中に、同一ネットワーク内で2つの無関係な攻撃者が同時に活動していたことを発見。そのうち一方がKnown脆弱性を悪用するWarlock ランサムウェアを展開するStorm-2603と特定されている。


🔗 [SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html)

---

### 2. FortiBleedキャンペーン——INC・Lynxランサムウェアへの"燃料"に
**2026年7月2日（BleepingComputer / SecurityWeek）**


FortiGateから大量の認証情報を窃取した「FortiBleed」キャンペーンが、INCおよびLynxランサムウェアオペレーションとリンクされており、盗まれたFortinet認証情報が将来のネットワーク侵入に利用される意図があることが示唆されている。
 
研究者らは、数十万台のFortiGateファイアウォールから収集された認証情報が、INCおよびLynxオペレーションによるランサムウェア攻撃の実行に使用されていると報告している。
 この大規模なクレデンシャル窃取キャンペーンは、境界セキュリティ機器自体が攻撃の踏み台になるという新たなリスクモデルを示しており、世界中の企業ネットワークへの影響が懸念される。

🔗 [FortiBleed Credential Theft Campaign Linked to Ransomware](https://www.bleepingcomputer.com/news/security/)

---

### 3. KDDIで最大1,420万件のメールアカウント情報が流出——日本の通信行政も動く
**2026年7月6日（Bright Defense / Cybernews）**


KDDIは、2026年6月に発生したデータ侵害により、最大1,420万件のISPアカウントのメールアドレスとパスワードが漏洩した可能性があると開示した。同社は6月17日に不正アクセスを検知し、攻撃者をブロックして防御措置を追加した。
 
攻撃者はKDDIの共有メールインフラに接続されたサードパーティソフトウェアの脆弱性を悪用。一部のパスワードは暗号化されていたが、保護されていたアカウントの数は未開示とされている。
 
日本の総務省は後に、電気通信事業法に基づき、7月6日までに報告書を提出するようKDDIに命令した。


🔗 [List of Recent Data Breaches in 2026](https://www.brightdefense.com/resources/recent-data-breaches/)

---

### 4. AirDrop・Quick Shareに6件のセキュリティ欠陥——50億台のデバイスに影響
**2026年7月2日（Cybernews）**


AppleのAirDropとAndroidのQuick Shareに脆弱性が発見された。約50億台のiPhoneとAndroid端末がファイル転送のために受信待機状態にあり、近傍の攻撃者がクラッシュ誘発・転送妨害・さらにはコード実行を行える可能性がある。研究者らはプロトコルを検査し、6件のセキュリティ欠陥を公開した。
 ワイヤレス近接通信機能の広範な普及がもたらすリスクとして、特に公共の場での利用に注意が必要だ。プロトコル設計レベルの脆弱性であるため、パッチ適用状況の継続的な確認が推奨される。

🔗 [Apple AirDrop and Android Quick Share Vulnerabilities](https://cybernews.com/)

---

## 🟠 AI Risk

### 5. 国連がAIガバナンスへの緊急行動を要請——初の「国連AIガバナンス対話」開催
**2026年7月6〜7日（UN News）**


2026年7月6〜7日、ジュネーブで初の「国連AIガバナンスに関するグローバル対話」とAI for Good Summitが開催された。国連事務総長グテーレス氏は、これらが世界に方向性を示さなければならないと強調した。
 
AIは「21世紀の偉大な平等化装置」となりうると述べる一方、「各国が安全基準、リスク評価、責任の割り当てについて合意したとき、安全性は技術とともに伝播する。そうでなければ、互換性のないルールが世界を分断し、誰も守れない」と警告した。
 
同氏はまた、「デジタルデバイドがAIデバイドとなり、安全保障格差・主権格差に発展することは許されない」とも訴えた。


🔗 [From AI to 'killer robots': UN chief issues urgent governance call](https://news.un.org/en/story/2026/07/1167873)

---

### 6. 中国系アクターがAI企業へのスパイ活動を加速——FBIが警告
**2026年7月1日（CNBC）**


「中国の経済スパイキャンペーンは、アメリカ経済に年間数千億ドルのコストをもたらし、国家安全保障を脅かす継続的な脅威だ」とFBIはCNBCに声明を発した。
 
DeepSeekのリリースが米中AIレースに火をつけた過去18ヶ月間で、中国の攻勢が顕著に増加しており、「中国はAIレースで中国企業を先頭に立たせようとしており、米国のAI企業の発展を抑制するために、サプライチェーン制限、従業員嫌がらせ、ハッキングなどの戦略を採る」と専門家は指摘する。
 
人間の脆弱性がより大きなリスクをもたらしており、特に攻撃者がAI強化コンテンツキャンペーンで増幅させた「ソーシャルエンジニアリング」戦術が問題だという。


🔗 [China-linked actors target more than technology as AI competition intensifies](https://www.cnbc.com/2026/07/01/china-ai-cyberattacks-startups-insider-risks-espionage.html)

---

## 🟡 Data & Privacy

### 7. 米国プライバシー法が7月に新ステージへ——アーカンソー法施行・コネチカットがニューラルデータを保護対象に追加
**2026年7月（Smarsh / Secure Privacy）**


2026年には、組織が米国の20近い州のデータプライバシー法に対応しなければならないという状況が続いている。当初はカリフォルニア州のCCPAとCPRAを中心としていたが、現代のプライバシー環境はより広範なものとなっている。
 
アーカンソー州では2026年7月より新たなプライバシー法が発効。未成年者データ・自動意思決定・データブローカーの透明性への規制フォーカスが強まっている。
 
コネチカット州は7月1日より、「ニューラルデータ」をセンシティブデータのカテゴリに追加した。
 さらに
コネチカット州のCTDPAに基づき、7月1日より個人データがChatGPT・Gemini・DeepSeekなどの大規模言語モデルの学習に使用されているかどうかを開示する義務が企業に課された。


🔗 [U.S. Data Privacy Laws and Regulations in 2026](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

### 8. 米国 SECURE Data Act 提出——連邦統一プライバシー法の実現なるか
**2026年4月22日（Clark Hill）**


2026年4月22日、下院エネルギー・商業委員会が「消費者の統一権利・データ執行確立法（SECURE Data Act）」を提出した。現在の州法パッチワークを単一の国家統一フレームワークに置き換えることを目的とする包括的な連邦プライバシー提案だ。
 
個人はデータへのアクセス・修正・削除・ポータブルコピー取得の権利を持ち、ターゲット広告・個人データ販売・一定のプロファイリング活動へのオプトアウト手段が提供されなければならない。
 連邦統一プライバシー法への長年の議論が具体化しつつあり、成立すれば各州プライバシー法の上位規範として機能するため、企業のコンプライアンス体制に根本的な変化をもたらしうる。

🔗 [House Introduces SECURE Data Act to Establish a Federal Privacy Framework](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

## 🟢 Security Governance

### 9. 「インシデント隠蔽」が業界最大のガバナンス課題——Bitdefender 2026レポートが警告
**2026年7月7日（The Hacker News）**

