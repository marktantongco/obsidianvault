#!/bin/bash
# Obsidian Plugin Installer
# Run this script to install plugins manually

set -e

PLUGIN_DIR="$HOME/obsidianvault/.obsidian/plugins"
mkdir -p "$PLUGIN_DIR"

echo "=== Obsidian Plugin Installer ==="
echo ""

# Function to install a plugin
install_plugin() {
    local name="$1"
    local repo="$2"
    local dir="$PLUGIN_DIR/$name"
    
    echo "Installing $name..."
    
    # Create plugin directory
    mkdir -p "$dir"
    
    # Get latest release
    echo "  Getting latest release..."
    local tag=$(curl -fsSL "https://api.github.com/repos/$repo/releases/latest" 2>/dev/null | grep -o '"tag_name":"[^"]*"' | cut -d'"' -f4)
    
    if [ -z "$tag" ]; then
        echo "  ⚠️  Could not get latest version, trying main branch..."
        # Try to download from main branch
        curl -fsSL "https://raw.githubusercontent.com/$repo/main/manifest.json" -o "$dir/manifest.json" 2>/dev/null || true
        curl -fsSL "https://raw.githubusercontent.com/$repo/main/main.js" -o "$dir/main.js" 2>/dev/null || true
    else
        echo "  Version: $tag"
        # Download release assets
        local zip_url="https://github.com/$repo/releases/download/$tag/$name.zip"
        curl -fsSL "$zip_url" -o "/tmp/$name.zip" 2>/dev/null || {
            echo "  ⚠️  Zip download failed, trying individual files..."
            curl -fsSL "https://raw.githubusercontent.com/$repo/main/manifest.json" -o "$dir/manifest.json" 2>/dev/null || true
            curl -fsSL "https://raw.githubusercontent.com/$repo/main/main.js" -o "$dir/main.js" 2>/dev/null || true
        }
        
        if [ -f "/tmp/$name.zip" ]; then
            unzip -o "/tmp/$name.zip" -d "$dir" 2>/dev/null
            rm -f "/tmp/$name.zip"
        fi
    fi
    
    # Check if main.js exists
    if [ -f "$dir/main.js" ]; then
        echo "  ✅ $name installed successfully"
    else
        echo "  ⚠️  $name needs manual installation"
    fi
    
    sleep 5  # Rate limiting protection
}

# Install plugins
install_plugin "calendar" "liamcain/obsidian-calendar-plugin"
install_plugin "templater-obsidian" "silentvoid13/Templater"
install_plugin "dataview" "blacksmithgu/obsidian-dataview"
install_plugin "obsidian-kanban" "obsidian-community/obsidian-kanban"
install_plugin "obsidian-excalidraw-plugin" "zsviczian/obsidian-excalidraw-plugin"
install_plugin "obsidian-tasks-plugin" "obsidian-tasks-group/obsidian-tasks"

echo ""
echo "=== Installation Complete ==="
echo ""
echo "Check which plugins are installed:"
ls -la "$PLUGIN_DIR"
echo ""
echo "If some plugins failed, install them manually through Obsidian:"
echo "1. Open Obsidian"
echo "2. Go to Settings → Community Plugins"
echo "3. Click Browse"
echo "4. Search for each plugin name"
echo "5. Click Install then Enable"
