#!/usr/bin/env bash
# PDF用の書体を準備する（DOC-03 §7、ADR-0005）。何度実行してもよい。
#  1) @fontsource（npm）から IBM Plex Mono と Zen Kaku Gothic New を .cache/fonts に取得（本文用）
#  2) IBM Plex Mono（欧文）を TTF に変換して ~/.local/share/fonts に入れる（Chrome のヘッダー・フッター用。
#     ヘッダー・フッターはページ内の @font-face を参照できないため、端末の書体として入れる）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.cache/fonts"
if [ ! -d "$DEST/node_modules/@fontsource/zen-kaku-gothic-new" ] || [ ! -f "$DEST/node_modules/@fontsource/ibm-plex-mono/300.css" ]; then
  mkdir -p "$DEST" && cd "$DEST"
  [ -f package.json ] || npm init -y >/dev/null
  npm install --silent --no-audit --no-fund @fontsource/zen-kaku-gothic-new @fontsource/ibm-plex-mono
  echo "fonts: installed to $DEST"
else
  echo "fonts: already installed"
fi
SYS="$HOME/.local/share/fonts/the-universal"
if ! fc-list | grep -q "IBM Plex Mono"; then
  python3 -c "import fontTools, brotli" 2>/dev/null || pip install --break-system-packages -q fonttools brotli
  mkdir -p "$SYS"
  python3 - "$DEST/node_modules/@fontsource/ibm-plex-mono/files" "$SYS" <<'PY'
import sys, glob, os
from fontTools.ttLib import TTFont
src, dst = sys.argv[1], sys.argv[2]
for w in ("300", "400", "500"):
    f = os.path.join(src, f"ibm-plex-mono-latin-{w}-normal.woff2")
    if os.path.exists(f):
        t = TTFont(f); t.flavor = None; t.save(os.path.join(dst, f"IBMPlexMono-{w}.ttf"))
PY
  fc-cache -f "$SYS" >/dev/null 2>&1 || true
  echo "fonts: IBM Plex Mono installed for header/footer"
fi
