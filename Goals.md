# Project Goals

## 1. Poe to Obsidian Transformer
**Goal:** Convert "User/Assistant" conversation blocks from Poe.com into Obsidian-friendly formatting.
- [ ] Parse `User:` and `Assistant:` blocks.
- [ ] Convert `User:` segments into `> [!note]` callouts.
- [ ] Quote all lines within the User segment.
- [ ] Preserve Assistant text as-is.

## 2. Whitespace Remover (AHK Equivalent)
**Goal:** Clean up clipboard text (e.g., from PDF or CLI output) by removing unnecessary whitespace and line breaks.
- [ ] Replace `\r\n` (Windows line endings) with space (context dependent).
- [ ] Remove leading/trailing whitespace.
- [ ] Collapse multiple spaces into single spaces.
- [ ] Handle "smart" joining of lines (e.g., un-breaking lines copied from a terminal).

## 3. Headless Execution
**Goal:** Run these tools via keyboard shortcut without opening a terminal window.
- [ ] Implement `main.py` entry point.
- [ ] Configure macOS Automator Quick Actions.

## 4. Python Error Formatter
**Goal:** Easily copy/paste Python stderr/traceback output to LLMs.
- [ ] Format clipboard content (error logs) into Markdown code blocks (` ``` `).
- [ ] Potentially strip sensitive paths or environment variables (optional).
