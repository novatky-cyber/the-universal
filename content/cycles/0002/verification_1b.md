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
