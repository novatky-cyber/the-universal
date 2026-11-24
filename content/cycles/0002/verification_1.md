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
