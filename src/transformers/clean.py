import re


def clean_whitespace(text: str) -> str:
    """
    Cleans clipboard text by:
    1. Normalizing line endings.
    2. Preserving paragraph breaks (double newlines, even with spaces).
    3. Unwrapping hard-wrapped lines (single newlines -> space).
    4. Collapsing multiple spaces into one.
    """
    if not text:
        return ""

    # Normalize Windows line endings
    text = text.replace("\r\n", "\n")

    # Split by "Paragraph Breaks"
    # A paragraph break is 2 or more newlines, possibly with whitespace in between.
    # regex matches: Newline, 0-or-more whitespace chars, Newline
    paragraphs = re.split(r"\n\s*\n", text)

    cleaned_paragraphs = []
    for p in paragraphs:
        if not p.strip():
            continue
        # Join words with single spaces
        # This collapses all internal whitespace (newlines, tabs, multi-spaces)
        cleaned_p = " ".join(p.split())
        cleaned_paragraphs.append(cleaned_p)

    return "\n\n".join(cleaned_paragraphs)
