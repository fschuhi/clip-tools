import pytest

# This import will fail first (Red State)
from src.launcher_state import LauncherState


def test_launcher_initialization_safe_start():
    """
    Verify initial state:
    - Query is empty
    - Matches contain all options
    - Selection is None (Safety feature: Enter key does nothing)
    """
    options = ["Poe", "Past", "Clean"]
    state = LauncherState(options)

    assert state.query == ""
    # Should be sorted alphabetically so 'Clean' -> 'Past' -> 'Poe'
    assert state.matches == ["Clean", "Past", "Poe"]
    assert state.selection is None


def test_valid_input_filtering():
    """
    User Scenario:
    Options: ["Poe", "Past"]
    1. Input: "p" -> Matches both, selects "Past" (alphabetical)
    2. Input: "o" -> Matches "Poe"
    """
    state = LauncherState(["Poe", "Past"])

    # 1. User presses 'p' (case insensitive match)
    success = state.handle_input("p")
    assert success is True
    assert state.query == "p"
    assert state.matches == ["Past", "Poe"]
    assert state.selection == "Past"

    # 2. User presses 'o'
    success = state.handle_input("o")
    assert success is True
    assert state.query == "po"
    assert state.matches == ["Poe"]
    assert state.selection == "Poe"


def test_invalid_input_rejected():
    """
    User Scenario:
    Input: "p" -> Valid
    Input: "e" -> Invalid (No option starts with "pe")
    """
    state = LauncherState(["Poe", "Past"])
    state.handle_input("p")

    # Pressing 'e' should return False and NOT update state
    success = state.handle_input("e")
    assert success is False
    assert state.query == "p"
    assert state.matches == ["Past", "Poe"]


def test_backspace_behavior():
    """
    User Scenario:
    Input: "po" -> Selection "Poe"
    Backspace -> "p" -> Selection "Past"
    """
    state = LauncherState(["Poe", "Past"])
    state.handle_input("p")
    state.handle_input("o")

    # Verify we are at "po"
    assert state.query == "po"

    # Backspace
    state.handle_backspace()
    assert state.query == "p"
    assert state.matches == ["Past", "Poe"]
    assert state.selection == "Past"


def test_backspace_to_empty_safety():
    """
    User Scenario:
    Input: "p" -> Selection "Past"
    Backspace -> "" -> Selection None (Safe State)
    """
    state = LauncherState(["Poe", "Past"])
    state.handle_input("p")

    state.handle_backspace()
    assert state.query == ""
    assert state.matches == ["Past", "Poe"]
    assert state.selection is None


def test_empty_options_edge_case():
    """
    Edge Case: No options available.
    State should remain locked in Safe State.
    """
    state = LauncherState([])

    assert state.selection is None
    assert state.matches == []

    # Input should be rejected
    success = state.handle_input("a")
    assert success is False
    assert state.query == ""
    assert state.selection is None
