import unittest
from unittest.mock import MagicMock
from day_31.src.card.card import Card
from day_31.src.card.card_deck import CardDeck


class TestCardDeck(unittest.TestCase):
    def setUp(self):
        """Set up a CardDeck instance with mocked Card instances."""
        self.deck = CardDeck()
        # Create mocked cards
        self.card1 = MagicMock(spec=Card)
        self.card2 = MagicMock(spec=Card)
        self.card3 = MagicMock(spec=Card)

    def test_add_to_deck(self):
        """Test adding mocked cards to the deck."""
        self.deck.add_to_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        self.deck.add_to_deck(self.card2)
        self.assertEqual(self.deck.get_card_count(), 2)

    def test_discard_from_deck(self):
        """Test discarding mocked cards from the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.discard_from_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        with self.assertRaises(ValueError):
            self.deck.discard_from_deck(self.card3)  # Card not in deck

    def test_put_back(self):
        """Test putting a mocked card back into the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.add_to_deck(self.card3)
        drawn_card = self.deck.draw_card()
        self.deck.put_back(drawn_card)
        self.assertEqual(self.deck.get_card_count(), 3)
        self.assertIn(drawn_card, self.deck._card_deck)

    def test_shuffle_deck(self):
        """Test shuffling the deck with mocked cards."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.add_to_deck(self.card3)

        before_shuffle = self.deck._card_deck[:]
        self.deck.shuffle_deck()
        after_shuffle = self.deck._card_deck

        # Retry shuffle if the order is accidentally the same
        attempts = 5
        while before_shuffle == after_shuffle and attempts > 0:
            self.deck.shuffle_deck()
            after_shuffle = self.deck._card_deck
            attempts -= 1

        self.assertNotEqual(before_shuffle, after_shuffle, "Deck order did not change after shuffling.")

    def test_draw_card(self):
        """Test drawing a mocked card from the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        drawn_card = self.deck.draw_card()
        self.assertEqual(drawn_card, self.card1)  # First card should be drawn
        self.assertEqual(self.deck.get_card_count(), 1)

        # Drawing from an empty deck should raise an error
        self.deck.draw_card()  # Draw remaining card
        with self.assertRaises(ValueError):
            self.deck.draw_card()

    def test_get_card_count(self):
        """Test getting the card count in the deck with mocked cards."""
        self.assertEqual(self.deck.get_card_count(), 0)  # Deck is initially empty
        self.deck.add_to_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        self.deck.add_to_deck(self.card2)
        self.assertEqual(self.deck.get_card_count(), 2)

    def test_is_empty(self):
        """Test checking if the deck is empty with mocked cards."""
        self.assertTrue(self.deck.is_empty())  # Deck should be empty initially
        self.deck.add_to_deck(self.card1)
        self.assertFalse(self.deck.is_empty())  # Deck is no longer empty


if __name__ == "__main__":
    unittest.main()
