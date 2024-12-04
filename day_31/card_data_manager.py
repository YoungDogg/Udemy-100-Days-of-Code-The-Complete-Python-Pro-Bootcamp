from card_deck import CardDeck
from card import Card


class CardDataManager:
    """
    Handles CRUD operations for the card deck.

    Attributes:
        cardDeck (CardDeck): An instance of CardDeck representing the deck.

    Methods:
        create_card(korean, japanese): Adds a new card to the deck.
        read_card(index): Retrieves a card from the deck.
        update_card(index, korean=None, japanese=None): Updates an existing card.
        delete_card(index): Removes a card from the deck.
    """
    def __init__(self):
        self.cardDeck = CardDeck()

    def create_card(self, korean: str, japanese: str) -> Card:
        card = Card(korean=korean, japanese=japanese)
        self.cardDeck.add_to_deck(card)
        return card

    def read_card(self, index: int) -> Card:
        if index < 0 or index >= len(self.cardDeck):
            raise IndexError("Card index out of range.")
        return self.cardDeck[index]

    def update_card(self, index: int, korean: str = None, japanese: str = None):
        card = self.read_card(index)
        if korean:
            card.korean = korean
        if japanese:
            card.japanese = japanese

    def delete_card(self, index: int):
        if index < 0 or index >= len(self.cardDeck):
            raise IndexError("Card index out of range.")
        self.cardDeck.discard_from_deck(index)

    def __repr__(self):
        return f"CardDataManager(deck_size={len(self.cardDeck)})"


if __name__ == "__main__":
    # Test code
    data_manager = CardDataManager()
    print("Initial Data Manager:", data_manager)  # Should show deck_size=0

    # Test creating cards
    print("\nCreating Cards:")
    data_manager.create_card(korean="안녕하세요", japanese="こんにちは")
    data_manager.create_card(korean="사랑해요", japanese="愛しています")
    data_manager.create_card(korean="감사합니다", japanese="ありがとうございます")
    print("Data Manager after adding cards:", data_manager)  # Should show deck_size=3

    # Test reading cards
    print("\nReading Cards:")
    try:
        card = data_manager.read_card(1)
        print(f"Card at index 1: {card}")
    except IndexError as e:
        print(f"Error: {e}")

    # Test updating a card
    print("\nUpdating Card at index 1:")
    data_manager.update_card(1, korean="보고싶어요", japanese="会いたいです")
    updated_card = data_manager.read_card(1)
    print(f"Updated Card at index 1: {updated_card}")

    # Test deleting a card
    print("\nDeleting Card at index 0:")
    data_manager.delete_card(0)
    print("Data Manager after deleting a card:", data_manager)  # Should show deck_size=2

    # Print all remaining cards
    print("\nRemaining Cards in Deck:")
    for i in range(len(data_manager.cardDeck)):
        card = data_manager.read_card(i)
        print(f"Card {i}: {card}")

    # Test error handling for invalid index
    print("\nTesting Error Handling:")
    try:
        data_manager.read_card(10)
    except IndexError as e:
        print(f"Error: {e}")

    try:
        data_manager.update_card(-1, korean="잘자요")
    except IndexError as e:
        print(f"Error: {e}")

    try:
        data_manager.delete_card(5)
    except IndexError as e:
        print(f"Error: {e}")
