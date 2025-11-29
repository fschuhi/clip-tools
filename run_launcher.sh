#!/bin/bash

# =============================================================================
# Clip Tools Launcher
# =============================================================================
# Self-locating script that activates the venv and runs the GUI launcher.
# Can be invoked from anywhere (Automator, Keyboard Maestro, Terminal, etc.)
# =============================================================================

# Get the directory where this script lives (= project root)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Activate the virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Run the launcher from the project directory
cd "$SCRIPT_DIR"
python -m src.main
