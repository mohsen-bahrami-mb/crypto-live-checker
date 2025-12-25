#!/bin/bash
# Build script for crypto-check executable on macOS

set -e

echo "🔨 Building crypto-check for macOS..."

# Clean previous builds
rm -rf build dist *.spec

# Install dependencies if needed
pipenv install --dev pyinstaller 2>/dev/null || true

# Build macOS executable
pipenv run pyinstaller main.py \
    --onefile \
    --name crypto-check \
    --icon=app_icon.icns 2>/dev/null || pipenv run pyinstaller main.py \
    --onefile \
    --name crypto-check

# Create macOS app bundle (optional - makes it more like a native app)
echo ""
echo "✅ macOS executable built successfully!"
@@echo "📍 Location: dist/crypto-check"
@@
@@# Detect OS
@@OS_TYPE=$(uname -s)
@@echo "🖥️  Built for: $OS_TYPE"
@@
@@echo ""
@@echo "To run the app:"
@@echo "  ./dist/crypto-check <symbol> [limit]"
@@echo ""
@@echo "Example:"
@@echo "  ./dist/crypto-check btcusdt"
