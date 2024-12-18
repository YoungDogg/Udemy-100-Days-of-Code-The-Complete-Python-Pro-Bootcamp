import unittest
from day_31.src.card.card import Card, Language


class TestCard(unittest.TestCase):
    def setUp(self):
        """Set up a Card instance for testing."""
        self.card = Card(
            JAPANESE="こんにちは",
            KOREAN="안녕하세요",
            ENGLISH="Hello"
        )

    def test_get_word_valid_language(self):
        """Test retrieving words for valid languages."""
        self.assertEqual(self.card.get_word(Language.JAPANESE), "こんにちは")
        self.assertEqual(self.card.get_word(Language.KOREAN), "안녕하세요")
        self.assertEqual(self.card.get_word(Language.ENGLISH), "Hello")

    def test_get_word_invalid_language(self):
        """Test retrieving words for an invalid language."""
        self.assertEqual(
            self.card.get_word(Language.FRENCH),
            "No word available for FRENCH"
        )

    def test_check(self):
        """Test marking the card as checked."""
        self.assertFalse(self.card.is_checked)  # Initially unchecked
        self.card.check()
        self.assertTrue(self.card.is_checked)   # After checking

    def test_uncheck(self):
        """Test marking the card as unchecked."""
        self.card.check()
        self.assertTrue(self.card.is_checked)   # Marked as checked
        self.card.uncheck()
        self.assertFalse(self.card.is_checked)  # After unchecking

    def test_invalid_language_key(self):
        """Test creating a card with an invalid language key."""
        with self.assertRaises(ValueError):
            Card(SPANISH="Hola")  # SPANISH is not in Language enum


if __name__ == "__main__":
    unittest.main()
