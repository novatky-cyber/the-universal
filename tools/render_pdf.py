"""原稿（Markdown）→ HTML → PDF（DOC-03 §2, §4、DOC-05 T-07〜T-10）。

使い方：
  python3 tools/render_pdf.py content/cycles/0001            # lesson.md と report.md を生成
  python3 tools/render_pdf.py content/cycles/0001 --allow-unverified   # 検証前の下書き用
終了コード：エラーがあれば1。
"""
import argparse
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from markdown_it import MarkdownIt
from pypdf import PdfReader

from common import ROOT, EPISTEMIC_FROM_JA, load_all
import figures

TEMPLATES = ROOT / "templates"
LESSON_REQUIRED = [str(i) for i in range(1, 15)] + ["付録A", "付録B", "付録C"]
REPORT_REQUIRED = [str(i) for i in range(1, 12)]
LIMITS = {"lesson": (16, 24), "report": (4, 8)}
BOX_TAGS = {"point": "POINT", "analogy": "ANALOGY", "caution": "CAUTION", "exercise": "EXERCISE",
            "background": "BACKGROUND", "term": "TERM", "summary": "SUMMARY"}
LESSON_LABELS = {0: "How to use", 1: "Recap", 2: "Map", 3: "Question", 4: "Main text", 5: "Evidence", 6: "Debates",
                 7: "Unknowns", 8: "Connections", 9: "Thinking tools", 10: "Now", 11: "Glossary", 12: "Explain",
                 13: "Check", 14: "Further reading", "付録A": "Answers", "付録B": "Sources", "付録C": "Submit"}
REPORT_LABELS = {1: "Summary", 2: "Versions", 3: "Changes", 4: "Corrections", 5: "Impact", 6: "Understanding",
                 7: "Questions", 8: "Forecasts", 9: "Pending", 10: "System", 11: "Next"}
FONT_PKGS = [("zen-kaku-gothic-new", ["400", "500", "700"]),  # 欧文1書体・和文1書体（ADR-0005）
             ("ibm-plex-mono", ["300", "400", "500"])]


def font_css():
    """@fontsource の CSS（file://）。未取得なら空（Noto CJK で代替）。DOC-03 §7。"""
    base = ROOT / ".cache" / "fonts" / "node_modules" / "@fontsource"
    out = []
    for pkg, ws in FONT_PKGS:
        for w in ws:
            f = base / pkg / f"{w}.css"
            if f.exists():
                out.append(f.as_uri())
    return out

md = MarkdownIt("commonmark", {"html": True, "typographer": False}).enable("table")


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("frontmatter がありません")
    return yaml.safe_load(m.group(1)), m.group(2)


FENCE = re.compile(r"^(```|~~~)")


def outside_code_md(text, fn):
    """Markdown のフェンス・インラインコードの外側だけに fn を適用する。"""
    out, in_fence, chunk = [], False, []
    for line in text.split("\n"):
        if FENCE.match(line.strip()):
            if not in_fence:
                out.append(_apply_inline_code(("\n".join(chunk)), fn)) if chunk else None
                chunk = []
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
        else:
            chunk.append(line)
            continue
    if chunk:
        out.append(_apply_inline_code("\n".join(chunk), fn))
    return "\n".join(out)


def _apply_inline_code(text, fn):
    parts = re.split(r"(`[^`\n]*`)", text)
    return "".join(p if p.startswith("`") and p.endswith("`") and len(p) > 1 else fn(p) for p in parts)


def outside_code_html(html, fn):
    """HTML の <pre>…</pre> と <code>…</code> の外側だけに fn を適用する。"""
    parts = re.split(r"(<pre[\s\S]*?</pre>|<code[\s\S]*?</code>)", html)
    return "".join(p if p.startswith("<pre") or p.startswith("<code") else fn(p) for p in parts)


class Renderer:
    def __init__(self, data, kind):
        self.data, self.kind = data, kind
        self.nodes = {n["id"]: n for n in data["nodes"]}
        self.sources = {s["id"]: s for s in data["sources"]}
        self.cited = []          # 出典の出現順
        self.errors, self.warnings = [], []
        self.fig_no = 0

    # ---- インライン記法（Markdown変換の前に処理）
    def inline(self, text):
        def src(m):
            sid = "src." + m.group(1)
            if sid not in self.sources:
                self.errors.append(f"[T-09] 出典 {sid} が sources.json にない")
                return "<sup class='cite'>[?]</sup>"
            if sid not in self.cited:
                self.cited.append(sid)
            return f"<sup class='cite'>[{self.cited.index(sid)+1}]</sup>"

        def node(m):
            nid, label = m.group(1), m.group(2)
            if nid not in self.nodes:
                self.errors.append(f"[T-09] ノード {nid} が存在しない")
                return label or nid
            label = label or self.nodes[nid]["title"]["ja"]
            return f"<span class='nref'>{label}<span class='nid'>{nid}</span></span>"

        def apply(t):
            t = re.sub(r"\[\[src:([a-z0-9-]+)\]\]", src, t)
            t = re.sub(r"\[\[node:([a-z]+\.[a-z0-9-]+)(?:\|([^\]]+))?\]\]", node, t)
            # 日本語の約物（「」など）に隣接する **太字** は CommonMark の規則で無効になるため、先に変換する
            t = re.sub(r"\*\*([^*\n]+?)\*\*", r"<strong>\1</strong>", t)
            for bad in re.findall(r"\[\[[^\]]*\]\]", t):
                self.errors.append(f"[T-09] 書式の誤った参照 {bad}")
            return t
        return outside_code_md(text, apply)

    def badges(self, html):
        def rep(m):
            ja = m.group(1)
            return f"<span class='ep ep-{EPISTEMIC_FROM_JA[ja]}'>{ja}</span>"
        return outside_code_html(html, lambda h: re.sub(r"\{(事実|理論|論争|規範|仮説|未知)\}", rep, h))

    def figure(self, name, highlight):
        if name not in figures.FIGURES:
            self.errors.append(f"未知の図 {name}")
            return ""
        fn, cap = figures.FIGURES[name]
        self.fig_no += 1
        return (f"<figure>{fn(self.data, highlight)}<figcaption><span class='fig'>FIG. {self.fig_no:02d}</span>{cap}</figcaption></figure>")

    def heading(self, key, title):
        labels = LESSON_LABELS if self.kind == "lesson" else REPORT_LABELS
        if key.startswith("付録"):
            num, lab = key[-1], labels.get(key, "APPENDIX")
            title = re.sub(r"^[\s　]*", "", title)
        else:
            num, lab = f"{int(key):02d}", labels.get(int(key), "")
        title = self.badges(self.inline(title))
        return (f"<h2 id='sec-{num}'><span class='sec'><span class='num'>{num}</span><span class='lab'>{lab}</span></span>"
                f"<span class='ttl'>{title}</span></h2>")

    def sources_html(self):
        items = []
        for sid in self.cited:
            s = self.sources[sid]
            meta = "．".join(x for x in [s.get("author"), s.get("publisher"), str(s["year"]) if s.get("year") else ""] if x)
            unv = "" if s["existence"] == "verified" else " <span class='unv'>［実在未確認］</span>"
            url = f"<br><span class='url'>{s['url']}</span>" if s.get("url") else ""
            items.append(f"<li>{s['title']}．{meta}{unv}{url}</li>")
        return "<ol class='srcs'>" + "".join(items) + "</ol>" if items else "<p class='small'>（参照なし）</p>"

    def render_body(self, body, highlight):
        out, lines, i = [], body.split("\n"), 0
        buf = []

        def flush():
            if buf:
                out.append(self.badges(md.render(self.inline("\n".join(buf)))))
                buf.clear()

        in_fence = False
        while i < len(lines):
            line = lines[i]
            if FENCE.match(line.strip()):
                in_fence = not in_fence
            if in_fence or FENCE.match(line.strip()):
                buf.append(line)
                i += 1
                continue
            m = re.match(r"^:::(point|analogy|caution|exercise|write|background|term|summary)\s*(.*)$", line)
            if m:
                flush()
                kind, title = m.group(1), m.group(2).strip()
                inner = []
                i += 1
                while i < len(lines) and lines[i].strip() != ":::":
                    inner.append(lines[i])
                    i += 1
                if i >= len(lines):
                    self.errors.append(f"閉じられていないブロック :::{kind} {title}")
                if kind == "write":
                    lm = re.search(r"lines=(\d+)", title)
                    n = int(lm.group(1)) if lm else 6
                    title = re.sub(r"\s*lines=\d+", "", title)
                    out.append(f"<div class='write'><div class='write-title'>ANSWER — {title}</div>" + "<div class='line'></div>" * n + "</div>")
                else:
                    inner_html = self.badges(md.render(self.inline("\n".join(inner))))
                    tag = BOX_TAGS[kind]
                    if kind == "term" and "｜" in title:
                        ja, en = title.split("｜", 1)
                        head = f"<span class='tag'>{tag}</span>{ja}<span class='en'>{en}</span>"
                    else:
                        head = f"<span class='tag'>{tag}</span>{title}"
                    out.append(f"<div class='box box-{kind}'><div class='box-title'>{head}</div>{inner_html}</div>")
                i += 1
                continue
            hm = re.match(r"^## (\d+|付録[A-Z])[.．]?\s*(.*)$", line)
            if hm:
                flush()
                out.append(self.heading(hm.group(1), hm.group(2)))
                i += 1
                continue
            fm = re.match(r"^\{\{figure:([a-z_]+)\}\}\s*$", line)
            if fm:
                flush()
                out.append(self.figure(fm.group(1), highlight))
            elif line.strip() == "{{sources}}":
                flush()
                out.append("@@SOURCES@@")      # 全文の処理後に置換（出典の出現順を確定させるため）
            elif line.strip() == "<!-- pagebreak -->":
                flush()
                out.append("<div class='pb'></div>")
            else:
                buf.append(line)
            i += 1
        flush()
        html = "\n".join(out)
        if self.kind == "lesson":
            for sid in self.cited:
                if self.sources[sid]["existence"] != "verified":
                    self.errors.append(f"[T-10] 教材が実在未確認の出典 {sid} を参照している")
        return html.replace("@@SOURCES@@", self.sources_html())



def section_heads(body):
    heads, in_fence = set(), False
    for line in body.split("\n"):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^## (\d+)[.．]", line) or re.match(r"^## (付録[A-Z])", line)
        if m:
            heads.add(m.group(1))
    return heads


def check_sections(bodies, kind):
    """必須セクションの検査（分冊時は前後編の合計で判定）。"""
    req = LESSON_REQUIRED if kind == "lesson" else REPORT_REQUIRED
    heads = set().union(*[section_heads(b) for b in bodies])
    return [f"[T-07] 必須セクション「{r}」がない" for r in req if r not in heads]


def _browser(p):
    exe = "/usr/bin/google-chrome"
    return p.chromium.launch(executable_path=exe) if Path(exe).exists() else p.chromium.launch()


def pdf_from_html(html_path, out_pdf, header, date="", cover=False):
    """HTMLファイル → PDF。表紙は余白・ヘッダーなし。"""
    from playwright.sync_api import sync_playwright
    style = "font-family:'IBM Plex Mono','Noto Sans Mono CJK JP',monospace;font-size:6.5px;letter-spacing:1.2px;color:#8a8a8a;width:100%;padding:0 20mm;display:flex;justify-content:space-between"
    head = f"<div style=\"{style}\"><span>THE UNIVERSAL</span><span>{header}</span></div>"
    foot = (f"<div style=\"{style}\"><span>ISSUED {date}</span>"
            "<span><span class='pageNumber'></span> / <span class='totalPages'></span></span></div>")
    with sync_playwright() as p:
        b = _browser(p)
        pg = b.new_page()
        pg.goto(Path(html_path).as_uri(), wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        if cover:
            pg.pdf(path=str(out_pdf), width="210mm", height="297mm", print_background=True,
                   margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}, prefer_css_page_size=False)
        else:
            pg.pdf(path=str(out_pdf), format="A4", print_background=True, display_header_footer=True,
                   header_template=head, footer_template=foot, prefer_css_page_size=True)
        b.close()


def merge_pdfs(parts, out_pdf):
    from pypdf import PdfWriter
    w = PdfWriter()
    for p in parts:
        w.append(str(p))
    with open(out_pdf, "wb") as f:
        w.write(f)


def build(path, kind, allow_unverified=False):
    data = load_all()
    fm, body = split_frontmatter(path.read_text(encoding="utf-8").replace("\r\n", "\n"))
    r = Renderer(data, kind)
    highlight = fm.get("nodes", [])
    for nid in highlight:
        if nid not in r.nodes:
            r.errors.append(f"[T-09] frontmatter のノード {nid} が存在しない")
    html_body = r.render_body(body, highlight)
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=False)
    css = (TEMPLATES / "print.css").read_text(encoding="utf-8")
    fonts = font_css()
    if not fonts:
        r.warnings.append("書体（@fontsource）が未取得のため Noto CJK で代替（tools/setup_fonts.sh を実行）")
    tpl = env.get_template(f"{kind}.html.j2")
    html = tpl.render(fm=fm, body=html_body, css=css, font_css=fonts)
    vol = fm.get("volume", "")
    stem = f"{fm['lesson_id']}{vol}_{fm['session']}" if kind == "lesson" else f"{fm['report_id']}_{str(fm['date']).replace('-', '')}"
    # 表紙
    if kind == "lesson":
        vol_en = {"a": "VOLUME A", "b": "VOLUME B"}.get(vol, "")
        kicker = f"{fm.get('phase_en', '')} · {fm['session']} · {vol_en}".strip(" ·")
        meta = [("LESSON", f"{fm['lesson_id']}{vol.upper()}"), ("SESSION", fm["session"]),
                ("MAP", f"v{fm['map_version']}"), ("ISSUED", fm["date"])]
        right = f"LESSON {fm['lesson_id']}{vol.upper()}"
    else:
        kicker = f"CHANGE REPORT · CYCLE {int(fm['cycle']):04d}"
        meta = [("REPORT", fm["report_id"]), ("MAP", f"v{fm['map_version']}"),
                ("SYSTEM", fm["system_version"]), ("ISSUED", fm["date"])]
        right = f"REPORT {fm['report_id']}"
    cover_html = env.get_template("cover.html.j2").render(
        fm=fm, css=css, font_css=fonts, art=figures.cover_art(data, highlight), kicker=kicker,
        kicker_right=right, en_title=fm.get("en_title", ""), meta=meta)
    debug = ROOT / "output" / "debug"
    debug.mkdir(parents=True, exist_ok=True)
    body_html_path, cover_html_path = debug / f"{stem}.html", debug / f"{stem}_cover.html"
    body_html_path.write_text(html, encoding="utf-8")
    cover_html_path.write_text(cover_html, encoding="utf-8")
    if allow_unverified:
        r.errors = [e for e in r.errors if not e.startswith("[T-10]")]
    out_dir = ROOT / "output" / ("lessons" if kind == "lesson" else "reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = out_dir / f"{stem}.pdf"
    if r.errors:
        return r, None, 0
    vol_ja = {"a": "前編", "b": "後編"}.get(vol, "")
    header = f"{fm.get('lesson_id', fm.get('report_id'))}{vol.upper()}　{fm['title']}　{vol_ja}".strip()
    tmp_body, tmp_cover = debug / f"{stem}_body.pdf", debug / f"{stem}_cover.pdf"
    pdf_from_html(cover_html_path, tmp_cover, header, fm.get("date", ""), cover=True)
    pdf_from_html(body_html_path, tmp_body, header, fm.get("date", ""))
    merge_pdfs([tmp_cover, tmp_body], out_pdf)
    pages = len(PdfReader(str(out_pdf)).pages)
    lo, hi = LIMITS[kind]
    if pages < lo:
        r.warnings.append(f"[T-08] {pages}ページ（標準 {lo}〜{hi}）：内容が不足していないか確認")
    if pages > hi:
        msg = f"[T-08] {pages}ページ（上限 {hi}）"
        (r.errors if kind == "lesson" else r.warnings).append(msg + ("：分冊が必要" if kind == "lesson" else ""))
    return r, out_pdf, pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cycle_dir")
    ap.add_argument("--allow-unverified", action="store_true")
    a = ap.parse_args()
    d = Path(a.cycle_dir)
    if not d.is_absolute():
        d = (Path.cwd() / d) if (Path.cwd() / d).exists() else (ROOT / d)
    d = d.resolve()
    ok = True
    jobs = []
    if (d / "lesson.md").exists():
        jobs.append(("lesson", [d / "lesson.md"]))
    elif (d / "lesson_a.md").exists():
        jobs.append(("lesson", sorted(d.glob("lesson_[a-z].md"))))
    if (d / "report.md").exists():
        jobs.append(("report", [d / "report.md"]))
    if not any(k == "lesson" for k, _ in jobs):
        print("ERROR lesson: lesson.md または lesson_a.md がない")
        ok = False
    for kind, paths in jobs:
        bodies = [split_frontmatter(p.read_text(encoding="utf-8").replace("\r\n", "\n"))[1] for p in paths]
        for e in check_sections(bodies, kind):
            print("ERROR", kind, e)
            ok = False
        for p in paths:
            r, pdf, pages = build(p, kind, a.allow_unverified)
            for w in r.warnings:
                print("WARN ", p.name, w)
            for e in r.errors:
                print("ERROR", p.name, e)
            if pdf:
                print(f"OK    {p.name}: {pdf.relative_to(ROOT)} ({pages} pages)")
            if r.errors:
                ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
