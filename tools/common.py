"""ツール共通の読み込み処理と座標計算（DOC-03 §3）。"""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EPISTEMIC_JA = {"fact": "事実", "theory": "理論", "debate": "論争", "normative": "規範", "hypothesis": "仮説", "unknown": "未知"}
EPISTEMIC_FROM_JA = {v: k for k, v in EPISTEMIC_JA.items()}
TYPE_PREFIX = {"theme": "thm", "concept": "con", "event": "evt", "actor": "act", "theory": "thy",
               "evidence": "evd", "question": "q", "method": "mth", "term": "trm"}


def load(rel):
    return json.loads((DATA / rel).read_text(encoding="utf-8"))


def load_all():
    return {
        "domains": load("graph/domains.json"),
        "nodes": load("graph/nodes.json"),
        "edges": load("graph/edges.json"),
        "sources": load("sources.json"),
        "understanding": load("understanding.json"),
        "questions": load("questions.json"),
        "forecasts": load("forecasts.json"),
        "curriculum": load("curriculum.json"),
        "state": load("state.json"),
    }


# ---------------------------------------------------------------- 座標（DOC-03 §3）
K = 10.0


def _h(s, salt=""):
    """IDから決まる 0〜1 の擬似乱数（毎回同じ配置にするため）。"""
    return int(hashlib.md5((salt + s).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def x_of_ya(ya):
    if ya >= 0:
        return -K * math.log10(1 + ya)
    return K * math.log10(1 + abs(ya))


def time_x(node, timeless_index=None, timeless_count=None):
    t = node.get("time")
    if t is None:
        # 時間を持たないノード：-95〜-5 に等間隔
        if timeless_count and timeless_count > 1:
            return -95 + 90 * timeless_index / (timeless_count - 1)
        return -50.0
    x0 = x_of_ya(t["start_ya"])
    if t.get("end_ya") is not None:
        return (x0 + x_of_ya(t["end_ya"])) / 2
    return x0


RADIUS = {2: 6.0, 3: 10.0, 4: 14.0}


def positions(node, domain_order, x):
    i = domain_order[node["domains"][0]]
    timeless = node.get("time") is None
    sector = 2 * math.pi / 10
    theta = sector * (i + 0.5) + (_h(node["id"], "a") - 0.5) * 0.7 * sector
    if node.get("type") == "term":
        # あなたのメモの用語：思考法（軸のすぐ近く）の外側に、薄い殻として並べる（DOC-03 §3.2）
        r = 3.2 + _h(node["id"], "r") * 2.2
    elif timeless:
        r = 1.5 + _h(node["id"], "r") * 0.8
    else:
        r = RADIUS[node["level"]] + (_h(node["id"], "r") - 0.5) * 2
    cyl = [x, r * math.cos(theta), r * math.sin(theta)]
    z = (i - 4.5) * 9 + (_h(node["id"], "z") - 0.5) * 5
    y = (4 - node["level"]) * 7 if not timeless else (-11 if node.get("type") == "term" else -6)
    flat = [x, y, z]
    return cyl, flat
