"""PDF用の自動生成図（DOC-03 §4.3）。すべてSVG文字列を返す。"""
import math
from html import escape
from common import x_of_ya

FONT = "Noto Sans CJK JP, sans-serif"
LEVEL_COLORS = ["#9ca3af", "#60a5fa", "#22d3ee", "#34d399", "#facc15", "#fb923c"]
TICKS = [(13.8e9, "138億年前"), (1e9, "10億"), (1e8, "1億"), (1e7, "1000万"), (1e6, "100万"),
         (1e5, "10万"), (1e4, "1万"), (1e3, "1000"), (1e2, "100年前"), (0, "現在")]


def _xmap(x0, x1, w0, w1):
    lo, hi = x_of_ya(13.8e9), x_of_ya(-30)
    return lambda x: w0 + (x - lo) / (hi - lo) * (w1 - w0)


def _node_x(n):
    t = n["time"]
    x = x_of_ya(t["start_ya"])
    if t.get("end_ya") is not None:
        x = (x + x_of_ya(t["end_ya"])) / 2
    return x


def minimap(data, highlight):
    """領域（行）×対数時間（列）に全ノードを点で描く。highlight のノードを強調。"""
    W, H = 560, 190
    L, R, T, B = 92, 500, 12, 160
    X = _xmap(0, 0, L, R)
    doms = sorted(data["domains"], key=lambda d: d["order"])
    rowh = (B - T) / len(doms)
    hl = set(highlight)
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">',
           f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="#f8fafc" stroke="#e2e8f0"/>',
           f'<rect x="{R+8}" y="{T}" width="{W-R-12}" height="{B-T}" fill="#f8fafc" stroke="#e2e8f0"/>',
           f'<text x="{(R+8+W-4)/2}" y="{B+12}" font-size="7" text-anchor="middle" fill="#64748b">時間なし</text>']
    for i, d in enumerate(doms):
        y = T + rowh * (i + 0.5)
        out.append(f'<text x="{L-4}" y="{y+2.5}" font-size="7" text-anchor="end" fill="#334155">{escape(d["ja"])}</text>')
        out.append(f'<line x1="{L}" x2="{R}" y1="{y}" y2="{y}" stroke="#e2e8f0" stroke-width="0.5"/>')
    for ya, lab in TICKS:
        x = X(x_of_ya(ya))
        out.append(f'<line x1="{x}" x2="{x}" y1="{T}" y2="{B}" stroke="#e2e8f0" stroke-width="0.5"/>')
        out.append(f'<text x="{x}" y="{B+12}" font-size="6.5" text-anchor="middle" fill="#64748b">{lab}</text>')
    dom_idx = {d["id"]: i for i, d in enumerate(doms)}
    timeless_counter = {}
    pts_bg, pts_hl = [], []
    for n in data["nodes"]:
        i = dom_idx[n["domains"][0]]
        y = T + rowh * (i + 0.5)
        if n["time"] is None:
            k = timeless_counter.get(i, 0)
            timeless_counter[i] = k + 1
            x = R + 14 + (k % 8) * 5
            y += (k // 8) * 3 - 2
        else:
            x = X(_node_x(n))
        (pts_hl if n["id"] in hl else pts_bg).append((x, y))
    for x, y in pts_bg:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="#cbd5e1"/>')
    for x, y in pts_hl:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="#1d4ed8" stroke="#fff" stroke-width="0.6"/>')
    out.append(f'<text x="{L}" y="{H-6}" font-size="7" fill="#64748b">← 過去（対数スケール：1目盛りで10倍）</text>')
    out.append(f'<text x="{R}" y="{H-6}" font-size="7" text-anchor="end" fill="#64748b">現在・未来 →</text>')
    out.append("</svg>")
    return "".join(out)


TIMELINE = ["evt.hot-dense-early", "evt.bbn", "evt.recombination", "evt.first-galaxies", "evt.solar-system",
            "evt.earth-formation", "evt.earliest-life", "evt.goe", "evt.cambrian", "evt.kpg", "evt.hominin-split",
            "evt.homo-sapiens", "evt.agriculture", "evt.writing", "evt.industrial-revolution", "evt.chatgpt"]


def cosmic_timeline(data, highlight):
    """対数時間軸。ラベルは等間隔のスロットに置き、実際の位置から引き出し線でつなぐ（初期宇宙の出来事が密集するため）。"""
    W, H = 560, 250
    L, R, Y = 20, 540, 125
    X = _xmap(0, 0, L, R)
    byid = {n["id"]: n for n in data["nodes"]}
    hl = set(highlight)
    evs = [byid[i] for i in TIMELINE if i in byid and byid[i]["time"]]
    evs.sort(key=lambda n: -n["time"]["start_ya"])
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">',
           f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#1e1b4b"/><stop offset="0.45" stop-color="#1e3a8a"/>'
           f'<stop offset="0.8" stop-color="#0e7490"/><stop offset="1" stop-color="#15803d"/></linearGradient></defs>',
           f'<rect x="{L}" y="{Y-4}" width="{R-L}" height="8" rx="4" fill="url(#g)"/>']
    for ya, lab in TICKS:
        x = X(x_of_ya(ya))
        out.append(f'<text x="{x}" y="{Y+1.8}" font-size="5" text-anchor="middle" fill="#fff">{lab}</text>')
    n = len(evs)
    slot = (R - L) / n
    for k, ev in enumerate(evs):
        x = X(x_of_ya(ev["time"]["start_ya"]))
        sx = L + slot * (k + 0.5)
        up = k % 2 == 0
        row = (k // 2) % 2
        ty = (Y - 30 - row * 40) if up else (Y + 38 + row * 40)
        col = "#1d4ed8" if ev["id"] in hl else "#475569"
        ly = ty + 10 if up else ty - 9
        out.append(f'<polyline points="{x:.1f},{Y + (-4 if up else 4)} {x:.1f},{Y + (-12 if up else 12)} {sx:.1f},{ly}" fill="none" stroke="{col}" stroke-width="0.5"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{Y}" r="2.4" fill="#fff" stroke="{col}" stroke-width="1"/>')
        title = ev["title"]["ja"]
        lines = [title[:11], title[11:22]] if len(title) > 11 else [title]
        for j, t in enumerate(lines):
            out.append(f'<text x="{sx:.1f}" y="{ty - (len(lines)-1-j)*8 if up else ty + j*8}" font-size="6.6" text-anchor="middle" fill="{col}" font-weight="bold">{escape(t)}</text>')
        lab_y = (ty + 8) if up else (ty + len(lines) * 8)
        out.append(f'<text x="{sx:.1f}" y="{lab_y}" font-size="5.8" text-anchor="middle" fill="#64748b">{escape(ev["time"]["label"][:14])}</text>')
    out.append("</svg>")
    return "".join(out)


def domain_coverage(data):
    W, H = 560, 210
    L, R, T = 120, 540, 14
    doms = sorted(data["domains"], key=lambda d: d["order"])
    und = data["understanding"]["nodes"]
    counts = {d["id"]: [0] * 6 for d in doms}
    for n in data["nodes"]:
        lv = und.get(n["id"], {}).get("level", 0)
        counts[n["domains"][0]][lv] += 1
    mx = max(sum(v) for v in counts.values()) or 1
    rowh = 17
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">']
    for i, d in enumerate(doms):
        y = T + i * rowh
        out.append(f'<text x="{L-6}" y="{y+10}" font-size="8" text-anchor="end" fill="#334155">{d["id"]} {escape(d["ja"])}</text>')
        x = L
        for lv, c in enumerate(counts[d["id"]]):
            if not c:
                continue
            w = (R - L - 30) * c / mx
            out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="12" fill="{LEVEL_COLORS[lv]}"/>')
            x += w
        out.append(f'<text x="{x+4:.1f}" y="{y+10}" font-size="8" fill="#334155">{sum(counts[d["id"]])}</text>')
    ly = T + len(doms) * rowh + 10
    for lv in range(6):
        lx = L + lv * 62
        out.append(f'<rect x="{lx}" y="{ly}" width="10" height="8" fill="{LEVEL_COLORS[lv]}"/>')
        out.append(f'<text x="{lx+13}" y="{ly+7}" font-size="7" fill="#475569">L{lv}</text>')
    out.append("</svg>")
    return "".join(out)
