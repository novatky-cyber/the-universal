# ADR-0003 PDFはMarkdown→HTML→Chrome印刷で生成する

- 日付：2026-11-23／状態：採用

## 背景
毎回同じ固定フォーマットの日本語PDF（A4縦、書き込み余白、図、色付きラベル）を自動生成する必要がある。

## 選択肢
1. Markdown → HTML（Jinja2）→ Chrome（Playwright）でPDF化
2. ReportLab で直接描画
3. LaTeX

## 決定
1を採用。

## 理由
- CSSで体裁を一元管理でき、SVGの図をそのまま埋め込める。
- 日本語の組版（Noto CJK）が安定している。作業環境にChromeとPlaywrightがある。
- 原稿がMarkdownなので、エージェントが書きやすく、Gitで差分が読める。

## 影響
Chrome／Playwrightが使えない環境ではPDFを生成できない。その場合はHTMLを残し、レポートに記載する。
