# R1 origin：生命の起源（調査メモ）

- 担当：R1（Researcher）／サイクル 0002／P01-S02
- 調査日：2026-11-24
- 範囲：生命の定義、研究史、主要仮説、最古の生命の証拠、LUCA、地球外からの材料、2025〜2026年の動向、日本語の用語
- 注意：PMC（pmc.ncbi.nlm.nih.gov）の一部ページはブラウザ検査で本文を取得できなかった。取得できた要旨・出版社ページ・機関の発表で確認した。記憶だけで書いた箇所には【未確認】を付けた。

---

## A. 生命の定義

## 主張 R1
- 内容：NASAの「作業定義（working definition）」として広く引用される「生命とは、ダーウィン型進化が可能な自己維持的な（化学）系である」は、1992年ごろNASAの外部生物学（Exobiology）分野の作業部会（12人の助言パネル）の議論から生まれた。正式な採決や公式の承認はなく、NASAは助成や探査計画の判断にこの定義を使っていない。Gerald Joyce（スクリプス研究所）が1994年の書籍の序文で紹介したため彼の定義とされることが多いが、本人は「自己維持的な化学系」という語句を提案しただけだと述べている。
- ラベル：事実
- 確信度：high
- 出典：Forming a Definition for Life: Interview with Gerald Joyce｜NASA Astrobiology｜（記事日付は未確認）｜https://astrobiology.nasa.gov/news/forming-a-definition-for-life/
- 関連ノード：新規候補（con.definition-of-life・生命の定義・level 2・親 thm.life）
- 補足：「NASAが定めた公式の定義」と書くのは不正確。「NASAの作業部会に由来する作業定義」と書くべき。

## 主張 R2
- 内容：この作業定義には限界がある。(1) ウイルスは宿主細胞の中でしか進化しないため、この定義ではウイルス単独は「生きていない」ことになる。(2)「自己維持的」は、生物どうしの相互依存を考えると曖昧。(3)「可能な（capable）」がどの程度の進化能力を指すか曖昧。Joyce の研究室は自己維持的に進化する化学系を作ったが、新しい機能を進化させておらず、本人も「可能」の基準を満たしていないと述べる。
- ラベル：論争
- 確信度：high
- 出典：同上｜https://astrobiology.nasa.gov/news/forming-a-definition-for-life/
- 関連ノード：新規候補 con.definition-of-life
- 補足：生命の定義は単一の合意がない「未解決の概念上の問題」として扱うのが適切。定義の選び方が、代謝先行説と遺伝先行説の対立とも絡むことを記事は指摘している。

---

## B. 研究史：オパーリン／ホールデンとミラー＝ユーリー実験

## 主張 R3
- 内容：ロシアの生化学者アレクサンドル・オパーリン（Aleksandr Oparin）と英国のJ・B・S・ホールデン（J. B. S. Haldane）は、1920年代にそれぞれ独立に、酸素がほとんどない還元的な原始大気のもとで、紫外線などのエネルギーにより無機物から有機物ができ、原始の海で最初の生命（従属栄養）が生じたという考えを提案した（オパーリン＝ホールデン説）。オパーリンはコアセルベート（coacervate、自発的にできる液滴状の集合体）を細胞の前段階とみなした。
- ラベル：事実（学説史として）／その内容は歴史的な理論
- 確信度：high（学説史）
- 出典：Oparin-Haldane theory｜Encyclopaedia Britannica｜（日付未確認）｜https://www.britannica.com/print/article/1791898
- 関連ノード：新規候補（thy.oparin-haldane・オパーリン＝ホールデン説（原始スープ説）・level 3・親 q.origin-of-life）、または evt.miller-urey の補足として統合
- 補足：個別の年（オパーリン1924年、ホールデン1929年）はBritannicaの当該ページでは確認できず【未確認】。「熱い薄いスープ（hot dilute soup）」というホールデンの表現も今回は原典で確認できていない【未確認】。

## 主張 R4
- 内容：スタンリー・ミラー（Stanley Miller）は1953年5月15日の Science 誌論文「A Production of Amino Acids Under Possible Primitive Earth Conditions」で、原始大気を模した気体に放電を加え、アミノ酸を合成したと報告した。論文で同定されたのは5種類（アスパラギン酸、グリシン、α-アミノ酪酸、2種類のアラニン）。指導教員はハロルド・ユーリー（Harold Urey）。
- ラベル：事実
- 確信度：high
- 出典：Miller-Urey Revisited｜NASA Astrobiology｜2008-10-16｜https://astrobiology.nasa.gov/news/miller-urey-revisited/
- 関連ノード：新規候補 evt.miller-urey
- 補足：使用気体（メタン・アンモニア・水素・水蒸気）は UChicago の解説で「アンモニア、メタン、水蒸気」と確認。水素については今回原典で確認できていない【一部未確認】。

## 主張 R5
- 内容：2008年、Johnson らはミラーが保管していた当時の試料を最新の分析法で再分析し、未発表だった「火山型」装置（放電フラスコに水蒸気の噴流を加え、水蒸気に富む火山噴火を模したもの）の生成物から22種類のアミノ酸を検出した。古典的装置の試料からも14種類のアミノ酸と5種類のアミンが見つかり、1953年当時の報告より多様だった。著者らは、雷を伴い還元的な気体を出す火山噴火が初期地球で一般的だったなら、局所的に前生物的な化合物が蓄積しえたと述べる。
- ラベル：事実（測定結果）／解釈は仮説
- 確信度：high
- 出典：The Miller volcanic spark discharge experiment｜Science 322(5900):404｜2008｜https://pubmed.ncbi.nlm.nih.gov/18927386/ ；Miller-Urey Revisited｜NASA Astrobiology｜2008｜https://astrobiology.nasa.gov/news/miller-urey-revisited/
- 関連ノード：新規候補 evt.miller-urey
- 補足：再分析は「実験の装置内で何ができたか」を示すもので、「初期地球の大気が実際にそうだった」ことを示すものではない。

## 主張 R6
- 内容：現在では、初期地球の大気はミラーとユーリーが想定した強い還元的な組成（アンモニア・メタン等）とは異なっていたと考えられている。それでもこの実験は前生物化学（prebiotic chemistry）という分野の出発点になった。
- ラベル：理論（大気組成の現在の主流見解）
- 確信度：medium（一般向け解説での記述。大気組成の詳細は今回一次資料で確認していない）
- 出典：Origin of life on Earth, explained｜University of Chicago News（Explainer Series）｜2025年11月最終確認｜https://news.uchicago.edu/explainer/origin-life-earth-explained
- 関連ノード：evt.miller-urey（新規候補）
- 補足：大気が弱い還元性〜中性（CO2・N2主体）だったとする見解が主流と理解しているが、一次資料での確認は未了【未確認】。教材では「想定と異なると考えられている」までに留めるのが安全。

---

## C. 主要仮説

## 主張 R7
- 内容：「RNAワールド（RNA world）」という名称は、ウォルター・ギルバート（Walter Gilbert）の1986年の Nature 論文「Origin of life: The RNA world」（Nature 319:618）に由来する。
- ラベル：事実
- 確信度：high（書誌は確認。命名者であることは書誌と広く知られた事実に基づく）
- 出典：Origin of life: The RNA world｜Nature 319, 618｜1986｜https://www.doi.org/10.1038/319618A0
- 関連ノード：新規候補 thy.rna-world
- 補足：論文本文は取得できず、要旨の中身（RNAが遺伝情報と触媒を兼ねた段階）は書誌と参考文献からの推定。

## 主張 R8
- 内容：RNAワールド仮説：現在の生命はDNA（遺伝情報）とタンパク質（酵素）に依存しているが、その前に、RNAの配列が遺伝情報を担い、RNA自身の触媒能力（リボザイム ribozyme：触媒として働くRNA）が細胞の機能を担う、より単純な段階があったとする。Joyce（2002）はこの先行段階があったと考える「強い理由」があると総説で述べる。
- ラベル：仮説（有力）
- 確信度：medium
- 出典：The antiquity of RNA-based evolution｜Nature 418:214–221（G. F. Joyce）｜2002｜https://www.nature.com/articles/418214a
- 関連ノード：新規候補 thy.rna-world
- 補足：支持の根拠としてよく挙げられる「リボソームでペプチド結合をつくる中心部分がRNAである」「リボザイムの発見で1989年ノーベル化学賞（チェック Cech とアルトマン Altman）」は今回の取得で確認できなかった【未確認】。教材に使う場合は Verifier で照合すること。

## 主張 R9
- 内容：RNAワールド仮説の最大の弱点は、活性化したヌクレオチド（RNAの部品）が前生物的な条件でどう作られたかについて説得力ある経路がないこと（2005年時点の研究者の発言）。また豊かな「原始スープ」を前提にする点に地質学的な裏付けが乏しいという批判がある。Szostak は自己複製に近い触媒RNAや、脂質小胞内での複製を示した。
- ラベル：論争
- 確信度：medium（2005年の解説記事。最新の進展は別途確認が必要）
- 出典：Jump-Starting a Cellular World: Investigating the Origin of Life, from Soup to Networks｜PLOS Biology（R. Robinson）｜2005｜https://journals.plos.org/plosbiology/article/info:doi/10.1371/journal.pbio.0030396
- 関連ノード：thy.rna-world（新規候補）
- 補足：2005年以降、ヌクレオチド合成経路の研究は進んでいる（Powner ら2009等）が今回は未確認【未確認】。「完全に自己複製するリボザイムはまだ作られていない」という点も一般に言われるが今回原典で確認していない【未確認】。

## 主張 R10
- 内容：代謝先行説（metabolism-first）：ヴェヒターズホイザー（Günther Wächtershäuser）は1988年、生命が黄鉄鉱（FeS2）表面の鉱物を使った代謝として、おそらく深海熱水噴出孔で始まったと提案した（鉄硫黄ワールド）。モロウィッツ（Harold Morowitz）は小分子どうしの触媒で代謝ネットワークが自己組織化しうると論じた。批判として、遺伝の仕組みなしに代謝ネットワークが進化しうるか不明で、提唱者側（Martin）も「RNAワールドなしでは成り立たない」と認めている。記事は、遺伝先行と代謝先行のどちらも決定的な優位にないと総括する。
- ラベル：仮説／論争
- 確信度：medium
- 出典：Jump-Starting a Cellular World｜PLOS Biology｜2005｜https://journals.plos.org/plosbiology/article/info:doi/10.1371/journal.pbio.0030396
- 関連ノード：新規候補（thy.metabolism-first・代謝先行説・level 3・親 q.origin-of-life）または con.origin-settings に統合
- 補足：「遺伝先行か代謝先行か」は二者択一ではなく統合されうる、という見方が記事内で示されている。

## 主張 R11
- 内容：アルカリ性熱水噴出孔仮説（Russell、Martin、Lane ら）：海底の蛇紋岩化反応（serpentinization）がpH 9〜11のアルカリ性の流体と水素を生み、やや酸性（pH 約6）だったとされる冥王代の海水との間の「天然のpH勾配（プロトン勾配）」が、細胞が膜の内外の水素イオン濃度差でATPを作る仕組み（化学浸透）の原型になったと考える。H2でCO2を還元する原始代謝や、鉄硫黄の隔壁を想定する。現代の類似例として大西洋中央海嶺付近の「ロスト・シティ」熱水域が挙げられる。
- ラベル：仮説
- 確信度：medium（仮説の内容の要約として）
- 出典：Natural pH Gradients in Hydrothermal Alkali Vents Were Unlikely to Have Played a Role in the Origin of Life｜Journal of Molecular Evolution 83:1–11（J. B. Jackson）｜2016｜https://link.springer.com/article/10.1007/s00239-016-9756-6
- 関連ノード：新規候補 con.origin-settings
- 補足：この出典は批判論文で、仮説の要約もこの論文による。提唱者側の一次総説（Sojo, Herschy, Lane ら 2016, Astrobiology）は今回本文を取得できなかった。

## 主張 R12
- 内容：アルカリ性噴出孔仮説への批判：ロスト・シティには薄い隔壁をはさんだ鋭いpH勾配は見られない、想定される無機の隔壁は脂質膜の200倍以上厚く勾配が拡散してしまう、勾配を利用するタンパク質以外の「分子機械」が偶然できる根拠がない、実験的実証がない、など。化学浸透は遺伝の仕組みができた後に進化したという別の説明もある。
- ラベル：論争
- 確信度：medium
- 出典：同上（Jackson 2016）｜https://link.springer.com/article/10.1007/s00239-016-9756-6
- 関連ノード：con.origin-settings（新規候補）
- 補足：これは「最も強い反論」の一つとして教材に入れる価値がある。提唱者の反論は未確認。

## 主張 R13
- 内容：陸上温泉（地熱池）仮説：Damer と Deamer（2020, Astrobiology）は、生命が陸上の火山性温泉の、水位が上下する池で始まったと提案する。乾燥と湿潤の繰り返し（wet-dry cycles）で脂質に包まれた重合体（原始細胞 protocell）ができ、選択を受けるという実験に基づく。著者らは淡水の温泉池が化学的に「最適」だと主張し、海洋噴出孔のシナリオと比較している。
- ラベル：仮説
- 確信度：medium
- 出典：The Hot Spring Hypothesis for an Origin of Life｜Astrobiology 20(4):429–452（B. Damer, D. Deamer）｜2020｜https://pubmed.ncbi.nlm.nih.gov/31841362/
- 関連ノード：con.origin-settings（新規候補）
- 補足：海中では分子が薄まり重合しにくい（「水の問題」）ことが陸上説の主な論拠と一般に言われるが、本論文の要旨では確認できず【未確認】。冥王代に陸地がどれだけあったかが弱点になりうる点も未確認【未確認】。

## 主張 R14
- 内容：パンスペルミア（panspermia、生命が他の天体から運ばれてきたという考え）は、生命起源の問題を地球から別の場所に「外注」するだけで、生命がどう始まったかという本当の問いは解決しない。太陽系内外に前生物的な化学が豊富にあることは、むしろ地球での起源をもっともらしくする、という指摘がある。微生物が惑星・衛星間を移動すること自体はありうるとされる。
- ラベル：論争（評価）
- 確信度：medium（Scientific American のブログ（旧ブログネットワーク）。著者名・日付は未確認）
- 出典：The Panspermia Paradox｜Scientific American（Life, Unbounded ブログ）｜日付未確認｜https://www.scientificamerican.com/blog/life-unbounded/the-panspermia-paradox/
- 関連ノード：q.origin-of-life
- 補足：資料の優先度は3〜4位。論理的な指摘（問題の先送り）として使い、査読論文の出典を Verifier 段階で補うことが望ましい。「材料（有機分子）が宇宙から来た」ことと「生命そのものが宇宙から来た」ことは別の主張である点を教材で区別すべき。

## 主張 R15
- 内容：生命の起源について提案されている答え（原始スープ、宇宙からの供給、深海熱水噴出孔・温泉、粘土鉱物など）は、いずれも検証されていない。
- ラベル：未知
- 確信度：high
- 出典：Origin of life on Earth, explained｜University of Chicago News｜2025年11月最終確認｜https://news.uchicago.edu/explainer/origin-life-earth-explained
- 関連ノード：q.origin-of-life
- 補足：ただし同解説は「最古の化石は約37億年前」と書いており、これは論争中の主張（R19・R20参照）を事実のように扱っている。この点は引用しないこと。

---

## D. 最古の生命の証拠

## 主張 R16
- 内容：Allwood ら（2006, Nature 441:714–718）は、オーストラリア・ピルバラ地塊の約34.3億年前のストレリー・プール・チャート（Strelley Pool Chert）で、数kmにわたる浅い潮間帯の炭酸塩台地にストロマトライト（stromatolite：微生物の膜がつくる層状の構造）の「礁」を記載し、7つの形態型を識別した。形の多様さと環境との対応から、非生物的な説明を退けると主張した。
- ラベル：事実（記載）／生物起源という解釈は広く受け入れられている理論
- 確信度：high
- 出典：Stromatolite reef from the Early Archaean era of Australia｜Nature 441:714–718｜2006｜https://ideas.repec.org/a/nat/nature/v441y2006i7094d10.1038_nature04764.html
- 関連ノード：evt.earliest-life
- 補足：Javaux（2019, Nature）の総説は「少なくとも34億年前までに微生物の生物圏があった」とする。つまり約34億年前が「比較的広く受け入れられる最古の線」。ただし同じピルバラでもエイペックス・チャートの「微化石」は鉱物の産物と再解釈されており、34億年前前後の証拠すべてが確実なわけではない。

## 主張 R17
- 内容：Javaux（2019, Nature の総説「Challenges in evidencing the earliest traces of life」）は、初期の岩石記録が少なくとも34億年前までの微生物の生物圏を示すとし、それより古い主張は「議論がある（disputably earlier）」と位置づける。生物起源と非生物起源の信号を区別するには、マイクロ〜ナノスケールの分析と地質学的な文脈を組み合わせる必要があると述べる。
- ラベル：理論（学界の評価の要約）
- 確信度：high
- 出典：Challenges in evidencing the earliest traces of life｜Nature 572（E. J. Javaux）｜2019｜https://link.springer.com/article/10.1038/s41586-019-1436-4
- 関連ノード：evt.earliest-life
- 補足：題名・巻号は検索結果と出版社ページから。論文タイトルは本文取得範囲で直接は確認できず、DOIで照合すること【一部未確認】。

## 主張 R18
- 内容：Nutman ら（2016, Nature, 2016年8月31日公開）は、グリーンランド南西部イスア（Isua）表成岩帯の約37億年前の岩石に、ストロマトライトとされる構造を報告し、生命が地球形成後「非常に早く」現れたと主張した。
- ラベル：論争
- 確信度：high（報告があったこと）／low（生物起源であること）
- 出典：Rapid emergence of life shown by discovery of 3,700-million-year-old microbial structures｜Nature（Nature Index ページ）｜2016｜https://www.nature.com/nature-index/article/10.1038/nature19355
- 関連ノード：evt.earliest-life
- 補足：下記 R19 の反論を必ず併記する。

## 主張 R19
- 内容：Allwood ら（2018, Nature 563:241–244）は、イスアの同じ構造を3次元の形と向き、元素の化学組成から再検討し、堆積後の変形でできた非生物的な構造である可能性が高いと結論した。火星で生命の痕跡を探す際の警告になるとも述べる。
- ラベル：論争
- 確信度：high（反論が出たこと）
- 出典：Reassessing evidence of life in 3,700-million-year-old rocks of Greenland｜Nature 563:241–244｜2018｜https://ideas.repec.org/a/nat/nature/v563y2018i7730d10.1038_s41586-018-0610-4.html
- 関連ノード：evt.earliest-life
- 補足：Nutman 側の再反論があるかは今回未確認【未確認】。教材では「37億年前の主張は反論があり未決着」とするのが妥当。

## 主張 R20
- 内容：Dodd ら（2017, Nature 543:60–64）は、カナダ・ケベック州のヌブアギトゥク（Nuvvuagittuq）帯の鉄に富む堆積岩中に、赤鉄鉱のマイクロメートル規模の管や糸状体を報告し、少なくとも37.7億年前、最大で42.8億年前の海底熱水噴出孔に関連した微生物の化石と解釈した。
- ラベル：論争
- 確信度：high（報告があったこと）／low（生物起源であること）
- 出典：Evidence for early life in Earth's oldest hydrothermal vent precipitates｜Nature 543:60–64｜2017｜https://pubs.usgs.gov/publication/70193303
- 関連ノード：evt.earliest-life
- 補足：岩石の年代自体（37.7億年か42.8億年か）にも議論がある点は今回未確認【未確認】。

## 主張 R21
- 内容：McMahon（2019, Proc. R. Soc. B 286）は、実験でつくった「化学の庭（chemical gardens：金属塩と溶液の反応で自発的にできる管状の沈殿）」が、ヌブアギトゥクの管や糸状体と大きさ・形・組成でよく似ており、原著者が非生物では説明できないとした特徴も再現できたと報告した。形態だけでは生物の決定的証拠にならず、非生物起源を真剣な帰無仮説として扱うべきだと結論した（化学の庭だと断定はしていない）。
- ラベル：論争
- 確信度：high
- 出典：Earth's earliest and deepest purported fossils may be iron-mineralized chemical gardens｜Proceedings of the Royal Society B 286(1916)｜2019｜https://pmc.ncbi.nlm.nih.gov/articles/PMC6939263
- 関連ノード：evt.earliest-life
- 補足：Papineau ら（2022, Science Advances）が生物起源を補強する追加報告をしている（検索結果で存在を確認、内容は未確認【未確認】）。

## 主張 R22
- 内容：Bell ら（2015, PNAS）は、オーストラリア・ジャックヒルズの41億年前のジルコン（zircon：風化に強い鉱物の粒）に完全に閉じ込められた石墨（グラファイト）を見つけ、その炭素が軽い炭素（12C）に富むことから、41億年前までに生命が誕生していた証拠「かもしれない」と述べた。題名も「潜在的に生物起源の（potentially biogenic）」と慎重。
- ラベル：仮説
- 確信度：medium（報告内容）／low（生命の証拠であること）
- 出典：Potentially biogenic carbon preserved in a 4.1 billion-year-old zircon｜PNAS｜2015｜https://ui.adsabs.harvard.edu/abs/2015PNAS..11214518B/abstract
- 関連ノード：evt.earliest-life
- 補足：軽い炭素は非生物的な過程でもできうる。UChicago の解説も「証明には不十分」とする。δ13C の具体値（約 −24‰ とされる）は今回確認できず【未確認】。産地名「ジャックヒルズ」も今回の取得範囲では未確認【未確認】。

---

## E. LUCA（全生物の最後の共通祖先）

## 主張 R23
- 内容：Moody ら（2024, Nature Ecology & Evolution 8:1654–1666、2024年7月12日公開）は、LUCA（Last Universal Common Ancestor：現在のすべての生物の最後の共通祖先、日本語では「最終普遍共通祖先」）の年代を約42億年前（95%信用区間 40.9億〜43.3億年前、ILN緩和時計モデル）と推定した。方法は、LUCA以前に遺伝子重複でできた5組の遺伝子（ATP合成酵素のサブユニット等）を使う分子時計と、13の化石・地質学的な較正点（最大は月を作った巨大衝突 約45.1億年前）。
- ラベル：仮説（推定値）
- 確信度：medium
- 出典：The nature of the last universal common ancestor and its impact on the early Earth system｜Nature Ecology & Evolution 8(9):1654–1666｜2024｜https://pmc.ncbi.nlm.nih.gov/articles/PMC11383801/
- 関連ノード：新規候補 con.luca
- 補足：「LUCA＝最初の生命」ではない。LUCAの前にも生命の歴史があり、LUCAと同時代の他の系統は子孫を残さなかった可能性がある（著者らはLUCAが確立した生態系の一員だったと推定）。

## 主張 R24
- 内容：同論文はLUCAの性質を、ゲノム約2.75 Mb（少なくとも2.5 Mb）、タンパク質約2,600個をもつ原核生物並みの複雑さで、ウッド・ユングダール経路で炭素を固定する嫌気性の酢酸生成菌であり、初期型のCRISPR-Cas（ウイルスに対する免疫の仕組み）を持っていたと推定した。著者ら自身、遺伝子の再構成は「おそらく不完全」で、系統樹の形（DPANN・CPRの位置）や分子時計の仮定に結果が依存し、生態系に関する推論はモデルに基づく推測だと述べている。
- ラベル：仮説
- 確信度：medium（推定の内容）／low（細部）
- 出典：同上｜https://pmc.ncbi.nlm.nih.gov/articles/PMC11383801/
- 関連ノード：con.luca（新規候補）
- 補足：免疫系を持つことは、LUCAがウイルスと共存していたことを示唆するとされる。

## 主張 R25
- 内容：Goldman と Becerra（2024, J. Mol. Evol. 92:659–661）の論評は、Moody らの再構成をより厳密な前進と評価しつつ、約42億年前という年代は「LUCAが生まれるまでの時間をほとんど残さない」（初期進化の期間が1〜2億年程度）と指摘し、分子時計は突然変異率の変動や選択の影響を受けると注意している。中核の399タンパク質ファミリーと推定ゲノムの大きさの差も、新たな問いとして挙げる。
- ラベル：論争
- 確信度：medium
- 出典：A New View of the Last Universal Common Ancestor｜Journal of Molecular Evolution 92:659–661｜2024｜https://link.springer.com/article/10.1007/s00239-024-10193-w
- 関連ノード：con.luca（新規候補）
- 補足：「42億年前」は地質記録で受け入れられている最古の証拠（約34億年前）より約8億年古い。分子推定と岩石記録の食い違い自体が教材の良い論点。

---

## F. 地球外からの材料

## 主張 R26
- 内容：Martins ら（2008, Earth and Planetary Science Letters）は、マーチソン隕石（炭素質コンドライト）中の核酸塩基（ウラシルとキサンチン）の炭素同位体比（δ13C がウラシル +44.5‰、キサンチン +37.7‰）が地球の生物由来の値と異なることから、これらが地球での汚染ではなく隕石固有（地球外起源）であると示した。
- ラベル：事実
- 確信度：high
- 出典：Extraterrestrial nucleobases in the Murchison meteorite｜arXiv:0806.2286（EPSL, doi:10.1016/j.epsl.2008.03.026）｜2008｜https://arxiv.org/abs/0806.2286
- 関連ノード：新規候補（evd.extraterrestrial-organics・地球外の有機物（隕石・小惑星試料）・level 3・親 q.origin-of-life）
- 補足：マーチソン隕石が1969年にオーストラリアに落下したことは今回確認できず【未確認】。アミノ酸の検出も UChicago 解説での言及のみ。

## 主張 R27
- 内容：Oba ら（2023, Nature Communications、2023年3月21日）は、JAXAの探査機はやぶさ2が持ち帰った小惑星リュウグウの試料から、RNAの塩基であるウラシル（6〜32 ppb）とビタミンB3（ニコチン酸、49〜99 ppb）を検出した。カプセルで密閉して持ち帰った試料のため、地球での汚染の可能性を排除できる点が隕石研究との違いである。
- ラベル：事実
- 確信度：high
- 出典：Uracil found in Ryugu samples（プレスリリース）｜北海道大学｜2023-03-22｜https://www.global.hokudai.ac.jp/?p=68201 （論文：Uracil in the carbonaceous asteroid (162173) Ryugu, Nature Communications, doi:10.1038/s41467-023-36904-3）
- 関連ノード：evd.extraterrestrial-organics（新規候補）
- 補足：2つの採取地点で濃度が異なり、原因（宇宙空間への曝露）は仮説段階。

## 主張 R28
- 内容：NASAのOSIRIS-RExが持ち帰った小惑星ベンヌの試料について、2025年1月29日に2本の論文が出た。Nature Astronomy（Glavin・Dworkin ら）は、地球の生物がタンパク質に使う20種のアミノ酸のうち14種、DNA・RNAに使う5種の核酸塩基すべて、非常に多量のアンモニアを報告。Nature（McCoy・Russell ら、66人）は、塩水が蒸発してできる11種の鉱物（蒸発岩：方解石、岩塩、カリ岩塩、地球外試料で初のトロナなど）を報告し、母天体の内部に長く液体の塩水があったことを示した。アミノ酸は左手型と右手型が等量で、地球の生物がなぜ左手型だけを使うかは説明できない。
- ラベル：事実
- 確信度：high
- 出典：NASA's Asteroid Bennu Sample Reveals Mix of Life's Ingredients｜NASA｜2025-01-29｜https://www.nasa.gov/news-release/nasas-asteroid-bennu-sample-reveals-mix-of-lifes-ingredients/ ；Asteroid Bennu Comes From a Long-lost Salty World With Ingredients For Life｜University of Arizona LPL｜2025-01-29｜https://lpl.arizona.edu/news/spotlight/asteroid-bennu-comes-long-lost-salty-world-ingredients-life
- 関連ノード：evd.extraterrestrial-organics（新規候補）
- 補足：何を示さないか：生命そのものの証拠ではない。部品から生物の長い鎖（重合体）がどう作られたかは未解明。示すのは「生命の材料と、それができる条件が初期太陽系に広く存在した」こと。

## 主張 R29
- 内容：2025年12月2日、Furukawa ら（東北大学）は Nature Geoscience で、ベンヌ試料からリボース（RNAの糖）とグルコース（地球外試料で初）を報告した。DNAの糖であるデオキシリボースは見つからなかった。これでRNAを作る部品（塩基・リボース・リン酸）がすべてベンヌ試料にそろったとされ、研究者はRNAワールド仮説と整合的とみる。
- ラベル：事実（検出）／RNAワールドとの関連は仮説
- 確信度：high（検出）／low（RNAワールドを支持するという解釈）
- 出典：Sugars, 'Gum,' Stardust Found in NASA's Asteroid Bennu Samples｜NASA｜2025-12-02｜https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/
- 関連ノード：evd.extraterrestrial-organics（新規候補）、thy.rna-world（新規候補）
- 補足：リボースはすでに2つの隕石で見つかっていた。生命の証拠ではない。デオキシリボース不在の推論は小惑星1つの試料に基づく。

---

## G. 2025〜2026年の動向

## 主張 R30
- 内容：2025年9月10日、NASAは火星探査車パーサヴィアランスがジェゼロ・クレーターのネレトヴァ谷「ブライト・エンジェル」層の岩石「チェヤヴァ・フォールズ（Cheyava Falls）」から採取した試料「サファイア・キャニオン（Sapphire Canyon）」に「潜在的なバイオシグネチャー（potential biosignature：生物由来かもしれないが、結論にはさらなるデータが必要な物質や構造）」があると発表した（Hurowitz ら, Nature, 2025）。「ヒョウ柄」の斑点にビビアナイト（リン酸鉄）とグレイガイト（硫化鉄）が反応前線状に並ぶ。両鉱物は高温・酸性などで非生物的にもできるが、この岩石に高温・酸性の証拠はない。NASAの科学者は非生物的説明は「可能性が低いが排除できない」とする。
- ラベル：論争（解釈未確定）
- 確信度：high（発表内容）／low（生命の痕跡であること）
- 出典：NASA Says Mars Rover Discovered Potential Biosignature Last Year｜NASA JPL｜2025-09-10｜https://www.jpl.nasa.gov/news/nasa-says-mars-rover-discovered-potential-biosignature-last-year/
- 関連ノード：新規候補（evt.cheyava-falls・火星の潜在的バイオシグネチャー（2025）・level 4・親 q.origin-of-life）または時事コラムとしてのみ扱う
- 補足：Hurowitz は、生命検出の確信度の尺度（CoLD scale）で段階3（生命が住めたかもしれない地質環境からの信号）と位置づけ、段階4には達していないと述べる。有機炭素の由来（隕石・熱水反応・生物）は未解決（The Planetary Society の解説, https://www.planetary.org/articles/a-biosignature-on-mars-unpacking-perseverances-cheyava-falls-find）。Allwood 2018（R19）と同じく「生命らしい形・化学は非生物でもできうる」という教訓とつながる。

## 主張 R31
- 内容：サンプルを地球に持ち帰って分析する計画「マーズ・サンプル・リターン（MSR）」は、2026年1月の米国の歳出法案で事実上中止された（議会の説明文書：既存のMSR計画を「支持しない」）。中国の天問3号が2028年打ち上げ・2031年試料回収を予定している。JPLの研究者は代替策として、地上の泥岩で斑点を微生物あり・なしの条件で再現する実験を計画している。
- ラベル：事実（政策の状況）
- 確信度：medium（報道のみ。NASA・議会の一次文書は未確認）
- 出典：NASA's Mars Sample Return is dead, leaving China to retrieve signs of life from the Red Planet｜Live Science｜2026-01-16｜https://www.livescience.com/space/mars/nasas-mars-sample-return-is-dead-leaving-china-to-retrieve-signs-of-life-from-the-red-planet ；Scientists Devise New Plan to Study the Most Exciting Rock on Mars｜Scientific American｜日付未確認（2025年と推定）｜https://www.scientificamerican.com/article/scientists-devise-new-plan-to-study-the-most-exciting-rock-on-mars/
- 関連ノード：evt.cheyava-falls（新規候補）
- 補足：記事時点では大統領の署名待ちとされていた。最終的な成立は実行時に再確認が必要【未確認】。2026年にサファイア・キャニオンの評価を大きく変える新論文は今回見つからなかった。

## 主張 R32
- 内容：Abramov ら（2026, Nature Communications 17:9790、2026年9月22日公開）は、45億〜35億年前の天体衝突による地殻の加熱を3次元モデルで計算し、RNA・ペプチド・脂質などの熱安定性と比べた。約44億年前までは衝突による滅菌的な事象が地球規模で繰り返されたが、約43.3億年前にはRNAワールドの化学が持続しうる条件（エネルギー豊富な熱水環境が広がった「スイートスポット」）が整った可能性があるとした。これはLUCAの推定年代より約1億3000万年早い。
- ラベル：仮説（モデル）
- 確信度：medium（発表内容）／low（実際にその時期に化学が起きたこと）
- 出典：A Hadean timeline for the emergence of the RNA World（研究ハイライト日本語版）｜Nature Japan（natureasia.com）｜2026-09｜https://www.natureasia.com/ja-jp/research/highlight/15625
- 関連ノード：thy.rna-world（新規候補）、con.luca（新規候補）
- 補足：著者らも明記するとおり、地球の熱的条件を評価しただけで、生命の出現時期を直接示すものではない。

## 主張 R33
- 内容：Wadsworth ら（2026, Nature Communications 17）は、RNAがDNAにない2'-ヒドロキシ基（2'-OH）のために、対応する一本鎖DNAより約10℃低い温度で液滴（相分離）をつくり、ゲル状の網目にも移りやすいことを示した。これが初期のRNAを保護する区画になりえたと示唆する。
- ラベル：仮説（実験結果の起源への応用）
- 確信度：low（報道記事経由。論文本文は未確認）
- 出典：One tiny chemical difference between RNA and DNA may help explain how life began｜ScienceDaily（University at Buffalo 発表）｜2026-10-01｜https://www.sciencedaily.com/releases/2026/09/260929053546.htm
- 関連ノード：thy.rna-world（新規候補）
- 補足：オパーリンのコアセルベート（R3）の現代版の研究潮流（膜のない区画）として位置づけられる。Nature の分野ページでも2026年にコアセルベート関連の論文が続いている（https://www.nature.com/subjects/origin-of-life）。

---

## H. 日本語の用語

## 主張 R34
- 内容：「化学進化（chemical evolution）」は、生命が出現する前に、原始大気中の簡単な分子から放電などでアミノ酸や糖などの有機化合物ができ、やがて原始細胞が生まれるまでの物質の変化の過程を指す（デジタル大辞泉）。宇宙での化学物質の変化を指す用法もある。生物進化（自然選択による進化）とは別の過程であり、教材では「化学進化」と「生物進化」を区別して書くべき。
- ラベル：事実（用語の定義）
- 確信度：high
- 出典：化学進化｜Weblio辞書（デジタル大辞泉・生物学用語辞典を収録）｜確認 2026-11-24｜https://www.weblio.jp/content/化学進化
- 関連ノード：q.origin-of-life
- 補足：Weblio は辞書の集約サイト。根拠としてはデジタル大辞泉（小学館）の記述。

## 主張 R35
- 内容：日本語の表記：「原始スープ（primordial soup）」「RNAワールド仮説」「ユーリー－ミラーの実験」（「ミラー・ユーリー」「ユーリー・ミラー」と表記が揺れる）、LUCA は「最終普遍共通祖先」、potential biosignature は「潜在的なバイオシグネチャー」。NASAのアストロバイオロジー漫画の日本語版（東京工業大学ELSI 製作）では「原始スープ」「RNAワールド仮説」「ユーリー-ミラーの実験」が使われている。
- ラベル：事実（用語）
- 確信度：medium
- 出典：アストロバイオロジー 第7巻 生命誕生以前の化学環境と生命の起源（日本語版）｜NASA / ELSI｜発行年未確認｜https://assets.science.nasa.gov/content/dam/science/psd/astrobiology/graphic-histories/Astrobiology%20Graphic%20Histories%20Issue%207%20Edition%201%20(ja)%20lowres.pdf ；Nature Japan 研究ハイライト（「最終普遍共通祖先」）｜2026｜https://www.natureasia.com/ja-jp/research/highlight/15625
- 関連ノード：evt.miller-urey（新規候補）、con.luca（新規候補）
- 補足：教材では「ミラー＝ユーリー実験」に統一し、初出で別表記を併記するのがよい。

---

## 担当範囲で見つけた、地図にない重要な概念（新規ノード候補）

| 仮ID | 名称 | level | 親 | 根拠 |
|---|---|---|---|---|
| con.definition-of-life | 生命の定義（NASAの作業定義とその限界） | 2 | thm.life | R1, R2 |
| thy.oparin-haldane | オパーリン＝ホールデン説（原始スープ説・化学進化説） | 3 | q.origin-of-life | R3, R34 |
| evt.miller-urey | ミラー＝ユーリー実験（1953）と2008年の再分析 | 3 | q.origin-of-life | R4–R6 |
| thy.rna-world | RNAワールド仮説 | 3 | q.origin-of-life | R7–R9, R29, R32, R33 |
| thy.metabolism-first | 代謝先行説（鉄硫黄ワールド等） | 3 | q.origin-of-life | R10（con.origin-settings への統合も可） |
| con.origin-settings | 生命起源の場の仮説（アルカリ性熱水噴出孔／陸上温泉） | 3 | q.origin-of-life | R11–R13 |
| con.luca | LUCA（最終普遍共通祖先） | 3 | thm.life | R23–R25 |
| evd.extraterrestrial-organics | 地球外の有機物（マーチソン隕石・リュウグウ・ベンヌ試料） | 3 | q.origin-of-life | R26–R29 |
| con.biosignature | バイオシグネチャー（生命の痕跡）と生物起源の判定の難しさ | 3 | q.origin-of-life（または evt.earliest-life と関連） | R17, R19, R21, R30。最古の生命の論争と火星の論争に共通する「形や化学だけでは生物と決められない」という考え方の核 |
| evt.cheyava-falls | 火星チェヤヴァ・フォールズの潜在的バイオシグネチャー（2025） | 4 | con.biosignature | R30, R31（時事コラムに留めるならノード化不要） |

※ パンスペルミア（R14）は独立ノードにせず、q.origin-of-life の「反論・別説」欄で扱うことを推奨（問題の先送りであるため）。

## 既存ノードの誤りの疑い

1. **evt.earliest-life**：「約34億年前の地層に…ストロマトライト」は Allwood 2006（約34.3億年前、ピルバラ）と Javaux 2019（少なくとも34億年前）に合致し、概ね妥当。ただし (a) 出典に Allwood 2006 と Javaux 2019 を登録すべき、(b)「より古い主張」の具体例として、イスア37億年前（Nutman 2016 → Allwood 2018 の反論）、ヌブアギトゥク37.7〜42.8億年前（Dodd 2017 → McMahon 2019 の反論）、41億年前ジルコン（Bell 2015、本人も「可能性」）を明記し、いずれも「論争」ラベルにすべき。(c) 分子時計によるLUCA約42億年前（Moody 2024）は「岩石の証拠」ではなく「推定」なので、このノードとは別扱い（con.luca）にすべき。
2. **thm.life**（計画書によれば開始時期「約40億年前？」の表記）：LUCA推定（約42億年前、95%区間 40.9〜43.3億年前）、居住可能性（約43億年前から可能だった可能性）、確かな化石記録（約34億年前）の三つが食い違う。「約40億年前？」という単一の数字は根拠が曖昧。「確かな痕跡は約34億年前。それ以前については複数の主張と推定があり未確定」と書き換えるのが妥当。
3. **q.origin-of-life**：記述（時期と機構は未解明、進化とは別の問題）は R15 と一致し妥当。出典未登録のため、UChicago 解説（R15）と Javaux 2019（R17）、NASAの定義記事（R1）を登録候補とする。「化学進化（chemical evolution）」という用語は生物進化と紛らわしいため、説明文で区別を明示することを推奨。
4. **注意（外部資料の誤り）**：University of Chicago の解説（2025年11月確認）は「最古の化石は約37億年前」と記すが、これは論争中（R18・R19）。この記述を地図や教材に取り込まないこと。

## 時事候補の推薦

**第一候補：小惑星ベンヌ試料から RNA の糖（リボース）とグルコースを検出（Furukawa ら, Nature Geoscience, 2025年12月2日, NASA 公式発表あり）** — R29
- 理由：一次資料（査読論文＋NASA公式発表）があり、日本の研究者（東北大学）が主導。2025年1月のアミノ酸・核酸塩基・塩類の報告（R28）、2023年のリュウグウのウラシル（R27）とつなげると「材料はそろった。しかし材料があることと生命ができることは別」という今回の中心テーマ（起源の未知）を説明しやすい。
- 次点：火星サファイア・キャニオンの潜在的バイオシグネチャー（Hurowitz ら, Nature, 2025年9月, NASA発表）— R30・R31。話題性は最大だが、2026年1月のMSR事実上中止で検証の見通しが立たず、「判定できない」こと自体が教材になる。最古の生命の論争（Allwood 2018）と同じ構図を示せる。
- 2026年の新しい成果として Abramov ら（Nature Communications, 2026年9月, R32）もあるが、熱モデルの研究で、時事コラムよりは本文の補足向き。

（以上、主張 35 件）
