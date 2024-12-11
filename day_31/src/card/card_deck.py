from __future__ import annotations

import random
from typing import List
from enum import Enum
from card import Card


class CardDeck:
    """
    Represents a collection of cards that can be added, discarded, or shuffled.

    Attributes:
        _card_deck (List[Card]): The list of cards in the deck.
    """

    def __init__(self):
        """
        Initializes an empty card deck.
        """
        self._card_deck: List[Card] = []

    def add_to_deck(self, card: Card) -> None:
        """
        Adds a card to the deck.

        Args:
            card (Card): The card to be added.
        """
        self._card_deck.append(card)

    def discard_from_deck(self, card: Card) -> None:
        """
        Removes a card from the deck if it exists.

        Args:
            card (Card): The card to be discarded.

        Raises:
            ValueError: If the card is not found in the deck.
        """
        try:
            self._card_deck.remove(card)
        except ValueError:
            raise ValueError("Card not found in the deck.")

    def shuffle_deck(self) -> None:
        """
        Shuffles the deck in place.
        """
        if not self._card_deck:
            raise ValueError("Cannot shuffle an empty deck.")
        random.shuffle(self._card_deck)

    def get_card_count(self) -> int:
        """
        Returns the number of cards in the deck.

        Returns:
            int: The number of cards in the deck.
        """
        return len(self._card_deck)

    def draw_card(self) -> Card:
        """
        Removes and returns the top card from the deck.

        Returns:
            Card: The top card from the deck.

        Raises:
            ValueError: If the deck is empty.
        """
        if not self._card_deck:
            raise ValueError("Cannot draw from an empty deck.")
        return self._card_deck.pop(0)


if __name__ == "__main__":
    # Test the CardDeck class (assumes a Card class exists with proper implementation)

    class Card:
        def __init__(self, name: str):
            self.name = name

        def __repr__(self):
            return f"Card({self.name})"


    # Example usage
    deck = CardDeck()

    card1 = Card("Ace of Spades")
    card2 = Card("King of Hearts")
    card3 = Card("Queen of Diamonds")
    card4 = Card("10 of Diamonds")

    # Add cards to the deck
    deck.add_to_deck(card1)
    deck.add_to_deck(card2)
    deck.add_to_deck(card3)
    deck.add_to_deck(card4)

    # Shuffle the deck
    deck.shuffle_deck()
    print(f"Shuffled Deck: ``{deck._card_deck}``")

    # Draw a card
    drawn_card = deck.draw_card()
    print(f"Drawn Card: ``{drawn_card}``")

    # Get remaining card count
    print(f"Remaining Cards: ``{deck.get_card_count()}``")

    # Discard a card
    deck.discard_from_deck(card2)
    print(f"Deck after discarding: ``{deck._card_deck}``")
