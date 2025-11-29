# Goals

Strategic work that shapes capabilities and architecture. Each goal has intent, rationale, and definition of done. See also [`TODO.md`](TODO.md) for tactical quick-wins.

---

## Traceback Tamer

- **Intent**: Create a transformer that wraps Python tracebacks/error output in Markdown code blocks for easy pasting into LLMs.
- **Why it matters**: When debugging with LLMs, raw stderr is hard to read and often loses formatting. A one-hotkey solution to "copy error → transform → paste to Claude" removes friction from the debugging workflow.
- **Design considerations**:
  1. Wrap content in triple-backtick code fence with `python` language hint
  2. Optionally strip sensitive paths (e.g., `/Users/frank/...` → `~/...`) - may be configurable
  3. Handle both single-error and chained exception tracebacks
- **Definition of done**: New `error.py` transformer registered in dispatcher; accessible via GUI and CLI; tests cover basic traceback formatting.
