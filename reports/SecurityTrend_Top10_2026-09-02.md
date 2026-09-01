# セキュリティトレンド Top 10 ニュース
**配信日：2026年9月2日（水）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **PaperCut ゼロデイ** | プリント管理ソフトの重大脆弱性（CVE-2026-82078／81578）が実際に悪用され、緊急パッチが2度発行。CISAのKEVカタログにも追加された。 |
| 2 | **Langflow RCE** | AIアプリ構築プラットフォームの未認証リモートコード実行脆弱性（CVE-2026-0768）が公開直後から積極的に悪用されている。 |
| 3 | **ヘルスケア侵害の継続** | Novocureなど医療関連企業へのサイバー攻撃が相次ぎ、患者・従業員データの漏えいが続いている。 |
| 4 | **CCPA執行強化** | GMへの過去最高額1,275万ドルの制裁金など、州レベルのプライバシー法執行が本格化している。 |
| 5 | **CIRCIA最終化** | CISAが9月にサイバーインシデント報告規則を最終化予定。72時間以内の報告義務化が焦点。 |

---

## 🔴 Cyber Security

### 1. Novocureで患者データ漏えい、1,400人以上の米国がん患者に影響
**2026年9月1日〜2日**
腫瘍治療機器メーカーNovocureが8月中旬のサイバー攻撃により、1,400人以上の米国がん患者と従業員のデータが流出したと発表。患者IDや医療従事者の連絡先情報が対象で、一部西部地域の患者については氏名などの識別情報も含まれる。医療機器自体への影響はないとしている。

🔗 [Novocure data breach affects more than 1,400 cancer patients](https://www.bleepingcomputer.com/news/security/novocure-data-breach-affects-more-than-1-400-cancer-patients/)

---

### 2. PaperCutが2度目の緊急パッチ、CISAのKEVカタログに追加
**2026年8月28日〜31日**
プリント管理ソフトPaperCut NG/MFの認証バイパス（CVE-2026-81578）と危険なクラスロード（CVE-2026-82078、CVSS 9.4）が実際に悪用され、最初のパッチ回避も確認されたため2度目の緊急パッチをリリース。両脆弱性は8月31日にCISAの既知悪用脆弱性（KEV）カタログに追加された。

🔗 [PaperCut releases second emergency patch for exploited flaws](https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/)

---

### 3. LangflowとRuby on RailsのRCE脆弱性が積極的に悪用
**2026年9月1日**
AIアプリ構築プラットフォームLangflow（CVE-2026-0768、CVSS 9.8）とRuby on Railsの重大脆弱性が、VulnCheckの調査により実際に悪用されていることが判明。公開から数時間で50件超の検知があり、月曜時点で360件に増加。攻撃者は認証情報の窃取や偵察活動を行っている。

🔗 [Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity](https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html)

---

### 4. WatchGuard Fireware OSに重大なRCE脆弱性、11万台以上のファイアウォールに影響
**2026年9月**
WatchGuardがFireware OSのikedプロセスに存在する3件の重大脆弱性（CVE-2026-19313、19315、19318、いずれもCVSS 9.3）を含む20件以上の脆弱性を修正。特別に細工したネットワークトラフィックによりリモートコード実行が可能になる。

🔗 [WatchGuard Patches Critical Vulnerabilities](https://www.securityweek.com/watchguard-patches-critical-vulnerabilities/)

---

## 🟠 AI Risk

### 5. 「AIリスク管理の実態調査2026」、自信と実態の乖離が拡大
**2026年**
企業のAI導入が加速する一方、AIリスクを管理する体制は認識されているほど整っていないとする調査結果が発表された。組織は平均月10種類のAIアプリケーションを利用しているが、多くが正式な承認を経ていない。高リスクなプロンプトの割合も2%から4%に倍増している。

🔗 [The State of AI Risk Management in 2026 Reveals a Growing Confidence Gap](https://www.esecurityplanet.com/artificial-intelligence/the-state-of-ai-risk-management-in-2026-reveals-a-growing-confidence-gap/)

---

### 6. 北朝鮮ハッカー、AIを活用したソーシャルエンジニアリングで暗号資産窃取
**2026年4月**
北朝鮮のハッカー集団がAIを活用した高度なソーシャルエンジニアリング手法により、約10万ドル相当の暗号資産を窃取したことが判明。AI技術の悪用により偵察やなりすましの精度が向上しており、国家主導のサイバー犯罪におけるAIリスクの高まりを示している。

🔗 [North Korean hackers use AI-powered social engineering to steal $100K in crypto](https://www.nknews.org/2026/04/north-korean-hackers-use-ai-powered-social-engineering-to-steal-100k-in-crypto/)

---

## 🟡 Data & Privacy

### 7. GMがCCPA史上最高額1,275万ドルの制裁金で和解、コネクテッドカーのデータ販売問題
**2026年5月8日**
カリフォルニア州司法長官は、GMがOnStar加入者数十万人分の走行・位置データを無断でデータブローカー（Verisk、LexisNexis）に販売していたとして、CCPA史上最高額となる1,275万ドルの和解金で合意したと発表。目的外利用やデータ最小化義務の違反が指摘された。

🔗 [Attorney General Bonta, Partners Secure $12.75 Million General Motors Privacy Settlement](https://oag.ca.gov/news/press-releases/when-it-comes-data-privacy-consumers-must-be-driver%E2%80%99s-seat-attorney-general)

---

## 🟢 Security Governance

### 8. CISAが9月にサイバーインシデント報告規則（CIRCIA）を最終化へ
**2026年9月予定**
CISAは長らく待たれていたCIRCIA（サイバーインシデント報告法）の最終規則を2026年9月に確定させる見通し。重大インシデント発生から72時間以内、ランサムウェア身代金支払いから24時間以内の報告が義務付けられる予定で、企業のインシデント対応体制に大きな影響を与える。

🔗 [CISA Plans to Finalize Cyber Incident Reporting Regulations in September 2026](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026)

---

### 9. CMMC Phase 2の11月10日期限、国防総省の60日間レビューで一時停止
**2026年9月時点**
国防関連契約企業に第三者機関によるセキュリティ認証（C3PAO）を義務付けるCMMC Phase 2は当初2026年11月10日開始予定だったが、国防総省（DoW）による60日間のレビューのため一時停止されている。9月中旬に追加のガイダンスが示される見通し。

🔗 [CMMC Phase 2 deadline November 10, 2026: What DoD Contractors need to know](https://www.strikegraph.com/blog/cmmc-phase-2-deadline-november-2026)

---

## 🟣 Crypto Currency

### 10. 北朝鮮が2026年の暗号資産ハッキング被害額の76%を占める
**2026年（Drift Protocolハック4月1日、KelpDAOハック4月18日）**
TRM Labsの分析によると、北朝鮮系ハッカーは2026年に約5億7,700万ドル相当の暗号資産を窃取し、これは同年の暗号資産ハッキング被害総額の76%に相当する。Drift Protocol（2.85億ドル）とKelpDAO（2.92億ドル）への攻撃が中心で、AI技術を活用した偵察・ソーシャルエンジニアリングの高度化が背景にあるとされる。

🔗 [North Korea Stole 76% of All Crypto Hack Value in 2026 — With Just Two Attacks](https://www.trmlabs.com/resources/blog/north-korea-stole-76-of-all-crypto-hack-value-in-2026-with-just-two-attacks)

---

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴 | PaperCut, Langflow, WatchGuard, Novocure |
| AI Risk | 🟠🟠 | AIリスク管理, AI悪用ソーシャルエンジニアリング |
| Data & Privacy | 🟡 | CCPA, GM和解金 |
| Security Governance | 🟢🟢 | CIRCIA, CMMC Phase 2 |
| Crypto Currency | 🟣 | 北朝鮮, DeFiハッキング |

---

*次回配信予定：2026年9月3日（木） | 収集ソース：BleepingComputer, The Hacker News, SecurityWeek, eSecurity Planet, NK News, California DOJ, Hunton Andrews Kurth, StrikeGraph, TRM Labs*
