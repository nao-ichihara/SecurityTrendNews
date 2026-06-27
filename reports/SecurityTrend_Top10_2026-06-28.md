# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月28日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVE-2026-12569（PTC Windchill）** | CVSS 9.3のRCE脆弱性。パッチ公開後も悪用が続き、CISAのKEVカタログに初めて追加された。 |
| 2 | **MCP（Model Context Protocol）セキュリティ** | AIコーディングアシスタントの設定ファイル経由でクラウド資格情報が窃取される新型サプライチェーンリスクが浮上。 |
| 3 | **Five Eyes AI警告** | 米英加豪NZの情報機関が「AIが数年でなく数ヶ月で防御網を突破する」と共同声明で警鐘。 |
| 4 | **MiCA（EU暗号資産規制）** | 移行期限の7月1日を控え、Binanceなど大手取引所がEU向けサービス停止に追い込まれている。 |
| 5 | **ロシア情報機関（RIS）のメッセージング詐取** | SMSフィッシングで政府関係者のSignal等バックアップ復元キーを狙う長期キャンペーンが発覚。 |

---

## 🔴 Cyber Security

### 1. PTC Windchillの重大RCE脆弱性、パッチ後も実環境で悪用継続
**2026年6月25日〜**
CVSS 9.3の入力検証不備（CVE-2026-12569）がPTC WindchillおよびFlexPLMに存在し、未認証の攻撃者がJSP Webシェルを設置して任意コードを実行できる。パッチ公開後も攻撃が続き、CISAはKnown Exploited Vulnerabilities（KEV）カタログに追加。自動車・航空・防衛分野での知財流出リスクが指摘されている。

🔗 [CISA Adds Exploited PTC Windchill RCE Flaw to KEV as Web Shell Attacks Continue](https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html)

---

### 2. Amazon Q DeveloperのMCP連携に重大欠陥、クラウド資格情報が窃取可能
**2026年6月26日（公開）**
Wiz Researchが発見したCVE-2026-12957（CVSS 8.5）は、悪意あるリポジトリ内の`.amazonq/mcp.json`を開くだけでAmazon Qが自動的にMCPサーバーを起動し、開発者のAWS認証情報をクリック不要で攻撃者サーバーへ送信できる脆弱性。AIコーディング支援ツールのMCP自動実行が新たな攻撃ベクトルであることを示した。

🔗 [Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs](https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html)

---

### 3. SSUとFBI、ロシア情報機関によるメッセージングアプリ詐取キャンペーンを暴露
**2026年6月25〜26日**
ウクライナ保安庁（SSU）と米FBIは、ロシア情報機関（RIS）がウクライナ・欧州・米国の政府高官、軍人、活動家らのSignal等メッセージング account を狙い、サポート窓口を装ったSMSフィッシングでバックアップ復元キーを詐取する長期作戦を実施していたと共同発表した。

🔗 [Ukraine Says Russian Intelligence Used Fake Support Texts to Steal Messaging Credentials](https://thehackernews.com/2026/06/ukraine-says-russian-intelligence-used.html)

---

### 4. ポーランド警察、通信会社侵入とSIMスワップ詐欺の組織犯罪グループ4人を逮捕
**2026年6月下旬**
通信事業者のパートナー企業に侵入してメールアカウントを乗っ取り、SIMスワッピング攻撃を行っていたとされる組織犯罪グループのメンバー4人がポーランド当局に逮捕された。サプライチェーン経由の通信事業者侵害が個人口座乗っ取りに直結する事例として注目されている。

🔗 [The Hacker News | #1 Trusted Source for Cybersecurity News](https://thehackernews.com/)

---

### 5. Linuxカーネルに権限昇格の脆弱性、ローカルユーザーがroot権限取得可能
**2026年6月**
ファイルバックメモリの破損を悪用してローカルユーザーがroot権限を取得できるLinuxカーネルの脆弱性（CVE-2026-43503、CVSS 8.8）が報告された。サーバー・クラウド基盤での悪用リスクが懸念される。

🔗 [The Hacker News | #1 Trusted Source for Cybersecurity News](https://thehackernews.com/)

---

## 🟠 AI Risk

### 6. Five Eyes、AIが数ヶ月内に政府・企業の防御網を突破すると共同警告
**2026年6月23日**
米英加豪NZの情報機関連合「Five Eyes」は、大規模サイバー攻撃を仕掛けられるAIモデルの登場が「数年でなく数ヶ月」の規模で迫っていると共同声明を発表。各国政府・企業に対し、防御強化のため「今すぐ行動する」ことを求めた。CrowdStrikeの報告でもAI利用攻撃が前年比89%増加している。

🔗 [AI on pace to bypass cybersecurity systems in months, not years, "Five Eyes" spy partners warn](https://www.cbsnews.com/news/ai-bypass-cybersecurity-systems-months-not-years-five-eyes/)

---

### 7. Anthropic、米政府の国家安全保障指令でFable 5・Mythos 5へのアクセスを停止
**2026年6月12〜13日**
米政府は国家安全保障上の権限を根拠に、AnthropicのFable 5・Mythos 5モデルについて、外国籍ユーザー（社員含む）への全アクセスを停止するよう輸出管理指令を発出。背景には脱獄（jailbreak）手法発見への懸念があるとされ、Anthropicは「過剰な対応」として異議を唱えている。

🔗 [Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

---

## 🟡 Data & Privacy

### 8. 米国の州データプライバシー法、2026年も拡大続く
**2026年（継続中）**
インディアナ、ケンタッキー、ロードアイランドの3州で新たな包括的データプライバシー法が施行され、米国で消費者データ権を規制する州はほぼ20州に拡大。カリフォルニア州CCPAも改正規則によりサイバーセキュリティ対策の強化、リスク評価の義務化、自動意思決定技術（ADMT）の透明性確保を新たに要求する。EUでは2026年8月2日にAI Actが完全施行となり、AIによる意思決定の説明義務が課される。

🔗 [U.S. Data Privacy Laws and Regulations in 2026](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

## 🟢 Security Governance

### 9. HHS、HIPAAランサムウェア関連の制裁金116.5万ドルを発表
**2026年4月23日**
米保健福祉省（HHS）の公民権局（OCR）は、4件のランサムウェア侵害調査の結果として総額116.5万ドルのHIPAA制裁金を発表。医療機関・保険プラン・業務提携先に対するコンプライアンス警告として位置づけられている。あわせてSECの重大サイバー事故開示規則（材料性判断後4営業日以内の開示義務）も、法務・財務・セキュリティ部門の報告体制に圧力をかけている。

🔗 [List Of Recent Compliance News in 2026](https://www.brightdefense.com/resources/recent-compliance-news/)

---

## 🟣 Crypto Currency

### 10. Binance、MiCA認可取得に失敗しEUサービス停止へ
**2026年6月25〜26日**
EUの暗号資産規制「MiCA」の移行期限（2026年7月1日）を前に、Binanceはギリシャでの認可申請を取り下げ、ポーランド・イタリア・スペイン・フランスの利用者に資金引き出し手続きを案内。フランスでの再申請を計画するが、認可は7月1日の期限後になる見通しで、当面EU向けサービスが利用できなくなる。

🔗 [Binance tells EU users it will no longer provide services after failing to secure MiCA license](https://www.coindesk.com/policy/2026/06/26/binance-tells-eu-users-it-will-no-longer-provide-services-after-failing-to-secure-mica-license)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | PTC Windchill, MCP脆弱性, RIS, SIMスワップ, Linuxカーネル |
| AI Risk | 🟠🟠 | Five Eyes警告, Anthropic Fable/Mythos停止 |
| Data & Privacy | 🟡 | 州プライバシー法, EU AI Act, ADMT |
| Security Governance | 🟢 | HIPAA制裁金, SEC開示規則, CMMC Phase 2 |
| Crypto Currency | 🟣 | MiCA, Binance, EU規制 |

---

*次回配信予定：2026年6月29日（月） | 収集ソース：The Hacker News, CBS News, Anthropic, Smarsh, BrightDefense, CoinDesk*
