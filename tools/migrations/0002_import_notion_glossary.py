"""あなたのNotionメモ（3つの用語集）を、知識の地図に「用語」ノードとして取り込む（DOC-01 F11、DOC-03 §1.3）。

入力：data/import/notion_glossary.json（Notionから抽出した用語名と1〜2文の定義。Notionは読むだけで書き換えない）
出力：data/graph/nodes.json（trm.* ノードと、受け皿のテーマ）、data/sources.json（user-note の出典3件）、
      data/import/notion_glossary_import_log.json（件数と除外のハッシュのみ）

- 用語の正本のキーは Notion のページID（notion_id）。ノードIDも notion_id から作るので、Notion で題名を直してもIDは変わらない。
- 既存の用語ノードは**更新**する（upsert）。定義が変わった用語だけ verification を unverified に戻し、history に記録する。
  Verifier が付けた verified、置き場所（domains／parent）、history は保つ。
- 受け皿のテーマは、なければ作る（既存のものは触らない）。
- 何度実行しても、入力が同じなら結果は同じ。
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

# 公開リポジトリのため取り込まないもの（DOC-01 F11 の除外基準）。
# 題名や理由の詳細を公開しないよう、notion_id の SHA-1（先頭16桁）と大まかな分類だけで指定する。
# notion_id はランダムなIDなので、ハッシュから題名は推測できない。
# 分類：privacy（顧客・居住地・個人的な行動を推測させうる）／duplicate（重複）／not-a-term（地図の単位にならない）／news-snapshot（時点の速報）
EXCLUDE = {
    "539e270057fe591f": "news-snapshot",
    "cead362c8f1143b4": "duplicate",
    "cd0827deb6a33f08": "not-a-term",
    "5b08f887cdf16fed": "privacy",
    "17c1eaef92eddfaf": "privacy",
    "5b29c7a9e6aab8e2": "duplicate",
    "11d547f0bbfd824a": "privacy",
    "123b5dd45d3d25a5": "privacy",
    "d8b710aaad42a74d": "privacy",
    "4f34322c263249f9": "privacy",
}

# 用語集 → 出典ID（資料にも glossary 属性を持たせ、ビューアと検査はそれを使う）
GLOSSARIES = {
    "ai": ("src.notion-ai-glossary", "AI用語集（あなたのNotionメモ）"),
    "business": ("src.notion-business-glossary", "ビジネス用語集（あなたのNotionメモ）"),
    "general": ("src.notion-general-glossary", "一般用語集（あなたのNotionメモ）"),
}

# 受け皿のテーマ（Claude由来。出典は今後のサイクルで付ける）
NEW_THEMES = [
    ("thm.ai-practice", "生成AIの実装と活用", "Building & using generative AI", ["D02", "D04"],
     "LLM・エージェント・RAG・MCPなど、生成AIを仕組みとして組み立て、業務で使うための概念群。"),
    ("thm.business-practice", "経営と業務の実務", "Management & business practice", ["D05"],
     "経営学・プロジェクトマネジメント・業務システム・マーケティングなど、組織を動かす実務の概念群。"),
    ("thm.body-medicine", "人体と医学", "The human body & medicine", ["D03"],
     "人体の構造と働き、健康と病気、医療と社会保障の制度。"),
    ("thm.regions-life", "地域・食・暮らし", "Regions, food & everyday life", ["D10", "D07"],
     "地域の自然条件と歴史・産業・食文化の関係、旅や暮らしの知識。"),
]

# 新しく取り込む用語の置き場所（主領域・親テーマ）。題名のキーワードで、上から順に最初に一致したもの。
# どれにも一致しなければ、用語集ごとの既定（DEFAULT）。既存の用語ノードの置き場所は変えない。
DEFAULT = {"ai": ("D02", "thm.ai-practice"), "business": ("D05", "thm.business-practice"), "general": ("D07", "thm.world-history")}
RULES = [
    (r"^半導体", ("D01", "thm.matter")),
    (r"^Transformer$", ("D02", "thm.computation")),
    (r"冪等性|閉域ネットワーク|ハードウェア|LP・HP作成|ITインフラ|セキュリティ|システム開発", ("D02", "thm.computation")),
    (r"経済学入門|デカップリング|サーキットブレーカー|追証|ポートフォリオ|エクイティ|確定拠出年金|401k|暦年贈与", ("D05", "thm.economy")),
    (r"法学入門|日本の法律|グローバルサウス", ("D06", "thm.state-order")),
    (r"^ISO$", ("D04", "thm.tech-history")),
    (r"太政官|幕府|朝廷|宗門人別帳|戸籍|壬申|戸長|苗字|門割|内閣制度|五・一五|二・二六|国家総動員|大政翼賛|家制度|霞が関", ("D07", "thm.modernity")),
    (r"^政治|^政・|^政府|^国家|^近代国家|政党政治|官僚|縦割り|イデオロギー|補完性原理|日本政治", ("D06", "thm.state-order")),
    (r"^プロトコル|社会学入門", ("D10", "thm.systems")),
    (r"レゾナンス|物理学入門|日常生活における物理学|化学入門", ("D01", "thm.matter")),
    (r"地学入門|オーロラ|Kp指数", ("D01", "thm.earth-solar")),
    (r"心理学効果", ("D03", "thm.mind")),
    (r"生物学入門", ("D03", "thm.life")),
    (r"微分積分|ベクトル|クロソイド", ("D02", "thm.probability")),
    (r"かさぶた|医療費控除|介護保険|医学入門|解剖学|生理学|人体の構造|交感神経", ("D03", "thm.body-medicine")),
    (r"インプロヴィゼーション|サント・シャペル|ジョルジョーネ|大和猿楽|文学入門|建築学入門|村上春樹|大滝詠一|ポップス伝|流行歌|映画市場|EBiDAN|風博士|ずとまよ", ("D09", "thm.arts")),
    (r"グッドイヤーウェルト|エンジン|バイク|空港", ("D04", "thm.tech-history")),
    (r"奈良県|大阪府|京都府|和歌山県|滋賀県|三重県|愛知県|静岡県|兵庫県|食文化|農作物|お茶|ビール|うなぎ|海外旅行|旅行英語|ビザ", ("D10", "thm.regions-life")),
]


def place(key, title):
    for pat, val in RULES:
        if re.search(pat, title):
            return val
    return DEFAULT[key]


def h16(s):
    return hashlib.sha1(s.encode()).hexdigest()[:16]


def node_id(key, notion_id):
    """notion_id から作る安定したID（DOC-03 §1.1：一度公開したIDは変えない）。"""
    return f"trm.{key[:3]}-{h16(notion_id)[:10]}"


def clean_title(t):
    """表示用の名前（DOC-03 §1.3）：副題（「｜」以降）、先頭の日付、末尾の版番号、仕事の文脈を示す語を除く。"""
    t = t.split("｜")[0].strip()
    t = re.sub(r"^\d{4}/\d{2}/\d{2}\s*", "", t)
    t = re.sub(r"\s+v\d+$", "", t)
    t = re.sub(r"(・|と)?提案実務", "", t)
    return {"心理学効果": "心理学効果（認知バイアス）"}.get(t, t)


def main():
    today = date.today().isoformat()
    mapv = json.loads((DATA / "state.json").read_text(encoding="utf-8"))["map_version"]
    imp_path = DATA / "import" / "notion_glossary.json"
    imp = json.loads(imp_path.read_text(encoding="utf-8"))
    nodes = json.loads((DATA / "graph" / "nodes.json").read_text(encoding="utf-8"))
    sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))

    by_id = {n["id"]: n for n in nodes}
    for tid, ja, en, doms, summ in NEW_THEMES:
        if tid not in by_id:
            by_id[tid] = {"id": tid, "type": "theme", "title": {"ja": ja, "en": en}, "summary": summ, "domains": doms,
                          "level": 2, "parent": None, "time": None, "epistemic": "theory", "confidence": "medium",
                          "sources": [], "verification": {"status": "unverified"}, "target_level": 2, "curriculum": [],
                          "origin": "claude",
                          "history": [{"map_version": mapv, "change": "作成", "reason": "あなたのメモの用語の受け皿（DOC-01 F11）"}]}

    src_by_id = {s["id"]: s for s in sources}
    for key, (sid, title) in GLOSSARIES.items():
        if sid not in src_by_id:
            s = {"id": sid, "title": title, "url": "", "author": "", "publisher": "Notion（非公開）", "year": None,
                 "kind": "user-note", "existence": "verified", "checked_at": today,
                 "note": "あなた自身のNotionメモ。正本はNotion（読むだけで書き換えない）。地図には用語名と1〜2文の定義だけを写す。内容の正確さはVerifierが少しずつ確認する（DOC-04 §2）。"}
            sources.append(s)
            src_by_id[sid] = s
        src_by_id[sid]["glossary"] = key

    counts = {"new": 0, "updated": 0, "unchanged": 0}
    excluded = {}
    for g in imp["glossaries"]:
        key = g["key"]
        kept = []
        for e in g["entries"]:
            hid = h16(e["notion_id"])
            if hid in EXCLUDE:
                excluded[hid] = EXCLUDE[hid]
                continue
            title = clean_title(e["title"])
            kept.append({**e, "title": title})
            nid = node_id(key, e["notion_id"])
            n = by_id.get(nid)
            if n is None:
                dom, parent = place(key, title)
                assert parent in by_id, parent
                pdoms = by_id[parent]["domains"]
                by_id[nid] = {
                    "id": nid, "type": "term",
                    "title": {"ja": title, **({"en": e["title_en"]} if e.get("title_en") else {})},
                    "summary": e["definition"], "domains": [dom] + [d for d in pdoms if d != dom][:1],
                    "level": 4, "parent": parent, "time": None, "epistemic": "fact", "confidence": "medium",
                    "sources": [GLOSSARIES[key][0]], "verification": {"status": "unverified"},
                    "target_level": 1, "curriculum": [],
                    "origin": "user-note", "glossary": key, "note_kind": e.get("kind", "term"),
                    "history": [{"map_version": mapv, "change": "取り込み", "reason": f"あなたのNotionメモから（{today}、DOC-01 F11）"}],
                }
                counts["new"] += 1
                continue
            changed = []
            if n["title"]["ja"] != title:
                n["title"]["ja"] = title
                changed.append("名前")
            if e.get("title_en") and n["title"].get("en") != e["title_en"]:
                n["title"]["en"] = e["title_en"]
                changed.append("英語名")
            if n["summary"] != e["definition"]:
                n["summary"] = e["definition"]
                n["verification"] = {"status": "unverified"}   # 定義が変わったら検証し直す
                changed.append("定義")
            if changed:
                n.setdefault("history", []).append({"map_version": mapv, "change": "・".join(changed) + "を更新",
                                                    "reason": f"Notionの記述が変わった（{today}）"})
                counts["updated"] += 1
            else:
                counts["unchanged"] += 1
        # 公開する取り込み元ファイルには、除外したものを残さず、題名も表示用の名前にそろえる
        g["entries"] = kept
    imp["excluded"] = []

    nodes = sorted(by_id.values(), key=lambda n: n["id"])   # DOC-02 §3-1：IDの昇順
    (DATA / "graph" / "nodes.json").write_text(json.dumps(nodes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "sources.json").write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    imp_path.write_text(json.dumps(imp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    log_path = DATA / "import" / "notion_glossary_import_log.json"
    prev = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    ex = {**prev.get("excluded_ids", {}), **excluded}
    by_cat = {}
    for c in ex.values():
        by_cat[c] = by_cat.get(c, 0) + 1
    log = {"fetched_at": imp.get("fetched_at"), "term_nodes": sum(1 for n in nodes if n["type"] == "term"),
           "excluded_by_category": dict(sorted(by_cat.items())), "excluded_ids": dict(sorted(ex.items()))}
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"用語ノード：新規 {counts['new']}／更新 {counts['updated']}／変化なし {counts['unchanged']}、除外 {len(excluded)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
