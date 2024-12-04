class GameFlow:
    """
    Controls the game from start to end.
    """

    def __init__(self, card_deck):
        """
        Initializes the GameFlow with a card deck.
        """
        self.card_deck = card_deck
        self.current_index = 0

    def game_start(self):
        """
        Shuffles the deck and prepares the game.
        """
        if len(self.card_deck) == 0:
            raise ValueError("Cannot start game: The deck is empty.")
        self.card_deck.shuffle()
        self.current_index = 0
        print("Game started! The deck has been shuffled.")

    def display_card(self, card):
        """
        Displays the current card.
        """
        print(f"Japanese: {card.japanese}")

    def get_user_input(self):
        """
        Gets input from the user.
        """
        while True:
            response = input("Do you know this word? (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'.")

    def is_game_over(self):
        """
        Checks if the game is over.
        """
        return len(self.card_deck) == 0

    def game_process(self):
        """
        Main game loop.
        """
        while not self.is_game_over():
            current_card = self.card_deck[self.current_index]
            self.display_card(current_card)
            user_knows = self.get_user_input()
            if user_knows:
                current_card.isChecked = True
                self.card_deck.discard_from_deck(self.current_index)
                if self.current_index >= len(self.card_deck):
                    self.current_index = 0
            else:
                print(f"{current_card.japanese} : {current_card.korean}")
                self.current_index += 1
                if self.current_index >= len(self.card_deck):
                    self.current_index = 0
            print(f"=============================================")
        self.game_over()

    def game_over(self):
        """
        Handles the end of the game.
        """
        print("Game Over! You've reviewed all the cards.")


if __name__ == "__main__":
    from card_deck import CardDeck
    from card import Card

    # Create a deck with some cards
    deck = CardDeck()
    deck.add_to_deck(Card(korean="안녕하세요", japanese="こんにちは"))
    deck.add_to_deck(Card(korean="사랑해요", japanese="愛しています"))
    deck.add_to_deck(Card(korean="감사합니다", japanese="ありがとうございます"))

    # Initialize the game flow
    game = GameFlow(deck)
    game.game_start()
    game.game_process()
