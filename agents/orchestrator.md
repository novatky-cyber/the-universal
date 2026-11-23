# Orchestrator（指揮）— 自律学習サイクル実行手順

定期実行タスクから起動されたセッションは、本書の手順を上から順に実行する。
前提：`CLAUDE.md` を読み終えていること。

## 0. 準備
0. 環境の準備：`bash tools/setup_fonts.sh`（PDFの書体）。ビューアの撮影確認には three.js のローカルコピーが必要（`mkdir -p /tmp/threepkg && cd /tmp/threepkg && npm init -y && npm install three@0.160.0`）。
1. `data/state.json` を読み、`cycle` を +1 した番号 NNNN（4桁）を今回のサイクル番号とする。
2. `git checkout -b cycle/NNNN`
3. `content/cycles/NNNN/` を作る。
4. `python3 tools/check_all.py` を実行し、開始時点で壊れていないことを確認する（壊れていたら修正を最優先の作業にする）。
5. ユーザーの指示が `state.awaiting_user` やチャット経由で届いていれば、それを最優先で反映する。

## 1. 計画（Planner：`agents/planner.md`）
- 入力：`state.json`、`curriculum.json`、`understanding.json`、`questions.json`、前回のレポート。
- DOC-04 §4（v1.2）に従い、回答の有無にかかわらず**毎回次のセッションへ進む**。同じセッションをやり直さない。回答の評価結果は、次の教材の第1節（事前チェック・復習）に反映する。
- カリキュラムの最後（P04）の後は、Phase 05 の深掘りシリーズ（`curriculum.json` の P05）を順に進める。ユーザーの要望（`questions.json` の origin=user で open のもの）があれば、P05 にセッションを追加して最優先で扱う（DOC-01 v1.3）。
- 出力：`content/cycles/NNNN/plan.md`（中心の問い、扱うノード、調査の分担、訂正候補、拡張の上限）。

## 2. 調査（Researcher：`agents/researcher.md`）
- plan.md の分担ごとに**サブエージェントを並行起動**する（2〜4体）。
- 各サブエージェントへの依頼文には、担当範囲・中心の問い・`agents/researcher.md` の全文・既存ノードの一覧（ID・名称・要約）を含める。
- 出力：`content/cycles/NNNN/research/<担当>.md`（主張ごとに出典・認識ラベル）。

## 3. 反論・多視点（Challenger：`agents/challenger.md`）
- サブエージェント1体。plan.md と research の要旨を渡す。
- 出力：`content/cycles/NNNN/research/challenge.md`。

## 4. 独立検証（Verifier：`agents/verifier.md`）
- research と challenge から「主張リスト」（主張・ラベル・出典ID・URL）を作り、`content/cycles/NNNN/claims.md` に保存する。
- サブエージェント1〜2体に、claims.md と `agents/verifier.md` のみを渡す（調査の経緯・下書きは渡さない）。
- 出力：`content/cycles/NNNN/verification.md`。判定が「確認済み」以外の主張は、修正して再検証するか、保留にする。

## 4b. あなたのメモの取り込みと検証（DOC-01 F11、DOC-04 §2 の6）
1. Notion で3つの用語集の索引ページ（「AI用語集」「ビジネス用語集」「用語集」。Memo の下）を検索して開き、子ページの notion_id を集める。`data/import/notion_glossary.json` にも、移行スクリプトの除外リスト（`EXCLUDE`：notion_id の SHA-1 先頭16桁）にもない notion_id だけを新しい用語として、同じ形式（題名・英語名・1〜2文の定義・notion_id・kind）で追記する。既存の用語の定義がNotion側で変わっていれば、その項目の definition を更新する。Notion の接続が使えないときは、この手順を飛ばしてレポートに書く。Notionは**読むだけで書き換えない**。顧客・案件・議事録・私生活のページ、公人以外の個人名は取り込まない。
2. `python3 tools/migrations/0002_import_notion_glossary.py` を実行する（何度実行しても同じ結果）。除外が必要なものは、スクリプトの `EXCLUDE_TITLES` に理由つきで足す。
3. Verifier（ステップ4と同じサブエージェントでよい）に、未検証の用語ノードから約10件を渡し、定義が一般的な理解・信頼できる資料と合っているかを確かめさせる。問題がなければ `verification.status` を verified（`by` に「verifier（あなたのメモの確認）」）にする。誤り・古さ・誤解を招く点があれば、ノードは直さず（正本はNotion）、変更点レポートの「あなたのメモへの指摘」に、用語名・指摘・根拠を書く。

## 5. 地図の統合（Cartographer：`agents/cartographer.md`）
- 確認済みの主張だけを `data/graph/*.json`・`data/sources.json` に反映する。
- `python3 tools/validate.py` を通す。

## 6. 教材の執筆（Educator：`agents/educator.md`）
- 出力：`content/cycles/NNNN/lesson.md`（DOC-03 §2 の記法、全セクション）。
- 教材に新たに書いた主張で、claims.md にないものは、追加の検証に回す。

## 7. 問題作成（Examiner：`agents/examiner.md` §作問）
- 教材第1節（復習）・第12節（説明課題）・第13節（確認問題）・付録A（解答）・付録C（回答提出用プロンプト）を作る。

## 8. 変更点レポート
- `python3 tools/map_diff.py`（引数なしで直前の版と比較）の結果をもとに `content/cycles/NNNN/report.md` を書く（DOC-03 §2.2、レポートの11節）。
- 訂正は重要度（DOC-04 §5）を付ける。保留事項・提案（要件変更の提案はここだけ）を書く。

## 9. 品質確認（Editor：`agents/editor.md`）
- `python3 tools/render_pdf.py content/cycles/NNNN` → `python3 tools/build_viewer_data.py` → `python3 tools/check_all.py`
- サブエージェント1体にPDFの見た目を確認させる（ページを画像化して渡す）。指摘を直す。

## 10. 公開
1. `data/state.json` を更新：cycle、map_version（MINOR+1）、last_run、current_session、next_cycle_plan、pending。
2. `data/understanding.json` の、今回の教材で扱ったノードの status を `presented` に（levelは変えない）。
3. コミット → `main` にマージ → push。マージ後のコミットを `state.map_refs["<版>"]` に記録して、もう一度コミット・push する（`git tag map-v<版>` は可能なら）。
4. 最後のメッセージに、ユーザー向けの要約（3〜5行）と、PDF2本のGitHub上のURLを書く。これが通知に表示される。

## 失敗時
- どの段階でも、解決できない失敗があれば `main` にマージしない。`state.json` の `pending` に記録した小さなコミットだけを `main` に入れ、次回に再試行する。
- 利用上限に近づいたら、調査（2〜3）の範囲を縮小し、教材は前回の続きの深化に切り替える。縮小したことをレポートに書く。

## サブエージェントの数の目安（合計8体以下）
Researcher 2〜4／Challenger 1／Verifier 1〜2／Editor 1
