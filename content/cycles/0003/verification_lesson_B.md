# L0003 教材本文の検証（グループB担当範囲）

- 検証日：2026-11-25
- 検証者：Verifier（独立検証。research/ は参照していない）
- 対象：`lesson_a.md` の 4.2（パラントロプス・料理仮説の言及）、4.5〜4.7、5.1 の該当行、冒頭の第3節と図の該当部分。`lesson_b.md` の 5.3、6.2（X に関わる論争を含む）、7（言語・ネアンデルタール人の行）、8（交易網・選択の単位・脳と認知）、11（該当用語）、13-4、付録A（9-1(3)、12-3、13-4）。
- 照合の基準：`claims/claims_B.md`、`verification_B.md`（前回の判定）、`data/sources.json` の該当エントリ。claims_B にない記述は、WebFetch／WebSearch で照合した（今回は検索が使えた）。

## 確認の結果（要約）

1. **修正要とした主張（C10, C19, C25, C30, C34, C39, C40, C41）は、本文で修正案どおりに直っている。**
   - C10：剥片は意図せず生じる、意図的な打ち欠きは未確認。[[src:mercader2002]] に依拠。
   - C19：可視性の別解釈を示し、「無視して退けるのは公正でない」と書いている。Zink & Lieberman は入っていない。
   - C25：「石材」と書いている。
   - C30：スペインとの比較は本文にない。
   - C34：「White を筆頭とする計44人」と書いている。
   - C39：2015年と書いている。
   - C40：骨器は約8000年前から減り、約3500年前に消えたとしている。魚食は扱っていない。
   - C41：「10の島」とし、接触の効果は書いていない。
2. **根拠不足とした【未確認】部分は本文に入っていない。** 確認した項目：
   - C16：層による差、寒冷期の主張
   - C29：レアン・テドンゲ
   - C38：批判
   - C39：邦訳
   - C53：公平性の批判
   - C56：北西海岸の例
   - C57：リンポポの具体的な記述（規範の部分だけを使っている）
3. 下の表の指摘は、ラベルの脱落、claims_B にない評価、出典IDのずれ。重大な事実誤りは見つからなかった。

| 場所（節） | 本文の該当箇所 | 問題 | 修正案 | 根拠URL |
|---|---|---|---|---|
| lesson_a 4.5 要点 | 「常用は約30万〜40万年前から、火おこしの最古の証拠は約40万年前です。」 | (4) ラベルの脱落。本文では「常用」を {論争}（Roebroeks & Villa の主張、C15）としているのに、要点では事実として断定している。 | 「常用は約30万〜40万年前からとする見方が有力（論争あり）」とする。 | https://ui.adsabs.harvard.edu/abs/2011PNAS..108.5209R |
| lesson_a 第3節（2.）、4.7 要点、4.7 まとめ | 「改良が積み重なる『累積的文化』の程度と速さ、と見る研究者が多い」「多くの研究者は、人間の文化の特徴を…『累積的文化』に見ます」「…と見る研究者が多い」 | (3) claims_B にない評価。「研究者が多い」という分布を支える出典がない。claims_B では「累積の程度と速度が桁違い」は本教材の整理（C46 補足）で、4.7 の本文もそう書いている。要点・まとめだけが研究者の多数意見として書いている。 | 「…と見る研究がある（トマセロら）。程度と速さの違いと整理すると、両方の証拠に合いやすい（本教材の整理）」とする。多数派だと書くなら、総説などの出典を加える。 | https://research-portal.st-andrews.ac.uk/en/publications/ratcheting-up-the-ratchet-on-the-evolution-of-cumulative-culture/ ／ https://www.news.uzh.ch/en/articles/media/2024/chimpanzee-culture.html |
| lesson_a 4.5「火おこし」 | 「作り手は初期のネアンデルタール人と推定されている[[src:ashton2025]]」 | (2)(3) 軽微。claims_B（C17）は「人骨は出ておらず、スワンズクーム頭骨などからの推定にとどまる」「黄鉄鉱が人に持ち込まれたことは推論」と限界を書いているが、本文はその限界を落としている。 | 「バーナムからは人骨が出ておらず、作り手は同時代の頭骨などから初期のネアンデルタール人と推定されているにとどまる」とする。 | https://www.nhm.ac.uk/discover/news/2025/december/earliest-fire-making-dating-back-400-000-years-unearthed-in-suffolk-england.html |
| lesson_b 6.2「ネアンデルタール人をどう描くか」 | 「White を筆頭とする計44人が…反論し[[src:white2020]]」 | (4) 出典IDのずれ。src.white2020 の URL（USF の書誌ページ）には著者3人（White, Bosinski, Bourrillon）しか載っておらず、「計44人」を支えるのは src.sciencenews-iberian2019（既存エントリ）。 | 「計44人」の直後に [[src:sciencenews-iberian2019]] を加える（white2020 は論点の出典として残す）。 | https://sciencenews.org/article/dating-questions-challenge-whether-neandertals-drew-spanish-cave-art ／ https://digitalcommons.usf.edu/kip_articles/5193 |
| lesson_b 7（未解明の表）「言語はいつ・どう生まれたか」 | 「約5万年前説から約100万年前説まで。FOXP2 は『言語遺伝子』ではない[[src:hauser2014]] {未知}」 | (4) 出典が中身に合わない。hauser2014 は「未解明である」ことの出典で、時期の幅（約5万年前：クライン、約100万年前：Dediu & Levinson）や FOXP2 の評価（Atkinson 2018）を述べていない。 | 「約5万年前説[[src:klein-stanford2002]]から約100万年前説[[src:dediu-levinson2013]]まで。FOXP2 は『言語遺伝子』ではない[[src:atkinson2018]]。基本的な問いは未解明[[src:hauser2014]] {未知}」とする。 | https://stanfordmag.org/contents/suddenly-smarter ／ https://www.mpg.de/7448453/Neandertals-language ／ https://escholarship.org/uc/item/45v626k8 ／ https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00401/full |
| lesson_b 8「選択の単位」 | 「集団間の競争による『文化的群淘汰』を重視する説があります。」 | (4) 出典もラベルもない。claims_B では C54 の補足（出典なし）にあたる。 | 出典として [[src:boyd-richerson1985]]（第7章「頻度依存バイアスと協力の進化」で文化的群淘汰を扱う。目次で確認）を付け、{理論} を付ける。 | https://chicagoreference.com/ucp/books/book/chicago/C/bo5970597.html |
| lesson_b 8「脳と認知」 | 「その学ぶ力自体が生まれつきか、文化的に学ばれた『認知の道具』かは論争中です[[src:clarke-heyes2017]]」 | (3) 軽微。出典の要旨は「文化的学習の仕組みは、文化進化の過程であると同時に産物でもある」とする。「認知の道具（cognitive gadgets）」は Heyes の別の著作（2018）の用語で、この出典にはない。「生まれつきか、学ばれたか」の二択にするのも、要旨より強い。 | 「その学ぶ仕組み自体も文化進化の産物である、とする批判がある[[src:clarke-heyes2017]] {論争}」とする。 | https://eprints.whiterose.ac.uk/id/eprint/112738/ |
| lesson_b 6.2「第三の立場」 | 「東アフリカの石器を調べると技術の選び方は大きく変動しており」 | (3) 軽微。要旨は「東アフリカの中期更新世後半の遺跡のデータ」で、行動の変動性が5万年前以降の集団と大差ないとする。中身は石器技術の分析と考えられるが、要旨では「石器」と明記していない。内容の向きは合っている。 | 「東アフリカの遺跡のデータでは、最古のサピエンスの行動の変動性は5万年前以降の集団と大きく違わず」とすると、要旨に忠実になる（任意）。 | https://researchconnect.stonybrook.edu/en/publications/homo-sapiens-is-as-homo-sapiens-was-behavioral-variability-versus/ |
| lesson_a・lesson_b 全体（出典の種類） | [[src:plummer2023]]、[[src:adler2014]]、[[src:garland2011]]、[[src:herrmann2007]]、[[src:evershed2022]]、[[src:braun2025]]、[[src:delatorre2025]]、[[src:berna2012]]、[[src:ashton2025]]、[[src:oktaviana2024]]、[[src:oktaviana2026]]、[[src:marin-monfort2026]]、[[src:vanleeuwen2024]] など | (4) 系統的。教材の根拠の多くが、大学の発表や ScienceDaily の報道（sources.json でも「報道」「プレスリリース」と表記）。内容は一致していたが、品質基準 §3-7（原典で照合）の観点では一次論文の DOI の併記が望ましい。 | 次回以降、sources.json の該当エントリの note か title に、一次論文の DOI を併記する（claims_B に DOI が書いてあるものは転記するだけで済む）。 | ― |

## 問題なしと確認した主な箇所（抜粋）

- lesson_a 4.5：ロメクウィ3と批判、オマキザル、チンパンジー（C10 の修正どおり）、BD 1、ニャヤンガ、ナモロトゥクナン、コキセレイ4、オルドヴァイの骨器27点（地点名を書かず、修正案どおり）、ノル・ゲギ、ワンダーワーク（2012・2026）、ゲシェル・ベノット・ヤーコブ（「少なくとも3種の食用植物」は修正案どおり）、ルボルックス＆ヴィラ、バーナム、料理仮説。
- lesson_a 4.6：Hauser らの立場の書き方は、前回の修正案（不連続性を重く見る立場）どおり。Dediu & Levinson、FOXP2（Atkinson、Krause）、ケバラの舌骨、オロルゲサイリエ（「石材」）、ビズムーン、ブロンボス、スラウェシ（2024・2026）、ショーヴェ。
- lesson_a 4.7：ホワイトゥンら、ザトウクジラ（「隣り合う集団のあいだ」）、ラチェット効果、ファン・レーウェンら、グナセカラムら、ヘンリック（2004。年代は修正案どおり）、クラインとボイド（10の島）、ヴェーセンら（本文の技能の列挙は原論文と一致）、二重継承理論、ヘンリック（2015）、ラクターゼ持続（ティシュコフら、エバーシェッドら）。
- lesson_b 6.2：クライン、マクブレアティとブルックス、ヴィラとルボルックス（要旨の「優越という前提に合わせてシナリオを組み立てた」と一致）、ホフマンら（2018・2020）、シンとグロワッキ（北西海岸の例はない）、「生きた化石ではない」（{規範}、出典なし。C57 の規範部分のみ）。
- lesson_b 8：トマセロらの相互依存仮説、ピンカー（「群淘汰の概念は混乱」「税・政府・軍隊などの普通の原因」は Edge の原文と一致）、ハーマンら（「類人猿（2種の合計）約33%」は修正案どおり）。
- lesson_b 13-4・付録A：FOXP2 の選択肢と解説、9-1(3) の乳の利用の年代、12-3 の採点観点は、claims_B と整合している。

## 件数

| 区分 | 件数 |
|---|---|
| 指摘（表の行） | 9（うち軽微・任意 3） |
| (1) 修正要の主張が修正案どおりでない | 0 |
| (2) 根拠不足・未確認の内容の混入 | 0（バーナムの限界の脱落を、(2)(3) の軽微な指摘として1件計上） |
| (3) claims_B にない評価・記述 | 3（研究者の多数意見、Clarke & Heyes の言い換え、Shea の言い換え） |
| (4) ラベル・出典IDのずれ | 5（要点のラベル脱落、white2020、言語の行の出典、文化的群淘汰の出典、報道依存（系統的）） |

## 確認した資料（今回あらたに開いたもの）

- https://researchconnect.stonybrook.edu/en/publications/homo-sapiens-is-as-homo-sapiens-was-behavioral-variability-versus/ （Shea 2011 の要旨）
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4005592 （Villa & Roebroeks 2014。ブラウザ確認画面のため要旨の一部のみ）／ https://ui.adsabs.harvard.edu/abs/2014PLoSO...996424V
- https://www.edge.org/node/21475 （Pinker 2012）
- https://eprints.whiterose.ac.uk/id/eprint/112738/ （Clarke & Heyes 2017 の要旨）
