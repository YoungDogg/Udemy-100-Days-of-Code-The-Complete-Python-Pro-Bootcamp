from day_31.src.card.card_deck import CardDeck
from day_31.src.data.data_file_manager import DataFileManager


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
        try:
            # Load the deck from the file
            file_manager = DataFileManager()

            self.card_deck = CardDeck.from_file(file_manager)

            # Check if the deck is empty
            if self.card_deck.is_empty():
                print("Error: The deck is empty!")
                return

            # Shuffle the deck and print its state
            print("Shuffling deck...")
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
        # Shuffle the deck
        self.card_deck.shuffle_deck()
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
        # print(f"Button Clicked: {button_clicked}")
        # print(f"Current Card Before Action: {self.current_card}")

        # Handle the button action
        if button_clicked == "✅":
            self.current_card.check()
            print(f"Card Checked: {self.current_card.is_checked}")
        elif button_clicked == "❌":
            self.current_card.uncheck()
            print(f"Card Unchecked: {self.current_card.is_checked}")

        # Draw the next card if the deck is not empty
        if not self.card_deck.is_empty():
            self.current_card = self.card_deck.draw_card()
        else:
            self.current_card = None  # No more cards to draw
            print("Processing the last card.")
            # self.end()

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
        self.current_card = None

    def play_game(self):
        """
        Runs the game loop until all cards are processed.

        The game loop repeatedly prompts the user for input, processes the current card,
        and advances to the next card. Ends when all cards are checked or discarded.
        """
        print("Game started! Good luck!")
        self.start()

        while self.current_card or not self.card_deck.is_empty():
            print(f"Current Card: {self.current_card}")

            button_clicked = input("Press 'v' to check or 'x' to uncheck: ").strip().lower()
            if button_clicked not in ["v", "x"]:
                print("Invalid input! Please enter 'v' or 'x'.")
                continue

            try:
                action = "✅" if button_clicked == "v" else "❌"
                self.handle_button_click(action)
            except ValueError as e:
                print(f"Error: {e}")

        # self.end()


if __name__ == "__main__":
    from card.card import Card
    from card.card_deck import CardDeck

    # Initialize the GameController
    game = GameController()

    # Example cards for testing
    card1 = Card(JAPANESE="こんにちは", KOREAN="안녕하세요", ENGLISH="Hello")
    card2 = Card(JAPANESE="さようなら", KOREAN="안녕히 가세요", ENGLISH="Goodbye")
    card3 = Card(JAPANESE="ありがとう", KOREAN="감사합니다", ENGLISH="Thank you")

    # Create a deck and add cards
    deck = CardDeck()
    deck.add_to_deck(card1)
    deck.add_to_deck(card2)
    deck.add_to_deck(card3)

    # Assign the deck to the controller
    game.card_deck = deck
    # Shuffle the deck and start the game
    print("\nStarting the Game...")
    game.before_start()
    print(f"Shuffled Deck: {game.card_deck.card_deck}")

    game.play_game()

