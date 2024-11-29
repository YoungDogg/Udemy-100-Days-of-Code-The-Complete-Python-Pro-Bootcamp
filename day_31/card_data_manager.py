from card import Card


class CardDataManager:
    def __init__(self):
        self.cards = []

    def create_card(self, english: str, japanese: str) -> Card:
        card = Card(english=english, japanese=japanese)
        self.cards.append(card)
        return card

    def read_card(self, index: int) -> Card:
        if index < 0 or index >= len(self.cards):
            raise IndexError("Card index out of range.")
        return self.cards[index]

    def update_card(self, index: int, english: str = None, japanese: str = None):
        card = self.read_card(index)
        if english:
            card.english = english
        if japanese:
            card.japanese = japanese

    def delete_card(self, index: int):
        if index < 0 or index >= len(self.cards):
            raise IndexError("Card index out of range.")
        self.cards.pop(index)
