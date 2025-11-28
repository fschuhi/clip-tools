
# Clip Tools

Headless, keyboard-driven clipboard transformation utilities for macOS.

---

## Vision

Streamline the workflow of moving text between applications (e.g., LLMs to Obsidian, CLI to Docs) by:
- **Removing friction:** No manual editing of copied text.
- **Staying invisible:** No windows, no terminals—just keyboard shortcuts.
- **Enforcing consistency:** Standardized formatting for quotes, code blocks, and citations.

---

## Architecture Overview

The system follows a **Dispatcher Pattern**. A single entry point receives a command, reads the system clipboard, transforms the content, and writes it back.

'''mermaid
graph LR
    User[User Shortcut] -->|Triggers| A[macOS Automator]
    A -->|Executes| P[Python Script]
    P -->|Reads| C[Clipboard]
    P -->|Transforms| L[Logic Modules]
    L -->|Returns| P
    P -->|Writes| C
    C -->|Paste| User
'''

| Component | Role |
|---|---|
| **macOS Automator** | The "Headless" runner. Binds global hotkeys to shell scripts. |
| **`src/main.py`** | The **Dispatcher**. Parses arguments (e.g., `--poe`, `--clean`) and routes to the correct module. |
| **`src/transformers/`** | Pure logic modules (e.g., `poe.py`) that take string input and return string output. |
| **`pyperclip`** | Handles cross-platform clipboard I/O. |

### Project Navigation & Context

This project uses a curated "manifest" approach to manage context for AI collaboration.

* **[`manifest.lst`](manifest.lst)**: **Start here.** The single source of truth for the project structure.
* **`make filesdump`**: Generates a complete context dump for LLMs.

---

## Setup

### Requirements
- Python **3.11+**
- macOS (for Automator integration)

### Installation
'''bash
make setup
'''

---

## Usage (Development)

Currently, the tools can be run via CLI or tests.

'''bash
# Run tests
make test

# Future: Run manually (Draft)
python src/main.py --mode poe
'''

## Makefile Targets

'''bash
make setup          # Install dependencies and project
make test           # Run all tests
make clean          # Remove venv and cache
make filesdump      # Create context dump for LLMs
'''

---

## Current Status

| Feature | Status |
|---|---|
| Project Scaffolding | ✅ |
| **Poe.com Transformer** | ✅ (Logic & Tests) |
| CLI Dispatcher (`main.py`) | 🚧 Planned |
| Automator Integration | ⏳ Pending |
| Whitespace Remover | ⏳ Pending |

**Reference:** See [`Goals.md`](Goals.md) and [`TODO.md`](TODO.md) for the roadmap.
