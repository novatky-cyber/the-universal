# サイクル 0002 検証ログ（統合）

独立した2体の Verifier による2回の照合。各ファイルの全文を以下に連結する。

---

<!-- verification_1.md -->
# サイクル 0002 独立検証 1（A01〜A15、B01〜B11、C01〜C07、F01〜F33）

- 検証日：2026-11-24
- 担当：Verifier（独立検証。主張の作成には関わっていない）
- 対象：`content/cycles/0002/claims.md` の 66 件
- 方法：`agents/verifier.md` の手順（出典の実在 → 主張を支えるか → ラベル → より新しい資料）。research/ 以下の下書きは読んでいない。

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| A01 | 確認済み | NASA Astrobiology の記事で、定義は1992年ごろの Exobiology Discipline Working Group（12人）の議論から生まれ、Joyce自身が「公式なものは何もない」「作業定義」と述べている。 | なし | https://astrobiology.nasa.gov/news/forming-a-definition-for-life/ |
| A02 | 確認済み | 同記事で、ウイルス（宿主細胞内でしか進化しない）、「self-sustaining」の誤読されやすさ、「capable」の基準の曖昧さが論じられている。 | なし | https://astrobiology.nasa.gov/news/forming-a-definition-for-life/ |
| A03 | 確認済み | Britannica：1920年代、オパーリンとホールデンが独立に、遊離酸素の乏しい還元的大気で外部エネルギーにより無機物から有機物ができ、原始の海で最初の生命が現れたと考えた。 | なし（1924年・1929年という個別の年は本出典にない。年を書く場合は別出典が必要） | https://www.britannica.com/print/article/1791898 |
| A04 | 確認済み | NASA記事：1953年5月15日の Science 論文、指導者はユーリー、同定されたアミノ酸は5種類（アスパラギン酸、グリシン、α-アミノ酪酸、2種のアラニン）。 | なし | https://astrobiology.nasa.gov/news/miller-urey-revisited/ |
| A05 | 確認済み | Johnson ら 2008（Science 322:404）が実在。NASA記事で、未発表の「火山型（アスピレーター）」装置の試料から22種のアミノ酸（有名な装置の試料からは14種）。 | なし | https://pubmed.ncbi.nlm.nih.gov/18927386/ ; https://astrobiology.nasa.gov/news/miller-urey-revisited/ |
| A06 | 確認済み | UChicago の解説：「初期地球の大気はミラーとユーリーの配合とは異なる化学組成だったと現在は考えられている」。ラベル「理論」は妥当。 | なし（出典は「強い還元的」という語は使っていない。教材で補足するなら一次文献を追加） | https://news.uchicago.edu/explainer/origin-life-earth-explained |
| A07 | 確認済み | Gilbert, W.「Origin of life: The RNA world」Nature 319:618（1986）の実在を書誌DB・PDF所蔵先で確認。DOI経由の出版社ページは本環境で表示できなかった。 | なし | https://scilit.com/publications/8231bcf1acd888f8cbebb341ae519b57 ; https://fenix.ciencias.ulisboa.pt/downloadFile/1688987299226660/Gilbert%201986.pdf |
| A08 | 確認済み | Joyce 2002「The antiquity of RNA-based evolution」Nature 418:214。要旨に「DNAとタンパク質の生命の前により単純な生命形態があったと結論する強い理由がある」。ラベル「仮説」は妥当。 | なし | https://www.nature.com/articles/418214a |
| A09 | 修正要 | Robinson 2005（PLoS Biol）は、Ferris の言として「活性化モノマーの説得力ある前生物的合成がない」と述べ、主張を支える。ただし2009年以降、Powner ら（Nature 459:239）が前生物的にありうる条件で活性化ピリミジンリボヌクレオチドを合成するなど進展があり、2005年時点の評価のままでは古い。 | 「RNAワールド仮説の弱点として、RNAの部品（ヌクレオチド）が前生物的な条件でどう作られ、つながったかの経路が挙げられてきた。2009年に Powner らがピリミジン型ヌクレオチドの合成経路を示すなど進展はあるが、すべての部品をそろえて長い鎖にする経路は未解決である。」 | https://journals.plos.org/plosbiology/article/info:doi/10.1371/journal.pbio.0030396 ; https://ui.adsabs.harvard.edu/abs/2009Natur.459..239P/abstract |
| A10 | 根拠不足 | Robinson 2005 は、ヴェヒターズホイザー（1988年）が黄鉄鉱による無機物から有機物への変換を伴う鉱物ベースの代謝を提案したことは支える。しかし「遺伝の仕組みなしに代謝ネットワークが進化しうるかが弱点」という批判は本出典に書かれていない（Martin の「RNAワールドなしでは成り立たない」という発言はある）。 | 前半はそのまま。弱点の部分に出典を追加：Vasas, Szathmáry, Santos（2010, PNAS）「Lack of evolvability in self-sustaining autocatalytic networks…」は、遺伝の仕組みのない自己触媒ネットワークは進化能力が乏しいと示した（なお Vasas ら 2012 は区画化で進化能力が生じうると反論的に示しており、併記が望ましい）。 | https://journals.plos.org/plosbiology/article/info:doi/10.1371/journal.pbio.0030396 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2824406 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3284417 |
| A11 | 確認済み | Jackson 2016（J Mol Evol 83:1–11）は仮説の内容（蛇紋岩化によるアルカリ性、ロスト・シティ）を紹介している。仮説の説明に批判論文を出典として使うのは可能だが、提唱側（Lane, Martin, Russell）の文献を併記するのが望ましい。 | なし（推奨：提唱側の一次文献を追加） | https://link.springer.com/article/10.1007/s00239-016-9756-6 |
| A12 | 修正要 | Jackson 2016 の要旨・本文は主張どおり（無機膜は1μm以上で脂質二重膜約5nmの200倍以上、実験的実証が必要、ロスト・シティに薄い膜の証拠なし、可能性は低い）。ただしその後、Hudson ら（2020, PNAS「CO2 reduction driven by a pH gradient」）が微小流路内の Fe(Ni)S 沈殿をはさんだpH勾配でCO2の還元を起こしたと報告しており、「実験的実証がない」は2016年時点の評価として明示すべき。 | 「Jackson（2016）は…可能性は低いと批判した。その後、Hudson ら（2020, PNAS）は実験室でpH勾配によるCO2の還元を報告したが、天然の噴出孔で同じことが起きたかは未確認で、論争は続いている。」 | https://link.springer.com/article/10.1007/s00239-016-9756-6 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7502746 |
| A13 | 確認済み | Damer & Deamer「The Hot Spring Hypothesis for an Origin of Life」Astrobiology 20(4):429–452（2020）。変動する火山性温泉池での湿潤・乾燥サイクルを提案。 | なし | https://pubmed.ncbi.nlm.nih.gov/31841362/ |
| A14 | 確認済み | UChicago：「さまざまな答えが提案されているが、いずれも検証されていない（all of which remain unverified）」。ラベル「未知」は妥当。 | なし | https://news.uchicago.edu/explainer/origin-life-earth-explained |
| A15 | 確認済み | Weblio（デジタル大辞泉「地球上で生命が出現するまでの物質の進化」、生物学用語辞典）。生物進化との区別は、対象を生命出現前に限る定義から読み取れる（明示的な対比の記述はない）。「原始細胞に至るまで」という語は確認できた定義には見当たらない。 | なし（推奨：「原始細胞に至るまで」を残すなら辞典の該当箇所か教科書を出典に追加） | https://www.weblio.jp/content/化学進化 |
| B01 | 確認済み | Allwood ら 2006, Nature 441:714–718。3,430百万年前のストレリー・プール・チャート（ピルバラ）、「おそらく生物起源」のストロマトライト。生物起源性は論争中と著者も認めつつ生物起源と解釈。ラベル「理論」は妥当。 | なし | https://doi.org/10.1038/nature04764 |
| B02 | 確認済み | Javaux 2019, Nature 572:451–460。要旨「少なくとも34億年前までに微生物の生物圏があり、それより前は議論がある（disputably earlier）」。 | なし | https://link.springer.com/article/10.1038/s41586-019-1436-4 |
| B03 | 確認済み | Nutman ら 2016, Nature（DOI 10.1038/nature19355）「Rapid emergence of life shown by discovery of 3,700-million-year-old microbial structures」、イスア緑色岩帯。 | なし（推奨：URLを nature-index ではなく DOI https://doi.org/10.1038/nature19355 に） | https://www.nature.com/nature-index/article/10.1038/nature19355 |
| B04 | 確認済み | Allwood ら 2018, Nature 563:241–244。「非生物的な堆積後の起源」、変形構造の一部と結論。 | なし | https://ideas.repec.org/a/nat/nature/v563y2018i7730d10.1038_s41586-018-0610-4.html |
| B05 | 確認済み | Dodd ら 2017, Nature 543:60–64。ヌブアギトゥク帯（ケベック）、少なくとも3,770百万年前、場合により4,280百万年前、ヘマタイトの管と糸状体を「推定上の」微化石と解釈。 | なし | https://pubs.usgs.gov/publication/70193303 |
| B06 | 確認済み | McMahon 2019, Proc. R. Soc. B 286:20192410。化学の庭でヌブアギトゥクの管・糸状体と「驚くほど似た」構造を作り、形態だけでは決定的でないと論じた。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6939263 |
| B07 | 確認済み | Bell ら 2015, PNAS「Potentially biogenic carbon preserved in a 4.1-billion-year-old zircon」。軽い炭素同位体、著者は「may be evidence」と慎重。ラベル「仮説」は妥当。 | なし | https://ui.adsabs.harvard.edu/abs/2015PNAS..11214518B/abstract |
| B08 | 確認済み | Moody ら 2024：要旨「LUCA は約42億年前（4.09–4.33 Ga）」。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC11383801/ |
| B09 | 確認済み | 同論文：約2,600タンパク質（本文 2,657）、嫌気性の酢酸生成菌、Cas1/Cas2 欠如から初期型のCRISPR-Cas、「再構成はおそらく不完全」「分子時計が深い分岐で大きく破れうる」。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC11383801/ |
| B10 | 確認済み | Goldman & Becerra 2024, J Mol Evol 92:659–661「A New View of the Last Universal Common Ancestor」。「LUCA が現れるまでの時間をほとんど残さない」「一定の変異率に基づく分子時計は信頼できない」。 | なし | https://link.springer.com/article/10.1007/s00239-024-10193-w |
| B11 | 確認済み | Moody ら 2024：LUCA は孤立して生きていたのではなく生態系の一部で、子孫を残さなかった他系統と初期地球を共有していた、と明記。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC11383801/ |
| C01 | 確認済み | Martins ら 2008（arXiv:0806.2286、EPSL 掲載）。ウラシル δ13C = +44.5‰、キサンチン +37.7‰ で非地球起源。 | なし | https://arxiv.org/abs/0806.2286 |
| C02 | 確認済み | 北大プレスリリース：Oba ら「Uracil in the carbonaceous asteroid (162173) Ryugu」Nature Communications 2023年3月21日。ウラシル 6–32 ppb（ナイアシンも検出）。 | なし | https://www.global.hokudai.ac.jp/?p=68201 |
| C03 | 確認済み | NASA 2025年1月29日：20種のうち14種のアミノ酸、5種すべての核酸塩基、塩水の蒸発でできる11種の鉱物、左右の型はほぼ等量。 | なし | https://www.nasa.gov/news-release/nasas-asteroid-bennu-sample-reveals-mix-of-lifes-ingredients/ |
| C04 | 確認済み | NASA 2025年12月2日：リボース（とグルコース）を検出、デオキシリボースは見つからず。筆頭は東北大学の古川善博、Nature Geoscience。 | なし（推奨：誌名 Nature Geoscience を明記） | https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/ |
| C05 | 確認済み | NASA：「生命そのものの証拠ではない」が、生命誕生の条件が初期太陽系に広く存在したことを示唆。 | なし | https://www.nasa.gov/news-release/nasas-asteroid-bennu-sample-reveals-mix-of-lifes-ingredients/ |
| C06 | 確認済み | Scientific American のブログ（Life, Unbounded）：宇宙パンスペルミアは起源を「外注」したもので「生命の起源という本当の問いを解決したわけではない」。ブログであり論文ではない点に注意。 | なし（推奨：教科書・総説レベルの出典を併記） | https://www.scientificamerican.com/blog/life-unbounded/the-panspermia-paradox/ |
| C07 | 確認済み | JPL 2025年9月10日：試料「サファイア・キャニオン」（岩石チェヤバ滝）に潜在的バイオシグネチャー、Hurowitz ら Nature。「非生物的説明は起こりにくいが排除できない」。ラベル「論争」は妥当。 | なし | https://www.jpl.nasa.gov/news/nasa-says-mars-rover-discovered-potential-biosignature-last-year/ |
| F01 | 確認済み | ICS v2024/12：カンブリア系基底 538.8 ± 0.6、エディアカラ系基底 ~635、K/Pg 66.00 Ma。 | なし | https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf |
| F02 | 確認済み | Poulton ら 2021（Nature 592）要旨：約24.3億年前に初めて上昇、約2億年にわたり閾値をはさんで変動、恒常的な酸素化は約22.2億年前（ロマガンディ炭素同位体異常とともに）。 | なし | https://eprints.whiterose.ac.uk/id/eprint/171586/ ; https://www.leeds.ac.uk/news/article/4797/extra-100-million-years-before-earth-saw-permanent-oxygen-rise |
| F03 | 確認済み | Lyons ら 2014：酸素発生型光合成の時期は合意がなく（38〜23.5億年前の幅）、「一時的には数億年早かった可能性」。Planavsky ら 2014（Nat Geosci 7:283）：GOE の少なくとも5億年前（約29.5億年前の岩石）。 | なし | https://people.earth.yale.edu/sites/default/files/files/Planavsky/30_%20Lyons%20et%20al%20Nature%202014.pdf ; https://www.nature.com/articles/ngeo2122 |
| F04 | 確認済み | Lyons ら 2014：地球内部からの還元的なガス・イオンによる消費で相殺、海底から陸上への火山活動の変化を支持しつつ完全には決着していない。Luo ら 2022（Sci China Earth Sci 65:1646）：「供給の増加か消費の減少かは不確か」。 | なし | https://people.earth.yale.edu/sites/default/files/files/Planavsky/30_%20Lyons%20et%20al%20Nature%202014.pdf ; https://link.springer.com/article/10.1007/s11430-021-9934-y |
| F05 | 確認済み | Lyons ら 2014：約18〜8億年前の大気酸素はおそらく現在の0.1%未満とも。炭素同位体記録が「有名なほど退屈」と記述。「退屈な10億年（boring billion）」の語そのものは本出典にないが、一般に定着した呼称。 | なし（推奨：呼称の出典を補うなら別文献） | https://people.earth.yale.edu/sites/default/files/files/Planavsky/30_%20Lyons%20et%20al%20Nature%202014.pdf |
| F06 | 確認済み | Rooney ら 2014（PNAS 111:51–56）：717〜635百万年前に少なくとも2回赤道付近まで氷が進出。スターティアン氷期の終わり 662.4 ± 3.9 Ma から約5500万年の継続を示唆。ICS でクリオジェニアン基底 ~720、エディアカラ基底 ~635。 | なし | https://durham-repository.worktribe.com/output/1473458 ; https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf |
| F07 | 確認済み | 中国科学院南京地質古生物研究所：明確な最古の真核生物は約16.5億年前の単細胞化石。華北・串嶺溝層の約16.35億年前の多細胞微化石（Science Advances 2024年1月24日）。 | なし | https://english.nigpas.cas.cn/new/hs/rp/202401/t20240124_656672.html |
| F08 | 修正要 | Kay ら 2025（Nature, 2025年12月3日「Dated gene duplications elucidate the evolutionary assembly of eukaryotes」）は実在。ただし約29億年前は「真核生物の起源」ではなく、核などの複雑な特徴の獲得（真核化）の「始まり」で、ミトコンドリアは後に獲得したとする。「起源＝29億年前」と読める書き方は不正確。 | 「分子時計による真核生物の成り立ちの推定には大きな幅があり、Kay ら（2025, Nature）は、真核生物の特徴が少しずつ積み重なる過程が約29億年前に始まり、ミトコンドリアの獲得はそれよりかなり後だったと推定した。」 | https://www.bristol.ac.uk/news/2025/december/complex-life-developed-earlier-than-previously-thought-new-study-reveals.html |
| F09 | 根拠不足 | Tong ら 2022（Curr Opin Microbiol 67:102141「Selective drivers of simple multicellularity」）は単純な多細胞性の論文で、「複雑な多細胞化が少なくとも6回」とも、褐藻とも書いていない。数字の出典は Knoll 2011（Annu Rev Earth Planet Sci 39）で、要旨に「複雑な多細胞生物は6つの系統のみ：動物、陸上植物、真正紅藻、褐藻（コンブ目）、菌類の2群」。 | 出典を Knoll（2011）に差し替え：「Knoll（2011）によれば、複雑な多細胞生物は動物、陸上植物、紅藻（真正紅藻類）、褐藻（コンブ類）、菌類の2群の6系統で独立に生じた。単純な多細胞性はさらに何十回も生じている。」ラベルは「理論」が妥当。 | https://par.nsf.gov/servlets/purl/10322817 ; https://annualreviews.org/doi/pdf/10.1146/annurev.earth.031208.100209 |
| F10 | 確認済み | メモリアル大学：ミステイクン・ポイントの最古の化石は少なくとも5億7400万年前（Matthews ら 2020, GSA Bulletin）。 | なし | https://mun.ca/marcomm/news-releases/archive/2019-2020/new-study-confirms-newfoundland-as-home-to-worlds-oldest-animal-fossils.php |
| F11 | 確認済み | Zhang & Shu 2021（PalZ 95:641–660）：「左右相称動物の多くの系統はカンブリア紀最初の2000万年に現れた」「段階的な進化的事象」「単一の原因で全体を説明できない」。 | なし | https://link.springer.com/article/10.1007/s12542-021-00568-5 |
| F12 | 修正要 | Wood ら 2019（Nat Ecol Evol 3:528–538）は実在し、酸化還元・栄養塩の変化と生物的フィードバックを挙げるが、要旨に捕食や化石の残りやすさは出てこない。論文の主旨は「カンブリア爆発は単一の出来事ではなく一連の放散の一つ」。捕食・酸化還元・各要因の不十分さの議論は Zhang & Shu 2021 が明確に扱う。 | 出典に Zhang & Shu（2021）を追加し、「原因の候補には、海と大気の酸化還元状態や栄養塩の変化、捕食などの生態的な相互作用、化石の残りやすさの変化があり、それぞれの重みは論争中（Wood ら 2019、Zhang と Shu 2021）。Wood らは、動物の進化はエディアカラ紀からの複数の放散の連なりだったと論じた。」 | https://research-portal.st-andrews.ac.uk/en/publications/integrated-records-of-environmental-change-and-evolution-challeng/ ; https://link.springer.com/article/10.1007/s12542-021-00568-5 |
| F13 | 確認済み | IUCN World Heritage Outlook：約5.2億〜5.3億年前、軟組織を含む保存、2012年に登録。 | なし | https://worldheritageoutlook.iucn.org/node/1170 |
| F14 | 確認済み | カナダ百科事典：カンブリア紀中期（5.05〜5.1億年前）、1909年8月30日にウォルコットが発見。 | なし | https://www.thecanadianencyclopedia.ca/en/article/burgess-shale-fossils |
| F15 | 確認済み | Rubinstein ら 2010（New Phytologist 188:365–369）：アルゼンチンのダピンギアン（約4.73〜4.71億年前）の隠胞子、「陸上植物の最古の証拠」。 | なし | https://repositoriosdigitales.mincyt.gob.ar/vufind/Record/CONICETDig_ac9305178331702ab005dfd0f9345ccf |
| F16 | 確認済み | ウプサラ大学：ポーランド・ザヘウミエ採石場の約3億9500万年前の足跡、骨格による最古の証拠より少なくとも1800万年古い（Nature）。 | なし | https://www.uu.se/en/press/press-releases/2009/2010-01-07-fossil-footprints-give-land-vertebrates-a-much-longer-history |
| F17 | 確認済み | Our World in Data の表：86%、75%、96%、80%、76%。出典注に Barnosky ら 2011（Nature）。これらは Barnosky ら 2011 の表の値。 | なし（F18 と組で、ペルム紀末の下方修正を併記すること） | https://ourworldindata.org/mass-extinctions |
| F18 | 修正要 | Marshall 2023（Cambridge Prisms: Extinction 1:e5）は実在。ペルム紀末 81%（Stanley 2016）は正しい。ただし原文は「5大絶滅は統計的に別のものではなく、最大から最小まで絶滅の強さは連続している」とし、補正した解析（Foote、Kocsis ら）でも5大絶滅は連続体の最大級に位置づけられる。「補正したデータでは平常時と区別できない」は、補正で大きさが消えたかのように読め、ずれがある。 | 「Marshall（2023）は、絶滅の強さは最大から最小まで連続しており、5大絶滅は統計的に別種の出来事とは言えない（ただし最大級ではある）として『5つ』の特別扱いを再検討し、ペルム紀末の喪失率も約81%（Stanley 2016）に下方修正されていると述べた。」 | https://cambridge.org/core/journals/cambridge-prisms-extinction/article/forty-years-later-the-status-of-the-big-five-mass-extinctions/D8B7C1C298686D3622273320E778D22A |
| F19 | 確認済み | Eos（Kozik ら 2021, AGU Advances の紹介）：寒冷化（氷室状態）、氷河性の海水準変動、大陸棚の無酸素化。 | なし（推奨：無酸素化も併記） | https://eos.org/editor-highlights/what-conditions-accompanied-the-late-ordovician-mass-extinction |
| F20 | 確認済み | Burgess ら 2014（PNAS 111:3316）：煤山の5層の火山灰、251.941 ± 0.037 〜 251.880 ± 0.031 Ma、「60 ± 48 ka」。 | なし | https://dspace.mit.edu/handle/1721.1/91514 |
| F21 | 確認済み | Burgess ら 2017（Nature Communications）：シベリア・トラップの岩床の最初の貫入が揮発性物質に富む堆積物を加熱し、温室効果ガスを放出して絶滅の引き金になったと提案。ラベル「理論」は妥当。 | なし | https://www.usgs.gov/publications/initial-pulse-siberian-traps-sills-trigger-end-permian-mass-extinction |
| F22 | 確認済み | Blackburn ら 2013（Science 340:941）：最初期の CAMP 火山活動が三畳紀末の絶滅と一致、約60万年で4回のパルス。 | なし | https://ui.adsabs.harvard.edu/abs/2013Sci...340..941B |
| F23 | 確認済み | Alvarez ら 1980（Science 208）：イタリア・デンマーク・ニュージーランドで背景の20〜160倍のイリジウム、衝突仮説。Smit & Hertogen 1980（Nature 285:198、5月22日）：地球外起源、大隕石の衝突の可能性。 | なし | https://ntrs.nasa.gov/citations/19800051929 ; https://www.nature.com/articles/285198a0.pdf |
| F24 | 確認済み | JPL：直径180km、天体は約10km。LBL：Schulte ら 2010（Science、41人の専門家）が「チクシュルーブ衝突が大量絶滅の究極の原因」と結論。 | なし | https://www.jpl.nasa.gov/news/a-smoking-gun-for-dinosaur-extinction/ ; https://newscenter.lbl.gov/2010/03/09/alvarez-theory-on-dinosaur/ |
| F25 | 確認済み | Renne ら 2013（Science 339:684）：K-Pg 境界と絶滅、チクシュルーブ衝突の同時性は3万2000年以内。 | なし | https://ui.adsabs.harvard.edu/abs/2013Sci...339..684R/abstract |
| F26 | 確認済み | National Geographic：Schoene ら（衝突の約10万年前に最大の噴火パルス）と Sprain ら（溶岩の約75%は衝突後）で解釈が異なる。Yale：Hull ら 2020「小惑星が唯一の絶滅要因」。 | なし | https://www.nationalgeographic.com/science/article/what-actually-killed-dinosaurs-volcanoes-heat-up-debate ; https://news.yale.edu/2020/01/16/death-dinosaurs-it-was-all-about-asteroid-not-volcanoes |
| F27 | 確認済み | Springer ら 2019（Front Genet 10）：爆発型・長い導火線型・短い導火線型・ソフト爆発型・K-Pg またぎ型のモデル、「合意はまだない」。白亜紀の真獣類にも言及。 | なし | https://www.frontiersin.org/articles/10.3389/fgene.2019.01241/text |
| F28 | 確認済み | IPBES：約100万種が絶滅の危機。直接要因は影響の大きい順に、陸と海の利用の変化、生物の直接採取、気候変動、汚染、侵略的外来種。 | なし | https://www.ipbes.net/news/Media-Release-Global-Assessment |
| F29 | 確認済み | OWID（2026年10月8日の報告の解説）：1970〜2022年、35,803個体群で平均73%減少。動物の数や種の喪失を意味しない（減少は個体群の半数、43%は増加、7%は安定）。WWF の2026年報告ページでも確認。 | なし | https://ourworldindata.org/2026-lpi-update ; https://www.worldwildlife.org/publications/2026-living-planet-report/ |
| F30 | 確認済み | Cowie ら 2022（Biological Reviews）：第6の大量絶滅が進行中。Marshall 2023：現在の速さは史上最高クラスだが、累積の絶滅数はまだ最大級の絶滅に比べてごく小さい（「まだだが、そうなりうる」）。 | なし | https://www.hawaii.edu/news/2022/01/14/6th-mass-extinction-progress/ ; https://cambridge.org/core/journals/cambridge-prisms-extinction/article/forty-years-later-the-status-of-the-big-five-mass-extinctions/D8B7C1C298686D3622273320E778D22A |
| F31 | 確認済み | Oxford：Durbin（筆頭）、Anderson（責任著者）、Science Advances、約8〜7億年前、エディアカラ紀の甕安（約5.9億年前）ではなくトニアン紀の堆積物を最大年代の較正に使用、「8億年前に動物がいたことを証明するものではない」。EurekAlert で掲載日 2026年10月2日を確認（Oxford のページの日付は9月23日）。 | なし | https://www.ox.ac.uk/news/2026-09-23-new-study-suggests-animals-may-have-evolved-vastly-earlier-than-fossil-evidence ; https://www.eurekalert.org/news-releases/1145493 |
| F32 | 修正要 | Zhang & Shu 2021 は分子時計が動物・左右相称動物の起源を化石より数千万〜数億年古く推定することを支える。しかし化石の残りやすさ（タフォノミー）については、ダーウィン以来の解釈として紹介しつつ、Daley ら 2018 の「エディアカラ紀の保存条件はカンブリア紀に劣らない」という反論を挙げ、初期の動物は小さく痕跡を残しにくかったという別の説明を示している。「残りやすさの変化が突然さの一部を説明する可能性」をそのまま支えるとは言いにくい。 | 「分子時計は動物の起源を最初の化石より数千万〜数億年古く推定することが多い。このずれについては、化石の残りやすさによる見かけだという解釈がある一方、エディアカラ紀の保存条件はカンブリア紀に劣らないという反論（Daley ら 2018）もあり、初期の動物が小さく化石に残りにくかったという説明も出されている（Zhang と Shu 2021）。」 | https://link.springer.com/article/10.1007/s12542-021-00568-5 |
| F33 | 修正要 | オーストラリア博物館：約700万〜600万年前、チャドのトロス・メナラ、人類系統への帰属は論争中（四肢骨がないため二足歩行の確認が困難、と記述）。ただし2026年1月に Williams ら（Science Advances 12(1), DOI 10.1126/sciadv.adv0130）が大腿骨の結節などから二足歩行の証拠を報告しており、出典の「四肢骨がない」という記述は古い。論争が決着したとまでは言えないが、最新の状況を反映すべき。 | 「サヘラントロプス・チャデンシス（チャド）は約700万〜600万年前のもので、人類系統に属するかには論争がある。2026年には、大腿骨の特徴から二足歩行をしていたとする研究（Williams ら, Science Advances）が出たが、他の研究者の評価は分かれている。」（反論の文献も確認して追記） | https://australian.museum/sahelanthropus-tchadensis ; https://www.sciencedaily.com/releases/2026/01/260103155024.htm |

## 件数集計

| 判定 | 件数 |
|---|---|
| 確認済み | 57 |
| 修正要 | 7（A09, A12, F08, F12, F18, F32, F33） |
| 根拠不足 | 2（A10, F09） |
| 出典不在 | 0 |
| 合計 | 66 |

## 全体を通じて気づいた系統的な問題

1. **古い評価がそのまま「現状」として書かれている**：A09（2005年の評価で2009年以降の進展なし）、A12（2016年の批判の後の2020年の実験）、F33（2026年の大腿骨研究）。論争中の主張は「いつ時点の、誰の評価か」を明記し、その後の反論・追試を確認する手順が必要。
2. **出典の範囲を超えた要約**：A10（批判の部分が出典にない）、F09（数字と系統が出典にない）、F12・F32（別の論文の内容が混ざっている）、F18（原文の「連続体」を「平常と区別できない」に言い換え）。一つの出典に複数の内容を寄せて書くときに起こりやすい。
3. **年代の数値が「起源」と「始まり」で混同されやすい**：F08（真核化の始まり＝起源と読める）。分子時計の結果は「何の分岐・何の獲得の年代か」を明記すること。
4. **二次資料への依存**：数値の多くがプレスリリース・解説記事（NASA、大学、OWID、Britannica）経由。今回はおおむね原論文と一致したが、A04/A05/F02/F17 などは原論文の要旨も併記すると検証しやすい。C06 はブログが唯一の出典。
5. **地域の視点**：中国（澄江、華北の真核生物、Zhang & Shu）、アルゼンチン、ポーランド、ロシア（オパーリン）が入っており偏りは小さいが、南アジア（デカン・トラップの研究はインドの研究者の貢献が大きい）、アフリカ（サヘラントロプスの発見チーム）の研究者の視点はほぼ出てこない。
6. **URL の質**：B03（nature-index）、A07（DOI 経由で表示できない）など、引用には DOI か出版社ページを使うことを推奨。

---

<!-- verification_2.md -->
# サイクル 0002 独立検証 その2（D01〜D19、E01〜E15、G01〜G14）

- 検証者：Verifier（主張の作成に関与していない独立のサブエージェント）
- 検証日：2026-11-24
- 対象：`content/cycles/0002/claims.md` の D・E・G 節（48件）
- 手順：`agents/verifier.md` に従う。research/ 以下の下書きは読んでいない。

## D. 進化の仕組み

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| D01 | 確認済み | リンネ協会の記事に、1858年7月1日に書記の J. J. Bennet が両者の論文を読み上げたこと、ダーウィン（病気と息子の死）・ウォレス（モルッカ諸島）とも欠席だったことが書かれている。 | — | https://www.linnean.org/news/2018/07/01/1st-july-2018-160th-anniversary-of-the-presentation-of-on-the-tendency-of-species-to-form-varieties |
| D02 | 確認済み | Darwin Online（Freeman）の解説に、初版の刊行日が1859年11月24日、"survival of the fittest" は第5版（1869）の第4章見出しが初出、"evolution" は第6版（1872）が初出とある。 | — | https://darwin-online.org.uk/EditorialIntroductions/Freeman_OntheOriginofSpecies.html |
| D03 | 確認済み | SEP はラマルクの理論を「歴史的時間における種の変化を説明した最初の一貫した理論」と書き、『動物哲学』（1809）をその詳しい表明としている。 | （任意）SEP によればラマルクの理論の主軸は「単純から複雑への前進」で、獲得形質の遺伝は補助的な過程だった。教材で「ラマルク＝用不用説」と単純化しないよう注記を勧める。 | https://plato.stanford.edu/archives/spr2024/entries/evolution-before-darwin/ |
| D04 | 確認済み | Britannica：スペンサーが『生物学原理』（1864）で初めて用い、ダーウィンが第5版（1869）で採用。 | — | https://www.britannica.com/science/survival-of-the-fittest |
| D05 | 確認済み | Understanding Evolution は自然選択の条件を変異・遺伝・繁殖の差の3つとしている。 | — | https://evolution.berkeley.edu/natural-selection-2 |
| D06 | 確認済み | 同資料に「生殖能力のある子をより多く残すほど適応度が高い」「強さ・速さ・大きさとは必ずしも相関しない」「自然選択には先見性も意図もない」とある。 | — | https://evolution.berkeley.edu/wp-content/uploads/2021/10/misconceptions_about_evolution_2020.pdf |
| D07 | 確認済み | ASU Embryo Project：1866年に Brünn 自然研究会の紀要で発表され、1900年にド・フリース、コレンス、チェルマクが独自に同じ結論に達した。 | （任意）同ページは、1899年にベイトソンがメンデルの仕事を紹介したとも書く。「3人による再発見」は通説どおりでよいが、再発見の経緯には異説（独立性の程度など）があることを注記してもよい。 | https://embryo.asu.edu/pages/experiments-plant-hybridization-1866-johann-gregor-mendel |
| D08 | 確認済み | NLM：Nature の論文は1953年4月25日付。フランクリンのデータは「決定的に重要」で、ウィルキンスとペルーツが彼女の知らないうちに二人に見せた、とある。 | （注意）D09 の再評価は「データを盗んだ」という見方を退けている。教材では D08 と D09 を並べて示し、D08 の書き方が「盗用」の印象を与えないようにする。 | https://profiles.nlm.nih.gov/spotlight/sc/feature/doublehelix |
| D09 | 根拠不足 | 科学博物館のブログは、Cobb と Comfort（2023, Nature）が「不当に扱われたヒロイン」ではなく「対等な貢献者」とみるべきだと論じた点を支える。しかし「評価は分かれている」を示す材料はない。ブログは批判や反論を一つも挙げておらず、従来の通俗的な語りと比べているだけ。追加の検索（Science News など）でも、この再評価に反論する研究者の発言は見つからなかった。 | 「Cobb と Comfort（2023）は、新たに見つかった書簡や草稿をもとに、フランクリンを『データを盗まれた被害者』ではなく『対等な貢献者』と位置づける再評価を示した。これは長く広まってきた通俗的な語りとは異なる見方である。」ラベルは「論争」から「理論」（あるいは解釈）に変えるか、「論争」のままにするなら反対の立場をとる出典を加える。 | https://blog.sciencemuseum.org.uk/rosalind-franklins-role-revealed-on-the-70th-anniversary-of-the-dna-double-helix-breakthrough/ ; https://www.sciencenews.org/?p=3123989 |
| D10 | 確認済み | NCBI は27の遺伝暗号表（ID 1〜33。欠番あり）を挙げている。表2（脊椎動物ミトコンドリア）では UGA がトリプトファン（W）を指定する。 | （任意）「20種以上」は正しいが、「27表（2026年11月時点）」と書けばより正確。 | https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi |
| D11 | 確認済み | OpenStax は、対立遺伝子の頻度を変える力として自然選択・突然変異・遺伝的浮動・遺伝子流動（移住）を挙げている。 | — | https://openstax.org/books/concepts-biology/pages/11-2-mechanisms-of-evolution |
| D12 | 確認済み | 同書に、浮動は偶然の効果であり、小さな集団ほど強く働くとある。ボトルネック効果と創始者効果（アフリカーナーの例）も説明されている。 | — | 同上 |
| D13 | 確認済み | Christ's College の Darwin200 のページに、『人間の由来』（1871）での性選択と、生存には不利でも雌に好まれるクジャクの尾の例がある。 | — | https://darwin200.christs.cam.ac.uk/node/37 |
| D14 | 確認済み | ミズーリ大学の展示ページは、現代的総合を1930年代前半から1950年代とし、ドブジャンスキー（1937）、マイヤー（1942）、ハクスリー（1942、"evolutionary synthesis" などの語を作った）を挙げている。 | — | https://library.missouri.edu/specialcollections/exhibits/show/darwin/genes |
| D15 | 確認済み | 総研大の太田朋子氏インタビューに、木村が1968年に中立説を提唱し、分子進化の多くを中立な突然変異が浮動で固定されることで説明した、とある。注記によれば、根拠は分子時計ではなくタンパク質の進化速度の解析。 | （任意）同時期に King と Jukes（1969, Science）も独立に同様の議論をした。補足すると単独の発見物語になりにくい。 | https://ir.soken.ac.jp/record/5154/files/%E5%A4%AA%E7%94%B0%E6%9C%8B%E5%AD%90%E6%B0%8F%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%93%E3%83%A5%E3%83%BC.pdf |
| D16 | 確認済み | Kimura (1977) Nature 267:275、題名は "Preponderance of synonymous changes as evidence for the neutral theory of molecular evolution"。 | — | https://www.nature.com/articles/267275a0 |
| D17 | 確認済み | Ohta (1973) Nature 246:96 "Slightly Deleterious Mutant Substitutions in Evolution"。わずかに有害な突然変異が偶然に固定されることを、中立仮説を拡張して論じている。 | — | https://www.nature.com/articles/246096a0 |
| D18 | 確認済み | ゼンケンベルクの記事に、中立説は大きな適応に対する自然選択を否定しないとある（キリンの斑点の例）。 | （任意）同記事によれば、中立突然変異が表現型の違いも生むという「拡張版」には論争がある。「形態の細部には中立的な変化もありうる」と一言加えると正確になる。記事は行動の適応には触れていない。 | https://www.senckenberg.de/en/?p=160416 |
| D19 | 根拠不足 | Kern と Hahn（2018, MBE 35:1366）が連鎖した選択を根拠に中立説を批判し、それでも中立モデルを帰無仮説として使うことは有用だと述べている点は、出典で確認できた。しかし「反論も出ている」の出典がない。また「（帰無仮説としての役割は）広く認められている」は、批判者自身が認めている点として書くほうが正確。 | 出典に Jensen ら（2019, Evolution, "The importance of the Neutral Theory in 1968 and 50 years on: A response to Kern and Hahn 2018"）を加える。文案：「Kern と Hahn（2018）は、連鎖した選択がゲノムの多くを形づくっているとして中立説の中心的主張を批判した。これに対し Jensen ら（2019）が反論している。批判した側も、中立モデルを帰無仮説として使う意義は認めている。」 | https://hahnlab.sitehost.iu.edu/Publications/KernHahn2018.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6496948 |

## E. 生命の木と証拠

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| E01 | 確認済み | Woese と Fox（1977, PNAS 74:5088）は、16S/18S rRNA の比較から真正細菌・古細菌（archaebacteria）・原始真核生物（urkaryotes）の3つの「一次界」を提案している。 | 1990年の「ドメイン」の部分は1977年の論文では裏づけられない。出典に Woese, Kandler & Wheelis（1990, PNAS 87:4576）を加える。1977年の論文では「ドメイン」ではなく「一次界（primary kingdoms）」と呼ばれていたことも注記するとよい。 | https://sites.usp.br/dbf/wp-content/uploads/sites/1573/2025/07/Woese_1977.pdf |
| E02 | 確認済み | Williams ら（Nature Ecology & Evolution 4:138–147。2019年12月にオンライン公開、2020年の号に掲載）は、モデルの当てはまりを適切に扱えば真核生物は古細菌の内側から生じる、という2ドメイン説を支持し、ヘイムダル古細菌を最有力の近縁群としている。 | （任意）ラベル「理論」は妥当。ただし3ドメイン説を支持する解析（Da Cunha ら 2017 など）もあり、議論が続いていることに一言触れるとよい。 | https://researchportal.bath.ac.uk/en/publications/phylogenomics-provides-robust-support-for-a-two-domains-tree-of-l/ |
| E03 | 確認済み | Spang ら（2015, Nature 521）が新しい門の候補ロキアーキオータを報告し、そのゲノムに真核生物に特有のタンパク質の遺伝子があることを確認した。Eme ら（2023, Nature 618:992）は真核生物をヒドアーキオータ目（Hodarchaeales、ヘイムダル古細菌綱）の姉妹群に置いた。この配置は、マーカー遺伝子の選び方や SR4 リコーディング・速い部位の除去を組み合わせたときにだけ安定して得られ、処理をしない最尤法ではニョルドアーキオータの姉妹群になる。主張の「配置は解析法に依存する」と一致する。 | （任意）採取地は repec の抄録には書かれていない。深海堆積物（ロキの城熱水域の付近）という記述は原論文の本文で確認する。 | https://ideas.repec.org/a/nat/nature/v521y2015i7551d10.1038_nature14447.html ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10307638 |
| E04 | 確認済み | Doolittle（1999, Science 284:2124）は「生命の歴史は木としては適切に表せない」と述べ、網目状の図（図3）を示している。 | （任意）Doolittle はこれを主に原核生物と初期の真核生物に限定しており、分類のための木そのものは捨てるべきでないとも述べている。教材ではこの限定を残す。 | https://www.cs.sjsu.edu/faculty/khuri/HUT_2008/Doolitle_1999.pdf |
| E05 | 確認済み | ASU：Journal of Theoretical Biology に掲載。ミトコンドリア、色素体、基底小体の共生起源を提案し、少なくとも15誌に投稿したのち受理された。 | （任意）論文は基底小体（鞭毛）の共生起源も提案したが、この部分は現在支持されていない。「ミトコンドリアや葉緑体など」の「など」が基底小体を指すなら、その点を注記する。 | https://embryo.asu.edu/pages/origin-mitosing-cells-1967-lynn-sagan |
| E06 | 確認済み | Sloan ら（2018, Nat Rev Genet）はミトコンドリアと色素体の祖先をアルファプロテオバクテリアとシアノバクテリアとしている。「広く受け入れられている」は OpenStax で確認した。 | 出典に OpenStax を加える。Sloan らは、ミトコンドリアのプロテオームの起源（複数の細菌が関わったかどうか）には議論があるとも述べている。 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6469396 ; https://openstax.org/books/concepts-biology/pages/13-2-eukaryotic-origins |
| E07 | 確認済み | Understanding Evolution は8つの証拠の系列を挙げ（化石と中間形、分布、相同、発生、入れ子の分類群、自然界での観察、実験、人為選択）、それらが「収束して」生命の歴史を語ると述べている。 | （任意）出典の8項目には「人為選択」がある。主張に加えてもよい。 | https://evolution.berkeley.edu/lines-of-evidence |
| E08 | 確認済み | Daeschler ら（2006, Nature 440:757）が北極圏カナダの後期デボン紀から四肢動物に似た魚を報告している。約3億7500万年前という年代と、適した年代・環境の地層を狙って探したことは、シカゴ大学の当時の記事（Daeschler の談話）で確認した。 | 出典にシカゴ大学の記事を加える（Nature の抄録だけでは年代と探索の経緯を裏づけられない）。 | https://ideas.repec.org/a/nat/nature/v440y2006i7085d10.1038_nature04639.html ; https://chronicle.uchicago.edu/060413/fossils.shtml |
| E09 | 修正要 | 出典（MSU Today、2025年11月11日）によれば、MSU で7万5000世代に達したあと、2022年に実験はテキサス大学オースティン校（Jeffrey Barrick）へ移り、そこで8万2000世代まで続いている。「7万5000世代を超えている」は誤りではないが、出典にあるより新しい数字を使っていない。クエン酸の利用は2003年ごろ（約3万1000世代）。「酸素のある条件で」は出典には書かれていない（Blount ら 2008 で確認できる）。 | 「レンスキーの大腸菌長期進化実験は1988年に12の集団で始まった。一つの集団では、酸素のある条件でクエン酸を利用する能力が約3万1000世代目に進化した（Blount ら 2008）。2022年にテキサス大学オースティン校へ移って続いており、2025年11月時点で約8万2000世代に達している。」公開時に最新の世代数を再確認する。 | https://msutoday.msu.edu/news/2025/11/evolution-under-a-microscope-going-strong-at-msu |
| E10 | 確認済み | Grant と Grant（2006, Science 313）：ダフネ・メジャー島のガラパゴスフィンチの一種 G. fortis では、1977年の干ばつ後に大きなくちばしの方向へ選択が働いた。2004〜05年には、増えた G. magnirostris との競争で小さなくちばしの方向へ強い選択が働いた（約0.70標準偏差の縮小）。 | （任意）対象の種（G. fortis）と競争相手（G. magnirostris）を明記する。 | https://eeb.tamu.edu/wp-content/uploads/sites/141/2015/01/Science-2006-Grant-224-6.pdf |
| E11 | 確認済み | WHO の2025年10月13日の発表：「2023年に、人の一般的な感染症を引き起こし、検査で確認された細菌感染の6件に1件が抗菌薬に耐性だった」。 | — | https://www.who.int/news/item/13-10-2025-who-warns-of-widespread-resistance-to-common-antibiotics-worldwide |
| E12 | 確認済み | NCSE：人間とチンパンジーは約600万年前の共通祖先集団から分かれた姉妹群で、どちらがより進化しているということもない。 | — | https://ncse.ngo/misconception-monday-lets-stop-monkeying-about-shall-we |
| E13 | 確認済み | Understanding Evolution の誤解集に「進化は十分に支持され、広く受け入れられた科学理論であり、単なる勘ではない」とある。 | — | https://evolution.berkeley.edu/wp-content/uploads/2021/10/misconceptions_about_evolution_2020.pdf |
| E14 | 確認済み | 同資料に "evolution produces a tree, not a ladder" とある。 | — | 同上 |
| E15 | 確認済み | SEP「選択の単位」は、ドーキンス（1976, 1982）の遺伝子中心の見方、複製子と相互作用子（Hull 1980）、群選択、血縁選択、多レベル選択を扱っている。 | — | https://plato.stanford.edu/archives/win2023/entries/selection-units/ |

## G. 論争・異説・社会

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| G01 | 確認済み | Nature 514:161–164（2014）"Does evolutionary theory need a rethink?" に、Laland らの "Yes, urgently"（発生のバイアス、可塑性、ニッチ構築、遺伝子以外の遺伝）と、Wray, Hoekstra らの "No, all is well" が並んで載っている。 | — | https://www.doi.org/10.1038/514161A |
| G02 | 根拠不足 | 出典は Eldredge 本人の回顧（Paleobiology, 2024年5月オンライン公開、2025年11月号に掲載）。停滞が「よく見られる現象として実証的に確立した」という記述はある。しかし「広く受け入れられている」かどうかと「仕組みに議論がある」ことは、断続平衡説の提唱者自身の見方でしか裏づけられていない。論争を示す主張なのに、出典が当事者の一方だけになっている。 | 独立した出典を加える。例：Hunt, Hopkins & Lidgard（2015, PNAS, "Simple versus complex models of trait evolution and stasis as a response to environmental change"）は、化石の系列で停滞がよく見られることを定量的に示し、その説明を検討している。文案の末尾：「…停滞がよく見られることは多くの化石系列の分析で確かめられているが、なぜ停滞するのか（安定化選択、環境の揺れの平均化、地理的な分断など）には議論がある。」 | https://www.cambridge.org/core/journals/paleobiology/article/reflections-on-punctuated-equilibria/C75F83CCFD766DE6E3B3CEB712078861 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4413263 |
| G03 | 確認済み | Abbot ら "Inclusive fitness theory and eusociality"（Nature 471:E1–E4, 2011年3月24日）、著者は計137人。White Rose のページには Nowak, Tarnita, Wilson（2010, Nature 466:1057）への反論だとは書かれていないが、Nature の "Brief Communications Arising"（既発表論文への反論欄）に載った記事で、反論の対象はこの論文である。 | （任意）出典に Nature 掲載版（471:E1–E4）の DOI を併記する（DOI は本検証では未照合）。 | https://eprints.whiterose.ac.uk/id/eprint/110877/ |
| G04 | 根拠不足 | Halstead（1985）"Anti-darwinian theory in Japan"（Nature 317）は実在し、今西の著作を扱っている。一方、src.yoshimura2016（生化学 88(1) 巻頭言「進化圧と評価」）は棲み分けと今西に触れるだけで、「棲み分けは生態学で評価される」「今西進化論は進化生物学では少数意見」のどちらも述べていない（棲み分けの科学的位置づけを問いかけて、答えていない）。主張の後半の評価を支える出典がない。 | 主張の後半の評価を直接述べている学術的な資料（科学史の論文、日本の生態学・進化学の教科書や学会誌の総説など）に置き換える。見つからないなら、後半を「今西の進化論は自然選択を中心に置く主流の進化生物学とは大きく異なり、Halstead（1985）など海外からも批判を受けた」に弱め、src.yoshimura2016 は根拠から外す。 | https://www.nature.com/articles/317587a0.pdf ; https://www.jbsoc.or.jp/100th_aniv/wp-content/uploads/2024/03/Vol.88_No.1.pdf |
| G05 | 確認済み | de Waal（2003, Animal Cognition 6:293 "Silent invasion"）は、個体に名前を付けて識別する方法は1950年代の今西に始まる東洋由来のもので、西洋の抵抗を経て「明らかに勝った（clearly won out）」と述べている。Matsuzawa と McGrew（2008, Current Biology 18:R587）の実在と主題（今西と日本の霊長類学の60年）は京都大学のページで確認した。DOI のリンク先は取得がタイムアウトしたため、本文は読んでいない。 | — | https://www.emory.edu/LIVING_LINKS/publications/articles/deWaal_2003b.pdf ; https://www.kyoto-u.ac.jp/en/archive/prev/news_data/h/h1/news6/2008/080723_1 （取得できなかったもの：https://doi.org/10.1016/j.cub.2008.05.040） |
| G06 | 確認済み | Gould（1988）"Kropotkin Was No Crackpot"（Natural History 97(7)）は、『相互扶助論』（1902）が、ロシアの研究者に主流だったダーウィン批判・解釈の流れに属すると論じている。厳しい環境との闘いでは協力が有利になるというクロポトキンの区別も紹介している。 | （任意）Gould はクロポトキンが「集団の利益」で説明しがちな点を批判している。最も強い反論として添えるとよい。 | https://www.marxists.org/subject/science/essays/kropotkin.htm |
| G07 | 確認済み | MSU の Seventeen Moments のページ：ルイセンコがメンデル遺伝学を退けた、1948年8月の農業科学アカデミー（VASKhNIL）の会合で党の介入により決着し、遺伝学研究は1960年代半ばまで止まった、ヴァヴィロフは1940年に逮捕された。Britannica：ヴァヴィロフは1943年1月26日にサラトフで死去。獲得形質の遺伝（ラマルク説）が1948年に公式の路線になったことは Britannica の Lamarckism の項で確認した。 | 「獲得形質の遺伝」の部分は MSU のページでは裏づけられないので、Britannica の "Lamarckism – Persistence of Lamarckism" を出典に加える。 | https://soviethistory.msu.edu/1947/lysenkoism-in-biology/ ; https://www.britannica.com/biography/Nikolai-Vavilov ; https://www.britannica.com/science/Lamarckism/Persistence-of-Lamarckism |
| G08 | 確認済み | NAS の2008年の発表に、"evolution's role as the central organizing principle of modern biology" と "the evidence for evolution can be fully compatible with religious faith" がある。 | — | https://www.nationalacademies.org/news/2008/01/scientific-evidence-supporting-evolution-continues-to-grow-nonscientific-approaches-do-not-belong-in-science-classrooms |
| G09 | 確認済み | 判決日は2005年12月20日（NCSE）。NCSE のページは「科学ではない」という判断を明示していないが、判決文（M.D. Pa. の意見書）に "ID is ... not a scientific theory" とある。 | 「科学ではない」の根拠として、判決文（pamd.uscourts.gov）を出典に加える。 | https://ncse.ngo/creationism/legal/intelligent-design-trial-kitzmiller-v-dover ; https://www.pamd.uscourts.gov/sites/pamd/files/kitzmiller_342.pdf |
| G10 | 確認済み | EWTN のメッセージは1996年10月22日付。第4段落に "recognition of evolution as more than an hypothesis"、第5段落に霊魂は神が直接創造する（Humani Generis の引用）とある。 | （任意）英訳は当初 "more than one hypothesis" と誤訳され、のちに訂正された。教材で引用するなら訂正後の訳を使う。 | https://www.ewtn.com/catholicism/library/message-to-the-pontifical-academy-of-science-on-evolution-8825 |
| G11 | 確認済み | Britannica：19世紀後半から20世紀初めに広まり、自由放任、不平等、帝国主義・植民地主義、人種主義の正当化に使われた。 | — | https://www.britannica.com/topic/social-Darwinism |
| G12 | 確認済み | NHGRI：ゴルトンが1883年にこの語を導入した。米国では1970年代までに30州の法律で少なくとも6万人、ナチス・ドイツでは少なくとも40万人が強制不妊手術を受けた。 | — | https://www.genome.gov/about-genomics/fact-sheets/Eugenics-and-Scientific-Racism |
| G13 | 確認済み | 法務省の資料（訟務月報71巻3号の判決要旨）：最高裁大法廷の判決は2024年7月3日、旧優生保護法の規定を憲法13条・14条1項に違反するとした。規定の適用期間は1948年9月11日〜1996年9月25日。 | （任意）同資料には「少なくとも約2万5000人」が不妊手術を受けたとある。「多くの人」をこの数字に置き換えると具体的になる。 | https://www.moj.go.jp/content/001457732.pdf |
| G14 | 確認済み | Watson と Szathmáry "How can evolution learn?"（Trends in Ecology & Evolution 31(2):147–157, 2016）。変異と選択による漸進的な適応と、学習理論とを結びつける見方を、仮説的な語調（"might"）で示している。ラベル「仮説」は妥当。 | — | https://eprints.soton.ac.uk/396543 |

## 集計

| 判定 | 件数 | 主張ID |
|---|---|---|
| 確認済み | 43 | 上記以外のすべて |
| 修正要 | 1 | E09 |
| 根拠不足 | 4 | D09, D19, G02, G04 |
| 出典不在 | 0 | — |
| 合計 | 48 | |

「確認済み」のうち、出典の追加を勧めるもの（主張の一部が挙げられた出典だけでは裏づけられず、別の資料で確認したもの）：E01（1990年のドメイン）、E06（広く受容）、E08（年代と探索の経緯）、G07（獲得形質の遺伝）、G09（「科学ではない」）。

## 系統的な問題

1. **「評価が分かれている」「広く認められている」を出典が支えていない**：D09、D19、G02、G04 はいずれも、評価の状況（論争中である、受け入れられている、少数意見である）を述べる部分が、挙げた出典に書かれていない。論争ラベルの主張では、対立する双方の出典、または論争を俯瞰した第三者の総説を少なくとも1つ付けることを勧める。
2. **当事者の自己評価だけに頼っている**：G02（断続平衡説の提唱者 Eldredge の回顧）のように、学説の提唱者自身の文章だけで、その学説の受容のされ方を裏づけている例がある。
3. **出典と主張の細部が食い違う**：E01・E08・G07・G09 では、主張の一部（年代、経緯、用語）が挙げた出典に書かれておらず、出典の外の知識で補われている。出典IDと主張を1文ずつ対応させる点検を勧める。
4. **時点のある数値の更新漏れ**：E09（長期進化実験の世代数）では、出典に書かれているより新しい数字が使われていない。時事・数値は公開直前に再確認する（CLAUDE.md 絶対ルール6）。
5. **視点の偏り**：G 節は日本（今西、旧優生保護法）、ロシア・ソ連（クロポトキン、ルイセンコ）、米国、カトリックを扱っており、多視点の配慮はある。一方、イスラム圏、中国、ラテンアメリカ、アフリカでの進化論の受容と論争はない。また、カトリック以外の宗教（プロテスタント福音派、イスラム、仏教など）が進化をどう見てきたかも欠けている。D 節（進化の仕組み）はほぼ英米中心の学説史で、日本の中立説（木村・太田）を除けば非英語圏の寄与が見えにくい。
6. **取得できなかった資料**：https://doi.org/10.1016/j.cub.2008.05.040（Matsuzawa & McGrew 2008）は取得の許可がタイムアウトしたため、本文を読んでいない。実在は京都大学のページで確認した。

---

<!-- verification_1b.md -->
# サイクル 0002 独立検証 1b（第2回・担当 V1：A09r〜N07、15件）

- 検証日：2026-11-24
- 担当：Verifier（独立検証。主張の作成には関わっていない）
- 対象：`content/cycles/0002/claims_round2.md` の「担当 V1」15件
- 方法：`agents/verifier.md` の手順。「既出」は claims.md の同じ出典を確認。出典が空欄のもの（N02, N05）は Verifier が資料を探した。research/ 以下は読んでいない。

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| A09r | 確認済み | Robinson 2005（PLoS Biol）で、活性化モノマーの前生物的合成が最大の課題とされている。Powner ら 2009（Nature 459:239, DOI 10.1038/nature08013）は、遊離のリボースや塩基を経ずに活性化ピリミジンリボヌクレオチドを合成した。プリンと重合はこの論文の範囲外で、「すべての部品をそろえて長い鎖にする経路は示されていない」は妥当。ラベル「論争／未知」も妥当。 | なし（推奨：プリンを含む統一経路の提案（Becker ら 2019, Science など）にも触れると最新の状況に近づく） | https://journals.plos.org/plosbiology/article/info:doi/10.1371/journal.pbio.0030396 ; https://ui.adsabs.harvard.edu/abs/2009Natur.459..239P/abstract |
| A10r | 確認済み | Vasas, Szathmáry, Santos「Lack of evolvability in self-sustaining autocatalytic networks constraints metabolism-first scenarios for the origin of life」PNAS 107(4):1470–1475（2010）。GARD モデルにもとづく理論・計算研究で、構成情報の複製が不正確で「系に進化能力がない」として、代謝先行説に注意を促した。「理論研究がある」という書き方は妥当。 | なし（推奨：区画化で進化能力が生じうるとした Vasas ら 2012（Biology Direct）を併記するとラベル「論争」に合う） | https://pmc.ncbi.nlm.nih.gov/articles/PMC2824406 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3284417 |
| A12r | 確認済み | Hudson ら 2020（PNAS「CO2 reduction driven by a pH gradient」）：微小流路内の Fe(Ni)S 沈殿をはさんだpH勾配で、H2によりCO2をギ酸に還元。pH勾配を小さくする、H2を除く、沈殿を除くと生成物は出なかった。実験室での結果で、天然の噴出孔での再現ではない。 | なし（推奨：「CO2をギ酸に還元」と生成物を明記） | https://www.pubmed.gov/32900930/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7502746 |
| F08r | 確認済み | Bristol 大学（2025年12月3日）：Kay ら Nature「Dated gene duplications elucidate the evolutionary assembly of eukaryotes」。複雑化の過程は約29億年前に始まり、ミトコンドリアは予想よりかなり後に生じた。ラベル「仮説」は妥当。 | なし | https://www.bristol.ac.uk/news/2025/december/complex-life-developed-earlier-than-previously-thought-new-study-reveals.html |
| F09r | 修正要 | Knoll 2011（Annu Rev Earth Planet Sci 39, DOI 10.1146/annurev.earth.031208.100209）の要旨は「複雑な多細胞生物は6つの系統のみ（only six clades）：動物、陸上植物、真正紅藻、コンブ目の褐藻、菌類の2群」。「少なくとも6つ」は原文の「6つのみ」と向きが逆。 | 「Knoll（2011）によれば、複雑な多細胞生物は、動物、陸上植物、紅藻（真正紅藻類）、褐藻（コンブ類）、菌類の2群の6つの系統で独立に生じた。単純な多細胞性はこれよりはるかに多くの回数生じている。」 | https://annualreviews.org/doi/pdf/10.1146/annurev.earth.031208.100209 |
| F12r | 修正要 | 前半（原因の候補と重みの論争）は Wood ら 2019 と Zhang & Shu 2021 で支えられる。後半の「単一の原因では説明できないという点はおおむね一致している」は、Zhang & Shu 自身の結論（"No simple, single cause can explain the entire phenomenon"）であり、研究者全体の合意を示す記述はこの2本にない。 | 後半を「Zhang と Shu（2021）は、単一の原因では全体を説明できないと結論している。Wood ら（2019）も、環境の変化と生物の相互作用が重なって一連の放散が起きたと論じた。」に変更。 | https://link.springer.com/article/10.1007/s12542-021-00568-5 ; https://research-portal.st-andrews.ac.uk/en/publications/integrated-records-of-environmental-change-and-evolution-challeng/ |
| F18r | 確認済み | Marshall 2023：5大絶滅は統計的に別のものではなく、最大から最小まで連続している。Raup の上限推定96%に対し、Stanley 2016 の希薄化法による種レベルの推定は81%（"still ferociously high but is not 96%"）。 | なし | https://cambridge.org/core/journals/cambridge-prisms-extinction/article/forty-years-later-the-status-of-the-big-five-mass-extinctions/D8B7C1C298686D3622273320E778D22A |
| F32r | 確認済み | Zhang & Shu 2021：分子時計は後生動物と左右相称動物の起源を化石より数千万〜数億年古く推定。化石化による見かけという解釈がある一方で、Daley ら 2018 の「エディアカラ紀の保存条件はカンブリア紀に劣らない」を紹介。初期の動物は小さく痕跡を残せなかったという説明（Valentine と Erwin）も挙げている。 | なし | https://link.springer.com/article/10.1007/s12542-021-00568-5 |
| N01 | 確認済み | ビクトリア博物館：1969年9月28日、メルボルンの北約160kmにあるビクトリア州マーチソン上空で爆発し落下。 | なし（推奨：出典を src.martins2008 から、落下を明記した Museums Victoria に変える） | https://museumsvictoria.com.au/article/the-murchison-meteorite/ |
| N02 | 確認済み | NOAA「The Atmosphere」（JetStream）：乾燥大気の窒素 78.084%、酸素 20.946%。「約21%」は妥当。乾燥大気での値である点に注意。 | なし（出典：NOAA JetStream「The Atmosphere」。推奨：「乾燥した空気の」と補う） | https://www.noaa.gov/jetstream/atmosphere |
| N03 | 確認済み | Nature 285:198 の所属：Smit はアムステルダムの地質学研究所（オランダ）、Hertogen はルーヴェン（ベルギー）。「オランダの研究者を含む」は正しい。Alvarez らはカリフォルニア大学バークレー校（米国）。 | なし（推奨：「オランダとベルギーの研究者」と書く方が正確） | https://www.nature.com/articles/285198a0 ; https://ntrs.nasa.gov/citations/19800051929 |
| N04 | 確認済み | Oxford：オックスフォード大学が主導し、UCバークレー、ETHチューリッヒ、イェール大学が参加。EurekAlert：Science Advances、2026年10月2日掲載。 | なし | https://www.ox.ac.uk/news/2026-09-23-new-study-suggests-animals-may-have-evolved-vastly-earlier-than-fossil-evidence ; https://www.eurekalert.org/news-releases/1145493 |
| N05 | 修正要 | 査読論文の出典として Barnosky ら 2011（Nature 471:51–57）「約35億年間に進化した推定40億種のうち、約99%（some 99%）が消えた」を見つけた。英国自然史博物館は「約98%」とする。「99%以上」は資料の値より強い。推定値であり、ラベル「理論」より「推定（理論）」の性格を明記すべき。 | 「これまで地球に現れた種のほとんど（推定で約99%）は、すでに絶滅している（Barnosky ら 2011）。」出典：Barnosky ら 2011。 | https://ib.berkeley.edu/labs/barnosky/Barnosky%20et%20al%20Sixth%20Extinction%20Nature.pdf ; https://www.nature.com/articles/nature09678 ; https://www.nhm.ac.uk/discover/what-is-mass-extinction-and-are-we-facing-a-sixth-one |
| N06 | 確認済み | JPL（2025年9月10日）：試料はチェヤバ滝の岩石から「昨年」（＝2024年）採取。チェヤバ滝の発見は2024年7月。 | なし | https://www.jpl.nasa.gov/news/nasa-says-mars-rover-discovered-potential-biosignature-last-year/ |
| N07 | 修正要 | エディアカラ生物群の最古の化石（ミステイクン・ポイント）が少なくとも5.74億年前、地球の年齢 45.4億年（USGS）、570/4540 ≈ 1/8 の計算は正しい。しかし「目に見える大きさの複雑な生物の化石はエディアカラ生物群から現れる」は誤り。中国・高于荘層の約15.6億年前の地層から最大30cmの多細胞真核生物の化石（Zhu ら 2016, Nature Communications）があり、エディアカラ紀初期の藍田生物群（Yuan ら 2011, Nature）もアヴァロン生物群より古い。 | 「動物らしい大型の化石は、約5.7億年前のエディアカラ生物群から現れる。これは地球の歴史（約45.4億年）の最後の約8分の1にあたる。肉眼で見える大きさの多細胞の真核生物の化石は、もっと古い約15.6億年前の地層（中国華北）からも見つかっている。」 | https://mun.ca/marcomm/news-releases/archive/2019-2020/new-study-confirms-newfoundland-as-home-to-worlds-oldest-animal-fossils.php ; https://pubs.usgs.gov/gip/geotime/age.html ; https://ui.adsabs.harvard.edu/abs/2016NatCo...711500Z ; https://ui.adsabs.harvard.edu/abs/2011Natur.470..390Y |

## 件数集計

| 判定 | 件数 |
|---|---|
| 確認済み | 11 |
| 修正要 | 4（F09r, F12r, N05, N07） |
| 根拠不足 | 0 |
| 出典不在 | 0 |
| 合計 | 15 |

## 全体を通じて気づいた系統的な問題

1. **修正文で原文の強さが変わる**：F09r（原文「6系統のみ」を「少なくとも6」）、N05（約99%を「99%以上」）。修正のときも原文の限定語（only, some, about）を保つこと。
2. **一つの論文の結論を「おおむね一致」と一般化**：F12r。合意を述べるには、総説か複数の立場の文献が必要。
3. **教材のために足した「やさしい一般化」に誤りが入りやすい**：N07（大型の化石はエディアカラから）。導入の一文も、他の主張と同じ水準で出典を確認すること。
4. **出典IDと主張の対応がずれている**：N01 は src.martins2008 を出典にしているが、落下地点を書いた資料ではない。主張ごとに、その内容を直接書いた資料を出典にすること。

---

<!-- verification_2b.md -->
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
