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
import anthropic
from datetime import datetime, timedelta


# ── 設定 ──────────────────────────────────────────────────────────
MODEL = "claude-sonnet-4-6"   # コスト重視なら "claude-haiku-4-5-20251001" に変更可
MAX_TOKENS = 4096
# ─────────────────────────────────────────────────────────────────


def get_japanese_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    return f"{dt.year}年{dt.month}月{dt.day}日（{weekdays[dt.weekday()]}）"


def get_next_japanese_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    return f"{dt.year}年{dt.month}月{dt.day}日（{weekdays[dt.weekday()]}）"


def build_prompt(report_date: str, today_jp: str, tomorrow_jp: str) -> str:
    return f"""あなたはセキュリティトレンド情報収集エージェントです。

今日の日付: {report_date}（{today_jp}）
翌日の日付: {tomorrow_jp}

以下の4カテゴリで最新ニュースをweb_searchツールを使って検索してください:
1. cyber security news {report_date} latest breach vulnerability
2. AI risk security news {report_date}
3. data privacy regulation news {report_date}
4. security governance compliance news {report_date}

収集した記事の中から重要度・新規性・影響範囲を基準にTop10を選定し、
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

（Cyber Securityは4〜5件、同形式で繰り返す）

## 🟠 AI Risk

（2〜3件、同形式）

## 🟡 Data & Privacy

（1〜2件、同形式）

## 🟢 Security Governance

（1〜2件、同形式）

## 📊 今日のカテゴリ別注目度

| カテゴリ | 注目度 | 主なキーワード |
|----------|--------|----------------|
| Cyber Security | 🔴🔴🔴🔴🔴 | キーワード |
| AI Risk | 🟠🟠🟠🟠 | キーワード |
| Data & Privacy | 🟡🟡🟡 | キーワード |
| Security Governance | 🟢🟢🟢 | キーワード |

---

*次回配信予定：{tomorrow_jp} | 収集ソース：使用したメディア名*
---フォーマット終了---"""


def generate_report(report_date: str) -> str:
    """Claude APIを呼び出してMarkdownレポートを生成する"""
    today_jp    = get_japanese_date(report_date)
    tomorrow_jp = get_next_japanese_date(report_date)
    prompt      = build_prompt(report_date, today_jp, tomorrow_jp)

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
        text_blocks = [b.text for b in response.content if b.type == "text"]
        if text_blocks:
            md_content = "\n".join(text_blocks)

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

    return md_content


def main():
    report_date = os.environ.get("REPORT_DATE", datetime.now().strftime("%Y-%m-%d"))
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] generate_report.py 開始")
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
