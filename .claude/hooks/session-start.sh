#!/bin/bash
# Anna (AI Construction Assistant) — SessionStart hook.
#
# 1. PDF toolkit (group standard — same block as every Fishbone KB repo).
# 2. Composio CLI, pinned, so unattended routine runs can use Anna's own
#    Composio connections (anna-gmail, anna-gmail-properties, anna-gmail-ops,
#    anna-googledrive) without a browser.
#
# COMPOSIO_API_KEY comes from the Anna environment's variables (set by
# Minda); it is never written to this repo or printed.
#   ck_...  consumer key -> used by the Composio Connect MCP server declared
#           in .mcp.json; the CLI stays signed out (expected).
#   uak_... user key     -> the CLI signs in with it (fallback path).
#   unset   -> CLI installed but not signed in; native connectors only.
#
# Idempotent, non-interactive, web/remote sessions only. Never aborts the
# session.
set -uo pipefail

# Web/remote sessions only — do nothing on a local machine.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# --- OCR engine + PDF rasteriser (system packages; best-effort, needs sudo) ---
if ! command -v tesseract >/dev/null 2>&1 || ! command -v pdftoppm >/dev/null 2>&1; then
  if command -v sudo >/dev/null 2>&1 && command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update -qq 2>/dev/null || true
    sudo apt-get install -y -qq tesseract-ocr poppler-utils >/dev/null 2>&1 \
      || echo "session-start: tesseract/poppler not installed — OCR of scanned PDFs may be unavailable" >&2
  fi
fi

# --- Python PDF libraries (text, tables, rendering, OCR bindings) ---
pip install --quiet pdfplumber pymupdf pdf2image pytesseract pillow pypdf \
  || echo "session-start: pip install of PDF libraries failed" >&2

# --- Composio CLI (pinned) ---
COMPOSIO_VERSION="0.4.1"
COMPOSIO_ORG="minda_workspace"
COMPOSIO_BIN="$HOME/.local/bin/composio"
if [ "$("$COMPOSIO_BIN" --version 2>/dev/null)" != "$COMPOSIO_VERSION" ]; then
  curl -fsSL https://composio.dev/install | sh -s -- "@composio/cli@${COMPOSIO_VERSION}" >/dev/null 2>&1 || true
fi
if [ ! -x "$COMPOSIO_BIN" ]; then
  echo "session-start: composio CLI not installed" >&2
else
  if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
  fi
  # --- Composio sign-in from the environment's API key (no browser) ---
  if "$COMPOSIO_BIN" whoami 2>/dev/null | grep -q '"email"'; then
    :  # already signed in
  elif [ "${COMPOSIO_API_KEY:0:3}" = "ck_" ]; then
    # Consumer key: used by the Composio Connect MCP server in .mcp.json
    # (x-consumer-api-key header), not for CLI sign-in. Nothing to do here.
    :
  elif [ -n "${COMPOSIO_API_KEY:-}" ]; then
    "$COMPOSIO_BIN" login --user-api-key "$COMPOSIO_API_KEY" --org "$COMPOSIO_ORG" \
      -y --no-skill-install >/dev/null 2>&1 || true
    "$COMPOSIO_BIN" whoami 2>/dev/null | grep -q '"email"' \
      || echo "session-start: composio sign-in with COMPOSIO_API_KEY failed — native connectors only this run" >&2
  else
    echo "session-start: COMPOSIO_API_KEY not set — composio installed but not signed in" >&2
  fi
fi

exit 0
