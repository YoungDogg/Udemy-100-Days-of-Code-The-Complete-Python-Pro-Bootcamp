import unittest
from unittest.mock import patch, MagicMock
from day_31.src.game_controller import GameController
from day_31.src.card.card_deck import CardDeck, Card


class TestGameController(unittest.TestCase):
    def setUp(self):
        """Set up a GameController instance with mocked CardDeck and Cards."""
        self.mock_deck = MagicMock(spec=CardDeck)
        self.game_controller = GameController(card_deck=self.mock_deck)

        # Create mocked cards
        self.card1 = MagicMock(spec=Card)
        self.card2 = MagicMock(spec=Card)
        self.card3 = MagicMock(spec=Card)

        # Add cards to the mocked deck using add_to_deck
        self.mock_deck.add_to_deck.side_effect = lambda card: card  # Mock the behavior of adding cards
        self.mock_deck.draw_card.side_effect = [self.card1, self.card2, self.card3]  # Mock draw behavior
        self.mock_deck.is_empty.side_effect = [False, False, True]  # Deck becomes empty after three cards

    @patch("day_31.src.card.card_deck.CardDeck.from_file")
    def test_before_start_success(self, mock_load_from_file):
        """Test that before_start correctly loads and shuffles the deck."""
        mock_load_from_file.return_value = self.mock_deck
        self.game_controller.before_start()
        self.assertIsNotNone(self.game_controller.card_deck)
        self.mock_deck.shuffle_deck.assert_called_once()

    @patch("day_31.src.card.card_deck.CardDeck.from_file", side_effect=FileNotFoundError)
    def test_before_start_file_not_found(self, mock_load_from_file):
        """Test handling of a missing data file."""
        with patch("builtins.print") as mock_print:
            self.game_controller.before_start()
            mock_print.assert_called_with("Error: data.json file not found!")

    def test_start_success(self):
        """Test starting the game when the deck is properly initialized."""
        # Add cards to the mock deck
        self.mock_deck.is_empty.return_value = False
        self.mock_deck.draw_card.return_value = self.card1  # Simulate drawing the first card

        with patch("builtins.print") as mock_print:
            self.game_controller.start()  # Call the start method
            # Verify that the start message is printed
            mock_print.assert_called_with("Game started! Good luck!")
            # Verify that the first card is set as the current card
            self.assertEqual(self.game_controller.current_card, self.card1)
            # Verify that draw_card was called
            self.mock_deck.draw_card.assert_called_once()

    def test_start_no_deck(self):
        """Test starting the game without initializing the deck."""
        self.game_controller.card_deck = None
        with patch("builtins.print") as mock_print:
            self.game_controller.start()
            mock_print.assert_called_with("Error: Card deck is not initialized!")
            self.assertIsNone(self.game_controller.current_card)

    def test_handle_button_click_valid_check(self):
        """Test handle_button_click with a valid '✅' button click."""
        self.card1.is_checked = False
        with patch("builtins.print") as mock_print:
            self.game_controller.handle_button_click("✅")
            mock_print.assert_any_call("Button Clicked: ✅")
            mock_print.assert_any_call(f"Current Card Before Action: {self.card1}")
            self.card1.check.assert_called_once()
            self.assertEqual(self.game_controller.current_card, self.card2)

    def test_handle_button_click_valid_uncheck(self):
        """Test handle_button_click with a valid '❌' button click."""
        self.card1.is_checked = True
        with patch("builtins.print") as mock_print:
            self.game_controller.handle_button_click("❌")
            mock_print.assert_any_call("Button Clicked: ❌")
            mock_print.assert_any_call(f"Current Card Before Action: {self.card1}")
            self.card1.uncheck.assert_called_once()
            self.assertEqual(self.game_controller.current_card, self.card2)

    def test_handle_button_click_invalid_button(self):
        """Test handle_button_click with an invalid button."""
        with self.assertRaises(ValueError) as context:
            self.game_controller.handle_button_click("invalid")
        self.assertEqual(str(context.exception), "Invalid button clicked.")

    def test_handle_button_click_empty_deck(self):
        """Test handle_button_click when the deck is empty."""
        self.mock_deck.is_empty.return_value = True
        with patch("builtins.print") as mock_print:
            self.game_controller.handle_button_click("✅")
            mock_print.assert_any_call("Card deck is not initialized or empty.")
            self.game_controller.end.assert_called_once()

    def test_handle_button_click_last_card(self):
        """Test handle_button_click when the last card is processed."""
        self.mock_deck.is_empty.side_effect = [False, True]  # Simulate last card in deck
        with patch("builtins.print") as mock_print:
            self.game_controller.handle_button_click("✅")
            mock_print.assert_any_call(f"Last card processed: {self.card1}")
            self.game_controller.end.assert_called_once()

    def test_end(self):
        """Test ending the game."""
        with patch("builtins.print") as mock_print:
            self.game_controller.end()
            mock_print.assert_called_with("Game over! Thanks for playing!")


if __name__ == "__main__":
    unittest.main()
