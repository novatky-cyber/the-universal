"""地図の差分集計（DOC-03 §5）。

使い方：python3 tools/map_diff.py <gitref|none> [--json out.json]
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
    try:
        out = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=ROOT, capture_output=True, check=True, text=True).stdout
        return json.loads(out)
    except subprocess.CalledProcessError:
        return []


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
    ap.add_argument("ref")
    ap.add_argument("--json")
    a = ap.parse_args()
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
    if a.json:
        (ROOT / a.json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
