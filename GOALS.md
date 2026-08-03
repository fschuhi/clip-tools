# clip-tools -- Goals and Roadmap

(Note: "I" in the following paragraphs refer to the user, "you" to you as the AI model.)

**Charter:** This file answers: where is the project going, in what order, and what happens next. It holds the strategic vision, the phased roadmap, and goals that need a strategy discussion before they are actionable. The _Current Session Pointer_ below is the single canonical "where we are / what's next" -- keep it to a few lines, update it, don't grow it; `FIRST_PROMPT.md` sends the reader here first. Concrete, startable work lives in `TODO.md`; the resolved-work record lives in `HISTORY.md` or `CHANGELOG.md`(on the heap, out of the per-session dump); architecture, contract, and settled decisions live in `README.md`.

---

## Traceback Tamer

- **Intent**: Create a transformer that wraps Python tracebacks/error output in Markdown code blocks for easy pasting into LLMs.
- **Why it matters**: When debugging with LLMs, raw stderr is hard to read and often loses formatting. A one-hotkey solution to "copy error → transform → paste to Claude" removes friction from the debugging workflow.
- **Design considerations**:
  1. Wrap content in triple-backtick code fence with `python` language hint
  2. Optionally strip sensitive paths (e.g., `/Users/frank/...` → `~/...`) - may be configurable
  3. Handle both single-error and chained exception tracebacks
- **Definition of done**: New `error.py` transformer registered in dispatcher; accessible via GUI and CLI; tests cover basic traceback formatting.
