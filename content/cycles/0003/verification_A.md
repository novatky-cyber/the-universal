# L0003 検証結果（グループA）

- 検証者：Verifier（独立検証。主張の作成には関与していない）
- 検証日：2026-11-25
- 対象：`claims/claims_A.md` の H1〜H56、X1〜X12（計68件）
- 方法：主張ごとに、記載の出典ページを WebFetch で開いて数値・年代・固有名詞・因果の向きを照合し、ラベルの適切さを確認した。
- **制約（重要）**：検証の途中で、この実行の WebSearch の利用上限（全エージェント共有）に達した。そのため後半は、主張に記載された URL と、それまでの検索で得た URL の WebFetch だけで確認した。記載の出典で確認できなかった点は、記憶にある別の資料名を「要確認」として修正案に書くにとどめ、確認済みとは扱っていない。開けなかったページ：PLOS ONE 本文（Villa & Roebroeks 2014、許可待ちで時間切れ）、PMC10427290（reCAPTCHA）、PubMed 32241925（本文なし）、eLife 19568 の本体ページ（JS 必須。PMC 版で代わりに確認）。

## 判定表

| 主張ID | 判定 | 理由 | 修正案 | 確認した資料（URL） |
|---|---|---|---|---|
| H1 | 確認済み | 「少なくとも7〜8 Ma」（本文は7〜13 Ma）、ゴリラ8〜19 Ma、ネアンデルタール人との分岐40万〜80万年前（本文は42.3万〜78.1万年前）、類人猿の突然変異率は未測定でヒトの値を仮定、のすべてが原文と一致。ラベル「論争」も妥当。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3465451 |
| H2 | 確認済み | Callaway 2012 は実在する（Nature 489:343–344、2012-09-18）。ただし公開部分は standfirst だけ。【未確認】だった率は Scally & Durbin 2012 で確認できた：系統法の約1×10⁻⁹/bp/年に対し、家系法は約0.4〜0.5×10⁻⁹。分岐年代は古い方へ動く（例：ヨルバ人と非アフリカ人の分岐が約5万年前から9万〜13万年前へ）。 | 出典に Scally & Durbin 2012（Nat Rev Genet 13:745–753）を加え、【未確認】を外す。 | https://www.nature.com/articles/489343a ／ https://wiki.helsinki.fi/xwiki/bin/download/mathstatKurssit/Kev%C3%A4t%202015/Statistical%20genetics%2C%20spring%202015/WebHome/Revising%20human%20mutation%20rate%2C%20understanding%20human%20evolution.pdf?rev=1.1 |
| H3 | 確認済み | トロス・メナラ、10Be による約7.2〜6.8 Ma、押しつぶされた頭骨・下顎片・歯、小さく先端がすり減る犬歯、雌の類人猿説が Scitable と一致（Brunet et al. 2002）。「2001年発見」「ジュラブ砂漠」は Scitable に明記がないが、phys.org（2001年前後の発見に言及）と一般的な記述に合う。 | 年代の原典として Lebatard et al. 2008（Scitable が引用）を併記するとよい。 | Scitable（主張記載のURL）／ https://phys.org/news/2020-11-partial-left-femur-sahelanthropus-tchadensis.html |
| H4 | 確認済み | 6.0〜5.7 Ma、BAR 1002'00、皮質骨の非対称、CT の質への批判（Ohman 2005、White 2006）と形質の有効性への批判（Andrews & Harrison 2005）、大きな犬歯、のすべてが一致。 | なし | Scitable |
| H5 | 確認済み | カダッバ 5.8〜5.2 Ma、ラミドゥス約4.4 Ma・110点・ARA-VP-6/500、ものをつかめる親指・土踏まずなし、条件付き二足歩行（facultative biped）、足指骨の層位の問題（Begun 2004）、のすべてが一致。 | なし | Scitable |
| H6 | 確認済み | 小さな犬歯と二足歩行の兆候が根拠であること、オレオピテクスによるホモプラシーの指摘（Wood & Harrison 2011）が Scitable と一致。 | なし | Scitable |
| H7 | 確認済み | JHE 2020。大腿骨は四足歩行の類人猿のもの、歯の大きさは根拠として不十分（小型の雌の類人猿の可能性）、人類ではない、という主張を報道で確認。【未確認】だったブリュネらの記載が Nature 2002 であることは、Scitable が Brunet et al. 2002 を引いていることで裏づけられる。phys.org の「査読のない雑誌」という記述は疑わしく、教材に使わない方針は妥当。 | 補足の【未確認】を「Brunet et al. 2002（Nature）で確認」に改める。 | phys.org（上記）／ Scitable |
| H8 | 確認済み | Nature 609:94–100（2022）、TM 266、大腿骨1点と尺骨2点、習慣的な二足歩行と相当な樹上行動、約7 Ma、のすべてが一致。 | なし | https://www.nature.com/articles/s41586-022-04901-z |
| H9 | 確認済み | 題名、JHE 2024-06-25、著者に Wood・Spassov を含むこと、習慣的二足歩行者だけが持つ特徴はないこと、肢の比率はアフリカの大型類人猿型、移動様式は不明、のすべてが一致。 | なし | https://mpg.de/22183908/what-about-bipedalism-in-sahelanthropus |
| H10 | 確認済み | 2026-01-02、Science Advances、DOI 10.1126/sciadv.adv0130（UChicago のリポジトリで確認）、著者6名、3D 幾何学的形態測定、大腿骨結節・前捻・殿筋・大腿骨と尺骨の比率の4点、前捻と殿筋は先行研究の確認、のすべてが一致。ラベル「論争」も妥当。 | なし | https://knowledge.uchicago.edu/records/p54a4-n6p31 ／ https://www.eurekalert.org/news-releases/1109959 |
| H11 | 確認済み | Cazenave（「弱い証拠」、結節の範囲は分からない）と Hawks（納得）は Smithsonian で、Carretero（題名が「無謀」、侵食面上の小さな隆起）と Potau（堅実なデータと手法）は SMC España で確認。 | Hawks は「完全に人類か完全に類人猿かで見るべきでない」と留保している。これを添えるとより正確になる。 | 主張記載の2つのURL |
| H12 | 確認済み | 1974-11-24、ハダール A.L. 288、約320万年前、47点、約40%、約388 cm³、アファレンシスは380万〜300万年前、のすべてが一致。 | なし | https://www.scientificamerican.com/article/fossil-human-ancestor-lucy-remains-pivotal-50-years-after-discovery |
| H13 | 確認済み | Scientific American に「upright walking evolved before large brains」と明記。スミソニアンの時期区分とも整合する。 | なし | 同上 ／ https://humanorigins.si.edu/human-characteristics/brains |
| H14 | 修正要 | 3.66 Ma、G地点、S1 は約165 cm（G2 より20 cm 以上大きい）、性的二型の可能性、は原文（PMC 版）と一致。【未確認】だった年代の原典は Deino & Harrison 2011（40Ar/39Ar）と論文中で確認できた。ただし「最古の人類の足跡」は2016年時点の表現である。2017年にクレタ島トラキロスの約570万年前の足跡を人類のものとする主張があり、論争中（記憶による。今回は未照合）。 | 「広く認められた最古の人類の足跡」に改める。原典を Deino & Harrison 2011 とする。 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5156529/ |
| H15 | 確認済み | KNM-ER 101000、トゥルカナ湖付近、約152万年前、Nature 2025-10-15（Mongle ら）、ヒト的な把持の比率、ゴリラ的な強い握力、道具製作・使用の可能性、精密なつまみ動作の欠如の可能性、のすべてが一致。 | なし | https://www.natureasia.com/ja-jp/nature/pr-highlights/15370 |
| H16 | 確認済み | 約204万〜195万年前、ESR・古地磁気・ウラン鉛法、3群の共存、ホモ・エレクトスが他より10万〜20万年古い、のすべてが一致。PubMed は今回も本文を取得できず、巻号は直接照合していない。 | 巻号（Science 368, eaaw7293）を原典で確かめておくこと。 | https://archaeology.org/news/2020/04/03/200406-drimolen-cave-dates/ |
| H17 | 確認済み | LD 350-1 の下顎、2.80〜2.75 Ma、Science 347(6228):1352–1355、原始的特徴と派生的特徴の混在、が一致。 | なし | https://pure.psu.edu/en/publications/early-homo-at-28-ma-from-ledi-geraru-afar-ethiopia/ |
| H18 | 確認済み | 通説で約200万年前、190万〜150万年前の化石、550〜1,250 cm³、1.4〜1.8 m、41〜65 kg、体の比率、トゥルカナ・ボーイ（約150万年前、「最も完全な」標本）、のすべてが NHM と一致。 | なし | https://www.nhm.ac.uk/discover/homo-erectus-our-ancient-ancestor.html |
| H19 | 修正要 | 本文は NHM と一致する（中国では少なくとも30万年前まで、ジャワでは少なくとも25万年前まで、ジャワの頭蓋の年代は「20万年前以上か5万年前未満か」で争われる）。ただし補足の Rizal ら 2020（ガンドン約11.7万〜10.8万年前）は、検索上限のため今回も照合できなかった。この年代が正しければ、「インドネシアでは少なくとも25万年前まで」は古い記述になる。 | 「NHM によれば少なくとも25万年前まで。ジャワのガンドンをより新しい年代（約11万年前）とする研究もある（要照合：Rizal et al. 2020, Nature 577）」と書き、Rizal の照合が済むまで数値を断定しない。 | NHM（同上） |
| H20 | 確認済み | 1.85〜1.78 Ma（Ferring ら、PNAS 108(26):10432–10436）。頭骨5点、下顎3点、単純な石器、約1.5 m、変異は現代人・チンパンジー並み、ゲオルギクス説とエレクトス説、は NHM で確認。 | Ferring 2011 の記録ページには出土品の記述がない。出土品と変異の出典は NHM と明記する（頭骨変異の原典は Lordkipanidze et al. 2013, Science）。 | https://www.iphes.cat/earliest-human-occupations-dmanisi-georgian-caucasus-dated-185%E2%80%93178-ma ／ NHM |
| H21 | 修正要 | 3倍、384 g と1,352 g、体重の2%で酸素・血流の20%、80万〜20万年前に最も急速、は一致。ただしスミソニアンは200万〜80万年前について「体の大型化とともに増大した」と書いており、「速まった」とは書いていない（相対的な脳の大きさは大きく変わらなかった、という含意がある）。補足の Du ら 2018 は今回も未照合。 | 「200万〜80万年前は体の大型化とともに増大」に改める。Du 2018 は照合するまで使わない。 | https://humanorigins.si.edu/human-characteristics/brains |
| H22 | 根拠不足 | スミソニアンが気候変動と脳の最速の増大を結びつけていることは確認できた（ラベル「仮説」は妥当）。しかし【未確認】の社会脳仮説・高価な組織仮説・調理仮説は、記載の出典に含まれず、今回も一次資料で照合できなかった。 | 一次資料を照合してから載せる（候補：Aiello & Wheeler 1995, Current Anthropology 36:199–221／Dunbar 1998, Evolutionary Anthropology／Wrangham の調理仮説）。照合するまでは「ほかにも仮説がある」とだけ書く。 | 同上 |
| H23 | 確認済み | TL の加重平均315±34 ka、イルード3 の286±32 ka、「報告された最古のホモ・サピエンス」、が一致。 | なし | https://www.nature.com/articles/doi:10.1038/nature22335 |
| H24 | 確認済み | 顔と歯は現代的で脳頭蓋は原始的なモザイク、「アフリカ大陸全体が関わった」、が一致。補足の後半は一般論として扱う。 | 補足の後半は「一般論」と明示したままにする。 | https://www.nature.com/articles/doi:10.1038/nature22336 |
| H25 | 確認済み | 233±22 ka（最小）、KHS 凝灰岩、シャラ火山 Qi2 の噴火、ガラスの地球化学的対比と40Ar/39Ar、Nature 601:579–583、が一致。 | なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8791829 |
| H26 | 確認済み | 23名、DOI 10.1016/j.tree.2018.05.005、化石・考古・遺伝・古環境の4領域から構造化された汎アフリカ起源を論じる、が一致。 | なし | https://www.ucl.ac.uk/human-evolution/news/2018/jul/did-our-species-evolve-subdivided-populations-across-africa-and-why-does-it-matter |
| H27 | 確認済み | トマ採石場 I、出土品（下顎3点〈成人2・子ども1〉・椎骨・歯・大腿骨）、773±4 ka、ブリュンヌ／松山境界、Nature 649(8098):902、DOI、エレクトス・アンテセッソルと区別されること、分岐の根元近くの集団、歯（エナメル・象牙境）による分類、のすべてが一致。 | なし | https://www.sciencedaily.com/releases/2026/02/260206012221.htm |
| H28 | 確認済み | 雲県2号、約100万年前、エレクトスから longi 系統の初期の一員へ、100万年以上前の分岐、遺伝学より約40万年早い、限界（アフリカ化石を含められなかった、理論的推定）、Science DOI 10.1126/science.ado9202、2025-09-25、が一致。 | 「潰れた頭骨の復元に依存」は発表文の限界の列挙には明記されていない。検証者の補足として区別する。 | https://www.nhm.ac.uk/press-office/press-releases/analysis-of-reconstructed-ancient-skull-pushes-back-our-origins-.html |
| H29 | 確認済み | 核DNAはネアンデルタール系統、約43万年前までに分岐、55万〜75万年前（ペーボの発言）、2013年の mtDNA はデニソワ人に近い、が一致。 | なし | https://www.mpg.de/10364707/hominins-sima-de-los-huesos |
| H30 | 確認済み | 5地域147人、約20万年前（14万〜29万年前）、変異の多くは集団内、後に約17万年前に修正、が一致。 | なし | https://embryo.asu.edu/pages/mitochondrial-dna-and-human-evolution-1987-rebecca-louise-cann-mark-stoneking-and-allan |
| H31 | 確認済み | 呼び名は同号の News and Views の記事に由来し、1987年論文自体は使っていない、が一致。「最初の女性ではない」などの否定の部分は、出典に明記はないが定義から直接導ける。 | 否定の部分は「定義からの帰結」と明記するとよい。 | 同上 |
| H32 | 確認済み | 上顎骨と歯、19.4万〜17.7万年前、完全なルヴァロワ技法、スフール・カフゼー（約12万〜9万年前）より古い、が一致。補足の「異論があり得る」【未確認】は照合できなかった。 | 異論の具体的な出典を示せないなら、補足のその一文は削る。 | https://openresearch-repository.anu.edu.au/items/d1428444-05fd-4215-8c54-6b0ca98d2888 |
| H33 | 確認済み | AW-1、95〜86 ka、アフリカとレヴァントの外で最古の直接年代、MIS 5 の後半、二段階モデル（130〜90 ka と 60〜50 ka）、より広い初期拡散、モンスーン、のすべてが一致。 | なし | https://www.nature.com/articles/s41559-018-0518-2 |
| H34 | 修正要 | 遺伝子流入が約5万年前に始まり約7,000年続いたこと（単一なら約4.7万年前）、主要な出アフリカは遅くとも4.35万年前、は一致。【未確認】の「それより古い拡散はほとんど寄与していない」は MPG の記事に記述がない。記事が書いているのは「非アフリカ系の分岐は交雑の最中か直後に始まった可能性」まで。ノーベル財団の「約7万年前」は確認できた。「5万〜6万年前」の一次資料は今回も確認できなかった。 | 後半は「推論（未照合）」と明記するか削る。出発の年代は「約7万年前（ノーベル財団）〜遅くとも4.35万年前（Iasi ら）と資料によって幅がある」と書く。 | https://www.mpg.de/23832006/new-timeline-for-neandertal-gene-flow-event ／ https://www.nobelprize.org/prizes/medicine/2022/193954-press-release-swedish/ |
| H35 | 確認済み | マジェドベベ、約6.5万年前、光ルミネッセンス年代、約1.1万点の石器、が一致。ラベル「論争」も妥当（H36・X4）。 | なし | https://www.nature.com/nature-index/article/10.1038/nature22968 |
| H36 | 確認済み | O'Connell & Allen（2025、Archaeology in Oceania）、交雑は51.5〜43.5 ka、多くの遺跡は約5.4万〜4.3万年前、マジェドベベは外れ値で重い石器が砂の中を沈んだ可能性、OSL 自体は否定しない、のすべてが一致。 | 論文名「Recent DNA Studies Question a 65 kya Arrival of Humans in Sahul」（DOI 10.1002/arco.70002）を出典に加える。 | https://www.global.utah.edu/stories/when-did-humans-first-colonize-australia/ ／ X4 の Otago のページ |
| H37 | 確認済み | 2010年の解読、平均1〜4%（ノーベル財団）、1〜2%（MPG 2024）、が一致。補足の「アフリカの集団にも逆流によるネアンデルタール由来成分がある」【未確認】は照合できなかった。 | その補足は照合するまで使わない（候補：Chen et al. 2020, Cell）。 | ノーベル財団・MPG（上記） |
| H38 | 確認済み | DOI、300ゲノム（うち59人は2,000〜45,000年前）、約5万年前に開始、約7,000年続いた、約4.7万年前、が一致。 | なし | MPG 2024（上記） |
| H39 | 根拠不足 | ラニスとズラティー・クーニ、現在の非アフリカ系と共通の交雑に由来すること、それより新しい交雑がないこと（「早い分岐」も）は確認できた。しかし【未確認】の「現在の人々に子孫を残さなかった」はプレスキットに記述がなく、照合できなかった。「約4.5万年前」も挿絵の説明文にしか出てこない。 | 「子孫を残さなかった」は削るか、Sümer et al. 2024（Nature）の本文で確認してから載せる。年代は論文の値で書く。 | https://www.eva.mpg.de/press/news/press-kits/2024/2024-12-12-1041-unraveling-human-history/ |
| H40 | 確認済み | 2008年、約4万年前の小指の骨、デニソワ洞窟、最大6%、がノーベル財団の発表と一致。 | なし | ノーベル財団（上記） |
| H41 | 修正要 | 「Denisovan or Denisovan-related」からの遺伝子移入、漢族ではごくまれ、が一致。ただし原文の「他の集団では見られない」は「調べた世界の集団の中では」という限定つきである。 | 「調べた他の集団では見られなかった」に改める。 | https://www.nature.com/articles/nature13408 |
| H42 | 修正要 | 14.6万年前以上、95種のタンパク質、デニソワ人に固有の変異3つ、Science と Cell の2本、2025-06-18、シベリアから中国東北部までの分布、倪喜軍の批判（DNA 混入、より多くの変異が必要）、錐体骨と触れられていないエナメル質からDNAが取れなかったこと、は一致。「2021年にホモ・ロンギと命名」の年は記載の出典で確認できなかった。 | 命名の年には出典（Ji et al. 2021, The Innovation）を付ける（要照合）。倪喜軍の批判は「変異の数が少ない」より「判断にはより多くの変異が必要」と書く方が原文に近い。 | https://www.eurekalert.org/news-releases/1087905 ／ https://www.sciencenews.org/article/skull-first-denisovan-human-cousin |
| H43 | 確認済み | 周口店・和県・孫家洞の6点、約40万年前、全標本に固有の変異、デニソワ人と共有する変異（フィリピン約21%、インド約1%）、交雑は「最も可能性の高い説明」、機能は不明、Nature 655(8121):141、DOI、が一致。ラベル「仮説」も妥当。 | 交雑の時期は記事に明記がない。「約40万年前に交雑」は「約40万年前の標本に交雑の痕跡」と書く方が正確。 | https://www.sciencedaily.com/releases/2026/11/261102202836.htm |
| H44 | 確認済み | 骨格約10万〜6万年前、石器約19万〜5万年前、旧推定（堆積物は約9.5万〜1.2万年前、LB1 は約1.8万年前）、Nature 2016-04-21、DOI、撤回の表示なし、が一致。 | なし | https://openresearch-repository.anu.edu.au/handle/1885/109256?mode=full |
| H45 | 確認済み | 33.5万〜23.6万年前、OSL・U-Th・古地磁気・US-ESR、eLife 6:e24231、が一致。 | なし | https://wiredspace.wits.ac.za/items/44c39ea9-5bcf-4352-b7e1-ab8ea320eb44 |
| H46 | 確認済み | カヤオ洞窟、中足骨は6.7万年前、少なくとも3個体、歯・手足の指骨など、新種、Nature 568:181–186、が一致。補足の「慎重論」【未確認】は照合できなかった。 | 慎重論は出典を示せるまで「資料が少ない」という事実の記述にとどめる。 | https://www.nature.com/articles/s41586-019-1067-9 |
| H47 | 確認済み | 著者 Macho ら、npj Palaeoecosystems 1(1)、DOI、発育パターンの違いから複数種の可能性、湿潤と乾燥の繰り返しによる隔離と再接触、が一致。記事本文の「Nature に掲載」が誤りであることも確認した。 | なし | https://www.sciencedaily.com/releases/2026/11/261118065531.htm |
| H48 | 確認済み | 約4万年前、4万〜3.8万年前の石器の組合せ、約500の石器群（3.8万〜3万年前）、人骨はすべて現生人類、金取遺跡 IVb（5万〜9万年前）、捏造事件、が中沢 2017 と一致。 | 中沢は捏造の始まりを「1980年代から」と書き、Hudson 2005（X12）は「少なくとも1976年から」と書く。教材で併記する場合は資料による違いに注意。 | https://www.journals.uchicago.edu/doi/10.1086/694447 |
| H49 | 確認済み | 2010年論文：人骨そのものを直接年代測定し、3点が16〜20 ka BP、118(3):173–183。2017年報道：少なくとも19個体、1,000点以上、約2.7万年前、意図的に置かれた可能性、が一致。 | 約2.7万年前は報道経由であることを残す（報告書の原文は未照合）。 | https://www.jstage.jst.go.jp/article/ase/118/3/118_091214/_article ／ https://japantimes.co.jp/news/2017/05/19/national/science-health/japans-oldest-human-skeleton-found-okinawan-cave |
| H50 | 確認済み | 18,250±650 BP と 16,600±300 BP、炭化物は II〜IV と同じ粘土層、I は別の区画（C5/6〜D6）、119(2):125–136、が一致。較正の有無は抄録に記載がない（主張の注記どおり）。 | なし | https://www.jstage.jst.go.jp/article/asj/119/2/119_110727/_article/-char/en |
| H51 | 確認済み | 2019年、7.5 m の丸木舟、約3万年前の石器の複製、225 km、45時間あまり、2025-06-25、2本の論文と DOI、が一致。 | なし | https://www.u-tokyo.ac.jp/focus/en/press/z0508_00414.html |
| H52 | 確認済み | 授賞理由、2010年のゲノム、2008年の指骨、古ゲノム学、免疫への影響、が一致。 | なし | ノーベル財団（上記） |
| H53 | 確認済み | 「中期更新世のDNA配列を調べられる、永久凍土以外の唯一の遺跡」（Meyer の発言）、ハルビンでのDNA混入の指摘、古代タンパク質（H42・H43）、が各出典と一致。 | なし | MPG 2016、Science News、ScienceDaily 2026（上記） |
| H54 | 確認済み | 85.4%・8.3%・6.3%、17の遺伝システム、強く再現されていること、Edwards 2003 の評価（推論の誤りの指摘は正しいが、ルウォンティン本人はその誤りを犯していない）、Phil Trans B 377:20200405、が一致。 | 「17の遺伝子座」は原文では「17の遺伝システム（タンパク質の変異）」。 | https://web.stanford.edu/group/rosenberglab/papers/EdgeEtAl2022-PhilTransB.pdf |
| H55 | 確認済み | 121集団、多様性が最大、14の祖先クラスター、起源地は南部アフリカ（南アフリカとナミビアの国境付近）、出発点は紅海中部、が一致。 | なし | https://www.sciencedaily.com/releases/2009/04/090430144524.htm |
| H56 | 確認済み | Edge ら（最も強い反論は統計的知見そのもの）、Embryo Project（変異の多くは集団内）と整合。ラベルも妥当。 | 1987年研究の「集団」は5つの地理的集団で、「人種」そのものではない。「地理的集団の間でも」と書く方が正確。 | Edge ら 2022 ／ Embryo Project |
| X1 | 根拠不足 | Wolpoff・Hawks・Caspari 2000（AJPA 112(1):129–136、「Multiregional does not mean independent multiple origins」）は確認できた。一方、同化モデルの出典（CROSBI）は書誌記録だけで、掲載誌・年が分からない。「現在の主流に最も近い」は出典が支えない評価である。 | 同化モデルは掲載誌と年が分かる版（例：Smith らの総説）で照合する。「主流に最も近い」は検証者の見解として区別するか、合意を示す資料を付ける。 | https://deepblue.lib.umich.edu/handle/2027.42/34270 ／ https://www.bib.irb.hr/860800 |
| X2 | 確認済み | Nature 617:755–763、弱く構造化された幹、約12万〜13.5万年前、数十万年の遺伝子流動、ゴースト交雑のパターンをこのモデルで説明できる、が一致。 | なし | https://pubmed.ncbi.nlm.nih.gov/37198480/ |
| X3 | 修正要 | Chan ら（Nature 575:185–190, 2019）の主張と、Schlebusch ら16名（Tishkoff を含む）による批判（Preprints 2019110193）は確認できた。ただし「批判は査読前のプレプリントとして出された」は古い可能性がある。この批判は後に Nature の Matters Arising として掲載されたと記憶している（2021年、Nature 593。検索上限のため今回は未照合）。 | 掲載の有無を確かめ、掲載されていれば「後に Nature に査読を経て掲載」と改める。 | https://eeg.zoo.cam.ac.uk/news/human-origins-southern-african-palaeo-wetlands-strong-claims-weak-evidence ／ https://www.zoology.ubc.ca/~otto/veg/Readings/Chan2019.pdf |
| X4 | 確認済み | 著者5名、e70005（2025-06-29、DOI 10.1002/arco.70005）、Veth・Brumm（スラウェシの岩壁画は少なくとも5.12万年前）・Groucutt と Scerri の発言、が Live Science と一致。 | Groucutt と Scerri は約5万年前の「行動の革命」にも異を唱えた。これは X5 とつながる。 | https://ourarchive.otago.ac.nz/esploro/outputs/letter/Do-Recent-DNA-Studies-Refute-a/9926753237301891 ／ https://www.livescience.com/archaeology/human-evolution/neanderthal-dna-may-refute-65-000-year-old-date-for-human-occupation-in-australia-but-not-all-experts-are-convinced |
| X5 | 確認済み | 【未確認】だった巻号は Current Anthropology 52(1):1–35（2011、DOI 10.1086/658067）と確認できた。東アフリカの25万〜6000年前の石器、ばらつきの大きさ、行動生態学の費用と便益、は Stony Brook の記事で確認。「行動の現代性」を捨てるべきという主張も一致。 | 巻号を記入して【未確認】を外す。「広く引用されている」には引用数などの裏づけがないため、評価の表現にとどめる。 | https://researchconnect.stonybrook.edu/en/publications/homo-sapiens-is-as-homo-sapiens-was-behavioral-variability-versus/ ／ https://news.stonybrookmedicine.edu/news/john-shea-refutes-long-standing-myth-about-human-origins-2 |
| X6 | 修正要 | 11の仮説、現生人類の優越を前提にシナリオを組み立ててきたこと、顔料・装身具・樹脂の精製、は PLOS のブログで確認。PLOS ONE 9:e96424 の書誌は ADS で確認。ただし、絶滅の別の説明として挙げた「人口が少なかったこと」「偶然」は確認できた資料に明確な記述がない。本文ページは開けなかった。 | 別の説明は原文の抄録で照合してから書く。照合できない場合は「優越説の多くは証拠に支えられない」までにとどめる。 | https://ui.adsabs.harvard.edu/abs/2014PLoSO...996424V ／ https://everyone.plos.org/2014/05/14/modern-humans-really-better-just-get-lucky/ |
| X7 | 確認済み | AABA 2019（人種は人類の生物学的変異を正確に表さない、クライン状の変異、植民地主義、人種差別による生物学的影響）、67名の公開書簡、Reich の NYT 寄稿（2018-03-23）、が一致。 | なし | https://bioanth.org/about/aaba-statement-on-race-racism/ ／ https://news.ucsc.edu/2018/04/reardon-buzzfeed/ |
| X8 | 確認済み | Bardill ら（Science 360(6387):384、「まず害をなさない」、遺骨には生きた研究参加者に準じた配慮、事前の協議、偏見・土地・返還への配慮）と、Alpaslan-Roodenberg ら（Nature 599:41–46、31か国、5つの指針）が一致。 | 「意見の違いが残る」【未確認】は出典がないため、教材では未確認と明記する。 | https://sciencedaily.com/releases/2018/04/180426141528.htm ／ https://nathannakatsuka.scholars.harvard.edu/publications/ethics-dna-research-human-remains-five-globally-applicable-guidelines |
| X9 | 確認済み | 【未確認】だった巻号は European Journal of Archaeology 21(2):159–191（2018、DOI 10.1017/eaa.2017.43）と確認できた。考古学的文化を遺伝的集団と同一視していること、一度きりの大移動という描き方への批判、が一致。Frieman & Hofmann（World Archaeology 51(4):528–545）の「Fortress Europe」と極右による利用も一致。 | 巻号を記入する。 | https://www.cambridge.org/core/product/B225B14D82066373B2C11295AA1D1462/core-reader ／ https://researchportalplus.anu.edu.au/en/publications/present-pasts-in-the-archaeology-of-genetics-identity-and-migrati/ |
| X10 | 根拠不足 | 記載の出典（バンベルク大学のページ）で確認できたのは、題名・著者・Science 381・2023年と「hybrid model」という語だけである。「約8000年前」も「ヨーロッパの諸語はステップ経由で広がった」も記載がない。 | 論文本体（Heggarty et al. 2023, Science 381:eabg0818、DOI 10.1126/science.abg0818。要照合）か、機関の詳しい発表で数値と内容を照合する。 | https://uni-bamberg.de/en/general-linguistics/all-news/artikel/indoeuropaeische-ursprache-haig |
| X11 | 根拠不足 | Science Advances 2021-09、三重構造（縄文・弥生・古墳期の東アジア系）、大陸からの分岐2万〜1.5万年前、は TCD のページで確認できた。しかし「アイヌと琉球は縄文系の割合が高く、それぞれ独自の歴史を持つ」は出典に記述がない。二重構造の総説（PMC10427290）は開けなかった。 | アイヌと琉球の記述には別の出典を付ける（例：Cooke ら 2021 の本文）。総説は書誌を確かめるまで使わない。 | https://www.tcd.ie/news_events/articles/ancient-dna-rewrites-early-japanese-history--modern-day-populations-have-tripartite-genetic-origin/ |
| X12 | 修正要 | Hudson 2005（113(2):131–139）の、少なくとも1976年から2000年、180以上の遺跡、50万年以上前の前期旧石器、「民衆の歴史」という背景、は抄録と一致。ただし「教科書にまで載った」「日本考古学協会の調査で検証済み」は確認した抄録に記述がない（協会は2004年の報告書が引用されているだけ）。また、添えられた Japan Times 2017 と エディンバラ大学 2025 の記事はアイヌの遺骨返還の話で、X12 の主張（捏造事件）を支えない。 | 遺骨返還の2つの出典は X12 から外し、X8（倫理）など適切な項目へ移す。教科書と協会の検証には出典を付ける（日本考古学協会 2004『前・中期旧石器問題の検証』。要照合）。 | https://www.jstage.jst.go.jp/article/ase/113/2/113_2_131/_article ／ https://japantimes.co.jp/news/2017/03/23/national/hokkaido-university-agrees-return-remains-ainu-descendants ／ https://www.ed.ac.uk/news/2025/university-returns-ancestral-remains-to-ainu-people-in-japan |

## 件数の集計

| 判定 | 件数 | 主張ID |
|---|---|---|
| 確認済み | 54 | 下記以外のすべて |
| 修正要 | 9 | H14, H19, H21, H34, H41, H42, X3, X6, X12 |
| 根拠不足 | 5 | H22, H39, X1, X10, X11 |
| 出典不在 | 0 | — |
| 合計 | 68 | |

## 系統的な問題

1. **【未確認】が補足に多く残っている**：H19（Rizal 2020）、H21（Du 2018）、H32・H46（異論・慎重論）、H37（アフリカ人のネアンデルタール由来成分）、H45（ナレディの埋葬）など。今回確認できたものは表に書いた（H2、H7、H14、X5、X9）。残りは検索上限のため照合できなかった。教材では、照合できていない補足を根拠として使わないこと。
2. **出典の範囲を少し越える一般化が多い**：H21「速まった」、H41「他の集団では見られない」、H43「約40万年前に交雑」、H56「人種」。原文の限定（「調べた集団では」「体の大型化とともに」など）が落ちる傾向がある。
3. **二次資料に頼りすぎている**：時事候補（H27、H43、H47）は ScienceDaily などの報道を経由している。今回の照合では書誌も内容も一致したが、原論文の本文は誰も確認していない。X10 と X11 は、出典の機関ページが主張の中身を支えていない。
4. **出典と主張の対応がずれている**：X12 にアイヌの遺骨返還の記事が付いていた。X1 の同化モデルの出典は書誌記録だけだった。
5. **「多数派」「主流」の判定に根拠がない**：X1、X4、X5、X11 の「支持の程度」は推測を含む。教材では「専門家の多数」と書く前に、学会の声明や総説を根拠にすること（X7 の AABA 声明のように）。
6. **視点の偏り（参考）**：アフリカとアジア（中国・東南アジア・日本）の扱いは比較的厚い。一方で南アジアの化石記録（例：ナルマダ）は扱われていない。また、アフリカの研究者や先住民の研究者の視点は X8 の倫理の項目に限られている。
7. **数値の更新の可能性**：H14（最古の足跡）、H19（ジャワのエレクトスの最終年代）、X3（批判の論文化）は、より新しい資料で表現が変わる可能性がある。次回、検索ができるときに再確認すること。
