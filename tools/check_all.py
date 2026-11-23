"""すべての自動テストを実行する（DOC-05 §1）。失敗があれば終了コード1。

使い方：python3 tools/check_all.py [--cycle content/cycles/NNNN] [--skip-pdf]
  --cycle を省略すると、state.json の cycle 番号のディレクトリを対象にする（0なら PDF 検査を省略）。
"""
import argparse
import subprocess
import sys

from common import ROOT, load

PY = sys.executable


def run(name, args):
    print(f"\n=== {name} ===", flush=True)
    r = subprocess.run([PY] + args, cwd=ROOT / "tools")
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cycle")
    ap.add_argument("--skip-pdf", action="store_true")
    a = ap.parse_args()
    ok = run("T-01〜T-05 データ検証", ["validate.py"])
    ok &= run("T-06 ビューア用データ", ["build_viewer_data.py"])
    cyc = a.cycle
    if not cyc:
        n = load("state.json")["cycle"]
        cyc = f"content/cycles/{n:04d}" if n else None
    if cyc and not a.skip_pdf:
        ok &= run(f"T-07〜T-10 PDF（{cyc}）", ["render_pdf.py", str(ROOT / cyc)])
    print("\ncheck_all:", "OK" if ok else "NG")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
