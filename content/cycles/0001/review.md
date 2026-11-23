# 独立レビュー結果（dev/p1-p2-prototype）

対象：tools/*.py、index.html、viewer/app.js、viewer/style.css、data/schema/*.schema.json、templates/*
基準：DOC-03 詳細設計書 v1.1、DOC-05 テスト計画 v1.0、agents/dev.md「Reviewer」

実行して確かめたこと：
- `validate.py` OK、`build_viewer_data.py` OK（136ノード）、`check_all.py --skip-pdf` OK
- `render_pdf.py content/cycles/0001 --allow-unverified`（リポジトリ直下から）：OK（前編16p／後編16p／レポート4p）。フラグなしだと T-10 が25件（未確認の出典40/46件のため。ゲートとしては意図どおり）
- `/tmp` の試験スクリプトで、コードブロック内の記法置換、閉じないブロック、見出し判定、CRLF、図の空データを確認

## 指摘一覧

| 重要度 | 場所（ファイル:行） | 内容 | 修正案 |
|---|---|---|---|
| 高 | tools/render_pdf.py:45-65, 67-71, 95-142 | 独自記法がコードブロック内でも置換される。`inline()` が Markdown 変換の前に生テキストへ正規表現をかけるため。試験では、```` ``` ```` 内の `[[node:…]]` がエスケープされた `&lt;span class='nref'&gt;…` というゴミになり、`[[src:nonexist]]` は `[?]` に置換され、**T-09エラーとして数えられた**（誤検出）。出典番号も消費される。`{事実}` はコードブロック内でもインラインコード内でもバッジになる。`:::point` `{{figure:}}` `<!-- pagebreak -->` も、フェンス内かどうかを見ずに行単位で処理される。付録Cの提出用プロンプトがコードブロックなので、今後ここに記法の例を書くと壊れる | 行ループでフェンス（```` ``` ```` / `~~~`）の開閉を追い、フェンス内は `buf` に入れるだけにして記法処理を飛ばす。インラインは markdown-it のトークン（`text` トークンだけ）に置換をかけるか、置換の前に `` `…` `` を退避する |
| 高 | tools/render_pdf.py:83-93, 131-142 | T-10（実在未確認の出典を教材に使っていない）の検査が `sources_html()` の中にあり、原稿に `{{sources}}` 行がなければ実行されない。そのため、付録Bを書き忘れると T-10 を素通りする。しかも `{{sources}}` は DOC-03 §2.3 の記法表に載っていない | T-10 は `render_body` の後に `self.cited` を対象に必ず実行する。`{{sources}}` を DOC-03 §2.3 に追記し、教材で `{{sources}}` がなければエラーにする |
| 高 | viewer/app.js:175, 210-211, 254, 267-278 | `treeGroup.clear()` / `edgeGroup.clear()` は子を外すだけで、`BufferGeometry` と `LineBasicMaterial` を dispose しない。ノードをタップするたび、モードを切り替えるたびに GPU メモリが増え続ける。iPhone Safari は WebGL のメモリ上限が厳しく、長く使うとコンテキストを失う（画面が黒くなる）おそれがある | `function disposeGroup(g){ g.children.forEach(o=>{o.geometry?.dispose(); o.material?.dispose();}); g.clear(); }` に置き換える。エッジのマテリアルは種類ごとに1個を共有する |
| 中 | viewer/app.js:204-209, 286-291 | モード切替の補間とカメラの飛行が、同じ変数 `tween` を共有している。切替アニメーション中（1秒）に検索結果やリンクから `select(id,true)` を呼ぶと補間が上書きされ、ノードが途中の位置で止まる。木の線とエッジも再生成されないまま残る（逆の順でも、飛行が途中で切れる） | `tweens` を配列（またはモード用・カメラ用の2本）にして並行に進める。もしくは補間中は `flyTo` を補間の完了後に回す |
| 中 | viewer/app.js:42-51, 411-417 | `PORTRAIT` を読み込み時に1回だけ判定している。iPhone を回転させても `camera.up` と時間軸の向きが変わらない（DOC-03 §3.4「縦長では縦、横長では横」に反する）。凡例（index.html:41「左が過去」）も縦長の表示と食い違う | resize（または `matchMedia('(orientation: portrait)')` の change）で判定し直し、`camera.up` を変えて `controls` を作り直す（または `controls.object.up` を変えたあと `controls.update()`）。凡例の文言は向きに応じて切り替える |
| 中 | index.html:10-15, 55 | importmap は iOS Safari 16.4 以上でしか使えない。それより古い端末ではモジュールが読み込まれず、例外も出ないまま「地図を読み込み中…」が永遠に表示される。CDN に届かない場合も同じ | `es-module-shims` を読み込むか、`<script nomodule>` と数秒のタイムアウトで「このブラウザは未対応です／通信を確認してください」と表示する。CDN にはバージョン固定に加えて integrity（SRI）を検討する |
| 中 | viewer/app.js:226-233 | タップの判定が単一ポインタ前提。2本指のピンチでは2本目の `pointerdown` が `down` を上書きし、指を離したときに動きが8px以下だと誤って選択される。さらに `Raycaster` は `visible` を見ないため、領域フィルタで隠したノード（:353）もタップで選択できてしまう | `pointerId` ごとに管理し、同時に押された数が1のときだけタップと判定する。`intersectObjects(meshes.filter(m=>m.visible))` にする |
| 中 | viewer/app.js:304, 309 | 出典URL（`s.url`）とPDFパス（`f`）は `esc()` されているが、スキームを検査していない。`javascript:` で始まるURLがデータに入るとXSSになる。sources.json はエージェントがWebから集めて書くデータなので、混入の経路はありうる | source.schema.json の `url` に `"pattern": "^https?://"` を追加する。ビューア側も `/^https?:\/\//.test(url)` の場合だけ `<a>` にする |
| 中 | tools/validate.py:52（cat上130） | T-04 の判定が `sources` 空かつ `status == "verified"` だけをエラーにしている。DOC-03 §1.3・DOC-05 T-04 は「sources が空なら unverified」なので、空の出典で `pending` のノードが通ってしまう | `if not n["sources"] and n["verification"]["status"] != "unverified":` にする |
| 中 | tools/map_diff.py:18-25, 40-44 | (1) 存在しない参照や打ち間違い（例：`HEAD~1` の時点で nodes.json がない、タグ名の誤記）を `CalledProcessError` で握りつぶして `[]` を返すため、「全件追加」という誤った差分を黙って出す。(2) DOC-03 §5 の「既定は直前の `map-vX.Y` タグ」と「JSONとMarkdownの両方を出力」が実装されていない（ref は必須引数、Markdown出力なし） | `git rev-parse --verify` で参照の存在を確かめ、なければエラーで終了する（ファイルがない場合だけ空扱いにする）。`git describe --tags --match 'map-v*' --abbrev=0` を既定値にする。`--md` 出力を追加する |
| 中 | tools/render_pdf.py:217-219 | 相対パスを CWD ではなく ROOT 基準で解決している。`cd tools && python3 render_pdf.py ../content/cycles/0001` は `/the-universal/../content/...` になり、「lesson.md または lesson_a.md がない」という誤解を招くエラーで失敗する（実際に再現した。レポートも生成されない） | `d = Path(a.cycle_dir).resolve()` を使い、CWD 基準で失敗したら ROOT 基準を試す。ディレクトリがなければ「ディレクトリがない」と明示する |
| 中 | tools/render_pdf.py:146-147 | 見出しの判定 `^## (\S+?)[.．\s]` が (a) フェンス内の `## 14.` も見出しとして数える（必須欠落の見落とし）、(b) `## 付録A（解答・解説）` のように空白なしで括弧が続くと「付録A（解答・解説）」として取り込み、欠落と誤判定する | フェンスを除外したうえで `^##\s+(\d+|付録[A-Z])` に一致させる |
| 中 | viewer/style.css:65-66（cat上122-123）, 70（127） | `.lbl` `.tick` の `transform: translateY(...)` は、CSS2DRenderer が毎フレーム `element.style.transform` をインラインで上書きするため効かない。ラベルがノードの中心に重なる。一方、重なり判定（app.js:384 の `-14`）はずれた位置を前提にしていて、両者が一致していない | `CSS2DObject.center.set(0.5, 1.6)` などで位置をずらすか、`margin-top` やラベル内の子要素側で transform を使う。app.js:384 の前提も合わせる |
| 中 | tools/render_pdf.py:161-163 / templates/print.css | フッターに「生成日」がない（DOC-03 §4.1「ページ番号／総ページ数、生成日」）。代わりに「The Universal」と表示している | フッター左を `生成 {date}` にする（`<span class='date'>` または fm.date） |
| 中 | tools/render_pdf.py:63-64 | 書式の崩れた参照（`[[src: x]]`、`[[node:Con.X]]`、`[[nod:…]]` など）は正規表現に一致しないため、生のテキストのままPDFに残る。エラーにもならないので、T-09「未解決0」を素通りする | 置換後に `\[\[(src|node)[^\]]*\]\]` や `\[\[` が残っていればエラーにする |
| 低 | tools/render_pdf.py:30 | frontmatter の正規表現が `\n` 固定で、CRLF の原稿や本文のない原稿は「frontmatter がありません」になる（試験で再現） | 読み込み時に `text.replace("\r\n","\n")` を行い、本文部分を `(.*)` から省略可にする |
| 低 | tools/render_pdf.py:190, 200 | frontmatter の必須キー（lesson_id、session、title、map_version、report_id、date）を検査しておらず、欠けると KeyError のトレースバックで落ちる。`volume` とファイル名（lesson_a/b）の一致も見ていない | 種類ごとの必須キーを検査して、ERROR 行で報告する |
| 低 | tools/render_pdf.py:201 | PDF生成（Playwright）の例外を捕まえていない。1冊が失敗すると以降の冊が処理されない（デバッグ用HTMLは先に保存されるので、DOC-03 §6 は満たしている） | try/except で errors に積み、次の冊へ進む |
| 低 | tools/render_pdf.py:196-208 | 24ページ超で T-08 エラーになっても、PDF は output/lessons に残る | エラー時は PDF を削除するか、debug へ移す |
| 低 | tools/render_pdf.py:194-196 / DOC-03 §4.4 | 分冊のファイル名が `L0001a_P01-S01.pdf` になる。設計書の「末尾に a / b」は `L0001_P01-S01a.pdf` とも読める。output/debug に古い `L0001_P01-S01.html` も残っている | 設計書に例（`L0001a_P01-S01.pdf`）を明記する |
| 低 | tools/figures.py:90-91（cat上340-341） | `cosmic_timeline` は、対象の出来事が0件だと `slot=(R-L)/n` で ZeroDivisionError になる（試験で再現） | `if not evs: return "<svg …>（データなし）</svg>"` |
| 低 | tools/figures.py:12-14, 57 | `_xmap` の引数 x0,x1 が使われていない（読みにくい）。30年後より先の未来や138億年より前の時刻は、軸の外（右側の「時間なし」枠の中）に描かれる（例：1000年後 → x=553） | 引数を整理し、x を [L,R] に clamp する |
| 低 | tools/build_viewer_data.py:42, 59 | validate を通さずに単独で実行すると、未登録の出典は KeyError になる。また、NaN を検出しても graph.json を `allow_nan=True` で書き出すため、ブラウザで読めない JSON が残る | `src.get(s)` で欠落をエラーとして数える。`json.dumps(..., allow_nan=False)` にし、エラー時は書き出さない |
| 低 | tools/validate.py | 未検査の項目：domains の ID 重複と `order` が 0〜9 で一意であること（座標の角度に直結する。ビューア app.js:136 は `order` ではなく配列の添字を使っており、並びが変わると Python 側と食い違う）、forecasts の ID 重複と nodes 参照、parent と子の level の大小、part_of エッジと parent の重複（DOC-03 §1.4）。JSON の構文エラーはトレースバックで落ちる | 該当する検査を追加する。ビューアは `d.order` を使う |
| 低 | tools/validate.py:97-99（cat上175-177） | 何もしないループ（`pass`）が残っている | 削除する |
| 低 | viewer/app.js:107 | `decodeURIComponent` が不正な `%` を含むハッシュで URIError を投げ、init 全体が失敗して「読み込みに失敗しました」になる。hashchange にも対応していない | try/catch で包む。`hashchange` で `select` する |
| 低 | viewer/app.js:89-92 | `r.ok` を確かめずに `r.json()` しているため、404 のときのエラーメッセージが分かりにくい | `if(!r.ok) throw new Error(r.status)` |
| 低 | viewer/app.js:185, 239, 298 | `posOf` は `meshes.find` の線形探索なので、buildTree は O(N²)、select は O(N·E)。今は136ノードで問題ないが、地図が数千ノードに育つと iPhone で重くなる | `meshById` の Map と、ノードごとの隣接リストを init で作る |
| 低 | viewer/app.js:402-409 | 静止中も毎フレーム描画し続けるため、iPhone のバッテリーを消費する | controls の `change` と補間中だけ描画する（render on demand） |
| 低 | viewer/app.js:158-159 | 全マテリアルが常に `transparent:true` なので、半透明の並べ替えのコストがかかり、深度の不具合も起きうる | 選択の濃淡を付けるときだけ transparent を切り替える |
| 低 | viewer/app.js:323 | `body` は設計上 Markdown（DOC-03 §1.3）だが、エスケープした1段落として表示され、改行も失われる | 当面は `white-space: pre-wrap`。将来は安全な Markdown 変換を使う |
| 低 | viewer/style.css:21-22, 40-42（cat上78-79, 97-99） | `backdrop-filter` に `-webkit-` 接頭辞がなく、iOS Safari 17 以前ではぼかしが効かない | `-webkit-backdrop-filter` を併記する |
| 低 | index.html:5 | `maximum-scale=1` でアクセシビリティ上の拡大が制限される（iOS は無視するが） | 削除を検討する |
| 低 | tools/screenshot_viewer.py:50-51（cat上151-152） | ループ内のラムダが `name` を遅延束縛するため、遅れて届くコンソールエラーに別の撮影名が付くことがある | `lambda m, name=name: ...` |
| 低 | 保守性全般 | 対数変換 `xOfYa`、目盛り（TICKS）、理解レベルの色が Python（common.py / figures.py）と JS（app.js）に二重定義されている。figures.py の L0 色（#9ca3af）は設計値（#6b7280）と異なる（印刷用の意図なら注記が必要） | 定数を graph.json に含めて JS 側で使う。または両方に「DOC-03 §3 と同期」とコメントする |
| 低 | プライバシー | graph.json には理解レベル（understanding）と、ユーザーが出した問い（questions、origin=user）がそのまま入る。GitHub Pages で公開すると、学習状況と本人の問いが一般に見える。外部送信は CDN（jsdelivr）へのアクセスだけで、回答の原文は含まれないことを確認した | 公開範囲を README/ADR に明記する。必要なら origin=user の問いを公開用データから除く |

### 問題なしと確認した点
- viewOffset と raycast は整合している。`setViewOffset` は projectionMatrix に反映され、`Raycaster.setFromCamera`、`Vector3.project`、CSS2DRenderer がいずれも同じ行列を使うため、全画面座標の NDC で正しく当たる。描画の中心は上へずれる（意図どおり）
- 座標計算（K=10、角度のずらし ±0.35 セクタ、半径 6/10/14 ±1、展開の z ±2.5、時間のないノードは −95〜−5）は DOC-03 §3.1〜3.3 と一致する。意味的ズームの距離閾値（190/95/45）、最大70件、優先度の順も §3.4 と一致する
- innerHTML に入る graph.json の文字列（タイトル、要約、注記、ラベル、出典名）はすべて `esc()` を通っている。ID は schema の pattern で英小文字・数字・ハイフンに制限され、属性への埋め込みも安全（URL のスキームだけが未対策。上記）
- `[[node:ID|表示名]]` の `|` は、Markdown 変換の前に置換されるため、表のセルを壊さない

## 総評
データ検証・座標計算・ビューアの基本構成は設計書とよく一致しており、XSS 対策も概ね行き届いている。
一方、原稿処理がコードブロックを区別しないこと、T-10 が `{{sources}}` の有無に依存して素通りしうること、ビューアのジオメトリが解放されないことの3点は、P3 に進む前に直すべきである。
iPhone での使い勝手（回転、マルチタッチ、importmap の非対応端末、補間の競合）と map_diff の黙った失敗も、次の版で併せて対処したい。

---
## 対応記録（Implementer）
- 高1 独自記法のコードブロック内置換：フェンス・インラインコード・<pre>/<code> の外側だけを処理するよう修正
- 高2 T-10 の検査位置：`{{sources}}` の有無に関係なく、教材の出典参照すべてを検査するよう修正
- 高3 線のジオメトリ解放：`clearGroup()` で dispose してから外すよう修正
- 中：tween の分離（modeTween / camTween）、画面の向きの変化でコントロールを作り直す、importmap 非対応時の案内、ピンチ後の誤選択防止と非表示ノードの除外、URL のスキーム検査（schema と表示側の両方）、T-04 の判定、map_diff の参照エラー・既定参照・Markdown出力、相対パスの解決、見出し判定、ラベル位置（CSS2DObject.center）、フッターの発行日、書式の誤った参照の検出
- 低：CRLF の正規化、NaN 時に graph.json を書き出さない、-webkit-backdrop-filter
- 未対応（次版で検討）：O(N²) の探索（現規模では問題なし）、graph.json に理解レベルと問いが含まれる点（要件どおり要約のみ公開）
