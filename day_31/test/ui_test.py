import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tkinter import ttk
from day_31.src.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()

    def test_set_up(self):
        """Test if the set_up method initializes components without errors."""
        try:
            self.ui.set_up()
        except Exception as e:
            self.fail(f"set_up() raised an exception: {e}")
        self.assertIsInstance(self.ui.window, tk.Tk)

    def test_flip_card(self):
        """Test the card flipping functionality."""
        self.ui.set_up()
        self.assertEqual(self.ui._card["text"], "Hello")
        self.ui.flip_card()
        self.assertEqual(self.ui._card["text"], "안녕하세요")
        self.ui.flip_card()
        self.assertEqual(self.ui._card["text"], "Hello")

    def test_v_button_command(self):
        """Test the functionality of the ✅ button command."""
        mock_callback = MagicMock()
        self.ui._v_btn_command = mock_callback
        self.ui.v_btn_command()
        mock_callback.assert_called_once()

    def test_x_button_command(self):
        """Test the functionality of the ❌ button command."""
        mock_callback = MagicMock()
        self.ui._x_btn_command = mock_callback
        self.ui.x_btn_command()
        mock_callback.assert_called_once()

    def test_card_binding(self):
        """Test if the card has the correct binding for flipping."""
        self.ui.set_up()
        bindings = self.ui._card.bind()
        self.assertIn("<Button-1>", bindings)

if __name__ == "__main__":
    unittest.main()
