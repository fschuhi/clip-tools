import pytest
from src.launcher_state import LauncherState


def test_launcher_initialization_safe_start():
    """Verify initial state has dummy item at top."""
    options = ["Poe", "Past"]
    state = LauncherState(options)
    assert state.matches == ["", "Past", "Poe"]
    assert state.selection_index == 0
    assert state.selection is None


def test_valid_input_auto_selects_first_match():
    """Input: 'p' -> Matches ['', 'Past', 'Poe'] -> Selection 'Past'"""
    state = LauncherState(["Poe", "Past"])
    state.handle_input("p")
    assert state.selection_index == 1
    assert state.selection == "Past"


def test_backspace_logic_partial():
    """'po' -> 'p' (Should stay on best match)"""
    state = LauncherState(["Poe", "Past"])
    state.handle_input("p")
    state.handle_input("o")  # Selection is Poe

    state.handle_backspace()  # Back to 'p'
    assert state.query == "p"
    assert state.selection == "Past"


def test_backspace_to_empty_resets_selection():
    """
    User Bug Report:
    'p' -> Selects 'Poe'
    Backspace -> Empty.
    EXPECTED: Selection should reset to index 0 (Dummy), NOT stay on 'Poe'.
    """
    state = LauncherState(["Poe"])
    state.handle_input("p")
    assert state.selection == "Poe"  # Index 1

    state.handle_backspace()
    assert state.query == ""
    # This was failing before (was 1)
    assert state.selection_index == 0
    assert state.selection is None
