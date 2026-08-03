# clip-tools -- TODO

(Note: "I" in the following paragraphs refer to the user, "you" to you as the AI model.)

## Charter 

- Forward-looking only -- concrete, startable work: tasks specified well enough that next-session-me can begin within ten minutes, plus investigation items, test specs, and scratchpad ideas awaiting promotion or deletion.
- Items are unordered within their theme sections; open questions are marked _Needs investigation_ in the bullet.
- When an item is completed, record its durable outcome in `HISTORY.md` during the same session while the evidence and rationale are fresh, then strike it through in `TODO.md` with a concise handover note.
- Retain struck-through items through the next session because `TODO.md` is included in the standard filesdump while `HISTORY.md` normally is not; at the end of that next session, remove the already-archived items from `TODO.md`. Strategic direction, ordering, and milestones live in `GOALS.md` -- anything that needs a strategy discussion before it is actionable goes there.
- Architecture, contract, and settled decisions live in `README.md`.

---

## Educational

- **Grok Errors** - Learn how to read and diagnose Python tracebacks/error output.

## Transformers

- **Paragraph Boundaries** - Investigate edge cases in `clean.py` where copying text from Markdown code blocks inserts extra `LF`, causing the regex to interpret lines as paragraphs. Refactor to handle these "double-spaced" inputs.

- **Clip Tools Launcher.workflow clipboard corruption** - macOS Service injects `rm -rf` fragments into pasted text containing `!r` format specifiers. Check ~/Library/Services/, determine source, remove or disable.
