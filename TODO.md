# TODO

## Learning Goals
- [ ] Learn how to read and diagnose Python tracebacks/error output.

## Backlog / Refactoring
- [ ] **Transformer (Clean):** Investigate edge cases where copying text from Markdown code blocks inserts extra `LF`, causing the regex to interpret lines as paragraphs. Refactor `clean_whitespace` to handle these "double-spaced" inputs.
- [ ] **Deployment:** Set up macOS Automator Quick Action (or Keyboard Maestro) to trigger `python -m src.main`.

## Development
- [ ] **Python Error Formatter:** Implement a transformer to wrap clipboard content (tracebacks) in Markdown code blocks.

## Completed
- [x] **Project Setup:** Infrastructure, Makefile, venv.
- [x] **Poe Transformer:** Logic and Tests.
- [x] **Architecture:** Implemented Dispatcher (`src/main.py`).
- [x] **GUI:** Implemented MVC-based Tkinter Launcher with searchable Listbox.
- [x] **GUI:** Added Arrow Key navigation.
- [x] **Transformer (Clean):** Initial implementation of `clean_whitespace`.
