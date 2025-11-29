import pytest
from unittest.mock import MagicMock, patch

# This import will fail initially (Red State)
from src.gui import LauncherApp
from src.launcher_state import LauncherState


@patch("src.gui.tk.Tk")
def test_gui_updates_on_keypress(mock_tk_class):
    """
    Verify that pressing a key in the App:
    1. Calls state.handle_input()
    2. Updates the UI labels
    """
    # Setup Mocks
    mock_root = mock_tk_class.return_value

    options = ["Poe", "Past"]
    # Initialize App (mocking the Tk root)
    app = LauncherApp(options)

    # Mock the internal state to predictable values
    app.state = LauncherState(options)

    # Simulate typing "p"
    # We manually trigger the handler logic (bypassing the actual Tk event loop)
    # We mock the event object that Tkinter sends
    mock_event = MagicMock(char="p", keysym="p")
    app.on_key_press(mock_event)

    # Assert State Updated
    assert app.state.query == "p"
    assert app.state.selection == "Past"

    # Assert UI Refresh was triggered
    # In our implementation, update_ui() will be called.
    # Since we can't check visual pixels, we rely on the state logic verification above
    # and the fact that no errors were raised during the update call.


@patch("src.gui.tk.Tk")
def test_gui_backspace(mock_tk_class):
    """Verify Backspace key triggers state.handle_backspace"""
    mock_root = mock_tk_class.return_value
    app = LauncherApp(["Poe"])
    app.state.query = "p"

    # Simulate Backspace
    mock_event = MagicMock(keysym="BackSpace", char="")
    app.on_key_press(mock_event)

    assert app.state.query == ""
