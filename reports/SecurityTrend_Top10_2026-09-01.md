# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月1日（火）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **SharePoint脆弱性** | Microsoft SharePointの複数の脆弱性が悪用され続けており、CISAがCVE-2026-55040などをKEVカタログに追加。ランサムウェア攻撃にも利用されている。 |
| 2 | **ランサムウェア（Qilin / Aurora）** | 米ATFへの攻撃を主張したQilinや、AIコーディングツールを侵入に悪用するAuroraなど、ランサムウェア集団の手口が高度化している。 |
| 3 | **AI悪用型攻撃** | 攻撃者がCursorなどのAIコーディングアシスタントやプロンプトインジェクションを使い、攻撃コード生成や侵入プロセスを効率化する事例が急増。 |
| 4 | **サプライチェーン攻撃** | crates.ioの悪意あるRustパッケージやStripe APIキー漏洩など、開発エコシステムを狙った攻撃が続発している。 |
| 5 | **EU AI Act施行** | 2026年8月2日にEU AI Actの本格執行が開始。違反時の罰則は最大3,500万ユーロまたは世界売上高7%に達する。 |

---

## 🔴 Cyber Security

### 1. Microsoft、398件の脆弱性を修正 ― Windowsドライバのゼロデイも含む
**2026年8月（August 2026 Patch Tuesday）**
2026年8月のパッチチューズデーでMicrosoftは398件の脆弱性を修正した。この中には既に悪用が確認されているWindowsドライバのゼロデイ脆弱性が含まれており、企業は優先的な対応が求められている。

🔗 [Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack](https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html)

---

### 2. 米ATF、Qilinランサムウェアによる攻撃を「重大インシデント」と認定
**2026年8月27日**
米アルコール・タバコ・火器及び爆発物取締局（ATF）は、システムへのサイバー攻撃を「重大インシデント」に分類したと発表。連邦議会への通知が必要となる正式な区分で、ランサムウェア集団Qilinが自身のリークサイトで犯行を主張している。対象システムには捜査対象者の情報が含まれていたとされる。

🔗 [ATF declares 'major incident' as ransomware gang claims hack](https://techcrunch.com/2026/08/27/atf-declares-major-incident-as-ransomware-gang-claims-hack/)

---

### 3. CISA、SharePointの複数脆弱性の悪用を警告 ― KEVカタログに追加
**2026年8月18日**
CISAはMicrosoft SharePointの複数の脆弱性（CVE-2026-32201、CVE-2026-45659、CVE-2026-56164、CVE-2026-58644、CVE-2026-50522、CVE-2026-55040など）が悪用されているとして注意喚起。特にCVE-2026-55040は認証回避の脆弱性として8月18日にKEVカタログへ追加され、ランサムウェア攻撃への悪用も確認されている。

🔗 [CISA warns that multiple vulnerabilities in SharePoint are under exploitation](https://www.cybersecuritydive.com/news/cisa-multiple-vulnerabilities-sharepoint-exploitation/825306/)

---

### 4. サプライチェーン攻撃が続発 ― 悪意あるRustパッケージとStripe APIキー漏洩
**2026年8月18日〜20日**
crates.io上でarrayref、internment、append-only-vecなどの人気Rustパッケージが乗っ取られ、ビルド時に不正ペイロードをダウンロード・実行する悪意あるバージョンが公開された（8月20日、約90分で削除）。また8月18日には、659のStripeマーチャントアカウントの有効なAPIキーと約35GBの顧客・決済データがダークウェブのフォーラムで公開された。

🔗 [Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More](https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html)

---

## 🟠 AI Risk

### 5. Auroraランサムウェア、AIコーディングアシスタント「Cursor」を侵入に悪用
**2026年8月（CloudSEK / Gambit Security調査）**
Aurora（別名Aur0ra）ランサムウェアに関連する攻撃者が、AIコーディングアシスタントCursorを標的ネットワークへの侵入に利用していることが判明。AIツールが攻撃の自動化・効率化に転用される事例として注目されている。

🔗 [Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More](https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html)

---

### 6. AIを用いた産業制御システム（Siemens S7 PLC）への攻撃が拡大
**2026年8月（米政府警告）**
米政府は、攻撃者がAIを使って水道・エネルギー・製造業など重要インフラで使われるSiemens S7シリーズPLC（プログラマブルロジックコントローラー）を狙う攻撃スクリプトを作成していると警告した。AIが実際の攻撃能力を底上げしている事例として警戒が強まっている。

🔗 [Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More](https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html)

---

## 🟡 Data & Privacy

### 7. GDPR罰金の累計が71億ユーロを突破 ― 2025年は過去最速ペース
**2026年（DLA Piper GDPR Fines and Data Breach Survey ほか）**
GDPR施行以来の累計罰金額が71億ユーロ（約84億ドル）を突破。2025年単年だけで12億ユーロの罰金が科され、施行開始以来最速のペースとなった。EU域外への不適切なデータ移転や、ダークパターン・事前チェック済み同意など同意取得の不備が主な摘発トリガーとなっている。

🔗 [GDPR Fines Hit €7.1 Billion: Data Privacy Enforcement Trends in 2026](https://www.kiteworks.com/gdpr-compliance/gdpr-fines-data-privacy-enforcement-2026/)

---

### 8. EDPB、GDPR透明性義務に関する第5次協調執行フレームワークを始動
**2026年3月19日（継続的な執行フェーズ）**
欧州データ保護会議（EDPB）は、GDPR第12条・13条・14条に基づく透明性・情報提供義務を対象とした「協調執行フレームワーク」の第5弾を正式に開始した。2026年は法整備から本格的な執行フェーズへの転換点と位置づけられている。

🔗 [GDPR Fines Hit €7.1 Billion: Data Privacy Enforcement Trends in 2026](https://www.kiteworks.com/gdpr-compliance/gdpr-fines-data-privacy-enforcement-2026/)

---

## 🟢 Security Governance

### 9. EU AI Actの本格執行が開始 ― 違反時罰則は最大3,500万ユーロ
**2026年8月2日**
EU AI Actの高リスクAIシステムに関する条項が2026年8月2日に発効し、欧州委員会のAI Officeと各国当局が本格的な執行権限を行使開始。汎用AI（GPAI）モデルは世界売上高3%または1,500万ユーロ、禁止行為は最大7%または3,500万ユーロの罰金対象となる。EU域内で展開されるAIチャットボットには、AIであることの明示や生成コンテンツへの電子透かし表示も義務付けられた。

🔗 [EU AI Act Enforcement Is Live: Fines Now Real](https://enterprisedna.co/resources/news/eu-ai-act-enforcement-fines-live-gpai-august-2026/)

---

## 🟣 Crypto Currency

### 10. Coldcardハードウェアウォレットの脆弱性悪用で最大1.3億ドル流出
**2026年7月30日〜8月**
Coinkite製ハードウェアウォレット「Coldcard」に存在した5年越しのファームウェア欠陥が悪用され、複数の攻撃者がビットコインを組織的に窃取。TRM Labsは7,700以上のアドレスから1.16億ドル超、Galaxy Researchは実質1.3億ドル規模と推定している。2021年3月〜パッチ適用までにシード生成したユーザーは要注意とされる。

🔗 [Hackers steal over $130M by exploiting bug in offline hardware wallets](https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | SharePoint、ランサムウェア、サプライチェーン攻撃、パッチチューズデー |
| AI Risk | 🟠🟠 | AIコーディングアシスタント悪用、産業制御システム、プロンプトインジェクション |
| Data & Privacy | 🟡🟡 | GDPR罰金、透明性義務、データ移転規制 |
| Security Governance | 🟢 | EU AI Act、罰則強化、コンプライアンス期限 |
| Crypto Currency | 🟣 | ハードウェアウォレット、秘密鍵漏洩、資産流出 |

---

*次回配信予定：2026年9月2日（水） | 収集ソース：The Hacker News、TechCrunch、Cybersecurity Dive、Kiteworks、Enterprise DNA*
