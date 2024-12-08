from enum import Enum


class Language(Enum):
    """
    Enum class for defining language keys dynamically.
    """
    JAPANESE = "JAP"
    KOREAN = "KOR"
    ENGLISH = "ENG"
    FRENCH = "FRA"  # You can add more languages as needed.


class Card:
    """
    Card class represents a single card containing words in multiple languages
    and a boolean to check if it's marked as checked.

    Attributes:
        _word (dict): A dictionary holding the words in various languages.
        _is_checked (bool): A flag to indicate if the card has been checked.
    """

    def __init__(self, **kwargs):
        """
        Initializes the card with words in multiple languages.

        Args:
            kwargs: Key-value pairs where the key is a string (language name) or
                    a Language enum, and the value is the word in that language.
        """
        self._word = {}
        for key, word in kwargs.items():
            if isinstance(key, Language):  # If the key is already a Language enum
                self._word[key] = word
            elif isinstance(key, str):  # If the key is a string, convert it to Language
                try:
                    enum_key = Language[key.upper()]
                    self._word[enum_key] = word
                except KeyError:
                    raise ValueError(f"Invalid language key: {key}")
        self._is_checked = False

    def get_word(self, language: Language) -> str:
        """
        Retrieves the word in the specified language.

        Args:
            language (Language): The language enum for the desired word.

        Returns:
            str: The word in the specified language.
        """
        return self._word.get(language, f"No word available for {language.name}")

    def check(self):
        """
        Marks the card as checked.
        """
        self._is_checked = True

    def uncheck(self):
        """
        Marks the card as unchecked.
        """
        self._is_checked = False

    @property
    def is_checked(self) -> bool:
        """
        Checks if the card is marked as checked.

        Returns:
            bool: True if the card is checked, False otherwise.
        """
        return self._is_checked


if __name__ == "__main__":
    # Test case for the Card class
    print("Running Card class tests...")

    # Create a card instance with dynamic languages
    card = Card(
        JAPANESE="こんにちは",
        KOREAN="안녕하세요",
        ENGLISH="Hello"
    )

    # Test initialization
    print(f"``Japanese Word: {card.get_word(Language.JAPANESE)}``")  # Expected: こんにちは
    print(f"``Korean Word: {card.get_word(Language.KOREAN)}``")      # Expected: 안녕하세요
    print(f"``English Word: {card.get_word(Language.ENGLISH)}``")    # Expected: Hello
    print(f"``French Word: {card.get_word(Language.FRENCH)}``")      # Expected: No word available for FRENCH
    print(f"``Is Checked: {card.is_checked}``")                   # Expected: False

    # Test check functionality
    card.check()
    print(f"``Is Checked after check(): {card.is_checked}``")      # Expected: True

    # Test uncheck functionality
    card.uncheck()
    print(f"``Is Checked after uncheck(): {card.is_checked}``")    # Expected: False
