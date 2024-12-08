import tkinter as tk
from tkinter import ttk
import logging

logging.basicConfig(level=logging.ERROR, filename="ui_errors.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

class UI:
    """
    UI class to create and manage a graphical user interface.

    Attributes:
        _window: The main application window.
        _card: A dictionary representing the card with text in different languages.
        _v_button: The ✅ button for marking check actions.
        _x_button: The ❌ button for marking dismiss actions.
        _v_btn_command: A callback for the ✅ button click.
        _x_btn_command: A callback for the ❌ button click.
    """

    def __init__(self):
        """
        Initializes the UI class attributes without assigning them values.
        """
        self._window = None
        self._card = None
        self._v_button = None
        self._x_button = None
        self._v_btn_command = None
        self._x_btn_command = None

    def set_up(self):
        """
        Sets up the UI by initializing the main components.
        Calls private methods for creating root, card, and buttons.
        """
        try:
            self._set_root()
            self._configure_styles()
            self._set_card()
            self._set_v_button()
            self._set_x_button()
        except Exception as e:
            logging.error(f"Error during UI setup: {e}")
            raise

    def _set_root(self):
        """
        Configures the root window with a dynamic size and grid layout.
        """
        try:
            self._window = tk.Tk()
            self._window.title("Flash Card UI")
            self._window.geometry("800x600")
            self._window.rowconfigure(0, weight=1)
            self._window.columnconfigure(0, weight=1)
        except Exception as e:
            logging.error(f"Error setting up root window: {e}")
            raise


    @staticmethod
    def _configure_styles():
        """
        Configures styles for the UI components.
        """
        style = ttk.Style()
        # Style for the card
        style.configure(
            "Card.TLabel",
            font=("Arial", 24),
            background="white",
            foreground="black",
            relief="groove",
        )
        # Style for buttons
        style.configure(
            "TButton",
            font=("Arial", 14),
            padding=10,
        )

    def _set_card(self):
        """
        Creates a clickable card widget with a flip functionality.
        """
        self._card = ttk.Label(
            self._window,
            text="Hello",
            style="Card.TLabel",
            anchor="center",
        )
        self._card.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # Bind click event to the card for flipping
        self._card.bind("<Button-1>", lambda event: self.flip_card())

    def _set_v_button(self):
        """
        Creates and configures the ✅ button with a command callback.
        """
        self._v_button = ttk.Button(self._window, text="✅", style="TButton", command=self.v_btn_command)
        self._v_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def _set_x_button(self):
        """
        Creates and configures the ❌ button with a command callback.
        """
        self._x_button = ttk.Button(self._window, text="❌", style="TButton", command=self.x_btn_command)
        self._x_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    def flip_card(self):
        """
        Flips the card to display the other side with a different background color
        and language.
        """
        try:
            if self._card["text"] == "Hello":
                self._card.config(text="안녕하세요", background="yellow", foreground="black")
            else:
                self._card.config(text="Hello", background="white", foreground="black")
        except Exception as e:
            logging.error(f"Error flipping card: {e}")

    def v_btn_command(self):
        """
        Executes the callback for the ✅ button if it is defined.
        """
        try:
            if self._v_btn_command:
                self._v_btn_command()
            else:
                print("✅ Button command is not set.")
        except Exception as e:
            logging.error(f"Error executing ✅ button command: {e}")

    def x_btn_command(self):
        """
        Executes the callback for the ❌ button if it is defined.
        """
        try:
            if self._x_btn_command:
                self._x_btn_command()
            else:
                print("❌ Button command is not set.")
        except Exception as e:
            logging.error(f"Error executing ❌ button command: {e}")

    @property
    def window(self):
        return self._window


if __name__ == "__main__":
    def v_callback():
        print("✅ Button clicked!")

    def x_callback():
        print("❌ Button clicked!")

    ui = UI()
    ui._v_btn_command = v_callback
    ui._x_btn_command = x_callback
    ui.set_up()
    ui.window.mainloop()
