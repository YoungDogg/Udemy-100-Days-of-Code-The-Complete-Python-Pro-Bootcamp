# card_deck.py

import random
from card import Card

class CardDeck:
    """
    Handles the collection of cards.

    Attributes:
        cards (list[Card]): A list of Card objects representing the deck.

    Methods:
        add_to_deck(card): Adds a card to the deck.
        discard_from_deck(index): Removes a card from the deck at the specified index.
        shuffle(): Shuffles the deck of cards.
        flip_card(index, delay=2): Simulates flipping a card after a delay.
        __getitem__(index): Allows indexing into the deck.
    """
    def __init__(self):
        """
        Initialize an empty deck of cards.
        """
        self.cards = []

    def add_to_deck(self, card: Card):
        """
        Adds a card to the deck.

        Args:
            card (Card): The card to add to the deck.
        """
        self.cards.append(card)

    def discard_from_deck(self, index: int):
        """
        Removes a card from the deck at the specified index.

        Args:
            index (int): The index of the card to remove.

        Returns:
            Card: The removed card.
        """
        if index < 0 or index >= len(self.cards):
            raise IndexError("Card index out of range.")
        return self.cards.pop(index)

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def flip_card(self, index: int, delay: int = 0):
        """
        Simulates flipping a card to reveal its Korean meaning.
        If click a card, it flips and shows in Korean.
        This function associates with UI.

        Args:
            index (int): The index of the card to flip.
            delay (int): The number of seconds before flipping. Default is 0 seconds, no delay.

        Returns:
            str: The Korean word of the flipped card.
        """
        if index < 0 or index >= len(self.cards):
            raise IndexError("Card index out of range.")
        card = self.cards[index]
        print(f"Flipping card after {delay} seconds...")
        # Simulate a delay (uncomment the next line to actually pause)
        # import time
        # time.sleep(delay)
        return card.korean

    def __len__(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self.cards)

    def __getitem__(self, index):
        """
        Allows indexing into the deck.

        Args:
            index (int): The index of the card.

        Returns:
            Card: The card at the specified index.
        """
        return self.cards[index]

    def __repr__(self):
        """
        String representation of the CardDeck for debugging.
        """
        return f"CardDeck(cards={len(self.cards)})"


if __name__ == "__main__":
    # Test code
    deck = CardDeck()
    print(deck)  # Output: CardDeck(cards=0)

    # Create some Card instances
    card1 = Card(korean="안녕하세요", japanese="こんにちは")
    card2 = Card(korean="사랑해요", japanese="愛しています")
    card3 = Card(korean="감사합니다", japanese="ありがとうございます")

    # Add cards to the deck using add_to_deck
    deck.add_to_deck(card1)
    deck.add_to_deck(card2)
    deck.add_to_deck(card3)

    print(deck)  # Output: CardDeck(cards=3)
    print("Initial deck:")
    for card in deck:
        print(card)

    # Access a card using indexing
    print("\nAccessing card at index 1 using __getitem__:")
    print(deck[1])

    # Shuffle the deck
    deck.shuffle()
    print("\nDeck after shuffling:")
    for card in deck:
        print(card)

    # Flip a card
    flipped_korean = deck.flip_card(0)
    print(f"\nFlipped card Korean word: {flipped_korean}")

    # Discard a card
    removed_card = deck.discard_from_deck(1)
    print(f"\nRemoved card: {removed_card}")
    print("Deck after discarding a card:")
    for card in deck:
        print(card)
    print(f"Deck size: {len(deck)}")
