# サイクル 0002 独立検証 第2回（担当 V2）

- 検証者：Verifier（主張の作成に関与していない独立のサブエージェント）
- 検証日：2026-11-24
- 対象：`content/cycles/0002/claims_round2.md` の「担当 V2」の表（D09r〜N16）。表には17行あり、依頼文の「16件」より1件多い。17件すべてを判定した。
- 手順：`agents/verifier.md` に従う。research/ 以下は読んでいない。URL が「既出」のものは、第1回（verification_2.md）で確認した claims.md の出典を見直した。

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| D09r | 確認済み | 科学博物館のブログによれば、Cobb と Comfort（2023, Nature）は、未発表の記事の草稿や1953年の王立協会の展示などの新しい資料をもとに、フランクリンを「不当に扱われたヒロイン」ではなく「対等な貢献者」と位置づけた。ラベル「理論」（解釈）は妥当。 | （任意）ブログが挙げる新資料は主に「未発表の記事の草稿」と「展示」なので、「新たに見つかった草稿や書簡など」と書くと出典に近くなる。 | https://blog.sciencemuseum.org.uk/rosalind-franklins-role-revealed-on-the-70th-anniversary-of-the-dna-double-helix-breakthrough/ |
| D19r | 確認済み | Jensen, Payseur, Stephan, Aquadro, Lynch, D. Charlesworth, B. Charlesworth "The importance of the Neutral Theory in 1968 and 50 years on: A response to Kern and Hahn 2018"（Evolution 73(1):111–114。2018年11月27日オンライン公開、2019年1月号）。著者らは Kern と Hahn の議論を「批判的に検討し、退ける」と書いている。Kern と Hahn（2018）自身が、中立モデルを帰無仮説として使うほかない場合が多いと認めていることは、第1回で確認済み。 | （任意）オンライン公開は2018年なので、「2019」は掲載号の年として書く。 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6496948 ; https://hahnlab.sitehost.iu.edu/Publications/KernHahn2018.pdf |
| E01r | 確認済み | PubMed 2112744 の題名は "Towards a natural system of organisms: proposal for the domains Archaea, Bacteria, and Eucarya"（Woese, Kandler, Wheelis, PNAS 87:4576, 1990）。題名に3つのドメインの提案が明示されている。PubMed と PMC の本文ページはボット確認の画面で読めず、書誌は検索結果の題名と WorldCat で確認した。 | — | https://pubmed.ncbi.nlm.nih.gov/2112744/ ; https://search.worldcat.org/oclc/678728346 |
| E06r | 確認済み | OpenStax Concepts of Biology 13.2 に、細胞内共生説は "is now widely accepted" とある。 | — | https://openstax.org/books/concepts-biology/pages/13-2-eukaryotic-origins |
| E08r | 確認済み | シカゴ大学の当時の記事に、約3億7500万年前とあり、Daeschler が「適した時代と古環境」の地層としてエルズミーア島を選んだと語っている。 | — | https://chronicle.uchicago.edu/060413/fossils.shtml |
| E09r | 確認済み | Blount, Borland, Lenski（2008, PNAS 105(23)）：集団 Ara-3 でクエン酸を利用できる変異体（Cit+）が現れたのは3万1000〜3万1500世代の間。酸素のある条件でクエン酸を使えないことが大腸菌を定義する特徴の一つだった、と明記されている。MSU Today（2025年11月）：2022年にテキサス大学オースティン校へ移り、8万2000世代まで続いている。 | （任意）pnas.org のリンクは取得の許可がタイムアウトしたため、PMC 版で確認した。出典の URL を PMC 版にするか併記する。公開直前に世代数を再確認する。 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2430337 ; https://msutoday.msu.edu/news/2025/11/evolution-under-a-microscope-going-strong-at-msu （取得できなかったもの：https://www.pnas.org/doi/10.1073/pnas.0803151105） |
| G02r | 確認済み | Hunt, Hopkins, Lidgard（2015, PNAS 112(16):4885–4890）：最も支持されたモデルの約38%が停滞で、"stasis is common in the fossil record" と述べている。環境の追跡モデルで停滞のパターンを再現できると示しつつ、それを「普遍的な説明とはみなさない」とし、メタ個体群の構造や生息地の追跡なども重要だと認めている。停滞の説明に議論が残っていることを裏づける。 | — | https://pmc.ncbi.nlm.nih.gov/articles/PMC4413263 |
| G04r | 根拠不足 | 後半（1985年、英国の古生物学者 Halstead が Nature の "Anti-darwinian theory in Japan" で、今西の著作が日本で人気があることを論じた）は出典で確認した。前半（今西が京都大学で、川の昆虫、とくにカゲロウの幼虫の棲み分けの観察から出発し、のちに独自の進化論を唱えた）は、src.halstead1985 の取得できた範囲では裏づけられない。ほかに確認できたのは、今西の学位論文が日本の渓流のカゲロウ類に関するものだという二次情報（Wikipedia、CiNii の記録を引用）だけ。CiNii の記録そのものは取得できなかった。 | 前半の出典として、今西の『生物の世界』（1941）や京都大学・学会による今西の伝記的資料など、カゲロウの幼虫の棲み分け研究を直接述べる資料を加える。用意できないなら、前半を「今西錦司は棲み分けの概念を提唱し、のちに自然選択を中心に置かない独自の進化論を唱えた」とし、「カゲロウの幼虫」「京都大学」の具体的な記述は出典を確認できるまで外す。 | https://www.nature.com/articles/317587a0.pdf ; https://en.wikipedia.org/wiki/Kinji_Imanishi （参考。根拠としては使わない） |
| G07r | 確認済み | Britannica "Lamarckism – Persistence of Lamarckism"：1948年のレーニン農業科学アカデミーの会合でラマルク説が公式の路線になり、メンデル遺伝学は退けられ、ルイセンコがソ連生物学の独裁者になった、とある。 | — | https://www.britannica.com/science/Lamarckism/Persistence-of-Lamarckism |
| G09r | 確認済み | 判決文（M.D. Pa., 2005年12月20日）に "ID is a religious view, a mere re-labeling of creationism, and not a scientific theory" とある。 | — | https://www.pamd.uscourts.gov/sites/pamd/files/kitzmiller_342.pdf |
| N10 | 確認済み | ASU Embryo Project：メンデルは "a monk in the Augustian St Thomas's Abbey in Brünn, Austria, now Brno, Czech Republic" で実験した。論文は19世紀の大部分のあいだほとんど注目されなかった。 | （任意）1866年の時点ではオーストリア帝国で、翌1867年からオーストリア＝ハンガリー帝国になる。「オーストリア帝国」の表記で正しい。 | https://embryo.asu.edu/pages/experiments-plant-hybridization-1866-johann-gregor-mendel |
| N11 | 確認済み | 総研大の太田朋子氏インタビューに、太田氏が国立遺伝学研究所の木村のグループに加わった直後の1968年に木村が中立説を提唱した、とある。 | — | https://ir.soken.ac.jp/record/5154/files/%E5%A4%AA%E7%94%B0%E6%9C%8B%E5%AD%90%E6%B0%8F%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%93%E3%83%A5%E3%83%BC.pdf |
| N12 | 確認済み | Darwin Online の挿図一覧："The Origin of species only had a single illustration"。William West のリトグラフの図で、共通の祖先からの由来によって変種や種の類似の程度を説明している。 | （任意）この一枚だけというのは英語の原書の各版の話。のちの翻訳版（1872年のデンマーク語版など）や没後の版には図が加えられたものもある。 | https://darwin-online.org.uk/graphics/Origin_Illustrations.html |
| N13 | 確認済み | 書店 honto の書誌：太田朋子『分子進化のほぼ中立説 偶然と淘汰の進化モデル』、講談社（ブルーバックス）、紙の本は2009年5月刊、ISBN 978-4-06-257637-6。講談社の書籍ページと国立国会図書館の書誌は検索で見つけられなかった。検索で出た講談社と NDL のページは別の本（『新しい分子進化学入門』、木村『分子進化の中立説』）だった。 | 書名にサブタイトル「偶然と淘汰の進化モデル」を加える。可能なら、公開前に NDL サーチか講談社のサイトで ISBN 9784062576376 を照合する。 | https://honto.jp/ebook/pd_26459526.html |
| N14 | 確認済み | 紀伊國屋書店：リチャード・ドーキンス『利己的な遺伝子 40周年記念版』、訳者は日高敏隆・岸由二・羽田節子・垂水雄二、紀伊國屋書店、2018年2月、ISBN 9784314011532。 | — | https://www.kinokuniya.co.jp/f/dsg-08-EK-0517150 |
| N15 | 確認済み | 全米科学アカデミー（NAS）の2008年1月3日の発表：『Science, Evolution, and Creationism』は NAS と米国医学研究所の共同刊行で、1984年版と1999年版に続く第3版。 | （任意）NAS は「book」と呼んでいる。「冊子」より「小冊子の本（第3版）」「報告書」と書くほうが正確。 | https://www.nationalacademies.org/news/2008/01/scientific-evidence-supporting-evolution-continues-to-grow-nonscientific-approaches-do-not-belong-in-science-classrooms |
| N16 | 確認済み | 挙げられた出典（Britannica の social Darwinism の項）は、事実と規範の区別そのものを論じていない。そこで Verifier が出典を示す。Internet Encyclopedia of Philosophy の "Evolutionary Ethics"（Doris Schroeder, Lancaster University）は、経験的な事実から規範を導けないと最初に一貫して論じたのはヒュームだとし、スペンサー（とダーウィン）が「である」から「べき」を導いている点を批判の中心に置いている。ムーアの自然主義的誤謬にも触れている。 | 出典を IEP "Evolutionary Ethics" に差し替えるか、併記する。（任意）ラベル「理論」は許容できる。ただし、メタ倫理学には「である」から「べき」を導けるとする異論（Searle 1964 など）もあるので、「哲学で広く受け入れられている原則」と書くとより正確になる。 | https://iep.utm.edu/evol-eth/ |

## 集計

| 判定 | 件数 | 主張ID |
|---|---|---|
| 確認済み | 16 | 上記以外のすべて |
| 修正要 | 0 | — |
| 根拠不足 | 1 | G04r |
| 出典不在 | 0 | — |
| 合計 | 17 | （表の行数。依頼文の「16件」より1件多い） |

## 系統的な問題

1. **出典の差し替えが必要なもの**：N16（Britannica → IEP）、E09r（pnas.org → PMC 版）、N13（書店の書誌 → 版元か NDL の書誌が望ましい）。
2. **人物の経歴の記述に一次・準一次の出典がない**：G04r の前半（今西とカゲロウの幼虫の研究）のような伝記的な細部は、学術資料か機関の資料で裏づける必要がある。Wikipedia は根拠に使っていない。
3. **取得できなかった資料**：https://www.pnas.org/doi/10.1073/pnas.0803151105 は取得の許可がタイムアウトした。PubMed と PMC の一部のページはボット確認の画面で本文を読めなかった。いずれも代わりの所蔵先で確認した。
