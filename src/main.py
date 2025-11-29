import argparse
import sys
import pyperclip
from src.transformers.poe import transform_poe_chat


def main():
    parser = argparse.ArgumentParser(description="Clip Tools Dispatcher")

    # We define the available modes here.
    # As we add new tools (like 'clean'), we just add them to this list.
    parser.add_argument("mode", choices=["poe"], help="The transformation mode to run")

    args = parser.parse_args()

    # 1. Read Clipboard
    text = pyperclip.paste()

    # 2. Transform based on mode
    new_text = ""
    if args.mode == "poe":
        new_text = transform_poe_chat(text)

    # 3. Write Clipboard
    pyperclip.copy(new_text)


if __name__ == "__main__":
    main()
