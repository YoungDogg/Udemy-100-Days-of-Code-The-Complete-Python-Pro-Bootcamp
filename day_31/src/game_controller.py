from day_31.src.card.card_deck import CardDeck


class GameController:
    """
    GameController manages the flow of the card game.

    Attributes:
        card_deck (CardDeck): The card deck, loaded from a JSON file.
    """

    def __init__(self, card_deck=None):
        self.card_deck = card_deck or CardDeck()
        self.current_card = None

    def before_start(self):
        """Assign the card deck and shuffle the card deck."""
        try:
            # Load the deck from the file
            self.card_deck = CardDeck.from_file("data.json")

            # Check if the deck is empty
            if self.card_deck.is_empty():
                print("Error: The deck is empty!")
                return

            # Shuffle the deck
            self.card_deck.shuffle_deck()
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

    def handle_button_click(self, button_clicked: str) -> None:
        """
        Handles button clicks and progresses the game.

        Args:
            button_clicked (str): The button clicked ('✅' or '❌').

        Raises:
            ValueError: If the button clicked is invalid.
        """
        # Check if the deck is valid
        if not self._is_deck_valid():
            print("Card deck is not initialized or empty.")
            self.end()
            return

        # Validate and log the button click
        button_clicked = self._validate_button(button_clicked)
        print(f"Button Clicked: {button_clicked}")
        print(f"Current Card Before Action: {self.current_card}")

        # Handle the button action
        if button_clicked == "✅":
            self.current_card.check()
            print(f"Card Checked: {self.current_card.is_checked}")
        elif button_clicked == "❌":
            self.current_card.uncheck()
            print(f"Card Unchecked: {self.current_card.is_checked}")

        # Handle the last card
        if self.card_deck.is_empty():
            print(f"Last card processed: {self.current_card}")
            self.end()
            return

        # Draw the next card
        self.current_card = self.card_deck.draw_card()
        print(f"Next Card Drawn: {self.current_card}")
        print(f"Deck After Drawing: {self.card_deck._card_deck}")

    def _is_deck_valid(self) -> bool:
        """Helper to check if the card deck is valid."""
        return self.card_deck and not self.card_deck.is_empty()

    def _validate_button(self, button_clicked: str) -> str:
        """Validates and converts button input."""
        if button_clicked not in ["✅", "❌"]:
            raise ValueError("Invalid button clicked.")
        return button_clicked

    def end(self):
        """Handle game over logic."""
        print("Game over! Thanks for playing!")  # Replace with proper UI handling

    def play_game(self):
        """Runs the game loop until the deck is empty."""
        print("Game started! Good luck!")
        self.start()  # Initialize the game

        while not self.card_deck.is_empty():
            # Prompt the user for input
            button_clicked = input("Press 'v' to check or 'x' to uncheck: ").strip().lower()

            if button_clicked not in ["v", "x"]:
                print("Invalid input! Please enter 'v' or 'x'.")
                continue

            # Map input to the appropriate action
            if button_clicked == "v":
                button_clicked = "✅"
            elif button_clicked == "x":
                button_clicked = "❌"

            try:
                self.during_progress(button_clicked)
            except ValueError as e:
                print(f"Invalid input: {e}")

        self.end()

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
    game.handle_button_click("✅")
    print(f"Next Card: ``{game.current_card}``")
    print(f"Deck After Progress: ``{game.card_deck._card_deck}``")

    print("\nDuring Progress: ❌ Button Clicked")
    game.handle_button_click("❌")
    print(f"Next Card: ``{game.current_card}``")
    print(f"Deck After Progress: ``{game.card_deck._card_deck}``")

    # Simulate ending the game when the deck is empty
    while not game.card_deck.is_empty():
        print(f"Deck Status Before Progress: {game.card_deck._card_deck}")
        game.handle_button_click("✅")
        print(f"Deck Status After Progress: {game.card_deck._card_deck}")

    game.end()
