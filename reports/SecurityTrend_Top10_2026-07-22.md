# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月22日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **AI主導型サイバー攻撃** | AIが人間の介入をほぼ受けずに侵入から悪用までの攻撃チェーンを自律実行する事例が増加。攻撃の速度と規模が急拡大している。 |
| 2 | **サンドボックスエスケープ／RCE** | ServiceNow AI Platformの重大脆弱性など、サンドボックスを突破し未認証のままリモートコード実行を許す不具合が相次いで悪用されている。 |
| 3 | **記録的規模のゼロデイパッチ** | Microsoftの2026年7月Patch Tuesdayは過去最大規模となり、SharePointやAD FSの悪用済みゼロデイを含む大量の脆弱性が公表された。 |
| 4 | **ブリッジ／オラクル悪用によるDeFiハック** | クロスチェーンブリッジや価格オラクルの操作を狙った攻撃が続き、単一のスマートコントラクトバグより運用・インフラ面の脆弱性が主要因になっている。 |
| 5 | **LLM学習データ開示義務** | 州レベルのプライバシー法改正により、企業に対しユーザーデータがAIモデル学習に使われているかの開示を義務付ける動きが拡大。 |

---

## 🔴 Cyber Security

### 1. ServiceNow AI Platformの重大脆弱性が公開直後から悪用
**2026年7月20日**
CVSS 9.5のサンドボックスエスケープ脆弱性（CVE-2026-6875）が、パッチ公開からわずか数日で悪用が確認された。未認証の攻撃者がRhinoエンジンを突破し、管理者ユーザー作成やシェルコマンド実行が可能になる恐れがある。自己ホスト型インスタンスの利用企業は早急なパッチ適用が必要。

🔗 [Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution](https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html)

---

### 2. Microsoft、過去最大規模の月例パッチで悪用済みゼロデイ2件を修正
**2026年7月14日〜15日**
2026年7月のPatch Tuesdayは約570〜622件のCVEに対応する過去最大規模となった。SharePoint Server（CVE-2026-56164）とActive Directory Federation Services（CVE-2026-56155）の悪用済みゼロデイを含み、59件が緊急（Critical）評価。米CISAは連邦機関に対し7月17日までの是正を要求した。

🔗 [Microsoft's July 2026 Patch Tuesday Addresses 569 CVEs](https://www.tenable.com/blog/microsofts-july-2026-patch-tuesday-addresses-569-cves-cve-2026-56155-cve-2026-56164)

---

### 3. 160万インストールの人気拡張機能ModHeaderがマルウェア認定で削除
**2026年7月中旬**
ヘッダー編集拡張機能「ModHeader」（Chrome/Edge、計約160万インストール）に、閲覧履歴を収集・暗号化し外部送信する休眠状態のコードが発見された。GoogleとMicrosoftは両ストアから削除。実際のデータ流出は確認されていないが、収集・保存・通信の仕組みはすでに実装されていたとされる。

🔗 [Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found](https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html)

---

### 4. Ernst & Young、ITサポートチケット基盤への不正アクセスを確認
**2026年3月28日〜4月12日（7月に確認・公表）**
EYは第三者がITサポートチケットプラットフォームに不正アクセスし、顧客の税務・投資保有関連文書をダウンロードしたことを確認したと発表。大手会計・コンサルティングファームを狙った標的型侵害の一例として注目されている。

🔗 [Hacked, leaked, and held for ransom: The worst breaches of 2026 so far](https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/)

---

## 🟠 AI Risk

### 5. AIが攻撃チェーン全体を自律実行する事例が急増
**2026年7月15日**
Check Pointの「AI Security Report 2026」によると、AIが数十セッションにわたり数千のコマンドを自律生成し、侵入から悪用までを人間の指示をほとんど受けずに実行する事例が過去12カ月で確認された。安全機構を除去したAIモデルを悪用する攻撃者グループが最大のリスクとされる。

🔗 [AI used to help plan the break-in, now it's doing the break-in](https://www.helpnetsecurity.com/2026/07/15/check-point-ai-security-report-2026/)

---

### 6. 欧州委員会、先進AIのサイバーセキュリティ活用とリスクへの新計画を発表
**2026年7月7日**
欧州委員会は先進AIがサイバーセキュリティにもたらすリスクと機会の両方に対応する新計画を発表。AIは防御力向上に寄与する一方、脆弱性の自動発見や攻撃の自動化・高速化・大規模化にも悪用され得ると警告している。

🔗 [New EU plan to address the risks and opportunities of advanced AI for cybersecurity](https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en)

---

## 🟡 Data & Privacy

### 7. コネチカット州、CTDPA改正法が7月1日に施行
**2026年7月1日**
改正コネチカットデータプライバシー法（CTDPA）が施行され、企業はChatGPT・Gemini・DeepSeek・Grokなど大規模言語モデルの学習にユーザーデータを利用・収集・販売しているか否かをプライバシー通知で明示することが義務化された。また「神経データ」が新たにセンシティブデータの定義に追加され、原則オプトイン同意が必要となる。

🔗 [2026 U.S. Data Privacy Developments: New and Amended Laws](https://www.gunster.com/newsroom/publications/2026-data-privacy-laws-state-changes-universal-opt-out-compliance)

---

## 🟢 Security Governance

### 8. CMMC第三者監査が一時停止、法的義務は継続と業界が指摘
**2026年7月**
国防関連サプライヤー向けのCMMC（サイバーセキュリティ成熟度モデル認証）第三者監査が一時停止されたことを受け、業界専門家は「監査は止まってもCUI（管理対象非機密情報）保護の法的義務そのものは継続する」との見解を示している。AI活用が進む中でガバナンス・コンプライアイス体制が実効性を保てるかが引き続き論点となっている。

🔗 [2026 Operational Guide to Cybersecurity, AI Governance & Emerging Risks](https://www.corporatecomplianceinsights.com/2026-operational-guide-cybersecurity-ai-governance-emerging-risks/)

---

## 🟣 Crypto Currency

### 9. Wanchainブリッジがエクスプロイトを受け約5.15億NIGHTトークンが流出
**2026年7月20日**
Wanchainのクロスチェーンブリッジが悪用され、約5.15億枚のNIGHTトークンが流出した。Midnightはコアネットワーク自体の安全性は確保されていると説明しているが、ニュース拡散とともにNIGHT価格は約38.5%急落した。

🔗 [Cardano News Today: Wanchain Bridge Exploit Drains 515M NIGHT](https://www.coingabbar.com/en/crypto-currency-news/cardano-news-today-wanchain-bridge-exploit-drains-515m-night)

---

### 10. Arbitrum上のOstiumプロトコルがオラクル操作で約2,400万ドル被害
**2026年7月15日**
実物資産（RWA）永続契約プロトコルOstiumが、登録済みのPriceUpKeep Forwarderと未来日付の権限付きオラクルレポートを組み合わせた手口で悪用され、人為的な取引利益を捏造された。当初検知額は約500万ドルだったが、資金フローの追跡により最終的な被害額は約2,400万ドルと判明した。

🔗 [Explained: The Ostium Hack (July 2026)](https://www.halborn.com/blog/post/explained-the-ostium-hack-july-2026)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | サンドボックスエスケープ、ゼロデイ、拡張機能マルウェア、データ侵害 |
| AI Risk | 🟠🟠 | 自律型AI攻撃、AIガバナンス |
| Data & Privacy | 🟡 | LLM学習データ開示、州プライバシー法 |
| Security Governance | 🟢 | CMMC、コンプライアンス継続義務 |
| Crypto Currency | 🟣🟣 | ブリッジエクスプロイト、オラクル操作 |

---

*次回配信予定：2026年7月23日（木） | 収集ソース：The Hacker News, Help Net Security, TechCrunch, Tenable, SecurityWeek, Gunster, Corporate Compliance Insights, CoinGabbar, Halborn, European Commission*
