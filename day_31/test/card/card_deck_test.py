import unittest
from day_31.src.card.card import Card, Language
from day_31.src.card.card_deck import CardDeck


class TestCardDeck(unittest.TestCase):
    def setUp(self):
        """Set up a CardDeck instance and some Card instances for testing."""
        self.deck = CardDeck()
        self.card1 = Card(JAPANESE="こんにちは", ENGLISH="Hello")
        self.card2 = Card(KOREAN="안녕하세요", ENGLISH="Hi")
        self.card3 = Card(JAPANESE="さようなら", KOREAN="안녕히 계세요", ENGLISH="Goodbye")

    def test_add_to_deck(self):
        """Test adding cards to the deck."""
        self.deck.add_to_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        self.deck.add_to_deck(self.card2)
        self.assertEqual(self.deck.get_card_count(), 2)

    def test_discard_from_deck(self):
        """Test discarding cards from the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.discard_from_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        self.assertRaises(ValueError, self.deck.discard_from_deck, self.card3)  # Card not in deck

    def test_shuffle_deck(self):
        """Test shuffling the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.add_to_deck(self.card3)
        before_shuffle = self.deck._card_deck[:]
        self.deck.shuffle_deck()
        after_shuffle = self.deck._card_deck
        self.assertNotEqual(before_shuffle, after_shuffle)  # Deck order should change

    def test_draw_card(self):
        """Test drawing a card from the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        drawn_card = self.deck.draw_card()
        self.assertEqual(drawn_card, self.card1)  # First card should be drawn
        self.assertEqual(self.deck.get_card_count(), 1)

        # Drawing from an empty deck should raise an error
        self.deck.draw_card()  # Draw remaining card
        self.assertRaises(ValueError, self.deck.draw_card)

    def test_get_card_count(self):
        """Test getting the card count in the deck."""
        self.assertEqual(self.deck.get_card_count(), 0)  # Deck is initially empty
        self.deck.add_to_deck(self.card1)
        self.assertEqual(self.deck.get_card_count(), 1)
        self.deck.add_to_deck(self.card2)
        self.assertEqual(self.deck.get_card_count(), 2)


if __name__ == "__main__":
    unittest.main()
