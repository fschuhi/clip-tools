import sys
from unittest.mock import patch
import pytest

# Note: This import will fail initially because src.main doesn't exist yet
from src.main import main


def test_main_poe_mode():
    """
    Verifies that running 'main.py poe' correctly:
    1. Reads from clipboard (mocked)
    2. Transforms the text using the poe transformer
    3. Writes back to clipboard (mocked)
    """
    # Test Data
    input_text = """User:
Testing
Assistant:
Response"""

    expected_output = """> [!note] User:
> Testing
Assistant:
Response"""

    # We use 'patch' to replace real system calls with fake ones
    # 1. sys.argv: Simulates command line arguments ["main.py", "poe"]
    # 2. pyperclip.paste: Returns our test input instead of real clipboard
    # 3. pyperclip.copy: Captures the output instead of writing to real clipboard
    with (
        patch("sys.argv", ["main.py", "poe"]),
        patch("src.main.pyperclip.paste", return_value=input_text) as mock_paste,
        patch("src.main.pyperclip.copy") as mock_copy,
    ):
        # Execute the main function
        main()

        # Assertions
        mock_paste.assert_called_once()
        mock_copy.assert_called_once_with(expected_output)


def test_main_unknown_mode():
    """Verifies that the script handles unknown modes gracefully."""
    with patch("sys.argv", ["main.py", "unknown_mode"]), pytest.raises(SystemExit):  # argparse usually exits on error

        main()
