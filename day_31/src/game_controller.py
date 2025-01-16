from day_31.src.card.card_deck import CardDeck
from day_31.src.data.data_file_manager import DataFileManager, Data

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
        """
        Initializes the card deck, loads data from file, and shuffles the deck.
        """
        print("Starting before_start()...")
        try:
            # Step 1: Initialize file manager and load deck
            print("Initializing DataFileManager...")
            file_manager = DataFileManager()

            print("Loading card deck from file...")
            self.card_deck = CardDeck.from_file(file_manager)

            # Step 2: Check if the deck is empty
            if self.card_deck.is_empty():
                print("Deck is empty after loading from file!")
                return

            # Step 3: Shuffle the deck and print its state
            print("Shuffling the deck...")
            self.card_deck.shuffle_deck()
            print(f"Deck shuffled successfully: {self.card_deck._card_deck}")

        except FileNotFoundError as e:
            print(f"Error: data.json file not found! Details: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred in before_start: {e}")
            raise
        finally:
            print("Exiting before_start()")

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



import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    logging.debug("Initializing GameController...")

    # Get the base path of the script and construct the file path for data.json
    base_path = Path(__file__).resolve().parent / "data"  # Stay in src and add the "data" directory
    file_name = base_path / Data.FILE_NAME.value  # Construct the full path to the data.json file
    logging.debug(f"Base path: {base_path}")
    logging.debug(f"Full path to data file: {file_name}")

    # Initialize the GameController and DataFileManager
    game = GameController()
    file_manager = DataFileManager(str(file_name))

    try:
        logging.debug("Attempting to read the file...")
        data = file_manager.read_file()

        if data.empty:
            logging.debug("Data file is empty. Creating an empty file...")
            file_manager.create_file()
            logging.info(f"No cards in {file_name}. Please populate the file with card data.")
        else:
            logging.debug(f"Loading cards from {file_name}...")
            game.card_deck = CardDeck.from_file(file_manager)

            logging.debug("Shuffling the deck and starting the game...")
            game.before_start()
            logging.debug(f"Shuffled Deck: {game.card_deck._card_deck}")
            game.play_game()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
