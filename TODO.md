# TODO

Tactical scratchpad for quick fixes, small refactors, and tasks under ~1 hour. For strategic work with intent/rationale/definition of done, see [`Goals.md`](Goals.md).

---

## Educational

- **Grok Errors** - Learn how to read and diagnose Python tracebacks/error output.

## Transformers

- **Paragraph Boundaries** - Investigate edge cases in `clean.py` where copying text from Markdown code blocks inserts extra `LF`, causing the regex to interpret lines as paragraphs. Refactor to handle these "double-spaced" inputs.

- **Clip Tools Launcher.workflow clipboard corruption** - macOS Service injects `rm -rf` fragments into pasted text containing `!r` format specifiers. Check ~/Library/Services/, determine source, remove or disable.
