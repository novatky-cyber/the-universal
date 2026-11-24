# サイクル 0002 計画（Planner）

## 1. 今回のセッションと判断理由
- セッション：**P01-S02 生命の起源と進化**（教材 L0002）
- 理由：`state.current_session` は P01-S01。DOC-04 §4・§4.1（集中期間：`intensive_until` 2026-12-01）により、回答の有無にかかわらず次のセッションへ進む。
- 回答の状況：第0回・第1回の回答は未着（`awaiting_user`）。理解レベルはすべて L0 のため、DOC-04 §3 の上限は「L2以上が増えていない」場合の **新規ノード20件** を適用する。
- ユーザー由来の open な問い：qq.0017（利己的な遺伝子と進化の単位）は P05-S01 で本格的に扱う。今回は「進化の単位」という問いの存在と、P05-S01 への橋渡しだけを置く（深入りしない）。

## 2. 中心の問い
**生命はどのように始まり、どのようにして多様になったのか。そして「起源」と「進化」は、なぜ別の問題なのか。**

## 3. 扱うノード
- 既存：thm.life、q.origin-of-life、evt.earliest-life、con.natural-selection、evt.goe、evt.cambrian、evt.kpg、evt.earth-formation、evd.radiometric-dating、con.cumulative-culture（次回への橋）、evt.hominin-split（次回への橋）
- 新規候補（上限20、最大で以下から選ぶ）：
  - 概念：生命の定義（con.definition-of-life）、遺伝的浮動（con.genetic-drift）、中立説（thy.neutral-theory）、共通祖先（con.common-descent）、LUCA（con.luca）、細胞内共生（thy.endosymbiosis）、3ドメイン（con.three-domains）、大量絶滅（con.mass-extinction）、進化の単位（q.units-of-selection）
  - 理論：ダーウィンの進化論（thy.darwinian-evolution）、現代的総合（thy.modern-synthesis）、RNAワールド仮説（thy.rna-world）、生命起源の環境仮説（熱水噴出孔／陸上温泉）（con.origin-settings）
  - 出来事：ミラー＝ユーリー実験（evt.miller-urey）、真核生物の出現（evt.eukaryotes）、全球凍結（evt.snowball-earth）、陸上への進出（evt.land-colonization）
  - 証拠：化石記録（evd.fossil-record）、分子系統（evd.molecular-phylogeny）、観察された進化（evd.observed-evolution）

## 4. 訂正候補
- evt.goe：出典未登録。開始年代（約24.3〜24.6億年前）と期間の最新推定を確認。
- evt.kpg：出典は ICS のみ。原因（チクシュルーブ衝突、デカン・トラップの関与）の扱いを確認。
- evt.cambrian：年代 538.8 Ma（ICS 2024）を再確認。
- con.natural-selection、q.origin-of-life：出典未登録。
- evt.earliest-life：約34億年前（Allwood 2006）以外の主張（37億年前 Isua、ヌブアギトゥク等）の最新の評価を確認。
- thm.life の開始時期「約40億年前？」の表記の妥当性。

## 5. 調査の分担（Researcher 3体）
| 担当 | 範囲 | 問い |
|---|---|---|
| R1 origin | 生命の定義、生命起源の研究史と主要仮説、最古の生命の証拠、LUCA、地球外からの材料（隕石・小惑星サンプル） | 起源について何が分かっていて、何が仮説で、何が未知か |
| R2 evolution | ダーウィンとウォレス、自然選択の条件、遺伝の仕組み（DNA）、遺伝的浮動と中立説、現代的総合、共通祖先と生命の木、3ドメイン、細胞内共生、観察された進化 | 進化はどんな仕組みで、どんな証拠で支えられるか |
| R3 history | 地球と生命の共進化：大酸化イベント、全球凍結、真核生物、多細胞化、エディアカラ紀・カンブリア紀、陸上進出、ビッグファイブ大量絶滅、K-Pg、現在の生物多様性の喪失、時事候補 | 生命史の大きな転換点は何で、原因はどこまで分かっているか |

Challenger 1体：異説（拡張された進化的総合、断続平衡、選択の単位、今西進化論、クロポトキン、創造論・ID の位置づけ）、地域の偏り、単一原因への還元。
Verifier 2体：(1) 教材の主張（claims.md）、(2) あなたのメモの用語約10件（notes_check.md）。Editor 1体。合計7体。

## 6. 復習対象
- `next_review` が今日以前のノード：なし（評価が未実施のため）。
- 第1節では第1回の要点（認識の区別、地球の形成年代、放射年代測定）から3〜4問を出す。

## 7. 時事候補（1件）
- 実行時点で R3 が確認する。候補：小惑星ベンヌ試料の分析（2025）、火星ジェゼロ・クレーターの「潜在的な生命の痕跡」（2025）、LUCA の年代推定（2024）、生物多様性に関する最新の国際報告。最も新しく一次資料のあるものを選ぶ。

## 8. 量の見込み
- 新規ノード：最大20、新規エッジ：最大40程度
- 教材：前編・後編の分冊を想定（各16〜24ページ）。網羅を優先。
