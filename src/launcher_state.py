class LauncherState:
    def __init__(self, options: list[str]):
        # We add an empty option at the top to serve as the "Safe Start" state
        # The user provided options are sorted below it
        self.options = [""] + sorted(options)

        self.query = ""
        self.matches = self.options.copy()

        # Selection starts at the top (the empty safe option)
        self.selection_index = 0

    @property
    def selection(self) -> str | None:
        """Returns the currently selected string, or None if it's the dummy item."""
        if not self.matches:
            return None

        item = self.matches[self.selection_index]
        return item if item != "" else None

    def handle_input(self, char: str) -> bool:
        """
        Processes a new character input.
        Returns True if the input led to valid matches, False otherwise.
        """
        new_query = self.query + char

        # Filter: Always keep the dummy item [""] + matches
        # We filter the *original options* (excluding the dummy at index 0)
        raw_matches = [opt for opt in self.options[1:] if opt.lower().startswith(new_query.lower())]

        if not raw_matches:
            return False

        self.query = new_query
        self.matches = [""] + raw_matches

        # Auto-select the first *real* match (index 1), if available
        if len(self.matches) > 1:
            self.selection_index = 1
        else:
            self.selection_index = 0

        return True

    def handle_backspace(self):
        """Removes the last character from the query."""
        if not self.query:
            return

        self.query = self.query[:-1]

        # Re-calculate matches
        raw_matches = [opt for opt in self.options[1:] if opt.lower().startswith(self.query.lower())]
        self.matches = [""] + raw_matches

        if self.query == "":
            # If we backspaced to empty, RESET to Safe State (Index 0)
            self.selection_index = 0
        elif len(self.matches) > 1:
            # If we still have query text, select the best match
            self.selection_index = 1
        else:
            self.selection_index = 0

    def handle_arrow(self, direction: str):
        """
        Moves selection index 'up' or 'down'.
        """
        if not self.matches:
            return

        if direction == "up":
            self.selection_index = max(0, self.selection_index - 1)
        elif direction == "down":
            self.selection_index = min(len(self.matches) - 1, self.selection_index + 1)
