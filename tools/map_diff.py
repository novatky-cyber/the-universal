"""地図の差分集計（DOC-03 §5）。

使い方：python3 tools/map_diff.py [gitref|none] [--json out.json] [--md out.md]
  gitref に none を指定すると、空の地図との差分（＝すべて追加）を出す（初版用）。
"""
import argparse
import json
import subprocess
import sys
from collections import Counter

from common import ROOT, load

FILES = {"nodes": "data/graph/nodes.json", "edges": "data/graph/edges.json", "sources": "data/sources.json"}
IGNORE = {"history", "verification"}


def at_ref(ref, rel):
    if ref == "none":
        return []
    r = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        if "exists on disk, but not in" in r.stderr or "does not exist in" in r.stderr:
            return []          # その時点ではファイルがなかった
        raise SystemExit(f"ERROR 参照 {ref} を読めない: {r.stderr.strip()}")
    return json.loads(r.stdout)


def latest_map_tag():
    r = subprocess.run(["git", "tag", "--list", "map-v*", "--sort=-v:refname"], cwd=ROOT, capture_output=True, text=True)
    tags = r.stdout.split()
    return tags[0] if tags else "none"


def to_markdown(result, ref):
    lines = [f"# 地図の差分（比較元：{ref}）", ""]
    for key in FILES:
        r = result[key]
        lines.append(f"## {key}：追加 {len(r['added'])}／削除 {len(r['removed'])}／変更 {len(r['changed'])}")
        for i in r["added"]:
            lines.append(f"- 追加 {i}")
        for i in r["removed"]:
            lines.append(f"- 削除 {i}")
        for c in r["changed"]:
            lines.append(f"- 変更 {c['id']}（{', '.join(c['fields'])}）")
        lines.append("")
    return "\n".join(lines)


def diff(old, new):
    o, n = {x["id"]: x for x in old}, {x["id"]: x for x in new}
    added = sorted(set(n) - set(o))
    removed = sorted(set(o) - set(n))
    changed = []
    for k in sorted(set(o) & set(n)):
        keys = sorted(a for a in set(o[k]) | set(n[k]) if a not in IGNORE and o[k].get(a) != n[k].get(a))
        if keys:
            changed.append({"id": k, "fields": keys})
    return {"added": added, "removed": removed, "changed": changed}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref", nargs="?", help="比較元のGit参照。省略時は最新の map-v* タグ（なければ none）")
    ap.add_argument("--json")
    ap.add_argument("--md")
    a = ap.parse_args()
    a.ref = a.ref or latest_map_tag()
    result = {}
    for key, rel in FILES.items():
        new = load(rel.replace("data/", ""))
        result[key] = diff(at_ref(a.ref, rel), new)
    nodes = {x["id"]: x for x in load("graph/nodes.json")}
    by_dom = Counter(nodes[i]["domains"][0] for i in result["nodes"]["added"] if i in nodes)
    result["added_by_domain"] = dict(sorted(by_dom.items()))
    for key in FILES:
        r = result[key]
        print(f"{key}: +{len(r['added'])} -{len(r['removed'])} ~{len(r['changed'])}")
    print("added_by_domain:", result["added_by_domain"])
    if a.md:
        (ROOT / a.md).write_text(to_markdown(result, a.ref), encoding="utf-8")
    if a.json:
        (ROOT / a.json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
