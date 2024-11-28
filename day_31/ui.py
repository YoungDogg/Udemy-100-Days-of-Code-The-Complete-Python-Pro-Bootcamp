import tkinter as tk
from tkinter import messagebox


class FlashCardUI:
    """UI for flash card"""

    LABEL_STYLE = {"font": ("Arial", 20, "bold"), "bg": "#4FC4B7", "fg": "white"}
    BUTTON_STYLE = {"font": ("Arial", 20, "bold"), "bg": "#38E2D6"}

    def __init__(self):
        self._root = tk.Tk()
        self._x_command = None
        self._check_command = None
        self._setup_root()
        self._setup_layout()

    def _setup_root(self):
        """Initializes the main window and its grid layout."""
        self._root.title("Flash Card")
        self._root.config(bg="#38E2D6")  # Background color
        self._root.geometry("500x300")  # Set a fixed window size

        # Configure grid layout
        for col in range(3):
            self._root.grid_columnconfigure(col, weight=1)
        for row in range(3):
            self._root.grid_rowconfigure(row, weight=1)

    def _setup_layout(self):
        """Sets up the flash card layout."""
        # Central box with text
        box_frame = tk.Frame(self._root, bg="#4FC4B7", bd=0)
        box_frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)

        tk.Label(box_frame, text="English", **self.LABEL_STYLE).pack()
        tk.Label(box_frame, text="Request", **self.LABEL_STYLE).pack()

        # Red 'X' in the bottom left
        tk.Button(
            self._root, text="X", fg="red", command=self._x_command, **self.BUTTON_STYLE
        ).grid(row=2, column=0, sticky="w", padx=40, pady=10)

        # Green checkmark in the bottom right
        tk.Button(
            self._root, text="✔", fg="green", command=self._check_command, **self.BUTTON_STYLE
        ).grid(row=2, column=2, sticky="e", padx=40, pady=10)

    def _set_command(self, command_name, command):
        """Generic method to set a command."""
        if command:
            setattr(self, command_name, command)
        else:
            messagebox.showerror(message=f"{command_name} is not set.")

    def _setup_x_button(self, command):
        """Sets the X button command."""
        self._set_command('_x_command', command)

    def _setup_check_button(self, command):
        """Sets the check button command."""
        self._set_command('_check_command', command)

    @property
    def root(self):
        """Returns the root Tkinter window."""
        return self._root


if __name__ == '__main__':
    ui = FlashCardUI()
    ui.root.mainloop()
