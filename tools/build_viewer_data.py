"""ビューア用データ viewer/data/graph.json を生成する（DOC-03 §3.5、DOC-05 T-06）。"""
import json
import math
import sys
from datetime import datetime, timezone

from common import ROOT, load_all, time_x, positions


def main():
    d = load_all()
    dom_order = {x["id"]: x["order"] for x in d["domains"]}
    src = {s["id"]: s for s in d["sources"]}
    und = d["understanding"]["nodes"]
    lessons = {}
    for ph in d["curriculum"]:
        for s in ph["sessions"]:
            lessons[s["id"]] = {"title": s["title"], "status": s["status"], "lessons": s.get("lessons", [])}

    # 時間を持たないノードは、主領域ごとに x を等間隔に割り当てる
    # 用語ノードは別の列に分け、用語が増えても他のノードの位置が動かないようにする（DOC-03 §3.1）
    timeless = {}
    for n in d["nodes"]:
        if n["time"] is None:
            timeless.setdefault((n["domains"][0], n["type"] == "term"), []).append(n["id"])

    out_nodes, errors = [], []
    for n in d["nodes"]:
        if n["time"] is None:
            grp = timeless[(n["domains"][0], n["type"] == "term")]
            x = time_x(n, grp.index(n["id"]), len(grp))
        else:
            x = time_x(n)
        cyl, flat = positions(n, dom_order, x)
        if any(math.isnan(v) or math.isinf(v) for v in cyl + flat):
            errors.append(f"[T-06] {n['id']}: 座標が計算できない")
        u = und.get(n["id"], {"level": 0, "status": "unseen"})
        out_nodes.append({
            "id": n["id"], "type": n["type"], "title": n["title"], "summary": n["summary"], "body": n.get("body", ""),
            "domains": n["domains"], "level": n["level"], "parent": n.get("parent"), "time": n["time"],
            "epistemic": n["epistemic"], "confidence": n["confidence"],
            "verification": n["verification"]["status"],
            "sources": [{"id": s, "title": src[s]["title"], "url": src[s].get("url", ""), "existence": src[s]["existence"]} for s in n["sources"]],
            "perspectives": n.get("perspectives", []),
            "understanding": {"level": u["level"], "status": u["status"]},
            "target_level": n["target_level"], "curriculum": n.get("curriculum", []),
            "origin": n.get("origin", "claude"), "glossary": n.get("glossary"), "note_kind": n.get("note_kind"),
            "pos": {"cyl": [round(v, 3) for v in cyl], "flat": [round(v, 3) for v in flat]},
        })
    # 変更点レポートの一覧（content/cycles/*/report.md の frontmatter と output/reports の PDF）
    import re, yaml
    reports = []
    for rp in sorted((ROOT / "content" / "cycles").glob("*/report.md")):
        m = re.match(r"^---\n(.*?)\n---\n", rp.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1))
        pdf = f"output/reports/{fm['report_id']}_{str(fm['date']).replace('-', '')}.pdf"
        reports.append({"id": fm["report_id"], "title": fm["title"], "date": str(fm["date"]), "cycle": fm["cycle"],
                        "map_version": fm["map_version"], "pdf": pdf if (ROOT / pdf).exists() else ""})
    phases = [{"id": ph["id"], "title": ph["title"], "goal": ph.get("goal", ""),
               "sessions": [{"id": s["id"], "title": s["title"], "goal": s.get("goal", ""), "status": s["status"],
                             "lessons": [f for f in s.get("lessons", []) if (ROOT / f).exists()]} for s in ph["sessions"]]}
              for ph in d["curriculum"]]
    graph = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "map_version": d["state"]["map_version"], "system_version": d["state"]["system_version"],
        "current_session": d["state"]["current_session"],
        "domains": d["domains"], "nodes": out_nodes, "edges": d["edges"], "sessions": lessons,
        "questions": d["questions"], "phases": phases, "reports": reports,
        "stats": {"nodes": len(out_nodes), "edges": len(d["edges"]),
                  "assessed": sum(1 for v in und.values() if v.get("status") == "assessed"),
                  "notes": sum(1 for n in out_nodes if n["origin"] == "user-note")},
        "glossaries": [{"key": s["glossary"], "title": s["title"], "source": s["id"]}
                       for s in d["sources"] if s.get("kind") == "user-note" and s.get("glossary")],
    }
    out = ROOT / "viewer" / "data" / "graph.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    if errors:
        for e in errors:
            print("ERROR", e)
        print("build_viewer_data: NG（graph.json は更新しない）")
        return 1
    out.write_text(json.dumps(graph, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    for e in errors:
        print("ERROR", e)
    print(f"build_viewer_data: {'NG' if errors else 'OK'} ({len(out_nodes)} nodes) -> {out.relative_to(ROOT)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
