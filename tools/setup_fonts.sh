#!/usr/bin/env bash
# PDF用の書体を @fontsource（npm）から .cache/fonts に取得する（DOC-03 §7、ADR-0004）。
# 何度実行してもよい。取得済みなら何もしない。
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.cache/fonts"
if [ -d "$DEST/node_modules/@fontsource/zen-kaku-gothic-new" ]; then echo "fonts: already installed"; exit 0; fi
mkdir -p "$DEST" && cd "$DEST"
[ -f package.json ] || npm init -y >/dev/null
npm install --silent --no-audit --no-fund \
  @fontsource/zen-kaku-gothic-new @fontsource/shippori-mincho-b1 @fontsource/ibm-plex-mono @fontsource/instrument-serif
echo "fonts: installed to $DEST"
