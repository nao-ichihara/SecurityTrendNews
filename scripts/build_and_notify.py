"""
GitHub Actions上で実行されるスクリプト
- 最新の .md レポートからHTMLを生成
- index.htmlを更新
- LINEに通知を送信

環境変数（GitHub Secrets）:
  LINE_TOKEN   : LINEチャンネルアクセストークン
  LINE_USER_ID : LINE送信先ユーザーID
  PAGES_BASE_URL: GitHub PagesのベースURL（例: https://nao-ichihara.github.io/SecurityTrendNews）
"""

import os
import re
import glob
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta


# ── 設定（環境変数から取得） ─────────────────────────
LINE_TOKEN     = os.environ.get("LINE_TOKEN", "")
LINE_USER_ID   = os.environ.get("LINE_USER_ID", "")
PAGES_BASE_URL = os.environ.get("PAGES_BASE_URL", "").rstrip("/")
# ────────────────────────────────────────────────────


def md_to_html(md_content: str, report_date: str) -> str:
    """MarkdownをGitHub Pages用スタイル付きHTMLに変換"""
    escaped = md_content.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SecurityTrend Top10 - {report_date}</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"></script>
  <style>
    :root {{
      --bg: #0f1117; --surface: #1a1d27; --border: #2d3148;
      --text: #e2e8f0; --muted: #8892a4; --accent: #6366f1;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.7; }}
    .container {{ max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem; }}
    .header {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2rem; display: flex; align-items: center; gap: 1rem; }}
    .header-logo {{ font-size: 2rem; }}
    .header-title {{ font-size: 1.4rem; font-weight: 700; color: var(--accent); }}
    .header-date {{ font-size: 0.9rem; color: var(--muted); margin-top: 0.25rem; }}
    .badge {{ display: inline-block; background: rgba(99,102,241,0.15); border: 1px solid var(--accent); color: var(--accent); font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 20px; margin-top: 0.5rem; }}
    #content h1 {{ display: none; }}
    #content h2 {{ font-size: 1.1rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; margin: 2.5rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border); }}
    #content h3 {{ font-size: 1.05rem; font-weight: 600; color: var(--text); margin: 1.5rem 0 0.5rem; }}
    #content p {{ color: #c8d3e0; margin-bottom: 0.75rem; }}
    #content a {{ color: var(--accent); text-decoration: none; }}
    #content a:hover {{ text-decoration: underline; }}
    #content hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }}
    #content blockquote {{ border-left: 3px solid var(--accent); padding: 0.75rem 1rem; background: rgba(99,102,241,0.08); border-radius: 0 8px 8px 0; margin: 1rem 0; color: var(--muted); font-size: 0.9rem; }}
    #content table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }}
    #content th {{ background: var(--surface); padding: 0.6rem 1rem; text-align: left; border: 1px solid var(--border); color: var(--muted); font-weight: 600; }}
    #content td {{ padding: 0.6rem 1rem; border: 1px solid var(--border); }}
    #content tr:hover td {{ background: rgba(99,102,241,0.05); }}
    .footer {{ margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); text-align: center; color: var(--muted); font-size: 0.85rem; }}
    .back-link {{ display: inline-block; margin-top: 1rem; color: var(--accent); text-decoration: none; font-size: 0.9rem; }}
    .back-link:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="header-logo">🔐</div>
      <div>
        <div class="header-title">SecurityTrend Top10</div>
        <div class="header-date">{report_date}</div>
        <div class="badge">AI Generated Report</div>
      </div>
    </div>
    <div id="content"></div>
    <div class="footer">
      <p>このレポートはClaudeのAIが独自に収集・編集したものです</p>
      <a class="back-link" href="../index.html">← 過去レポート一覧へ</a>
    </div>
  </div>
  <script>
    const md = `{escaped}`;
    document.getElementById('content').innerHTML = marked.parse(md);
  </script>
</body>
</html>"""


def build_index_html(entries: list) -> str:
    """一覧index.htmlを生成（entries: [(date, url), ...]）"""
    rows = ""
    for date, url in entries:
        rows += f'      <tr><td>{date}</td><td><a href="{url}">レポートを読む →</a></td></tr>\n'
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SecurityTrend Top10 - レポート一覧</title>
  <style>
    :root {{ --bg:#0f1117; --surface:#1a1d27; --border:#2d3148; --text:#e2e8f0; --muted:#8892a4; --accent:#6366f1; }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ background:var(--bg); color:var(--text); font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }}
    .container {{ max-width:700px; margin:0 auto; padding:3rem 1.5rem; }}
    h1 {{ font-size:1.6rem; font-weight:700; color:var(--accent); margin-bottom:0.5rem; }}
    .subtitle {{ color:var(--muted); font-size:0.9rem; margin-bottom:2rem; }}
    table {{ width:100%; border-collapse:collapse; }}
    th {{ background:var(--surface); padding:0.75rem 1rem; text-align:left; border:1px solid var(--border); color:var(--muted); font-size:0.85rem; text-transform:uppercase; letter-spacing:0.05em; }}
    td {{ padding:0.75rem 1rem; border:1px solid var(--border); }}
    tr:hover td {{ background:rgba(99,102,241,0.05); }}
    a {{ color:var(--accent); text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .footer {{ margin-top:2rem; color:var(--muted); font-size:0.8rem; text-align:center; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>🔐 SecurityTrend Top10</h1>
    <p class="subtitle">Claude AIが毎日収集・編集するセキュリティトレンドレポート</p>
    <table>
      <thead><tr><th>配信日</th><th>レポート</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
    <div class="footer">AIが独自に収集・編集した情報です</div>
  </div>
</body>
</html>"""


def update_index_html(report_date: str, report_pages_url: str):
    """index.htmlにエントリを追加（ローカルファイルI/O）"""
    index_path = "index.html"
    entries = []
    if os.path.exists(index_path):
        with open(index_path, encoding="utf-8") as f:
            existing = f.read()
        for m in re.finditer(r'<tr><td>(.+?)</td><td><a href="(.+?)">', existing):
            entries.append((m.group(1), m.group(2)))

    if not any(d == report_date for d, _ in entries):
        entries.insert(0, (report_date, report_pages_url))

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(build_index_html(entries))
    print(f"✅ index.html 更新: {len(entries)}件")


def md_to_line_summary(md: str, report_date_str: str, report_url: str, index_url: str) -> str:
    """LINE向け簡潔サマリーを生成"""
    next_date_jp = ""
    try:
        report_dt = datetime.strptime(report_date_str, "%Y-%m-%d")
        next_dt = report_dt + timedelta(days=1)
        weekdays_jp = ["月", "火", "水", "木", "金", "土", "日"]
        next_date_jp = f"{next_dt.year}年{next_dt.month}月{next_dt.day}日（{weekdays_jp[next_dt.weekday()]}）"
    except ValueError:
        pass

    delivery_date, trend_words, headlines, current_category = "", [], [], ""
    for line in md.splitlines():
        if line.startswith("**配信日："):
            delivery_date = line.strip("*").replace("配信日：", "").strip()
        elif line.startswith("## 🔴"):
            current_category = "🔴 Cyber Security"
        elif line.startswith("## 🟠"):
            current_category = "🟠 AI Risk"
        elif line.startswith("## 🟡"):
            current_category = "🟡 Data & Privacy"
        elif line.startswith("## 🟢"):
            current_category = "🟢 Security Governance"
        elif line.startswith("### "):
            title = re.sub(r'\*\*(.+?)\*\*', r'\1', line[4:])
            headlines.append(f"{current_category}｜{title}")
        elif re.match(r'^\|\s*\d+\s*\|', line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            cells = [re.sub(r'\*\*(.+?)\*\*', r'\1', c) for c in cells if c and not re.match(r'^-+$', c)]
            if len(cells) >= 2:
                trend_words.append(f"  {cells[0]}. {cells[1]}")

    parts = [
        "=" * 28,
        "🔐 SecurityTrend Top10",
        f"📅 {delivery_date}",
        "=" * 28,
        "※ AIが独自に収集・編集した情報です",
    ]
    if trend_words:
        parts += ["", "【🔥 今日のトレンドワード】"] + trend_words[:5]
    if headlines:
        parts += ["", "【📋 今日のTop10】"]
        for i, h in enumerate(headlines[:10], 1):
            parts.append(f"{i}. {h}")
    parts += ["", "─" * 14]
    if next_date_jp:
        parts.append(f"次回配信：{next_date_jp}")
    if report_url:
        parts += ["", "📰 詳細レポート（Web）", report_url]
    if index_url:
        parts += ["", "📚 過去レポート一覧", index_url]

    return "\n".join(parts)


def send_line_message(text: str) -> bool:
    """LINE Push Messageを1通で送信"""
    if not LINE_TOKEN or not LINE_USER_ID:
        print("⚠️ LINE_TOKEN / LINE_USER_ID が未設定です（GitHub Secretsを確認）")
        return False
    if len(text) > 4900:
        text = text[:4850] + "\n…\n（詳細はWebリンクを確認）"

    payload = json.dumps({"to": LINE_USER_ID, "messages": [{"type": "text", "text": text}]}).encode()
    req = urllib.request.Request(
        "https://api.line.me/v2/bot/message/push",
        data=payload,
        headers={"Authorization": f"Bearer {LINE_TOKEN}", "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as res:
            print(f"✅ LINE送信成功 (HTTP {res.status}) / {len(text)}文字")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ LINE送信失敗 (HTTP {e.code}): {e.read().decode()}")
        return False


def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] build_and_notify 開始")

    # 最新の .md ファイルを取得
    files = sorted(glob.glob("reports/SecurityTrend_Top10_*.md"), reverse=True)
    if not files:
        print("❌ reports/ に .mdファイルが見つかりません")
        return

    latest_md_path = files[0]
    filename = os.path.basename(latest_md_path)
    report_date = filename.replace("SecurityTrend_Top10_", "").replace(".md", "")
    print(f"📄 処理対象: {filename} ({report_date})")

    with open(latest_md_path, encoding="utf-8") as f:
        md_content = f.read()

    # HTML生成・保存
    html_filename = filename.replace(".md", ".html")
    html_path = f"reports/{html_filename}"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(md_to_html(md_content, report_date))
    print(f"✅ HTML生成: {html_path}")

    # GitHub Pages URL
    report_url = f"{PAGES_BASE_URL}/reports/{html_filename}" if PAGES_BASE_URL else ""
    index_url  = f"{PAGES_BASE_URL}/" if PAGES_BASE_URL else ""

    # index.html 更新
    update_index_html(report_date, report_url)

    # LINE送信
    text = md_to_line_summary(md_content, report_date, report_url, index_url)
    print(f"📝 LINEメッセージ文字数: {len(text)}")
    send_line_message(text)


if __name__ == "__main__":
    main()
