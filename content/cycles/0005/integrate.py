# サイクル0005 地図の統合（Cartographer）。確認済み・修正済みの主張のみを反映する。
import json, re
R='/home/claude/the-universal/'
N=json.load(open(R+'data/graph/nodes.json')); E=json.load(open(R+'data/graph/edges.json')); S=json.load(open(R+'data/sources.json'))
U=json.load(open(R+'data/understanding.json'))
MV='1.5'; D='2026-11-28'; BY='verifier（L0005の主張照合）'
ids={n['id']:n for n in N}; sids={s['id'] for s in S}
# ---- sources
new=json.load(open('/tmp/newsrc.json')); st=json.load(open('/tmp/srcstatus.json'))
st['src.antras-voth2003']='unverified'
def kind(d):
    p=(d['publisher']+' '+d['title']).lower()
    if any(k in p for k in ['stanford encyclopedia','britannica','encyclopedia','worldhistory']): return 'reference'
    if any(k in p for k in ['review','書評','nyrb','lrb','london review','new york review']): return 'review'
    if any(k in p for k in ['news','報道','allafrica','eurekalert','full fact','scientific american']): return 'news'
    if any(k in p for k in ['archives','national','外務省','国立','文化庁','文部','museum','library','nobel','riksbank','auswärtiges','auswaertiges','un news','unesco','iugs','imf','観光庁','北海道','élysée','elysee','jacar','アジア歴史','ieee','royal society','bnf','founders']): return 'agency'
    if any(k in p for k in ['press','university press','springer','verso','beacon','knopf','profile']): return 'textbook'
    return 'primary'
for sid,d in new.items():
    if sid in sids: continue
    y=d['year']; m=re.match(r'^(\d{4})$',y or '')
    rec=dict(id=sid,title=d['title'],author=d['author'],publisher=d['publisher'],year=int(y) if m else (y or None),
             url=d['url'] if re.match(r'^https?://\S+$',d['url'] or '') else '',kind=kind(d),existence=st.get(sid,'unverified'),
             checked_at=D,note='サイクル0005 の Researcher が提示し、Verifier が実在と内容を照合（L0005の主張照合）。' if st.get(sid)=='verified' else 'サイクル0005 で書誌のみ確認。本文・内容は独立検証で照合できていないため、教材の根拠に使わない。')
    S.append(rec); sids.add(sid)
def need(ss):
    for s in ss: assert s in sids, s
    return ss
# ---- helpers
def ver(): return {"status":"verified","date":D,"by":BY}
def upd(i,change,reason,**kw):
    n=ids[i]; n.update(kw); n['verification']=ver(); need(n['sources'])
    n.setdefault('history',[]).append({"map_version":MV,"change":change,"reason":reason})
def add(i,typ,ja,en,summary,domains,level,parent,time,epi,conf,sources,target=2,persp=None):
    assert i not in ids, i
    n=dict(id=i,type=typ,title={"ja":ja,"en":en},summary=summary,domains=domains,level=level,parent=parent,time=time,
           epistemic=epi,confidence=conf,sources=need(sources),verification=ver(),target_level=target,curriculum=["P01-S05"],
           history=[{"map_version":MV,"change":"作成","reason":"サイクル0005（L0005 近代化と産業革命）の確認済みの主張から"}])
    if persp: n['perspectives']=persp
    N.append(n); ids[i]=n
def T(s,e,label,unc=None):
    t={"start_ya":2026-s,"end_ya":(2026-e) if e is not None else None,"label":label}
    if unc: t['uncertainty']=unc
    return t
# ---- existing nodes (訂正・深化)
upd('evt.industrial-revolution','訂正（中）：始まりと速度の記述を追加、「革命」は一部門の急変で経済全体の加速は緩やかだったことを明記',
    '語の由来（OpenLearn）と成長の推計（Crafts 2004、Kuznets 1971）',
    summary='18世紀後半の英国で、綿工業・製鉄・蒸気動力などの一部の部門が急に変わり、のちに世界へ広がった工業化の過程。語に一人の名付け親はなく、1884年のトインビーの講義が学術的な枠組みを作った。経済全体の加速は緩やかで、蒸気が生産性に最も効いたのは1850〜70年。「近代経済成長」（一人あたり生産が伸び続ける状態）とは区別して扱う。',
    sources=['src.openlearn-origins-ir','src.kuznets1971','src.crafts2004-steam','src.owid-tech'],epistemic='fact',confidence='high')
upd('con.industrial-revolution-causes','深化：主要な原因説を出典つきで整理（ラベルは論争のまま）','L0005 の主張照合',
    summary='原因に決着はない。高賃金・安価な石炭による誘発された発明（アレン）、有機経済から鉱物エネルギー経済への転換（リグリー）、有用な知識と産業的啓蒙（モキイア）、議会・財政などの制度（ノース＝ワインガスト、アセモグルら）、石炭の立地と植民地の「幽霊耕地」（ポメランツ）、家計の勤勉革命（ド・フリース）などが競合する。説ごとに「なぜ英国で」「なぜ止まらなかったか」のどちらを説明するかが違う。',
    sources=['src.allen2011','src.cam-wrigley2010','src.nobel-econ2025-popular','src.cox2012','src.ajr2005','src.cage-pomeranz','src.devries1994','src.humphries-schneider2019'],
    perspectives=[{"label":"マルクス主義","view":"植民地・奴隷貿易・略奪による「原始的蓄積」を資本主義の前史とみる（マルクス『資本論』第1巻第31章）。","sources":["src.marx1867-ch31"]},
                  {"label":"観念・言説","view":"市場・商業・ブルジョワについての語り方と評価の変化（尊厳と自由）が近代の豊かさの原因だとし、物質的・制度的な説明を退ける（マクロスキー）。","sources":["src.mccloskey2010"]},
                  {"label":"東アジアの経路","view":"東アジアの労働集約型工業化を中心に置き、西洋の資本集約型モデルを一つの経路として読み直す（オースティン＆杉原編）。","sources":["src.austin-sugihara2013"]}])
upd('evt.scientific-revolution','訂正（中）：「科学革命」という概念への批判と、ヨーロッパ外の天文学とのつながりを追加',
    '概念は20世紀に作られ、1990年代に多くの科学史家が単一の出来事としての像を捨てた（Secord 2023、Shapin 1996）',
    summary='16〜17世紀ヨーロッパの天文学・力学の変化（コペルニクス1543、ケプラー1609・1619、ガリレオ1610〜1638、ニュートン1687）と、実験・学会・学術誌などの新しい作法を指す。ただし「一つのまとまった革命」という像は20世紀に作られた概念で、多くの科学史家が批判している。コペルニクスの幾何学の道具は13〜14世紀のマラーガ学派のものと一致するが、伝わった経路は論争中。',
    sources=['src.sep-copernicus','src.sep-kepler','src.sep-galileo','src.sep-newton','src.secord2023','src.shapin1996','src.warwick-hi296-intro','src.blasjo2018'],
    epistemic='debate',confidence='high')
upd('evt.enlightenment','深化：啓蒙の定義・担い手・多様性と、人種・奴隷制との関係の論争を追加','L0005 の主張照合',
    summary='17世紀後半〜18世紀、理性による批判と知識の公開を掲げた思想の運動。カントは1784年に「自ら招いた未成年状態から抜け出ること」と定義した。主な源は科学革命で、『百科全書』（1751〜72）、スコットランド啓蒙（スミス『国富論』1776）、スピノザに根ざす「急進的啓蒙」（イスラエルの説。論争的）など多様。平等の理念と人種の階層化がともに啓蒙の中で論じられ、その関係は両義的とみる読みが最も広い。',
    sources=['src.kant1784','src.sep-enlightenment','src.ree2002-lrb-israel','src.vartija-race-enlightenment'],epistemic='theory',confidence='high',
    perspectives=[{"label":"グローバル・ヒストリー","view":"ヨーロッパから世界へ広がったのではなく、世界規模の相互作用の中で共同生産されたとみる（コンラート）。","sources":["src.conrad2013-zeitenblicke"]}])
upd('evt.atlantic-revolutions','訂正（中）：題名と範囲を拡大（ハイチ革命・イスパノアメリカの独立を追加）',
    'アメリカ独立とフランス革命だけを挙げると、史上最も成功した奴隷反乱と南米の独立が抜ける（品質基準3。Trouillot 1995）',
    title={"ja":"大西洋革命（アメリカ・フランス・ハイチ・イスパノアメリカ）","en":"Atlantic revolutions"},
    summary='1770年代〜1820年代、大西洋の両岸で主権・権利・独立をめぐる革命が連鎖した。アメリカ独立宣言（1776）、フランスの人権宣言（1789。第3条で主権は国民に存するとした）、ハイチ革命（1791〜1804、元奴隷が建てた最初の国）、イスパノアメリカとブラジルの独立（1808〜1826）。権利の担い手の範囲（奴隷・女性・先住民）は革命ごとに争われた。',
    sources=['src.founders-declaration-1776','src.elysee-ddhc1789','src.britannica-haitian-revolution','src.trouillot1995'],
    time=T(1776,1826,'1776〜1826年'))
upd('evt.imperialism','訂正（中）：ラベルを fact → debate に。原因の学説と、支配された側の応答を追加',
    '帝国主義の原因は学説が分かれる（ホブソン、レーニン、シュンペーター、ギャラハー＆ロビンソン）。出典なしで fact／high だった',
    title={"ja":"19世紀の帝国主義と世界の応答","en":"New imperialism and responses"},
    summary='19世紀、工業化した国々は蒸気船・電信（1866年に大西洋横断ケーブル）・スエズ運河（1869）・キニーネなどを使って支配を広げ、1914年までにアフリカの約90%がヨーロッパの帝国に組み込まれた。原因は、余った資本の行き先（ホブソン）、独占資本主義（レーニン）、旧来の支配層の戦争志向（シュンペーター）、非公式帝国（ギャラハー＆ロビンソン）などで論争がある。技術だけでは決まらず、アドワの戦い（1896）やシャム・オスマン・エジプトの防衛的な近代化のように、支配された側の応答も結果を左右した。',
    sources=['src.britannica-economic-imperialism','src.attard2023-informal-empire','src.gillin2018-niger','src.bnf-suez','src.iet-atlantic-cable','src.britannica-scramble-africa','src.britannica-adwa'],
    epistemic='debate',confidence='high')
upd('evt.electrification','深化：中央発電所の始まり（1882年パール街）と普及の遅れを出典つきで',
    'ETHW（IEEE マイルストーン）、David 1990',
    summary='19世紀末から電力が普及した。エジソンのパール街発電所（ニューヨーク、1882年9月4日、直流）が中央発電所方式の原型で、交流と直流の「方式の争い」は1880年代に起こり1890年頃に交流が勝った。工場の動力の半分強が電化されたのは最初の中央発電所から約40年後の1920年代初めで、工場の配置の作り直しに時間がかかった。',
    sources=['src.ethw-pearlstreet','src.mokyr2008-handbook','src.david1990','src.owid-tech'],time=T(1882,1930,'1882年〜20世紀前半'))
upd('con.capitalism','深化：定義と起源の学説の違いを出典つきで','L0005 の主張照合',
    summary='私的所有・市場・資本の蓄積を軸とする経済の仕組み。定義と起源は学説で大きく違う：スミスは「自然的自由」と呼び、マルクスは資本家と労働者の構造的な関係と原始的蓄積を、ウェーバーは計算可能な合理的経営と「資本主義の精神」を、ブローデルは市場経済の上で独占と信用によって競争を逃れる層を資本主義と呼んだ。',
    sources=['src.sep-weber','src.thomas1984-braudel','src.marx1867-ch31'],epistemic='debate',confidence='high')
upd('thm.economy','出典登録：近代経済成長の定義と長期推計','Kuznets 1971、Maddison Project 2023',
    sources=['src.kuznets1971','src.maddison2023-rug'])
upd('thm.modernity','出典登録・深化：「複数の近代」の見方を追加','Eisenstadt 2000',
    summary='科学革命・啓蒙・産業革命・近代国家・帝国主義から、世界大戦・冷戦・情報化までの流れ。近代化を西洋化と同じとみる1950年代の近代化論に対し、近代は地域ごとに異なる形をとるとする「複数の近代」の見方がある。',
    sources=['src.eisenstadt2000','src.halperin-britannica-development'])
upd('thm.tech-history','出典登録：汎用技術の普及の遅さ','Crafts 2004、David 1990',sources=['src.owid-tech','src.crafts2004-steam','src.david1990'])
upd('thm.state-order','出典登録：近代国家の定義と国家形成の理論','Weber 1919、Tilly（Stuurman 1995）',sources=['src.weber1919-politik','src.stuurman1995-tilly','src.osiander2001'])
# ---- new nodes
add('con.great-divergence','concept','大分岐','Great Divergence',
    '西ヨーロッパ（とくに北西部）とアジアの経済の差が、いつ・なぜ開いたかをめぐる論争。ポメランツは長江デルタなどと英国の差を1800年頃と遅く置き、石炭の立地と植民地の「幽霊耕地」を重視した。ブロードベリーらの所得推計は、分岐はそれより早いがヨーロッパ中心の旧説より遅いとする。日本は北西ヨーロッパより低いが、中国・インドと違ってプラスの趨勢成長があった（アジア内の小分岐）。',
    ['D05','D07'],3,'thm.economy',T(1300,1900,'1300年頃〜1900年頃（論者により異なる）','分岐の時期は論者により1300年頃〜1800年頃'),
    'debate','high',['src.cage-pomeranz','src.pomeranz2000','src.broadberry-guan-li2018','src.bassino2019','src.parthasarathi2011'],3)
add('con.malthusian-escape','concept','マルサスの罠と近代経済成長','Malthusian trap and modern economic growth',
    '産業化以前は技術が進んでも人口が増えて一人あたり所得が長く伸びなかった（マルサスの罠）。18世紀後半以降、一人あたりの生産と人口がともに伸び続ける「近代経済成長」（クズネッツ）が一部の国で始まった。マディソン・プロジェクト2023年版では世界の加速ははっきり1820年以降で、それ以前にも局地的な成長の小島があった。',
    ['D05','D07'],3,'thm.economy',T(1820,None,'1820年頃〜'),'theory','high',['src.kuznets1971','src.maddison2023-rug','src.clark2007'],3)
add('con.high-wage-cheap-energy','concept','高賃金・安価なエネルギー説','High-wage, cheap-energy thesis',
    'アレンの説。18世紀の英国は賃金が国際的に高く石炭が安かったため、労働を資本とエネルギーで置き換える発明の採算が合った（誘発された発明）。改良後に海外へ普及した。手紡ぎの賃金は低く横ばいだったとする反証（ハンフリーズ＆シュナイダー2019）や、高賃金は主に男性の賃金の話だという批判がある。',
    ['D05','D04'],4,'con.industrial-revolution-causes',T(1700,1800,'18世紀'),'debate','high',['src.allen2011','src.allen2009','src.humphries-schneider2019','src.humphries-weisdorf2015'])
add('con.industrious-revolution','concept','勤勉革命','Industrious revolution',
    '産業革命の前に家計が時間と労働を組み替え、市場向けの生産と市場での購入を増やした変化（ド・フリース、需要側の特徴）。語を作った速水融は、江戸日本で家族経営の小農が手間をかける耕作で収量を上げたことに当てはめた。ド・フリースは日本の例を供給側の現象とみる。資本（機械・家畜）を使う産業革命と、労働を多く使う勤勉革命は逆の方向を向く。',
    ['D05','D07'],4,'con.industrial-revolution-causes',T(1600,1850,'17〜19世紀前半'),'theory','high',['src.devries1994','src.hayami2015','src.devries2011-consumer'])
add('con.institutions-growth','concept','制度と経済成長','Institutions and economic growth',
    '1688年の名誉革命後に英国王の約束が信用できるものになり、財政と資本市場が強まったとするノース＝ワインガスト説（1989）と、改革は1688年以前から進み金利も下がっていないとする批判、それに対するコックス（2012）の反論がある。アセモグルらは、大西洋交易で豊かになった商人層が財産権を求めた国で制度が大きく変わったとする。強制の弱い国では問題は略奪より調整の失敗だったという批判（イリゴイン＆グラーフェ）もある。',
    ['D05','D06'],4,'con.industrial-revolution-causes',T(1500,1850,'1500〜1850年'),'debate','high',['src.cox2012','src.pincus-robinson','src.ajr2005','src.irigoin-grafe2012','src.nobel-econ2025-popular'])
add('con.organic-mineral-economy','concept','有機経済から鉱物エネルギー経済へ','From organic to mineral-based energy economy',
    'リグリーの説。産業化以前の熱と動力（薪・人と家畜の筋肉）は光合成に頼り、土地の広さに縛られていた。数億年分の光合成が蓄積された石炭を蒸気機関で動力に変えて、その限界が外れた。代わりに社会はいつか尽き、地球を転換点へ押しやりうるエネルギー源に頼るようになった（「パンドラの箱」）。',
    ['D05','D04','D01'],4,'con.industrial-revolution-causes',T(1700,1900,'18〜19世紀'),'theory','high',['src.cam-wrigley2010'])
add('evt.steam-engine','event','蒸気機関の発達と普及','Steam engine',
    'ニューコメンの大気圧機関（1712年頃、炭鉱の排水）を、ワットが分離凝縮器（1765年に着想、1769年に特許）で改良し、石炭の消費を約3分の2減らした。ただし普及は遅く、蒸気の馬力が水力と並んだのは1830年頃、英国の労働生産性の伸びへの寄与が最大になったのは1850〜70年（年0.38%、うち鉄道0.26%）。',
    ['D04','D05'],4,'evt.industrial-revolution',T(1712,1870,'1712年〜1870年頃'),'fact','high',['src.sciencemuseum-watt2019','src.britannica-watt-engine','src.crafts2004-steam'])
add('evt.cotton-mechanization','event','綿工業の機械化とインド綿布','Mechanization of cotton textiles',
    '18世紀初め、綿布の最大の輸出国はインドで、英国の賃金はインドのおよそ4倍だった。ジェニー紡績機（1764年頃）、水力紡績機（1769年特許）、ミュール紡績機（1779年）で紡績が機械化され、英国の綿製品の輸出がインド綿布の輸入を上回ったのは1790年代初め。キャラコ禁止法（1701・1721〜1774年）の効果はほぼ中立と評価される。19世紀の原綿は米国南部の奴隷労働に大きく依存した。',
    ['D04','D05','D07'],4,'evt.industrial-revolution',T(1700,1860,'1700〜1860年'),'fact','high',['src.broadberry-gupta2009','src.broadberry-gupta-gehn','src.beckert2014-atlantic'])
add('con.slavery-industrialization','concept','奴隷制・植民地と産業化','Slavery, empire and industrialization',
    'ウィリアムズ（1944）は奴隷制と三角貿易の利益が英国の工業化の資金になったと論じた。エルティス＆エンガーマン（2000）は砂糖と奴隷貿易は特に大きな産業ではなかったとし、ヘブリッヒらは奴隷所有者の富が国民所得を約3.5%押し上げた（モデルによる推定）とする。ベッカートの「綿と奴隷制」論にも数量経済史からの批判がある。量的な重要性は論争だが、奴隷にされた人々が代価を払ったことは事実で、二つの問いは分けて考える。',
    ['D05','D07'],4,'con.industrial-revolution-causes',T(1700,1865,'18世紀〜1865年'),'debate','high',['src.eltis-engerman2000','src.heblich-redding-voth2022','src.mount2015-williams','src.olmstead-rhode2018','src.beckert2014-atlantic'])
add('evt.second-industrial-revolution','event','第二次産業革命','Second Industrial Revolution',
    'およそ1860/70〜1914年、科学をより集中的に使った技術の波。ベッセマー法（1856）などで鋼が安くなり、ドイツの化学工業は合成染料で世界市場の約85〜90%を占め、電化（1882年〜）、ハーバー＝ボッシュ法によるアンモニアの工業合成（1913年オッパウ）が続いた。米国は1840年までに製造業の労働生産性で英国を上回り、経済全体では1890年代に逆転した。',
    ['D04','D05'],3,'thm.tech-history',T(1860,1914,'1860/70〜1914年'),'fact','high',['src.mokyr2008-handbook','src.smg-bessemer','src.nobel-haber1918','src.basf-1913','src.broadberry-irwin2006'])
add('con.science-institutions','concept','科学の制度化：学会・学術誌・実験の作法','Institutionalization of science',
    '王立協会（1660年の会合が起点、1662年に勅許、標語「だれの言葉もうのみにしない」）、『フィロソフィカル・トランザクションズ』（1665年、当初は個人の事業）、国家が会員に給与を払うパリ王立科学アカデミー（1666）。査読は創刊時からではなく、審査は1832年、体系的な査読は19世紀半ばに定着した。ボイルの実験の「事実」は、装置・文章・作法の組み合わせで作られたとする研究もある。',
    ['D08','D07','D01'],3,'evt.scientific-revolution',T(1660,1850,'1660年〜19世紀半ば'),'fact','high',['src.royalsociety-history','src.royalsociety-phil-trans-history','src.st-andrews-phil-trans','src.lindahall-academie','src.shapin-schaffer1985'],2,
    [{"label":"ヨーロッパ外の科学","view":"清ではイエズス会士が既存の国家天文学の制度（欽天監）に登用された。日本では『解体新書』（1774）がオランダ語訳の解剖書から訳された。","sources":["src.mhs-oxford-chinese-heaven","src.jpsearch-kaitai-shinsho"]}])
add('evt.newtonian-synthesis','event','『プリンキピア』とニュートンの総合','Newton\'s Principia',
    'ニュートンの『自然哲学の数学的諸原理』（1687）は、天体と地上の運動を一つの数学的法則で扱った。初版は約300部。英国では1700〜1710年頃に定着したが、大陸では遠隔作用への反発から受容が1740〜50年代に遅れ、教科書の「ニュートン力学」の多くは1740〜1800年に大陸で作り直された。ニュートンは錬金術・神学にも同じくらいの労力を注いだ。',
    ['D01','D08','D07'],4,'evt.scientific-revolution',T(1687,1800,'1687年〜18世紀末'),'fact','high',['src.sep-newton'])
add('con.sovereign-state','concept','主権国家と「ウェストファリア神話」','Sovereign state and the Westphalian myth',
    'ウェーバーは「今日の国家」を、一定の領域の内部で正当な物理的暴力の独占を実効的に要求する人間の共同体と定義した（1919）。1648年のウェストファリア条約が主権国家体系を作ったという通説は、19〜20世紀の関心から作られた過去だとする批判がある（オジアンダー2001）。英国は課税と国債で戦争を支える「財政＝軍事国家」になり（ブリュワー）、ティリーは戦争と資本の組み合わせで国家形成を説明した。',
    ['D06','D07'],3,'thm.state-order',T(1648,1900,'17〜19世紀'),'debate','high',['src.weber1919-politik','src.britannica-westphalia','src.osiander2001','src.stone1990-nyrb-brewer','src.stuurman1995-tilly'])
add('con.nationalism','concept','ナショナリズムと国民国家','Nationalism and the nation-state',
    '国民は古くからあったとする原初主義（穏健版にスミスのエスノ象徴主義）と、近代に生まれたとする近代主義が対立する。アンダーソンは出版資本主義が匿名の同胞の「想像の共同体」を作ったとし、ゲルナーは産業社会が標準化された高い文化を求めたとした。ホブズボームらは古く見える伝統の多くが19世紀後半以降に作られたと論じた。',
    ['D06','D07','D09'],3,'thm.state-order',T(1776,1914,'18世紀後半〜20世紀初め'),'debate','high',['src.sep-nationalism','src.anderson1991','src.oleary1997','src.hobsbawm1983-intro'])
add('evt.haitian-revolution','event','ハイチ革命','Haitian Revolution',
    '1791年8月、サン＝ドマング（世界有数の砂糖植民地。約50万人が奴隷にされていた）で奴隷にされた人々が蜂起し、1793〜94年に奴隷制が廃止され、1804年1月1日にハイチとして独立した。元奴隷が建てた最初の国。フランスは1825年、承認と引き換えに1億5000万フランの賠償を課し（1838年に9000万へ減額）、支払いと借款の返済は20世紀まで続いた。',
    ['D07','D06'],4,'evt.atlantic-revolutions',T(1791,1804,'1791〜1804年'),'fact','high',['src.britannica-haitian-revolution','src.bnf-haiti-debt','src.un-news-2025-haiti','src.trouillot1995'])
add('evt.meiji-industrialization','event','開国・明治維新と日本の工業化','Opening of Japan, Meiji Restoration and industrialization',
    'ペリー来航（1853）と日米和親条約（1854）、領事裁判権と協定関税を含む日米修好通商条約（1858）で開国した。明治政府は岩倉使節団（1871〜73）、お雇い外国人と留学生による置き換え、官営模範工場の富岡製糸場（1872）などで技術を導入した。工女の長時間労働、足尾鉱毒、アイヌの土地の喪失などの代価を伴った。条約改正は1894年（領事裁判権の撤廃）と1911年（関税自主権）に実現した。',
    ['D07','D04','D05'],3,'thm.modernity',T(1853,1911,'1853〜1911年'),'fact','high',['src.ndl-kaikoku','src.bunka-ansei-treaty','src.jacar-iwakura','src.mext-gakusei100-oyatoi','src.bunka-tomioka','src.ishii2024-tomioka-factory-act','src.mofa-treaty-revision-1894','src.huffman2010-ashio','src.mlit-hokkaido-ainu'],2,
    [{"label":"代価","view":"小作の家族と女工の労働が工業化と国家を支えたとする見方（鶴見『Factory Girls』）。","sources":["src.tsurumi1990"]}])
add('evt.opium-wars','event','アヘン戦争と東アジアの開港','Opium Wars',
    '英国商人がインドから中国へ違法に持ち込んだアヘンが1820年頃以降に急増し、清の取り締まりを機に第一次アヘン戦争（1839〜42）が起きた。南京条約（1842）で香港島の割譲、5港の開港、計2100万ドルの賠償が定められ、最初の不平等条約となった。第二次アヘン戦争（1856〜60）では英仏が北京を占領した。同時期の太平天国の乱（1850〜64）の死者は約2000万人と推定される。',
    ['D07','D06'],4,'evt.imperialism',T(1839,1864,'1839〜1864年'),'fact','high',['src.britannica-opium-wars','src.britannica-treaty-nanjing','src.usc-treaty-nanjing-text','src.britannica-taiping'])
add('evt.scramble-for-africa','event','アフリカ分割','Scramble for Africa',
    '1870年代にヨーロッパが支配したアフリカの領域は約10%だったが、1914年には約90%となり、独立を保ったのはエチオピアとリベリアだけだった。ベルリン会議（1884〜85、14か国、アフリカの代表なし）は領有の主張に「実効的占有」を求めた。コンゴ自由国（1885〜1908）では強制労働と暴力が行われ、ドイツ領南西アフリカでのヘレロ・ナマへのジェノサイド（1904〜08）はドイツ政府が2021年に認めた。エチオピアはアドワの戦い（1896）でイタリアを破った。',
    ['D07','D06'],4,'evt.imperialism',T(1870,1914,'1870年代〜1914年'),'fact','high',['src.britannica-scramble-africa','src.whe-berlin-conference','src.britannica-congo-free-state','src.auswaertiges-amt-2021-namibia','src.britannica-adwa'])
add('evt.abolition','event','奴隷貿易・奴隷制の廃止','Abolition of the slave trade and slavery',
    '英国は1807年に奴隷貿易を、1833年の法（1834年施行）で奴隷制を廃止した。元奴隷は1838年まで年季奉公人として縛られ、奴隷所有者には当時の政府支出の約40%にあたる2000万ポンドが補償された（奴隷にされた側への補償はなかった）。1831年のジャマイカの大反乱が廃止を早めた。米国は1865年（修正第13条）、ブラジルは1888年に廃止した。',
    ['D07','D06','D05'],4,'evt.atlantic-colonialism',T(1807,1888,'1807〜1888年'),'fact','high',['src.rmg-slave-trade-end','src.tna-1833-abolition','src.fullfact-slavery-loan','src.ucl-lbs-context','src.tna-baptist-war','src.nara-13th-amendment','src.brown-brazil-abolition'])
add('con.industrial-labour','concept','工場労働と生活水準','Industrial labour and living standards',
    '19世紀前半の英国では労働者一人あたりの生産が伸びたのに実質賃金が伸び悩み（1800〜30年は年0.00%）、利潤率が倍増した（アレンの「エンゲルスの休止」）。1840〜1900年には実質賃金が約123%伸びた。成人男性の身長は1820〜39年生まれ（約173cm）の後に下がり、1860〜79年生まれからゆっくり回復した。児童労働の参加は1800〜1830年代に最も高く、1833年工場法が9歳未満の就労を禁じた。',
    ['D05','D10','D07'],4,'evt.industrial-revolution',T(1780,1900,'1780〜1900年'),'debate','high',['src.allen-engels2009','src.floud1998','src.tna-factoryact1833','src.humphries2010'])
# 理解レイヤー（Examiner への提案：status のみ presented。level は変えない）
# ---- edges
eid=max(int(e['id'][2:]) for e in E)
def edge(f,t,typ,epi,note,src):
    global eid; eid+=1
    assert f in ids and t in ids,(f,t); need(src)
    E.append(dict(id=f'e.{eid:04d}',**{'from':f},to=t,type=typ,epistemic=epi,note=note,sources=src))
edge('evt.scientific-revolution','con.science-institutions','enables','fact','学会と学術誌が実験の報告と検証の場になった',['src.royalsociety-history','src.royalsociety-phil-trans-history'])
edge('evt.newtonian-synthesis','evt.enlightenment','enables','theory','『プリンキピア』が啓蒙の時代の模範とされた',['src.sep-enlightenment'])
edge('evt.enlightenment','con.industrial-revolution-causes','supports','debate','有用な知識と産業的啓蒙が持続的な技術進歩の前提になったとする説（モキイア）',['src.nobel-econ2025-popular'])
edge('con.high-wage-cheap-energy','evt.industrial-revolution','causes','debate','高賃金と安い石炭が労働節約型の発明を英国で採算に乗せた（アレン説。反証あり）',['src.allen2011','src.humphries-schneider2019'])
edge('con.organic-mineral-economy','con.malthusian-escape','enables','theory','土地に縛られたエネルギーの限界が石炭で外れ、成長が止まらなくなった（リグリー）',['src.cam-wrigley2010'])
edge('evt.steam-engine','con.organic-mineral-economy','enables','fact','石炭を動力に変える装置',['src.cam-wrigley2010','src.sciencemuseum-watt2019'])
edge('con.institutions-growth','evt.industrial-revolution','causes','debate','名誉革命後の信用できる約束が財政と資本市場を強めたとする説と批判',['src.cox2012','src.pincus-robinson'])
edge('evt.atlantic-colonialism','con.institutions-growth','causes','theory','大西洋交易で豊かになった商人層が財産権を求めた（アセモグルら）',['src.ajr2005'])
edge('con.great-divergence','con.industrial-revolution-causes','raises','debate','分岐の時期の推計が、どの原因説が成り立つかを左右する',['src.cage-pomeranz','src.broadberry-guan-li2018'])
edge('evt.atlantic-colonialism','con.great-divergence','causes','debate','植民地の「幽霊耕地」が英国の土地の制約を緩めた（ポメランツ）',['src.cage-pomeranz'])
edge('con.industrious-revolution','evt.industrial-revolution','precedes','theory','家計の勤勉革命が産業革命に先行した（ド・フリース）',['src.devries1994'])
edge('con.industrious-revolution','evt.meiji-industrialization','precedes','theory','江戸日本の勤勉革命（速水融）が明治の工業化の土台になった',['src.hayami2015'])
edge('evt.cotton-mechanization','evt.industrial-revolution','part_of','fact','産業革命の中心部門',['src.broadberry-gupta-gehn'])
edge('con.slavery-industrialization','evt.cotton-mechanization','supports','debate','米国南部の奴隷労働が原綿を供給した。量的な重要性は論争',['src.beckert2014-atlantic','src.olmstead-rhode2018'])
edge('con.slavery-industrialization','con.industrial-revolution-causes','supports','debate','奴隷制の利益が工業化の資金になったとする説（ウィリアムズ）と批判',['src.mount2015-williams','src.eltis-engerman2000','src.heblich-redding-voth2022'])
edge('evt.industrial-revolution','con.industrial-labour','causes','debate','生産性の伸びが当初は利潤に偏り、都市の生活環境が悪化した',['src.allen-engels2009','src.floud1998'])
edge('evt.industrial-revolution','evt.second-industrial-revolution','precedes','fact','',['src.mokyr2008-handbook'])
edge('evt.second-industrial-revolution','evt.electrification','part_of','fact','',['src.mokyr2008-handbook'])
edge('evt.steam-engine','evt.imperialism','enables','debate','蒸気船・鉄道が支配を可能にしたとする「帝国の道具」論（技術決定論への批判あり）',['src.gillin2018-niger'])
edge('evt.imperialism','evt.opium-wars','part_of','fact','',['src.britannica-opium-wars'])
edge('evt.imperialism','evt.scramble-for-africa','part_of','fact','',['src.britannica-scramble-africa'])
edge('evt.haitian-revolution','evt.abolition','causes','theory','奴隷にされた人々自身の蜂起が廃止を促した（ハイチ、1831年ジャマイカ）',['src.rmg-slave-trade-end','src.tna-baptist-war'])
edge('evt.atlantic-revolutions','con.nationalism','enables','theory','主権を国民に置く考え（人権宣言第3条）と、西半球の独立国家が国民国家のモデルになった',['src.elysee-ddhc1789','src.anderson1991'])
edge('con.sovereign-state','con.state-formation-theories','instance_of','theory','近代国家の定義（ウェーバー）と戦争による国家形成（ティリー）',['src.weber1919-politik','src.stuurman1995-tilly'])
edge('evt.opium-wars','evt.meiji-industrialization','precedes','fact','清の敗北と不平等条約が、日本の開国と条約の型の前例になった',['src.bunka-ansei-treaty'])
edge('evt.meiji-industrialization','evt.imperialism','part_of','fact','日本は不平等条約を課された側から、下関条約（1895）で課す側にもなった',['src.naj-shimonoseki','src.naj-sino-japanese-commerce-1896'])
edge('con.organic-mineral-economy','q.ai-vs-past-revolutions','raises','hypothesis','エネルギーの制約と汎用技術の普及の遅さは、AIの比較の手がかりになるが類比には限界がある',['src.crafts2004-steam','src.david1990'])
edge('evt.electrification','q.ai-vs-past-revolutions','analogous','theory','電動機の生産性効果は工場の作り直しを待って遅れた（デイヴィッドの類比。本人は文字通りに取るなと警告）',['src.david1990'])
for i,n in ids.items():
    if 'P01-S05' in (n.get('curriculum') or []) or i in ('con.capitalism','thm.state-order'):
        U['nodes'].setdefault(i,{"level":0,"status":"unseen","history":[],"next_review":None,"recheck":False})
        U['nodes'][i]['status']='presented'
json.dump(N,open(R+'data/graph/nodes.json','w'),ensure_ascii=False,indent=1)
json.dump(E,open(R+'data/graph/edges.json','w'),ensure_ascii=False,indent=1)
json.dump(S,open(R+'data/sources.json','w'),ensure_ascii=False,indent=1)
json.dump(U,open(R+'data/understanding.json','w'),ensure_ascii=False,indent=1)
print('nodes',len(N),'edges',len(E),'sources',len(S))
