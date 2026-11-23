"""PDF用の図（DOC-03 §4.3、§7）。細い線画＋朱赤のアクセント。すべてSVG文字列を返す。"""
import math
import random
from html import escape
from common import x_of_ya

INK, MUTED, HAIR, RED, CREAM = "#141414", "#7a7a7a", "#cfcac0", "#c8402a", "#e9dcc0"
GOTHIC = "Zen Kaku Gothic New, Noto Sans CJK JP, sans-serif"
MONO = "IBM Plex Mono, Noto Sans Mono CJK JP, monospace"
LEVEL_COLORS = ["#bdbdbd", "#e9dcc0", "#e6be96", "#e0966d", "#d46a45", "#c8402a"]
TICKS = [(13.8e9, "13.8 Gyr"), (1e9, "1 Gyr"), (1e8, "100 Myr"), (1e7, "10 Myr"), (1e6, "1 Myr"),
         (1e5, "100 kyr"), (1e4, "10 kyr"), (1e3, "1 kyr"), (1e2, "100 yr"), (0, "NOW")]
TICKS_JA = {13.8e9: "138億年前", 1e9: "10億年前", 1e8: "1億年前", 1e7: "1000万年前", 1e6: "100万年前",
            1e5: "10万年前", 1e4: "1万年前", 1e3: "1000年前", 1e2: "100年前", 0: "現在"}


def _svg(w, h, body, bg=None):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{GOTHIC}">{rect}{body}</svg>'


def _t(x, y, s, size=7, fill=INK, anchor="start", font=None, weight="normal", ls=0):
    f = f' font-family="{font}"' if font else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{f} '
            f'font-weight="{weight}" letter-spacing="{ls}">{escape(str(s))}</text>')


class _X:
    def __init__(self, w0, w1, tx=0, tdx=0):
        self.lo, self.hi = x_of_ya(13.8e9), x_of_ya(-30)
        self.w0, self.w1, self.timeless_x, self.timeless_dx = w0, w1, tx, tdx

    def __call__(self, x):
        return self.w0 + (x - self.lo) / (self.hi - self.lo) * (self.w1 - self.w0)


def _node_x(n):
    t = n["time"]
    x = x_of_ya(t["start_ya"])
    if t.get("end_ya") is not None:
        x = (x + x_of_ya(t["end_ya"])) / 2
    return x


def _layout(data, X, y0, y1):
    """ノードの2次元配置：横＝対数時間、縦＝領域（時間なしは右端の帯）。"""
    doms = sorted(data["domains"], key=lambda d: d["order"])
    idx = {d["id"]: i for i, d in enumerate(doms)}
    rowh = (y1 - y0) / len(doms)
    pos, tl = {}, {}
    for n in sorted(data["nodes"], key=lambda n: n["id"]):
        i = idx[n["domains"][0]]
        h = (sum(n["id"].encode()) * 7919 % 997) / 997
        if n["time"] is None:
            k = tl.get(i, 0)
            tl[i] = k + 1
            x = X.timeless_x + (k % 7) * X.timeless_dx
            y = y0 + rowh * (i + 0.25 + 0.3 * (k // 7))
        else:
            x = X(_node_x(n))
            y = y0 + rowh * (i + 0.2 + 0.6 * h)
        pos[n["id"]] = (x, y)
    return doms, rowh, pos


def _curve(pos, a, b):
    (x1, y1), (x2, y2) = pos[a], pos[b]
    mx = (x1 + x2) / 2
    return f"M{x1:.2f},{y1:.2f} C{mx:.2f},{y1:.2f} {mx:.2f},{y2:.2f} {x2:.2f},{y2:.2f}"


# ---------------------------------------------------------------- 表紙の線画（黒地）
def cover_art(data, highlight):
    W, H = 210, 297
    X = _X(22, 166, 176, 2.0)
    doms, rowh, pos = _layout(data, X, 40, 160)
    hl = set(highlight)
    out = []
    for ya, lab in TICKS:
        x = X(x_of_ya(ya))
        out.append(f'<line x1="{x:.2f}" x2="{x:.2f}" y1="36" y2="164" stroke="#262626" stroke-width="0.15"/>')
        out.append(_t(x, 169, lab, 2.1, "#6b6760", "middle", MONO, ls=0.2))
    out.append(f'<line x1="172" x2="172" y1="36" y2="164" stroke="#262626" stroke-width="0.15" stroke-dasharray="0.6 0.8"/>')
    out.append(_t(183, 169, "TIMELESS", 2.1, "#6b6760", "middle", MONO, ls=0.2))
    for i, d in enumerate(doms):
        out.append(_t(20, 40 + rowh * i + 2.4, d["id"], 1.9, "#55524c", "end", MONO, ls=0.2))
    for n in data["nodes"]:
        if n.get("parent") in pos:
            out.append(f'<path d="{_curve(pos, n["parent"], n["id"])}" fill="none" stroke="#f2efe8" stroke-opacity="0.16" stroke-width="0.12"/>')
    for e in data["edges"]:
        if e["from"] in pos and e["to"] in pos:
            hot = e["from"] in hl and e["to"] in hl
            out.append(f'<path d="{_curve(pos, e["from"], e["to"])}" fill="none" stroke="{RED if hot else "#f2efe8"}" '
                       f'stroke-opacity="{0.8 if hot else 0.26}" stroke-width="{0.24 if hot else 0.14}"/>')
    for nid, (x, y) in pos.items():
        if nid in hl:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.85" fill="{RED}"/>')
        else:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.45" fill="#f2efe8" fill-opacity="0.75"/>')
    return _svg(W, H, "".join(out))


# ---------------------------------------------------------------- 本文用の小さな地図
def minimap(data, highlight):
    W, H = 170, 76
    X = _X(26, 140, 147, 2.6)
    doms, rowh, pos = _layout(data, X, 4, 62)
    hl = set(highlight)
    out = []
    for i, d in enumerate(doms):
        y = 4 + rowh * i
        out.append(f'<line x1="26" x2="166" y1="{y:.2f}" y2="{y:.2f}" stroke="{HAIR}" stroke-width="0.12"/>')
        out.append(_t(24, y + rowh * 0.65, d["ja"], 2.3, MUTED, "end"))
    for ya, lab in TICKS:
        x = X(x_of_ya(ya))
        out.append(f'<line x1="{x:.2f}" x2="{x:.2f}" y1="4" y2="63" stroke="{HAIR}" stroke-width="0.12"/>')
        out.append(_t(x, 67, TICKS_JA[ya], 2.1, MUTED, "middle"))
    out.append(_t(156, 67, "時間なし", 2.1, MUTED, "middle"))
    for e in data["edges"]:
        a, b = e["from"], e["to"]
        if a in pos and b in pos:
            hot = a in hl and b in hl
            out.append(f'<path d="{_curve(pos, a, b)}" fill="none" stroke="{RED if hot else INK}" '
                       f'stroke-opacity="{0.5 if hot else 0.08}" stroke-width="{0.2 if hot else 0.12}"/>')
    for nid, (x, y) in pos.items():
        if nid in hl:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.9" fill="{RED}"/>')
        else:
            out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.5" fill="#fff" stroke="{MUTED}" stroke-width="0.15"/>')
    out.append(_t(26, 73, "← 過去（対数：1目盛りで10倍）", 2.1, MUTED))
    out.append(_t(140, 73, "現在 →", 2.1, MUTED, "end"))
    return _svg(W, H, "".join(out))


# ---------------------------------------------------------------- 宇宙の年表
TIMELINE = ["evt.hot-dense-early", "evt.bbn", "evt.recombination", "evt.first-galaxies", "evt.solar-system",
            "evt.earth-formation", "evt.earliest-life", "evt.goe", "evt.cambrian", "evt.kpg", "evt.hominin-split",
            "evt.homo-sapiens", "evt.agriculture", "evt.writing", "evt.industrial-revolution", "evt.chatgpt"]


def cosmic_timeline(data, highlight):
    W, H = 170, 92
    L, R, Y = 6, 164, 46
    X = _X(L, R)
    by = {n["id"]: n for n in data["nodes"]}
    hl = set(highlight)
    evs = sorted([by[i] for i in TIMELINE if i in by and by[i]["time"]], key=lambda n: -n["time"]["start_ya"])
    out = [f'<line x1="{L}" x2="{R}" y1="{Y}" y2="{Y}" stroke="{INK}" stroke-width="0.35"/>']
    for ya, lab in TICKS:
        x = X(x_of_ya(ya))
        out.append(f'<line x1="{x:.2f}" x2="{x:.2f}" y1="{Y-1}" y2="{Y+1}" stroke="{INK}" stroke-width="0.25"/>')
        out.append(_t(x, Y + 3.6, lab, 1.9, MUTED, "middle", MONO, ls=0.1))
    n = len(evs)
    slot = (R - L) / n
    for k, ev in enumerate(evs):
        x = X(x_of_ya(ev["time"]["start_ya"]))
        sx = L + slot * (k + 0.5)
        up = k % 2 == 0
        row = (k // 2) % 2
        ty = (Y - 10 - row * 15) if up else (Y + 13 + row * 15)
        col = RED if ev["id"] in hl else INK
        ly = ty + 3 if up else ty - 3.2
        out.append(f'<polyline points="{x:.2f},{Y} {x:.2f},{Y + (-3 if up else 3)} {sx:.2f},{ly:.2f}" fill="none" stroke="{col}" stroke-width="0.14" stroke-opacity="0.7"/>')
        out.append(f'<circle cx="{x:.2f}" cy="{Y}" r="0.75" fill="#fff" stroke="{col}" stroke-width="0.3"/>')
        title = ev["title"]["ja"]
        lines = [title[:10], title[10:20]] if len(title) > 10 else [title]
        for j, t in enumerate(lines):
            yy = ty - (len(lines) - 1 - j) * 2.6 if up else ty + j * 2.6
            out.append(_t(sx, yy, t, 2.2, col, "middle", weight="bold"))
        lab_y = (ty + 2.6) if up else (ty + len(lines) * 2.6)
        out.append(_t(sx, lab_y, ev["time"]["label"][:13], 1.9, MUTED, "middle"))
    return _svg(W, H, "".join(out))


# ---------------------------------------------------------------- 説明図
_ARROW = (f'<defs><marker id="ar" markerWidth="4" markerHeight="4" refX="3" refY="2" orient="auto">'
          f'<path d="M0,0 L4,2 L0,4" fill="none" stroke="{INK}" stroke-width="0.5"/></marker></defs>')


def expansion(data=None, highlight=None):
    W, H = 170, 62
    out = [_ARROW]

    def grid(ox, oy, s, label):
        g = []
        for i in range(6):
            g.append(f'<line x1="{ox}" x2="{ox + s*5}" y1="{oy + s*i}" y2="{oy + s*i}" stroke="{HAIR}" stroke-width="0.2"/>')
            g.append(f'<line x1="{ox + s*i}" x2="{ox + s*i}" y1="{oy}" y2="{oy + s*5}" stroke="{HAIR}" stroke-width="0.2"/>')
        pts = [(1, 1), (3, 2), (2, 4), (4, 4)]
        for (a, b) in pts[1:]:
            g.append(f'<line x1="{ox + s*1}" y1="{oy + s*1}" x2="{ox + s*a}" y2="{oy + s*b}" stroke="{RED}" stroke-width="0.2" stroke-dasharray="0.8 0.6"/>')
        for k, (a, b) in enumerate(pts):
            g.append(f'<circle cx="{ox + s*a}" cy="{oy + s*b}" r="1.1" fill="{RED if k == 0 else INK}"/>')
        g.append(_t(ox, oy - 2.5, label, 2.4, INK, font=MONO, ls=0.4))
        return "".join(g)
    out.append(grid(8, 10, 8, "EARLIER"))
    out.append(grid(80, 4, 10.4, "LATER"))
    out.append(f'<path d="M58,30 L74,30" stroke="{INK}" stroke-width="0.3" marker-end="url(#ar)"/>')
    out.append(_t(66, 27, "時間", 2.3, MUTED, "middle"))
    out.append(_t(8, 60, "格子（空間の尺度）そのものが大きくなる。赤い点から見ると、遠くの点ほど大きく遠ざかる。どの点を基準にしても同じで、中心はない。", 2.2, MUTED))
    return _svg(W, H, "".join(out))


def clocks(data=None, highlight=None):
    W, H = 170, 64
    out = [f'<line x1="8" x2="70" y1="52" y2="52" stroke="{INK}" stroke-width="0.4"/>',
           _t(8, 57, "GROUND", 2.1, MUTED, font=MONO, ls=0.3)]
    for (cx, cy, lab, fast) in [(26, 44, "低い位置", False), (52, 30, "約33cm高い位置", True)]:
        c = RED if fast else INK
        out.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="none" stroke="{c}" stroke-width="0.35"/>')
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-4.2}" stroke="{c}" stroke-width="0.35"/>')
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + (3.2 if fast else 2.6)}" y2="{cy + (1.5 if fast else 2.2)}" stroke="{c}" stroke-width="0.35"/>')
        out.append(_t(cx, cy + 9.5, lab, 2.2, INK, "middle"))
    out.append(_t(39, 10, "高い方がわずかに速く進む", 2.5, RED, "middle", weight="bold"))
    out.append(_t(39, 14, "（重力が弱いほど時計は速く進む）", 2.1, MUTED, "middle"))
    out.append(f'<circle cx="128" cy="44" r="10" fill="none" stroke="{INK}" stroke-width="0.35"/>')
    out.append(_t(128, 45, "地球", 2.3, INK, "middle"))
    out.append(f'<circle cx="128" cy="44" r="27" fill="none" stroke="{HAIR}" stroke-width="0.2" stroke-dasharray="1 1"/>')
    out.append(f'<rect x="146" y="22" width="5" height="3" fill="none" stroke="{RED}" stroke-width="0.35"/>')
    out.append(_t(149, 19.5, "GPS衛星", 2.2, RED, "middle"))
    out.append(_t(92, 6, "重力が弱い → 速く進む（＋）", 2.2, INK))
    out.append(_t(92, 9.6, "高速で動く → 遅く進む（−）", 2.2, INK))
    out.append(_t(92, 13.2, "差し引き 1日約38マイクロ秒 速い → 補正", 2.2, RED, weight="bold"))
    return _svg(W, H, "".join(out))


def time_origin(data=None, highlight=None):
    W, H = 170, 66
    out = []
    cols = [(28, "BEGINNING", "時間に始まりがある", "過去に端がある（北極点のように）"),
            (85, "BOUNCE", "始まりの前がある", "収縮 → 反転 → 膨張"),
            (142, "EMERGENT", "時間は根本的でない", "より根本的な構造から現れる")]
    x = cols[0][0]
    out.append(f'<path d="M{x},50 L{x-16},14 M{x},50 L{x+16},14" fill="none" stroke="{INK}" stroke-width="0.35"/>')
    for yy in [20, 28, 36, 44]:
        w = (50 - yy) * 16 / 36
        out.append(f'<ellipse cx="{x}" cy="{yy}" rx="{w:.2f}" ry="{w*0.22:.2f}" fill="none" stroke="{HAIR}" stroke-width="0.25"/>')
    out.append(f'<circle cx="{x}" cy="50" r="0.9" fill="{RED}"/>')
    x = cols[1][0]
    out.append(f'<path d="M{x-16},14 Q{x-2},32 {x-16},50 M{x+16},14 Q{x+2},32 {x+16},50" fill="none" stroke="{INK}" stroke-width="0.35"/>')
    for yy in [18, 25, 39, 46]:
        w = 16 - 13 * (1 - abs(yy - 32) / 18)
        out.append(f'<ellipse cx="{x}" cy="{yy}" rx="{w:.2f}" ry="{w*0.22:.2f}" fill="none" stroke="{HAIR}" stroke-width="0.25"/>')
    out.append(f'<ellipse cx="{x}" cy="32" rx="3" ry="0.7" fill="none" stroke="{RED}" stroke-width="0.4"/>')
    x = cols[2][0]
    out.append(f'<path d="M{x-16},14 L{x-9},38 M{x+16},14 L{x+9},38" fill="none" stroke="{INK}" stroke-width="0.35"/>')
    for k in range(40):
        a = (k * 2.399) % (2 * math.pi)
        r = 7 * math.sqrt((k + 0.5) / 40)
        out.append(f'<circle cx="{x + r*math.cos(a)*1.3:.2f}" cy="{45 + r*math.sin(a)*0.7:.2f}" r="0.35" fill="{RED}" fill-opacity="{0.25 + 0.6*(k%3)/3:.2f}"/>')
    for (cx, en, ja, sub) in cols:
        out.append(_t(cx, 6, en, 2.3, RED, "middle", MONO, ls=0.4))
        out.append(_t(cx, 57, ja, 2.6, INK, "middle", weight="bold"))
        out.append(_t(cx, 61, sub, 2.1, MUTED, "middle"))
    out.append(_t(2, 12, "未来", 2.1, MUTED))
    out.append(_t(2, 52, "過去", 2.1, MUTED))
    return _svg(W, H, "".join(out))


def entropy(data=None, highlight=None):
    W, H = 170, 60
    out = [_t(6, 4.5, "MICROSTATES — 10個の粒子を左右の部屋に分ける場合の数", 2.2, MUTED, font=MONO, ls=0.15)]

    def box(ox, label, left, count, hot):
        g = [f'<rect x="{ox}" y="8" width="44" height="30" fill="none" stroke="{INK}" stroke-width="0.35"/>',
             f'<line x1="{ox+22}" x2="{ox+22}" y1="8" y2="38" stroke="{HAIR}" stroke-width="0.25" stroke-dasharray="1 1"/>']
        rnd = random.Random(left)
        for k in range(10):
            x = ox + (2 + rnd.random() * 18 if k < left else 24 + rnd.random() * 18)
            g.append(f'<circle cx="{x:.2f}" cy="{10 + rnd.random() * 26:.2f}" r="1" fill="{RED if hot else INK}"/>')
        g.append(_t(ox + 22, 44, label, 2.4, INK, "middle", weight="bold"))
        g.append(_t(ox + 22, 48.5, f"配置の数：{count}通り", 2.3, RED if hot else MUTED, "middle"))
        return "".join(g)
    out.append(box(6, "左10・右0", 10, 1, False))
    out.append(box(62, "左7・右3", 7, 120, False))
    out.append(box(118, "左5・右5", 5, 252, True))
    out.append(_t(6, 56, "粒子の数が増えると、この差は桁違いに広がる。だから「広がった状態」へ変化する確率が圧倒的に高い（第二法則の統計的な意味）。", 2.1, MUTED))
    return _svg(W, H, "".join(out))


def matter_flow(data=None, highlight=None):
    W, H = 170, 44
    steps = [("最初の数分", "水素・ヘリウムの", "原子核ができる"), ("約38万年後", "中性の原子ができ", "光が直進（CMB）"),
             ("数億年", "最初の恒星・", "銀河ができる"), ("数十億年", "恒星・超新星などで", "重い元素ができる"),
             ("約46億年前", "太陽系と", "地球ができる")]
    out = []
    for k, (t, a, b) in enumerate(steps):
        x = 4 + k * 33
        out.append(f'<rect x="{x}" y="10" width="30" height="22" fill="none" stroke="{RED if k in (0, 3) else INK}" stroke-width="0.35"/>')
        out.append(_t(x + 15, 7, t, 2.2, RED, "middle", MONO))
        out.append(_t(x + 15, 19, a, 2.3, INK, "middle"))
        out.append(_t(x + 15, 23.5, b, 2.3, INK, "middle"))
        if k < len(steps) - 1:
            out.append(f'<line x1="{x+30.5}" x2="{x+32.5}" y1="21" y2="21" stroke="{INK}" stroke-width="0.35"/>')
    out.append(_t(4, 40, "赤枠：元素がつくられる二つの段階（はじめの数分と、恒星などの内部・最期）", 2.1, MUTED))
    return _svg(W, H, "".join(out))


def evidence(data=None, highlight=None):
    W, H = 170, 58
    out = []
    items = [(28, "REDSHIFT", "赤方偏移", "遠い銀河ほど", "光が赤くずれる"),
             (85, "CMB", "宇宙マイクロ波背景放射", "全天から届く", "約2.7Kの放射"),
             (142, "ABUNDANCE", "軽元素の存在比", "水素・ヘリウムの", "割合が予測と一致")]
    for (x, en, ja, a, b) in items:
        out.append(f'<rect x="{x-24}" y="4" width="48" height="22" fill="none" stroke="{INK}" stroke-width="0.35"/>')
        out.append(_t(x, 9, en, 2.1, RED, "middle", MONO, ls=0.3))
        out.append(_t(x, 14, ja, 2.5, INK, "middle", weight="bold"))
        out.append(_t(x, 18.5, a, 2.1, MUTED, "middle"))
        out.append(_t(x, 22, b, 2.1, MUTED, "middle"))
        out.append(f'<path d="M{x},26 C{x},38 85,36 85,44" fill="none" stroke="{RED}" stroke-width="0.35"/>')
    out.append(f'<rect x="43" y="44" width="84" height="10" fill="#141414"/>')
    out.append(_t(85, 50.3, "高温・高密度の初期宇宙から膨張・冷却してきた", 2.5, "#fbfaf7", "middle", weight="bold"))
    return _svg(W, H, "".join(out))


def h0_chart(data=None, highlight=None):
    W, H = 170, 50
    lo, hi = 64, 76
    X = lambda v: 56 + (v - lo) / (hi - lo) * 104
    rows = [("Planck 2018（CMB＋ΛCDM）", 67.4, 0.5, INK), ("CCHP（JWST・別の距離指標）", 70.39, 1.9, MUTED),
            ("H0DN 2026（距離はしご）", "73.50", 0.81, RED)]
    out = []
    for v in range(lo, hi + 1, 2):
        out.append(f'<line x1="{X(v):.2f}" x2="{X(v):.2f}" y1="6" y2="38" stroke="{HAIR}" stroke-width="0.15"/>')
        out.append(_t(X(v), 42, v, 2.1, MUTED, "middle", MONO))
    out.append(_t(108, 47, "H₀（km/s/Mpc）", 2.2, MUTED, "middle"))
    for k, (lab, v, e, col) in enumerate(rows):
        y = 12 + k * 10
        out.append(_t(54, y + 0.9, lab, 2.3, INK, "end"))
        txt = str(v)
        v = float(v)
        out.append(f'<line x1="{X(v-e):.2f}" x2="{X(v+e):.2f}" y1="{y}" y2="{y}" stroke="{col}" stroke-width="0.5"/>')
        out.append(_t(X(v), y - 2.5, f"{txt} ± {e}" + ("（統計・系統誤差を合成）" if txt == "70.39" else ""), 2.1, col, "middle", MONO))
        out.append(f'<circle cx="{X(v):.2f}" cy="{y}" r="1" fill="{col}"/>')
    return _svg(W, H, "".join(out))


def composition(data=None, highlight=None):
    W, H = 170, 30
    parts = [("通常の物質", 4.9, INK, "約4.9%"), ("ダークマター", 26.4, "#7a7a7a", "約26%"), ("ダークエネルギー", 68.7, CREAM, "約69%")]
    out, x = [], 6
    for k, (lab, v, col, txt) in enumerate(parts):
        w = 158 * v / 100
        out.append(f'<rect x="{x:.2f}" y="9" width="{w:.2f}" height="8" fill="{col}"/>')
        out.append(_t(x + (0.5 if k else 0), 6 - (0 if k != 1 else 0), f"{lab} {txt}", 2.3, INK))
        x += w
    out.append(_t(6, 22.5, "ΛCDMモデルを仮定した推定。体積の割合ではなく、エネルギー密度の割合。ダークマター・ダークエネルギーの正体は未解明。", 2.1, MUTED))
    return _svg(W, H, "".join(out))


def unknown_types(data=None, highlight=None):
    W, H = 170, 36
    cols = [("OBSERVABLE", "観測が進めば決着しうる", ["ハッブル張力", "ダークエネルギーの時間変化"]),
            ("THEORETICAL", "新しい理論が必要", ["量子重力", "インフレーションの仕組み"]),
            ("BEYOND REACH", "原理的に観測が難しい", ["観測可能な宇宙の外側", "時間の「前」"])]
    out = []
    for k, (en, ja, items) in enumerate(cols):
        x = 4 + k * 56
        out.append(f'<line x1="{x}" x2="{x+52}" y1="3" y2="3" stroke="{INK}" stroke-width="0.6"/>')
        out.append(_t(x, 8, en, 2.2, RED, font=MONO, ls=0.3))
        out.append(_t(x, 13, ja, 2.6, INK, weight="bold"))
        for j, it in enumerate(items):
            out.append(_t(x, 19 + j * 4.4, "— " + it, 2.3, INK))
    return _svg(W, H, "".join(out))


def domain_coverage(data, highlight=None):
    W, H = 170, 72
    L, R, T = 50, 160, 4
    doms = sorted(data["domains"], key=lambda d: d["order"])
    und = data["understanding"]["nodes"]
    counts = {d["id"]: [0] * 6 for d in doms}
    for n in data["nodes"]:
        counts[n["domains"][0]][und.get(n["id"], {}).get("level", 0)] += 1
    mx = max(sum(v) for v in counts.values()) or 1
    out = []
    for i, d in enumerate(doms):
        y = T + i * 5.6
        out.append(_t(L - 2, y + 3, f'{d["id"]}  {d["ja"]}', 2.3, INK, "end"))
        x = L
        for lv, c in enumerate(counts[d["id"]]):
            if c:
                w = (R - L) * c / mx
                out.append(f'<rect x="{x:.2f}" y="{y}" width="{w:.2f}" height="3.6" fill="{LEVEL_COLORS[lv]}"/>')
                x += w
        out.append(_t(x + 1.5, y + 3, sum(counts[d["id"]]), 2.2, MUTED, font=MONO))
    ly = T + len(doms) * 5.6 + 3
    for lv in range(6):
        lx = L + lv * 19
        out.append(f'<rect x="{lx}" y="{ly}" width="4" height="2.6" fill="{LEVEL_COLORS[lv]}"/>')
        out.append(_t(lx + 5, ly + 2.3, f"L{lv}", 2.1, MUTED, font=MONO))
    return _svg(W, H, "".join(out))


FIGURES = {
    "minimap": (minimap, "今回の範囲（赤）と、知識の地図全体（横：対数の時間、縦：10領域）"),
    "cosmic_timeline": (cosmic_timeline, "宇宙・地球・生命・人類の主な出来事（対数の時間軸）"),
    "expansion": (expansion, "宇宙膨張のイメージ：爆発ではなく、空間の尺度が大きくなる"),
    "clocks": (clocks, "時間の進み方は重力と運動で変わる（光時計の実験とGPS）"),
    "time_origin": (time_origin, "時間の起源をめぐる3つの立場（いずれも観測による確証はない仮説）"),
    "entropy": (entropy, "エントロピーの直感：「広がった状態」に対応する配置の数は圧倒的に多い"),
    "matter_flow": (matter_flow, "物質の歴史：原子核から、私たちの体をつくる元素まで"),
    "evidence": (evidence, "独立した3つの証拠が、同じ一つの描像を指す（証拠の収斂）"),
    "h0_chart": (h0_chart, "ハッブル定数の値の比較（各値の出典は本文）"),
    "composition": (composition, "宇宙のエネルギー密度の内訳（Planck 2018、ΛCDMを仮定）"),
    "unknown_types": (unknown_types, "未解明の問いの3つの種類"),
    "domain_coverage": (domain_coverage, "領域ごとのノード数（色は理解レベル）"),
}
