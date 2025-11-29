import pytest

# This will fail initially
from src.transformers.clean import clean_whitespace


def test_clean_basic_spacing():
    """Verify multiple spaces are collapsed and ends are trimmed."""
    input_text = "   This   has    too    many    spaces.   "
    expected = "This has too many spaces."
    assert clean_whitespace(input_text) == expected


def test_clean_windows_line_endings():
    """Verify CRLF are replaced by space."""
    input_text = "Line 1\r\nLine 2"
    expected = "Line 1 Line 2"
    assert clean_whitespace(input_text) == expected


def test_clean_smart_unwrapping():
    """
    Verify that single newlines are treated as spaces (unwrapping),
    but double newlines are preserved (paragraph breaks).
    """
    input_text = """The built-in macOS app switcher doesn't show window 
previews, but you can use AltTab (free, open-source). It
replaces Cmd+Tab with a Windows-style switcher showing 
actual window thumbnails instead of just app icons. 

So yes, you can get closer to this experience on macOS,
though it requires some tweaking and third-party tools."""

    expected = """The built-in macOS app switcher doesn't show window previews, but you can use AltTab (free, open-source). It replaces Cmd+Tab with a Windows-style switcher showing actual window thumbnails instead of just app icons.

So yes, you can get closer to this experience on macOS, though it requires some tweaking and third-party tools."""

    # Note: We strip the result to handle any final trailing newline variances
    assert clean_whitespace(input_text).strip() == expected.strip()
