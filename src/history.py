# src/history.py

class BrowserHistory:
    def __init__(self):
        # Start with an empty list and index at -1 (no page loaded yet)
        self._history = []
        self._index = -1
# src/history.py

class BrowserHistory:
    def __init__(self):
        self._history = []
        self._current_index = None

    def visit(self, url: str):
        """Visit a new URL. Clears forward history if not at the tail."""
        if self._current_index is None:
            self._history = [url]
            self._current_index = 0
        else:
            # Truncate forward history if not at the end
            self._history = self._history[: self._current_index + 1]
            self._history.append(url)
            self._current_index += 1

    def current(self):
        """Return the current page URL, or None if empty."""
        if self._current_index is None:
            return None
        return self._history[self._current_index]

    def back(self):
        """Go back one page if possible, else stay."""
        if self._current_index is None:
            return None
        if self._current_index > 0:
            self._current_index -= 1
        return self._history[self._current_index]

    def forward(self):
        """Go forward one page if possible, else stay."""
        if self._current_index is None:
            return None
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
        return self._history[self._current_index]

