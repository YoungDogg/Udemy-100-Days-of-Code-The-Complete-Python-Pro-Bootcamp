from __future__ import annotations
from typing import Optional, Dict, Any
from day_31.src.card.card import Card, Language


class CardCRUD:
    """
    Handles in-memory CRUD operations for Card-like objects.

    Attributes:
        card (Optional[Dict[str, Any]]): The current card being managed.
    """

    def __init__(self, card: Optional[Dict[str, Any]] = None):
        """
        Initializes the CRUD handler with an optional card.

        Args:
            card (Optional[Dict[str, Any]]): The card to be managed. A dictionary
                                             representing card data (e.g., language-word pairs).
        """
        self.card = card

    def create(self, **kwargs) -> Dict[str, Any]:
        """
        Creates a new card object with the given data.

        Args:
            kwargs: Key-value pairs representing language and corresponding words.

        Returns:
            Dict[str, Any]: The newly created card object.
        """
        self.card = kwargs
        return self.card

    def read(self, language: str) -> str:
        """
        Reads a word in the specified language from the current card.

        Args:
            language (str): The language to read.

        Returns:
            str: The word in the specified language.

        Raises:
            ValueError: If no card is currently managed or the language does not exist.
        """
        if not self.card:
            raise ValueError("No card is currently managed.")
        if language not in self.card:
            raise ValueError(f"Language {language} not found in the card.")
        return self.card[language]

    def update(self, language: str, word: str) -> None:
        """
        Updates a word in the current card for a specified language.

        Args:
            language (str): The language to update.
            word (str): The new word to associate with the language.

        Raises:
            ValueError: If no card is currently managed or if the language is not supported.
        """
        if not self.card:
            raise ValueError("No card is currently managed.")

        # Check if the language is supported
        if language.upper() not in Language.__members__:
            raise ValueError(
                f"Unsupported language: {language}. Supported languages are: {', '.join(Language.__members__.keys())}")

        # Update the word in the card
        self.card[language.upper()] = word

    def delete_language(self, language: str) -> None:
        """
        Deletes a word from the current card for a specified language.

        Args:
            language (str): The language to delete.

        Raises:
            ValueError: If no card is currently managed or the language does not exist.
        """
        if not self.card:
            raise ValueError("No card is currently managed.")
        if language not in self.card:
            raise ValueError(f"Language {language} not found in the card.")
        del self.card[language]

    def clear_card(self) -> None:
        """
        Clears the currently managed card, resetting it to None.
        """
        self.card = None


if __name__ == "__main__":
    # Create a CRUD instance
    crud = CardCRUD()

    # Create a new card
    card = crud.create(JAPANESE="こんにちは", KOREAN="안녕하세요", ENGLISH="Hello")
    print(f"Created Card: {card}")

    # Read a word
    japanese_word = crud.read("JAPANESE")
    print(f"Japanese Word: {japanese_word}")

    # Update a word
    # crud.update("CHINESE", "NIHAO")
    crud.update("ENGLISH", "Hi")
    print(f"Updated Card: {crud.card}")

    # Delete a word
    crud.delete_language("KOREAN")
    print(f"Card After Deletion: {crud.card}")

    # Clear the card
    crud.clear_card()
    print(f"Cleared Card: {crud.card}")
