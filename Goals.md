# Project Goals

## 1. Poe to Obsidian Transformer
**Goal:** Convert "User/Assistant" conversation blocks from Poe.com into Obsidian-friendly formatting.
- [x] Parse `User:` and `Assistant:` blocks.
- [x] Convert `User:` segments into `> [!note]` callouts.
- [x] Quote all lines within the User segment.
- [x] Preserve Assistant text as-is.

## 2. Whitespace Remover (AHK Equivalent)
**Goal:** Clean up clipboard text (e.g., from PDF or CLI output) by removing unnecessary whitespace and line breaks.
- [x] Replace `\r\n` (Windows line endings) with space (context dependent).
- [x] Remove leading/trailing whitespace.
- [x] Collapse multiple spaces into single spaces.
- [x] Handle "smart" joining of lines.
*(Note: Refactoring required for code-block edge cases)*

## 3. Headless Execution
**Goal:** Run these tools via keyboard shortcut with minimal UI.
- [x] Implement `src/main.py` dispatcher.
- [x] Create lightweight "Launcher" GUI (Tkinter) with search filtering.
- [ ] Configure macOS Automator / Keyboard Maestro triggers.

## 4. Python Error Formatter
**Goal:** Easily copy/paste Python stderr/traceback output to LLMs.
- [ ] Format clipboard content (error logs) into Markdown code blocks (`'''`).
- [ ] Potentially strip sensitive paths or environment variables (optional).
