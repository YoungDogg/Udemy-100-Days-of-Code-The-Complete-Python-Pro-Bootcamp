from day_31.src.card.card_deck import CardDeck


class GameController:
    """
    GameController manages the flow of the card game.

    Attributes:
        card_deck (CardDeck): The card deck, loaded from a JSON file.
    """

    def __init__(self):
        self.card_deck = None
        self.current_card = None

    def before_start(self):
        """Assign the card deck and shuffle the card deck."""
        try:
            self.card_deck = CardDeck.from_file("data.json")  # Hypothetical method
            self.card_deck.shuffle()
        except FileNotFoundError:
            print("Error: data.json file not found!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def start(self):
        """Start the game."""
        if not self.card_deck:
            print("Error: Card deck is not initialized!")
            return

        self.current_card = self.card_deck.draw_card()
        print("Game started! Good luck!")  # Replace with UI logic if needed

    def during_progress(self, button_clicked: str) -> None:
        """
        Handles button clicks and progresses the game.

        Args:
            button_clicked (str): The button clicked ('✅' or '❌').

        Raises:
            ValueError: If the button clicked is invalid.
        """
        if button_clicked not in ["✅", "❌"]:
            raise ValueError("Invalid button clicked.")

        print(f"\nButton Clicked: {button_clicked}")
        print(f"Current Card Before Action: {self.current_card}")

        if button_clicked == "✅":
            self.current_card.check()
            print(f"Card Checked: {self.current_card.is_checked}")
        elif button_clicked == "❌":
            self.current_card.uncheck()
            print(f"Card Unchecked: {self.current_card.is_checked}")

        # Handle the last card separately
        if len(self.card_deck._card_deck) == 0:
            print(f"Last card processed: {self.current_card}")
            self.end()
            return

        # Draw the next card as usual
        self.current_card = self.card_deck.draw_card()
        print(f"Next Card Drawn: {self.current_card}")
        print(f"Deck After Drawing: {self.card_deck._card_deck}")

    def end(self):
        """Handle game over logic."""
        print("Game over! Thanks for playing!")  # Replace with proper UI handling

if __name__ == "__main__":
    from card.card import Card
    from card.card_deck import CardDeck
    from game_controller import GameController

    # Example test script for GameController
    print("Initializing Game Controller...")
    game = GameController()

    # Create some cards and add them to the deck
    card1 = Card(JAPANESE="エース", KOREAN="에이스", ENGLISH="Ace")
    card2 = Card(JAPANESE="キング", KOREAN="킹", ENGLISH="King")
    card3 = Card(JAPANESE="クイーン", KOREAN="퀸", ENGLISH="Queen")
    card4 = Card(JAPANESE="10", KOREAN="10", ENGLISH="10")

    # Create and set up the deck
    deck = CardDeck()
    deck.add_to_deck(card1)
    deck.add_to_deck(card2)
    deck.add_to_deck(card3)
    deck.add_to_deck(card4)

    # Assign the deck to the game controller and shuffle
    game.card_deck = deck
    game.card_deck.shuffle_deck()
    print(f"Shuffled Deck: ``{game.card_deck._card_deck}``")

    # Start the game
    game.start()
    print(f"Current Card: ``{game.current_card}``")

    # Simulate progress
    print("\nDuring Progress: ✅ Button Clicked")
    game.during_progress("✅")
    print(f"Next Card: ``{game.current_card}``")
    print(f"Deck After Progress: ``{game.card_deck._card_deck}``")

    print("\nDuring Progress: ❌ Button Clicked")
    game.during_progress("❌")
    print(f"Next Card: ``{game.current_card}``")
    print(f"Deck After Progress: ``{game.card_deck._card_deck}``")

    # Simulate ending the game when the deck is empty
    while not game.card_deck.is_empty():
        print(f"Deck Status Before Progress: {game.card_deck._card_deck}")
        game.during_progress("✅")
        print(f"Deck Status After Progress: {game.card_deck._card_deck}")

    game.end()
