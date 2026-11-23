"""データ検証（DOC-05 T-01〜T-05）。エラーがあれば終了コード1。"""
import sys
import json
from jsonschema import Draft202012Validator
from common import DATA, TYPE_PREFIX, load_all

SCHEMAS = {
    "graph/domains.json": "domain", "graph/nodes.json": "node", "graph/edges.json": "edge",
    "sources.json": "source", "understanding.json": "understanding", "questions.json": "question",
    "forecasts.json": "forecast", "curriculum.json": "curriculum", "state.json": "state",
}


def main():
    errors, warnings = [], []
    # T-01 スキーマ
    for rel, sch in SCHEMAS.items():
        schema = json.loads((DATA / "schema" / f"{sch}.schema.json").read_text(encoding="utf-8"))
        doc = json.loads((DATA / rel).read_text(encoding="utf-8"))
        for e in Draft202012Validator(schema).iter_errors(doc):
            errors.append(f"[T-01] {rel}: {'/'.join(map(str, e.path))}: {e.message}")
    if errors:
        return report(errors, warnings)

    d = load_all()
    node_ids = [n["id"] for n in d["nodes"]]
    ids = set(node_ids)
    src_ids = {s["id"] for s in d["sources"]}
    dom_ids = {x["id"] for x in d["domains"]}

    # T-02 重複・参照
    for coll, key in [(d["nodes"], "nodes"), (d["edges"], "edges"), (d["sources"], "sources"), (d["questions"], "questions")]:
        seen = set()
        for x in coll:
            if x["id"] in seen:
                errors.append(f"[T-02] {key}: ID重複 {x['id']}")
            seen.add(x["id"])
    src_kind = {x["id"]: x.get("kind") for x in d["sources"]}
    src_glossary = {x["id"]: x.get("glossary") for x in d["sources"] if x.get("kind") == "user-note"}
    for n in d["nodes"]:
        if TYPE_PREFIX[n["type"]] != n["id"].split(".")[0]:
            errors.append(f"[T-02] {n['id']}: 接頭辞が種類 {n['type']} と一致しない")
        if n.get("parent") and n["parent"] not in ids:
            errors.append(f"[T-02] {n['id']}: parent {n['parent']} が存在しない")
        if n["type"] != "theme" and not n.get("parent"):
            errors.append(f"[T-02] {n['id']}: テーマ以外は parent が必要")
        for dm in n["domains"]:
            if dm not in dom_ids:
                errors.append(f"[T-02] {n['id']}: 領域 {dm} が存在しない")
        for s in n["sources"] + [s for p in n.get("perspectives", []) for s in p.get("sources", [])]:
            if s not in src_ids:
                errors.append(f"[T-02] {n['id']}: 出典 {s} が sources.json にない")
        # T-03 は必須属性としてスキーマで検査済み。T-04：
        if not n["sources"] and n["verification"]["status"] != "unverified":
            errors.append(f"[T-04] {n['id']}: 出典が空なのに verification.status が unverified でない")
        # T-11 あなたのメモの用語（DOC-01 F11）：用語ノードは user-note 由来で、出典は user-note の資料だけ
        is_term, is_note = n["type"] == "term", n.get("origin") == "user-note"
        if is_term != is_note:
            errors.append(f"[T-11] {n['id']}: type term と origin user-note は対応していなければならない")
        if is_term and (not n.get("glossary") or not n["sources"]
                        or any(src_glossary.get(s) != n["glossary"] for s in n["sources"])):
            errors.append(f"[T-11] {n['id']}: 用語ノードには glossary と、同じ用語集の user-note の出典が必要")
        if not is_term and any(src_kind.get(s) == "user-note" for s in n["sources"]):
            errors.append(f"[T-11] {n['id']}: user-note の資料はClaude由来のノードの根拠にしない")
        t = n.get("time")
        if t and t.get("end_ya") is not None and t["end_ya"] > t["start_ya"]:
            errors.append(f"[T-02] {n['id']}: end_ya が start_ya より過去")
    # parent の循環
    parent = {n["id"]: n.get("parent") for n in d["nodes"]}
    for nid in ids:
        seen, cur = set(), nid
        while cur:
            if cur in seen:
                errors.append(f"[T-02] {nid}: parent が循環している")
                break
            seen.add(cur)
            cur = parent.get(cur)
    for e in d["edges"]:
        for end in ("from", "to"):
            if e[end] not in ids:
                errors.append(f"[T-02] {e['id']}: {end} {e[end]} が存在しない")
        for s in e.get("sources", []):
            if s not in src_ids:
                errors.append(f"[T-02] {e['id']}: 出典 {s} が存在しない")
        if e["from"] == e["to"]:
            errors.append(f"[T-02] {e['id']}: 自己ループ")
    for q in d["questions"]:
        for nid in q["nodes"]:
            if nid not in ids:
                errors.append(f"[T-02] {q['id']}: 関連ノード {nid} が存在しない")
    for ph in d["curriculum"]:
        for s in ph["sessions"]:
            for nid in s.get("nodes", []):
                if nid not in ids:
                    errors.append(f"[T-02] {s['id']}: ノード {nid} が存在しない")
    sess_ids = {s["id"] for ph in d["curriculum"] for s in ph["sessions"]}
    for n in d["nodes"]:
        for c in n.get("curriculum", []):
            if c not in sess_ids:
                errors.append(f"[T-02] {n['id']}: セッション {c} が存在しない")
    if d["state"]["current_session"] not in sess_ids:
        errors.append(f"[T-02] state.current_session {d['state']['current_session']} が存在しない")
    # T-05 理解レイヤー
    for nid in d["understanding"]["nodes"]:
        if nid not in ids:
            errors.append(f"[T-05] understanding: {nid} が存在しない")
    # 警告
    unv = sum(1 for n in d["nodes"] if n["verification"]["status"] != "verified")
    warnings.append(f"未検証のノード {unv}/{len(ids)} 件（verification.status != verified）")
    return report(errors, warnings, d)


def report(errors, warnings, d=None):
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    if d:
        print(f"nodes={len(d['nodes'])} edges={len(d['edges'])} sources={len(d['sources'])} "
              f"questions={len(d['questions'])} forecasts={len(d['forecasts'])}")
    print("validate:", "NG" if errors else "OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
