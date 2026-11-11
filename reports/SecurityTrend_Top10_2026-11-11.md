# セキュリティトレンド Top 10 ニュース
**配信日：2026年11月11日（水）**

> ⚠️ この記事はClaude AIとxAI Grok API（話題性分析）を組み合わせて収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **SSHole（OpenSSH CVE-2026-123158）** | 11月6日から実攻撃が観測されたOpenSSHの脆弱性。CISAがKEVに追加し、連邦機関の期限は11月12日。ボットネットやクリプトマイナーの展開にも使われている。 |
| 2 | **AIエージェントの攻撃転用** | 攻撃用に転用されたAntiFox、DeepSeekを脱獄させたBroadWorks攻撃、Chainalysis侵害など、エージェント型AIが実際の侵入に使われる事例が同時に複数出ている。 |
| 3 | **LLMjacking** | 盗んだLLMアクセスを不正なルーティングゲートウェイに転売する金銭目的の攻撃。Fireworks AI侵害ではモデル重み・データセット、Notion AIのチャット記録にまで被害が及んだ。 |
| 4 | **Shahid Kaveh（IRGC系OT攻撃）** | フランスが約700店舗の冷蔵設備攻撃をIRGC系部隊によるものと公式に断定し、イラン大使を召喚。重要インフラ・小売OTが地政学リスクの対象になっている。 |
| 5 | **ソーシャルログイン型ウォレット** | Web3Authの欠陥でGoogle/Appleログインで作ったKeplrウォレットの鍵が露出。利便性を優先した鍵管理基盤が単一障害点になるリスクが表面化した。 |

---

## 🔴 Cyber Security

### 1. OpenSSHの「SSHole」が実攻撃で悪用、CISAがIBM Aspera・FreeSWITCH・GPUStackと合わせてKEVに追加
**2026年11月9日〜10日**
CISAがOpenSSHの「SSHole」（CVE-2026-123158、CVSS 8.1）に加え、IBM Aspera Faspex、SignalWire FreeSWITCH、GPUStack（いずれもCVSS 9.8）の計4件をKEVに追加した。SSHoleは11月6日から悪用が確認され、GreyNoiseは6つのIPから侵入後の活動（18の攻撃チェーン）を確認。C2エージェント、ボットネット、クリプトマイナーの展開も報告されている。連邦機関の対応期限は11月12日で、インターネットに公開しているSSHサーバーは最優先でパッチを当てる必要がある。

🔗 [CISA Warns of Active Exploitation of OpenSSH, GPUStack, FreeSWITCH, and IBM Flaws（The Hacker News）](https://thehackernews.com/2026/11/cisa-warns-of-active-exploitation-of.html)
🔗 [Hackers exploit SSHole OpenSSH flaw to breach Linux systems（BleepingComputer）](https://www.bleepingcomputer.com/news/security/hackers-exploit-sshole-openssh-flaw-to-breach-linux-systems/)

---

### 2. Cisco BroadWorksのXXE脆弱性がKEV入り、脱獄したAIモデルを使った通信事業者攻撃の報告も
**2026年11月10日〜11日**
CISAがCisco BroadWorksのOCI XMLパーサーにある認証不要のXXE脆弱性（CVE-2026-20320、8月にパッチ公開済み）をKEVに追加した。BOD 26-04に基づく期限は11月24日。Malbear Labsは、中国語話者の攻撃者が脱獄させたDeepSeekモデルを使ってこの脆弱性を悪用し、欧州の通信事業者とそのデータセンターを使う13組織を攻撃して、秘密鍵やSSL認証情報を奪ったと主張している（ベンダーの主張であり、CISAは確認していない）。

🔗 [CISA flags Cisco BroadWorks flaw as actively exploited in attacks（BleepingComputer）](https://www.bleepingcomputer.com/news/security/cisa-flags-cisco-broadworks-flaw-as-actively-exploited-in-attacks/)
🔗 [CISA Adds Six Known Exploited Vulnerabilities to Catalog（CISA）](https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog)

---

### 3. N-able、N-centralの大量ゼロデイ公開を受けてセキュリティホットフィックスを公開（続報）
**2026年11月9日〜11日**
研究者がRMMプラットフォームN-centralの30件超のゼロデイを一斉に公開した問題で、N-ableはホスト環境をオフラインにしたうえでホットフィックスをリリースした。RMMはMSPを経由して多数の顧客環境に直結するため、オンプレミス利用者はホットフィックスの適用と、不審な管理者アカウントやログの監査を急ぐ必要がある。

🔗 [N-able releases security hotfixes for zero-day vulnerabilities（BleepingComputer）](https://www.bleepingcomputer.com/news/security/n-able-releases-security-hotfixes-for-zero-day-vulnerabilities/)
🔗 [N-able takes cloud platform offline after 30 zero-days published（BleepingComputer）](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-zero-days-published/)

---

## 🟠 AI Risk

### 4. オープンソースのAIペンテストエージェント「AntiFox」が実攻撃に転用、AWSのシークレットを窃取
**2026年11月11日**
Arctic Wolfによると、攻撃者はARTEX 0.1.1をフォークした中国語UIのエージェント型ペンテストツール「AntiFox」をAlibaba Cloud上で自前運用し、エクスプロイト、Webシェル設置、認証情報の検証、AWSシークレットの収集に使っていた。ある侵入では、有効なIAMユーザーとEC2ロールを使い、約30分で数百件のAPIリクエストを実行して本番環境のシークレットに到達した。別の事例ではS3オブジェクトの読み取り・コピー・削除も確認されている。

🔗 [Hackers use AntiFox AI agents in AWS credential-theft attacks（BleepingComputer）](https://www.bleepingcomputer.com/news/security/hackers-use-antifox-ai-agents-in-aws-credential-theft-attacks/)
🔗 [AntiFox AI pentesting platform linked to attacks（The Hacker News）](https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html)

---

### 5. Fireworks AIの侵害が拡大、モデル重み・データセットにも被害 ― LLMjackingグループの犯行と判断
**2026年11月10日**
AI推論基盤のFireworks AIが、10月に公表したインシデントの追加調査結果を公表した。攻撃者は10月23〜24日にサードパーティのクラウド上にある開発用マシンへ侵入し、課金情報、リソースのメタデータ、一部アカウントの未完成のモデル重みやデータセットにアクセスした。カード番号は保存されていなかった。犯行は、盗んだLLMアクセスを不正ゲートウェイに転売する金銭目的のLLMjackingグループによるものとみられる。AIサプライチェーン上の推論事業者が攻撃の標的になるリスクを示す事例だ。

🔗 [Fireworks AI Confirms Wider Breach Affecting Customer Datasets, Model Weights and Notion AI Chats（The Hacker News）](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html)
🔗 [AI company Fireworks says hackers stole data, billing info during October breaches（The Record）](https://therecord.media/ai-company-fireworks-says-hackers-stole-data-in-oct-attacks)

---

## 🟡 Data & Privacy

### 6. Maerskが買収先のレガシーシステムからのデータ流出を確認、WhiteArmorが500万ドルを要求
**2026年11月11日**
海運大手Maerskが、買収した企業のレガシーシステムへの不正アクセスとデータの持ち出しを確認した。ランサムウェアグループWhiteArmorは約100GBを窃取したと主張し、500万ドルを要求しているが、Maersk側は機密データ流出の規模について強く否定している。M&Aで引き継いだシステムの資産管理と統合の遅れが攻撃の入り口になりやすいことを改めて示した。

🔗 [Maersk confirms data breach as WhiteArmor ransomware demands $5 million（BleepingComputer）](https://www.bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million/)

---

### 7. Notion、Fireworks侵害で一部ワークスペースのAIチャット記録が露出したと公表
**2026年11月10日〜11日**
NotionのAI機能を支えるFireworks AIの侵害により、Notionワークスペースの1%未満で、Insights機能に使われていたNotion AIのチャット記録が露出した。ゼロリテンションを前提としていたAIプロバイダー側にデータが残っていた点が問題視されており、AI委託先でのデータ保持・削除契約が実際に守られているかを確認・監査する必要性が浮き彫りになった。

🔗 [Notion says Fireworks breach exposed customer AI chat transcripts（BleepingComputer）](https://www.bleepingcomputer.com/news/security/notion-says-fireworks-breach-exposed-customer-ai-chat-transcripts/)

---

## 🟢 Security Governance

### 8. フランスが約700店舗の冷蔵設備攻撃をIRGC系「Shahid Kaveh」によるものと断定、イラン大使を召喚
**2026年11月9日〜10日**
フランス外務省は、10月11〜12日に起きたDanfoss製冷蔵コントローラーへの攻撃を、イラン革命防衛隊（IRGC）系部隊「Shahid Kaveh」によるものと公式に断定した。約700の小売店舗が狙われ、少なくとも15件の火災が発生し、食品損失は数千万ユーロにのぼる。カルフールやルクレールなど大手チェーンが被害を受け、小規模水力発電施設のSchneider製システムも攻撃された。フランスはイラン大使を召喚し、制裁を検討している。11月の第2波（欧州6カ国、115店舗超）の攻撃者はまだ特定されていない。

🔗 [France blames Iranian hackers for supermarket attacks that sparked fires（BleepingComputer）](https://www.bleepingcomputer.com/news/security/france-blames-iranian-hackers-for-supermarket-attacks-that-sparked-fires/)
🔗 [France blames Iran for a cyberattack that heated supermarket refrigerators（SecurityWeek）](https://www.securityweek.com/france-blames-iran-for-a-cyberattack-that-heated-supermarket-refrigerators/)

---

## 🟣 Crypto Currency

### 9. Web3Authの欠陥でKeplrウォレットの秘密鍵が露出、4.4万超のウォレットから約600万ドルを「救出」
**2026年11月8日〜9日**
Web3Authの基盤の欠陥により、Google/Appleログインで作成したKeplrウォレットの秘密鍵が露出した。Web3Authは同じ経路を使って、危険にさらされたウォレットの資産を回収用ウォレットへ先回りして移した。Bitquery の分析では、4万4,000超のウォレットから少なくとも601万ドルが移されたが、これは窃取ではなく救出とみなされている。一方、GoPlusは少なくとも約100万ドルが盗まれたとしている。Keplrはソーシャルログインを停止した。MetaMaskへの影響は確認されていない。

🔗 [Web3Auth Flaw Exploited to Steal Keplr Crypto（The Hacker News）](https://thehackernews.com/2026/11/web3auth-flaw-exploited-to-steal-keplr.html)
🔗 [Web3Auth says it frontran hackers by moving $5.6 million out of exposed Keplr wallets（The Block）](https://www.theblock.co/news/defi/2026-11-08-web3auth-says-it-frontran-hackers-by-moving-5-6-million-out-of-exposed-keplr-wallets-436029)

---

### 10. ブロックチェーン分析大手Chainalysisがデータ侵害を公表、「攻撃的エージェント技術」が使われたと説明
**2026年11月**
暗号資産の追跡・捜査支援を担うChainalysisが、攻撃的なエージェント型AI技術を使った侵入によるデータ侵害を公表した。法執行機関や取引所が利用する分析基盤の事業者が狙われた点で、暗号資産エコシステムへの波及が懸念される。詳細な被害範囲は続報を確認したい（本項は一次記事の詳細を完全には確認できていない）。

🔗 [Chainalysis discloses data breach from "offensive agentic techniques"（BleepingComputer）](https://www.bleepingcomputer.com/news/security/chainalysis-discloses-data-breach-from-offensive-agentic-techniques/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | SSHole、CISA KEV、Cisco BroadWorks、N-central |
| AI Risk | 🟠🟠 | AntiFox、エージェント型攻撃、LLMjacking、Fireworks AI |
| Data & Privacy | 🟡🟡 | Maersk/WhiteArmor、Notion AIチャット記録、AI委託先 |
| Security Governance | 🟢 | IRGC・Shahid Kaveh、OT攻撃の公式断定、外交的対応 |
| Crypto Currency | 🟣🟣 | Web3Auth/Keplr、ソーシャルログイン、Chainalysis |

---

*次回配信予定：2026年11月12日（木） | 収集ソース：The Hacker News、BleepingComputer、CISA、SecurityWeek、The Record、The Block、xAI Grok API*
