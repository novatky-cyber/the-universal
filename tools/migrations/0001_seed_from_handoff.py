"""地図 v1.0 の初期データを、引き継ぎ資料（docs/reference/handoff_mapofchaos.md）から生成する。

一度だけ実行する移行スクリプト。生成後の正本は data/ 以下のJSONであり、以後はJSONを直接更新する。
実行： python3 tools/migrations/0001_seed_from_handoff.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
TODAY = "2026-11-23"
NOW_YEAR = 2026

nodes, edges, sources = [], [], []


def ya_from_year(year):  # 西暦（紀元前は負）→ 何年前
    return NOW_YEAR - year


def T(start, end=None, label="", unc=None):
    t = {"start_ya": start, "end_ya": end, "label": label}
    if unc:
        t["uncertainty"] = unc
    return t


def N(id, type, ja, en, summary, domains, level, parent, time, ep, conf="high",
      src=(), cur=(), target=2, body=None, persp=None):
    n = {
        "id": id, "type": type, "title": {"ja": ja, "en": en}, "summary": summary,
        "domains": list(domains), "level": level, "parent": parent, "time": time,
        "epistemic": ep, "confidence": conf, "sources": list(src),
        "verification": {"status": "unverified", "date": None, "by": None},
        "target_level": target, "curriculum": list(cur),
        "history": [{"map_version": "1.0", "change": "作成", "reason": "引き継ぎ資料からの初期投入"}],
    }
    if body:
        n["body"] = body
    if persp:
        n["perspectives"] = persp
    nodes.append(n)


def E(frm, to, type, ep="theory", note=None, src=()):
    e = {"id": f"e.{len(edges)+1:04d}", "from": frm, "to": to, "type": type, "epistemic": ep}
    if note:
        e["note"] = note
    if src:
        e["sources"] = list(src)
    edges.append(e)


def S(id, title, url="", author="", publisher="", year=None, kind="agency", existence="unverified", note=""):
    s = {"id": id, "title": title, "url": url, "author": author, "publisher": publisher, "year": year,
         "kind": kind, "existence": existence, "checked_at": TODAY if existence == "verified" else None}
    if note:
        s["note"] = note
    sources.append(s)


# ---------------------------------------------------------------- 資料
S("src.planck2018-vi", "Planck 2018 results. VI. Cosmological parameters", "https://arxiv.org/abs/1807.06209",
  "Planck Collaboration", "Astronomy & Astrophysics 641, A6", 2020, "primary", "verified")
S("src.ics-chart-2024", "International Chronostratigraphic Chart (v2024/12)", "https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf",
  "Cohen, Finney, Gibbard, Fan", "International Commission on Stratigraphy", 2024, "agency", "verified")
S("src.desi-dr2-2025", "New DESI Results Strengthen Hints That Dark Energy May Evolve",
  "https://newscenter.lbl.gov/2025/03/19/new-desi-results-strengthen-hints-that-dark-energy-may-evolve/",
  "", "Lawrence Berkeley National Laboratory", 2025, "agency", "verified")
S("src.h0dn-2026", "A global collaboration reaches 1% precision on the local expansion rate of the Universe",
  "https://icc.ub.edu/news/a-global-collaboration-reaches-1-precision-local-expansion-rate-universe",
  "", "Institute of Cosmos Sciences, University of Barcelona", 2026, "agency", "verified")
S("src.nasa-hubble-tension", "NASA's Webb, Hubble Telescopes Affirm Universe's Expansion Rate, Puzzle Persists",
  "https://science.nasa.gov/missions/webb/nasas-webb-hubble-telescopes-affirm-universes-expansion-rate-puzzle-persists/",
  "", "NASA", 2024, "agency", "verified")
S("src.nasa-universe", "Universe Overview", "https://science.nasa.gov/universe/overview/", "", "NASA", None, "agency")
S("src.nasa-webb-bigbang", "Big Bang and the Evolution of the Universe (Webb)",
  "https://science.nasa.gov/mission/webb/big-bang-and-the-evolution-of-the-universe/", "", "NASA", None, "agency")
S("src.nasa-solar-system", "Solar System Facts", "https://science.nasa.gov/solar-system/solar-system-facts/", "", "NASA", None, "agency")
S("src.esa-planck", "Planck", "https://www.esa.int/Science_Exploration/Space_Science/Planck", "", "ESA", None, "agency")
S("src.usgs-age-earth", "Age of the Earth", "https://pubs.usgs.gov/gip/geotime/age.html", "", "USGS", None, "agency")
S("src.sep-cosmology", "Philosophy of Cosmology", "https://plato.stanford.edu/entries/cosmology/", "Smeenk & Ellis",
  "Stanford Encyclopedia of Philosophy", None, "reference")
S("src.sep-time-thermo", "Thermodynamic Asymmetry in Time", "https://plato.stanford.edu/entries/time-thermo/", "Callender",
  "Stanford Encyclopedia of Philosophy", None, "reference")
S("src.chou2010", "Optical Clocks and Relativity", "https://doi.org/10.1126/science.1192720",
  "Chou, Hume, Rosenband, Wineland", "Science 329, 1630", 2010, "primary")
S("src.ashby2003", "Relativity in the Global Positioning System", "https://doi.org/10.12942/lrr-2003-1",
  "Ashby", "Living Reviews in Relativity 6, 1", 2003, "review")
S("src.penzias-wilson-1965", "A Measurement of Excess Antenna Temperature at 4080 Mc/s", "https://doi.org/10.1086/148307",
  "Penzias & Wilson", "Astrophysical Journal 142, 419", 1965, "primary")
S("src.fixsen2009", "The Temperature of the Cosmic Microwave Background", "https://doi.org/10.1088/0004-637X/707/2/916",
  "Fixsen", "Astrophysical Journal 707, 916", 2009, "primary")
S("src.hubble1929", "A relation between distance and radial velocity among extra-galactic nebulae",
  "https://doi.org/10.1073/pnas.15.3.168", "Hubble", "PNAS 15, 168", 1929, "primary")
S("src.pdg-bbn", "Big-Bang Nucleosynthesis (Review of Particle Physics)", "https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf",
  "Fields, Molaro, Sarkar", "Particle Data Group", 2024, "review")
S("src.nobel2011", "The Nobel Prize in Physics 2011 — Press release", "https://www.nobelprize.org/prizes/physics/2011/press-release/",
  "", "Nobel Prize Outreach", 2011, "agency")
S("src.codata-planck-time", "CODATA value: Planck time", "https://physics.nist.gov/cgi-bin/cuu/Value?plkt", "", "NIST", None, "agency")
S("src.jades-z14", "A shining cosmic dawn: spectroscopic confirmation of two luminous galaxies at z≈14",
  "https://doi.org/10.1038/s41586-024-07860-9", "Carniani et al.", "Nature 633, 318", 2024, "primary")
S("src.smithsonian-human", "Introduction to Human Evolution", "https://humanorigins.si.edu/education/introduction-human-evolution",
  "", "Smithsonian Institution", None, "agency")
S("src.big-history", "Big History Project", "https://www.bighistoryproject.com/", "", "Big History Project", None, "reference")
S("src.unesco-silk", "Silk Roads Programme", "https://www.unesco.org/en/silk-roads", "", "UNESCO", None, "agency")
S("src.owid-tech", "Technology over the long run", "https://ourworldindata.org/technology-long-run", "", "Our World in Data", None, "reference")
S("src.dartmouth-ai", "Artificial Intelligence Coined at Dartmouth", "https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth",
  "", "Dartmouth College", None, "agency")
S("src.vaswani2017", "Attention Is All You Need", "https://arxiv.org/abs/1706.03762", "Vaswani et al.", "NeurIPS 2017", 2017, "primary")
S("src.openai-chatgpt", "Introducing ChatGPT", "https://openai.com/index/chatgpt/", "", "OpenAI", 2022, "primary")
S("src.hai-ai-index", "AI Index Report", "https://hai.stanford.edu/ai-index", "", "Stanford HAI", None, "agency")
S("src.ai100", "One Hundred Year Study on Artificial Intelligence (AI100)", "https://ai100.stanford.edu/", "", "Stanford University", None, "agency")
S("src.iea-energy-ai", "Energy and AI", "https://www.iea.org/reports/energy-and-ai", "", "IEA", 2025, "agency")
S("src.ipcc-ar6-syr", "AR6 Synthesis Report: Climate Change 2023", "https://www.ipcc.ch/report/ar6/syr/", "", "IPCC", 2023, "agency")
S("src.un-wpp", "World Population Prospects", "https://population.un.org/wpp/", "", "United Nations", None, "agency")
S("src.unesco-futures", "Futures Literacy", "https://www.unesco.org/en/futures-literacy", "", "UNESCO", None, "agency")
S("src.uk-systems", "Systems thinking for civil servants", "https://www.gov.uk/government/publications/systems-thinking-for-civil-servants",
  "", "UK Government", 2022, "agency")
S("src.uk-futures", "The Futures Toolkit", "https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts",
  "", "UK Government", 2017, "agency")
S("src.dunlosky2013", "Improving Students' Learning With Effective Learning Techniques", "https://doi.org/10.1177/1529100612453266",
  "Dunlosky et al.", "Psychological Science in the Public Interest 14(1)", 2013, "review")

# ---------------------------------------------------------------- テーマ（level 2）
BB = 13.8e9
N("thm.cosmology", "theme", "宇宙論と宇宙史", "Cosmology & cosmic history",
  "高温・高密度の初期宇宙から現在までの宇宙の進化と、その証拠・理論・未解明を扱う。", ["D01"], 2, None,
  T(BB, 0, "約138億年前〜現在"), "theory", "high", ["src.nasa-universe", "src.planck2018-vi"], ["P01-S01"], 3)
N("thm.time", "theme", "時間と時空", "Time & spacetime",
  "時間とは何か、時間に始まりはあるか、なぜ時間に向きがあるのかを、物理学と哲学から扱う。", ["D01", "D08"], 2, None,
  None, "debate", "high", ["src.sep-cosmology", "src.sep-time-thermo"], ["P01-S01"], 3)
N("thm.matter", "theme", "物質・元素・エネルギー", "Matter, elements & energy",
  "軽元素の合成から恒星・超新星などによる元素の生成、物質とエネルギーの性質までを扱う。", ["D01"], 2, None,
  T(BB, 0, "約138億年前〜現在"), "theory", "high", ["src.pdg-bbn"], ["P01-S01"], 2)
N("thm.earth-solar", "theme", "太陽系と地球", "Solar system & Earth",
  "太陽系と地球の形成、その年代の測り方、地球環境の長期的な変化を扱う。", ["D01"], 2, None,
  T(4.567e9, 0, "約46億年前〜現在"), "fact", "high", ["src.ics-chart-2024", "src.usgs-age-earth"], ["P01-S01"], 2)
N("thm.probability", "theme", "確率・統計・推論", "Probability, statistics & inference",
  "不確実なことを数で扱い、証拠から結論を導く方法。AIの学習・推論の数学的な基盤でもある。", ["D02"], 2, None,
  None, "theory", "high", [], ["P02-S03"], 3)
N("thm.computation", "theme", "計算と情報", "Computation & information",
  "論理・計算理論・情報理論。計算機とは何か、計算できることの限界は何かを扱う。", ["D02"], 2, None,
  None, "theory", "high", [], ["P02-S01"], 3)
N("thm.life", "theme", "生命の起源と進化", "Origin & evolution of life",
  "生命の起源（未解明）と、その後の進化・絶滅・生態系の変化を扱う。起源と進化は別の問題として区別する。", ["D03"], 2, None,
  T(4.0e9, 0, "約40億年前？〜現在", "生命の起源の時期は未確定"), "theory", "high", ["src.ics-chart-2024"], ["P01-S02"], 2)
N("thm.human-evolution", "theme", "人類の進化", "Human evolution",
  "人類系統の分岐からホモ・サピエンスの出現、道具・火・言語・累積的文化の発展までを扱う。", ["D03", "D07"], 2, None,
  T(7e6, 0, "約700万年前〜現在", "分岐年代に幅"), "theory", "high", ["src.smithsonian-human"], ["P01-S03"], 2)
N("thm.mind", "theme", "脳・認知・知能", "Brain, cognition & intelligence",
  "人間の知能はどう成り立つか。AIの知能との共通点・相違点を考える基盤。", ["D03", "D08"], 2, None,
  None, "debate", "medium", [], ["P01-S07"], 3)
N("thm.tech-history", "theme", "技術革新の歴史", "History of technological change",
  "道具・農耕・印刷・産業革命・電化・コンピューターまで、技術の変化と社会の関係を扱う。", ["D04"], 2, None,
  T(3.3e6, 0, "数百万年前〜現在"), "theory", "high", ["src.owid-tech"], ["P01-S05"], 2)
N("thm.ai-history", "theme", "計算機とAIの歴史", "History of computing & AI",
  "機械式計算から電子計算機、AI研究の誕生、深層学習、Transformer、生成AIまでの流れ。", ["D04", "D02"], 2, None,
  T(ya_from_year(1640), 0, "17世紀〜現在"), "fact", "high", ["src.dartmouth-ai", "src.vaswani2017"], ["P01-S07", "P02-S04"], 4)
N("thm.economy", "theme", "経済発展と資本主義", "Economic development & capitalism",
  "資本主義・労働・企業・金融・イノベーションと、経済の長期的な変化を扱う。", ["D05"], 2, None,
  T(500, 0, "近世〜現在"), "debate", "medium", [], ["P01-S05", "P03-S01"], 2)
N("thm.ai-economy", "theme", "AIと経済", "AI & the economy",
  "AIによって生産性・雇用・賃金・企業利益がどう変わるか。因果の推定が難しい領域。", ["D05"], 2, None,
  T(10, -10, "2010年代〜近未来"), "debate", "medium", [], ["P02-S05"], 3)
N("thm.state-order", "theme", "国家と国際秩序", "States & international order",
  "国家・民主主義・権力・法・地政学・国際秩序の成り立ちと変化を扱う。", ["D06"], 2, None,
  T(5500, 0, "初期国家〜現在"), "theory", "medium", [], ["P01-S06", "P03-S02"], 2)
N("thm.ai-governance", "theme", "AIの開発・支配・規制", "AI development, power & regulation",
  "AIを誰が開発・支配・規制するのか。国家競争・安全保障・制度設計を扱う。", ["D06"], 2, None,
  T(10, -10, "2010年代〜近未来"), "debate", "medium", [], ["P03-S02"], 2)
N("thm.civilization", "theme", "文明の成立", "Emergence of civilizations",
  "農耕・牧畜、都市、初期国家、文字の発展。地域ごとに経路が異なり、必然の一本道ではない。", ["D07"], 2, None,
  T(12000, 2500, "約1万2000年前〜古代"), "theory", "medium", [], ["P01-S03"], 2)
N("thm.world-history", "theme", "世界史の多地域比較", "Comparative world history",
  "同じ時代の世界を地域横断で見る。帝国・宗教・交易・思想・技術・芸術の交流と、支配・暴力も含める。", ["D07"], 2, None,
  T(5500, ya_from_year(1750), "紀元前3500年頃〜1750年頃"), "theory", "medium", ["src.unesco-silk"], ["P01-S04"], 2)
N("thm.modernity", "theme", "近代化と現代", "Modernization & the modern world",
  "科学革命・啓蒙・産業革命・近代国家・帝国主義・世界大戦・冷戦・情報化までの流れ。", ["D07", "D06"], 2, None,
  T(ya_from_year(1600), 0, "17世紀〜現在"), "theory", "medium", [], ["P01-S05", "P01-S06"], 2)
N("thm.epistemology", "theme", "認識論・科学哲学", "Epistemology & philosophy of science",
  "何を、どの根拠で知っていると言えるか。学問ごとの証拠と方法の違いを扱う。", ["D08"], 2, None,
  None, "theory", "medium", ["src.sep-cosmology"], ["P01-S01", "P01-S08"], 3)
N("thm.ethics", "theme", "倫理・価値・人間観", "Ethics, values & views of humanity",
  "知能・意識・人間・自由・幸福・責任とは何か。望ましさは観測事実だけでは決まらない。", ["D08"], 2, None,
  None, "normative", "medium", [], ["P03-S03"], 2)
N("thm.arts", "theme", "文化・文学・芸術と創造", "Culture, literature, arts & creativity",
  "美学・芸術史・文学・音楽・メディア。AIが生成できる時代に、創造や真正性の意味は何か。", ["D09"], 2, None,
  T(100000, 0, "先史時代〜現在", "象徴的行動の最古の証拠の年代には諸説"), "debate", "medium", [], ["P03-S04"], 2)
N("thm.systems", "theme", "複雑系・システム思考", "Complex systems & systems thinking",
  "要素の関係・フィードバック・非線形性・創発から全体を考える。", ["D10"], 2, None,
  None, "theory", "high", ["src.uk-systems"], ["P01-S01"], 3)
N("thm.futures", "theme", "未来研究", "Futures studies",
  "未来を複数の条件付きの可能性として考え、予測を記録して検証する。", ["D10"], 2, None,
  T(0, -30, "現在〜2050年代"), "hypothesis", "medium", ["src.uk-futures", "src.unesco-futures"], ["P04-S01"], 3)
N("thm.watch", "theme", "現代の重点観察テーマ", "Key contemporary issues",
  "AI・デジタル化、国際秩序、人口構造、エネルギー・気候、生物・医療技術、民主主義、所得分配、文化と価値。", ["D10", "D06"], 2, None,
  T(10, -10, "2010年代〜近未来"), "debate", "medium", ["src.ipcc-ar6-syr", "src.un-wpp"], ["P04-S01"], 2)

# ---------------------------------------------------------------- 第1回：時間と時空
N("con.newtonian-time", "concept", "ニュートンの絶対時間", "Newtonian absolute time",
  "時間は宇宙のどこでも一様に流れる、という考え方。日常的な速度・重力では非常によい近似になる。", ["D01", "D08"], 3, "thm.time",
  None, "theory", "high", ["src.sep-cosmology"], ["P01-S01"], 2)
N("thy.special-relativity", "theory", "特殊相対性理論", "Special relativity",
  "光速はどの観測者にも同じであり、時間と空間は観測者の運動によって変わる。時間と空間は一体の「時空」をなす。", ["D01"], 3, "thm.time",
  T(ya_from_year(1905), None, "1905年"), "theory", "high", ["src.chou2010"], ["P01-S01"], 2)
N("thy.general-relativity", "theory", "一般相対性理論", "General relativity",
  "重力を時空の曲がりとして説明する理論。重力の強い場所ほど時間の進み方が遅い。宇宙論の基礎になる。", ["D01"], 3, "thm.time",
  T(ya_from_year(1915), None, "1915年"), "theory", "high", ["src.ashby2003", "src.chou2010"], ["P01-S01"], 2)
N("con.spacetime", "concept", "時空", "Spacetime",
  "時間と空間を一体のものとして扱う四次元の枠組み。相対論では、時間は宇宙の外にある普遍的な時計ではない。", ["D01"], 3, "thm.time",
  None, "theory", "high", ["src.sep-cosmology"], ["P01-S01"], 2)
N("con.time-dilation", "concept", "時間の遅れ", "Time dilation",
  "運動している時計や、重力の強い場所にある時計は、遅れて進む。精密時計とGPSで実際に確かめられている。", ["D01"], 4, "thy.general-relativity",
  None, "fact", "high", ["src.chou2010", "src.ashby2003"], ["P01-S01"], 2)
N("evd.clock-tests", "evidence", "原子時計・GPSによる相対論の検証", "Clock & GPS tests of relativity",
  "高さを33cm変えただけで時計の進み方の差が測定された実験や、GPS衛星の時計補正が、相対論の時間の遅れを支える。", ["D01"], 4, "thy.general-relativity",
  T(ya_from_year(2010), None, "2010年の実験ほか"), "fact", "high", ["src.chou2010", "src.ashby2003"], ["P01-S01"], 2)
N("con.singularity", "concept", "特異点（初期宇宙）", "Initial singularity",
  "古典的な一般相対論を過去へたどると、密度が無限大になる点が現れる。実在の証明ではなく、理論の適用限界を示している可能性が高い。", ["D01"], 4, "thm.time",
  T(BB, None, "約138億年前（理論上）"), "hypothesis", "medium", ["src.sep-cosmology"], ["P01-S01"], 3)
N("con.planck-time", "concept", "プランク時間", "Planck time",
  "約5.39×10⁻⁴⁴秒。量子重力の効果が重要になると考えられる時間の尺度。「宇宙最初の一瞬」を立証する数字ではない。", ["D01"], 4, "thm.time",
  None, "theory", "high", ["src.codata-planck-time"], ["P01-S01"], 2)
N("thy.big-bounce", "theory", "ビッグバウンス仮説", "Big Bounce",
  "現在の膨張の前に、収縮する宇宙などの別の状態があったとする仮説群。観測による確証はない。", ["D01"], 4, "thm.time",
  None, "hypothesis", "medium", ["src.sep-cosmology"], ["P01-S01"], 2)
N("thy.emergent-time", "theory", "創発的な時間", "Emergent time",
  "時間を根本的な実在とせず、より根本的な（量子重力的な）構造から現れるものとみる研究の方向。未確立。", ["D01", "D08"], 4, "thm.time",
  None, "hypothesis", "low", ["src.sep-cosmology"], ["P01-S01"], 2)
N("con.arrow-of-time", "concept", "時間の矢", "Arrow of time",
  "割れたコップが元に戻らないような、巨視的な現象の不可逆性。時間の起源とは別の問題。", ["D01", "D08"], 3, "thm.time",
  None, "theory", "high", ["src.sep-time-thermo"], ["P01-S01"], 2)
N("con.entropy", "concept", "エントロピー", "Entropy",
  "巨視的な状態に対応する微視的な状態の数に関わる物理量。単に「乱雑さ」と言い換えると不正確になる。", ["D01", "D02"], 3, "thm.time",
  None, "theory", "high", ["src.sep-time-thermo"], ["P01-S01"], 2)
N("thy.second-law", "theory", "熱力学第二法則", "Second law of thermodynamics",
  "孤立した系のエントロピーは（統計的に）減らない。時間の矢を説明する主要な枠組み。", ["D01"], 3, "thm.time",
  None, "theory", "high", ["src.sep-time-thermo"], ["P01-S01"], 2)

# ---------------------------------------------------------------- 第1回：宇宙論
N("thy.hot-big-bang", "theory", "ビッグバン理論（高温高密度の初期宇宙）", "Hot Big Bang model",
  "宇宙はかつて高温・高密度の状態にあり、そこから膨張・冷却してきたとする理論。複数の独立した証拠に支えられている。", ["D01"], 3, "thm.cosmology",
  T(BB, None, "約138億年前"), "theory", "high", ["src.nasa-webb-bigbang", "src.planck2018-vi"], ["P01-S01"], 3)
N("con.cosmic-expansion", "concept", "宇宙膨張", "Cosmic expansion",
  "空間の尺度そのものが大きくなり、遠く離れた点どうしの距離が増えること。空間の一点での爆発ではなく、中心を必要としない。", ["D01"], 3, "thm.cosmology",
  None, "theory", "high", ["src.hubble1929", "src.nasa-universe"], ["P01-S01"], 3,
  persp=[{"label": "通俗的なイメージとの違い", "view": "原子・地球・太陽系・重力で束縛された銀河は、それ自体は膨張しない。"}])
N("thy.inflation", "theory", "インフレーション理論", "Cosmic inflation",
  "誕生直後の極めて短い時間に宇宙が急膨張したとする理論的枠組み。宇宙の一様さなどを説明する有力候補だが、機構と決定的な実証は未確立。", ["D01"], 4, "thm.cosmology",
  T(BB, None, "誕生直後の極短時間"), "debate", "medium", ["src.sep-cosmology", "src.planck2018-vi"], ["P01-S01"], 2)
N("thy.lcdm", "theory", "ΛCDMモデル（標準宇宙モデル）", "ΛCDM model",
  "宇宙定数Λ（ダークエネルギー）と冷たいダークマターを含む標準的な宇宙モデル。多くの観測をよく説明するが、緊張関係も指摘されている。", ["D01"], 3, "thm.cosmology",
  None, "theory", "high", ["src.planck2018-vi"], ["P01-S01"], 3)
N("con.dark-matter", "concept", "ダークマター", "Dark matter",
  "光では見えないが重力の効果から存在が推定される物質。ΛCDMでは宇宙のエネルギー密度の約26%。正体は不明。", ["D01"], 4, "thy.lcdm",
  None, "theory", "high", ["src.planck2018-vi"], ["P01-S01"], 2)
N("con.dark-energy", "concept", "ダークエネルギー", "Dark energy",
  "宇宙の加速膨張を説明する成分。ΛCDMでは約69%。正体は不明で、時間とともに変化する可能性も議論されている。", ["D01"], 4, "thy.lcdm",
  None, "theory", "medium", ["src.planck2018-vi", "src.nobel2011", "src.desi-dr2-2025"], ["P01-S01"], 2)
N("con.cosmic-composition", "concept", "宇宙の組成（エネルギー密度の内訳）", "Cosmic energy budget",
  "Planck 2018（ΛCDMを仮定）では、通常の物質 約4.9%、ダークマター 約26%、ダークエネルギー 約69%。体積の割合ではない。", ["D01"], 4, "thy.lcdm",
  None, "theory", "high", ["src.planck2018-vi"], ["P01-S01"], 2)
N("con.age-of-universe", "concept", "宇宙の年齢", "Age of the universe",
  "約138億年（Planck 2018、ΛCDMを仮定した推定で137.87±0.20億年）。直接計時した値ではなく、観測とモデルから推定した値。", ["D01"], 4, "thm.cosmology",
  None, "theory", "high", ["src.planck2018-vi"], ["P01-S01"], 2)
N("con.hubble-tension", "concept", "ハッブル張力", "Hubble tension",
  "宇宙の現在の膨張率（ハッブル定数）が、近傍の距離はしごによる測定（約73）と、CMBにΛCDMを当てはめた推定（約67）で食い違う問題。", ["D01"], 4, "thy.lcdm",
  T(10, 0, "2010年代〜現在"), "debate", "high", ["src.h0dn-2026", "src.nasa-hubble-tension", "src.planck2018-vi"], ["P01-S01"], 2)
N("con.evolving-dark-energy", "concept", "ダークエネルギーの時間変化の兆候", "Hints of evolving dark energy",
  "DESIなどの観測を組み合わせると、ダークエネルギーの影響が時間とともに弱まっている可能性が示唆されている。発見の基準（5σ）には未到達。", ["D01"], 4, "con.dark-energy",
  T(2, 0, "2024年〜現在"), "debate", "medium", ["src.desi-dr2-2025"], ["P01-S01"], 2)
N("evd.redshift", "evidence", "遠方銀河の赤方偏移", "Redshift of distant galaxies",
  "遠い銀河ほど光の波長が長く（赤く）ずれており、距離と赤方偏移の関係が宇宙膨張を支持する。", ["D01"], 4, "thy.hot-big-bang",
  T(ya_from_year(1929), None, "1929年（ハッブル）"), "fact", "high", ["src.hubble1929"], ["P01-S01"], 2)
N("evd.cmb", "evidence", "宇宙マイクロ波背景放射（CMB）", "Cosmic microwave background",
  "全天から届く約2.7Kの放射。約38万年後の宇宙の名残で、温度のわずかなゆらぎから宇宙の年齢や組成が推定される。", ["D01"], 4, "thy.hot-big-bang",
  T(ya_from_year(1965), None, "1965年に発見"), "fact", "high", ["src.penzias-wilson-1965", "src.fixsen2009", "src.planck2018-vi"], ["P01-S01"], 2)
N("evd.bbn-abundances", "evidence", "軽元素の存在比（ビッグバン元素合成）", "Light-element abundances",
  "水素・ヘリウムなどの量が、初期数分の元素合成の予測とよく一致する。リチウムには食い違いが残る。", ["D01"], 4, "thy.hot-big-bang",
  None, "fact", "high", ["src.pdg-bbn"], ["P01-S01"], 2)
N("con.lithium-problem", "concept", "リチウム問題", "Cosmological lithium problem",
  "古い恒星で観測されるリチウム7の量が、ビッグバン元素合成の予測より数倍少ない問題。原因は未解決。", ["D01"], 4, "evd.bbn-abundances",
  None, "unknown", "high", ["src.pdg-bbn"], ["P01-S01"], 1)

# ---------------------------------------------------------------- 年表：宇宙・地球・生命
N("evt.hot-dense-early", "event", "高温・高密度の初期宇宙からの膨張", "Expansion from the hot dense early universe",
  "約138億年前、宇宙は高温・高密度の状態から膨張を始めた。究極の始まりは未解明。", ["D01"], 3, "thm.cosmology",
  T(BB, None, "約138億年前"), "theory", "high", ["src.planck2018-vi", "src.nasa-universe"], ["P01-S01"], 2)
N("evt.inflation-epoch", "event", "インフレーション期（仮説）", "Inflationary epoch",
  "誕生直後の極めて短い時間に起きたとされる急膨張。", ["D01"], 4, "thy.inflation",
  T(BB, None, "誕生直後"), "hypothesis", "medium", ["src.sep-cosmology"], ["P01-S01"], 1)
N("evt.bbn", "event", "ビッグバン元素合成", "Big Bang nucleosynthesis",
  "誕生後の最初の数分間に、主に水素・ヘリウムの原子核がつくられた（中性の原子ができるのは約38万年後）。", ["D01"], 3, "thm.matter",
  T(BB, None, "誕生後数分"), "theory", "high", ["src.pdg-bbn"], ["P01-S01"], 2)
N("evt.recombination", "event", "再結合（宇宙の晴れ上がり）", "Recombination",
  "約38万年後、電子と原子核が結びついて中性の原子ができ、光がまっすぐ進めるようになった。CMBの起源。", ["D01"], 3, "thm.cosmology",
  T(BB - 3.8e5, None, "誕生後約38万年"), "theory", "high", ["src.planck2018-vi", "src.nasa-webb-bigbang"], ["P01-S01"], 2)
N("evt.first-galaxies", "event", "最初の恒星・銀河の形成", "First stars & galaxies",
  "最初の数億年のうちに、重力によって恒星と銀河が形成された。JWSTは誕生後約3億年の銀河を分光で確認している。", ["D01"], 3, "thm.cosmology",
  T(13.5e9, None, "誕生後数億年"), "theory", "high", ["src.jades-z14", "src.nasa-webb-bigbang"], ["P01-S01"], 2)
N("evt.element-synthesis", "event", "恒星・超新星などによる元素の生成", "Stellar nucleosynthesis",
  "恒星内部の核融合、超新星爆発、中性子星の合体などで、炭素・酸素・鉄などの多様な元素がつくられ、宇宙に広がった。", ["D01"], 3, "thm.matter",
  T(13.5e9, 0, "数十億年にわたり継続"), "theory", "high", ["src.nasa-universe"], ["P01-S01"], 2)
N("evt.solar-system", "event", "太陽系の形成", "Formation of the Solar System",
  "約45.67億年前、原始太陽と原始惑星系円盤から太陽系が形成された。", ["D01"], 3, "thm.earth-solar",
  T(4.567e9, None, "約46億年前"), "fact", "high", ["src.ics-chart-2024", "src.nasa-solar-system"], ["P01-S01"], 2)
N("evt.earth-formation", "event", "地球の形成", "Formation of the Earth",
  "約45.4億年前。隕石などの放射年代測定から推定されている。", ["D01"], 3, "thm.earth-solar",
  T(4.54e9, None, "約45.4億年前"), "fact", "high", ["src.usgs-age-earth"], ["P01-S01"], 2)
N("evd.radiometric-dating", "evidence", "放射年代測定", "Radiometric dating",
  "放射性同位体が一定の速さで壊れることを利用して、岩石や隕石の年代を測る方法。", ["D01"], 4, "thm.earth-solar",
  None, "fact", "high", ["src.usgs-age-earth"], ["P01-S01"], 2)
N("evt.earliest-life", "event", "最古の生命活動の痕跡", "Earliest evidence of life",
  "遅くとも約35億年前には生命活動の痕跡がある。生命が誕生した時期と機構は不明。", ["D03"], 3, "thm.life",
  T(3.5e9, None, "遅くとも約35億年前", "より古い痕跡の主張もあるが議論が続く"), "theory", "medium", [], ["P01-S01", "P01-S02"], 2)
N("evt.goe", "event", "大酸化イベント", "Great Oxidation Event",
  "約24億年前、大気中の酸素が増えた。生命（光合成）が地球環境を大きく変えた例。", ["D03", "D01"], 3, "thm.life",
  T(2.4e9, None, "約24億年前"), "theory", "high", [], ["P01-S02"], 2)
N("evt.cambrian", "event", "カンブリア紀の動物の多様化", "Cambrian diversification",
  "カンブリア紀（約5億3880万年前から）に動物が急速に多様化した。変化はエディアカラ紀から段階的に進んだ面もある。", ["D03"], 3, "thm.life",
  T(538.8e6, None, "約5億3880万年前〜"), "fact", "high", ["src.ics-chart-2024"], ["P01-S02"], 2)
N("evt.kpg", "event", "白亜紀末の大量絶滅", "K–Pg extinction",
  "約6600万年前、非鳥類型の恐竜などが絶滅した。", ["D03"], 3, "thm.life",
  T(66e6, None, "約6600万年前"), "fact", "high", ["src.ics-chart-2024"], ["P01-S02"], 2)
N("evt.hominin-split", "event", "人類系統の分岐", "Hominin divergence",
  "約700万〜600万年前以降、チンパンジーとの共通祖先から人類の系統が分かれた。化石から推定される年代には幅がある。", ["D03"], 3, "thm.human-evolution",
  T(7e6, 6e6, "約700万〜600万年前", "推定に幅"), "theory", "medium", ["src.smithsonian-human"], ["P01-S03"], 2)
N("evt.homo-sapiens", "event", "ホモ・サピエンスの出現", "Emergence of Homo sapiens",
  "約30万年前、アフリカで現生人類が現れた。", ["D03"], 3, "thm.human-evolution",
  T(300000, None, "約30万年前"), "theory", "high", ["src.smithsonian-human"], ["P01-S03"], 2)
N("con.natural-selection", "concept", "自然選択", "Natural selection",
  "遺伝する変異のうち、生存・繁殖に有利なものが集団内に広がる過程。進化の主要な仕組みの一つ。", ["D03"], 3, "thm.life",
  None, "theory", "high", [], ["P01-S02"], 3)
N("con.cumulative-culture", "concept", "累積的文化・社会的学習", "Cumulative culture",
  "他者から学んだ知識や技術が世代を超えて積み重なり、改良されていくこと。文化を持つのは人間だけではない。", ["D03", "D07"], 3, "thm.human-evolution",
  None, "theory", "medium", [], ["P01-S03"], 3)
N("evt.tools-fire", "event", "道具と火の利用", "Tools & fire",
  "数百万年前から石器が使われ、のちに火の利用が広がった。協力と社会的学習の発展と結びつく。", ["D04", "D03"], 3, "thm.tech-history",
  T(3.3e6, None, "数百万年前〜", "最古の石器・火の利用の年代は議論がある"), "debate", "medium", [], ["P01-S03"], 2)
N("evt.symbolic-behavior", "event", "言語・象徴・芸術の発展", "Language, symbols & art",
  "先史時代に、言語・象徴・芸術・儀礼・広域の交流が発展した。単発の「革命」に還元しない。", ["D09", "D07"], 3, "thm.arts",
  T(100000, None, "先史時代", "最古の証拠の年代と解釈には諸説"), "debate", "low", [], ["P01-S03"], 2)

# ---------------------------------------------------------------- 文明・世界史・近代
N("evt.agriculture", "event", "農耕・牧畜の発展（複数地域）", "Agriculture (multiple centers)",
  "約1万2000年前以降、複数の地域でそれぞれ農耕・牧畜が始まった。移行は一様でなく、農耕から国家へは必然ではない。", ["D07"], 3, "thm.civilization",
  T(12000, None, "約1万2000年前以降"), "theory", "high", ["src.big-history"], ["P01-S03"], 2)
N("evt.early-states", "event", "都市と初期国家", "Cities & early states",
  "紀元前4千年紀以降、一部の地域で都市・行政・初期国家が展開した。", ["D07", "D06"], 3, "thm.civilization",
  T(6000, None, "紀元前4千年紀〜"), "theory", "medium", [], ["P01-S03"], 2)
N("evt.writing", "event", "初期の文字体系", "Early writing systems",
  "紀元前3200年頃からメソポタミアやエジプトなどで文字が使われた。記録・税・交易・法・知識の継承と関わる。他地域でも独自に発展。", ["D07"], 3, "thm.civilization",
  T(ya_from_year(-3200), None, "紀元前3200年頃〜"), "fact", "medium", [], ["P01-S03"], 2,
  persp=[{"label": "文字の有無と文明", "view": "文字を持たない文化も豊かであり、文字の有無で文明の優劣を決めない。"}])
N("con.periodization", "concept", "時代区分の相対性", "Periodization is contextual",
  "「古代→中世→近代」はヨーロッパ由来の区分であり、世界の全地域が同じ段階をたどったわけではない。", ["D07", "D08"], 3, "thm.world-history",
  None, "debate", "high", [], ["P01-S04"], 2)
N("con.trade-networks", "concept", "交易網による伝播", "Exchange networks",
  "シルクロードやインド洋交易などの交易網は、物資だけでなく数学・紙・印刷・宗教・美術様式も運んだ。", ["D07", "D09"], 3, "thm.world-history",
  T(2200, ya_from_year(1500), "古代〜近世"), "fact", "medium", ["src.unesco-silk"], ["P01-S04"], 2)
N("evt.printing", "event", "印刷技術の発展と普及", "Printing",
  "中国での木版・活字印刷の発展と、15世紀ヨーロッパの活版印刷の普及。知識の複製と流通を変えた。", ["D04", "D07"], 3, "thm.tech-history",
  T(1300, ya_from_year(1500), "唐代〜15世紀"), "fact", "medium", [], ["P01-S04"], 2)
N("evt.atlantic-colonialism", "event", "大西洋交易・植民地支配・奴隷貿易", "Atlantic trade, colonialism & slavery",
  "1500年頃以降、大西洋をまたぐ交易・植民地支配・奴隷貿易が拡大した。暴力性と、利益・負担の偏った分配を含めて理解する。", ["D07", "D05", "D06"], 3, "thm.world-history",
  T(ya_from_year(1500), ya_from_year(1880), "16〜19世紀"), "fact", "high", [], ["P01-S04"], 2)
N("evt.scientific-revolution", "event", "科学革命", "Scientific Revolution",
  "16〜17世紀、観察・実験・数学による自然理解の方法が発展した。", ["D07", "D08", "D01"], 3, "thm.modernity",
  T(ya_from_year(1543), ya_from_year(1700), "16〜17世紀"), "theory", "medium", [], ["P01-S05"], 2)
N("evt.enlightenment", "event", "啓蒙思想", "The Enlightenment",
  "17〜18世紀、理性・自由・統治をめぐる思想が展開した。", ["D08", "D06"], 3, "thm.modernity",
  T(ya_from_year(1680), ya_from_year(1800), "17〜18世紀"), "theory", "medium", [], ["P01-S05"], 2)
N("evt.industrial-revolution", "event", "産業革命・工業化", "Industrial Revolution",
  "18世紀後半に英国で始まり、化石燃料・工場・労働・都市化・資本のあり方を変えた。", ["D04", "D05", "D07"], 3, "thm.modernity",
  T(ya_from_year(1760), ya_from_year(1850), "18世紀後半〜19世紀"), "fact", "high", ["src.owid-tech"], ["P01-S05"], 3)
N("con.industrial-revolution-causes", "concept", "産業革命の原因（多要因）", "Causes of the Industrial Revolution",
  "蒸気機関だけでは説明できない。資源・投資・制度・市場・労働・帝国と交易など複数の要因が議論されている。", ["D05", "D07"], 4, "evt.industrial-revolution",
  None, "debate", "high", [], ["P01-S05"], 3)
N("evt.atlantic-revolutions", "event", "アメリカ独立とフランス革命", "Atlantic revolutions",
  "18世紀後半、市民権・憲法・主権・平等をめぐる革命が起き、近代国家の形成につながった。", ["D06", "D07"], 3, "thm.modernity",
  T(ya_from_year(1776), ya_from_year(1799), "18世紀後半"), "fact", "high", [], ["P01-S05"], 2)
N("evt.imperialism", "event", "鉄道・電信・世界市場と帝国主義", "Railways, telegraph & imperialism",
  "19世紀、交通・通信の発達と世界市場の拡大、帝国主義による支配が進んだ。", ["D06", "D05", "D04"], 3, "thm.modernity",
  T(ya_from_year(1830), ya_from_year(1914), "19世紀"), "fact", "high", [], ["P01-S05"], 2)
N("evt.electrification", "event", "電化", "Electrification",
  "19世紀末から20世紀にかけて電力が普及し、生産と生活を変えた。", ["D04"], 3, "thm.tech-history",
  T(ya_from_year(1880), ya_from_year(1950), "19世紀末〜20世紀"), "fact", "high", ["src.owid-tech"], ["P01-S05"], 2)
N("evt.world-wars", "event", "世界大戦・大恐慌・全体主義", "World wars & the Depression",
  "1914〜1945年、二つの世界大戦、革命、大恐慌、ファシズムが国際秩序を揺るがした。", ["D06", "D07"], 3, "thm.modernity",
  T(ya_from_year(1914), ya_from_year(1945), "1914〜1945年"), "fact", "high", [], ["P01-S06"], 2)
N("evt.cold-war", "event", "冷戦・核兵器・国際機関・脱植民地化", "Cold War & decolonization",
  "1945〜1991年、冷戦と核兵器、国際機関の形成、脱植民地化が進んだ。", ["D06"], 3, "thm.state-order",
  T(ya_from_year(1945), ya_from_year(1991), "1945〜1991年"), "fact", "high", [], ["P01-S06"], 2)
N("evt.digital-revolution", "event", "半導体・コンピューター・インターネットの普及", "Digital revolution",
  "1970〜2000年代、情報化が進み、産業の分業と世界経済が変わった。", ["D04", "D05"], 3, "thm.tech-history",
  T(ya_from_year(1970), ya_from_year(2005), "1970〜2000年代"), "fact", "high", [], ["P01-S06"], 3)
N("evt.globalization", "event", "冷戦後の秩序と経済のグローバル化", "Post-Cold War globalization",
  "1991年以降、経済のグローバル化と中国の台頭が進み、相互依存と地政学が交錯している。", ["D06", "D05"], 3, "thm.state-order",
  T(ya_from_year(1991), 0, "1991年〜"), "theory", "medium", [], ["P01-S06"], 2)

# ---------------------------------------------------------------- 計算機とAI
N("con.semiconductor", "concept", "半導体", "Semiconductors",
  "電気の流れを制御できる物質。トランジスタと集積回路を通じて計算機の物理的な基盤になる。", ["D01", "D04"], 3, "thm.matter",
  None, "fact", "high", [], ["P02-S02"], 3)
N("evt.mechanical-calculation", "event", "機械式計算と数理論理・統計の発展", "Mechanical calculation & mathematical logic",
  "17〜19世紀、機械式計算機、数理論理、統計、確率の研究が進んだ。", ["D02", "D04"], 3, "thm.ai-history",
  T(ya_from_year(1642), ya_from_year(1900), "17〜19世紀"), "fact", "medium", [], ["P02-S01"], 2)
N("evt.computation-theory", "event", "計算理論・電子計算機・情報理論", "Theory of computation & electronic computers",
  "20世紀前半、計算理論、電子計算機、情報理論、神経科学が発展した。", ["D02", "D04"], 3, "thm.ai-history",
  T(ya_from_year(1936), ya_from_year(1950), "20世紀前半"), "fact", "high", [], ["P02-S01"], 3)
N("evt.dartmouth", "event", "ダートマス会議", "Dartmouth workshop",
  "1956年、「Artificial Intelligence」の研究分野が形成された。", ["D04", "D02"], 3, "thm.ai-history",
  T(ya_from_year(1956), None, "1956年"), "fact", "high", ["src.dartmouth-ai"], ["P01-S07"], 2)
N("con.symbolic-and-statistical-ai", "concept", "記号AIと統計的機械学習", "Symbolic AI & statistical learning",
  "1960〜2000年代、記号AI・探索・知識表現と、統計・機械学習が並行して発展した。", ["D02", "D04"], 3, "thm.ai-history",
  T(ya_from_year(1960), ya_from_year(2005), "1960〜2000年代"), "fact", "medium", [], ["P02-S04"], 2)
N("evt.deep-learning", "event", "深層学習の進展", "Rise of deep learning",
  "2010年代、GPU・データ・計算資源の進歩により深層学習が大きく進展した。", ["D02", "D04"], 3, "thm.ai-history",
  T(ya_from_year(2012), ya_from_year(2019), "2010年代"), "fact", "high", ["src.hai-ai-index"], ["P02-S04"], 3)
N("con.gpu-compute", "concept", "GPUと計算資源", "GPUs & compute",
  "並列計算に強いGPUと大規模な計算資源が、深層学習の大規模化を可能にした。", ["D04", "D01"], 3, "thm.ai-history",
  None, "fact", "high", [], ["P02-S02"], 3)
N("con.big-data", "concept", "大規模データ", "Large-scale data",
  "インターネットの普及で蓄積された大量のデータが、機械学習の学習材料になった。", ["D04", "D02"], 3, "thm.ai-history",
  None, "fact", "high", [], ["P02-S03"], 3)
N("evt.transformer", "event", "Transformer論文", "Transformer (Attention Is All You Need)",
  "2017年、注意機構に基づくTransformerが提案され、大規模言語モデルの基盤になった。", ["D02", "D04"], 3, "thm.ai-history",
  T(ya_from_year(2017), None, "2017年"), "fact", "high", ["src.vaswani2017"], ["P02-S04"], 4)
N("con.llm", "concept", "大規模言語モデル（LLM）", "Large language models",
  "大量のテキストで学習し、文章の続きを予測することを基本にして、多様な言語課題をこなすモデル。", ["D02", "D04"], 3, "thm.ai-history",
  None, "fact", "high", ["src.vaswani2017"], ["P02-S04"], 4)
N("evt.chatgpt", "event", "ChatGPTの一般公開", "ChatGPT public release",
  "2022年11月、対話型の生成AIが一般に公開され、急速に普及した。", ["D04", "D05"], 3, "thm.ai-history",
  T(ya_from_year(2022), None, "2022年11月"), "fact", "high", ["src.openai-chatgpt"], ["P01-S07"], 3)
N("evt.agents-multimodal", "event", "推論・マルチモーダル・エージェントの展開", "Reasoning, multimodal & agents",
  "2024〜2026年、推論能力の向上、マルチモーダル化、ツール利用・エージェントが展開した。能力・信頼性・社会実装には分野差が大きく、用途は並存している。", ["D04"], 3, "thm.ai-history",
  T(ya_from_year(2024), 0, "2024〜2026年"), "fact", "medium", ["src.hai-ai-index"], ["P01-S07"], 3)
N("con.ai-energy-demand", "concept", "AIと電力需要", "AI & electricity demand",
  "AIの利用拡大はデータセンターの電力需要を増やし、電力供給やコストが制約になり得る。", ["D10", "D05", "D01"], 3, "thm.watch",
  T(5, -10, "2020年代〜"), "theory", "medium", ["src.iea-energy-ai"], ["P02-S02"], 2)

# ---------------------------------------------------------------- 経済・政治・哲学・芸術・未来
N("con.capitalism", "concept", "資本主義", "Capitalism",
  "私的所有・市場・資本の蓄積を軸とする経済の仕組み。定義と起源には学説の違いがある。", ["D05"], 3, "thm.economy",
  T(500, 0, "近世〜現在"), "debate", "medium", [], ["P03-S01"], 2)
N("con.ai-productivity-confounding", "concept", "AI導入と生産性の交絡", "AI adoption & productivity (confounding)",
  "「AI導入企業は生産性が高い」という相関だけでは因果効果は言えない。改革能力・資本・人材が両方に影響する交絡因子かもしれない。", ["D05", "D02"], 4, "thm.ai-economy",
  None, "theory", "high", [], ["P01-S01"], 3)
N("con.path-dependence-legacy", "concept", "基幹システムの経路依存", "Path dependence of legacy systems",
  "長年使った基幹システムは、代替技術が優れていても、教育・移行費用・連携・既存投資のために変えにくい。", ["D05", "D04"], 4, "thm.ai-economy",
  None, "theory", "medium", [], ["P01-S01"], 3)
N("con.scenarios-2035", "concept", "2035年AI社会の3シナリオ（説明用）", "Three AI scenarios for 2035",
  "A：急速な自動化、B：段階的な普及、C：普及の停滞。予測確率ではなく、条件の違いを考えるための整合的な未来像。", ["D10", "D05"], 4, "thm.futures",
  T(-9, None, "2035年"), "hypothesis", "medium", [], ["P01-S01"], 3)
N("con.first-cause", "concept", "第一原因と説明の限界", "First cause & the limits of explanation",
  "宇宙に始まりがあるなら、その原因は何か、という哲学・宗教哲学の問い。因果が時間を前提にするなら、問い自体の意味が問われる。", ["D08"], 3, "thm.epistemology",
  None, "debate", "medium", ["src.sep-cosmology"], ["P01-S01"], 2)
N("con.science-religion", "concept", "科学・哲学・宗教の問いの区別", "Science, philosophy & religion",
  "科学の未解明部分は、神の存在や不在を証明するものではない。それぞれの問いの種類と方法を区別する。", ["D08", "D07"], 3, "thm.epistemology",
  None, "normative", "medium", ["src.sep-cosmology"], ["P01-S01"], 2)
N("con.disciplinary-evidence", "concept", "学問ごとの証拠と方法の違い", "Evidence across disciplines",
  "形式科学・自然科学・歴史学・社会科学・哲学・芸術研究では、証拠と検証の方法が異なる。", ["D08"], 3, "thm.epistemology",
  None, "theory", "high", [], ["P01-S08"], 3)

# ---------------------------------------------------------------- 思考法（時間を持たない）
M = [
 ("mth.causal-inference", "因果推論", "Causal inference", "XとYが一緒に起きることと、XがYを引き起こすことを区別し、交絡因子・反事実を検討して因果を推定する方法。", ["D02", "D05"], "thm.probability"),
 ("mth.bayesian-updating", "ベイズ的更新", "Bayesian updating", "新しい証拠を得たとき、事前の確信を、仮説が正しい場合と誤りの場合に証拠が出る確率の比で更新する考え方。", ["D02"], "thm.probability"),
 ("mth.base-rate", "基準率の利用", "Base rates", "個別の情報を見る前に、その事象が対象集団でどれほど普通かを確認する。基準率を無視すると判断を大きく誤る。", ["D02"], "thm.probability"),
 ("mth.feedback", "システムのフィードバック", "Feedback loops", "結果が原因に戻る循環。変化を増幅する強化ループと、抑える均衡ループがある。時間遅れと境界の取り方に注意する。", ["D10"], "thm.systems"),
 ("mth.path-dependence", "経路依存性", "Path dependence", "過去の選択・偶然・自己強化・切替コストが現在の選択肢を制約すること。維持の仕組みを特定して初めて説明になる。", ["D05", "D07"], "thm.systems"),
 ("mth.counterfactual", "反実仮想", "Counterfactual reasoning", "もし要因Xがなかったら結果Yはどうなったかを、変える条件と固定する条件を明示して考える。", ["D08", "D07"], "thm.epistemology"),
 ("mth.scenario-analysis", "シナリオ分析", "Scenario analysis", "主要な不確実性を変えた、複数の整合的な未来を描く。予言ではない。", ["D10"], "thm.futures"),
 ("mth.forecast-calibration", "予測の校正", "Forecast calibration", "70%と予測した事象が実際に約70%起きているかを検証する。校正に加えて識別力・鋭さも見る。", ["D10", "D02"], "thm.futures"),
 ("mth.seven-steps", "8思考法を統合した7ステップ", "Seven-step analysis", "定義→基準率→因果・反実仮想→フィードバック・制約・経路依存→シナリオ→予測の記録→更新と校正。", ["D10"], "thm.systems"),
 ("mth.nine-questions", "9つの共通質問", "Nine common questions", "何か／いつ・どこか／なぜか／どう機能するか／誰に関係するか／何につながるか／どう知るか／何が分からないか／今後どうなり得るか。", ["D08"], "thm.epistemology"),
 ("mth.twelve-axes", "世界を動かす12の分析軸", "Twelve analytical axes", "物質・資源、エネルギー、自然環境、人口、技術・知識、生産・経済、政治・権力、法・制度、文化・思想、社会関係、情報・メディア、偶然・危機・選択。法則ではなくチェックリスト。", ["D10"], "thm.systems"),
 ("mth.epistemic-categories", "認識の6分類", "Six epistemic categories", "観測された事実／強い証拠のある理論／解釈・論争／規範的判断／予測・仮説／未知・未解明を区別する。", ["D08"], "thm.epistemology"),
 ("mth.five-maps", "5種類の地図", "Five maps", "時間・空間・学問・構造と因果・認識と限界の5つの地図を、あらゆるテーマに重ねる。", ["D08", "D10"], "thm.epistemology"),
]
for mid, ja, en, summ, doms, par in M:
    N(mid, "method", ja, en, summ, doms, 3, par, None, "theory", "medium", [], ["P01-S01"], 4)

# ---------------------------------------------------------------- 問い
Q = [
 ("q.origin-of-time", "時間そのものに起源はあるか", "Did time have a beginning?", "時間に過去の端があるのか、それとも「ビッグバン以前」に意味があるのか。宇宙モデルと時間観に依存し、未解明。", ["D01", "D08"], "thm.time", "unknown", "P01-S01"),
 ("q.low-entropy-past", "なぜ初期宇宙は低エントロピーだったのか", "Why was the early universe low-entropy?", "時間の矢の究極の起源に関わる未解明の問い（過去仮説）。", ["D01", "D08"], "thm.time", "unknown", "P01-S01"),
 ("q.nature-dark-matter-energy", "ダークマターとダークエネルギーの正体は何か", "What are dark matter and dark energy?", "重力的な効果や加速膨張から推定されるが、根本的な正体は未解明。", ["D01"], "thy.lcdm", "unknown", "P01-S01"),
 ("q.origin-of-life", "生命はどのように誕生したのか", "How did life originate?", "生命の起源の時期と機構は未解明。進化の仕組みとは別の問題。", ["D03"], "thm.life", "unknown", "P01-S02"),
 ("q.why-genai-2020s", "なぜ生成AIは2020年代に急速に発展・普及したのか", "Why did generative AI take off in the 2020s?", "第一の本格探究テーマ。技術的・経済的・社会的な条件と、今後の制約を問う。", ["D04", "D05", "D02"], "thm.ai-history", "debate", "P01-S07"),
 ("q.computation-physics", "半導体はなぜ計算でき、計算にはなぜ電力が必要か", "Why can semiconductors compute, and why does computing need energy?", "宇宙・物理学から生成AIへの接続の問い。", ["D01", "D04"], "thm.matter", "theory", "P02-S02"),
 ("q.math-of-learning", "AIの学習・推論は数学的にどう成り立つか", "How do AI learning and inference work mathematically?", "数学・情報科学から生成AIへの接続の問い。", ["D02"], "thm.probability", "theory", "P02-S03"),
 ("q.human-vs-ai-intelligence", "人間の知能とAIの知能の共通点と相違点は何か", "How do human and machine intelligence compare?", "生命・脳科学から生成AIへの接続の問い。", ["D03", "D08"], "thm.mind", "debate", "P01-S07"),
 ("q.ai-vs-past-revolutions", "AI革命は過去の技術革新と何が似て、何が異なるか", "How does AI compare with past technological revolutions?", "技術・産業史から生成AIへの接続の問い。", ["D04", "D07"], "thm.tech-history", "debate", "P03-S01"),
 ("q.ai-economy-effects", "AIで生産性・雇用・賃金・企業利益はどうなるか", "How will AI affect productivity, jobs, wages and profits?", "経済・経営学から生成AIへの接続の問い。", ["D05"], "thm.ai-economy", "debate", "P03-S01"),
 ("q.ai-control", "AIを誰が開発・支配・規制するのか", "Who develops, controls and regulates AI?", "政治・法・国際関係から生成AIへの接続の問い。", ["D06"], "thm.ai-governance", "debate", "P03-S02"),
 ("q.knowledge-transmission", "知識・技術・制度はどう蓄積・伝播したか", "How have knowledge, technology and institutions accumulated and spread?", "歴史・文明・宗教から生成AIへの接続の問い。", ["D07"], "thm.world-history", "theory", "P01-S04"),
 ("q.what-is-intelligence", "知能・意識・人間・自由・責任とは何か", "What are intelligence, consciousness and responsibility?", "哲学・倫理・思想から生成AIへの接続の問い。", ["D08"], "thm.ethics", "normative", "P03-S03"),
 ("q.creativity-authenticity", "AIが生成できる時代に、創造や真正性の意味は何か", "What do creativity and authenticity mean in the age of generative AI?", "文化・文学・芸術から生成AIへの接続の問い。", ["D09"], "thm.arts", "normative", "P03-S04"),
 ("q.ai-society", "AI社会はどのような仕組み・格差・機会を生むか", "What structures, inequalities and opportunities will an AI society create?", "社会・未来研究から生成AIへの接続の問い。", ["D10"], "thm.futures", "hypothesis", "P04-S01"),
]
for qid, ja, en, summ, doms, par, ep, cur in Q:
    N(qid, "question", ja, en, summ, doms, 3, par, None, ep, "high", [], [cur], 3)

# ---------------------------------------------------------------- エッジ
seq = ["evt.hot-dense-early", "evt.bbn", "evt.recombination", "evt.first-galaxies", "evt.element-synthesis",
       "evt.solar-system", "evt.earth-formation", "evt.earliest-life", "evt.goe", "evt.cambrian", "evt.kpg",
       "evt.hominin-split", "evt.homo-sapiens", "evt.agriculture", "evt.early-states", "evt.writing"]
for a, b in zip(seq, seq[1:]):
    E(a, b, "precedes", "fact")
seq2 = ["evt.scientific-revolution", "evt.enlightenment", "evt.industrial-revolution", "evt.imperialism",
        "evt.world-wars", "evt.cold-war", "evt.globalization"]
for a, b in zip(seq2, seq2[1:]):
    E(a, b, "precedes", "fact")
seq3 = ["evt.mechanical-calculation", "evt.computation-theory", "evt.dartmouth", "evt.deep-learning",
        "evt.transformer", "evt.chatgpt", "evt.agents-multimodal"]
for a, b in zip(seq3, seq3[1:]):
    E(a, b, "precedes", "fact")

E("evd.redshift", "con.cosmic-expansion", "evidence_for", "fact", "距離と赤方偏移の関係", ["src.hubble1929"])
E("evd.cmb", "thy.hot-big-bang", "evidence_for", "fact", "高温の初期宇宙の名残", ["src.penzias-wilson-1965"])
E("evd.bbn-abundances", "thy.hot-big-bang", "evidence_for", "fact", "初期数分の元素合成の予測との一致", ["src.pdg-bbn"])
E("con.cosmic-expansion", "thy.hot-big-bang", "supports", "theory")
E("evt.recombination", "evd.cmb", "causes", "theory", "再結合で光が自由に進めるようになり、その光が現在CMBとして観測される")
E("evt.bbn", "evd.bbn-abundances", "causes", "theory")
E("thy.general-relativity", "thy.lcdm", "requires", "theory", "ΛCDMは一般相対論を前提とする宇宙モデル")
E("thy.general-relativity", "con.singularity", "raises", "theory", "古典的な一般相対論を過去へ外挿すると現れる")
E("con.singularity", "q.origin-of-time", "raises", "hypothesis")
E("thy.big-bounce", "q.origin-of-time", "addresses", "hypothesis", "始まりの前に別の状態があった可能性")
E("thy.emergent-time", "q.origin-of-time", "addresses", "hypothesis", "時間そのものが根本的でない可能性")
E("con.planck-time", "con.singularity", "supports", "theory", "この尺度より前では量子重力が必要と考えられ、古典論の外挿は信頼できない")
E("thy.special-relativity", "con.newtonian-time", "contradicts", "fact", "絶対時間を否定。ただし日常的な条件では近似として有効")
E("thy.special-relativity", "con.spacetime", "enables", "theory")
E("evd.clock-tests", "con.time-dilation", "evidence_for", "fact", "", ["src.chou2010"])
E("con.time-dilation", "thy.general-relativity", "instance_of", "theory")
E("con.entropy", "thy.second-law", "part_of", "theory")
E("thy.second-law", "con.arrow-of-time", "supports", "theory", "時間の矢の主要な説明枠組み")
E("con.arrow-of-time", "q.low-entropy-past", "raises", "unknown")
E("q.origin-of-time", "con.arrow-of-time", "analogous", "theory", "混同しやすいが別の問題（起源と向き）")
E("thy.lcdm", "con.dark-matter", "requires", "theory")
E("thy.lcdm", "con.dark-energy", "requires", "theory")
E("con.hubble-tension", "thy.lcdm", "contradicts", "debate", "測定の系統誤差か、新しい物理か", ["src.h0dn-2026"])
E("con.evolving-dark-energy", "thy.lcdm", "contradicts", "debate", "宇宙定数（一定）との緊張。5σ未満", ["src.desi-dr2-2025"])
E("con.lithium-problem", "thy.hot-big-bang", "contradicts", "unknown", "理論全体の反証ではなく、未解決の食い違い")
E("con.dark-matter", "q.nature-dark-matter-energy", "raises", "unknown")
E("con.dark-energy", "q.nature-dark-matter-energy", "raises", "unknown")
E("thy.inflation", "evt.inflation-epoch", "supports", "debate")
E("evd.cmb", "con.age-of-universe", "evidence_for", "theory", "ΛCDMを仮定した推定", ["src.planck2018-vi"])
E("evd.cmb", "con.cosmic-composition", "evidence_for", "theory", "", ["src.planck2018-vi"])
E("evd.radiometric-dating", "evt.earth-formation", "evidence_for", "fact")
E("evt.element-synthesis", "evt.earliest-life", "enables", "theory", "炭素・酸素などの元素が生命の材料になった")
E("evt.earliest-life", "evt.goe", "causes", "theory", "光合成をする生物が酸素を増やした")
E("con.natural-selection", "evt.cambrian", "enables", "theory")
E("q.origin-of-life", "evt.earliest-life", "raises", "unknown")
E("con.cumulative-culture", "evt.agriculture", "enables", "debate")
E("evt.agriculture", "evt.early-states", "enables", "debate", "必然ではない。地域によって経路が異なる")
E("evt.writing", "q.knowledge-transmission", "addresses", "theory")
E("con.trade-networks", "q.knowledge-transmission", "addresses", "theory")
E("evt.printing", "evt.scientific-revolution", "enables", "debate")
E("evt.scientific-revolution", "evt.industrial-revolution", "enables", "debate")
E("con.industrial-revolution-causes", "evt.industrial-revolution", "addresses", "debate")
E("evt.atlantic-colonialism", "evt.industrial-revolution", "enables", "debate", "帝国と交易が資源・市場・資本の面で関わったという議論")
E("evt.industrial-revolution", "evt.electrification", "precedes", "fact")
E("evt.electrification", "evt.computation-theory", "enables", "theory")
E("con.semiconductor", "evt.digital-revolution", "enables", "fact")
E("con.semiconductor", "con.gpu-compute", "enables", "fact")
E("evt.digital-revolution", "con.big-data", "enables", "theory")
E("con.gpu-compute", "evt.deep-learning", "enables", "theory")
E("con.big-data", "evt.deep-learning", "enables", "theory")
E("evt.transformer", "con.llm", "enables", "fact", "", ["src.vaswani2017"])
E("con.llm", "evt.chatgpt", "enables", "fact")
E("con.gpu-compute", "q.why-genai-2020s", "addresses", "theory")
E("con.big-data", "q.why-genai-2020s", "addresses", "theory")
E("evt.transformer", "q.why-genai-2020s", "addresses", "theory")
E("con.symbolic-and-statistical-ai", "evt.deep-learning", "precedes", "fact")
E("con.llm", "con.ai-energy-demand", "causes", "theory", "", ["src.iea-energy-ai"])
E("q.computation-physics", "con.semiconductor", "raises", "theory")
E("con.first-cause", "q.origin-of-time", "analogous", "debate", "物理学の問いと哲学の問いの接点")
E("con.science-religion", "con.first-cause", "supports", "normative")
E("mth.causal-inference", "con.ai-productivity-confounding", "applies", "theory")
E("mth.base-rate", "mth.bayesian-updating", "part_of", "theory", "基準率は事前確率にあたる")
E("mth.feedback", "con.ai-energy-demand", "applies", "theory", "利用増→電力需要増→制約、の均衡ループの例")
E("mth.path-dependence", "con.path-dependence-legacy", "applies", "theory")
E("mth.counterfactual", "evt.transformer", "applies", "hypothesis", "Transformerがなかったら、という思考実験")
E("mth.scenario-analysis", "con.scenarios-2035", "applies", "hypothesis")
E("mth.forecast-calibration", "mth.bayesian-updating", "analogous", "theory")
E("mth.epistemic-categories", "con.disciplinary-evidence", "supports", "theory")
E("mth.twelve-axes", "con.industrial-revolution-causes", "applies", "theory")
E("con.periodization", "thm.world-history", "supports", "debate")

# ---------------------------------------------------------------- 書き出し
DOMAINS = [
 ("D01", "宇宙・物理学", "Universe & Physics", "半導体はなぜ計算できるか。計算になぜ電力が必要か"),
 ("D02", "数学・情報科学", "Mathematics & Information", "AIの学習・推論は数学的にどう成立するか"),
 ("D03", "生命・脳科学", "Life & Brain Sciences", "人間の知能とAIの知能の共通点・相違点は何か"),
 ("D04", "技術・産業史", "Technology & Industry", "AI革命は過去の技術革新と何が似て異なるか"),
 ("D05", "経済・経営学", "Economics & Management", "AIで生産性・雇用・賃金・企業利益はどうなるか"),
 ("D06", "政治・法・国際関係", "Politics, Law & International Relations", "AIを誰が開発・支配・規制するか"),
 ("D07", "歴史・文明・宗教", "History, Civilization & Religion", "知識・技術・制度はどう蓄積・伝播したか"),
 ("D08", "哲学・倫理・思想", "Philosophy, Ethics & Thought", "知能、意識、人間、自由、幸福、責任とは何か"),
 ("D09", "文化・文学・芸術", "Culture, Literature & Arts", "AIが生成できる時代に創造・真正性の意味は何か"),
 ("D10", "社会・未来研究", "Society & Futures", "AI社会はどのような仕組み・格差・機会を生むか"),
]
domains = [{"id": d, "ja": ja, "en": en, "order": i, "ai_question": q} for i, (d, ja, en, q) in enumerate(DOMAINS)]

# 出典が空のノードは unverified のまま。出典のあるノードも、独立検証（Verifier）を通るまでは pending。
for n in nodes:
    n["verification"]["status"] = "pending" if n["sources"] else "unverified"

nodes.sort(key=lambda n: n["id"])
sources.sort(key=lambda s: s["id"])

S01 = [n["id"] for n in nodes if "P01-S01" in n.get("curriculum", [])]
understanding = {"scale": "L0未学習 L1認知 L2説明 L3専門理解 L4統合応用 L5批判的検証",
                 "nodes": {nid: {"level": 0, "status": "presented", "history": [], "next_review": None, "recheck": False,
                                 "note": "ChatGPT上で講義提示済み（2026-11-23）・理解度は未評価"} for nid in S01}}

questions = []
qmap = [("q.origin-of-time", "handoff", "exploring"), ("q.low-entropy-past", "open-problem", "open-problem"),
        ("q.nature-dark-matter-energy", "open-problem", "open-problem"), ("q.origin-of-life", "open-problem", "open-problem"),
        ("q.why-genai-2020s", "handoff", "open")] + [(q[0], "handoff", "open") for q in Q[5:]]
for i, (qid, origin, status) in enumerate(qmap, 1):
    node = next(n for n in nodes if n["id"] == qid)
    questions.append({"id": f"qq.{i:04d}", "text": node["title"]["ja"], "origin": origin, "status": status,
                      "nodes": [qid], "created": TODAY})
questions.append({"id": f"qq.{len(questions)+1:04d}", "text": "（第1回・問1）「宇宙が約138億年前に始まった」という説明から、最も正確に言えることはどれか",
                  "origin": "handoff", "status": "open", "nodes": ["thy.hot-big-bang", "q.origin-of-time"], "created": TODAY,
                  "notes": "ChatGPT上で提示・未回答・未採点。選択肢Bは画面の初期値であり、ユーザーの回答ではない。"})

P01 = [("P01-S01", "宇宙・物質・地球の形成、時間の起源", "宇宙の時間尺度、ビッグバンの意味、観測証拠と未解明を説明できる", "presented"),
       ("P01-S02", "生命の起源と進化", "生命起源と進化の違い、自然選択・絶滅・生態系を説明できる", "not-started"),
       ("P01-S03", "人類・文化・農耕・文明", "累積的学習、農耕、都市、国家、文字を説明できる", "not-started"),
       ("P01-S04", "世界史・宗教・思想・文化", "多地域比較、文明間交流、歴史的多様性を説明できる", "not-started"),
       ("P01-S05", "近代化と産業革命", "科学革命・工業化・国家・資本主義・帝国主義を説明できる", "not-started"),
       ("P01-S06", "20世紀と現代", "世界大戦・冷戦・国際制度・デジタル社会を説明できる", "not-started"),
       ("P01-S07", "学問体系と生成AIの位置", "生成AIの成立要因を5つの地図に配置できる（成果物：生成AIの成立条件マップ）", "not-started"),
       ("P01-S08", "総合演習・理解度検証", "全体史・学問・因果・不確実性を自力で説明できる", "not-started")]
P02 = [("P02-S01", "計算機の原理", "計算とは何か、計算機がどう動くかを説明できる"),
       ("P02-S02", "半導体・GPU・電力", "計算の物理的基盤とエネルギーの制約を説明できる"),
       ("P02-S03", "確率・統計・学習", "データから学ぶことの数学的な意味を説明できる"),
       ("P02-S04", "機械学習・深層学習・Transformer・LLM", "LLMの仕組みと限界を説明できる"),
       ("P02-S05", "研究開発・投資・データ・社会需要・制度の統合", "生成AIが2020年代に普及した条件を因果的に説明できる")]
P03 = [("P03-S01", "産業革命と雇用、AIと経済", ""), ("P03-S02", "国家競争・安全保障・AIガバナンス", ""),
       ("P03-S03", "倫理・意識・人間観", ""), ("P03-S04", "芸術・真正性・文化", "")]
P04 = [("P04-S01", "現実の問題への応用と予測", "根拠つきの分析、予測の記録、理解度の検証")]
def sess(lst, default="not-started"):
    out = []
    for t in lst:
        sid, title, goal = t[0], t[1], t[2]
        status = t[3] if len(t) > 3 else default
        out.append({"id": sid, "title": title, "goal": goal, "status": status,
                    "nodes": [n["id"] for n in nodes if sid in n.get("curriculum", [])], "lessons": []})
    return out
curriculum = [
 {"id": "P01", "title": "世界の全体地図", "goal": "宇宙から現代までを俯瞰する知識の座標軸をつくる", "sessions": sess(P01)},
 {"id": "P02", "title": "生成AIの成立条件と技術の深掘り", "goal": "計算機・半導体・機械学習・LLMを因果的に説明する", "sessions": sess(P02)},
 {"id": "P03", "title": "歴史・経済・政治・国際・哲学・宗教・文化への展開", "goal": "学際的な分析・比較、異論の理解", "sessions": sess(P03)},
 {"id": "P04", "title": "現実の問題への応用と未来予測", "goal": "根拠付きの分析、予測記録、理解度検証", "sessions": sess(P04)},
]
state = {"cycle": 0, "map_version": "1.0", "system_version": "0.1.0", "last_run": None, "current_session": "P01-S01",
         "next_cycle_plan": "サイクル1：P01-S01（宇宙・時間の起源）の教材L0001と初回レポートR0001を作成",
         "schedule": "未設定（確認③で決定）", "pending": [], "awaiting_user": ["確認②：試作の見た目・使い心地", "GitHub Pagesの有効化"],
         "phase_gate": "P2（試作）"}

w = lambda p, o: (DATA / p).write_text(json.dumps(o, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
w("graph/domains.json", domains)
w("graph/nodes.json", nodes)
w("graph/edges.json", edges)
w("sources.json", sources)
w("understanding.json", understanding)
w("questions.json", questions)
w("forecasts.json", [])
w("curriculum.json", curriculum)
w("state.json", state)
print(f"nodes={len(nodes)} edges={len(edges)} sources={len(sources)} questions={len(questions)} S01={len(S01)}")
