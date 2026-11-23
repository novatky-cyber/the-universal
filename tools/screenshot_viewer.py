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
    ap.add_argument("--fonts-local", help="@fontsource のディレクトリ（Google Fonts の代わりに使う）")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    srv = serve()
    base = f"http://127.0.0.1:{srv.server_address[1]}/index.html"
    errors = []
    # (名前, 幅, 高さ, ハッシュまたは ?menu=節, 端末に保存された設定)
    D, L, P = {"theme": "dark"}, {"theme": "light"}, {"theme": "light", "view": "plane"}
    shots = [("iphone", 390, 844, "", D), ("iphone_node", 390, 844, "#con.entropy", D), ("ipad", 820, 1180, "#evd.cmb", D),
             ("iphone_menu", 390, 844, "?menu=index", D), ("desktop", 1440, 900, "", D),
             ("iphone_light", 390, 844, "", L), ("iphone_light_node", 390, 844, "#con.entropy", L),
             ("iphone_plane", 390, 844, "", P), ("desktop_plane", 1440, 900, "", {"theme": "dark", "view": "plane"}),
             ("iphone_settings", 390, 844, "?menu=settings", L)]
    with sync_playwright() as p:
        exe = "/usr/bin/google-chrome" if Path("/usr/bin/google-chrome").exists() else None
        b = p.chromium.launch(executable_path=exe, args=["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"])
        for name, w, h, hash_, prefs in shots:
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2, is_mobile=True, has_touch=True)
            ctx.add_init_script("".join(f"localStorage.setItem('tu.{k}', '{v}');" for k, v in prefs.items()))
            pg = ctx.new_page()
            if a.three_local:
                local = Path(a.three_local)
                pg.route(CDN + "**", lambda route: route.fulfill(
                    path=str(local / route.request.url[len(CDN):]), content_type="application/javascript"))
            if a.fonts_local:
                fl = Path(a.fonts_local)
                css = []
                for pkg, ws in [("zen-kaku-gothic-new", ["400", "500", "700"]), ("ibm-plex-mono", ["300", "400", "500"])]:
                    for w in ws:
                        f = fl / pkg / f"{w}.css"
                        if f.exists():
                            css.append(f.read_text().replace("url(./files/", f"url(https://fonts.local/{pkg}/files/"))
                body = "\n".join(css)
                pg.route("https://fonts.googleapis.com/**", lambda route: route.fulfill(body=body, content_type="text/css"))
                pg.route("https://fonts.local/**", lambda route: route.fulfill(
                    path=str(fl / route.request.url[len("https://fonts.local/"):]), content_type="font/woff2"))
            pg.on("console", lambda m: errors.append(f"{name}: {m.text}") if m.type == "error" else None)
            pg.on("pageerror", lambda e: errors.append(f"{name}: {e}"))
            if hash_.startswith("?menu="):
                pg.goto(base)
                pg.wait_for_timeout(3000)
                pg.click("#btn-menu")
                pg.wait_for_timeout(300)
                pg.click(f"[data-sec={hash_.split('=')[1]}]")
                pg.wait_for_timeout(600)
            else:
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
