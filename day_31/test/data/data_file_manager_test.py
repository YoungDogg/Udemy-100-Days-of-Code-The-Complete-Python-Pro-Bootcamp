import unittest
import os
import pandas as pd
from day_31.src.data.data_file_manager import DataFileManager, Card, Language


class TestDataFileManager(unittest.TestCase):
    def setUp(self):
        """Set up the DataFileManager instance and test data."""
        self.file_name = "test_data.json"
        self.manager = DataFileManager(self.file_name)
        self.manager.create_file()

        # Create some test cards
        self.card1 = Card(JAPANESE="こんにちは", KOREAN="안녕하세요", ENGLISH="Hello")
        self.card2 = Card(JAPANESE="さようなら", KOREAN="안녕히 계세요", ENGLISH="Goodbye")

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_create_file(self):
        """Test creating the JSON file."""
        self.assertTrue(os.path.exists(self.file_name))
        data = self.manager._read_file()
        self.assertTrue(data.empty)  # File should start empty

    def test_save(self):
        """Test saving a new card to the file."""
        self.manager.save(self.card1)
        data = self.manager._read_file()

        # Convert stringified keys back to Language enum for comparison
        saved_words = {Language[key.split(".")[1]]: value for key, value in data.iloc[0]["words"].items()}
        self.assertEqual(saved_words, self.card1.word)  # Now comparison will work

    def test_check_duplicate(self):
        """Test checking for duplicate cards."""
        self.manager.save(self.card1)
        self.assertTrue(self.manager.check_duplicate(self.card1))
        self.assertFalse(self.manager.check_duplicate(self.card2))

    def test_save_duplicate(self):
        """Test saving a duplicate card raises an error."""
        self.manager.save(self.card1)
        with self.assertRaises(ValueError):
            self.manager.save(self.card1)

    def test_update_existing_card(self):
        """Test updating an existing card in the file."""
        self.manager.save(self.card1)  # Save the card
        self.card1.check()  # Mark the card as checked
        updated = self.manager.update(self.card1)  # Update the card
        self.assertTrue(updated)  # Ensure the update method returns True
        data = self.manager._read_file()  # Read updated file
        self.assertTrue(data.iloc[0]["is_checked"])  # Ensure is_checked is True

    def test_update_non_existing_card(self):
        """Test updating a non-existing card."""
        updated = self.manager.update(self.card2)
        self.assertFalse(updated)

    def test_remove_existing_card(self):
        """Test removing an existing card."""
        self.manager.save(self.card1)
        removed = self.manager.remove(self.card1)
        self.assertTrue(removed)
        data = self.manager._read_file()
        self.assertTrue(data.empty)

    def test_remove_non_existing_card(self):
        """Test removing a non-existing card."""
        removed = self.manager.remove(self.card2)
        self.assertFalse(removed)

    def test_read_write_file(self):
        """Test reading and writing to the file."""
        self.manager.save(self.card1)
        data = self.manager._read_file()
        self.assertEqual(len(data), 1)

        # Normalize keys in the words column for comparison
        saved_words = {Language[key.split(".")[1]]: value for key, value in data.iloc[0]["words"].items()}
        self.assertEqual(saved_words, self.card1.word)

    def test_clear_empty_file(self):
        """Test clearing the JSON file when empty."""
        data = self.manager._read_file()
        self.assertTrue(data.empty)

    def test_read_invalid_file(self):
        """Test reading from an invalid JSON file."""
        with open(self.file_name, "w") as file:
            file.write("INVALID JSON")
        data = self.manager._read_file()
        self.assertTrue(data.empty)  # Should handle invalid JSON gracefully


if __name__ == "__main__":
    unittest.main()
