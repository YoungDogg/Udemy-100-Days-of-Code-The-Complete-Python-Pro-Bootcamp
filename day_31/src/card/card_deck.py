from __future__ import annotations

import random
from typing import List
from day_31.src.data.data_file_manager import DataFileManager
from day_31.src.card.card import Card # for the unit test


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

    @property
    def card_deck(self):
        return self._card_deck

    @classmethod
    def from_file(cls, file_manager: DataFileManager):
        """
        Loads card data from a file and initializes the CardDeck.

        Args:
            file_manager: An instance of DataFileManager to handle file reading.

        Returns:
            An instance of CardDeck populated with cards from the file.
        """
        print("Starting from_file()...")
        try:
            # Step 1: Read the data from file
            print("Reading file using DataFileManager...")
            data = file_manager.read_file()
            print(f"Data read successfully: {data}")

            # Step 2: Initialize the deck
            print("Initializing CardDeck...")
            deck = cls()

            # Step 3: Add cards to the deck
            for index, row in data.iterrows():
                try:
                    print(f"Creating card from row {index}: {row}")
                    card = Card(**row)
                    deck.add_to_deck(card)
                    print(f"Card added successfully: {card}")
                except ValueError as e:
                    print(f"Error creating card from row {index}: {e}")
                    raise

            print("CardDeck initialized successfully.")
            return deck

        except FileNotFoundError as e:
            print(f"FileNotFoundError in from_file: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred in from_file: {e}")
            raise
        finally:
            print("Exiting from_file()")

    def add_to_deck(self, card: Card) -> None:
        """
        Adds a card to the deck.

        Args:
            card (Card): The card to be added.
        """
        self._card_deck.append(card)

    def put_back(self, card: Card) -> None:
        """
        Puts a card back into the deck and shuffles it if the deck is not empty.
        Args:
            card (Card): The card to be put back into the deck.
        """
        self._card_deck.append(card)  # Add the card to the bottom of the deck
        if len(self._card_deck) > 1:  # Shuffle only if there is more than one card
            self.shuffle_deck()

    def discard_from_deck(self, card: Card) -> None:
        """
        Removes a card from the deck if it exists.

        Args:
            card (Card): The card to be discarded.

        Raises:
            ValueError: If the card is not found in the deck.
        """
        try:
            # for c in self._card_deck:
            #     print(f"Deck Card: {c}, To Remove: {card}, Equal: {c == card}")
            self._card_deck.remove(card)
        except ValueError:
            raise ValueError("Card not found in the deck.")

    def shuffle_deck(self) -> None:
        """
        Shuffles the deck in place.

        Does nothing if the deck contains one card.
        Raises:
            ValueError: If the deck is empty.
        """
        if not self._card_deck:  # Deck is empty
            raise ValueError("Cannot shuffle an empty deck.")
        if len(self._card_deck) <= 1:  # Deck has only one card
            print("Deck has one or no cards, skipping shuffle.")
            return

        print(f"Deck before shuffle: {[str(card) for card in self._card_deck]}")
        random.shuffle(self._card_deck)
        print(f"Deck after shuffle: {[str(card) for card in self._card_deck]}")


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

    def is_empty(self) -> bool:
        """
        Checks if the deck is empty.

        Returns:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self._card_deck) == 0


if __name__ == "__main__":
    from card import Card, Language  # Importing the updated Card and Language classes

    # Example usage
    deck = CardDeck()
    card1 = Card(JAPANESE="エース", KOREAN="에이스", ENGLISH="Ace")
    card2 = Card(JAPANESE="キング", KOREAN="킹", ENGLISH="King")
    card3 = Card(JAPANESE="クイーン", KOREAN="퀸", ENGLISH="Queen")
    card4 = Card(JAPANESE="10", KOREAN="10", ENGLISH="10")

    # Add cards to the deck
    deck.add_to_deck(card1)
    deck.add_to_deck(card2)
    deck.add_to_deck(card3)
    deck.add_to_deck(card4)

    # Shuffle the deck
    deck.shuffle_deck()
    print(f"Shuffled Deck: ``{deck.card_deck}``")

    # Draw a card
    drawn_card = deck.draw_card()
    print(f"Drawn Card: ``{drawn_card}``")

    # Get remaining card count
    print(f"Remaining Cards: ``{deck.get_card_count()}``")

    # Discard a card
    deck.discard_from_deck(card2)
    print(f"Deck after discarding: ``{deck.card_deck}``")

    # Test the put_back method
    print("\nTesting put_back method:")
    deck.put_back(drawn_card)  # Put the drawn card back to the bottom of the deck
    print(f"Deck after putting back at the bottom: ``{deck.card_deck}``")

    deck.put_back(card3)  # Put card3 back at the top of the deck
    print(f"Deck after putting back at the top: ``{deck.card_deck}``")

    # Shuffle again and verify
    deck.shuffle_deck()
    print(f"Deck after reshuffling: ``{deck.card_deck}``")
