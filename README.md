# Clip Tools

Headless, keyboard-driven clipboard transformation utilities for macOS.

---

## Vision

Streamline the workflow of moving text between applications (e.g., LLMs to Obsidian, CLI to Docs) by:
- **Removing friction:** No manual editing of copied text.
- **Staying invisible:** No windows, no terminals—just keyboard shortcuts.
- ** enforcing consistency:** Standardized formatting for quotes, code blocks, and citations.

---

## Architecture Overview

The system follows a **Dispatcher Pattern**. A single entry point receives a command, reads the system clipboard, transforms the content, and writes it back.

```mermaid
graph LR
    User[User Shortcut] -->|Triggers| A[macOS Automator]
    A -->|Executes| P[Python Script]
    P -->|Reads| C[Clipboard]
    P -->|Transforms| L[Logic Modules]
    L -->|Returns| P
    P -->|Writes| C
    C -->|Paste| User
