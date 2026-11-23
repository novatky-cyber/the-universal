# 独立検証レポート：L0001「宇宙・物質・地球の形成、時間の起源」

- 検証者：Verifier（作成に関与していない独立したエージェント）
- 検証日：2026-11-23
- 対象：`content/cycles/0001/lesson.md`、`data/sources.json`（全46件）
- 出典の実在確認の結果：`content/cycles/0001/source_check.json`（確認済み44件／未確認2件：`src.nasa-webb-bigbang`、`src.unesco-silk`）
- 方法：WebFetch／WebSearch で出典の原文または公式ページを取得し、主張の数値・年代・固有名詞・因果の向き・認識ラベルを照合した。実行環境の制約で、DOIのリダイレクト先（Science、Springer）と一部のサイト（LBL、NASAの一部、IPCC）は直接取得できなかった。その場合は、同じ内容の公式発表、ADS、arXiv、PMC で代わりに確認した。
- 「出典不在」は、引用した出典が実在を確認できない場合に加えて、**数値・年代・因果を含むのに出典が付いていない**場合にも使った（内容が正しくても同じ扱い）。CLAUDE.md 規則5「出典のない主張を地図に入れない」に合わせたため。

## 判定表

| 主張ID | 該当箇所 | 主張（要約） | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|---|---|
| C01 | §2 | 人類の歴史（約30万年）は138億年の最後の約0.002% {ラベルなし} | 出典不在 | 計算（3×10⁵ ÷ 1.38×10¹⁰ ≈ 0.0022%）は正しい。ただし「約30万年」に出典がない。出典一覧に `src.smithsonian-human` があるのに引用されていない | 「約30万年（ホモ・サピエンスの出現）[[src:smithsonian-human]]」と出典を付ける | https://humanorigins.si.edu/education/introduction-human-evolution |
| C02 | §2 たとえ | 100年前から1歩ごとに10倍にすると「10歩ほど」で宇宙の始まりに届く | 修正要 | 10²年から10^10.14年までは約8歩。「10歩ほど」はやや過大 | 「わずか8歩ほどで」に直す | （計算による） |
| C03 | §3 1 | 宇宙はかつて高温・高密度で、そこから膨張・冷却してきた {理論} | 確認済み | 第5節の三つの証拠（赤方偏移・CMB・軽元素）と Planck 2018 に支えられている。{理論} は妥当 | — | https://arxiv.org/abs/1807.06209 |
| C04 | §3 2／§4.4 | 特異点は理論を過去へ延ばしすぎた結果で、一般相対論の適用限界のサインと多くの研究者が考える {仮説} | 確認済み | SEP に「特異点の予言は通常、一般相対論の深い欠陥とみなされる」とある。「〜かもしれない」という言い方なら {仮説} で整合する | （任意）§4.4 は「多くの研究者が考えている」という**学界の見方の記述**なので、{理論}（主流の解釈）と書き分けてもよい | https://plato.stanford.edu/entries/cosmology/ |
| C05 | §4.1 表 | インフレーションは「有力な仮説」{論争} | 修正要 | 本文では「仮説」と呼び、ラベルは {論争}、§6.1では「理論的枠組み」と、同じ対象の呼び方が節によって揺れている。ラベル（{論争}）自体は妥当 | 表の記述を「急膨張（インフレーション）が起きたとする有力な理論的枠組み（決定的な実証はない）」にそろえる | https://plato.stanford.edu/entries/cosmology/ |
| C06 | §4.1 表 | 最初の数分で水素・ヘリウムなど軽元素の原子核ができる {理論} | 確認済み | PDG の BBN レビューと一致 | — | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf |
| C07 | §4.1 | 宇宙の年齢 137.87±0.20億年（Planck衛星のデータにΛCDMを当てはめた推定）{理論} | 修正要 | 137.87±0.20億年（13.787±0.020 Gyr）は **Planck＋BAO** を組み合わせた値。Planck単独なら 13.797±0.023 Gyr。一方、§6.2 の H0=67.4±0.5 は Planck単独（TT,TE,EE+lowE+lensing）の値で、データの組み合わせが混在している | 「Planck衛星のデータに、銀河分布の観測（BAO）を組み合わせ、ΛCDMモデルを当てはめた推定で、137.87±0.20億年です（Planck単独では137.97±0.23億年）」 | https://www.aanda.org/articles/aa/full_html/2020/09/aa33880-18/T7.html |
| C08 | §4.2 | ビッグバンは一点の爆発ではなく、空間の尺度の変化。中心は不要 {理論} | 出典不在 | 内容は正しい。しかし引用している `src.nasa-webb-bigbang` の URL は実在を確認できなかった。同じ趣旨はNASAの別ページ（Webb Telescope & The Big Bang: "The universe doesn't have a center"）で確認できる | 出典を `https://science.nasa.gov/mission/webb/big-bang-q-and-a/` に差し替える（sources.json の URL と題名を修正） | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ |
| C09 | §4.2 注意 | 宇宙全体が一点だったかは分からない。全体が無限なら、無限の宇宙が薄まってきた {未知} | 出典不在 | 内容とラベルは妥当（SEP でも扱われる論点）。ただし出典が付いていない | 文末に [[src:sep-cosmology]] を付ける | https://plato.stanford.edu/entries/cosmology/ |
| C10 | §4.2 注意 | 重力・電磁気力で束縛された系（原子・地球・銀河）は膨張しない {理論} | 出典不在 | 内容は標準的な理解として正しい。出典が付いていない | NASA等の入門ページ、または教科書（Weinberg）を出典として付ける | — |
| C11 | §4.3 | 17世紀のニュートン力学は絶対時間を前提にできた {理論} | 確認済み | 『プリンキピア』（1687年）の絶対時間の定義として周知。ラベル {理論} も妥当（出典の付与が望ましい） | （任意）SEP「Newton's Views on Space, Time, and Motion」を出典に加える | — |
| C12 | §4.3 | 特殊相対性理論（1905年）、一般相対性理論（1915年）{理論} | 出典不在 | 年代と内容は正しいが、出典がない | 出典を付ける（例：Ashby 2003 の序論、または SEP の相対論の項目） | — |
| C13 | §4.3 | 2010年、**光格子時計**を使った実験で、高さを33cm変えただけで時計の進みの差を検出 {事実} | 修正要 | 33cm・2010年・Chou et al. は正しい。しかし、使われたのは**アルミニウムイオン光時計（量子論理時計）**で、光格子時計ではない（NIST の2010年9月の発表で確認） | 「2010年、アルミニウムイオンを使った光時計（量子論理時計）2台による実験で、高さを約33cm変えただけで…」 | https://www.nist.gov/news-events/news/2010/09/nist-pair-aluminum-atomic-clocks-reveal-einsteins-relativity-personal ／ https://ui.adsabs.harvard.edu/abs/2010Sci...329.1630C |
| C14 | §4.3 | GPS衛星の時計は差し引きで1日あたり約38マイクロ秒進むため、補正されている {事実} | 確認済み | Ashby の分数周波数ずれ 4.4645×10⁻¹⁰ × 86400秒 ≈ 38.6μs/日。重力で進む効果と速度で遅れる効果の向きも正しい | （任意）「約38マイクロ秒（重力で約46μs進み、速度で約7μs遅れる）」と内訳を示す | https://pmc.ncbi.nlm.nih.gov/articles/PMC5253894 ／ https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system |
| C15 | §4.3 | 補正しなければ、位置の誤差は1日で数km規模に積み上がる | 修正要 | 引用した Ashby 2003（LRR）には km の数値がなく、「容認できない大きな誤差」とだけある。同じ著者の Physics Today 2002 年の記事では「1日で11kmを超える航法誤差」としている。「数km規模」は過小で、出典とも合わない | 「補正しなければ、1日で10km以上（約11km）の誤差が生じる計算になります[[src:ashby2002-physicstoday]]」とし、Ashby (2002) Physics Today 56(5) を sources.json に追加する | https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system |
| C16 | §4.4 | 一般相対論で過去へさかのぼると、密度と温度が無限大になる点（初期特異点）に行き着く | 確認済み | SEP の記述と一致 | — | https://plato.stanford.edu/entries/cosmology/ |
| C17 | §4.4 | 量子重力理論はまだ完成していない {未知} | 確認済み | SEP の記述と一致。ラベルも妥当 | — | https://plato.stanford.edu/entries/cosmology/ |
| C18 | §4.4 | プランク時間 約5.39×10⁻⁴⁴秒 {理論} | 確認済み | CODATA 2022 の値は 5.391 247(60)×10⁻⁴⁴ s。数値は正しい。ただし NIST の値ページは取得ツールで表示できなかった | 「これより短い時間について、現在の物理学は信頼できる説明を持たない」は {理論} より {未知} に近い。一文に分けてラベルを付け直す | https://physics.nist.gov/cgi-bin/cuu/Value?plkt （表示できず。CODATA 2022 資料で確認） |
| C19 | §4.4 表 | 「時間に始まりがある」の一例として、量子宇宙論の「無境界仮説」{仮説} | 根拠不足 | 引用している SEP「Philosophy of Cosmology」の本文は無境界仮説を扱っておらず、文献表に Hartle & Hawking (1983) があるだけ。ラベル {仮説} は妥当 | Hartle & Hawking (1983) Phys. Rev. D 28, 2960 を sources.json に追加して引用する | https://plato.stanford.edu/entries/cosmology/ |
| C20 | §4.4 表 | ビッグバウンス、創発的な時間 {仮説} | 確認済み | SEP に bounce（量子効果で特異点を回避する可能性）、ループ量子重力での時空の「創発」の記述がある | — | https://plato.stanford.edu/entries/cosmology/ |
| C21 | §4.4 | どれも観測による確証はない {未知} | 確認済み | SEP の記述と整合 | — | https://plato.stanford.edu/entries/cosmology/ |
| C22 | §4.4 | 5世紀の神学者アウグスティヌスは「世界は時間の中でではなく、時間とともに造られた」趣旨を述べた（『神の国』第11巻）{事実} | 確認済み | 第11巻第6章 "the world was made, not in time, but simultaneously with time" を確認。『神の国』の執筆は413〜426年で「5世紀」も正しい | （任意）「第11巻第6章」と章まで示す。似た趣旨は『告白』第11巻にもあるため、混同を避ける注記があるとよい | https://www.newadvent.org/fathers/120111.htm |
| C23 | §4.4 | この発想は現代物理学より1500年以上前からあった | 確認済み | 『神の国』（5世紀前半）から一般相対論（1915年）・ルメートル（1927・1931年）までは約1500年。「以上」はぎりぎり成り立つ | （任意）「約1500年前から」 | — |
| C24 | §4.5 | 物理学の基本法則の多くは時間反転しても成り立つ | 確認済み | SEP「Thermodynamic Asymmetry in Time」と一致。「多くは」という限定は、弱い相互作用での T の破れを考えると適切 | — | https://plato.stanford.edu/entries/time-thermo/ |
| C25 | §4.5 | 時間の向きを説明する主要な枠組みは熱力学第二法則とエントロピー {理論} | 確認済み | SEP と一致 | — | https://plato.stanford.edu/entries/time-thermo/ |
| C26 | §4.5 | ボルツマンは S = k log W と表した {理論} | 確認済み | SEP に S_B = k log\|Γ_M\| として記載。歴史的には、この形（k を使う表記）を書いたのはプランクだが、ボルツマンのエントロピーとして呼ぶのは慣例 | （任意）「ボルツマンの考えは S = k log W と表されます（式の形はプランクが整えた）」 | https://plato.stanford.edu/entries/time-thermo/ |
| C27 | §4.5 注意 | 重力が効く系では、物質が集まって星ができる方がエントロピーが大きい場合がある {ラベルなし} | 出典不在 | 出典もラベルもない。SEP は「重力的な一様さ＝低エントロピー、不均一＝高エントロピーという緩い対応」を紹介しつつ、自己重力系に第二法則がどう適用されるかを**未解決の問い**としている | 「重力が効く系では、物質が一様に広がった状態よりも、集まって構造をつくった状態の方がエントロピーが大きいとする見方が一般的です（ただし自己重力系のエントロピーの扱いには議論があります）[[src:sep-time-thermo]] {論争}」 | https://plato.stanford.edu/entries/time-thermo/ |
| C28 | §4.5 | 初期宇宙が低エントロピーだったという前提は「過去仮説」と呼ばれ、理由は未解明 {未知} | 確認済み | SEP（Albert 2000 の用語）と一致。ラベルも妥当 | 「過去仮説に説明が必要かどうか自体にも、哲学者の間で意見の対立がある（Callender vs Price）」と一文加えると、SEP の内容により忠実になる | https://plato.stanford.edu/entries/time-thermo/ |
| C29 | §4.6 | BBN：質量で水素約75%、ヘリウム約25%、重水素・リチウムがわずか {理論} | 確認済み | PDG：Yp ≈ 0.25（予測）、観測値 0.245±0.003 | （任意）「ヘリウム約24〜25%」 | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf |
| C30 | §4.6 | 再結合は約38万年後、約3000K。その光が CMB として届く {理論} | 出典不在 | 数値は標準的な値（Planck 2018：z*≈1090、2.7255K×1091≈2970K）で正しい。しかし引用している `src.nasa-webb-bigbang` は実在を確認できなかった。代わりの候補の NASA「Early Universe」ページには「24万〜30万年」という別の数値も書かれており不適 | 出典を [[src:planck2018-vi]]（z*）と NASA「Webb Telescope & The Big Bang」（38万年）に差し替える。温度は「約3000K（現在のCMB温度×約1100）」と根拠を示す | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ ／ https://arxiv.org/abs/1807.06209 |
| C31 | §4.6 | 最初の恒星・銀河は最初の数億年、わずかな密度のむらが重力で育った {理論} | 確認済み | NASA「Overview（Cosmic History）」の記述と整合。ラベルも妥当（出典の付与が望ましい） | 文末に [[src:nasa-universe]] を付ける | https://science.nasa.gov/universe/overview/ |
| C32 | §4.6 | JWST は宇宙誕生から約3億年後の銀河を分光観測で確認（JADES-GS-z14-0）{事実} | 確認済み | Carniani et al. 2024, Nature 633, 318：z=14.32、"300 million years after the Big Bang" | sources.json の題名を掲載版の "Spectroscopic confirmation of two luminous galaxies at a redshift of 14" に直す。最遠記録は更新されている（MoM-z14、z=14.44、約2.8億年後、Naidu et al. 2025）ので、「最遠」とは書かないこと（現状の文は問題なし） | https://www.nature.com/articles/s41586-024-07860-9 ／ https://arxiv.org/abs/2505.11263 |
| C33 | §4.6 | 炭素・酸素・鉄などは恒星内部の核融合、超新星、中性子星合体でつくられた {理論} | 根拠不足 | 内容とラベルは正しい。しかし引用している NASA「Universe Overview」には、超新星・中性子星合体による元素合成の記述がない | 元素の起源を扱う資料（例：NASA の元素合成の解説、Johnson 2019 "The origin of the elements" Science 363, 474 の周期表）を出典にする | https://science.nasa.gov/universe/overview/ |
| C34 | §4.7 | 約45.67億年前、太陽系が形成された {事実} | 根拠不足 | ICS 年代層序表 v2024/12 には冥王代の基底として 4567 Ma が載っているが、「太陽系の形成」とは書かれていない（間接的な根拠）。数値そのものは CAI の年代（約45.673億年、Connelly et al. 2012）と合う | 一次資料 Connelly et al. (2012) Science 338, 651 を追加して引用するか、「ICS の年代表では地質時代の始まりを45.67億年前としており、これは太陽系最古の固体（CAI）の年代にあたる」と書く | https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf |
| C35 | §4.7 | 地球の年齢 約45.4億年、隕石・月の岩石の放射年代測定から推定 {事実} | 確認済み | USGS：4.54 billion years（誤差1%未満）、隕石と月の岩石にもとづく | — | https://pubs.usgs.gov/gip/geotime/age.html |
| C36 | §4.7 | 放射年代測定の原理（一定の速さで崩壊する）{事実} | 確認済み | USGS の説明と一致 | （任意）ラベルは {理論}（確立した原理）の方が他節と整合する | https://pubs.usgs.gov/gip/geotime/age.html |
| C37 | §4.7 | 遅くとも約35億年前には、地球に生命活動の痕跡が現れる {ラベルなし} | 出典不在 | 出典もラベルもない。35億年前（ストロマトライト等）の解釈には争いがあり、より古い（37〜41億年前）痕跡を主張する研究もある | 「遅くとも約35億年前には生命の痕跡とされるものが見つかっています（これより古い痕跡の主張もあり、解釈に議論があります）{論争}」とし、出典を追加する（次回 L0002 の出典と共通化） | — |
| C38 | §5 証拠1 | 1929年、ハッブルは距離と後退速度の関係を示した {事実} | 確認済み | PNAS 15, 168 (1929) | — | https://ui.adsabs.harvard.edu/abs/1929PNAS...15..168H/abstract |
| C39 | §5 証拠1 | 1927年にルメートルが理論と観測から同じ関係を導いていた {事実} | 根拠不足 | 内容は正しい。しかし引用している IAU の発表ページには「1927年」の記述がなく、ルメートルの貢献を一般的に述べているだけ | Lemaître (1927) Annales de la Société Scientifique de Bruxelles 47, 49 を sources.json に追加して引用する | https://www.iau.org/news/pressreleases/detail/iau1812/ |
| C40 | §5 証拠1 | IAU は2018年、「ハッブル・ルメートルの法則」と呼ぶよう推奨 {事実} | 確認済み | 2018年10月の電子投票の結果を確認 | — | https://www.iau.org/news/pressreleases/detail/iau1812/ |
| C41 | §5 証拠2 | 1965年、ペンジアスとウィルソンが全天のどの方向からも来る正体不明の電波雑音を発見 {事実} | 確認済み | ApJ 142, 419：超過温度は "isotropic, unpolarized, and free from seasonal variations" | — | https://ui.adsabs.harvard.edu/abs/1965ApJ...142..419P/abstract |
| C42 | §5 証拠2／§11 | CMB の現在の温度 約2.725K（セ氏約−270度）、全天でほぼ一様 {事実} | 確認済み | Fixsen 2009：2.72548±0.00057 K。−270.4℃ | — | https://arxiv.org/abs/0911.1955 |
| C43 | §5 証拠2 | 10万分の1程度の温度のむら。その分析で年齢・組成を推定できる {理論} | 確認済み | Planck 2018 の解析の枠組みと一致（ΔT/T ~10⁻⁵） | — | https://arxiv.org/abs/1807.06209 |
| C44 | §5 証拠2 | ビッグバン理論は熱の名残の放射を予測しており、CMB の発見と合致 {理論} | 出典不在 | 歴史的に正しい（Alpher & Herman 1948、Dicke ら 1965）。しかし出典がない | Alpher & Herman (1948) Nature 162, 774、またはワインバーグ『The First Three Minutes』を引用する | — |
| C45 | §5 証拠3 | 軽元素の観測値は BBN の予測とよく一致 {事実} | 確認済み | PDG："D/H and 4He are in agreement"、"overall concordance remains remarkable" | — | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf |
| C46 | §5 証拠3／§7 | リチウム7は観測値が予測より「数倍」少ない（リチウム問題）{未知} | 修正要 | PDG では予測が観測の**約3.1倍**（4.4σ）。「数倍」は幅が広すぎる。この行だけ出典がない | 「観測値が予測の約3分の1しかない（約3倍の食い違い）[[src:pdg-bbn]]」 | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf |
| C47 | §5 歴史 | 1940〜60年代、定常宇宙論が有力な対抗馬だった {事実}。CMB を説明できず、CMB の発見で評価が変わった {理論} | 根拠不足 | 引用している SEP「Philosophy of Cosmology」の本文は定常宇宙論を扱っていない。また定常宇宙論の提唱は1948年（Bondi & Gold、Hoyle）なので、「1940年代」は「1940年代末」が正確 | 「1948年に提唱され、1960年代半ばまで有力な対抗馬だった」に直す。出典は Kragh『Cosmology and Controversy』（1996）や Bondi & Gold (1948)、Hoyle (1948) などに差し替える | https://plato.stanford.edu/entries/cosmology/ |
| C48 | §6.1 | インフレーションは地平線問題・平坦性問題を説明し、CMB のむらの性質も再現する {理論} | 確認済み | SEP："a natural account of the three otherwise puzzling features"。Planck の観測（n_s など）と整合 | （任意）推論の根拠としては Planck 2018 X（Constraints on inflation）の方が直接的 | https://plato.stanford.edu/entries/cosmology/ ／ https://arxiv.org/abs/1807.06209 |
| C49 | §6.1 | インフレーションの仕組みは未確定。モデルが多く反証しにくいという批判 {論争} | 確認済み | SEP："If the properties of the inflaton field are unconstrained, inflationary cosmology is extremely flexible"。ラベル {論争} も妥当 | — | https://plato.stanford.edu/entries/cosmology/ |
| C50 | §6.2 表 | 距離はしご（H0DN 2026）73.50±0.81 {事実}、Planck 2018 67.4±0.5 {理論} | 修正要 | 数値はどちらも正しい。しかし、距離はしごの値を {事実}、CMB からの値を {理論} とすると、読者に「距離はしご側が真の値」と受け取らせるおそれがある。距離はしごも較正モデル（セファイド・Ia型超新星の標準化）に依存しており、Pantos 2026 はむしろ距離はしご側が他のすべての方法から外れていると論じている | 両方を {事実}（各チームの測定・推定の結果）とし、表に「前提：距離指標の較正」「前提：ΛCDMモデル」という列を加える | https://icc.ub.edu/news/a-global-collaboration-reaches-1-precision-local-expansion-rate-universe ／ https://arxiv.org/abs/2601.00650 |
| C51 | §6.2／§10 | 2026年、H0DN が約1%の精度で測定 | 確認済み | ICC-UB の発表で確認（A&A に掲載予定） | 査読付き論文の掲載状況を記載する（「A&A掲載予定」） | https://icc.ub.edu/news/a-global-collaboration-reaches-1-precision-local-expansion-rate-universe |
| C52 | §6.2 | 張力はおよそ5〜7σ {事実} | 確認済み | ICC-UB："approximately 5–7 standard deviations"（CMB+BAO、ΛCDMの推定との比較） | 「どの推定値と比べるかで5〜7σの幅がある」と添える | 同上 |
| C53 | §6.2 | JWST とハッブルの検証でも、測定誤差だけでは説明できないという見方が強まっている {論争} | 修正要 | NASA 2024 の記事（Riess）は確認できた。しかし、同じく JWST を使った Freedman らの CCHP は H0≈70.4（TRGB）を得て、「ΛCDMと整合し新しい物理は不要」と結論している。この**最も強い反対の立場**が書かれておらず、一方の見方に偏っている（CLAUDE.md 品質基準11） | 「一方、同じくJWSTを使ったシカゴ・カーネギーのチーム（Freedmanら）はH₀≈70を得ており、張力は小さいと主張しています[[src:freedman-cchp-2025]]」と加え、出典を追加する | https://science.nasa.gov/missions/webb/nasas-webb-hubble-telescopes-affirm-universes-expansion-rate-puzzle-persists/ ／ https://arxiv.org/abs/2408.06153 |
| C54 | §6.2 | 原因として (a) 系統誤差、(b) 新しい物理、の二方向の議論 {論争} | 確認済み | NASA・ICC-UB・Pantos の各資料と整合 | — | 同上 |
| C55 | §6.2 | 「初期 vs 近傍」でなく「距離はしご vs それ以外のほぼすべて」と見るべきだという分析 {論争} | 確認済み | Pantos & Perivolaropoulos 2026 の要旨と一致 | 査読前のプレプリントであることと、相関を考慮すると6.5σ→3.9σに下がることを添える | https://arxiv.org/abs/2601.00650 |
| C56 | §6.3／§9.1 | 2025年、DESI 3年分のデータを CMB・超新星と組み合わせ、2.8〜4.2σ でダークエネルギーが弱まっている可能性 {論争} | 修正要 | 2025年3月の発表としては正しい（UCSC/LBL）。しかし2025年11月の DES 超新星データの再較正（arXiv:2511.07517）で、DESI DR2＋CMB＋DES-SN の組み合わせは**4.2σ→3.2σに低下**した。CLAUDE.md 規則6（最新の数値を実行時に再確認する）に照らして更新が必要。演習9-1の数値も同じ | 「2025年3月の発表では2.8〜4.2σでしたが、その後の超新星データの再較正で、最も強かった組み合わせは約3.2σに下がりました[[src:des-dovekie-2025]]。いずれも5σには達していません」 | https://news.ucsc.edu/2025/03/desi-dark-energy-evolve/ ／ https://arxiv.org/abs/2511.07517 |
| C57 | §6.3／§9 | 5σ ＝ 約350万分の1、3σ ＝ 約740分の1 | 確認済み | 5σの片側 p ≈ 2.9×10⁻⁷（UCSC："1 in 3.5 million"）、3σの片側 ≈ 1/741 | — | https://news.ucsc.edu/2025/03/desi-dark-energy-evolve/ |
| C58 | §6.4 | Planck 2018：通常物質 約4.9%、ダークマター 約26%、ダークエネルギー 約69% {理論} | 確認済み | 表2：Ωbh²=0.02237、h=0.6736 → Ωb≈4.9%。Ωch²=0.1200 → Ωc≈26.4%。ΩΛ=0.6847≈68.5%（Planck＋BAOなら68.9%）。「約69%」は四捨五入で許容範囲 | （任意）「約68.5%」とした方が Planck 単独の値に忠実 | https://www.aanda.org/articles/aa/full_html/2020/09/aa33880-18/T7.html |
| C59 | §6.4 訂正 | 「26.8%／68.3%」は2013年の Planck 初期公表値に対応 | 確認済み | ESA 2013年3月21日の発表：通常物質4.9%、ダークマター26.8%（ダークエネルギー68.3%は同時の "Planck cosmic recipe" の図） | 出典が付いていない。ESA 2013 の発表を sources.json に追加して引用する | https://www.esa.int/Science_Exploration/Space_Science/Planck/Planck_reveals_an_almost_perfect_universe |
| C60 | §6.4 | 組成は体積の割合ではなく、モデルを仮定した推定値 | 確認済み | Planck 2018 の解析方法と整合 | — | https://arxiv.org/abs/1807.06209 |
| C61 | §6.5 | 第一原因の問いと因果の時間的先行の問題 {論争}／宗教は意味・価値を問う営み {規範}／科学の未解明は神の存在・不在を証明しない {規範} | 確認済み | ラベルの使い分けは適切（{規範} として価値判断であることを明示） | （任意）「宗教を科学と別の土俵に置く」という見方（グールドの NOMA など）自体にも異論がある（一部の神学者・科学者は両者の重なりを主張）と一言添えると、多視点の基準を満たす | — |
| C62 | §7 | 宇宙の加速膨張は強く支持される（2011年ノーベル物理学賞）{未知} | 確認済み | 受賞理由と一致。この行のラベル {未知} は「正体」についてのものなので妥当 | — | https://www.nobelprize.org/prizes/physics/2011/press-release/ |
| C63 | §7 | 初期宇宙では物質と反物質が同じだけできたはずだが、今の宇宙はほぼ物質だけ。理由は不明 {未知} | 確認済み | CERN："The Big Bang should have created equal amounts of matter and antimatter" | — | https://home.cern/science/physics/matter-antimatter-asymmetry-problem |
| C64 | §7 | 観測可能な宇宙の範囲では空間はほぼ平坦 {未知} | 確認済み | Planck 2018：Ω_K ≈ 0.001±0.002 | 出典 [[src:planck2018-vi]] を付ける | https://arxiv.org/abs/1807.06209 |
| C65 | §8 | シャノンの情報エントロピーは統計力学のエントロピーと数学的に同じ形 {事実}、同一視には解釈の対立 {論争} | 修正要 | シャノン自身が "recognized as that of entropy as defined in certain formulations of statistical mechanics"（ボルツマンのH定理に言及）と書いており、趣旨は正しい。しかし §4.5 で示した S = k log W とは見た目の形が異なる（同じ形なのはギブズのエントロピー S = −k Σ pᵢ log pᵢ）。読者が両式を見比べて混乱するおそれがある | 「シャノンの H = −Σ pᵢ log pᵢ は、統計力学の**ギブズのエントロピー** S = −k Σ pᵢ log pᵢ と同じ形をしています（すべての状態が等確率なら S = k log W に一致します）」 | https://people.csail.mit.edu/dmoshkov/courses/codes/shannon1948.pdf |
| C66 | §8 表／§11 | σ は「偶然でこの結果が出る確率がどれほど小さいか」「結果が偶然の揺らぎで説明できる可能性の小ささ」 | 修正要 | 「偶然で説明できる可能性」と書くと、「仮説が誤りである確率」と取り違えやすい（p値のよくある誤解）。演習9-2のベイズ的更新とも整合しない | 「**標準モデル（帰無仮説）が正しいと仮定したとき**、統計的な揺らぎだけでこれほど極端な結果が出る確率の小ささを表す尺度。仮説が正しい確率そのものではない」 | — |
| C67 | §8 表 | ダークエネルギーの性質が宇宙の遠い未来を左右する {仮説} | 確認済み | ノーベル賞プレスリリース（加速が続けば "end in ice"）と整合。ラベルも妥当 | — | https://www.nobelprize.org/prizes/physics/2011/press-release/ |
| C68 | §9.1 | OPERA 2011：光より速いという結果は、装置の不具合（光ファイバーケーブルの接続不良など）が原因で、修正後は光速を超えなかった {事実} | 根拠不足 | 引用している論文 v4（JHEP 2012）は、修正後の値が光速と矛盾しない（(v−c)/c = 2.7±3.1(stat)×10⁻⁶）ことは支える。しかし「光ファイバーの接続不良」という原因は論文に書かれておらず、報道（Nature 2012年など）が根拠 | 原因を説明する一次資料を追加する（例：Nature News 483, 17 (2012) "Neutrinos not faster than light"、または CERN の2012年6月の発表）。原因は「GPS同期用光ファイバーの接続不良と、マスタークロックの発振器の不具合」と二つに分けて書く | https://arxiv.org/abs/1109.4897 ／ https://www.nature.com/articles/483017a |
| C69 | §9.1 | BICEP2 2014：原始重力波の発見発表 → Planck との共同解析で、信号の大部分は銀河の塵と区別できない {事実} | 確認済み | PRL 114, 101301："strong evidence for dust and no statistically significant evidence for tensor modes"、r<0.12 | 2014年の BICEP2 の原論文（PRL 112, 241101）を出典に追加すると経緯が完結する | https://arxiv.org/abs/1502.00612v2 |
| C70 | §9.1 演習 | ハッブル張力は5σ以上、10年以上持続、複数の独立した方法で確認 | 修正要 | 「複数の独立した方法」については、Pantos 2026 が「距離はしご（30件）対 それ以外（58件）」と整理しており、高い値を出しているのは主に距離はしご系の方法。Freedman らの JWST の結果も食い違いを小さくしている。「独立した方法で確認」は言い過ぎ | 「5σ以上、10年以上持続。ただし高い値は主に距離はしご系の方法から得られており、独立した確認の度合いには議論がある」 | https://arxiv.org/abs/2601.00650 ／ https://arxiv.org/abs/2408.06153 |
| C71 | §10 | H0DN：網の目のように複数の経路で確かめ、「一か所の見落とし」で張力を説明するのは難しくなったと研究者が述べる {論争} | 確認済み | ICC-UB："explanations invoking a single overlooked systematic ... increasingly difficult to sustain" | — | https://icc.ub.edu/news/a-global-collaboration-reaches-1-precision-local-expansion-rate-universe |
| C72 | §10 | Euclid・Rubin などのデータで今後数年に大きく動く可能性 {仮説} | 確認済み | 予測として {仮説} と明示しており適切 | — | — |
| C73 | §14 | ワインバーグ『The First Three Minutes』初版1977年／ロヴェッリ『The Order of Time』（邦訳『時間は存在しない』NHK出版） | 確認済み | Basic Books 1977、Riverhead 2018、NHK出版 2019年8月（冨永星訳）を確認 | 邦訳の訳者名「冨永星訳」と刊行年「2019年」を記載する。原著はイタリア語（2017年）であることも書く | https://www.kinokuniya.co.jp/f/dsg-01-9784140817902 ／ https://www.kirkusreviews.com/book-reviews/carlo-rovelli/the-order-of-time/ |

## 件数の集計

| 判定 | 件数 | 主張ID |
|---|---|---|
| 確認済み | 46 | C03, C04, C06, C11, C14, C16, C17, C18, C20, C21, C22, C23, C24, C25, C26, C28, C29, C31, C32, C35, C36, C38, C40, C41, C42, C43, C45, C48, C49, C51, C52, C54, C55, C57, C58, C59, C60, C61, C62, C63, C64, C67, C69, C71, C72, C73 |
| 修正要 | 12 | C02, C05, C07, C13, C15, C46, C50, C53, C56, C65, C66, C70 |
| 根拠不足 | 6 | C19, C33, C34, C39, C47, C68 |
| 出典不在 | 9 | C01, C08, C09, C10, C12, C27, C30, C37, C44 |
| **合計** | **73** | |

補足：C18（プランク時間のラベルの分け方）、C32（sources.jsonの題名）、C59（ESA 2013の出典を付けていない）、C64（出典を付けていない）は「確認済み」としたが、修正案の欄に軽微な修正を推奨している。

## 系統的な問題

1. **出典の「つまみ食い」型の不一致（最多）**：出典そのものは実在するのに、引用箇所の具体的な記述を支えていない例が繰り返し見られた（C15 GPSのkm、C19 無境界仮説、C33 重元素、C34 太陽系年代、C39 ルメートル1927、C47 定常宇宙論、C68 OPERAの原因）。総論的な出典（SEP、NASAの概観ページ、ICS年代表）を、各論の根拠に流用している。**主張1つにつき、その数値・固有名詞が実際に書かれている資料を当てる**運用が必要。
2. **未確認の出典への依存**：`src.nasa-webb-bigbang` は実在を確認できなかったのに、§4.2・§4.6・§14の3か所で根拠や推薦文献として使われている（CLAUDE.md 規則5違反）。同じ趣旨のNASAページへの差し替えが必要。
3. **最新情報の再確認の漏れ（規則6）**：DESI の有意度は2025年11月の超新星データの再較正で下がっている（C56）が、教材は2025年3月時点の数値のまま。サイクルごとに「時事の数値」の再検索を手順として必須にすべき。
4. **ハッブル張力の記述が一方の立場に偏っている**：§6.2・§9・§10 は距離はしご側（SH0ES/H0DN）の見方で一貫している。JWSTを使ったFreedmanら（CCHP）の「張力は小さい」という最も強い反論が欠けている（C50, C53, C70）。ラベルの非対称（距離はしご＝{事実}、CMB＝{理論}）もこの偏りを強めている。品質基準11（最も強い反論を含める）に反する。
5. **データの組み合わせの混在**：Planck の年齢（Planck＋BAO）と H0（Planck単独）を同じ「Planck 2018」として並べている（C07）。数値を引用するときは、どのデータの組み合わせかまで明記すべき。
6. **ラベルの付け忘れ・出典の付け忘れ**：§4.5（重力とエントロピー）、§4.7（35億年前の生命）、§2（30万年）など、数値・因果を含む文にラベルも出典もない（C01, C27, C37）。§4.3 の相対論の年代、§5 の CMB の予測史も出典がない。
7. **用語・実験の取り違え**：「光格子時計」（実際はアルミニウムイオンの量子論理時計、C13）。日本で有名な東大・香取グループの光格子時計による相対論の検証（東京スカイツリー、2020年）と混同した可能性がある。固有名詞は原典の一字一句で照合する必要がある。
8. **視点の偏り（地域・文化）**：§6.5 の「科学以外の問い」は、アウグスティヌス（西方キリスト教）と、抽象的な「世界の多くの宗教」にとどまっている。インド思想の循環する時間（カルパ）、仏教の無始の世界観、中国思想（宇宙生成論）、イスラーム哲学のカラーム宇宙論的論証（ガザーリー：時間の始まりと第一原因の議論で、§6.5 の論点に直結する）など、具体的な非西洋の視点が欠けている。品質基準3・11 の観点から、少なくとも1〜2例は具体的に挙げるべき。
9. **sources.json の書誌の細部**：JADES の題名がarXiv版のまま（C32）、BICEP/Planck の題名の先頭の "A" が欠落、UK Futures Toolkit の年（2014/2017）の不一致、ロヴェッリの原著年・訳者の欠落。未使用の出典（AI関連など18件）が本教材の出典一覧に混在しているかどうかも、`{{sources}}` の展開時に確認が必要。

## 2次検証（改訂版）

- 検証日：2026-11-23
- 対象：`lesson_a.md`（前編）、`lesson_b.md`（後編）、`data/sources.json` に追加された20件
- 出典の実在確認：`source_check.json` に `[2次]` の印を付けて22行を追記（追加20件＋URLを差し替えた2件）。追加20件のうち、確認済み18件、未確認2件（`src.britannica-kalpa`：URLの誤り、`src.nasa-wmap-cmb`：ページが現存しない）。**書誌の誤り**が3件ある：`src.des-recal-2025`（題名・著者）、`src.nature-opera-2012`（題名）、`src.freedman-cchp-2025`（掲載誌の欄が未確定 → ApJ 985, 203, 2025）。

### A. 1次検証で「確認済み」以外だった27件の再判定

| 主張ID | 該当箇所（改訂版） | 1次 | 2次 | 理由 | 残る修正案 | 確認した資料（URL） |
|---|---|---|---|---|---|---|
| C01 | 前編§2 | 出典不在 | 根拠不足 | 出典は付いたが、Smithsonian「Introduction to Human Evolution」のページには約30万年という記述がない（記述があるのは「過去10万年」「6万年」など） | 出典を Smithsonian の Homo sapiens の種のページ（humanorigins.si.edu/evidence/human-fossils/species/homo-sapiens）などに替え、30万年の記述を確かめたうえで引用する | https://humanorigins.si.edu/education/introduction-human-evolution |
| C02 | 前編§2 | 修正要 | 解消 | 「8歩ほど」に修正済み | — | — |
| C05 | 前編§4.1 | 修正要 | 解消 | 「有力な理論的枠組み（決定的な実証はない）」に統一 | — | — |
| C07 | 前編§4.1 | 修正要 | 解消 | Planck＋BAO と Planck単独（137.97±0.23）を区別している | — | https://www.aanda.org/articles/aa/full_html/2020/09/aa33880-18/T7.html |
| C08 | 前編§4.2 | 出典不在 | 解消 | 差し替えた NASA の Q&A ページが「中心がない」を支える。Davis & Lineweaver も「空間の膨張であり、空間の中の運動ではない」と書いている | — | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ |
| C09 | 前編§4.2 | 出典不在 | 解消 | SEP を付与 | — | https://plato.stanford.edu/entries/cosmology/ |
| C10 | 前編§4.2 | 出典不在 | 根拠不足 | 付与された Davis & Lineweaver (2004) の全文（ar5iv）を確認したが、束縛系（原子・太陽系・銀河）が膨張しないという記述はない | Cooperstock, Faraoni & Vollick (1998) ApJ 503, 61 "The influence of the cosmological expansion on local systems"、または Price (2005) "In an expanding universe, what doesn't expand?" などを確かめて差し替える | https://arxiv.org/abs/astro-ph/0310808 |
| C12 | 前編§4.3 | 出典不在 | 解消 | Einstein 1905（Ann. Phys. 17, 891）、1916（Ann. Phys. 49, 769）を確認。「1915年に完成、1916年に総まとめの論文」も正確 | — | https://zenodo.org/records/7113360 ／ https://zenodo.org/records/7113388 |
| C13 | 前編§4.3 | 修正要 | 解消 | アルミニウムイオンの量子論理時計に修正済み | — | https://www.nist.gov/news-events/news/2010/09/nist-pair-aluminum-atomic-clocks-reveal-einsteins-relativity-personal |
| C15 | 前編§4.3 | 修正要 | 解消 | 「10km以上（約11km）」とし、Ashby 2002 を追加 | — | https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system |
| C19 | 前編§4.4 | 根拠不足 | 解消 | Hartle & Hawking 1983 を追加 | — | https://inspirehep.net/literature/192909 |
| C27 | 前編§4.5 | 出典不在 | 解消 | SEP の記述（緩い対応＋自己重力系は未解決の問い）に沿って書き直し、{論争} を付与 | — | https://plato.stanford.edu/entries/time-thermo/ |
| C30 | 前編§4.6 | 出典不在 | 解消 | NASA の Q&A（約38万年）、Planck 2018、「約1100倍」（z*+1≈1091）で支えられる | — | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ |
| C33 | 前編§4.6 | 根拠不足 | 解消 | Johnson 2019 Science 363, 474（元素の起源の周期表）を確認 | — | https://news.osu.edu/the-stuff-of-the-universe-keeps-changing/ |
| C34 | 前編§4.7 | 根拠不足 | 解消 | Connelly 2012 の CAI 年代 4567.30±0.16 Ma と ICS を正しく役割分担して引用している | — | https://pmc.ncbi.nlm.nih.gov/articles/PMC4946626 |
| C37 | 前編§4.7 | 出典不在 | 修正要 | Allwood 2006 は**約34.3億年前**（Strelley Pool）。「約35億〜34億年前」のうち35億年はこの出典では支えられない。ラベル {論争} は妥当。また「{論争}宇宙が…」の間に区切りがない | 「約34億年前（34.3億年前）の地層には、生命がつくったと考えられるストロマトライトが見つかっています[[src:allwood2006]]。」とする。35億年前を残すなら、Dresser 層などの別の出典を追加する | https://ideas.repec.org/a/nat/nature/v441y2006i7094d10.1038_nature04764.html |
| C39 | 前編§5 | 根拠不足 | 解消 | Lemaître 1927（Ann. Soc. Sci. Bruxelles A47, 49）を追加。英訳と研究史の論文で書誌を確認 | — | https://arxiv.org/pdf/1305.6470 |
| C44 | 前編§5 | 出典不在 | 解消 | Alpher & Herman 1948 Nature 162, 774 を確認（約5Kの予測） | （任意）「予測した温度（約5K）は、当時の物質密度の不確かさのため目安にすぎなかった」と添えると、Peebles の評価に忠実 | https://arxiv.org/pdf/1310.2146 |
| C46 | 前編§5・§7 | 修正要 | 解消 | 「約3分の1（約3倍の食い違い）」とし、PDG を付与 | — | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf |
| C47 | 前編§5 | 根拠不足 | 解消 | 1948年の提唱と、Bondi & Gold、Hoyle（ともに MNRAS 108）を ADS で確認 | — | https://articles.adsabs.harvard.edu/pdf/1948MNRAS.108..252B |
| C50 | 前編§6.2 | 修正要 | 解消 | 両方を {事実} とし、「前提」の列と「どちらが真の値かは決まっていない」を追加 | — | — |
| C53 | 前編§6.2 | 修正要 | 解消 | CCHP（H₀≈70、標準モデルと整合）を追加。内容は出典と一致 | sources.json の publisher を「The Astrophysical Journal 985, 203」に直す | https://doaj.org/article/7e6311b92b434ce8a0fd86590eb6f41f |
| C56 | 前編§6.3・後編§9.1 | 修正要 | 解消（書誌は要修正） | 本文の「最も強かった組み合わせは約3.2σ」は出典と一致 | sources.json の題名と著者を正しいものに直す（source_check.json 参照） | https://arxiv.org/abs/2511.07517 |
| C65 | 後編§8 | 修正要 | 解消 | ギブズのエントロピーの式と、等確率なら S=k log W に一致することを明記 | — | https://people.csail.mit.edu/dmoshkov/courses/codes/shannon1948.pdf |
| C66 | 後編§8・§11 | 修正要 | 一部残る | §8と用語集は修正済み。しかし§9.1の冒頭に「5σ（偶然でこうなる確率が約350万分の1）」という旧い言い方が残っている | 「5σ（標準モデルが正しいと仮定したとき、揺らぎだけでこれ以上極端な結果が出る確率が約350万分の1）」とする | — |
| C68 | 後編§9.1 | 根拠不足 | 解消（書誌は要修正） | 二つの不具合は Nature の記事で確認。修正後に光速と矛盾しないことは OPERA の論文 v4 で確認 | sources.json の題名を "Timing glitches dog neutrino claim" に直す | https://www.nature.com/articles/483017a ／ https://arxiv.org/abs/1109.4897 |
| C70 | 後編§9.1・付録A | 修正要 | 解消 | 演習文と解答に、独立した確認の程度に議論があることと CCHP を追記 | 付録Aの9-1の解答で「ただし」が続けて3回出てくる。最後の「ただし、『本物の食い違い』と…」は「なお、」に替える | — |

再判定の集計（27件）：**解消22件**（うち書誌の修正が必要なもの2件：C56, C68）／**一部残る1件**（C66）／**修正要1件**（C37）／**根拠不足2件**（C01, C10）。

### B. 改訂で新しく加わった主張

| 主張ID | 該当箇所 | 主張（要約） | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|---|---|
| N01 | 前編§4.3 | 一般相対論は1915年に完成し、1916年に総まとめの論文 | 確認済み | Ann. Phys. 49, 769（1916年3月20日） | — | https://zenodo.org/records/7113388 |
| N02 | 前編§4.5 | 重力系では、構造をつくった状態の方がエントロピーが大きいとする見方が一般的（扱いには議論）{論争} | 確認済み | SEP の記述と一致 | — | https://plato.stanford.edu/entries/time-thermo/ |
| N03 | 前編§6.2 表 | 距離はしご 73.50±0.81／Planck 67.4±0.5、ともに {事実}、前提の列あり | 確認済み | 数値・前提とも出典と一致 | — | https://icc.ub.edu/news/a-global-collaboration-reaches-1-precision-local-expansion-rate-universe ／ https://arxiv.org/abs/1807.06209 |
| N04 | 前編§6.2 | CCHP（フリードマンら）は JWST・別の距離指標で H₀≈70 を得て、張力は小さく標準モデルと整合すると主張 {論争} | 確認済み | ApJ 985, 203（2025）：TRGB 70.39±1.22±1.33±0.70、「ΛCDM と整合し新しい物理は不要」 | — | https://arxiv.org/abs/2408.06153v3 |
| N05 | 前編§6.3 | DES の再較正後、最も強かった組み合わせは約3.2σに低下 {論争} | 確認済み | arXiv:2511.07517："3.2σ, down from 4.2σ" | 書誌を修正（上記） | https://arxiv.org/abs/2511.07517 |
| N06 | 前編§6.5 | ヒンドゥー教の伝統に、創造と消滅を繰り返す巨大な時間の単位「カルパ（劫）」 | 確認済み（URL要修正） | Britannica「Indian chronology」の記述と一致（ヒンドゥー教・仏教の宇宙論の周期、ブラフマーの1日）。ただし sources.json のURLは開けない | URLを https://www.britannica.com/topic/kalpa-Indian-chronology に直す | https://www.britannica.com/topic/kalpa-Indian-chronology |
| N07 | 前編§6.5 | 仏教は生死の輪廻（サンサーラ）に始まりを想定しない | 根拠不足 | Britannica「samsara」には、輪廻の始まりについての記述がない。内容自体は、パーリ経典『相応部』無始相応（SN 15、「輪廻の始まりは知られない」）に対応する | 一次資料（SN 15.1–3 の英訳、例：Access to Insight / SuttaCentral）を確かめて出典にする。「始まりを想定しない」より、経典の言い方に合わせて「輪廻の始まりは知りえないとする」が正確 | https://www.britannica.com/topic/samsara |
| N08 | 前編§6.5 | 中世イスラームの神学者たちが「始まりを持つものには原因がある。宇宙には始まりがある。ゆえに宇宙には原因がある」というカラーム宇宙論的論証を展開し、現代の宗教哲学でも議論されている {事実} | 修正要 | SEP では、時間的な論証の起源は mutakallimūn とガザーリー（1058〜1111）にあり、この三段論法の形は**W. L. Craig による現代の定式化**として紹介されている。中世の神学者がこの形で述べたとすると、時代がずれる | 「中世イスラームの神学者たち（ガザーリーら）は、宇宙には始まりがあり、始まりを持つものには原因が必要だと論じました。これを現代の哲学者クレイグが『始まりを持つものには原因がある／宇宙には始まりがある／ゆえに宇宙には原因がある』という形に整理したのが**カラーム宇宙論的論証**で、今も賛否の議論が続いています[[src:sep-cosmological-argument]]。」 | https://plato.stanford.edu/entries/cosmological-argument/ |
| N09 | 前編§6.5 | アウグスティヌスに「キリスト教の神学者」と追記 | 確認済み | — | — | — |
| N10 | 後編§8 | H = −Σpᵢ log pᵢ と S = −kΣpᵢ log pᵢ が同じ形。等確率なら S = k log W | 確認済み | Shannon 1948 の記述と、数学的な帰結（pᵢ = 1/W）で確認 | — | https://people.csail.mit.edu/dmoshkov/courses/codes/shannon1948.pdf |
| N11 | 後編§10 | JWST で別の距離指標を使ったチームは張力が小さいと主張。食い違いは距離はしごとそれ以外の間にあるという分析 {論争} | 確認済み | CCHP、Pantos 2026 と一致 | ただし§10の**要点**の文（「ハッブル張力は『測定の誤りでは片づけにくい問題』として、いっそうはっきりしました」）は、本文の両論併記と食い違い、なお一方の立場の結論になっている。「距離はしご側の測定は約1%の精度に達し、張力をめぐる議論はさらに鋭くなりました」などに改める | https://arxiv.org/abs/2408.06153v3 |
| N12 | 後編§9.1・付録A | 演習9-1と解答の改訂（再較正後の最大約3.2σ、独立性に議論、CCHP） | 確認済み | 数値と記述は出典と一致 | 解答の文体（C70の残りの修正案）を参照 | — |
| N13 | 後編§14 | 文献表「NASA『Big Bang and the Evolution of the Universe』」 | 修正要 | 出典を差し替えたのに、文献表の題名が実在しない旧題名のまま | 「NASA『Webb Telescope & The Big Bang』」に直し、紹介文も Q&A の内容（中心がない、約38万年、CMB）に合わせる | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ |

新しい主張の集計（13件）：確認済み10件（うち URL の修正が必要なもの1件：N06）／修正要2件（N08, N13）／根拠不足1件（N07）

### 2次検証のまとめ：まだ残る問題

1. **sources.json の書誌の誤り（3件）と URL の誤り（2件）**：
   - `src.des-recal-2025`：題名と著者が誤り（正しくは Popovic et al.、"The Dark Energy Survey Supernova Program: A Reanalysis Of Cosmology Results And Evidence For Evolving Dark Energy With An Updated Type Ia Supernova Calibration"、MNRAS）。
   - `src.nature-opera-2012`：題名は "Timing glitches dog neutrino claim"。
   - `src.freedman-cchp-2025`：掲載誌を ApJ 985, 203 (2025) と確定させる。
   - `src.britannica-kalpa`：URL の誤り。
   - `src.nasa-wmap-cmb`：ページが現存しない（未使用なので削除を推奨）。
2. **出典が主張を支えていない（3件）**：C01（30万年）、C10（束縛系は膨張しない）、N07（輪廻に始まりがない）。いずれも、出典を付けただけで、その記述があるかを確かめていない。1次検証の「系統的な問題1」が、追加された出典でも繰り返されている。
3. **内容の修正（3件）**：C37（35億年はAllwoodで支えられない）、N08（カラーム論証の三段論法はクレイグによる現代の定式化）、N13（§14の文献表の題名が旧いまま）。
4. **文言の残り（3件）**：C66（§9.1の「偶然でこうなる確率」）、N11（§10の要点が一方の立場）、C70（付録Aの「ただし」の重複）。

## 3次検証

- 検証日：2026-11-23
- 対象：2次検証で残った12件、新しく追加された出典3件（`src.hublin2017`、`src.cooperstock1998`、`src.sn15-anamatagga`）
- `source_check.json` に `[3次]` の印を付けて8行を追記した。新しい出典3件は、いずれも実在を確認した。

| 主張ID | 該当箇所 | 2次の判定 | 3次の判定 | 理由 | 残る修正案 | 確認した資料（URL） |
|---|---|---|---|---|---|---|
| C01 | 前編§2 | 根拠不足 | 解消 | Hublin 2017（Nature 546, 289）：Jebel Irhoud の化石は 315±34 ka。「約30万年」を支える | — | https://pubmed.ncbi.nlm.nih.gov/28593953/ |
| C10 | 前編§4.2 | 根拠不足 | 修正要（軽微） | Cooperstock ら 1998 は、膨張の影響が太陽系・銀河・銀河団でも**無視できるほど小さい**ことを示している。ただし著者は「膨張はすべての規模で進むと考えるのが最も妥当」とも書いており、本文の「それ自体は膨張しません」という断定は、出典より強い | 「重力や電磁気力で強く結びついたもの（原子・地球・太陽系・銀河）では、結びつける力に比べて膨張の影響は無視できるほど小さく、実質的に大きくなることはありません[[src:cooperstock1998]]。」 | https://arxiv.org/abs/astro-ph/9803097 |
| N07 | 前編§6.5 | 根拠不足 | 解消 | SN 15.1（Sujato 訳）："transmigration has no known beginning. No first point is found..." が「輪廻の始まりは知りえない」を支える | — | https://nikaya2.pages.dev/kinhtuongung/sujato-en/15-linked-discourses-on-the-unknowable-beginning |
| C37 | 前編§4.7 | 修正要 | 解消 | 「約34億年前」となり、Allwood 2006（34.3億年前）と一致 | — | https://ideas.repec.org/a/nat/nature/v441y2006i7094d10.1038_nature04764.html |
| N08 | 前編§6.5 | 修正要 | 解消 | ガザーリーらの議論の系譜を、クレイグが三段論法に整理したという記述になり、SEP と一致 | — | https://plato.stanford.edu/entries/cosmological-argument/ |
| N13 | 後編§14 | 修正要 | 解消 | 文献表の題名が「Webb Telescope & The Big Bang」になった | — | https://science.nasa.gov/mission/webb/big-bang-q-and-a/ |
| C66 | 後編§9.1 | 一部残る | 解消 | 「標準モデルが正しいとしても、揺らぎだけでこれほど極端な結果が出る確率」に修正。§8・用語集と整合する | — | — |
| N11 | 後編§10 要点 | 修正要 | 解消 | 両方の立場を並べ、「決着はついていない」とした | — | — |
| C70 | 後編 付録A 9-1 | 一部残る | 解消 | 「ただし」の重複がなくなった（「もっとも」「また」に変更） | — | — |
| 書誌1 | src.des-recal-2025 | 要修正 | 解消 | 題名・著者（Popovic ら）・MNRAS の DOI が正しい | — | https://arxiv.org/abs/2511.07517 |
| 書誌2 | src.nature-opera-2012 | 要修正 | 解消 | "Timing glitches dog neutrino claim"（Reich）に修正済み | — | https://www.nature.com/articles/483017a |
| 書誌3 | src.freedman-cchp-2025 | 要修正 | 解消 | The Astrophysical Journal 985, 203（2025） | — | https://doaj.org/article/7e6311b92b434ce8a0fd86590eb6f41f |
| 書誌4 | src.britannica-kalpa | 要修正 | 解消（軽微な指摘あり） | URL は修正済み。題名欄は「kalpa」のまま（ページの見出しは「Indian chronology」） | （任意）題名を「Indian chronology（kalpa）」とする | https://www.britannica.com/topic/kalpa-Indian-chronology |
| 書誌5 | src.nasa-wmap-cmb | 削除推奨 | 解消 | sources.json から削除済み | — | — |

集計（2次検証の残り12件＋新しい出典の対象3件＝15項目）：**解消14件／修正要（軽微）1件（C10）**。

### 3次検証のまとめ：まだ残る問題
- **C10**：前編§4.2 の「束縛系は、それ自体は膨張しません」は、新しい出典（Cooperstock ら 1998）より強い断定。著者は「膨張はすべての規模で進むが、局所系への影響は無視できる」と述べている。上の修正案のように、「影響は無視できるほど小さく、実質的に大きくならない」と書き換える。
- （任意）`src.britannica-kalpa` の題名欄を、ページの見出しに合わせる。
