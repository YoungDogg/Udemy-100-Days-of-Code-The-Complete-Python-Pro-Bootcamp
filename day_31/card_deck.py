import random
from card import Card


class CardDeck:
    """
    Handles the collection of cards.

    Attributes:
        cards (list[Card]): A list of Card objects representing the deck.

    Methods:
        shuffle(): Shuffles the deck of cards.
        flip_card(index, delay=2): Simulates flipping a card after a delay.
    """

    def __init__(self):
        """
        Initialize an empty deck of cards.
        """
        self.cards = []

    def add_card(self, card: Card):
        """
        Adds a Card to the deck.

        Args:
            card (Card): The Card object to add.
        """
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck.")
        self.cards.append(card)

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def flip_card(self, index: int, delay: int = 2):
        """
        Simulates flipping a card to reveal its Japanese meaning.

        Args:
            index (int): The index of the card to flip.
            delay (int): The number of seconds before flipping. Default is 2 seconds.

        Returns:
            str: The Japanese word of the flipped card.
        """
        if index < 0 or index >= len(self.cards):
            raise IndexError("Card index out of range.")
        card = self.cards[index]
        print(f"Flipping card after {delay} seconds...")
        # Simulate a delay (optional: use time.sleep if needed for real delays)
        return card.japanese

    def __len__(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self.cards)

    def __repr__(self):
        """
        String representation of the CardDeck for debugging.
        """
        return f"CardDeck(cards={len(self.cards)})"
