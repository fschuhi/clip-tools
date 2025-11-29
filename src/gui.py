import tkinter as tk
from src.launcher_state import LauncherState


class LauncherApp:
    def __init__(self, options: list[str], on_select=None):
        self.state = LauncherState(options)
        self.on_select_callback = on_select

        # --- Main Window Setup ---
        self.root = tk.Tk()
        self.root.title("Launcher")

        # Compact / Mini-App Style
        self.bg_color = "#202020"
        self.fg_color = "#E0E0E0"
        self.font_ui = ("Menlo", 12)  # Small, readable fixed-width for input
        self.font_list = ("Menlo", 11)  # Even smaller for list

        self.root.configure(bg=self.bg_color)
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # --- Layout ---
        # Main container with padding
        self.main_frame = tk.Frame(self.root, bg=self.bg_color, padx=5, pady=5)
        self.main_frame.pack(fill="both", expand=True)

        # 1. Query Label (The Input Display)
        self.query_label = tk.Label(
            self.main_frame, text="Type to search...", font=self.font_ui, bg=self.bg_color, fg="#808080", anchor="w"
        )
        self.query_label.pack(fill="x", pady=(0, 5))

        # Separator (Thin line)
        tk.Frame(self.main_frame, bg="#404040", height=1).pack(fill="x", pady=(0, 5))

        # 2. Native Listbox
        # We use 'activestyle="none"' to avoid the underlined text on some platforms
        # 'highlightthickness=0' removes the focus border
        self.listbox = tk.Listbox(
            self.main_frame,
            font=self.font_list,
            bg=self.bg_color,
            fg=self.fg_color,
            selectbackground="#005fb8",  # Mac Blue
            selectforeground="#ffffff",
            highlightthickness=0,
            activestyle="none",
            borderwidth=0,
            height=5,  # Show roughly 5 items
        )
        self.listbox.pack(fill="both", expand=True)

        # --- Bindings ---
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Up>", lambda e: self.on_arrow("up"))
        self.root.bind("<Down>", lambda e: self.on_arrow("down"))

        # Initial Draw
        self.update_ui()
        self.center_window()
        self.force_focus()

    def center_window(self):
        self.root.update_idletasks()
        # Compact dimensions
        width = 250
        height = 140

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 3) - (height // 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def force_focus(self):
        self.root.lift()
        self.root.focus_force()
        try:
            self.root.tk.call("::tk::unsupported::MacWindowStyle", "style", self.root._w, "help", "none")
        except tk.TclError:
            pass

    def on_arrow(self, direction):
        self.state.handle_arrow(direction)
        self.update_ui()

    def on_key_press(self, event):
        keysym = event.keysym.lower()

        if keysym == "escape":
            self.root.quit()
            return

        if keysym == "return":
            selection = self.state.selection
            if selection and self.on_select_callback:
                self.on_select_callback(selection)
                self.root.quit()
            return

        if keysym == "backspace":
            self.state.handle_backspace()
            self.update_ui()
            return

        if len(event.char) == 1 and event.char.isprintable():
            self.state.handle_input(event.char)
            self.update_ui()

    def update_ui(self):
        # 1. Update Query Label
        if self.state.query:
            self.query_label.config(text=self.state.query, fg=self.fg_color)
        else:
            self.query_label.config(text="Type to search...", fg="#808080")

        # 2. Update Listbox Content
        self.listbox.delete(0, tk.END)

        for item in self.state.matches:
            display = "..." if item == "" else item
            self.listbox.insert(tk.END, " " + display)

            # 3. Update Selection
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(self.state.selection_index)
        self.listbox.activate(self.state.selection_index)
        self.listbox.see(self.state.selection_index)

    def run(self):
        self.root.mainloop()
