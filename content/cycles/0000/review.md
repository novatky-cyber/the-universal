# コードレビュー：dev/v0.5-glossary-orientation（Reviewer・独立）

- 対象：`git diff main...HEAD -- tools/ viewer/app.js viewer/style.css index.html data/schema/ docs/02_基本設計書.md docs/03_詳細設計書.md docs/05_テスト計画.md agents/`
- 照合した設計書：DOC-03 v3.2（§1.3・§3.1〜3.2・§3.6・§4.3）、DOC-05 v1.1（T-11）、`agents/dev.md`（Reviewer）
- 実施した確認（リポジトリの複製 `/tmp` で実施。本リポジトリのファイルとgitは変更していない）
  - `python3 tools/validate.py`：OK（未検証 311/356 の警告のみ）
  - `0002_import_notion_glossary.py` を複製上で2回目実行：4ファイルとも1回目とバイト一致（同じ日付・同じ入力なら冪等）
  - 複製上で、用語ノード1件を verified にし、受け皿テーマに出典を付けてから再実行 → **両方とも消えて unverified／出典なしに戻った**（指摘 H-01）
  - 複製上で、用語ノードの `sources` を空にして `validate.py` → **OK のまま通った**（指摘 M-03）
  - `nodes.json` の並び：main では ID 昇順、本ブランチでは昇順でない（指摘 M-05）
  - 新しい図4点を Chromium で描画し、全 `<text>` の getBBox を viewBox と照合：はみ出し0、文字どうしの重なり0
  - `screenshot_viewer.py`（three・書体はローカル）：16枚撮影、コンソールエラーなし。iphone_term・iphone_glossary・desktop を目視

## 指摘

| ID | 重要度 | 場所 | 指摘 | 修正案 |
|---|---|---|---|---|
| H-01 | 高 | `tools/migrations/0002_import_notion_glossary.py` `main()`（`nodes = [n for n in nodes if n["type"] != "term" and n["id"] not in NEW_THEMES]`） | 再実行のたびに用語ノードと受け皿4テーマを**作り直す**ため、後から付いた情報が消える。`agents/orchestrator.md` 4b は毎サイクル「追記→本スクリプト実行→Verifierが verified にする」の順なので、**前サイクルで Verifier が付けた `verification`（verified・by・日付）が次サイクルの実行で毎回 unverified に戻る**（複製で再現済み）。受け皿テーマに今後付ける出典（スクリプト内コメント「出典は今後のサイクルで付ける」）、`history`、`perspectives`、`curriculum` も同様に消える。R-05（1サイクル約10件ずつ確認）が永久に積み上がらない。 | 既存ノードを ID で引き、取り込み元が持つ項目（title・summary・domains・parent・glossary・note_kind）だけを更新し、`verification`・`sources`（テーマ）・`history`・`curriculum` 等は保持する（upsert）。定義が変わった用語だけ `verification` を unverified に戻し、`history` に「定義の更新」を追記する。テーマは「無ければ作る」に変える。 |
| H-02 | 高 | 同 `EXCLUDE`／`title_hash`、`data/import/notion_glossary_import_log.json` | 除外の指定と公開ログが「元の題名の SHA-1 先頭16桁（塩なし）」。題名は短く候補が限られるため**辞書攻撃で題名を復元できる**。特に除外理由「市町村単位の地域メモ」は、全国約1,700の市区町村名（＋「〇〇市」「〇〇町の…」程度の変形）をハッシュして照合するだけで当たりうり、居住地・行動の推測という除外の目的そのものを損なう。業種名（顧客の業種）も同様に候補が少ない。さらに理由文が公開されていること自体が「市町村単位のメモがある」ことを示す。 | 除外キーを推測できない値にする：(a) `notion_id`（ランダムなUUID）のハッシュで指定する、または (b) 鍵つきハッシュ（HMAC、鍵は gitignore したローカルファイル／環境変数）にする。公開ログの `excluded` は件数と大分類（「プライバシー」「重複」等）だけにし、市町村・業種などの具体的な理由文は載せない。すでに push 済みなら、ハッシュを変えれば旧ハッシュは無意味になるが、履歴には残る点に注意（main へのマージ前に直すのが望ましい）。 |
| M-01 | 中 | `viewer/app.js` `buildLinks()`／`applyVisibility()` | `buildLinks` は**全ノード**の親子線を描き、表示状態を見ない。NOTES を HIDE にしても、各テーマから見えない用語の位置へ約216本の線が残る（領域絞り込み時は `groups.links` ごと隠すので出ないが、NOTES 単独では出る）。また `applyVisibility` は線を作り直さないので、SETTINGS で切り替えた直後に反映されない。 | `buildLinks` で `isShown(n.id) && isShown(n.parent)`（関係線も両端）を条件にし、`applyVisibility` の最後で `buildLinks()`（FOCUS中なら `buildHot()` と `renderChips()` も）を呼ぶ。select/clearSelection は直後に buildLinks を呼んでいるので順序だけ確認する。 |
| M-02 | 中 | 同 `slug()`、DOC-03 §1.1（「一度公開したIDは変えない」） | 用語のIDが「用語集キー＋**表示用の題名**のハッシュ」。ユーザーがNotionで題名を直す、または `clean_title` の規則を変えるとIDが変わり、`understanding.json`・今後の edges・問題の参照が切れる。H-01 と合わさると履歴も失われる。 | IDのハッシュ部分を `notion_id` から作る（例 `trm.ai-<ascii>-<sha1(notion_id)[:8]>`）。既存216件は対応表で移行するか、今回はまだ公開直後なので本ブランチ内で切り替える。ADR-0006 に「IDは notion_id 由来」と記す。 |
| M-03 | 中 | `tools/validate.py` T-11 | 条件が `any(src_kind.get(s) != "user-note" for s in n["sources"])` なので、**`sources` が空の用語ノードが通る**（複製で確認）。DOC-05 T-11 は「user-note の出典を持ち」。また glossary と出典の対応（ai の用語に business の出典など）も見ていない。 | `not n["sources"]` をエラー条件に加える。可能なら `GLOSSARY_SOURCE = {"ai": "src.notion-ai-glossary", ...}` を common.py に置き、`n["sources"] == [GLOSSARY_SOURCE[n["glossary"]]]` を検査する。edges の `sources` に user-note が使われていないかも T-11 に含めるとよい（絶対ルール5の趣旨）。 |
| M-04 | 中 | `agents/orchestrator.md` 4b-1 と移行スクリプトの書き戻し | 4b-1 は「`notion_glossary.json` にない新しい用語だけ追記」と**題名で差分を取る**前提だが、スクリプトは取り込み元を表示用の題名（「｜」以降・日付・v番号・「提案実務」を除去）に書き換え、除外分を削除する。次サイクルで Notion の生の題名と比べると、題名を整えた項目と除外した項目が毎回「新しい用語」とみなされ、(1) 除外した題名が作業ツリーの公開ファイルに再び書かれる（移行に失敗したまま commit されると漏れる）、(2) 取り込み元に重複が増える。 | 差分は `notion_id` で取ると明記する（4b-1 の文言とスクリプトの両方）。除外した `notion_id`（またはそのハッシュ、H-02）を照合用に残し、追記の段階で弾く。 |
| M-05 | 中 | 同 `main()` の書き出し、DOC-02 §3-1（「nodes.json：IDで昇順に並べる」） | 用語とテーマを末尾に追加して並べ替えないため、`nodes.json` が ID 昇順でなくなった（main では昇順）。差分が読みにくくなり、他のツールが同じ規則で書くと毎回大きな差分が出る。 | 書き出し前に `nodes.sort(key=lambda n: n["id"])`。validate に昇順の検査（警告でも可）を足す。 |
| M-06 | 中 | 同 `TODAY = "2026-11-24"`、`history` の `map_version: "1.1"` | 毎サイクル実行する前提なのに日付と地図の版が固定。今後の取り込みでも `checked_at`・`imported_at`・history がすべて 2026-11-24／1.1 になり、変更点レポート・map_diff の記録が誤る。 | `datetime.date.today()`（または `--date` 引数）と `state.json` の `map_version` を使う。冪等性の確認は「同じ日付・同じ入力なら同じ結果」と定義し直す。 |
| M-07 | 中 | `tools/build_viewer_data.py` `glossaries`（`s["id"].split("-")[1]`） | 資料IDの命名（`src.notion-<key>-glossary`）にキーの切り出しを依存させている。`src.notion-ai-glossary-2` や `src.user-notes-ai` 等に変わると黙って誤ったキーになり、GLOSSARY が空になる。並び順も sources.json の順に依存。 | 資料に `glossary` 属性（ai／business／general）を持たせ schema に追加するか、移行スクリプトの `GLOSSARIES` を common.py に移して両方から参照する。ビューアの並びは ai→business→general に固定する。 |
| L-01 | 低 | `tools/common.py` `positions()`／`build_viewer_data.py` の timeless の x | 用語（216件、全ノードの約6割）が他の時間なしノードと**同じ領域内の等間隔の列**に入るため、用語を足すと既存の思考法・問いなどの x 位置がずれる（地図の配置が取り込みのたびに動く）。また時間なしノードは時間軸の −95〜−5 に並ぶ既存仕様のため、desktop.png では「生成AIの実装と活用」「経営と業務の実務」などが 13.8 Gyr〜100 Myr の目盛りの上に見え、時間の位置と誤読されやすい（既存仕様の問題が件数増で目立つようになった）。 | 用語は別の列（例：用語だけで等間隔、または ID ハッシュで −95〜−5 に散らす）にし、既存ノードの位置を変えない。時間なしの帯に目盛りと区別する表示（例「TIMELESS」の帯ラベル）を検討する。DOC-03 §3.1 に追記。 |
| L-02 | 低 | `common.py` 半径 3.2〜5.4 | 時間を持つテーマ（level 2）の半径は 6±1 = 5〜7 なので、5.0〜5.4 で用語の殻とテーマが重なる。 | 用語を 3.0〜4.8 程度にする、または DOC-03 §3.2 に重なりを許容すると記す。 |
| L-03 | 低 | 移行スクリプト（用語ノードの `epistemic: "fact"`）、DOC-03 §1.3 | 未検証のユーザーメモ（うち75件は「経済学入門」「政治イデオロギー」等の解説記事 `note_kind: topic`）に一律「事実」ラベルが付き、パネルに「TERM — 事実」と表示される。CLAUDE.md §3-1 のラベルの趣旨（事実・理論・論争の区別）に照らすと強すぎる。 | 設計判断として、用語は unverified の間は epistemic を表示しない（パネルで origin=user-note のときラベルを「メモ」とする）か、topic は `theory` 等にする。DOC-03 を先に改訂。 |
| L-04 | 低 | 移行スクリプト `place()` | ai 用語集の場合だけ「題名が Transformer／半導体のときに RULES を回す」という二重の判定で読みにくい。general の既定が `thm.world-history` のため、規則に当たらない一般用語がすべて世界史に入る。 | `RULES` に用語集の指定（`(keys, pattern, value)`）を持たせて1本のループにする。既定に落ちた件数を実行時に表示し、変更点レポートで確認できるようにする。 |
| L-05 | 低 | DOC-03 §1.3 と `clean_title()` | 設計書は「題名の『｜』以降は除く」とだけあるが、実装は日付の接頭辞・v番号・「提案実務」の除去と「心理学効果」の改名もしている（設計書にない変更）。 | DOC-03 §1.3 に名前の整え方の規則を列挙する（絶対ルール2）。 |
| L-06 | 低 | `viewer/app.js` SETTINGS の NOTES 切替 | 切替後に FOCUS のチップ（「該当なし」）や `buildHot` が更新されない（M-01 と同じ箇所で直る）。また非表示の用語を GLOSSARY から開くと表示されるが、別のノードへ移ると消える点は仕様どおり（§3.6）で問題なし。 | M-01 の修正で `renderChips()`・`buildHot()` も呼ぶ。 |
| L-07 | 低 | `viewer/app.js` `SHAPES.term`（`CircleGeometry(0.5, 6)`）と `wire.rotation` | EdgesGeometry は同一平面の内部の辺を除くので外周の六角形だけになり正しい。ただ平面の図形に既存の擬似ランダム回転をかけるため、向きによっては線（真横）に見えるノードがある。半径0.5は他の形（約0.95）の半分で、密集した領域では見つけにくい。 | 用語だけ回転をかけずカメラ向きにする（`wire.quaternion.copy(camera.quaternion)` を毎フレーム、または `Sprite`）か、回転を x 軸だけ小さくする。 |
| L-08 | 低 | `tools/figures.py` `confounding`／`feedback_loops` | 共通の矢じり `#ar` が黒なので、赤い矢印の先だけ黒い。均衡ループは4本とも同じ矢印で、どれが負の向きかが図だけでは分からない（注記で補っている）。はみ出し・重なりは無し。 | 赤用の矢じり（`#ar-red`）を追加する。均衡ループの最後の矢印の脇に「−」を置く（因果ループ図の一般的な記法）。 |
| L-09 | 低 | `tools/screenshot_viewer.py` | 撮影対象に用語のIDを直書き（`#trm.ai-ai-agent-ai-36937991`）。M-02 でIDが変わると撮影が黙って「選択なし」になる。NOTES=HIDE の状態の撮影がない。 | 撮影前に graph.json から最初の term を選ぶ。`notes: "off"` の localStorage で1枚追加する（M-01 の確認用）。 |

XSS：GLOSSARY・パネルの FROM YOUR NOTES・INDEX・SETTINGS の追加部分は、データ由来の文字列がすべて `esc()` を通っている。`#ver` の `G.stats.notes` は build 側で数える整数。問題なし。

## 総評
設計書（DOC-02 v1.3／DOC-03 v3.2／DOC-05 v1.1）は先に改訂されており、ビューア側（05 GLOSSARY、08 SETTINGS の NOTES、選択中ノードの常時表示、INDEX から用語を除く、六角形の形、FROM YOUR NOTES）は §3.6 どおりに実装されている。新しい図4点もはみ出しはなく、表示とコンソールにも問題はなかった。

一方で、取り込みの仕組みは「1回だけ動かす移行」としては正しいが、`agents/orchestrator.md` 4b が求める**毎サイクルの再実行**には耐えない。再実行で検証結果が毎回消え（H-01）、題名の書き換えと除外が次回の差分取りと噛み合わない（M-04）。さらにIDも題名に依存している（M-02）。いずれも「題名ではなく `notion_id` を正本のキーにし、既存ノードは更新（upsert）する」に変えれば、まとめて直る。

プライバシー面では、除外を塩なしの題名ハッシュで公開しているため、市町村名のような候補の少ない題名は辞書照合で復元できる（H-02）。公開リポジトリなので、main へマージする前に直すことを勧める。

## 対応（作成者による）
| ID | 対応 |
|---|---|
| H-01 | 移行スクリプトを upsert 方式に書き直した。既存の用語ノードは名前・英語名・定義だけを更新し、定義が変わったときだけ unverified に戻す。verification・置き場所・history・受け皿テーマは保つ。2回目の実行で nodes.json がバイト単位で同じことを確認 |
| H-02 | 除外の指定と記録を notion_id（ランダムなID）のハッシュ＋大まかな分類（privacy など）に変更。題名・詳しい理由は公開ファイルに残さない。過去のコミットに残らないよう、ブランチは1コミットにまとめ直してから main に入れる |
| M-01 | buildLinks を表示中のノードどうしだけに。applyVisibility から buildLinks／buildHot／renderChips を呼ぶ |
| M-02 | 用語のIDを notion_id から作るように変更（DOC-03 §1.1） |
| M-03 | T-11 で出典が空の用語ノードをエラーに。用語集と出典（資料の glossary 属性）の一致も検査 |
| M-04 | Orchestrator 4b の差分は notion_id で取る（取り込み元ファイルと除外ハッシュの両方に無いIDだけが新規） |
| M-05 | 移行スクリプトの出力をIDの昇順に |
| M-06 | 日付は実行日、地図の版は state.json から取る |
| M-07 | 資料に glossary 属性を持たせ、build_viewer_data はそれを使う |
| 低：列の共有 | 時間を持たないノードの x の列を、用語とそれ以外で分けた |
| 低：形 | 平面の六角形をやめ、六角柱にした |
| 低：図の矢印 | 赤い矢印には赤い矢じり。均衡ループの各矢印に ＋／− を付けた |
| 低：撮影ID | graph.json の最初の用語を使う |
| 低：その他 | 「事実」ラベル（未検証のメモ）、半径の一部重なり、題名の整え方は DOC-03 §1.3 に明記して現状維持 |
