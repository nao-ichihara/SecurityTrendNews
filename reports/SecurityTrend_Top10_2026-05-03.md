# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月3日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Linuxカーネル特権昇格（CVE-2026-31431）** | 2017年以降の全Linuxディストリビューションに影響する深刻な脆弱性。わずか732バイトのスクリプトでroot権限が奪取可能。 |
| 2 | **AIエージェントセキュリティ** | 自律型AIエージェントが企業SaaS環境に急速に浸透し、非人間IDの管理・制御が2026年最大のリスク領域として浮上。 |
| 3 | **SECURE Data Act** | 米国下院が提出した連邦統一プライバシー法案。州法パッチワーク状態を解消すべく、FTC執行・データブローカー規制などを一本化。 |
| 4 | **Silk Typhoon（中国APT）** | 中国政府系ハッカーがアジア・NATOの政府・防衛セクターを標的にした新スパイキャンペーン「SHADOW-EARTH-053」が発覚。 |
| 5 | **CIRCIA（サイバーインシデント報告義務）** | 重大インシデント72時間・ランサムウェア支払い24時間以内の報告を義務付ける規則が2026年コンプライアンスの焦点に。 |

---

## 🔴 Cyber Security

### 1. セキュリティ企業Trellixがソースコードリポジトリへの不正アクセス被害を公表
**2026年5月3日（12時間前）**


サイバーセキュリティ企業Trellixは、ソースコードリポジトリへの不正アクセスを受け、ソースコードの「一部」が侵害されたと発表した。
同社は「大手フォレンジック専門家」と連携して即座に対応を開始し、法執行機関にも通知したとしている。
攻撃者がアクセスしたデータの詳細は開示されていないが、ソースコードが悪用された証拠はないとしている。


🔗 [Trellix Confirms Source Code Breach With Unauthorized Repository Access](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html)

---

### 2. Linuxカーネルに9年間潜伏した特権昇格ゼロデイ「Copy Fail」（CVE-2026-31431）
**2026年4月30日〜5月1日**


セキュリティ研究者が、ローカルの非特権ユーザーがroot権限を取得できるLinuxのローカル特権昇格（LPE）脆弱性（CVE-2026-31431、CVSSスコア7.8）の詳細を公開した。
この脆弱性はLinuxカーネルの暗号化サブシステム「algif_aead」モジュールのロジック欠陥に起因し、2017年8月のコミットで混入した。
Amazon Linux、RHEL、SUSE、Ubuntuなど2017年以降にリリースされた事実上すべてのLinuxディストリビューションが影響を受ける。


🔗 [Linux Local Privilege Escalation Flaw CVE-2026-31431](https://thehackernews.com/)

---

### 3. 中国系APT「SHADOW-EARTH-053」がアジア・NATO政府を標的に大規模スパイ活動
**2026年5月1日**


セキュリティ研究者が、南・東・東南アジアの政府・防衛セクターとNATO加盟欧州政府1カ国を標的にした新たな中国系スパイキャンペーンを開示した。Trend Microは「SHADOW-EARTH-053」として追跡しており、少なくとも2024年12月から活動中とされる。
このグループはMicrosoft ExchangeやIISサーバーのN-day脆弱性（ProxyLogonなど）を悪用し、Webシェル「Godzilla」とDLLサイドローディングでShadowPadインプラントを展開する。


🔗 [China-Linked Hackers Target Asian Governments, NATO State](https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html)

---

### 4. 英国サイバーセキュリティ侵害調査：フィッシングが依然として侵害の主要経路
**2026年5月1日**


英国の2025/2026年サイバーセキュリティ侵害調査では、企業の43%・慈善団体の28%が過去1年間にサイバーインシデントを報告した。
フィッシングが最も一般的で破壊的なインシデントタイプであり、企業の38%・慈善団体の25%が過去12カ月にフィッシング攻撃を報告。被害組織に限れば、約85〜86%でフィッシングが関与していた。


🔗 [1st May 2026 Cyber Update: UK Survey Shows Phishing Still Owns the Breach Economy](https://www.cybernewscentre.com/1st-may-2026-cyber-update-uk-survey-phishing-breach-economy/)

---

### 5. CordialSpider・SnarkySpiderがVishing・SSO悪用でSaaS環境に高速侵入
**2026年5月1日**


セキュリティ研究者は、SaaS環境内でほとんど痕跡を残さずに「迅速かつ高インパクトな攻撃」を実行する2つのサイバー犯罪グループへの警戒を呼びかけている。
Cordial Spider（別名BlackFile、UNC6671）とSnarky Spider（別名UNC6661）の2グループが、VishingとSSO悪用を組み合わせた高速データ窃取を行っていると属性付けされている。


🔗 [Cybercrime Groups Using Vishing and SSO Abuse in Rapid SaaS Extortion Attacks](https://thehackernews.com/2026/05/cybercrime-groups-using-vishing-and-sso.html)

---

## 🟠 AI Risk

### 6. Proofpoint調査：グローバル企業の半数がAIセキュリティ管理を導入しても侵害を経験
**2026年4月28日**


Proofpointは「2026 AI and Human Risk Landscape」レポートを発表。12カ国1,400人以上のセキュリティ専門家を対象に、AIの急速な導入によって企業コラボレーションのセキュリティコントロールとインシデント対応に構造的な弱点が露呈していることを調査した。
「AIは既存のリスクを機械的なスピードとスケールで増幅させている。信頼できないコードの実行、機密データの誤処理、認証情報の紛失は、人間が数十年にわたり引き起こしてきた課題であり、AIはそれを機械速度で実行する」と指摘している。


🔗 [Proofpoint 2026 AI and Human Risk Landscape Report](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-reveals-half-global-organizations-experienced-ai)

---

### 7. 米・英・豪政府が共同警告：Agentic AIの拡大する攻撃対象領域
**2026年5月（直近）**


Forbes、CyberScoop、Bloomberg Lawの各メディアが、AIエージェントのセキュリティ脆弱性・ID脅威・AIガバナンス警告を相次いで報道。
Bloomberg Lawは、米国・英国・オーストラリアの政府機関が連名でAIエージェントシステムの攻撃対象領域拡大について共同警告を発したと報じた。
AI関連攻撃は前年比490%近く増加しているとする調査結果も示されており、業界全体の警戒水準が急上昇している。


🔗 [AI Agents News May 2026 – Agentic AI Risk](https://blog.mean.ceo/ai-agents-news-may-2026/)

---

### 8. Trend Micro 2026年セキュリティ予測：「AIによるサイバー脅威の自動化」が主要リスクに
**2026年（継続トレンド）**


サイバー脅威はかつてないほど高速・自動化・協調的になっており、AIがサイバー犯罪の規模・速度・高度化を牽引するエンジンとなっている。
「Vibe coding」の開発プラットフォームへの統合で迅速なプロトタイプ作成が可能になった一方、AI生成コードは安全性が低く、本番システムへの攻撃経路を生む可能性があると警告している。


🔗 [The AI-fication of Cyberthreats: Trend Micro Security Predictions 2026](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/predictions/the-ai-fication-of-cyberthreats-trend-micro-security-predictions-for-2026)

---

## 🟡 Data & Privacy

### 9. 米国下院、連邦統一プライバシー法案「SECURE Data Act」を提出
**2026年4月22日**


2026年4月22日、下院エネルギー・商業委員会が「SECURE Data Act」（消費者権利の確保と統一施行を目的とした包括的連邦プライバシー法案）を提出。現在の州法パッチワーク状態を単一の国家的枠組みで置き換えることを意図している。
同法案は連邦データブローカー基準を設け、FTCへの登録と公開開示を義務付ける。また最も議論を呼ぶ条項として、州法を連邦法で先取りする「プリエンプション条項」を含んでいる。


🔗 [House Introduces SECURE Data Act to Establish a Federal Privacy Framework](https://www.clarkhill.com/news-events/news/comprehensive-federal-privacy-bill-secure-data-act-introduced-by-house-republicans/)

---

### 10. EU AI法（EU AI Act）が2026年8月2日に完全施行へ
**2026年（施行予定）**


EU AI Actは2026年8月2日に完全施行となり、企業はAIによる消費者への意思決定を説明する義務を負う。また欧州委員会の「Digital Omnibus Regulation」提案による改正も想定されている。
EU AI Actの完全適用により（一部高リスク製品は2027年まで延長）、日本企業を含むグローバル企業に対しても対応が急務となっている。


🔗 [Global Data Privacy Laws: What to Look For in 2026](https://cdslegal.com/insights/global-data-privacy-laws-the-current-environment-and-what-to-look-for-in-2026/)

---

## 🟢 Security Governance

### 11. CIRCIA・NIST CSF 2.0がサイバーインシデント報告・ガバナンス体制を再定義
**2026年（施行中）**


連邦インシデント報告に関する勢いが加速しており、CIRCIA（重要インフラ向けサイバーインシデント報告法）とCISAによる規則制定が進行中。重大インシデントを72時間以内・ランサムウェア支払いを24時間以内に報告することを対象事業者に義務付ける規則案が提示されている。
NIST Cybersecurity Framework 2.0の公開により、法務・コンプライアンス・広報・経営幹部を統合したインシデント対応計画を求める、ガバナンス主導のサイバーセキュリティプログラムに関する連邦の期待値が明確化された。


🔗 [Cybersecurity & Privacy 2026: Enforcement & Regulatory Trends](https://www.morganlewis.