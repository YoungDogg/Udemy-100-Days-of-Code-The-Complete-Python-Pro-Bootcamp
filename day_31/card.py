class Card:
    """
    A single card object.

    Attributes:
        korean (str): The korean word.
        japanese (str): The Japanese translation of the word.
        isChecked (bool): Indicates whether the card is marked as checked.
    """

    def __init__(self, korean: str = "", japanese: str = ""):
        """
        Initialize a Card object with optional korean and Japanese values.
        """
        self.korean: str = korean
        self.japanese: str = japanese
        self.isChecked: bool = False

    def validate(self):
        """
        Validates the attributes.
        Raises an error if either korean or Japanese is empty.
        """
        if not self.korean:
            raise ValueError("korean word is missing")
        if not self.japanese:
            raise ValueError("Japanese word is missing")

    def __repr__(self):
        """
        String representation of the Card object for debugging.
        """
        return f"Card(korean='{self.korean}', japanese='{self.japanese}', isChecked={self.isChecked})"


if __name__ == "__main__":
    # Valid card
    card1 = Card(korean="안녕하세요", japanese="こんにちは")
    print(card1)  # Output: Card(korean='Hello', japanese='こんにちは', isChecked=False)

    # Invalid card
    card2 = Card()
    try:
        card2.validate()
    except ValueError as e:
        print(f"Validation Error: {e}")  # Output: Validation Error: korean word is missing

