"""
GitHub Actions上でClaude APIを呼び出してセキュリティトレンドレポートを生成するスクリプト

使用条件:
  - 環境変数 ANTHROPIC_API_KEY が設定されていること（GitHub Secrets）
  - 環境変数 REPORT_DATE が YYYY-MM-DD 形式で設定されていること
  - pip install anthropic

出力:
  reports/SecurityTrend_Top10_YYYY-MM-DD.md
"""

import os
import json
import urllib.request
import anthropic
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))


# ── 設定 ──────────────────────────────────────────────────────────
MODEL = "claude-sonnet-4-6"   # コスト重視なら "claude-haiku-4-5-20251001" に変更可
MAX_TOKENS = 4096

# xAI Grok連携（任意）: XAI_API_KEY が設定されていない場合は自動的にスキップされ、
# 従来どおりClaude単独のweb_searchでレポートを生成する（フォールバック）。
XAI_API_KEY = os.environ.get("XAI_API_KEY")
XAI_MODEL = "grok-4.6"
XAI_ENDPOINT = "https://api.x.ai/v1/responses"
# ─────────────────────────────────────────────────────────────────


def fetch_grok_trending_topics(report_date: str) -> str | None:
    """xAI Grok API（x_search + web_search）で、直近7日間のXの投稿量・エンゲージメント
    およびニュース報道量をもとに「話題性」の高いセキュリティ関連トピック候補を収集する。

    XAI_API_KEY未設定、またはAPI呼び出し・解析に失敗した場合はNoneを返す。
    呼び出し側はNoneの場合、Claude単独のweb_searchのみで従来どおりレポートを生成する。
    """
    if not XAI_API_KEY:
        return None

    dt = datetime.strptime(report_date, "%Y-%m-%d")
    from_date = (dt - timedelta(days=7)).strftime("%Y-%m-%d")
    to_date = report_date

    # プロンプト設計はxAI (Grok) 自身の推奨テンプレートを参考に、評価基準の明示・
    # 話題性スコアの自己評価・信頼できる情報源の指定・未確認情報のマーキングを組み込んでいる。
    prompt = f"""あなたはサイバーセキュリティ・データプライバシー・AIリスク・暗号資産セキュリティの専門アナリストです。

{from_date} 00:00〜{to_date} 09:00（JST基準、直近1週間のうち特に直近24〜48時間の動きを重視）の期間で、
以下5つの対象領域から特に話題性の高かったトピックを、カテゴリごとに2〜4件抽出してください。

【対象領域】
- Cyber Security（脆弱性、攻撃キャンペーン、APT、ランサムウェアなど）
- AI Risk（モデル悪用、エージェント型攻撃、安全性・アラインメント問題、蒸留攻撃など）
- Data & Privacy（大規模漏洩、規制、個人情報侵害）
- Security Governance（規制執行、コンプライアンス、業界標準）
- Crypto Currency（ウォレット侵害、フィッシング、サプライチェーン攻撃、オンチェーン関連）

【話題性の評価基準】（優先順位順）
1. 報道量・複数メディアでの取り上げ頻度
2. 実際の影響規模（被害組織数・ユーザー数・金額など）
3. 技術的新規性・攻撃手法の進化
4. 政策・規制・業界への波及度
5. X（旧Twitter）での議論の活発さ・エンゲージメント（投稿数・いいね/リポスト/返信の多さ）

情報源はSecurityWeek、BleepingComputer、The Hacker News、CISA、Anthropic公式など信頼できる媒体を優先してください。
事実に基づき推測は最小限にし、確認できない情報は「未確認」と明記してください。日本語で回答してください。

各トピックについて、Markdownの箇条書きで以下を出力してください（前置き・後置きの説明文は不要）:
- タイトル（簡潔に）とカテゴリ
- 要約（150〜200文字程度）
- 話題性の根拠（上記評価基準のうちどれに該当するか、具体的な数値・報道状況を含めて）
- 話題性スコア（1〜10の自己評価）
- 参照できるURLと日付（複数可）"""

    payload = {
        "model": XAI_MODEL,
        "input": [{"role": "user", "content": prompt}],
        "tools": [
            {"type": "x_search", "from_date": from_date, "to_date": to_date},
            {"type": "web_search"},
        ],
    }

    req = urllib.request.Request(
        XAI_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {XAI_API_KEY}",
        },
        method="POST",
    )

    try:
        # x_search + web_search を使った複数ラウンドのエージェント的検索は時間がかかりやすいため
        # タイムアウトを長めに設定する（GitHub Actionsのジョブ制限時間は十分に余裕がある）。
        with urllib.request.urlopen(req, timeout=280) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"⚠️  Grok API呼び出しに失敗しました（Claude単独のWeb検索で続行します）: {e}")
        return None

    try:
        chunks = []
        for item in data.get("output", []):
            if item.get("type") == "message":
                for c in item.get("content", []):
                    if c.get("type") in ("output_text", "text") and c.get("text"):
                        chunks.append(c["text"])
        text = "\n".join(chunks).strip()
        return text or None
    except Exception as e:
        print(f"⚠️  Grok APIレスポンスの解析に失敗しました（Claude単独のWeb検索で続行します）: {e}")
        return None


def get_japanese_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    return f"{dt.year}年{dt.month}月{dt.day}日（{weekdays[dt.weekday()]}）"


def get_next_japanese_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    return f"{dt.year}年{dt.month}月{dt.day}日（{weekdays[dt.weekday()]}）"


def build_prompt(report_date: str, today_jp: str, tomorrow_jp: str, grok_topics: str | None = None) -> str:
    grok_section = ""
    if grok_topics:
        grok_section = f"""
## 話題性分析の参考情報（xAI Grok APIによる事前収集）
以下は、xAI Grok API（X Search + Web Search）が直近7日間のX投稿量・エンゲージメントおよび
ニュース報道量をもとに抽出した「話題性の高いトピック候補」です。
Top10選定にあたっては、このリストにあるトピックを優先的に検討してください。
ただし内容が古い・裏付けが取れない場合は採用せず、自分のweb_searchで最新情報の確認・補完を行ってください。
このリストにない重要な速報がある場合は、そちらを優先して構いません。

---Grok話題性分析 開始---
{grok_topics}
---Grok話題性分析 終了---
"""

    return f"""あなたはセキュリティトレンド情報収集エージェントです。

今日の日付: {report_date}（{today_jp}）
翌日の日付: {tomorrow_jp}
{grok_section}
以下の5カテゴリで最新ニュースをweb_searchツールを使って検索してください:
1. cyber security news {report_date} latest breach vulnerability
2. AI risk security news {report_date}
3. data privacy regulation news {report_date}
4. security governance compliance news {report_date}
5. cryptocurrency crypto security hack fraud regulation news {report_date}

収集した記事の中から重要度・新規性・影響範囲（Grok話題性分析がある場合はそれも加味）を基準にTop10を選定し
（Crypto Currencyを必ず1〜2件含めること）、
以下のフォーマットに厳密に従ってMarkdownレポートを生成してください。
Markdownテキストのみを出力し、前置き・後置きの説明文は不要です。

---フォーマット開始---
# セキュリティトレンド Top 10 ニュース
**配信日：{today_jp}**

> ⚠️ この記事はClaudeのAIが独自に収集・編集したものです。情報の正確性については各ソースをご確認ください。

---

## 🔥 今日のトレンドワード Top 5

| # | トレンドワード | 解説 |
|---|--------------|------|
| 1 | **キーワード1** | 1〜2行の解説 |
| 2 | **キーワード2** | 1〜2行の解説 |
| 3 | **キーワード3** | 1〜2行の解説 |
| 4 | **キーワード4** | 1〜2行の解説 |
| 5 | **キーワード5** | 1〜2行の解説 |

---

## 🔴 Cyber Security

### 1. タイトル
**日付**
本文（2〜4行）

🔗 [記事タイトル](URL)

---

（Cyber Securityは3〜4件、同形式で繰り返す）

## 🟠 AI Risk

（1〜2件、同形式）

## 🟡 Data & Privacy

（1〜2件、同形式）

## 🟢 Security Governance

（1〜2件、同形式）

## 🟣 Crypto Currency

（1〜2件、同形式）

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | キーワード |
| AI Risk | 🟠🟠🟠🟠 | キーワード |
| Data & Privacy | 🟡🟡🟡 | キーワード |
| Security Governance | 🟢🟢🟢 | キーワード |
| Crypto Currency | 🟣🟣🟣 | キーワード |

---

*次回配信予定：{tomorrow_jp} | 収集ソース：使用したメディア名*
---フォーマット終了---"""


def generate_report(report_date: str) -> str:
    """Claude APIを呼び出してMarkdownレポートを生成する"""
    today_jp    = get_japanese_date(report_date)
    tomorrow_jp = get_next_japanese_date(report_date)

    grok_topics = fetch_grok_trending_topics(report_date)
    if grok_topics:
        print("✅ Grok API（X Search + Web Search）で話題性の高いトピック候補を取得しました")
    else:
        print("ℹ️  Grok連携なし（XAI_API_KEY未設定 or 取得失敗）→ Claude単独のWeb検索で続行します")

    prompt = build_prompt(report_date, today_jp, tomorrow_jp, grok_topics)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    print(f"🤖 Claude API ({MODEL}) でレポート生成中...")

    # web_search ツールを有効にしてリクエスト
    # Claude が web_search を複数回使う場合に備えてループで処理
    messages = [{"role": "user", "content": prompt}]
    md_content = ""

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=messages,
        )

        # テキストブロックを収集
        # web_search中はClaudeが「検索します」等の前置きを複数回はさむことがあり、
        # response.content内に複数のtextブロックが混在する（例:「検索します」→検索結果→「レポートを生成します」→本文）。
        # 途中の独り言がレポートに混入しないよう、各レスポンスの「最後のtextブロック」のみを採用する
        # （実際の成果物は常に最後に出力されるため）。
        text_blocks = [b.text for b in response.content if b.type == "text"]
        if text_blocks:
            md_content = text_blocks[-1]

        # 終了条件: end_turn になったら完了
        if response.stop_reason == "end_turn":
            break

        # tool_use が返ってきた場合（サーバーサイドツールの場合は通常ここには来ないが念のため）
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    # web_search はサーバーサイドツールのため結果は空で返す
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": ""
                    })
            messages.append({"role": "user", "content": tool_results})
            continue

        # その他の stop_reason は終了
        break

    if not md_content.strip():
        raise ValueError("レポートの生成に失敗しました（空のレスポンス）")

    # 保険: 万一「# セキュリティトレンド」より前に前置き文が残っていた場合は切り落とす
    heading_pos = md_content.find("# セキュリティトレンド")
    if heading_pos > 0:
        md_content = md_content[heading_pos:]

    return md_content


def main():
    report_date = os.environ.get("REPORT_DATE", datetime.now(JST).strftime("%Y-%m-%d"))
    print(f"[{datetime.now(JST).strftime('%Y-%m-%d %H:%M')}] generate_report.py 開始")
    print(f"📅 対象日: {report_date}")

    # レポート生成
    md_content = generate_report(report_date)

    # ファイル保存
    os.makedirs("reports", exist_ok=True)
    output_path = f"reports/SecurityTrend_Top10_{report_date}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"✅ レポート保存完了: {output_path}")
    print(f"   文字数: {len(md_content):,}")


if __name__ == "__main__":
    main()
