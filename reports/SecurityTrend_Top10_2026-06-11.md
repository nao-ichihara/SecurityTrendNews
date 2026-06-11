# セキュリティトレンド Top 10 ニュース
**配信日：2026年6月11日（木）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **Patch Tuesday（6月）** | 
Microsoftが6月度のセキュリティアップデートを公開。198件の脆弱性に対処し、近年最大規模の単月パッチとなった。
 |
| 2 | **AIエージェント攻撃** | 
LLMエージェントが自律的に後処理行動を実行し、AWSデータベースを1時間以内に外部流出させる初の実証攻撃が記録された。AIエージェント・FastAPI・vLLMなど数百万件の実装に影響する脆弱性が悪用された。
 |
| 3 | **DPRK暗号資産窃取** | 
北朝鮮は国家目標の資金調達と制裁回避のために暗号資産窃取を継続。74%少ない既知の攻撃件数で記録的な2025年の成果を達成しており、氷山の一角にすぎない可能性が指摘されている。
 |
| 4 | **米国州プライバシー規制** | 
2026年、企業はほぼ20州に及ぶ独自データプライバシー規制の複雑な環境下での対応を迫られている。かつてはCCPA・CPRAが中心だったが、規制の地図は大きく広がった。
 |
| 5 | **CMMC Phase 2** | 
2026年11月10日よりCMMC（サイバーセキュリティ成熟度モデル認証）フェーズ2が開始し、多くの米国防省請負業者に対してサードパーティによる認証が契約資格の要件となる。
 |

---

## 🔴 Cyber Security

### 1. Microsoft、6月度Patch Tuesdayで198件の脆弱性を修正 ─ ゼロデイ3件含む大規模パッチ
**2026年6月10日**


Microsoftは2026年6月度のPatch Tuesdayセキュリティアップデートを公開し、製品エコシステム全体で198件の脆弱性に対処した。近年最大規模の単月パッチとなり、パッチ公開前に公表済みだったゼロデイ3件の修正と32件のCritical級および166件のImportant級の問題が含まれる。
 
公開済みゼロデイの中には、BitLockerのドライブ暗号化をバイパスできるCVE-2026-50507も含まれており、エンドポイントのデータ保護としてBitLockerに依存する組織にとって深刻な懸念となっている。
 
さらにPatch Tuesday直後、セキュリティ研究者「Nightmare Eclipse」がGitHub上に新たなWindowsゼロデイ「RoguePlanet」を公開するという報復的な行為も発生した。


🔗 [Microsoft Patches 198 Vulnerabilities in June 2026 Security Update](https://cyberpress.org/microsoft-patches-198-vulnerabilities/)

---

### 2. フランス政府の暗号化メッセージングアプリ「Tchap」が標的に ─ 公務員データ漏洩の懸念
**2026年6月10日〜11日**


フランス政府が公務員向けに採用している暗号化メッセージングプラットフォーム「Tchap」でセキュリティ侵害が発生した。WhatsAppやSignalといった海外製アプリを公用通信から制限した後に採用されたプラットフォームであり、当局は今回のインシデントとともに、より広範なメッセージやユーザーデータが流出していないかについて調査中だ。
 
DINUMはハッカーが乗っ取ったユーザーアカウントを使ってTchapに侵入したと警告している。


🔗 [Security breach hits French government chat app Tchap](https://cybernews.com/security/)

---

### 3. ServiceNow、顧客データへの不正アクセスを認める「セキュリティインシデント」を開示
**2026年6月10日**


米国の大手ソフトウェア企業ServiceNowが、攻撃者が顧客データへのアクセスを得た「セキュリティインシデント」を開示した。
 
ServiceNowは、認証不要でアクセスできる脆弱なAPIエンドポイントを悪用した攻撃者によって顧客インスタンスからデータが照会されたと警告している。
 
同社は4月7日から把握していたとされるセキュリティ問題に対処するため、ホスト型顧客インスタンスを更新した。


🔗 [ServiceNow data breach: security issue gives attacker access](https://cybernews.com/security/)

---

### 4. Veeam Backup & Replicationに深刻なRCE脆弱性（CVSS 9.4）─ 即時パッチ適用を推奨
**2026年6月10日**


VeeamはBackup & Replicationソフトウェアにリモートコード実行（RCE）につながるCritical脆弱性CVE-2026-44963（CVSSスコア9.4）のセキュリティパッチを公開した。認証済みドメインユーザーがバックアップサーバーでRCEを実行できる脆弱性だ。
 
Veeam Backup & Replication 12.3.2.4465以前のバージョン12系に影響し、バージョン13.xのアーキテクチャ変更により13系には影響しない。修正版はバージョン12.3.2.4854で提供されている。


🔗 [Veeam Backup & Replication Critical RCE Vulnerability](https://thehackernews.com/)

---

## 🟠 AI Risk

### 5. LLMエージェントが自律的にAWSデータベースを侵害 ─ AIを悪用した初の実証攻撃
**2026年6月初旬**


セキュリティ企業Sysdigが、LLMエージェントが自律的に後処理行動を実行し、AWSデータベースを1時間以内に外部流出させた初の実証済みライブサイバー攻撃を記録した。攻撃はCVE-2026-48710（"BadHost"）、PythonウェブフレームワークStarletteに存在するHTTPホストヘッダーインジェクション脆弱性を悪用したものだ。
 
この脆弱性はFastAPIアプリ・vLLMデプロイメント・LiteLLMインスタンス・これらのフレームワーク上のMCPサーバーすべてに影響し、数百万のAIエージェントと AI応用アプリケーションに影響する可能性がある。Sysdigはハッカーが人間の個別指示なしにMarimo Notebook経由で脆弱性を悪用したことを確認した。


🔗 [First Live LLM Agent Cyberattack: AWS Database Exfiltrated in Under an Hour](https://www.buildfastwithai.com/blogs/ai-news-today-june-1-2026)

---

### 6. 米ホワイトハウス、国家安全保障AIリスク管理戦略の策定を命じる大統領覚書を発出
**2026年6月6日**


ホワイトハウスはNSPM-11（国家安全保障大統領覚書）を発出し、米国の最重要AIシステムの機密性・完全性・可用性確保のため、120日以内にDNI・国防長官・NSA長官らが国家安全保障機構向けのAIリスク管理・保証戦略と、AIセキュリティのベースラインプラクティスを確立する実施ガイダンスを共同で策定するよう命じた。
 
また、別の大統領令ではAI企業に対し、最も強力なモデルを公開30日前に政府テストへ自主的に提出するよう要請。連邦機関にAIモデルのサイバー能力を評価するベンチマーク策定と「AIサイバーセキュリティ情報共有センター」の設置を指示している。


🔗 [National Security Presidential Memorandum/NSPM-11](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/)

---

## 🟡 Data & Privacy

### 7. 米国、州プライバシー法が急増 ─ CCPA自動意思決定規制・未成年者データ保護が焦点
**2026年6月（施行状況）**


2026年より米国の州プライバシー執行活動が活発化している。カリフォルニア州のCCPAにおける自動意思決定技術（ADMT）規制・リスクアセスメント・サイバーセキュリティ監査要件が年初から適用開始となり、インディアナ・ケンタッキー・ロードアイランド各州でも包括的プライバシー法が新たに施行された。
 
2026年の米国プライバシー規制環境は、①新たな包括的州法、②既存法の大幅改正、③米国プライバシー史上最も積極的な執行気運という三つの力によって形成されている。
 
EUでは2026年8月2日にEU AI法が完全施行となり、消費者に影響するAI主導の決定について企業による説明が義務付けられる。


🔗 [2026 Data Privacy Laws and Regulations](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

### 8. FTC、学生データ保護のIlluminate Education社との合意に最終承認 ─ HIPAA執行も強化
**2026年6月5日**


FTCは2026年6月5日、学生の個人データを適切に保護しなかったとする疑惑を解決するためにIlluminate Education社との合意に最終承認を与えた。
 
また、FTCは5月19日より「TAKE IT DOWN法」の執行を開始し、センシティブな位置情報データを数百万台のモバイルデバイスにリンクして販売したとしてKochava社の禁止命令も下した。
 
HHSのOCRも2026年4月23日に医療機関を対象としたHIPAAランサムウェア和解として計116.5万ドルを発表し、427,000人以上に影響したランサムウェア事案を対象に4事例について執行上の警告を発した。


🔗 [Privacy and Security Enforcement | FTC](https://www.ftc.gov/news-events/topics/protecting-consumer-privacy-security/privacy-security-enforcement)

---

## 🟢 Security Governance

### 9. CMMC Phase 2迫る ─ DoD請負業者に第三者認証が契約条件として義務化へ
**2026年11月10日施行予定（直前対応フェーズ）**


CMMC（サイバーセキュリティ成熟度モデル認証）フェーズ2が2026年11月10日より開始し、多くの国防省請負業者に対してサードパーティのC3PAO認証が契約資格の要件となる。32 CFR Part 170の下で、連邦契約情報（FCI）や管理対象非機密情報（CUI）を扱う請負業者はもはやセルフアセスメントを安全な選択肢として扱えなくなり、Level 2 C3PAO認証・SPRS登録・年次宣誓・証拠保全・POA&M完了が入札準備に直結する。
 
連邦レベルでは重要インフラを対象としたCIRCIA（サイバーインシ