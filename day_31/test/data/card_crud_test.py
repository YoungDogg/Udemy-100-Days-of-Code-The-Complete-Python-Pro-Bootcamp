import unittest

# from day_31.src.card.card import Card, Language
from day_31.src.data.card_crud import CardCRUD, Card, Language


class TestCardCRUD(unittest.TestCase):
    def setUp(self):
        """Set up a CardCRUD instance for testing."""
        self.crud = CardCRUD()

    def test_create(self):
        """Test creating a new card."""
        card = self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요", ENGLISH="Hello")
        expected_card = {
            "JAPANESE": "こんにちは",
            "KOREAN": "안녕하세요",
            "ENGLISH": "Hello"
        }
        self.assertEqual(self.crud.card, expected_card)
        self.assertEqual(card, expected_card)

    def test_read_existing_language(self):
        """Test reading a word from an existing language."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요", ENGLISH="Hello")
        self.assertEqual(self.crud.read("JAPANESE"), "こんにちは")
        self.assertEqual(self.crud.read("KOREAN"), "안녕하세요")
        self.assertEqual(self.crud.read("ENGLISH"), "Hello")

    def test_read_non_existing_language(self):
        """Test reading a word from a non-existing language."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요")
        with self.assertRaises(ValueError):
            self.crud.read("ENGLISH")

    def test_update_existing_language(self):
        """Test updating a word in an existing language."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요")
        self.crud.update("JAPANESE", "さようなら")
        self.assertEqual(self.crud.card["JAPANESE"], "さようなら")

    def test_update_non_supported_language(self):
        """Test updating a word in a non-supported language."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요")
        with self.assertRaises(ValueError):
            self.crud.update("SPANISH", "Hola")

    def test_delete_existing_language(self):
        """Test deleting a word from an existing language."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요")
        self.crud.delete_language("JAPANESE")
        self.assertNotIn("JAPANESE", self.crud.card)

    def test_delete_non_existing_language(self):
        """Test deleting a word from a non-existing language."""
        self.crud.create(JAPANESE="こんにちは")
        with self.assertRaises(ValueError):
            self.crud.delete_language("ENGLISH")

    def test_clear_card(self):
        """Test clearing the current card."""
        self.crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요")
        self.crud.clear_card()
        self.assertIsNone(self.crud.card)

    def test_read_no_card(self):
        """Test reading when no card is managed."""
        with self.assertRaises(ValueError):
            self.crud.read("JAPANESE")

    def test_update_no_card(self):
        """Test updating when no card is managed."""
        with self.assertRaises(ValueError):
            self.crud.update("JAPANESE", "こんにちは")

    def test_delete_no_card(self):
        """Test deleting a language when no card is managed."""
        with self.assertRaises(ValueError):
            self.crud.delete_language("JAPANESE")


if __name__ == "__main__":
    unittest.main()
