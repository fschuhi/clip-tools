class LauncherState:
    def __init__(self, options: list[str]):
        # We sort options to ensure consistent behavior (e.g. "Clean" before "Past")
        self.options = sorted(options)
        self.query = ""
        self.matches = self.options.copy()
        self.selection: str | None = None

    def handle_input(self, char: str) -> bool:
        """
        Processes a new character input.
        Returns True if the input was accepted (matches a prefix), False otherwise.
        """
        new_query = self.query + char

        # Filter matches based on the new query (case-insensitive prefix match)
        new_matches = [opt for opt in self.options if opt.lower().startswith(new_query.lower())]

        if not new_matches:
            # Reject input if it leads to no matches
            return False

        # Accept input
        self.query = new_query
        self.matches = new_matches

        # Auto-select the first match (alphabetical)
        self.selection = self.matches[0]
        return True

    def handle_backspace(self):
        """
        Removes the last character from the query.
        """
        if not self.query:
            return

        self.query = self.query[:-1]

        if not self.query:
            # Revert to Safe State
            self.matches = self.options.copy()
            self.selection = None
        else:
            # Re-calculate matches for the shorter query
            self.matches = [opt for opt in self.options if opt.lower().startswith(self.query.lower())]
            # Auto-select the first match
            self.selection = self.matches[0]
