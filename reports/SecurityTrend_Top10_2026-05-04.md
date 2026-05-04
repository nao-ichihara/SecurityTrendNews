# セキュリティトレンド Top 10 ニュース
**配信日：2026年5月4日（月）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **CVE-2026-31431 (Copy Fail)** | 2017年から存在するLinuxカーネルの権限昇格脆弱性。CISAがKEVカタログに追加し、クラウド・コンテナ環境への深刻な影響が懸念される。 |
| 2 | **Mythos（AnthropicのAIモデル）** | 脆弱性探索コストを劇的に下げる可能性があるAIモデル。ホワイトハウスが広範なアクセス拡大に反対し、日本の金融機関も防衛体制強化に動いた。 |
| 3 | **サプライチェーン攻撃** | PyTorchやSAP NOMパッケージへの悪意あるコード注入が確認され、オープンソースエコシステム全体へのリスクが再び浮上。 |
| 4 | **Shadow AI（シャドーAI）** | 組織内で管理されないAI利用が急増。31%のユーザーが雇用主からShadow AIに関するトレーニングを受けておらず、ガバナンスの空白が拡大。 |
| 5 | **CIRCIA最終規則（2026年5月期限）** | 重要インフラへのサイバーインシデント・ランサムウェア支払い報告を義務化する最終規則が2026年5月に公表予定。約30万組織に影響。 |

---

## 🔴 Cyber Security

### 1. CISAがLinux権限昇格脆弱性「Copy Fail」をKEVカタログに追加
**2026年5月3日**


米CISAは、各種Linuxディストリビューションに影響する脆弱性CVE-2026-31431（CVSSスコア7.8）をKnown Exploited Vulnerabilities（KEV）カタログに追加した。この脆弱性は権限のないローカルユーザーがroot権限を取得できるローカル権限昇格（LPE）の欠陥である。
 
Kasperskyの分析によると、Copy FailはDockerやKubernetesなどのコンテナ環境のisolation破壊と物理マシン制御奪取のリスクをもたらす深刻な脅威とされている。
 
修正はLinuxカーネルバージョン6.18.22、6.19.12、7.0で提供されている。


🔗 [CISA Adds Actively Exploited Linux Root Access Bug CVE-2026-31431 to KEV](https://thehackernews.com/2026/05/cisa-adds-actively-exploited-linux-root.html)

---

### 2. サイバーセキュリティ企業Trellixがソースコードリポジトリへの不正アクセスを確認
**2026年5月3日**


セキュリティ企業Trellixは、ソースコードリポジトリへの不正アクセスにより、ソースコードの「一部」が侵害されたことを発表し、現在対応中であることを明らかにした。
 
同社は「大手フォレンジック専門家」と連携して即座に対応に着手し、法執行機関にも通知したとしている。
 
ただし、ソースコードの流出や悪用の証拠は現時点では見つかっていないと述べており、リリース・配布プロセスへの影響も確認されていない。


🔗 [Trellix Confirms Source Code Breach With Unauthorized Repository Access](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html)

---

### 3. Microsoft SharePoint ゼロデイ脆弱性（CVE-2026-32201）が1,300台超のサーバーで悪用中
**2026年5月初旬**


Microsoft SharePoint管理者は、1,300台以上のサーバーに影響するゼロデイ脆弱性の発見を受けて即時パッチ適用が強く求められている。CVE-2026-32201はリモートコード実行を可能にする脆弱性で、既に野外での悪用が確認されており、組織はパッチ適用とインターネットへの公開制限を優先すべきとされている。


🔗 [Supply Chain Attacks, AI Security, and Major Breaches Define This Week in Cybersecurity in May 2026](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)

---

### 4. PyTorchおよびSAP NOMパッケージへのサプライチェーン攻撃が発覚
**2026年5月1日**


PyTorch LightningのPyPI上の悪意あるバージョン2.6.2と2.6.3が、認証情報窃取ペイロードを展開し、盗んだGitHubトークンを通じて拡散していることが判明した。
 
さらにSAPのNOMパッケージにも悪意ある事前インストールスクリプトが仕込まれ、「Mini Shai-Hulud」キャンペーンとしてクラウドおよびローカルの認証情報が流出した。
 これらは組織のCI/CDパイプラインを直撃するオープンソース・サプライチェーン攻撃として重大視されている。

🔗 [Cybersecurity News | Daily Recap [01 May 2026]](https://www.hendryadrian.com/cybersecurity-news-daily-recap-01-may-2026/)

---

### 5. 中国系APT「Silk Typhoon」ハッカーをCOVID研究機関へのサイバー攻撃でアメリカが身柄引き渡し受領
**2026年5月初旬**


中国系スパイキャンペーンが南アジア・東南アジア・NATO加盟欧州の政府・防衛セクターを標的にしており、Trend MicroはこれをSHADOW-EARTH-053として追跡している。このグループは少なくとも2024年12月から活動しているとみられる。
 
攻撃者はMicrosoft ExchangeやIISサーバーのNデイ脆弱性を悪用し、Webシェル（Godzilla）を展開して持続的アクセスを確立、ShadowPadインプラントをDLLサイドローディングで展開している。


🔗 [The Hacker News – Chinese Silk Typhoon](https://thehackernews.com/)

---

## 🟠 AI Risk

### 6. AnthropicのAIモデル「Mythos」が脆弱性探索コストを激変させる可能性
**2026年4月下旬〜5月初旬**


Mythosに関する議論は2026年4月末から5月にかけて加速した。テストの結果、Mythosはソフトウェアの脆弱性を発見・連鎖させるコストを従来の攻撃的セキュリティ作業よりも根本的に低下させる可能性が示された。
 
Politicoの報道によると、Mythosは27年前の脆弱性を1回のテストわずか50ドルのコストで発見したとされ、より広範なテストの総費用は約2万ドルであった。
 
WSJはアクセス拡大計画にホワイトハウスが反対しており、セキュリティ上の懸念とコンピューティングリソースの問題が背景にあると報じた。


🔗 [Mythos News | May, 2026 (STARTUP EDITION)](https://blog.mean.ceo/mythos-news-may-2026/)

---

### 7. AIエージェントが生むアイデンティティリスク——ガバナンスが市場に遅れる
**2026年5月初旬**


Forbes、CyberScoop、Bloomberg Lawの報道はいずれも、AIエージェントのセキュリティ脆弱性・アイデンティティ脅威・グローバルサイバーセキュリティ警告が同じ方向性を示していると指摘する。
 
最新のSaaS＋AI調査によれば、AIに関連した攻撃は前年比で約490%増加しており、数千のSaaSアプリケーション全体にAIが明確な所有権・可視性・管理なしに展開されている。
 
AIエージェント・自動化・サービスアカウントが急増しており、それぞれが独自のパーミッション・認証情報・アクセスパスを持つ非人間アイデンティティであるが、大多数の組織がこれらの完全なインベントリを持っていない。


🔗 [AI Agents News | May, 2026 (STARTUP EDITION)](https://blog.mean.ceo/ai-agents-news-may-2026/)

---

### 8. AnthropicがClaude Securityをパブリックベータ公開——AI駆動の脆弱性スキャンで防御側を支援
**2026年5月1日**


Anthropicは、AI駆動のエクスプロイトが加速する中、リポジトリの脆弱性スキャン・再現手順の説明・パッチガイダンス生成を行うClaude Securityをパブリックベータとして公開した。
 
Mythosが事実上「瞬時のエクスプロイト」という新時代を示す中、Anthropicはクロード・セキュリティを防御側が追いつくための手段として位置付けている。
 また
Ciscoはサードパーティ製AIモデルのフィンガープリント・改ざん検出・サプライチェーンリスク評価のためのModel Provenance Kitをオープンソースで公開した。


🔗 [Cybersecurity News | Daily Recap [01 May 2026]](https://www.hendryadrian.com/cybersecurity-news-daily-recap-01-may-2026/)

---

## 🟡 Data & Privacy

### 9. 米国で州プライバシー法が続々施行——EU AI Actも2026年8月に完全適用へ
**2026年通年トレンド（5月更新）**


米国の2026年プライバシー規制は、新しい包括的州プライバシー法・既存法の大幅改正・米国史上最も積極的な執行環境という3つの力によって形成されている。企業は拡大する消費者の権利・青少年保護義務・精密な位置情報制限・ユニバーサルオプトアウトシグナルへの対応を迫られている。
 
EUのAI法は、一部の高リスク製品（タイムラインは2027年まで延長）を除いて、2026年8月2日に完全適用される予定である。
 
カリフォルニア州では「Delete Act」に基づくDROPプラットフォームが2026年に開始され、データブローカーは2026年8月から削除リクエストの処理が義務化され、他州への波及効果も見込まれる。


🔗 [Data privacy laws: what to expect for 2026 – Ketch](https://www.ketch.com/blog/posts/us-privacy-laws-2026)

---

## 🟢 Security Governance

### 10. CIRCIA最終規則が2026年5月公表予定——重要インフラ30万組織に報告義務
**2026年5月（規則公表予定）**


重要インフラへのサイバーインシデント報告を義務化するCIRCIA（Cyber Incident Reporting for Critical Infrastructure Act）は、16の重要インフラセクターにまたがる推定30万組織に新たな報告義務を課すものであり、CISAが2025年秋に最終規則公表を2026年5月に延期した。
 
連邦レベルのインシデント報告に向けた動きは2025年に加速しており、対象エンティティは重大なサ