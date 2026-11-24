# R3 history：地球と生命の共進化・生命史の転換点（サイクル 0002）

- 担当：Researcher R3（history）
- 調査日：2026-11-24（WebSearch／WebFetch で確認した内容のみ記載。年代は ICS 国際年代層序表 v2024/12 を優先）
- 中心の問い（歴史側）：生命史の大きな転換点は何で、原因はどこまで分かっているか
- 表記：Ga＝10億年前、Ma＝100万年前、ka＝1000年
- 注意：pmc.ncbi.nlm.nih.gov と pubmed.ncbi.nlm.nih.gov の一部ページは取得できなかった（閲覧許可の要求が時間切れ。対象：PMC7289717、PMC5677351、pubmed 22891323、news.mit.edu 2014/an-extinction-in-the-blink-of-an-eye-0210）。代わりに同じ論文の別の所蔵先（MIT DSpace、St Andrews、USGS など）で確認した。

---

## A. 年代の物差し

## 主張 R1
- 内容：ICS の国際年代層序表の最新版は v2024/12。この表では、カンブリア紀の始まりは 538.8 ± 0.6 Ma、エディアカラ紀の始まりは約635 Ma、クリオジェニアン紀の始まりは約720 Ma、オルドビス紀は 486.85 ± 1.5 Ma、デボン紀は 419.62 ± 1.36 Ma、三畳紀は 251.902 ± 0.024 Ma、ジュラ紀は 201.4 ± 0.2 Ma、古第三紀（白亜紀の終わり）は 66.00 Ma。原生代前半の区分（シデリアン紀 2500 Ma、リアキアン紀 2300 Ma、オロシリアン紀 2050 Ma）は地層の模式地（GSSP）ではなく、年代値（GSSA）で定義されている。
- ラベル：事実（国際的な取り決めとしての年代値）
- 確信度：high（ただしPDFから読み取った値。シルル紀・フラニアン期などは対応関係の読み取りに不確かさがあるため、ここでは使わない）
- 出典：International Chronostratigraphic Chart v2024/12｜International Commission on Stratigraphy｜2024｜https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf
- 関連ノード：evt.cambrian、evt.kpg、evd.radiometric-dating
- 補足：「～」付きの値は暫定値。年代表は数年ごとに改訂されるため、教材では版（v2024/12）を明記する。

---

## B. 大酸化イベント（GOE）と酸素発生型光合成

## 主張 R2
- 内容：Poulton ら（2021, Nature）は、南アフリカのトランスバール超層群のボーリングコアの硫黄同位体（MIF-S、硫黄同位体の質量に依存しない分別。大気に酸素がほとんどないときにだけ残る信号）を分析した。その結果、GOEは約24.3億年前に始まり、大気の酸素は約2億年にわたって増減を繰り返し、恒常的に定着したのは約22.2億年前だったと推定した。それまでの通説（約23.2億年前に定着）より約1億年遅い。著者らはこの期間を「大酸化エピソード（Great Oxidation Episode）」と呼び直した。
- ラベル：理論（硫黄同位体という代理指標にもとづく推定）
- 確信度：medium-high（MIF-S は頑健な指標と評価されている。一方で、増減を起こした仕組みは未解明）
- 出典：Extra 100 million years before Earth saw permanent oxygen rise｜University of Leeds｜2021-03-29｜https://www.leeds.ac.uk/news/article/4797/extra-100-million-years-before-earth-saw-permanent-oxygen-rise ／ Timing of Earth's oxygenation may need a 100-million-year revision｜Eos (AGU)｜2021｜https://eos.org/articles/timing-of-earths-oxygenation-may-need-a-100-million-year-revision ／ 論文：Poulton et al., Nature (2021) doi:10.1038/s41586-021-03393-7｜https://link.springer.com/10.1038/s41586-021-03393-7
- 関連ノード：evt.goe
- 補足：GOEは一瞬の出来事ではなく、約2億年かけた揺れ動く移行だった。この点が、既存の evt.goe の「約24億年前」という一点の書き方と食い違う。

## 主張 R3
- 内容：Warke ら（2020, PNAS）は、GOEの開始を約25.0〜24.3億年前に絞り込み、GOEが最初の全球凍結（約24.2億年前）より前に起きたと結論した。
- ラベル：理論
- 確信度：medium
- 出典：Snowball's chance in Earth and early signs of life｜University of St Andrews｜2020-06-01｜https://news.st-andrews.ac.uk/archive/snowballs-chance-in-earth-and-early-signs-of-life/
- 関連ノード：evt.goe、新規候補 evt.snowball-earth
- 補足：大学の広報で確認した（原著は未取得）。「酸素の増加がメタン温室を弱め、凍結を引き起こした」という因果の筋書きを支持する材料だが、因果そのものを証明したわけではない。

## 主張 R4
- 内容：総説（Lyons, Reinhard & Planavsky 2014, Nature）は、次の点をまとめている。(1) 酸素発生型光合成の始まりの推定には約38億〜23.5億年前という大きな幅があり、論争中である。初期のシアノバクテリアや真核生物を示すとされたバイオマーカーには、汚染の疑いがある。(2) 硫黄の MIF 信号が消えることから、大気が酸化に転じたのは約24〜23億年前に絞られる。(3) GOEは長く揺れ動く移行だった。
- ラベル：論争（光合成の始まり）／理論（GOEの年代）
- 確信度：high（総説としての整理）
- 出典：The rise of oxygen in Earth's early ocean and atmosphere｜Nature 506:307–315｜2014｜https://people.earth.yale.edu/sites/default/files/files/Planavsky/30_%20Lyons%20et%20al%20Nature%202014.pdf （doi:10.1038/nature13068）
- 関連ノード：evt.goe
- 補足：その後の研究でも、決着はついていない（2014年以降の文献は今回網羅していない）。

## 主張 R5
- 内容：Planavsky ら（2014, Nature Geoscience）は、南アフリカ・ポンゴラ超層群の約29.5億年以上前の地層でモリブデン同位体を分析し、浅い海ではGOEの約5億年前から光合成による酸素がたまり始めていたと推定した。
- ラベル：仮説（有力な証拠の一つ）
- 確信度：medium
- 出典：Evidence for oxygenic photosynthesis half a billion years before the Great Oxidation Event｜Nature Geoscience 7:283–286｜2014｜https://www.nature.com/articles/ngeo2122
- 関連ノード：evt.goe
- 補足：「光合成の始まり」と「大気の酸化（GOE）」は別の出来事であり、その間に数億年の遅れがあった可能性が高い。

## 主張 R6
- 内容：酸素の生産が始まってから大気に酸素がたまるまでに遅れがあったことは、主に次のように説明されている。火山から出る還元的なガス（水素・硫黄・鉄など）が酸素を消費していたが、やがて生産が消費を上回った。補助的な要因として、水素の宇宙への散逸や、海底火山から陸上火山への比重の移行が挙げられている。
- ラベル：理論（複数の要因の組み合わせ）
- 確信度：medium
- 出典：Lyons et al. 2014（R4と同じ）
- 関連ノード：evt.goe
- 補足：GOEを「生命が酸素を出したから」の一因に単純化しない（品質基準4）。酸素の生産（生物）と消費（地質）のつり合いの問題として説明する。

## 主張 R7
- 内容：GOEのあと、原生代中期（約18〜8億年前）には大気の酸素が低いまま長く続き、深海はほぼ無酸素だった。これは「退屈な10億年（boring billion）」と呼ばれる。酸素の再上昇は原生代末（エディアカラ紀ごろ）とされるが、時期の制約は弱い。著者らは、動物の進化と酸素量を結びつける議論が循環論法に陥る危険を指摘している。
- ラベル：理論（酸素が低かったこと）／論争（再上昇の時期と動物との因果）
- 確信度：medium
- 出典：Lyons et al. 2014（R4と同じ）
- 関連ノード：新規候補 con.boring-billion（下記参照）、evt.cambrian
- 補足：「酸素が増えたから動物が現れた」という単線的な説明は、慎重に扱う必要がある。

---

## C. 全球凍結（スノーボールアース）

## 主張 R8
- 内容：クリオジェニアン紀（約7.2〜6.35億年前）には、赤道付近まで氷が達した氷河期が少なくとも2回あった（スターティアン氷河期とマリノアン氷河期）。Rooney ら（2014, PNAS）はスターティアン氷期の直後の地層を 662.4 ± 3.9 Ma と年代測定し、既存の U-Pb 年代と合わせて、スターティアン氷期が約5500万年続いたことを示した。氷が赤道に達したのは「717〜635 Ma」の間とされる。
- ラベル：理論（年代は測定値、全球凍結という解釈は有力仮説）
- 確信度：high（年代）／medium（完全な凍結か、部分的に海が開いていたか）
- 出典：Re-Os geochronology and coupled Os-Sr isotope constraints on the Sturtian snowball Earth｜PNAS 111(1):51–56｜2014｜https://durham-repository.worktribe.com/output/1473458
- 関連ノード：新規候補 evt.snowball-earth
- 補足：マリノアン氷期の終わりは約6.35億年前で、エディアカラ紀の始まり（ICS 約635 Ma）と一致する。マリノアン氷期の始まりの年代は、今回は一次資料で確認できていない（Britannica は「クリオジェニアン紀の最後の約1500万年」と記述）。

## 主張 R9
- 内容：Britannica によれば、クリオジェニアン紀は約7.2〜6.35億年前。スターティアン氷期は最初の5000万〜6000万年、マリノアン氷期は最後の約1500万年を占め、その間に短い間氷期があった。全球凍結の間、生命は熱水噴出孔のまわり、火山近くの融け水、氷の割れ目から光が届く浅い海などで生き延びた可能性がある。
- ラベル：理論（百科事典による整理）
- 確信度：medium
- 出典：Cryogenian Period｜Encyclopaedia Britannica｜（閲覧 2026-11-24）｜https://www.britannica.com/science/Cryogenian-Period
- 関連ノード：新規候補 evt.snowball-earth
- 補足：「完全に凍った（hard snowball）」か「一部に海が開いていた（slushball など）」かは論争がある【この論争の具体的な文献は未確認】。

## 主張 R10
- 内容：古原生代にも全球凍結に相当する氷河期があった（マクガニエネ氷河期／ヒューロニアン氷河期、約24〜21億年前。北米の記録ではゴウガンダ層が約23億年前）。Poulton ら（2021）は、24.3〜22.2億年前の間に複数回の氷河期があり、そのうち3回が酸素量の増減と対応すると報告している。
- ラベル：理論
- 確信度：medium
- 出典：20.6 When were the Snowballs?｜Historical Geology (Bentley et al.), OpenGeology / LibreTexts｜https://geo.libretexts.org/Bookshelves/Geology/Historical_Geology_(Bentley_et_al.)/20%3A_(Case_Study)_Snowball_Earth_glaciations/20.06%3A_When_were_the_Snowballs ／ Eos 2021（R2と同じ）
- 関連ノード：新規候補 evt.snowball-earth、evt.goe
- 補足：LibreTexts は大学の教科書で、一次資料を引用していない。年代の幅はおおよその目安として扱う。古原生代の氷河期が本当に「全球」凍結だったかには異論もある【未確認】。

---

## D. 真核生物と多細胞化

## 主張 R11
- 内容：中国科学院南京地質古生物研究所の報告（Miao, Yin, Knoll, Qu, Zhu ら, 2024, Science Advances）によると、議論の余地のない最古の真核生物の化石は単細胞で、約16.5億年前（華北・北オーストラリア）。華北の川林溝（Chuanlinggou）層からは、約16.3億年前の多細胞の真核生物 *Qingshania magnifica*（細胞が2〜20個以上つながった糸状体）が報告された。これは多細胞化の最古記録を約7000万年さかのぼらせる。それまで確かとされた単純な多細胞化石は約10.5億年前だった。
- ラベル：事実（化石の年代）／仮説（*Qingshania* の分類上の位置。藻類の可能性が高いが確定していない）
- 確信度：medium-high
- 出典：Fossils from North China indicate eukaryotes first acquired multicellularity by 1.63 billion years ago｜NIGPAS, CAS｜2024-01-24｜https://english.nigpas.cas.cn/new/hs/rp/202401/t20240124_656672.html
- 関連ノード：新規候補 evt.eukaryotes、新規候補 evt.multicellularity
- 補足：中国の研究機関による発見であり、地域の偏りを補う例として使える。これより古い多細胞化石の主張には論争がある。

## 主張 R12
- 内容：Brocks ら（2023, Nature）は、北オーストラリアの約16億年前の岩石から、初期の真核生物に由来する分子化石（プロトステロール）を見つけた。この「プロトステロール生物群（Protosterol Biota）」は約16億年前から約8億年前まで広く存在し、その後の「トニアン変革（Tonian Transformation）」で現生型の真核生物に置き換わったとされる。
- ラベル：理論（分子化石の解釈）
- 確信度：medium
- 出典：Scientists discover 'lost world' of our earliest ancestors｜Australian National University｜2023-06-08｜https://www.anu.edu.au/news/all-news/scientists-discover-lost-world-of-our-earliest-ancestors ／ 論文 PDF：https://www.nature.com/articles/s41586-023-06170-w.pdf
- 関連ノード：新規候補 evt.eukaryotes
- 補足：「最初の捕食者だったかもしれない」という記述は広報上の推測にとどまる。

## 主張 R13
- 内容：Kay ら（2025-12-03, Nature）は、遺伝子重複の年代を分子時計で推定した。その結果、真核生物の複雑な細胞の形成（真核生物化）は約29億年前に始まり、核などの内部構造がミトコンドリアより先に現れたとした（「CALM＝Complex Archaeon, Late Mitochondrion」シナリオ）。ミトコンドリアの獲得は大気の酸素の最初の大きな増加と同時期だったとしている。
- ラベル：仮説（新しい分子時計の推定。化石の裏付けはない）
- 確信度：low-medium（単一の研究。他の推定より約10億年古い）
- 出典：Complex life developed earlier than previously thought, new study reveals｜University of Bristol｜2025-12｜https://www.bristol.ac.uk/news/2025/december/complex-life-developed-earlier-than-previously-thought-new-study-reveals.html ／ 論文情報：Dated gene duplications elucidate the evolutionary assembly of eukaryotes｜Nature｜2025-12-03｜https://www.nature.com/nature-index/article/10.1038/s41586-025-09808-z （doi:10.1038/s41586-025-09808-z）
- 関連ノード：新規候補 evt.eukaryotes、新規候補 thy.endosymbiosis（R2 の担当）
- 補足：真核生物の起源の推定には、化石（約16.5億年前）、分子時計（17〜18億年前前後から29億年前まで）と大きな幅がある。これは「分からない」状態の典型例として教材で扱える。

## 主張 R14
- 内容：複雑な多細胞化（細胞の分化や組織を持つもの）は、少なくとも6回独立に起きた。動物、陸上植物（緑藻の系統から）、紅藻、褐藻（巨大なケルプを含む）、菌類（少なくとも2回）である。単純な多細胞化はもっと多くの系統で起きており、独立に生じた回数の推定は「ほぼ確実に過小評価」とされる。
- ラベル：事実（複数回独立に起きたこと）／未知（正確な回数）
- 確信度：high（複数回であること）／medium（「6回」という数）
- 出典：28.1 The phylogenetic distribution of multicellular organisms｜Macmillan Learning の大学生物学教科書（書名はページ上で確認できず）｜https://digfir-published.macmillanusa.com/hlw/hlw_ch28_2.html ／ Tong, Bozdag & Ratcliff, Selective drivers of simple multicellularity｜Current Opinion in Microbiology 67｜2022｜https://par.nsf.gov/servlets/purl/10322817
- 関連ノード：新規候補 evt.multicellularity
- 補足：「多細胞化は一度きりの奇跡」という見方は誤り。収斂（独立に似た性質が生じること）の例になる。

---

## E. エディアカラ紀とカンブリア紀

## 主張 R15
- 内容：カナダ・ニューファンドランド島のミステイクン・ポイントにある、最古のエディアカラ生物群の化石は少なくとも5億7400万年前のもの（Matthews ら 2020, GSA Bulletin。年代の誤差は約65万年）。約5億6800万年前には、より複雑な生物と、筋肉を使った移動の最古の証拠が現れる。
- ラベル：事実（年代測定）
- 確信度：high
- 出典：New study confirms Newfoundland as home to world's oldest animal fossils｜Memorial University of Newfoundland｜2020-07-30｜https://mun.ca/marcomm/news-releases/archive/2019-2020/new-study-confirms-newfoundland-as-home-to-worlds-oldest-animal-fossils.php
- 関連ノード：新規候補 evt.ediacaran-biota、evt.cambrian
- 補足：エディアカラ生物の多くは、現生の動物門との関係がはっきりしない（R16の総説）。「最古の動物化石」という呼び方自体にも議論がある。

## 主張 R16
- 内容：Zhang & Shu（2021, PalZ）の総説によると、左右相称動物の主な系統の多くは、カンブリア紀の最初の約2000万年で化石記録に現れる。生痕化石（はい跡など）には段階があり、フォーチュニアン期（約538.8〜529 Ma）に多様性が急増し、続く約529〜509 Ma に再び多様化して、より深い堆積物へのもぐり込みが現れる。著者らは、カンブリア爆発を一度の瞬間的な爆発ではなく、段階的で、単一の原因では説明できない出来事と位置づけている。
- ラベル：理論（現象の記述）／論争（速さと原因）
- 確信度：medium-high
- 出典：Current understanding on the Cambrian Explosion: questions and answers｜PalZ 95:641–660｜2021｜https://link.springer.com/article/10.1007/s12542-021-00568-5
- 関連ノード：evt.cambrian
- 補足：著者は中国・西北大学の研究者で、中国の化石産地の知見が厚い。

## 主張 R17
- 内容：分子時計は、動物の起源を最初の化石より数千万〜数億年前と推定することが多い。カンブリア爆発の「突然さ」の一部は、化石が残りやすくなったこと（硬い殻の獲得、保存条件の変化）による見かけである可能性がある。一方で、分子時計は系統的に古すぎる推定を出しやすいという批判もある。
- ラベル：論争
- 確信度：medium
- 出典：Zhang & Shu 2021（R16と同じ）／ 批判側の例として、Survival and selection biases in early animal evolution and a source of systematic overestimation in molecular clocks｜（検索結果で題名を確認、本文は未取得）｜https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333906/
- 関連ノード：evt.cambrian、新規候補 evd.molecular-phylogeny
- 補足：批判側の論文は題名しか確認していない。教材で使う場合は本文を照合すること。

## 主張 R18
- 内容：Durbin, Anderson ら（2026-10-02, Science Advances）は、分子時計の「最大年代」の較正点を見直した。新たに8.5〜7.3億年前の化石産地（スヴァンベリフェレット、ビター・スプリングス、チュアーなど）を較正に用い、それまでのエディアカラ紀の甕安（Weng'an）生物群による制約に置き換えた。その結果、動物の起源を8億〜7億年前と推定した（従来より約2億年古い）。モンゴルのケシーン生物群の微化石140試料以上も調べたが、動物と確定できるものはなかった。著者ら自身が「8億年前に動物がいたことの証明ではない」と述べている。
- ラベル：仮説
- 確信度：low-medium（推定の前提である較正点の選び方に依存する）
- 出典：New study suggests animals may have evolved vastly earlier than fossil evidence suggests｜University of Oxford｜2026-09-23（ニュース URL の日付）／ EurekAlert! 2026-10-02｜https://www.ox.ac.uk/news/2026-09-23-new-study-suggests-animals-may-have-evolved-vastly-earlier-than-fossil-evidence ／ https://www.eurekalert.org/news-releases/1145493 ／ 論文：Re-evaluating molecular clock maximum age calibrations revives pre-Ediacaran divergence estimates for animals｜doi:10.1126/sciadv.aeg6289
- 関連ノード：evt.cambrian、新規候補 evd.molecular-phylogeny
- 補足：時事候補（下記）。分子時計と化石の食い違いを示す、最新の具体例になる。

## 主張 R19
- 内容：澄江（チェンジャン）化石産地（中国雲南省）は、約5.2億年前（カンブリア紀前期）の海の生物群を、軟らかい組織まで含めて保存している。カンブリア紀前期の海洋生物群集としては最も完全な記録とされる。最古級の脊索動物を含み、少なくとも16〜20門・196〜300種以上が知られる（IUCN の評価文書の中でも数値に幅がある）。2012年に世界遺産に登録された。
- ラベル：事実
- 確信度：high（年代・登録）／medium（種数）
- 出典：Chengjiang Fossil Site｜IUCN World Heritage Outlook｜https://worldheritageoutlook.iucn.org/node/1170
- 関連ノード：evt.cambrian、新規候補 evd.fossil-record
- 補足：地域の偏りを補う（欧米の産地だけでカンブリア爆発を語らない）。

## 主張 R20
- 内容：バージェス頁岩（カナダ、ヨーホー国立公園）はカンブリア紀中期（約5億1000万〜5億500万年前）の化石産地で、1909年に C. D. ウォルコットが発見した。軟体性の生物を保存しており、*Pikaia*、*Anomalocaris* などが知られる。カナディアン・ロッキー山脈自然公園群として世界遺産になっている。
- ラベル：事実
- 確信度：high
- 出典：Burgess Shale Fossils｜The Canadian Encyclopedia｜https://www.thecanadianencyclopedia.ca/en/article/burgess-shale-fossils
- 関連ノード：evt.cambrian、新規候補 evd.fossil-record
- 補足：グールド『ワンダフル・ライフ』をめぐる偶然性と収斂の論争は、この資料では確認していない【未確認】。

---

## F. 陸上への進出

## 主張 R21
- 内容：陸上植物の最古の確実な証拠は胞子化石（クリプトスポア）である。Rubinstein ら（2010, New Phytologist）は、アルゼンチンのオルドビス紀中期ダピンギアン期（約4.73〜4.71億年前）の地層から5属を含むクリプトスポアを報告し、それまでの最古記録（約4.63〜4.61億年前、サウジアラビア・チェコ）を約800万〜1200万年さかのぼらせた。著者らは、陸上植物がゴンドワナ大陸で生まれた可能性、そして起源はさらに古い（オルドビス紀前期またはカンブリア紀）可能性を示唆している。
- ラベル：事実（胞子の年代）／仮説（起源の場所と時期）
- 確信度：medium-high
- 出典：Early Middle Ordovician evidence for land plants in Argentina (eastern Gondwana)｜New Phytologist 188(2):365–369｜2010｜https://repositoriosdigitales.mincyt.gob.ar/vufind/Record/CONICETDig_ac9305178331702ab005dfd0f9345ccf
- 関連ノード：新規候補 evt.land-colonization
- 補足：植物の体の化石（大型化石）が現れるのはシルル紀以降で、それより前の証拠は胞子に頼る。

## 主張 R22
- 内容：Morris ら（2018, PNAS）は、化石と分子を組み合わせた年代推定により、陸上植物の起源をカンブリア紀中期〜オルドビス紀前期（約5.15億〜4.7億年前）、維管束植物の起源をオルドビス紀後期〜シルル紀と推定した。
- ラベル：理論
- 確信度：medium
- 出典：The timescale of early land plant evolution｜PNAS 115(10):E2274｜2018｜https://ui.adsabs.harvard.edu/abs/2018PNAS..115E2274M
- 関連ノード：新規候補 evt.land-colonization
- 補足：ADS の要旨で確認した。年代は「約5.1億〜4.8億年前」とまとめられていた。

## 主張 R23
- 内容：四肢動物への移行の中間形である *Tiktaalik roseae*（約3億7500万年前、カナダ北極圏のエルズミーア島）は、ひれと鱗を持つ一方で、首・肋骨・肢のようなひれの骨を持っていた（Daeschler, Shubin, Jenkins 2006, Nature）。
- ラベル：事実
- 確信度：high
- 出典：University of Chicago Chronicle｜2006-04-13｜https://chronicle.uchicago.edu/060413/fossils.shtml
- 関連ノード：新規候補 evt.land-colonization、新規候補 evd.fossil-record
- 補足：*Tiktaalik* は「祖先そのもの」ではなく、中間的な特徴を持つ近縁の系統（エルピストステゲ類）の一例として扱う。

## 主張 R24
- 内容：ポーランドのザヘウミェ（Zachelmie）採石場で見つかった四肢動物の足跡は、約3億9500万年前（デボン紀中期のはじめ）のもので、骨格化石にもとづく四肢動物の出現（約3.8億年前）より約1800万年古い（Niedźwiedzki ら 2010, Nature）。この発見により、エルピストステゲ類と四肢動物が少なくとも1000万年共存したことになり、移行が浅い海の潮間帯で起きた可能性も示された。
- ラベル：事実（足跡の年代）／論争（足跡の解釈と、移行が起きた環境）
- 確信度：medium
- 出典：Fossil footprints give land vertebrates a much longer history｜Uppsala University｜2010-01-07｜https://www.uu.se/en/press/press-releases/2009/2010-01-07-fossil-footprints-give-land-vertebrates-a-much-longer-history
- 関連ノード：新規候補 evt.land-colonization
- 補足：化石記録の空白が、出来事の順序の推定を左右するよい例になる。

---

## G. ビッグファイブ大量絶滅

## 主張 R25
- 内容：Barnosky ら（2011, Nature）にもとづく整理では、5大絶滅は次のとおり。オルドビス紀末（約4.44億年前、種の約86%）、デボン紀後期（約3.6億年前、約75%）、ペルム紀末（約2.5億年前、約96%）、三畳紀末（約2億年前、約80%）、白亜紀末（約6500万年前、約76%）。
- ラベル：理論（推定値）
- 確信度：medium（種の喪失率の推定は方法によって大きく変わる。R26参照）
- 出典：Mass extinctions｜Our World in Data（Barnosky et al. 2011 Nature 471:51–57 にもとづく表）｜https://ourworldindata.org/mass-extinctions
- 関連ノード：新規候補 con.mass-extinction、evt.kpg
- 補足：年代は ICS v2024/12 と少しずれる（白亜紀末は 66.0 Ma が正確）。教材では ICS の値に統一する。

## 主張 R26
- 内容：Marshall（2023, Cambridge Prisms: Extinction）は「5大絶滅」の考え方を再検討した。補正したデータでは、5つの絶滅は互いに、また平常時の絶滅（背景絶滅）とも統計的にはっきり区別できず、連続した分布の上位にすぎないので、「5つ」を特別扱いするのはやや恣意的だと論じた。ペルム紀末の種の喪失率も、従来の上限96%から81%（Stanley 2016）へ下方修正されている（属レベルでは56〜69%）。デボン紀後期は短い一回の絶滅ではなく、長い絶滅期間とみなすべきだとしている。
- ラベル：論争
- 確信度：medium
- 出典：Forty years later: The status of the "Big Five" mass extinctions｜Cambridge Prisms: Extinction 1, e5｜2023｜https://cambridge.org/core/journals/cambridge-prisms-extinction/article/forty-years-later-the-status-of-the-big-five-mass-extinctions/D8B7C1C298686D3622273320E778D22A
- 関連ノード：新規候補 con.mass-extinction
- 補足：「ビッグファイブ」は便利な枠組みだが、自然にある区切りというより、研究者が選んだ区切りという面がある。

## 主張 R27
- 内容：オルドビス紀末の大量絶滅（ヒルナンティアン期、約4.45億年前）では海の生物種の約85%が失われ、2つの段階（パルス）で起きたとされる。ゴンドワナ大陸の氷河の発達と後退、それに伴う海水準の変化、寒冷化、大陸棚の無酸素化が原因として挙げられている（Kozik ら 2021, AGU Advances）。一方、Wang ら（2019, Earth-Science Reviews）は、1回の急激な絶滅とその後の長い回復とみなす解釈を提案している。
- ラベル：理論（気候との関連）／論争（1段階か2段階か）
- 確信度：medium
- 出典：What conditions accompanied the Late Ordovician mass extinction?｜Eos Editors' Highlight｜2022｜https://eos.org/editor-highlights/what-conditions-accompanied-the-late-ordovician-mass-extinction ／ The end-Ordovician mass extinction: A single-pulse event?｜Earth-Science Reviews 192:15｜2019｜https://ui.adsabs.harvard.edu/abs/2019ESRv..192...15W
- 関連ノード：新規候補 con.mass-extinction
- 補足：寒冷化による大量絶滅の例であり、「大量絶滅＝温暖化」という一般化への反例になる。著者名の「Wang」は書誌コードから推測したもの【未確認】。

## 主張 R28
- 内容：デボン紀後期の絶滅は、主に2つの出来事からなる。ケルワッサー事変（約3億7220万年前、フラニアン期とファメニアン期の境界）と、ハンゲンベルク事変（デボン紀末、約3.59億年前）である。両者を合わせて動物種の約70〜80%が失われたが、5大絶滅の中では最も規模が小さい。原因の候補は、海底の無酸素化（黒色頁岩に記録）、根を持つ陸上植物の拡大による栄養塩の流入、寒冷化、衝突（スウェーデンのシリヤン・クレーター、約3.77億年前）などで、単一の原因は確定していない。
- ラベル：論争（原因）
- 確信度：medium
- 出典：Devonian extinctions｜Encyclopaedia Britannica｜https://www.britannica.com/science/Devonian-extinctions
- 関連ノード：新規候補 con.mass-extinction、新規候補 evt.land-colonization
- 補足：陸上植物の進出が海の絶滅につながったかもしれないという、地球と生命の共進化の例になる（仮説）。

## 主張 R29
- 内容：ペルム紀末の大量絶滅は、中国・浙江省の煤山（Meishan）の火山灰層を U-Pb ジルコン法で年代測定した結果、251.941 ± 0.037 Ma から 251.880 ± 0.031 Ma の間、つまり 60 ± 48 ka という地質学的には非常に短い間に起きた（Burgess, Bowring & Shen 2014, PNAS）。
- ラベル：事実（測定値）
- 確信度：high
- 出典：High-precision timeline for Earth's most severe extinction｜PNAS 111(9):3316–3321｜2014｜https://dspace.mit.edu/handle/1721.1/91514
- 関連ノード：新規候補 evt.end-permian、新規候補 con.mass-extinction
- 補足：ICS の三畳紀の始まり（251.902 ± 0.024 Ma）は、この絶滅の時期と重なる。

## 主張 R30
- 内容：Burgess, Muirhead & Bowring（2017, Nature Communications）は、シベリア・トラップ（シベリアの巨大な洪水玄武岩の火山活動）が、地表に溶岩を流す段階から地下に水平に貫入するシル（岩床）の段階に移った時期が、ペルム紀末絶滅の始まりと一致すると報告した。シルの熱が揮発性物質に富む堆積岩を加熱し、大量の温室効果ガスを放出したことが絶滅の引き金になった、と論じている。Marshall（2023）は、具体的な殺傷の仕組みとして「温度に依存した低酸素（Penn ら 2018）」を挙げている。
- ラベル：理論（シベリア・トラップとの関連は広く支持されている）／仮説（シルが引き金という仕組み）
- 確信度：medium-high（関連）／medium（仕組み）
- 出典：Initial pulse of Siberian Traps sills as the trigger of the end-Permian mass extinction｜Nature Communications｜2017｜https://www.usgs.gov/publications/initial-pulse-siberian-traps-sills-trigger-end-permian-mass-extinction （doi:10.1038/s41467-017-00083-9）／ Marshall 2023（R26と同じ）
- 関連ノード：新規候補 evt.end-permian
- 補足：温暖化・海洋酸性化・無酸素化が重なった連鎖として説明され、現在の気候変動との類比がしばしば語られる。ただし速さと規模は異なり、類比には限界がある（推測）。

## 主張 R31
- 内容：三畳紀末の大量絶滅は、中央大西洋マグマ区（CAMP）の最初期の火山活動と同時に起きた。マグマの放出は約60万年の間に4回のパルスで起き、生物が回復している間も続いた（Blackburn ら 2013, Science）。Marshall（2023）は、CAMP に関連した無酸素化の危機が約5万年続いたとする研究（He ら 2020）を紹介している。
- ラベル：理論
- 確信度：medium-high
- 出典：Zircon U-Pb Geochronology Links the End-Triassic Extinction with the Central Atlantic Magmatic Province｜Science 340:941｜2013｜https://ui.adsabs.harvard.edu/abs/2013Sci...340..941B ／ Marshall 2023
- 関連ノード：新規候補 con.mass-extinction
- 補足：三畳紀末の絶滅のあと、ジュラ紀に恐竜が優勢になった。この因果の詳細は今回確認していない【未確認】。

## 主張 R32
- 内容：Alvarez, Alvarez, Asaro, Michel（1980, Science）は、白亜紀と第三紀の境界の粘土層でイリジウムが背景値の約30倍（イタリア）、約160倍（デンマーク）、約20倍（ニュージーランド）に濃集していることを示し、地球外からの原因（天体衝突）を提案した。同じ年に、Smit & Hertogen（1980, Nature）もスペインの地層から独立に同じ趣旨の結論を出している。
- ラベル：事実（測定）／歴史（学説の提唱）
- 確信度：high
- 出典：Extraterrestrial cause for the Cretaceous-Tertiary extinction（Science 208, 1980）｜NASA Technical Reports Server｜https://ntrs.nasa.gov/citations/19800051929 ／ An extraterrestrial event at the Cretaceous–Tertiary boundary｜Nature 285:198–200｜1980｜https://www.nature.com/articles/285198a0.pdf
- 関連ノード：evt.kpg
- 補足：「アルバレスだけが見つけた」という英雄物語にしない。独立に到達した研究があった。

## 主張 R33
- 内容：チクシュルーブ・クレーター（メキシコ、ユカタン半島）は、直径約180km、深さ約900mで、直径約10kmの小天体（小惑星説が優勢、彗星説もある）によってできた。約1kmの若い地層に埋もれている。1990年に NASA の研究者が衛星画像でセノーテ（陥没穴）の環に気づき、メキシコの石油会社の重力・磁気データと合わせた1991年の研究で、衝突地点として広く受け入れられた。2010年には41人の専門家による総説（Schulte ら, Science）が、チクシュルーブ衝突を大量絶滅の究極的な原因と結論し、硫酸塩に富む地層に衝突したことで硫黄エアロゾルが被害を強めたとした。
- ラベル：理論（科学的な合意が強い）
- 確信度：high
- 出典：A Smoking Gun for Dinosaur Extinction｜NASA JPL｜https://www.jpl.nasa.gov/news/a-smoking-gun-for-dinosaur-extinction/ ／ Alvarez theory on dinosaur die-out upheld｜Berkeley Lab｜2010-03-09｜https://newscenter.lbl.gov/2010/03/09/alvarez-theory-on-dinosaur/
- 関連ノード：evt.kpg
- 補足：JPL の記事は年代を「約6500万年前」と古い値で書いている。ICS と Renne 2013 の 66.0 Ma に統一する。

## 主張 R34
- 内容：Renne ら（2013, Science）は、⁴⁰Ar/³⁹Ar 法により、K-Pg 境界の大量絶滅と衝突が3万2000年以内で同時だったことを示した。そのうえで、衝突は「すでに臨界に近いストレスを受けていた生態系」の状態を転換させた可能性が高い、と述べている。Marshall（2023）は、K-Pg 境界の年代を 66.043 ± 0.043 Ma（2σ）としている。
- ラベル：事実（同時性）／理論（「ストレス下の生態系」という解釈）
- 確信度：high（同時性）／medium（事前のストレス）
- 出典：Time Scales of Critical Events Around the Cretaceous-Paleogene Boundary｜Science 339:684｜2013｜https://ui.adsabs.harvard.edu/abs/2013Sci...339..684R/abstract ／ Marshall 2023
- 関連ノード：evt.kpg
- 補足：「事前のストレス」の正体をデカン・トラップと見るかどうかが、R35・R36の論争につながる。

## 主張 R35
- 内容：インドのデカン・トラップの年代について、2019年の Science に2本の論文が出た。どちらも、噴火は衝突の約40万年前に始まり、K-Pg 境界の約60万年後まで続いたとする点では一致している。違いは次の点にある。Schoene ら（プリンストン）は4回の噴火のパルスを認め、最大のものは衝突の約10万年前だったとして、火山活動が衝突の前に生態系を弱らせた可能性を示した。Sprain ら（バークレー）はパルスを認めず、溶岩の約75%は衝突の後に噴出したと推定した。
- ラベル：論争
- 確信度：medium（報道による要約。原著は未取得）
- 出典：What actually killed the dinosaurs? Volcanoes heat up debate｜National Geographic｜2019-02｜https://www.nationalgeographic.com/science/article/what-actually-killed-dinosaurs-volcanoes-heat-up-debate
- 関連ノード：evt.kpg
- 補足：報道は単独では確信度 low だが、内容は2本の査読論文の要約である。教材で使う前に原著で照合する。

## 主張 R36
- 内容：Hull ら（2020, Science）は、海の化石の炭素同位体と気温の記録を気候モデルと比べ、デカン・トラップのガス放出の大半は衝突よりかなり前に起きていたと結論した。火山活動は約2℃の緩やかな温暖化をもたらしたが、大量絶滅は起こさず、絶滅の原因は衝突だけだったとしている。
- ラベル：論争（衝突単独説の側の有力な研究）
- 確信度：medium
- 出典：Death of the dinosaurs? It was all about the asteroid, not volcanoes｜Yale University｜2020-01-16｜https://news.yale.edu/2020/01/16/death-dinosaurs-it-was-all-about-asteroid-not-volcanoes
- 関連ノード：evt.kpg
- 補足：現在の大まかな構図は次のとおり。衝突が主因であることには強い合意がある。デカン・トラップがどの程度関わったか（ほとんど関わらない／事前に弱らせた／回復を遅らせた）は議論が続いている。

---

## H. K-Pg後の哺乳類・霊長類・人類系統

## 主張 R37
- 内容：有胎盤類（胎盤を持つ哺乳類）の多様化については、3つのモデルがある（Archibald & Deutschman による）。爆発（Explosive）モデル、短導火線（Short Fuse）モデル、長導火線（Long Fuse）モデルである。分子時計の研究は長導火線モデル（主な系統の分岐は白亜紀にあり、生態的な多様化は K-Pg の後）を最もよく支持するが、形態による系統解析は白亜紀の真獣類を有胎盤類の外側に置くため、このモデルを支持しない。著者ら（Springer ら 2019）は、合意はまだないとしている。
- ラベル：論争
- 確信度：medium
- 出典：Evolutionary Models for the Diversification of Placental Mammals Across the KPg Boundary｜Frontiers in Genetics 10｜2019｜https://www.frontiersin.org/articles/10.3389/fgene.2019.01241/text
- 関連ノード：新規候補 evt.mammal-radiation、evt.kpg
- 補足：「恐竜が消えたから哺乳類が生まれた」は誤り。哺乳類は中生代からいた。K-Pg の後に変わったのは、生態的な広がりである。

## 主張 R38
- 内容：最古の霊長類の仲間（プルガトリウス類）の化石は、米国モンタナ州の K-Pg 境界の約10.5万〜13.9万年後の地層から見つかっている（Wilson Mantilla ら 2021, Royal Society Open Science）。このことから、霊長類の系統（汎霊長類）と有胎盤類は白亜紀後期にはすでに生まれていた可能性が高い。
- ラベル：理論
- 確信度：medium
- 出典：Earliest Palaeocene purgatoriids and the initial radiation of stem primates｜Royal Society Open Science｜2021｜https://ui.adsabs.harvard.edu/abs/2021RSOS....810050W
- 関連ノード：新規候補 evt.mammal-radiation、thm.human-evolution（橋）
- 補足：霊長類の起源が K-Pg より前か後かには論争がある。

## 主張 R39
- 内容：サヘラントロプス・チャデンシス（チャド、2002年に命名、愛称トゥーマイ）は約700万〜600万年前のもので、人類系統とチンパンジー系統の分岐のころにあたる。年代は火山灰ではなく、一緒に出た動物化石から推定されている。二足歩行していたか、人類系統に属するかには論争がある。
- ラベル：論争
- 確信度：medium
- 出典：Sahelanthropus tchadensis｜Australian Museum｜https://australian.museum/sahelanthropus-tchadensis
- 関連ノード：evt.hominin-split（橋）
- 補足：次回（人類の進化）への橋として使う。

## 主張 R40
- 内容：Langergraber ら（2012, PNAS）は、野生のチンパンジーとゴリラの世代時間を測り、化石を使わずに分岐年代を推定した。その結果、ヒトとチンパンジーの分岐を「少なくとも700万〜800万年前」とし、600万〜700万年前の人類系統の化石とも整合しうると結論した。
- ラベル：理論
- 確信度：medium
- 出典：Generation times in wild chimpanzees and gorillas suggest earlier divergence times in great ape and human evolution｜PNAS 109(39):15716–15721｜2012｜https://research-portal.st-andrews.ac.uk/en/publications/generation-times-in-wild-chimpanzees-and-gorillas-suggest-earlier/
- 関連ノード：evt.hominin-split
- 補足：既存の evt.hominin-split の「約700万〜600万年前以降」は、化石にもとづく推定としては妥当。分子時計による推定はもう少し古くなりうることを補足するとよい。

---

## I. 生物多様性の現在

## 主張 R41
- 内容：IPBES 地球規模評価（2019年5月6日に政策決定者向け要約を発表）は、約100万種の動植物が絶滅の危機にあり、その多くが数十年以内に絶滅しうると評価した。十分に調べられた動植物のグループでは、平均約25%の種が絶滅の危機にある。直接の要因は影響の大きい順に、(1) 陸と海の利用の変化、(2) 生物の直接的な採取・利用、(3) 気候変動、(4) 汚染、(5) 侵略的外来種。現在の絶滅速度は過去1000万年の平均の「数十〜数百倍」で、加速している。評価は50か国145人の執筆者によるもので、約1万5000件の文献にもとづく。
- ラベル：事実（報告の内容）／理論（推定値）
- 確信度：high（報告がそう述べていること）／medium（「100万」という推定値。算出方法は広報ページには書かれていない）
- 出典：Media Release: Nature's Dangerous Decline 'Unprecedented'; Species Extinction Rates 'Accelerating'｜IPBES｜2019-05-06｜https://www.ipbes.net/news/Media-Release-Global-Assessment
- 関連ノード：新規候補 con.biodiversity-crisis
- 補足：「100万種」は、25%という割合を、推定約800万種（その多くは昆虫）に当てはめたものとされる【算出方法は未確認。本文で確認が必要】。

## 主張 R42
- 内容：WWF の Living Planet Report 2024 では、Living Planet Index（ZSL が作成）は1970〜2020年に平均73%減少した（34,836個体群）。この数値は、各個体群の変化率の幾何平均であり、種や個体の73%が失われたという意味ではない。実際には個体群の約50%が減少、43%が増加、7%が横ばいだった。2022年版の69%から73%への変化は、主にデータの変更による。
- ラベル：事実（指標の値）／規範に関わらない注意（解釈の誤りを防ぐ）
- 確信度：high
- 出典：2024 Living Planet Index｜Our World in Data｜2024-10｜https://ourworldindata.org/2024-living-planet-index
- 関連ノード：新規候補 con.biodiversity-crisis
- 補足：2026年版が出ている（R43）。

## 主張 R43
- 内容：Living Planet Report 2026（WWF、2026年10月）では、Living Planet Index は1970〜2022年に平均73%（73.2%、年平均2.5%）減少した。対象は脊椎動物5,790種の35,803個体群。減少は淡水が最も急で、地域別では中南米・カリブ、アフリカ、アジア太平洋で大きい。ヨーロッパと北米の減少が小さいのは、大きな影響の多くが1970年の基準年より前に起きていたためである。主な脅威は生息地の喪失と劣化、乱獲、気候変動、汚染、外来種、病気。回復の例としてトラ（2010年の約3,200頭から2025年の約5,700頭）、クロマグロ、南部アフリカのゾウ、アオウミガメ（2025年に「低懸念」へ引き下げ）を挙げている。
- ラベル：事実（指標の値）
- 確信度：high
- 出典：Living Planet Report 2026 Media Summary｜WWF｜2026-10｜https://wwfint.awsassets.panda.org/downloads/lpr-2026_10-2_media_brief_1_1.pdf ／ A 73% average decline in wildlife populations: an overview of the 2026 Living Planet Index report｜Our World in Data｜2026-10-08｜https://ourworldindata.org/2026-lpi-update
- 関連ノード：新規候補 con.biodiversity-crisis
- 補足：2024年版と2026年版は同じ73%だが、データセットが拡張されているため、単純に延長した比較はできない（OWID）。地域ごとの割合はPDFからの読み取りで対応が不確かなため、記載しない。

## 主張 R44
- 内容：現在を「第6の大量絶滅」と呼ぶことには論争がある。Cowie, Bouchet & Fontaine（2022, Biological Reviews）は、陸生の貝類のデータから外挿し、1500年以降に既知の約200万種のうち7.5〜13%（約15万〜26万種）がすでに失われた可能性があると推定して、無脊椎動物を含めれば第6の大量絶滅は進行中だと主張した。これに対し Marshall（2023）は、現在の絶滅速度は過去5億年で白亜紀末に次ぐ2番目に高い可能性があるが、絶滅した種の総数はビッグファイブに比べてまだ小さいとして、「まだそうではない、しかしそうなりうる」と述べ、「初期の人新世大量絶滅（incipient Anthropocene mass extinction）」という呼び方を提案した。
- ラベル：論争
- 確信度：medium
- 出典：Strong evidence shows Sixth Mass Extinction of global biodiversity in progress｜University of Hawaiʻi｜2022-01-14｜https://www.hawaii.edu/news/2022/01/14/6th-mass-extinction-progress/ ／ Marshall 2023（R26と同じ）
- 関連ノード：新規候補 con.biodiversity-crisis、新規候補 con.mass-extinction
- 補足：論点は「速さ（率）」と「量（累積）」の区別にある。どちらの立場も、深刻な危機であることには同意している。Cowie らの推定は陸生の貝類からの外挿に依存しており、不確かさが大きい。

---

## 担当範囲で見つけた、地図にない重要な概念（新規ノード候補）

| 仮ID | 名称 | level（案） | 親 | 根拠 |
|---|---|---|---|---|
| evt.snowball-earth | 全球凍結（古原生代・クリオジェニアン紀） | 出来事 | thm.life（または thm.earth-solar と共有） | R3, R8–R10 |
| evt.eukaryotes | 真核生物の出現（化石約16.5億年前／分子推定は最大約29億年前） | 出来事 | thm.life | R11–R13 |
| evt.multicellularity | 多細胞化（複数回独立。最古約16.3億年前） | 出来事 | thm.life | R11, R14 |
| evt.ediacaran-biota | エディアカラ生物群（約5.74億年前〜） | 出来事 | thm.life（evt.cambrian の前段） | R15 |
| evt.land-colonization | 陸上への進出（植物：オルドビス紀／四肢動物：デボン紀） | 出来事 | thm.life | R21–R24 |
| con.mass-extinction | 大量絶滅（ビッグファイブとその枠組みの是非） | 概念 | thm.life | R25–R31 |
| evt.end-permian | ペルム紀末の大量絶滅（251.94 Ma、シベリア・トラップ） | 出来事 | con.mass-extinction | R29–R30 |
| evt.mammal-radiation | K-Pg 後の哺乳類の多様化（3つのモデル） | 出来事 | thm.life（evt.hominin-split への橋） | R37–R38 |
| con.biodiversity-crisis | 現在の生物多様性の喪失（IPBES・LPI、「第6の大量絶滅」論争） | 概念 | thm.life | R41–R44 |
| con.boring-billion | 退屈な10億年（原生代中期の低酸素） | 概念 | evt.goe の後段 | R7（優先度低。evt.goe の補足でもよい） |
| evd.fossil-record | 化石記録（特に保存のよい化石産地：澄江・バージェス） | 証拠 | thm.life | R19–R20, R23（計画の候補にもある） |
| evd.molecular-phylogeny | 分子系統・分子時計 | 証拠 | thm.life | R13, R17, R18, R40（計画の候補にもある） |

- 新規候補の上限（20件）があるため、優先度は次のとおり。evt.snowball-earth、evt.eukaryotes、evt.land-colonization、con.mass-extinction は計画の候補リストに既にある（または相当する）ので最優先。evt.multicellularity と con.biodiversity-crisis はその次。evt.end-permian と con.boring-billion は、上限に余裕がなければ親ノードの補足にとどめる。
- 地図の設計上の注意：GOE・全球凍結・デボン紀後期の絶滅（陸上植物の影響）は「生命が地球を変え、地球が生命を変える」という共進化のエッジ（例：evt.goe →（引き金の可能性）→ evt.snowball-earth、evt.land-colonization →（仮説）→ デボン紀後期の絶滅）として表すと、中心の問いに効く。

## 既存ノードの誤りの疑い

1. **evt.goe**（「約24億年前、大気中の酸素が増えた。生命（光合成）が地球環境を大きく変えた例。」）
   - 一点の出来事のように書かれているが、最新の推定では約25.0〜24.3億年前に始まり、約22.2億年前まで約2億年にわたって酸素が増減を繰り返した（R2, R3）。「約24.3億年前に始まり、約22億年前までに定着した、長い移行」と書くべき。
   - 「生命（光合成）」の部分は、酸素発生型光合成（シアノバクテリア）の始まりがGOEより数億年早かった可能性が高く（R4, R5）、GOEの時期は火山ガスなどによる酸素の消費とのつり合いで決まった（R6）。光合成とGOEを直接の一因で結ぶのは単純化しすぎ。
   - 出典が未登録。Poulton 2021、Lyons 2014 を登録すべき。
2. **evt.kpg**（「約6600万年前、非鳥類型の恐竜などが絶滅した。」）
   - 年代は正しい（ICS 66.00 Ma／Renne 2013・Marshall 2023 の 66.043 ± 0.043 Ma）。誤りではないが、原因の記述がない。「チクシュルーブ衝突が主因であることに強い合意（Alvarez 1980、Schulte 2010、Renne 2013）。デカン・トラップの関与の程度は論争中（Schoene 2019 と Sprain 2019、Hull 2020）」を加えるべき（R32–R36）。
   - 種の喪失率（約76%、Barnosky 2011）の追記も候補。
3. **evt.cambrian**（「約5億3880万年前から…段階的に進んだ面もある」）
   - 538.8 Ma は ICS v2024/12 で再確認した（±0.6 Myr）。記述に誤りはない。補足するなら、「主な左右相称動物の系統の多くが最初の約2000万年で現れる（Zhang & Shu 2021）」と、「分子時計は起源を8億〜7億年前とする推定もあり、化石との差が論争になっている（Durbin ら 2026）」の2点（R16–R18）。
4. **thm.life**
   - 既存ノードの一覧（_existing_nodes.txt）にある thm.life の説明には「約40億年前？」の表記は見当たらなかった（計画 §4 で言及されている表記は、ノードの別の欄にある可能性がある）。生命の始まりの年代は R1（origin）の担当範囲なので、ここでは判断しない。歴史側から言えるのは次の点。「？」で不確かさを示すのではなく、認識ラベル（未知／論争）と推定の幅で表すべき。また、範囲の説明に「地球環境との共進化（大気の酸化、全球凍結）」と「現在の生物多様性の喪失」を明記すると、今回の新規ノードの親として整合する。
5. **evt.hominin-split**（参考）：誤りではないが、分子時計による推定（Langergraber 2012：少なくとも700万〜800万年前）を補足すると、化石と分子の推定の差という、今回の教材の共通テーマにつながる（R40）。

## 時事候補の推薦

**第1候補：Durbin, Anderson ら「動物の起源はエディアカラ紀より前（8億〜7億年前）か」**
- 発表：2026年10月2日（Science Advances、オックスフォード大学の発表は2026-09-23付のURL、EurekAlert! は 2026-10-02）
- 一次資料：論文 doi:10.1126/sciadv.aeg6289「Re-evaluating molecular clock maximum age calibrations revives pre-Ediacaran divergence estimates for animals」／ https://www.ox.ac.uk/news/2026-09-23-new-study-suggests-animals-may-have-evolved-vastly-earlier-than-fossil-evidence ／ https://www.eurekalert.org/news-releases/1145493
- 選んだ理由：今回の中心の問い（どのように多様になったか）と evt.cambrian に直接つながる。「化石と分子時計の食い違い」「仮説を証拠から区別する」という、学び方の練習になる。著者自身が「証明ではない」と明言しており、認識ラベル（仮説）を付ける稽古に向いている。
- 注意：論文本文は未取得。Verifier が doi で原著を照合すること。

**第2候補：WWF Living Planet Report 2026（2026年10月）**
- 一次資料：https://wwfint.awsassets.panda.org/downloads/lpr-2026_10-2_media_brief_1_1.pdf ／ 解説：https://ourworldindata.org/2026-lpi-update（2026-10-08）
- 選んだ理由：生物多様性の現在（con.biodiversity-crisis）につながり、「73%の誤読」を正す、数値の読み方の稽古になる。生命史の議論（大量絶滅）と現在を結ぶ。

**参考（第3候補）**：Kay ら「Dated gene duplications elucidate the evolutionary assembly of eukaryotes」Nature 2025-12-03（doi:10.1038/s41586-025-09808-z）。真核生物の起源を約29億年前とする推定。発表から1年近く経っているため、時事としての新しさは上の2件に劣る。
