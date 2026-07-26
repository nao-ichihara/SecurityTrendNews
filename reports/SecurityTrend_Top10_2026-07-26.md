収集した情報を基にレポートを生成します。

# セキュリティトレンド Top 10 ニュース
**配信日：2026年7月26日（日）**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **SonicWall RCE脆弱性（CVE-2026-15409/10）** | CVSS 10.0の最高深刻度。認証不要のSSRF＋コードインジェクション連鎖によりSMA1000アプライアンスで完全RCE達成。CISAのKEVカタログ登録済み。 |
| 2 | **EU AI Act 完全施行（8月2日）** | 高リスクAIシステムへの完全コンプライアンス要件が8月2日に発効。違反時は最大€3,500万または全世界売上の7%の制裁金。 |
| 3 | **DeFiブリッジハック急増** | 7月単月の暗号資産ハック被害は約9,700万ドルに到達。ブリッジ（チェーン間橋渡しプロトコル）が集中攻撃を受けている。 |
| 4 | **BlueNoroff暗号資産フィッシングキット** | 北朝鮮系APTがZoom/Teams偽装フィッシングで被害者の暗号資産ウォレットを事前偵察後にマルウェアを送り込む高度な手口を展開中。 |
| 5 | **米国州レベルプライバシー法の多重施行** | アーカンソー州の新プライバシー法が7月施行。Connecticut州はニューラルデータを要保護センシティブデータに追加。州法の乱立が加速。 |

---

## 🔴 Cyber Security

### 1. SonicWall SMA1000に深刻なRCEチェーン脆弱性　CVSS 10.0を実環境で積極悪用
**2026年7月23日**


CVE-2026-15409は認証不要のサーバーサイドリクエストフォージェリ（SSRF）でCVSS 10.0の評価を受けており、コードインジェクション脆弱性CVE-2026-15410と連鎖させることでSMA1000アプライアンス上で完全なリモートコード実行（RCE）が可能となる。
 
CISAは両脆弱性を7月14日付けでKnown Exploited Vulnerabilities（KEV）カタログに追加した。
 
InfraTrustのレポートはCVSSスコアのみで優先度を決定するアプローチの危険性を指摘しており、インターネット公開中の低スコアのバグが、ローカル管理者権限を必要とするクリティカルな脆弱性より早急な対応を要する場合があると警告している。


🔗 [July 2026 InfraTrust Report Flags 26 Unauthenticated Vulnerabilities and Exploited SonicWall Flaws](https://cybersecuritynews.com/infratrust-flags-26-vulnerabilities/)

---

### 2. ChatGPT「AgentForger」脆弱性　フィッシング1通でAIエージェントを組織内に不正展開
**2026年7月24日**


サイバーセキュリティ研究者たちが、OpenAIのChatGPT Workspace Agentsにおける重大な脆弱性を公開した。単一のフィッシングリンクにより、攻撃者が被害組織内部に密かに自律型AIエージェントを構築・認証・展開できるという内容だ。
 
この脆弱性はZenity Labsによって「AgentForger」と命名されており、OpenAIは責任ある開示を受け、2026年6月8日までに修正を完了している。
 AIエージェントの普及と攻撃面の拡大が交差する典型的な事例として業界に衝撃を与えた。

🔗 [ChatGPT Workspace Agent Vulnerability "AgentForger"](https://thehackernews.com/)

---

### 3. DHS（米国土安全保障省）ネットワークへの不正侵入が確認　レガシー情報共有環境が標的に
**2026年7月上旬**


Nextgov/FCWの報道によれば、国土安全保障省（DHS）は2件の警告を誤検知として退けた後に、Homeland Security Information Networkへの能動的な侵入を確認した。DHSは7月1日に事案を公式認定し、レガシーな非機密情報共有環境に影響したものの、機密ネットワークへの侵害はなかったと述べた。
 
セキュリティ研究者らは、そのリスク水準が2025年の広域ToolShellキャンペーンに匹敵する可能性があると警告している。


🔗 [SWK Cybersecurity News Recap July 2026](https://www.swktech.com/swk-cybersecurity-news-recap-july-2026/)

---

### 4. OFACがランサムウェア支援VPNプロバイダーを史上初めて制裁指定　Operation Saffronの成果
**2026年7月（月内）**


この制裁は、2026年5月にFBIボストン支局が支援した欧州の法執行作戦「Operation Saffron」に続くもので、27カ国にまたがる33台のサーバーを押収し、1VPNSウェブサイトを閉鎖。OFACがランサムウェアの幇助でVPNプロバイダーを制裁指定したのは史上初めてのことだ。
 
財務省の制裁指定はあらゆる米国人による取引を禁止し、下流のサービスプロバイダーにもコンプライアンスリスクをもたらす。


🔗 [SWK Cybersecurity News Recap July 2026](https://www.swktech.com/swk-cybersecurity-news-recap-july-2026/)

---

## 🟠 AI Risk

### 5. Claude Cowork VMサンドボックス脱出欠陥　AIエージェントがMacファイルへアクセス可能に
**2026年7月24日**


AIエージェントがエンドユーザーシステムへのファイルレベルアクセスを獲得するにつれ、Claude CoworkのVM（仮想マシン）サンドボックスバイパスという新興リスクが表面化した。また、機械IDに対する合成ID攻撃が複雑化しており、エンタープライズ自動化における本人確認の水準引き上げが急務となっている。
 
ディフェンダー側はAIサンドボックスの堅牢化、機械的詐欺の監視、急速なデータセンター拡張リスクの評価で対応する必要がある。


🔗 [AI Security Daily Briefing: July 24, 2026](https://techmaniacs.com/2026/07/24/ai-security-daily-briefing-july-24-2026/)

---

### 6. EU AI Act　8月2日に主要施行フェーズ到来　GPAIプロバイダーへの制裁権限が発動
**2026年7月（施行直前）**


8月2日、EUの人工知能法（規則2024/1689）が最も重要な施行フェーズに入り、高リスクAIシステムと汎用AIモデルに対して拘束力ある義務が発動する。制裁金は最大€3,500万または全世界年間売上の7%に達し、GDPRの上限を超え、世界中の技術企業のAI開発・展開・ガバナンス体制の再構築を迫る「ブリュッセル効果」を生み出している。
 
デジタル・オムニバス改正案は欧州議会で可決され、AI法の高リスク義務を12〜16カ月延長したが、Article 50の透明性義務とGPAI執行権限は変更されず、8月2日に発効する。


🔗 [EU AI Act Enforcement: August 2026 Compliance Deadline](https://informedclearly.com/en/ai/55795/eu-ai-act-compliance-deadline-2026)

---

## 🟡 Data & Privacy

### 7. アーカンソー州新プライバシー法が7月施行　米国のデータ保護法「乱立時代」が本格化
**2026年7月**


2026年、企業は20近くの州が独自規制を導入する米国データプライバシー法の拡大する地形を乗り越えなければならない。
 
アーカンソー州は2026年7月に発効する新プライバシー法を導入した。
 
コネチカット州は2026年7月1日よりニューラルデータを「センシティブデータ」の定義に含め、高度な保護とオプトイン同意が必要となった。
 
米国のプライバシー規制は「新規包括的州法」「既存法の改正」「米国史上最も積極的な執行環境」の3つの力によって形成されており、拡大する消費者の権利、未成年者保護義務、詳細なルール策定への対応が企業に求められる。


🔗 [U.S. Data Privacy Laws and Regulations in 2026](https://www.smarsh.com/blog/thought-leadership/data-privacy-laws/)

---

### 8. GDPR施行8年　欧州デジタル・オムニバス改正でGDPR義務の簡素化を欧州委が検討
**2026年（進行中）**


2026年の最も顕著な変化の一つは、法整備の局面から法執行の局面への移行だ。過去10年間で世界中に多くのデータプライバシー法が生まれたが、規制当局は今、既存のルールが適切に遵守されているかの確認に注力している。
 
GDPRはEUにおけるグローバルな基準であり続けているが、2026年は欧州委員会のデジタル・オムニバス提案が一部のGDPR義務を再形成し、中小企業のコンプライアンス負担を軽減しながら個人の基本的権利を損なわない形での見直しが図られる転換点となっている。


🔗 [Data privacy in 2026: How GDPR compliance landscape is evolving](https://www.tjc-group.com/blogs/data-privacy-in-2026-how-gdpr-compliance-landscape-is-evolving/)

---

## 🟢 Security Governance

### 9. CMMC フェーズII移行を米国防総省が一時停止　60日間の再検討に入る
**2026年7月**


米国防総省（Department of War）は、2026年11月10日施行予定だったCMMC（サイバーセキュリティ成熟度モデル認証）フェーズII要件への移行計画を停止し、CMMMCプログラムの将来について60日間の調査を開始すると発表した。
 
ただし、防衛請負業者はDFARS条項252.204-7012のもとで連邦データ保護義務を引き続き負っており、警戒を緩めることはできない。
 調達プロセスへの影響と準備企業への混乱が懸念される。

🔗 [Top 5 Cybersecurity Headlines to Know this Month – BARR Advisory](https://www.barradvisory.com/resource/top-5-headlines-july-2026/)

---

## 🟣 Crypto Currency

### 10. BlueNoroff（北朝鮮）がZoom偽装フィッシングキットで暗号資産ウォレットを事前プロファイリング後に攻撃
**2026年7月24日**


北朝鮮系脅威アクターBlueNoroffが、タイポスクワットされたZoomおよびMicrosoft Teamsドメインを用いたClickFix型キャンペーンに加え、ビデオ会議プラットフォームを偽装した能動的なフィッシングキットを運用し、マルウェア配信を目的としたソーシャルエンジニアリングキャンペーンを展開していることが確認された。
 