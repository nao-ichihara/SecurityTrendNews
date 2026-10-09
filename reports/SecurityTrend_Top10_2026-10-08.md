# セキュリティトレンド Top 10 ニュース
**配信日：2026年10月8日（木）**

> ⚠️ この記事はClaude AIとxAI Grok API（話題性分析）を組み合わせて収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **FortiBleed** | FortiGate/SSL VPNを狙う資格情報収集が継続。FBI・シークレットサービスが共同警告し、86,644台超（194カ国）が影響。 |
| 2 | **PoeLLM** | LiteLLM/OllamaなどAIサーバー3,400台超に感染。GitHub上の詩からC2を算出する新手法で、暗号マイニングも展開。 |
| 3 | **CPR漏洩** | デンマーク国民ID登録簿から約880万件が流出。第三者の正規アクセス悪用によるサプライチェーンリスク。 |
| 4 | **Atlassian CVE-2026-21589** | PoC公開から数時間で悪用が始まった未認証ファイルアクセス脆弱性。パッチ適用の猶予が急速に縮小。 |
| 5 | **ccTLDレジストリ侵害** | .gh/.sl/.asのレジストリが侵害され、Googleドメインの不正証明書が発行された。 |

---

## 🔴 Cyber Security

### 1. FortiBleed継続、FBIとシークレットサービスが共同警告
**2026年10月7日**
FortiGate/SSL VPNを狙う資格情報収集が続き、86,644台以上（194カ国）が影響。盗用・弱い資格情報による管理者ロックアウトが発生しており、ランサムウェア侵入の足がかりになっている。

🔗 [FBI: ongoing FortiBleed attacks lock out FortiGate VPN admins](https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/)

---

### 2. Atlassian CVE-2026-21589、PoC公開直後から悪用
**2026年10月7日**
Jira、Confluence、BitbucketなどData Center 8製品に影響する未認証の任意ファイルアクセス脆弱性。パッチ公開翌日にPoCが出て数時間で悪用試行が観測され、資格情報窃取やCI/CD侵入のおそれがある。

🔗 [Hackers exploit critical Atlassian flaw after public PoC release](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-atlassian-flaw-after-public-poc-release/)
🔗 [Exploitation attempts against critical Atlassian flaw have begun (Help Net Security)](https://www.helpnetsecurity.com/2026/10/07/exploitation-attempts-against-critical-atlassian-flaw-have-begun-cve-2026-21589/)

---

### 3. ccTLDレジストリ侵害でGoogleドメインの不正証明書が発行
**2026年10月7日**
.gh、.sl、.asのレジストリが侵害され、権威DNSレコードの改ざんを伴ってGoogleドメイン向けの不正HTTPS証明書が発行された。証明書透明性ログで確認されたレジストリレベルのドメインハイジャックという点で新規性が高い。

🔗 [Hackers hijack Google domains after breaching ccTLD registries](https://www.bleepingcomputer.com/news/security/hackers-hijack-google-domains-after-breaching-cctld-registries/)

---

## 🟠 AI Risk

### 4. PoeLLMマルウェア、露出AI/LLMサーバー3,400台超に感染
**2026年10月7日**
LiteLLMやOllamaなど外部公開されたAIインフラを標的に感染が拡大。GitHub上の詩からC2アドレスを算出する新手法でステルス性を高め、XMRigなどの暗号マイニングを展開。感染サーバーはスキャナーとして再利用され、ピーク時は1日800台規模で増えた。

🔗 [PoeLLM malware infects 3,400 servers (The Hacker News)](https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html)
🔗 [Canto Incognito: Tracking the PoeLLM malware (Lumen)](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)

---

### 5. フィッシングメールに人間とAIアシスタントの両方を狙う仕掛け
**2026年10月7日**
Barracudaの調査で、パスワード保護添付による人間向けの手口と、AIアシスタント向けの隠しプロンプトインジェクションを同一メールに併用する攻撃が確認された。HTMLコメント、CSS隠しテキスト、Base64、ゼロ幅文字で命令を隠し、要約の操作や送金指示を狙う。

🔗 [Attackers hide AI prompt injections in phishing emails (Infosecurity Magazine)](https://www.infosecurity-magazine.com/news/attackers-hide-ai-prompt/)
🔗 [Email attacks target both humans and AI assistants (Barracuda)](https://blog.barracuda.com/2026/10/07/email-attacks-target-both-humans-ai-assistants)

---

## 🟡 Data & Privacy

### 6. デンマーク中央個人登録簿（CPR）から約880万件が漏洩
**2026年10月5〜7日**
第三者企業の正規アクセス権が悪用され、ほぼ全国民と故人・出国者を含む約880万件の氏名・住所・CPR番号が流出。9月中の約10日間に発生し、高額請求で発覚した。当局はCPR番号を本人確認に使うことの停止を呼びかけている。

🔗 [8.8 million impacted by data breach at Denmark's Central Person Register (SecurityWeek)](https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/)
🔗 [デンマーク高等教育・科学省の発表](https://ufm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/)

---

### 7. ASOSの第三者通知基盤が侵害、不正プッシュ通知を送信
**2026年10月7日**
顧客通知用の第三者プラットフォームが侵害され、「Snowflake完全侵害」を名乗る不正プッシュ通知がユーザーに届いた。氏名・連絡先にアクセスされた可能性があり、同社はカード情報とパスワードは影響なしとしている。

🔗 [ASOS confirms cyberattack, data breach (SecurityWeek)](https://www.securityweek.com/asos-confirms-cyberattack-data-breach/)
🔗 [ASOS data breach app notification (Help Net Security)](https://www.helpnetsecurity.com/2026/10/07/asos-data-breach-app-notification/)

---

## 🟢 Security Governance

### 8. CISA KEV追加とOT Coalitionによる連邦OTセキュリティ義務化の要請
**2026年10月7日**
Citrix NetScaler、FortiMail、Atlassian関連などがKEVに追加され、連邦機関に迅速なパッチ適用義務が生じた。OT CoalitionはCISAに対し、連邦のOTセキュリティ義務化を求めた。

🔗 [OT Coalition urges CISA to mandate OT security (Infosecurity Magazine)](https://www.infosecurity-magazine.com/news/ot-coalition-urges-cisa-mandate/)

---

### 9. FBI請負業者のパッチ未適用でShinyHuntersが職員データ窃取
**2026年10月6日**
Accentureの請負業者がパッチを適用せず、FBI職員データがShinyHuntersに漏洩したと報じられ、FBIは当該請負業者を排除した。委託先のパッチ管理というサプライチェーンガバナンスの失敗例となった。

🔗 [The Hacker News](https://thehackernews.com/)

---

## 🟣 Crypto Currency

### 10. OkoBotマルウェアが暗号資産投資家を標的に
**2026年10月7日**
Kasperskyが、ClickFixやトロイの木馬化したGitHubアプリを経由してウォレットファイル、ブラウザデータ、資格情報を窃取するフレームワークを開示。クリップボード監視や拡張機能注入も行い、1月以降に複数の攻撃が確認されている。

🔗 [Kaspersky（OkoBot調査）](https://securelist.com/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴 | FortiBleed、Atlassian、ccTLD |
| AI Risk | 🟠🟠 | PoeLLM、プロンプトインジェクション |
| Data & Privacy | 🟡🟡 | CPR、ASOS |
| Security Governance | 🟢🟢 | CISA KEV、請負業者管理 |
| Crypto Currency | 🟣 | OkoBot、ウォレット窃取 |

---

*次回配信予定：2026年10月9日（金） | 収集ソース：Claude Web検索、The Hacker News、BleepingComputer、SecurityWeek、Help Net Security、Infosecurity Magazine、xAI Grok API*
