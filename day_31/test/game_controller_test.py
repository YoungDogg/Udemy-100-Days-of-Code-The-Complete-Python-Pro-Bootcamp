import unittest
from unittest.mock import patch, MagicMock
from day_31.src.game_controller import GameController
from day_31.src.card.card_deck import CardDeck, Card


class TestGameController(unittest.TestCase):
    def setUp(self):
        """Set up a GameController instance with mocked CardDeck and Cards."""
        self.game_controller = GameController()
        self.mock_deck = MagicMock(spec=CardDeck)
        self.game_controller.card_deck = self.mock_deck

        # Create mocked cards
        self.card1 = MagicMock(spec=Card)
        self.card2 = MagicMock(spec=Card)
        self.card3 = MagicMock(spec=Card)
        self.mock_deck._card_deck = [self.card1, self.card2, self.card3]

    @patch("day_31.src.card.card_deck.CardDeck.from_file")
    def test_before_start_success(self, mock_load_from_file):
        """Test that before_start correctly loads and shuffles the deck."""
        mock_load_from_file.return_value = self.mock_deck
        self.game_controller.before_start()
        self.assertIsNotNone(self.game_controller.card_deck)
        self.mock_deck.shuffle.assert_called_once()

    @patch("day_31.src.card.card_deck.CardDeck.from_file", side_effect=FileNotFoundError)
    def test_before_start_file_not_found(self, mock_load_from_file):
        """Test handling of a missing data file."""
        with patch("builtins.print") as mock_print:
            self.game_controller.before_start()
            mock_print.assert_called_with("Error: data.json file not found!")

    def test_start_success(self):
        """Test starting the game when the deck is properly initialized."""
        self.mock_deck.draw_card.return_value = self.card1
        with patch("builtins.print") as mock_print:
            self.game_controller.start()
            mock_print.assert_called_with("Game started! Good luck!")
            self.assertEqual(self.game_controller.current_card, self.card1)

    def test_start_no_deck(self):
        """Test starting the game without initializing the deck."""
        self.game_controller.card_deck = None
        with patch("builtins.print") as mock_print:
            self.game_controller.start()
            mock_print.assert_called_with("Error: Card deck is not initialized!")
            self.assertIsNone(self.game_controller.current_card)

    def test_during_progress_check(self):
        """Test during_progress with a '✅' button click."""
        self.game_controller.current_card = self.card1
        self.mock_deck.draw_card.return_value = self.card2
        self.card1.is_checked = False

        with patch("builtins.print") as mock_print:
            self.game_controller.during_progress("✅")
            mock_print.assert_any_call("Button Clicked: ✅")
            mock_print.assert_any_call(f"Current Card Before Action: {self.card1}")
            self.card1.check.assert_called_once()
            self.assertEqual(self.game_controller.current_card, self.card2)

    def test_during_progress_uncheck(self):
        """Test during_progress with a '❌' button click."""
        self.game_controller.current_card = self.card1
        self.mock_deck.draw_card.return_value = self.card2
        self.card1.is_checked = True

        with patch("builtins.print") as mock_print:
            self.game_controller.during_progress("❌")
            mock_print.assert_any_call("Button Clicked: ❌")
            mock_print.assert_any_call(f"Current Card Before Action: {self.card1}")
            self.card1.uncheck.assert_called_once()
            self.assertEqual(self.game_controller.current_card, self.card2)

    def test_during_progress_invalid_button(self):
        """Test during_progress with an invalid button click."""
        self.game_controller.current_card = self.card1
        with self.assertRaises(ValueError):
            self.game_controller.during_progress("Invalid")

    def test_end(self):
        """Test ending the game."""
        with patch("builtins.print") as mock_print:
            self.game_controller.end()
            mock_print.assert_called_with("Game over! Thanks for playing!")

    def test_empty_deck_during_progress(self):
        """Test during_progress when the deck becomes empty."""
        self.game_controller.current_card = self.card3
        self.mock_deck._card_deck = []
        with patch("builtins.print") as mock_print:
            self.game_controller.during_progress("✅")
            mock_print.assert_any_call(f"Last card processed: {self.card3}")
            mock_print.assert_called_with("Game over! Thanks for playing!")

    def test_game_flow(self):
        """Simulate a full game flow."""
        self.mock_deck.is_empty.side_effect = [False, False, True]  # Deck becomes empty after two actions
        self.mock_deck.draw_card.side_effect = [self.card1, self.card2]  # Cards to draw

        with patch("builtins.print") as mock_print:
            self.game_controller.start()
            self.game_controller.during_progress("✅")
            self.game_controller.during_progress("❌")
            mock_print.assert_any_call("Game over! Thanks for playing!")


if __name__ == "__main__":
    unittest.main()