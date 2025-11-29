import argparse
import sys
import pyperclip
from src.transformers.poe import transform_poe_chat
from src.transformers.clean import clean_whitespace  # Import the new tool
from src.gui import LauncherApp

# Map Display Names (GUI) to Functions
TRANSFORMERS = {"Poe": transform_poe_chat, "Clean": clean_whitespace}  # Register it here


def run_gui():
    def on_select(selection):
        """Callback when user selects an item and hits Enter."""
        if selection in TRANSFORMERS:
            # 1. Read Clipboard
            text = pyperclip.paste()

            # 2. Transform
            func = TRANSFORMERS[selection]
            try:
                new_text = func(text)
                # 3. Write Clipboard
                pyperclip.copy(new_text)
                print(f"✅ Processed '{selection}'")
            except Exception as e:
                print(f"❌ Error processing '{selection}': {e}")

    # Initialize and run the app
    # We pass the list of keys (e.g., ["Poe", "Clean"]) to the launcher
    app = LauncherApp(list(TRANSFORMERS.keys()), on_select=on_select)
    app.run()


def main():
    parser = argparse.ArgumentParser(description="Clip Tools Dispatcher")

    # 'nargs="?"' makes the argument optional
    parser.add_argument("mode", nargs="?", choices=["poe"], help="The transformation mode to run (CLI)")

    args = parser.parse_args()

    # Dispatch Logic
    if args.mode is None:
        # No args? Run the Headless GUI
        run_gui()
    else:
        # Args present? Run CLI mode (legacy/scripting)
        text = pyperclip.paste()
        new_text = ""

        if args.mode == "poe":
            new_text = transform_poe_chat(text)

        pyperclip.copy(new_text)


if __name__ == "__main__":
    main()
