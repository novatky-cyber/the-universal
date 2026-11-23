"""ビューアのスクリーンショット確認（DOC-05 R-03）。

使い方：python3 tools/screenshot_viewer.py [出力先ディレクトリ] [--three-local /path/to/node_modules/three]
  - リポジトリをローカルHTTPで配信し、iPhone相当（390×844）とiPad相当（820×1180）で撮影する。
  - CDNに接続できない環境では --three-local で three.js のローカルコピーに差し替える。
  - コンソールのエラーを表示し、エラーがあれば終了コード1。
"""
import argparse
import functools
import http.server
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CDN = "https://cdn.jsdelivr.net/npm/three@0.160.0/"


def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    h.func.log_message = lambda *a, **k: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", nargs="?", default=str(ROOT / "output" / "debug" / "viewer"))
    ap.add_argument("--three-local")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    srv = serve()
    base = f"http://127.0.0.1:{srv.server_address[1]}/index.html"
    errors = []
    shots = [("iphone", 390, 844, ""), ("iphone_node", 390, 844, "#con.entropy"), ("ipad", 820, 1180, "#evd.cmb")]
    with sync_playwright() as p:
        exe = "/usr/bin/google-chrome" if Path("/usr/bin/google-chrome").exists() else None
        b = p.chromium.launch(executable_path=exe, args=["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"])
        for name, w, h, hash_ in shots:
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2, is_mobile=True, has_touch=True)
            pg = ctx.new_page()
            if a.three_local:
                local = Path(a.three_local)
                pg.route(CDN + "**", lambda route: route.fulfill(
                    path=str(local / route.request.url[len(CDN):]), content_type="application/javascript"))
            pg.on("console", lambda m: errors.append(f"{name}: {m.text}") if m.type == "error" else None)
            pg.on("pageerror", lambda e: errors.append(f"{name}: {e}"))
            pg.goto(base + hash_)
            pg.wait_for_timeout(3500)
            pg.screenshot(path=str(out / f"{name}.png"))
            ctx.close()
        b.close()
    srv.shutdown()
    for e in errors:
        print("ERROR", e)
    print("screenshot_viewer:", "NG" if errors else "OK", "->", out)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
