#!/usr/bin/env bash
#
# build.sh - Package the Mighty Vehicles addon into .mcaddon format
#
# Usage: ./build.sh
#
# Produces: build/MightyVehicles.mcaddon
#   (a zip containing MightyVehicles_BP.mcpack and MightyVehicles_RP.mcpack)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="$SCRIPT_DIR/build"
BP_DIR="$SCRIPT_DIR/MightyVehicles_BP"
RP_DIR="$SCRIPT_DIR/MightyVehicles_RP"
ADDON_NAME="MightyVehicles"

# Clean previous build
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "=== Building $ADDON_NAME.mcaddon ==="

# Increment patch version in both manifests
BP_MANIFEST="$BP_DIR/manifest.json"
RP_MANIFEST="$RP_DIR/manifest.json"

CURRENT_VERSION=$(grep -m1 '"version"' "$BP_MANIFEST" | sed 's/.*\[\s*\([0-9]*\),\s*\([0-9]*\),\s*\([0-9]*\)\s*\].*/\1.\2.\3/')
MAJOR=$(echo "$CURRENT_VERSION" | cut -d. -f1)
MINOR=$(echo "$CURRENT_VERSION" | cut -d. -f2)
PATCH=$(echo "$CURRENT_VERSION" | cut -d. -f3)

NEW_PATCH=$((PATCH + 1))
echo "Version: $MAJOR.$MINOR.$PATCH -> $MAJOR.$MINOR.$NEW_PATCH"

sed -i "s/\"version\": \[$MAJOR, $MINOR, $PATCH\]/\"version\": [$MAJOR, $MINOR, $NEW_PATCH]/g" "$BP_MANIFEST" "$RP_MANIFEST"

# Update version in pack descriptions
sed -i "s/Mighty Vehicles v$MAJOR\.$MINOR\.$PATCH/Mighty Vehicles v$MAJOR.$MINOR.$NEW_PATCH/g" "$BP_MANIFEST" "$RP_MANIFEST"

# Package Behavior Pack
echo "Packaging Behavior Pack..."
(cd "$BP_DIR" && zip -r "$BUILD_DIR/${ADDON_NAME}_BP.mcpack" . -x ".*")

# Package Resource Pack
echo "Packaging Resource Pack..."
(cd "$RP_DIR" && zip -r "$BUILD_DIR/${ADDON_NAME}_RP.mcpack" . -x ".*")

# Combine into .mcaddon
echo "Creating .mcaddon..."
(cd "$BUILD_DIR" && zip "$ADDON_NAME.mcaddon" "${ADDON_NAME}_BP.mcpack" "${ADDON_NAME}_RP.mcpack")

echo ""
echo "=== Build complete ==="
echo "Output: $BUILD_DIR/$ADDON_NAME.mcaddon"
ls -lh "$BUILD_DIR/$ADDON_NAME.mcaddon"
