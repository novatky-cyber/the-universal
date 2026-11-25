# R3 調査報告：文明の成立（農耕・都市・国家・文字）

- 担当：Researcher R3（civilization）
- 調査日：2026-11-25
- 問い：農耕・都市・国家・文字は、なぜ・どのように・どこで生まれ、必然だったのか。
- 方法：WebSearch／WebFetch で論文のアブストラクト・機関ページ（UNESCO、大学、PMC 等）を確認。ページ本文を開けなかったもの（PMC の一部、CDLI、Britannica の一部）は、検索結果で書誌の実在のみ確認し、その旨を補足に書いた。記憶だけで書いた箇所には【未確認】を付けた。
- 年代表記：cal BP＝較正年代（1950年基準の「〜年前」）。BC＝紀元前。

---

## A. 農耕・牧畜の複数の独立起源

## 主張 V1
- 内容：栽培化・家畜化は約1万2000〜1万1000年前（最終氷期の終わり）に始まり、旧大陸と新大陸の少なくとも11の地域が独立した起源地だったとされる（さらに数か所の候補がある）。地域は南西アジア、南アジア、東アジア、ニューギニア、東アフリカ・南アラビア、北米、メソアメリカ、南米など。
- ラベル：事実（起源地が複数あること）／論争（正確な数）
- 確信度：high（複数であること）、medium（「11」という数）
- 出典：Larson, G. et al. "Current perspectives and the future of domestication studies"｜PNAS 111(17):6139–6146｜2014｜https://escholarship.org/content/qt6sd6f5bc/qt6sd6f5bc.pdf （DOI: 10.1073/pnas.1323964111）
- 関連ノード：evt.agriculture、thm.civilization
- 補足：数は「一次的な起源」と「二次的な栽培化（他地域から来た作物の影響下での栽培化）」の区別に左右される。証拠が乏しい地域（熱帯など）は過小評価されやすいと同論文自身が述べる。教材では「少なくとも十数か所」と幅で示すのが妥当。

## 主張 V2
- 内容：栽培化は地域ごとに時期がずれている（非同時的）。Larson らは関心の集中する時期を「完新世への移行期（約1.2万〜9000年前）」と「完新世中期（約7000〜4000年前）」の2つとし、新大陸では作物の栽培化が動物の家畜化より数千年早く、アフリカ・アラビア・インドでは逆だったと指摘する。
- ラベル：事実
- 確信度：high
- 出典：Larson et al. 2014（V1と同じ）
- 関連ノード：evt.agriculture
- 補足：「1万年前に世界で一斉に農耕が始まった」という言い方は不正確。最初の波は確かに完新世初めに複数地域で起きたが、アフリカ（サヘル）や北米東部などは数千年遅い。

## 主張 V3
- 内容：イヌの家畜化は農耕より前、更新世末にさかのぼる。古代のイヌ27個体のゲノム解析では、約1万1000年前までに少なくとも5つの主要な系統がすでに分岐していた。
- ラベル：事実（農耕以前であること）／論争（家畜化の正確な時期と場所）
- 確信度：high
- 出典：Bergström, A. et al. "Origins and genetic legacy of prehistoric dogs"｜Science 370(6516):557–564｜2020｜https://pubmed.ncbi.nlm.nih.gov/33122379/ （DOI: 10.1126/science.aba9572）
- 関連ノード：新規候補 evt.dog-domestication（イヌの家畜化、level: event、親: evt.agriculture または thm.human-evolution）
- 補足：Larson ら（2014）は約3万年前の「イヌ」の主張は論争中としている。イヌの家畜化の場所（東西ユーラシアのどこか、1回か複数回か）は未決着。

## 主張 V4
- 内容：肥沃な三日月地帯（南西アジア）では、コムギ・オオムギの栽培化の指標である「非脱粒性（穂が熟しても粒が落ちない性質）」の固定に長い時間がかかった。Fuller（2007）は、粒の大型化が先に約500〜1000年で進み、非脱粒性の固定はその後1000〜2000年かかったと推定し、コムギで約1500年、オオムギで約2000年以上とする。
- ラベル：理論（「ゆっくりとした栽培化」protracted domestication）
- 確信度：high
- 出典：Fuller, D. Q. "Contrasting patterns in crop domestication and domestication rates: recent archaeobotanical insights from the Old World"｜Annals of Botany 100(5):903–924｜2007｜https://pmc.ncbi.nlm.nih.gov/articles/PMC2759199 （DOI: 10.1093/aob/mcm048）
- 関連ノード：新規候補 con.protracted-domestication（ゆっくりとした栽培化、level: concept、親: evt.agriculture）
- 補足：鎌での収穫を仮定した実験的モデル（Hillman & Davies 1990）は20〜100年で固定し得るとしたが、考古植物学のデータはそれよりはるかに遅い。Larson ら（2014）はコムギ・オオムギ・イネで非脱粒性の固定に約2000〜4000年としている（数値の幅は研究により異なる）。「速い単一の発明」とする見方（Abbo らなど）との論争がある。

## 主張 V5
- 内容：完全に栽培化された作物が現れる前に、野生型の植物を何世紀も栽培する「栽培化前の栽培（pre-domestication cultivation）」の段階があった。
- ラベル：理論
- 確信度：high
- 出典：Larson et al. 2014（V1と同じ）
- 関連ノード：con.protracted-domestication（新規候補）
- 補足：「栽培（cultivation：人が育てる行為）」と「栽培化（domestication：植物の遺伝的変化）」を区別することが、農耕の起源を理解する鍵。用語は初出で区別して教えるべき。

## 主張 V6
- 内容：中国・長江下流域の上山（Shangshan）遺跡では、イネの機動細胞ケイ酸体（プラントオパール）の直接の炭素14年代から、最古の居住が約9400 cal BP とされた。ケイ酸体の形態（魚鱗状の模様の数）は野生と栽培の中間的で、イネの栽培化が完新世の初めに始まっていた可能性を示す。
- ラベル：事実（年代）／理論（栽培化の開始の解釈）
- 確信度：medium
- 出典：Zuo, X. et al. "Dating rice remains through phytolith carbon-14 study reveals domestication at the beginning of the Holocene"｜PNAS 114(25):6486–6491｜2017｜https://pmc.ncbi.nlm.nih.gov/articles/PMC5488950 （DOI: 10.1073/pnas.1704304114）
- 関連ノード：evt.agriculture
- 補足：「部分的に栽培化された」段階であり、完全な栽培化はさらに後（Fuller 2007 は耕作開始から1000〜1500年程度と推定）。イネの起源地（長江下流域か、他の地域か）にも議論がある。

## 主張 V7
- 内容：中国北部（黄河流域）の磁山（Cishan）遺跡の貯蔵穴の穀物は、約1万300〜8700 cal BP にはキビ（Panicum miliaceum）のみで、約8700 cal BP 以降に少量（0.4〜2.8%）のアワが加わる。東アジアのキビの栽培化は約1万年前にさかのぼるとされた。
- ラベル：事実（年代）／論争（栽培化の段階の判定）
- 確信度：medium
- 出典：Lu, H. et al. "Earliest domestication of common millet (Panicum miliaceum) in East Asia extended to 10,000 years ago"｜PNAS 106(18):7367–7372｜2009｜https://pmc.ncbi.nlm.nih.gov/articles/PMC2678631 （DOI: 10.1073/pnas.0900158106）
- 関連ノード：evt.agriculture
- 補足：同定はケイ酸体と生体分子の分析による。中国は「南のイネ・北のアワ・キビ」という少なくとも2つの系統の起源を持つと整理される。

## 主張 V8
- 内容：ニューギニア高地のクク湿地では、遅くとも約6950〜6440 cal BP までに農耕が独立に成立していた（Denham ら 2003）。UNESCO は、マウンド（盛り土）での栽培を経て、約4000年前以降に木の道具で溝を掘って湿地を排水する技術が続いたこと、土地の利用は約1万年前にさかのぼる可能性があることを記す。作物はバナナ・タロイモ・ヤムイモなど栄養繁殖（株分けや挿し木で増やす）作物。
- ラベル：事実（独立起源であること、約7000年前の年代）／論争（約1万年前の利用を「農耕」と呼べるか）
- 確信度：high（独立起源）、medium（1万年前）
- 出典：Denham, T. et al. "Origins of agriculture at Kuk Swamp in the Highlands of New Guinea"｜Science 301:189–193｜2003｜https://openresearch-repository.anu.edu.au/items/d601182a-a8b6-4509-9f84-99f2b3974a51 （DOI: 10.1126/science.1085255。巻・ページは【未確認】）／Kuk Early Agricultural Site｜UNESCO World Heritage Centre｜（2008年登録【未確認】）｜https://whc.unesco.org/en/list/887
- 関連ノード：evt.agriculture
- 補足：依頼文の「約7000〜1万年前」は妥当だが、確実に「農耕」と言えるのは約7000年前、1万年前は植物の利用・管理の段階と区別すべき。穀物ではなく根栽・果実の農耕である点は、「農耕＝穀物」という固定観念への反例になる。

## 主張 V9
- 内容：メキシコ・バルサス川中流域のシワトクストラ（Xihuatoxtla）岩陰では、トウモロコシのデンプン粒とカボチャのケイ酸体が、8990〜8610 cal BP（少なくとも約8700年前）の層から見つかった。トウモロコシの最古の記録とされる。トウモロコシの祖先はテオシント（バルサス・テオシント）。
- ラベル：事実
- 確信度：high
- 出典：Piperno, D. R. et al. "Starch grain and phytolith evidence for early ninth millennium B.P. maize from the Central Balsas River Valley, Mexico"｜PNAS 106(13):5014–5018｜2009｜https://pmc.ncbi.nlm.nih.gov/articles/PMC2664064 （DOI: 10.1073/pnas.0812590106）
- 関連ノード：evt.agriculture
- 補足：「約9000年前」という依頼文の値は較正年代として妥当。ただしトウモロコシが主食級の作物になるのはずっと後で、栽培化から集約的な依存までに数千年の開きがある（V12参照）。

## 主張 V10
- 内容：南米アマゾン南西部（ボリビアのジャノス・デ・モホス）では、人工の「森の島」のケイ酸体から、キャッサバ（マニオク）約1万350年前、カボチャ約1万250年前、トウモロコシ約6850年前の痕跡が見つかった。研究者はこの地域で4700以上の人工の森の島を数えた。
- ラベル：事実（年代）／理論（「栽培化の中心」とする解釈）
- 確信度：medium
- 出典：Lombardo, U. et al. "Early Holocene crop cultivation and landscape modification in Amazonia"｜Nature 581:190–193｜2020｜https://www.doi.org/10.1038/s41586-020-2162-7 ／Penn State News「Amazonian crops domesticated 10,000 years ago」｜2020-04-08｜https://www.psu.edu/news/research/story/amazonian-crops-domesticated-10000-years-ago
- 関連ノード：evt.agriculture
- 補足：年代の数値は大学の発表で確認（論文本文は開けなかった。巻・ページは【未確認】）。アマゾンが「手つかずの原生林」ではなく人が改変した景観だったという議論と結び付く。アンデス高地（ジャガイモ・キヌア・ラクダ科の家畜）の起源については今回一次資料を確認できなかった【未確認】。

## 主張 V11
- 内容：北米東部は独立した植物栽培化の中心である。栽培化の形態的証拠の最古は、カボチャ（Cucurbita pepo）約5025年前（ミズーリ州フィリップス・スプリング）、ヒマワリ約4840年前、マーシュエルダー（Iva annua）約4400年前、アカザ（Chenopodium berlandieri）約3700年前（いずれも較正年代）。
- ラベル：事実
- 確信度：high
- 出典：Smith, B. D. "Eastern North America as an independent center of plant domestication"｜PNAS 103(33):12223–12228｜2006｜https://pmc.ncbi.nlm.nih.gov/articles/PMC1567861 （DOI: 10.1073/pnas.0604335103）
- 関連ノード：evt.agriculture
- 補足：トウモロコシは後にメソアメリカから伝わった作物で、北米東部の在来作物群（Eastern Agricultural Complex）とは別。農耕起源の「周縁」とみなされがちな地域でも独自の栽培化があった例。

## 主張 V12
- 内容：アフリカ西部（マリ北部）のトウジンビエ（パールミレット）は、紀元前5千年紀に野生型が土器の混和材として使われ、紀元前4千年紀に栽培化前の栽培が始まったと推定され、紀元前3千年紀半ばに栽培化の特徴（非脱粒性など）が明確になり、約2000 BC までに固定したとされる。栽培型はその後、東スーダン（約1850 BC）とインド（約1700 BC）に達した。
- ラベル：事実（年代）／理論（栽培開始の推定）
- 確信度：medium
- 出典：Fuller, D. Q. et al. "Transition From Wild to Domesticated Pearl Millet (Pennisetum glaucum) Revealed in Ceramic Temper at Three Middle Holocene Sites in Northern Mali"｜African Archaeological Review 38(2):211–230｜2021｜https://pmc.ncbi.nlm.nih.gov/articles/PMC8550313 （DOI: 10.1007/s10437-021-09428-8）
- 関連ノード：evt.agriculture
- 補足：同論文は Winchell ら（2018）を引き、アフリカの穀物栽培に「中央サハラの小粒の雑穀、東サヘルのモロコシ、西サヘルのトウジンビエ」の3つの並行した経路を挙げる。アフリカでは牛の牧畜が作物の栽培化より先行した。モロコシの栽培化年代は今回一次資料で確認できなかった【未確認】。

## 主張 V13
- 内容：2026年、南レバントの3000〜6000年前のコムギの粒の古代ゲノム解析から、栽培コムギの成立は「モザイク状」で、非脱粒性に関わる2つの遺伝子（TtBtr1-A と TtBtr1-B）の変異が北と南の野生集団で別々に生じ、それらの交雑によって組み合わさった（少なくとも2回）とするモデルが提案された。その後も野生エンマーコムギからの遺伝子流入が続いた。
- ラベル：仮説（新しいモデル）
- 確信度：medium
- 出典：Lev-Mirom, Y. et al. "Ancient grains illuminate the mosaic origin of domesticated wheat"｜Nature Plants 12(5):954–963｜2026｜https://cris.huji.ac.il/en/publications/ancient-grains-illuminate-the-mosaic-origin-of-domesticated-wheat/ （DOI: 10.1038/s41477-026-02283-y）
- 関連ノード：evt.agriculture、con.protracted-domestication（新規候補）
- 補足：単一の場所・単一の発明という見方への反証材料になる。発行日は機関ページで「2026年5月号」とあるが、メタデータに別の日付も記載されており、正確な公開日は要再確認。時事候補。

---

## B. 農耕が始まった理由

## 主張 V14
- 内容：気候仮説：Richerson・Boyd・Bettinger（2001）は、更新世（氷期）には気候が10年単位で激変し、大気中のCO2も低かったため農耕は事実上不可能だったが、完新世に気候が安定し、CO2と降水が増えたことで多くの地域で農耕が可能になった、と論じた。ただし気候だけでは足りず、社会制度と技術の発達に数千年を要したとも述べる。
- ラベル：理論（有力な説明の一つ）
- 確信度：medium
- 出典：Richerson, P. J., Boyd, R., Bettinger, R. L. "Was Agriculture Impossible during the Pleistocene but Mandatory during the Holocene? A Climate Change Hypothesis"｜American Antiquity 66(3)｜2001｜https://www.doi.org/10.2307/2694241 ／UC Davis News「Cold Planet Stopped Agriculture From Developing」｜https://www.ucdavis.edu/news/cold-planet-stopped-agriculture-developing
- 関連ノード：evt.agriculture、新規候補 thy.holocene-climate-agriculture（完新世の気候安定仮説、level: theory、親: evt.agriculture）
- 補足：「なぜ1万年前ごろ複数地域でほぼ同時に？」への最も強い答えの一つ。気候は必要条件（不可能を可能にする）であって十分条件ではない、という論理の区別を教材で示すとよい。題名の「mandatory（必須）」は強い主張で、農耕をしなかった完新世の社会（縄文など、V25）が反例になる。

## 主張 V15
- 内容：ヤンガードリアス（約1.29万〜1.17万年前の急な寒冷化の揺り戻し）が、レバントのナトゥーフ文化の人々に野生穀物の栽培を促したという説（Bar-Yosef ら）がある。
- ラベル：仮説（論争中）
- 確信度：low
- 出典：Bar-Yosef, O. "The Natufian culture in the Levant, threshold to the origins of agriculture"｜Evolutionary Anthropology 6(5)｜1998｜（書誌の実在は検索で確認。本文は未読）https://www.scilit.net/publications/437ba7050fb81a5391496590e74508f9
- 関連ノード：thy.holocene-climate-agriculture（新規候補）
- 補足：ヤンガードリアスの年代と、その影響で栽培が始まったという因果の具体的な内容は【未確認】（記憶による）。年代の再検討により、栽培の開始とヤンガードリアスの対応関係を疑う研究もある【未確認】。

## 主張 V16
- 内容：Zeder（2015）は、栽培化の説明として、最適採餌理論（資源が減ったため効率の悪い食料に手を出したという「押し出し」型）よりも、ニッチ構築理論（人が環境を意図的・非意図的に改変し、その結果が選択を変えるという見方）に基づく枠組みの方が経験的な支持が大きいと論じる。
- ラベル：論争（学派間の対立）
- 確信度：medium
- 出典：Zeder, M. A. "Core questions in domestication research"｜PNAS 112(11):3191–3198｜2015｜https://ui.adsabs.harvard.edu/abs/2015PNAS..112.3191Z （DOI: 10.1073/pnas.1501711112）
- 関連ノード：新規候補 thy.niche-construction（ニッチ構築、level: theory、親: evt.agriculture／con.cumulative-culture と関連）
- 補足：最適採餌理論側からの反論（ニッチ構築は検証可能な予測を出しにくい、等）もある【未確認】。教材では「人口圧・資源不足（押し出し）」「豊かな環境での管理の深まり（引き込み）」「社会的動機」の3系統を並べるとよい。

## 主張 V17
- 内容：社会的要因説（宴会・威信）：B. Hayden は、威信を競う宴会のために余剰食料や特別な食料（酒など）を求めたことが栽培化を促したと論じた。
- ラベル：仮説
- 確信度：low
- 出典：【未確認】（Hayden の主要論文を今回開けていない。ギョベクリ・テペの宴会説は V21 の Banning 2023 が言及）
- 関連ノード：thy.niche-construction（新規候補）と並ぶ説明の一つとして
- 補足：検証が難しい説。ギョベクリ・テペなどで「宴会」の痕跡がどう解釈されるかと結び付く。

## 主張 V18
- 内容：農耕は当初から「生活の質の向上」だったわけではない。成人の身長は、農業への依存が強まるにつれ、多くの地域・時期で全般に低下した。人口密度の上昇と感染症の増加が要因として挙げられ、感染症・歯の病気・栄養欠乏の増加を示した以前の研究（Cohen & Armelagos 1984）の結論は新しいデータでも維持された。
- ラベル：理論（強い証拠のある一般化）
- 確信度：medium
- 出典：Mummert, A., Esche, E., Robinson, J., Armelagos, G. J. "Stature and robusticity during the agricultural transition: Evidence from the bioarchaeological record"｜Economics & Human Biology 9(3):284–301｜2011｜https://ideas.repec.org/a/eee/ehbiol/v9y2011i3p284-301.html
- 関連ノード：新規候補 con.neolithic-health-costs（農耕移行の健康への代償、level: concept、親: evt.agriculture）
- 補足：地域差・例外がある（一律ではない）。身長は健康の指標の一つにすぎない。「農耕は人類最大の過ち」（Diamond 1987 のエッセイ）のような強い言い方は価値判断を含むため、事実と分けて扱う。

## 主張 V19
- 内容：新石器時代の人口転換（Neolithic Demographic Transition）：世界各地の墓地のデータで、採集から農耕への移行期に子どもの骨の割合が急増する。Bocquet-Appel はこれを出生率の上昇（女性1人あたり約2人の増加と推定）による人口増加の始まりと解釈した。
- ラベル：理論
- 確信度：medium
- 出典：Bocquet-Appel, J.-P. "When the World's Population Took Off: The Springboard of the Neolithic Demographic Transition"｜Science 333(6042):560–561｜2011｜（書誌とアブストラクトを図書館目録で確認）https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_hal_primary_oai_HAL_hal_00834316v1 （DOI: 10.1126/science.1208880）
- 関連ノード：新規候補 con.neolithic-demographic-transition（新石器時代の人口転換、level: concept、親: evt.agriculture）
- 補足：健康の悪化（V18）と人口の増加は矛盾しない。個人の健康が悪くても出生が増えれば集団は増える、という点が教材の良い問いになる。墓地の年齢推定の偏りへの批判もある【未確認】。

## 主張 V20
- 内容：農耕はアイデアだけでなく人の移動によっても広がった。古代DNAによれば、ヨーロッパ各地の初期農耕民は、ギリシャ北部・アナトリア北西部の新石器時代の集団から途切れない祖先のつながりで由来する（Hofmanová ら 2016）。ドイツ・ハンガリー・スペインの初期農耕民（約8000〜7000年前）は在来の狩猟採集民と遺伝的に異なる近縁な集団だった。さらに約4500年前、ステップのヤムナヤ系の集団がヨーロッパに大規模に移動し（ドイツの縄目文土器文化の人々は祖先の約75%がヤムナヤ系）、インド・ヨーロッパ語の一部の拡散と結び付けられている（Haak ら 2015）。
- ラベル：事実（遺伝的な系統）／理論（言語の拡散との結び付き）
- 確信度：high（農耕民の移住）、medium（言語との結び付き）
- 出典：Hofmanová, Z. et al. "Early farmers from across Europe directly descended from Neolithic Aegeans"｜PNAS 113(25):6886–6891｜2016｜https://pmc.ncbi.nlm.nih.gov/articles/PMC4922144 （DOI: 10.1073/pnas.1523951113）／Haak, W. et al. "Massive migration from the steppe was a source for Indo-European languages in Europe"｜Nature 522:207–211｜2015｜https://pubmed.ncbi.nlm.nih.gov/25731166/ （DOI: 10.1038/nature14317）
- 関連ノード：新規候補 con.farming-dispersal（農耕の拡散：人の移動と文化の伝播、level: concept、親: evt.agriculture）
- 補足：「移住か、文化の伝播か」は地域で異なる。南米アンデス南部では在来の狩猟採集民が自ら農耕を採用した例（V43）がある。遺伝子の系統と言語・民族の同一視は避ける。

---

## C. ギョベクリ・テペと縄文：農耕なしの巨大建造・定住

## 主張 V21
- 内容：トルコ南東部のギョベクリ・テペは、先土器新石器時代（約9600〜8200 BCE）に狩猟採集民の集団が建てた巨石建造物群で、高さ最大5.5mのT字形の石灰岩の柱に野生動物などが浮き彫りされている。UNESCO は儀礼（葬送儀礼の可能性）と社会的な催しに使われたとする。
- ラベル：事実（年代・建造者が狩猟採集民であること）／理論（用途）
- 確信度：high
- 出典：Göbekli Tepe｜UNESCO World Heritage Centre｜（2018年登録【未確認：ページ上で年を確認できず】）｜https://whc.unesco.org/en/list/1572/
- 関連ノード：新規候補 evt.gobekli-tepe（ギョベクリ・テペ、level: event、親: evt.agriculture）
- 補足：「狩猟採集民が、農耕以前に大規模な共同作業をした」ことが重要。依頼文の「約1.15万年前」は 9600 BCE ≒ 1.16万年前で整合。

## 主張 V22
- 内容：発掘者 K. シュミットの「狩猟採集民の祭祀センター（世界最初の神殿）で、人は住んでいなかった」という解釈は修正されつつある。Banning（2023）の総説によれば、発掘チームは現在、炉や廃棄物層をもつ小型の非モニュメント的建物（住居的要素）を認め、岩を掘った穴や溝を貯水施設の可能性として扱い、数千点のすり石（穀物加工の使用痕）や野生・栽培の可能性がある穀物のケイ酸体も報告している。大型の建物に屋根があった可能性も一部で受け入れられている。
- ラベル：論争
- 確信度：medium
- 出典：Banning, E. B. "Paradise Found or Common Sense Lost? Göbekli Tepe's Last Decade as a Pre-Farming Cult Centre"｜Open Archaeology 9(1):20220317｜2023｜https://www.degruyterbrill.com/document/doi/10.1515/opar-2022-0317/html （DOI: 10.1515/opar-2022-0317）
- 関連ノード：evt.gobekli-tepe（新規候補）
- 補足：Banning はシュミットの初期の批判者であり、発掘チーム側は家庭的な廃棄物を「宴会」の痕跡と解釈する立場も残している（Banning はそれを批判）。「神殿が先、農耕が後」という単純な物語は、一般向けの説明に今も残るが、研究上は「定住的な集落の中の特別な建物」へと見方が移っている。両論を併記する。

## 主張 V23
- 内容：中国江西省の仙人洞（Xianrendong）遺跡の土器片は約2万年前（最終氷期）のもので、東アジアの狩猟採集民は定住や農耕より約1万年前から土器を使っていた。
- ラベル：事実
- 確信度：high
- 出典：Wu, X. et al. "Early Pottery at 20,000 Years Ago in Xianrendong Cave, China"｜Science 336(6089):1696–1700｜2012｜（書誌はボストン大学の発表で確認）https://www.bu.edu/articles/2012/a-prehistoric-pottery-barn/
- 関連ノード：新規候補 con.pottery-before-farming（農耕より古い土器、level: concept、親: thm.civilization）
- 補足：「土器＝新石器時代＝農耕」という西アジア・ヨーロッパ由来の図式は東アジアに当てはまらない（con.periodization と関連）。

## 主張 V24
- 内容：青森県の大平山元Ⅰ遺跡の最古段階の土器に付着した炭化物の年代は、未較正で約1万2680〜1万3780 BP（Nakamura ら 2001）。較正すると約1.6万年前前後になり、日本最古級の土器とされる。
- ラベル：事実（未較正年代）／【未確認】（較正年代の具体的な値「約1万6500年前」）
- 確信度：medium
- 出典：Nakamura, T., Taniguchi, Y., Tsuji, S., Oda, H. "Radiocarbon Dating of Charred Residues on the Earliest Pottery in Japan"｜Radiocarbon 43(2B)｜2001｜https://www.cambridge.org/core/journals/radiocarbon/article/radiocarbon-dating-of-charred-residues-on-the-earliest-pottery-in-japan/D2DE167CFF67D9B361D5D2E3AF198BD8 （DOI: 10.1017/S0033822200041783）
- 関連ノード：con.pottery-before-farming（新規候補）、新規候補 evt.jomon（縄文文化）
- 補足：較正値（約1万6500年前とされることが多い）は今回の確認ページに数値がなく、教材に載せる前に原典の較正結果で確認が必要。土器が付いた試料と年代の対応にも議論があり得る。

## 主張 V25
- 内容：「北海道・北東北の縄文遺跡群」（17遺跡）は2021年に世界遺産に登録された。UNESCO によれば、縄文の人々は狩猟・漁労・採集による定住社会で、約1.5万年前（土器の出現）から定住を始め、約1万年以上にわたり農耕に移行せずにこの暮らしを続けた（登録範囲は約13,000〜400 BCE）。
- ラベル：事実
- 確信度：high
- 出典：World Heritage Committee decision on "Jomon Prehistoric Sites in Northern Japan"（第44回拡大会合）｜UNESCO World Heritage Committee｜2021｜https://whc.unesco.org/en/decisions/7956
- 関連ノード：新規候補 evt.jomon（縄文文化：農耕なしの定住、level: event、親: thm.civilization）
- 補足：「定住→農耕→国家」という一本道への強い反例。ただし縄文に植物の管理（クリなど）や小規模な栽培がなかったわけではない（V26）。決定番号の枝番は【未確認】。

## 主張 V26
- 内容：三内丸山遺跡（青森市）は縄文時代前期〜中期（約5900〜4300年前）の最大級の集落の一つで、500以上の竪穴住居、最大32mの大型建物、約500基の成人の墓、直径約1mのクリの柱6本の大型掘立柱建物などがある。花粉分析ではナラ・ブナの森がクルミ類、やがてほぼクリに置き換わり、植栽や手入れなど積極的な管理を示すとする研究者もいる。ヒスイは約500km、黒曜石は最大約580km離れた産地から運ばれた。
- ラベル：事実（規模・遺構）／理論（クリの管理）
- 確信度：high（遺構）、medium（クリの管理）
- 出典：The Sannai Maruyama Site｜Jomon Prehistoric Sites in Northern Japan（推薦主体の公式サイト）｜2021｜https://jomon-japan.jp/en/wp-content/uploads/2021/02/F006b000002b.pdf
- 関連ノード：evt.jomon（新規候補）、con.trade-networks
- 補足：遺跡全体の約40%しか発掘されていない。依頼文の「三内丸山」は年代を約5900〜4200年前とする資料もあり、終わりの年代は資料で幅がある。ニワトコの種子の集積から果実酒を推定する説は可能性にとどまる。

## 主張 V27
- 内容：日本への水稲農耕の到来（弥生時代の始まり）は、国立歴史民俗博物館の AMS 炭素14年代測定により、北部九州で紀元前10世紀後半とされ、従来の説より約500年さかのぼった。近畿の弥生前期の始まりは紀元前8〜7世紀と推定される。
- ラベル：論争（年代の早期化は有力だが、反対意見もある）
- 確信度：medium
- 出典：今村峯雄（研究代表）「縄文・弥生時代の高精度年代体系の構築」実績報告（2003年度）｜KAKEN（科学研究費助成事業データベース）｜2004｜https://kaken.nii.ac.jp/ja/report/KAKENHI-PROJECT-13308009/133080092003jisseki ／小林青樹「（弥生開始年代についての記事）」｜JSPS 科研費NEWS 2011 vol.2｜https://www.jsps.go.jp/j-grantsinaid/22_letter/data/news_2011_vol2/p-5.pdf
- 関連ノード：新規候補 evt.yayoi-rice（日本列島への水稲農耕の到来、level: event、親: con.farming-dispersal）
- 補足：土器付着炭化物の「海洋リザーバー効果」（海産物由来の炭素で古く出る）などを理由に、早期化に慎重な研究者もいる【未確認】。拡散は列島内で地域差が大きく、北海道・南西諸島は水稲農耕を受け入れなかった【未確認】。

---

## D. 都市

## 主張 V28
- 内容：チャタルヒュユク（トルコ中部）の東丘には18の新石器時代の層があり、約7400〜6200 BC にわたる。面積は約37ha、2000年以上同じ場所で維持された。通りがなく家々が背中合わせに密集し、屋根から出入りした。住居の規模はほぼ同等で、UNESCO は「主に平等主義的な原則に基づく」集落とする。
- ラベル：事実（年代・構造）／理論（平等主義の解釈）
- 確信度：high
- 出典：Neolithic Site of Çatalhöyük｜UNESCO World Heritage Centre｜（2012年登録【未確認】）｜https://whc.unesco.org/en/list/1405
- 関連ノード：新規候補 evt.catalhoyuk（チャタルヒュユク、level: event、親: evt.early-states または新規 con.city-vs-state）
- 補足：数千人規模の大集落だが、宮殿・神殿・行政の痕跡がなく、国家ではない。「大きな集落＝都市＝国家」ではないことを示す代表例。

## 主張 V29
- 内容：チャタルヒュユクの131人の古代DNA解析（2025年）では、同じ建物に埋葬された人どうしは父系より母系でより近縁だった。紀元前7千年紀には女性の系統が男性の系統より重要だったとされ、世帯レベルでの母方居住の可能性がある。ただし同じ家に埋葬された人の多くは互いに血縁がなく、世帯は血縁以外の原理でも構成されていた。研究者自身は「女性が権力を持つ母権制」を示すものではないとしている。
- ラベル：事実（遺伝的な関係）／理論（社会構造の解釈）
- 確信度：medium
- 出典：Yüncü, E. et al. "Female lineages and changing kinship patterns in Neolithic Çatalhöyük"｜Science｜2025（ボン大学の発表 2025-06-27）｜https://www.uni-bonn.de/en/news/was-the-neolithic-settlement-at-catalhoyuk-a-matriarchate （DOI: 10.1126/science.adr2915）
- 関連ノード：evt.catalhoyuk（新規候補）
- 補足：時事候補（2025年）。居住パターンは権力関係の直接の証拠ではない。報道の一部は「女性中心の社会」と強く見出しを付けているが、原典の主張はより慎重。

## 主張 V30
- 内容：メソポタミア南部のウルクは紀元前3100年までに約250ha、北部のテル・ブラクは紀元前4千年紀半ばまでに約130haに達した。J. ウルは、都市を「血縁から合理的な官僚国家への革命的転換」ではなく、「家（世帯）」の比喩が神殿・都市へと拡大した結果として説明し、都市は多くの点で意図されない結果だったと論じる。
- ラベル：事実（面積）／理論（ウルの解釈）
- 確信度：high（面積）、medium（解釈）
- 出典：Ur, J. "Households and the Emergence of Cities in Ancient Mesopotamia"｜Cambridge Archaeological Journal 24(2):249–268｜2014｜https://scholar.harvard.edu/sites/scholar.harvard.edu/files/jasonur/files/ur_2014_caj_households_and_the_emergence_of_cities.pdf （DOI: 10.1017/S095977431400047X）
- 関連ノード：evt.early-states、新規候補 evt.uruk（ウルクと最初の都市、level: event、親: evt.early-states）
- 補足：人口の推定値は同論文にない（一般向けに「数万人」とされることが多いが【未確認】）。テル・ブラクの存在は「南部だけが都市化した」という単線の見方への修正になる。

## 主張 V31
- 内容：インダス文明のモヘンジョダロは紀元前3千年紀の都市で、UNESCO は繁栄を約2500〜1500 BC とする。西に高い基壇上の城塞部、東に直角に交わる街路の下町があり、精巧な排水システム・井戸・汚水溜め、大浴場などがある。
- ラベル：事実
- 確信度：high（構造）、medium（年代の幅）
- 出典：Archaeological Ruins at Moenjodaro｜UNESCO World Heritage Centre｜https://whc.unesco.org/en/list/138
- 関連ノード：evt.early-states
- 補足：UNESCO の「穀物倉」「神官の学院」といった名称は発掘初期の解釈に由来し、現在の研究では疑問視されている【未確認】。インダスでは王墓や王の像が明確でなく、支配の形が他の文明と異なる可能性がある（論争）【未確認】。年代も UNESCO の記載と、成熟期を約2600〜1900 BC とする一般的な区分の間に差がある【未確認】。

## 主張 V32
- 内容：中国の二里頭（にりとう）遺跡（河南省）は、中国の初期国家・初期都市の候補として重要で、炭素14のウィグルマッチングで年代が絞り込まれてきた。Liu & Xu（2007）は、二里頭を伝説上の「夏王朝」と前提として同一視する伝統的な方法を批判し、文献史と考古学の編年を切り離すべきだと論じた。
- ラベル：論争（夏王朝との同一視）
- 確信度：medium
- 出典：Zhang, X. et al. "14C Dating of the Erlitou Site"｜Radiocarbon 64(4)｜2022｜https://www.cambridge.org/core/journals/radiocarbon/article/14c-dating-of-the-erlitou-site/475359D750D8F9AE70E5126CF4744A4C （DOI: 10.1017/RDC.2021.72）／Liu, L., Xu, H. "Rethinking Erlitou: legend, history and Chinese archaeology"｜Antiquity 81(314):886–901｜2007｜DOI: 10.1017/S0003598X00095983
- 関連ノード：evt.early-states
- 補足：二里頭文化の具体的な年代（約1750〜1520 BC とされることが多い）は今回のページで数値を確認できなかった【未確認】。殷（商）の後期の都・殷墟（安陽）は甲骨文の出土地（V39）。

## 主張 V33
- 内容：ペルーのスーペ谷のカラル（Caral-Supe）は約5000年前（後期アルカイック期、3000〜1800 BC）に建設され、約1000年間使われた。6つの大型の基壇、5つの広場、円形の沈み広場、住居群がある。ICOMOS は「アメリカ大陸の文明の発祥地」と評価し、ギャラリー・ピラミッドから中央アンデス最古とされるキープ（結び目の記録具）が出土したと記す。
- ラベル：事実（年代・遺構）／論争（「都市」「国家」と呼べるか）
- 確信度：high（年代）、medium（評価）
- 出典：ICOMOS evaluation, Sacred City of Caral-Supe (Peru) No 1269｜ICOMOS／UNESCO｜2009｜https://whc.unesco.org/document/152221
- 関連ノード：evt.early-states、新規候補 con.city-vs-state
- 補足：メソポタミア・エジプトとほぼ同時期に、土器も文字もない社会が大規模な公共建築をもった。国家だったか（首長制か）は論争【未確認】。キープの年代の確実性も慎重に扱う。2009年に世界遺産登録【未確認】。

## 主張 V34
- 内容：メキシコのテオティワカンは紀元1〜7世紀に建設・使用された都市で、最盛期には約36km²、住民は少なくとも2万5000人（UNESCO）。太陽のピラミッドは底辺225×222m、高さ75m。7世紀に焼かれ放棄された。
- ラベル：事実
- 確信度：high（遺構）、medium（人口）
- 出典：Pre-Hispanic City of Teotihuacan｜UNESCO World Heritage Centre｜https://whc.unesco.org/en/list/414
- 関連ノード：evt.early-states
- 補足：UNESCO の人口「少なくとも2.5万人」は控えめな値で、研究者の推定は10万人前後とするものが多い【未確認】。支配者の名前や王墓が明確でなく、集団的な統治だった可能性が議論されている【未確認】。

## 主張 V35
- 内容：マリのジェンネ＝ジェノは、紀元前3世紀（約250 BC）から人が住んだイスラーム以前の都市遺跡で、円形・方形の泥レンガの住居、葬送用の甕、鉄の鉱滓などが見つかっている。
- ラベル：事実
- 確信度：high
- 出典：Old Towns of Djenné｜UNESCO World Heritage Centre｜https://whc.unesco.org/en/list/116
- 関連ノード：evt.early-states、新規候補 con.city-vs-state
- 補足：ジェンネ＝ジェノは、宮殿や中央集権の明確な痕跡がないまま発展した「異質な（ヘテラーキー的な）都市」の例とされる（R. & S. McIntosh）【未確認】。都市化が必ずしも国家の形成と同時ではないことを示す。

## 主張 V36
- 内容：Graeber & Wengrow『The Dawn of Everything』（2021）は、狩猟採集民が季節ごとに政治体制を切り替えた例（クワキウトルなど）を挙げ、農耕への移行は実験的・漸進的で、約6000年前のメソポタミアなどの初期の都市には地区評議会や市民集会による集団的な意思決定があったと論じる。また国家を「暴力の支配・知識の官僚的管理・支配者のカリスマ」の3要素の組み合わせとして捉える。
- ラベル：論争（挑戦的な再解釈。専門家からの批判も多い）
- 確信度：medium（書籍の主張の要約として）
- 出典：Bower, B.「'The Dawn of Everything' rewrites 40,000 years of human history」｜Science News｜2021｜https://www.sciencenews.org/article/human-history-society-dawn-of-everything-book ／（批判）Scheidel, W. の書評｜https://zenodo.org/records/5907061/files/Scheidel%20on%20Graeber%20and%20Wengrow.pdf（実在は検索で確認、本文未読）
- 関連ノード：evt.early-states、新規候補 con.city-vs-state
- 補足：歴史学者 W. シャイデルらは、証拠を引き伸ばしている、例外を一般化していると批判している【未確認：批判の具体的内容は未読】。教材では「平等な大集落があった」という事実と、「人類は常に自由に体制を選べた」という一般化を区別する。

---

## E. 国家

## 主張 V37
- 内容：灌漑説：K. ウィットフォーゲル（『Oriental Despotism（東洋的専制）』1957）は、大規模な灌漑・治水を国家が管理する必要から官僚的・専制的な国家が生まれたと論じた（例：エジプト、メソポタミア、中国、インド、先コロンブス期のメキシコ・ペルー）。批判として、灌漑の重要性の過大評価、挙げた特徴が一緒に現れないこと、モデルが静的であることが挙げられ、R. M. アダムズは考古学的証拠が灌漑を強制的政治制度の主因とすることを支持しないと論じた（ただし灌漑が政治的支配の強化に役立った可能性は認めた）。
- ラベル：理論（現在は主因としては支持が少ない）
- 確信度：medium
- 出典：「Hydraulic civilization」｜Encyclopaedia Britannica｜（閲覧 2026-11-25）｜https://www.britannica.com/topic/hydraulic-civilization
- 関連ノード：新規候補 thy.state-formation（国家形成の諸説、level: theory、親: evt.early-states）
- 補足：「メソポタミアでは大規模灌漑は国家成立の後に発達した」という具体的な批判は今回の資料に記載がなく【未確認】。冷戦期の政治的文脈（ソ連・中国批判）の中で書かれた本である点も、学説史として示す価値がある【未確認】。

## 主張 V38
- 内容：戦争・環境限定説：R. カーネイロ（1970）は、社会契約説・余剰自動発生説・灌漑説のような「自発的」な説明を退け、強制力（主に戦争）が国家形成を進めたと論じた。戦争は国家のない場所でも起きるため必要条件にすぎず、山・海・砂漠に囲まれて敗者が逃げられない「環境の限定（circumscription）」が加わると国家が生じる、とする。例としてペルーの山地・海岸の谷、ナイル、チグリス・ユーフラテス、インダス、メキシコ盆地を挙げる。
- ラベル：理論
- 確信度：medium
- 出典：Carneiro, R. L. "A Theory of the Origin of the State"｜Science 169:733–738｜1970｜https://eml.berkeley.edu/~saez/course/carneiro70.pdf
- 関連ノード：thy.state-formation（新規候補）
- 補足：必要条件と十分条件を区別した議論の好例（CLAUDE.md §3-4 に対応）。反例として、限定のない地域での国家形成や、限定された地域で国家が生じなかった例が議論される【未確認】。

## 主張 V39
- 内容：穀物と課税：J. C. スコット『Against the Grain』（2017）は、初期の国家はすべて穀物（雑穀・ムギ類など）と不自由な労働に依拠し、農耕・家畜・捕虜などの「家畜化」の積み重ねの上に成り立ったと論じる。定住を避けた人々の利点、密集による感染症、国家の外の「野蛮人」と国家の緊張も扱う。
- ラベル：理論（解釈的な総合）
- 確信度：medium
- 出典：「Against the Grain: A Deep History of the Earliest States」｜Yale News｜2017-08-28｜https://news.yale.edu/2017/08/28/against-grain-deep-history-earliest-states
- 関連ノード：thy.state-formation（新規候補）、新規候補 con.outside-the-state（国家の外の人々、level: concept、親: evt.early-states）
- 補足：スコットの「穀物は目に見え、分割でき、査定でき、貯蔵できるので課税に向く」という論点、および「初期国家は脆く頻繁に崩壊した」という論点は、今回確認したページには明記されていない【未確認】。

## 主張 V40
- 内容：Mayshar・Moav・Pascali（2022）は、農耕による土地生産性の上昇が余剰を生み国家を生んだという通説に挑み、収奪しやすい（appropriable）穀物への依存が階層化をもたらしたと論じる。複数のデータセットで、穀物栽培が階層に因果的な効果をもち、土地生産性には同様の効果が見られないと報告した。
- ラベル：理論（実証研究による支持。スコットの議論と親和的）
- 確信度：medium
- 出典：Mayshar, J., Moav, O., Pascali, L. "The Origin of the State: Land Productivity or Appropriability?"｜Journal of Political Economy 130(4):1091–1144｜2022｜https://econpapers.repec.org/RePEc:ucp:jpolec:doi:10.1086/718372 （DOI: 10.1086/718372）
- 関連ノード：thy.state-formation（新規候補）
- 補足：根栽農耕（V8 のニューギニアなど）では国家が生まれにくかった理由の説明として使える。ただし経済学の操作変数による因果推定には前提があり、考古学者の評価は分かれる【未確認】。

## 主張 V41
- 内容：国家の定義：社会科学では、国家を「一定の領域内で正当な物理的強制力の独占を（うまく）主張する人間の共同体」とする M. ウェーバーの定義がよく使われる。考古学では、官僚制（専門の行政官）、課税・貢納、強制力、階層化した居住地（3〜4段階の集落階層）などを指標として、首長制と区別することが多い。
- ラベル：理論（作業定義。単一の合意はない）
- 確信度：medium
- 出典：【未確認】（ウェーバー『職業としての政治』1919 の定義、および Wright & Johnson 1975 の集落階層の指標は記憶による。今回一次資料を開けていない）
- 関連ノード：evt.early-states、thy.state-formation（新規候補）
- 補足：定義によって「最初の国家」の場所・時期が変わる（例：カラル、インダス、テオティワカンを国家とみなすか）。教材では定義を先に明示すること。

## 主張 V42
- 内容：国家・複雑社会の崩壊：J. テインター『The Collapse of Complex Societies』（1988）は、社会が問題解決のために複雑さ（官僚・軍・インフラ）を増すと、その投資の限界的な見返りが減少し、やがて崩壊に至りやすいと論じた。
- ラベル：理論
- 確信度：medium
- 出典：Tainter, J. A. The Collapse of Complex Societies｜Cambridge University Press｜1988｜（Nature 誌の書評で実在を確認）https://www.nature.com/articles/335021a0
- 関連ノード：新規候補 con.state-fragility（国家の脆さと崩壊、level: concept、親: evt.early-states）
- 補足：崩壊を「文明の終わり」ではなく「より単純な組織への再編」とみる見方もあり、崩壊後も人々の暮らしは続く。気候・災害・内紛など原因を一つに単純化しない（CLAUDE.md §3-4）。

## 主張 V43
- 内容：アンデス南部（アルゼンチンのウスパジャタ谷）の46人の古代ゲノム（2026年）では、狩猟採集民（約2200年前）と後の農耕民の間に強い遺伝的連続性があり、在来の人々が農耕を採用した。トウモロコシの消費は時期によって増減し、完全な依存への一方向の移行ではなかった。約800〜600年前にトウモロコシに強く依存した移住者の集団は、気候の不安定・子どもの栄養不良・結核などと重なって長期的な人口減少を経験した。
- ラベル：事実（遺伝・同位体データ）／理論（危機の解釈）
- 確信度：medium
- 出典：Barberena, R. et al. "Local agricultural transition, crisis and migration in the Southern Andes"｜Nature｜2026（ScienceDaily 2026-03-21）｜https://www.sciencedaily.com/releases/2026/03/260321012642.htm （DOI: 10.1038/s41586-026-10233-z）
- 関連ノード：con.farming-dispersal（新規候補）、con.neolithic-health-costs（新規候補）
- 補足：時事候補（2026年）。農耕への依存が「進歩」ではなく危機を招き得たこと、農耕の採用が可逆的・揺れ動くものだったことを示す。報道（ScienceDaily）経由の確認のため、原典で数値を再確認するべき。

## 主張 V44
- 内容：約1万6000人分の古代ゲノム（西ユーラシア）の解析（2026年）では、過去1万年に数百の遺伝子変異に方向性選択がかかっており、農耕への移行後に選択が加速した。強く選択された479の対立遺伝子が特定され、例としてコムギ農耕の開始後に頻度が上がったグルテン不耐症（セリアック病）の主要なリスク変異がある。ただし方向性選択は遺伝子頻度の変化の約2%を説明するにすぎない。
- ラベル：事実（統計的検出）／理論（農耕との因果の解釈）
- 確信度：medium
- 出典：Akbari, A. et al. "Ancient DNA reveals pervasive directional selection across West Eurasia"｜Nature｜2026-04-15 オンライン｜https://www.broadinstitute.org/news/massive-ancient-dna-study-reveals-natural-selection-has-accelerated-recent-human-evolution （DOI: 10.1038/s41586-026-10358-1）
- 関連ノード：con.natural-selection、新規候補 con.neolithic-health-costs
- 補足：時事候補（2026年）。現代の形質との関連が古代に選択された理由を示すとは限らない。西ユーラシアのみの結果。「農耕によって人が賢く・健康になった」という解釈は研究者自身が否定している。

---

## F. 文字

## 主張 V45
- 内容：シカゴ大学東洋研究所（現 ISAC）の展示「Visible Language」（2010）は、文字は書き言葉の知識なしに「ゼロから」少なくとも4回、メソポタミア、エジプト、中国、メソアメリカで発明されたとし、他の文字体系はこれらから派生した可能性が高いとする。メソポタミア最古の楔形文字の粘土板は約3200 BC。
- ラベル：理論（多数説）／論争（エジプトの独立性）
- 確信度：medium
- 出典：「Origins of writing make for engaging new exhibition at Oriental Institute Museum」｜UChicago News｜2010｜https://news.uchicago.edu/story/origins-writing-make-engaging-new-exhibition-oriental-institute-museum ／Woods, C. (ed.) Visible Language: Inventions of Writing in the Ancient Middle East and Beyond｜Oriental Institute Museum Publications 32｜2010｜https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/oimp32.pdf
- 関連ノード：evt.writing
- 補足：エジプトがメソポタミアの影響（「文字というアイデア」の伝播）を受けたかは論争（V48）。インダス文字・ラパヌイのロンゴロンゴなどは未解読で、独立発明かどうか判定できない。

## 主張 V46
- 内容：原楔形文字（proto-cuneiform）は紀元前4千年紀後半（ウルク後期、ウルクⅣ・Ⅲ期、おおむね約3500〜3000 BC の区分内）に現れた。テキストの平均で約85%が行政（会計）文書、約15%が語彙リスト（学習用の単語表）で、ウルクⅣ期の語彙リストはごくわずか、ウルクⅢ期で約20%に増える。Englund は、約3300 BC 以前の粘土の封球（ブッラ）に封入されたトークンの圧痕が初期の「数字の粘土板」の数記号と対応するとして、文字は数記号（会計）から始まったと論じる。
- ラベル：事実（行政文書が大部分であること）／理論（数記号起源）
- 確信度：high（会計中心）、medium（トークンとの系譜）
- 出典：Englund, R. K. "Accounting in Proto-Cuneiform"（Englund 2004 "Proto-cuneiform account-books and journals", in Hudson & Wunsch eds., Creating Economic Order, CDL Press, pp. 23–46 の改訂版）｜CDLI｜2011｜https://cdli.ucla.edu/staff/englund/publications/englund2011a.pdf
- 関連ノード：evt.writing、新規候補 thy.token-theory（トークン説、level: theory、親: evt.writing）
- 補足：文字は「言葉を書き留めるため」ではなく「物と数を管理するため」に始まった、という点が教材の中心的な論点になる。原楔形文字は話し言葉を完全には写さない（文法要素がほとんど書かれない）【未確認】。

## 主張 V47
- 内容：トークン説（D. シュマント＝ベッセラ：新石器時代の小さな粘土製トークンが会計の道具となり、楔形文字に発展した）には強い批判がある。Zimansky（1993）は、トークンと文字記号の対応が見た目の類似に頼り、分類が恣意的で、統計的支持が弱い（例：「羊」のトークンは15点のみ）と批判した。Bennison-Chapman（2019）は約3000点と56遺跡のデータから、トークンは多機能な道具で単純な計数には使われた可能性があるが、農産物の管理のために作られたわけではなく、統一された記号体系でもなかったと論じる。
- ラベル：論争
- 確信度：medium
- 出典：Zimansky, P. Review of Before Writing Vols. I–II｜Journal of Field Archaeology 20(4):513–517｜1993｜https://urkesh.org/attach/Zimansky1993.pdf ／Bennison-Chapman, L. E. "Reconsidering 'Tokens': The Neolithic Origins of Accounting or Multifunctional, Utilitarian Tools?"｜Cambridge Archaeological Journal 29(2):233–259｜2019｜https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/reconsidering-tokens-the-neolithic-origins-of-accounting-or-multifunctional-utilitarian-tools/7E6C04CB040AD8AA0EA84B94D4D275C4 （DOI: 10.1017/S0959774318000513）
- 関連ノード：thy.token-theory（新規候補）
- 補足：「平らなトークン→封球の圧痕→数字の粘土板」という後期（ウルク期）の系譜（V46）は比較的支持されるが、「新石器時代全体のトークンが文字の祖先」という強い版は疑われている、と段階を分けて示すのが公平。

## 主張 V48
- 内容：エジプト・アビドスの先王朝時代の王墓（U-j 墓、いわゆる「スコルピオン1世」の墓）から出た骨・象牙の小さなラベル（各約2×1.5cm、1〜4文字）と墨書土器は、G. ドライヤーにより約3200 BC（封泥は約3400 BC）とされ、エジプト最古の文字とされる。ラベルは物品の量と産地（地名・機関名）を記した。
- ラベル：事実（年代・用途）／論争（メソポタミアからの独立性、年代の幅）
- 確信度：medium
- 出典：「Earliest Egyptian Glyphs」｜Archaeology（Archaeological Institute of America）｜1999｜https://archive.archaeology.org/9903/newsbriefs/egypt.html
- 関連ノード：evt.writing
- 補足：依頼文の「紀元前3250年頃」は、この遺物群の年代として広く引かれる値（約3320〜3150 BC とする資料もある）で、記事は約3200 BC とする。年代の幅を示すこと。この発見により、エジプトの文字がメソポタミアより遅れて伝播したという見方が揺らいだ。

## 主張 V49
- 内容：殷（商）後期の甲骨文の炭素14年代（ベイズ解析）では、武丁（ぶてい）期の甲骨は 1254〜1197 cal BC（68%範囲、各相の誤差は約±10年）で、武丁の在位をこの期間と推定した。甲骨文は2017年に UNESCO「世界の記憶」に登録された。
- ラベル：事実
- 確信度：high
- 出典：Liu, K. et al. "Radiocarbon Dating of Oracle Bones of Late Shang Period in Ancient China"｜Radiocarbon 63(1)｜2021｜https://cambridge.org/core/services/aop-cambridge-core/content/view/S0033822220000909 （DOI: 10.1017/RDC.2020.90）／China Daily「Oracle bones added to UNESCO memory」｜2017-12-26｜https://www.chinadaily.com.cn/a/201712/26/WS5a41b031a31008cf16da379d.html
- 関連ノード：evt.writing
- 補足：甲骨文はすでに成熟した体系で、それ以前の発展段階が見つかっていないことから、より古い起源（竹簡などの消えやすい素材）を想定する説がある【未確認】。依頼文の「約1250 BC」は整合。

## 主張 V50
- 内容：メソアメリカ：ベラクルス州で見つかったカスカハル石板（62の刻まれた記号、一部は最大4回繰り返す）は、オルメカのサン・ロレンソ期（約900 BCE に終わる）の紀元前1千年紀初頭とされ、新大陸最古の文字の候補とされた。ただし道路工事の残土から見つかったため年代は共伴遺物からの間接的な推定で、未解読である。マヤ文字では、グアテマラのサン・バルトロで約300〜200 BC の文字が見つかっている（炭素14は共伴した木材による）。
- ラベル：論争（カスカハル石板の年代・文字性）／事実（サン・バルトロの年代）
- 確信度：low（カスカハル）、medium（サン・バルトロ）
- 出典：Brown University News「Oldest writing in the New World discovered in Veracruz, Mexico」（Rodríguez Martínez, M. del C. et al. "Oldest Writing in the New World", Science 313, 2006 について）｜2006｜https://archive2.news.brown.edu/1987-2007/2006-07/06-021.html ／Science News「Getting a read on early Maya writing」（Saturno, W. A. et al., Science, 2006-03 について）｜2006｜https://www.sciencenews.org/article/getting-read-early-maya-writing
- 関連ノード：evt.writing
- 補足：サポテカ（オアハカ）の文字も初期のメソアメリカ文字の候補だが、今回一次資料を確認していない【未確認】。メソアメリカの文字は暦・王の事績の記録と結び付き、メソポタミアの「会計起源」とは性格が異なる、という対比は教材で使える（ただし保存の偏りに注意）。

## 主張 V51
- 内容：インダス文字は100年以上の研究にもかかわらず未解読である。刻まれた資料は6000点未満で、平均約5記号と短く、背後の言語が不明で、二言語併記の碑文がないことが理由に挙げられる。
- ラベル：未知
- 確信度：high（未解読であること）
- 出典：Mukhopadhyay, B. A. "Semantic scope of Indus inscriptions comprising taxation, trade and craft licensing, commodity control and access control"｜Humanities and Social Sciences Communications 10:972｜2023｜https://www.nature.com/articles/s41599-023-02320-7.pdf （DOI: 10.1057/s41599-023-02320-7）
- 関連ノード：evt.writing、新規候補 q.indus-script（インダス文字は言語を写す文字か、level: question、親: evt.writing）
- 補足：インダス記号が「言語を写す文字」かどうか自体にも論争がある（Farmer ら 2004 は非言語的記号体系と主張【未確認】）。出典の著者は大学所属ではないが査読誌掲載。数値は他の総説で確認するのが望ましい。解読を主張する個人の説は多いが、合意されたものはない。

## 主張 V52
- 内容：アンデスのキープ（結び目の紐による記録）は、主に数を記録する道具とされてきたが、Hyland（2017）はペルー山村に伝わる2つの「書簡キープ」に95の異なる記号を見出し、地域の会計キープよりはるかに多く、ロゴシラビック（表語＋音節）な文字の範囲に入ると論じ、キープが解読可能な文字体系だった可能性を提起した。
- ラベル：論争（キープが文字かどうか）
- 確信度：low
- 出典：Hyland, S. "Writing with Twisted Cords: The Inscriptive Capacity of Andean Khipus"｜Current Anthropology 58(3):412–419｜2017｜https://research-portal.st-andrews.ac.uk/en/publications/writing-with-twisted-cords-the-inscriptive-capacity-of-andean-khi/ （DOI: 10.1086/691682）
- 関連ノード：新規候補 con.khipu（キープ：文字なしの記録、level: concept、親: evt.writing）
- 補足：インカ帝国は（通常の意味での）文字なしで広大な国家を運営したことは広く認められる。これは「国家には文字が必要」という見方への反例（ただし植民地期の記録に依存する部分がある）。キープの最古の例はカラル（V33）と ICOMOS は記す。

## 主張 V53
- 内容：2025年、ボローニャ大学のチームは、文字以前の印章（円筒印章など）の図像のうち、容器や織物の運搬を表す図柄（房飾りの布、網に入った壺）が、原楔形文字の記号（ZATU662、ZATU190 など）の象徴的な前身であると論じた。印章と文字は紀元前4千年紀後半に相乗的に働きつつ、別の体系であり続けた。
- ラベル：仮説
- 確信度：medium
- 出典：Kelley, K., Cartolano, M., Ferrara, S. "Seals and signs: tracing the origins of writing in ancient South-west Asia"｜Antiquity 99(403):64–82｜2025（オンライン 2024-11-05）｜https://www.cambridge.org/core/journals/antiquity/article/seals-and-signs-tracing-the-origins-of-writing-in-ancient-southwest-asia/B3C2D400F3F80A7A0162D9035C9C2804 （DOI: 10.15184/aqy.2024.165）
- 関連ノード：evt.writing、thy.token-theory（新規候補：トークン以外の前身の候補として）
- 補足：時事候補（2025年2月号）。トークン説だけでなく「印章の図像」も文字の源の一つだったという、複数の起源を示す議論。記号の意味の読み（油、亜麻布など）は著者自身も不確実としている。

---

## G. 必然だったのか（総合）

## 主張 V54
- 内容：「農耕→定住→都市→国家→文字」は一本道ではない。反例として、農耕なしの定住・大集落（縄文 V25–V26）、農耕以前の巨大建造物（ギョベクリ・テペ V21）、国家でない大集落（チャタルヒュユク V28）、文字なしの大規模建築・国家（カラル V33、インカのキープ V52）、農耕の採用が揺れ動き危機を招いた例（アンデス南部 V43）がある。
- ラベル：理論（複数の一次資料からの総合。総合そのものはこの報告の解釈）
- 確信度：medium
- 出典：上記各主張の出典
- 関連ノード：thm.civilization、evt.agriculture、evt.early-states、con.periodization
- 補足：一方で、独立した複数の地域が似た順序（栽培化→集落の拡大→階層化）をたどった傾向もあり、「全くの偶然」でもない。「条件がそろうと起こりやすいが、必然ではなく、経路と速さは地域で異なる」という整理が、現在の証拠に最も近い。完新世の気候（V14）は必要条件の候補、穀物（V39–V40）は国家の形の条件の候補として示せる。

---

## 担当範囲で見つけた、地図にない重要な概念
1. con.protracted-domestication（ゆっくりとした栽培化／栽培化前の栽培）— V4, V5, V13
2. thy.holocene-climate-agriculture（完新世の気候安定と農耕の可能化）— V14, V15
3. thy.niche-construction（ニッチ構築による栽培化の説明）— V16（con.cumulative-culture と接続）
4. con.neolithic-demographic-transition（新石器時代の人口転換）— V19
5. con.neolithic-health-costs（農耕移行の健康への代償）— V18, V43, V44
6. con.farming-dispersal（農耕の拡散：移住と伝播、古代DNA）— V20, V27, V43
7. evt.dog-domestication（イヌの家畜化：農耕以前）— V3
8. evt.gobekli-tepe（ギョベクリ・テペと「神殿が先」説の修正）— V21, V22
9. evt.jomon（縄文：農耕なしの定住）と con.pottery-before-farming（農耕より古い土器）— V23–V26
10. evt.yayoi-rice（日本列島への水稲農耕の到来と年代の論争）— V27
11. con.city-vs-state（大集落・都市・国家の区別）— V28, V33, V35, V36
12. thy.state-formation（国家形成の諸説：灌漑・戦争と限定・穀物と収奪）— V37–V41
13. con.outside-the-state（国家の外の人々）と con.state-fragility（国家の脆さと崩壊）— V39, V42
14. thy.token-theory（トークン説とその批判）— V46, V47, V53
15. con.khipu（キープ：文字なしの記録）、q.indus-script（インダス文字の未解読）— V51, V52

## 既存ノードの誤りの疑い
1. **evt.writing**（「紀元前3200年頃からメソポタミアやエジプトなどで文字が使われた」）：大きな誤りではないが、(a) エジプトのアビドスの資料は約3200 BC（封泥は約3400 BC とする見方もある）で、メソポタミアとほぼ同時かやや早い可能性があり、「メソポタミアが先、エジプトが後」と読める書き方は避けるべき（V48）。(b)「他地域でも独自に発展」は曖昧で、「独立発明は少なくとも4回（メソポタミア・エジプト・中国・メソアメリカ）、エジプトの独立性には論争、インダス文字は未解読」と明示した方がよい（V45, V51）。(c)「記録・税・交易・法・知識の継承」のうち、最初期の用途は会計・行政が中心だったことを書き分けるとよい（V46）。
2. **evt.early-states**（「紀元前4千年紀以降、一部の地域で都市・行政・初期国家が展開した」）：都市と国家を一括しているため、チャタルヒュユク（約7400 BC〜、大集落だが国家ではない）やジェンネ＝ジェノ（中央集権の痕跡が乏しい都市）の位置付けが曖昧になる（V28, V35）。また「紀元前4千年紀以降」はメソポタミアには当てはまるが、中国（二里頭は紀元前2千年紀）・メソアメリカ（テオティワカンは紀元後）・アフリカ西部（紀元前3世紀〜）では大きく遅れる。地域ごとに時期が異なることを明記すべき。
3. **evt.agriculture**（「約1万2000年前以降、複数の地域で…」）：おおむね正しい（Larson 2014 と整合）。ただし「農耕・牧畜」をまとめているが、イヌの家畜化は農耕より前であり（V3）、地域によって作物と家畜の順序が逆になる（V2）点を補足するとよい。誤りではない。

## 時事候補（2025〜2026年）
1. **Yüncü ら「Female lineages and changing kinship patterns in Neolithic Çatalhöyük」Science, 2025年6月**（DOI: 10.1126/science.adr2915）：131人の古代DNAで、同じ家の埋葬者は母系でより近縁。ただし母権制ではない（V29）。
2. **Barberena ら「Local agricultural transition, crisis and migration in the Southern Andes」Nature, 2026年3月**（DOI: 10.1038/s41586-026-10233-z）：在来民による農耕の採用、トウモロコシ依存の揺れと危機（V43）。
3. **Akbari ら「Ancient DNA reveals pervasive directional selection across West Eurasia」Nature, 2026年4月15日オンライン**（DOI: 10.1038/s41586-026-10358-1）：約1.6万人の古代ゲノム、農耕後に選択が加速（V44）。
- 次点：Lev-Mirom ら「Ancient grains illuminate the mosaic origin of domesticated wheat」Nature Plants 12(5), 2026（V13）、Kelley ら「Seals and signs」Antiquity 99(403), 2025年2月（V53）。

## 確認できなかった資料（WebFetch の取得失敗・許可待ちで開けなかったもの）
- Britannica「cuneiform」「oracle bone」項目（許可待ちでタイムアウト）
- Europe PMC の API（許可待ちでタイムアウト）
- CDLI wiki「proto-cuneiform」（ボット対策で拒否）、PMC の一部ページ（reCAPTCHA）
