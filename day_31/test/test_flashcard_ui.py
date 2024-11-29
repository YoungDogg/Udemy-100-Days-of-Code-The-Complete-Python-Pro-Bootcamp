import unittest
import tkinter as tk
from flashcard_ui import FlashCardUI  # Replace with your file name


class TestFlashCardUI(unittest.TestCase):
    def setUp(self):
        """Setup for tests."""
        self.ui = FlashCardUI()

    def tearDown(self):
        """Clean up after tests."""
        self.ui.root.destroy()

    def test_root_configuration(self):
        """Test if the root window is configured properly."""
        self.assertEqual(self.ui.root.title(), "Flash Card")
        self.assertEqual(self.ui.root["bg"], "#38E2D6")
        self.assertEqual(self.ui.root.geometry(), "500x300")

    def test_grid_configuration(self):
        """Test grid layout configuration."""
        for col in range(3):
            self.assertEqual(self.ui.root.grid_columnconfigure(col, "weight"), 1)
        for row in range(3):
            self.assertEqual(self.ui.root.grid_rowconfigure(row, "weight"), 1)

    def test_buttons_and_labels(self):
        """Test if buttons and labels are created correctly."""
        # Find the 'X' button by text
        x_button = None
        for child in self.ui.root.winfo_children():
            if isinstance(child, tk.Button) and child["text"] == "X":
                x_button = child
                break
        self.assertIsNotNone(x_button)
        self.assertEqual(x_button["fg"], "red")

        # Find the check button
        check_button = None
        for child in self.ui.root.winfo_children():
            if isinstance(child, tk.Button) and child["text"] == "✔":
                check_button = child
                break
        self.assertIsNotNone(check_button)
        self.assertEqual(check_button["fg"], "green")

    def test_set_command(self):
        """Test setting button commands."""
        def mock_command():
            pass

        self.ui._setup_x_button(mock_command)
        self.assertEqual(self.ui._x_command, mock_command)

        self.ui._setup_check_button(mock_command)
        self.assertEqual(self.ui._check_command, mock_command)

    def test_set_command_error(self):
        """Test error handling in _set_command."""
        with self.assertRaises(tk.TclError):
            self.ui._set_command('_x_command', None)

if __name__ == "__main__":
    unittest.main()
