from card.card_deck import CardDeck


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
            self.card_deck = CardDeck.load_from_file("data.json")  # Hypothetical method
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

    def during_progress(self, button_clicked):
        """Handle button clicks and game progression."""
        if not self.card_deck:
            print("Error: Card deck is not initialized!")
            return

        # If the card is unchecked (❌), put it back into the deck and shuffle it
        if button_clicked == "✅":
            self.current_card.check()
        elif button_clicked == "❌":
            self.current_card.uncheck()
            self.card_deck.put_back(self.current_card)  # Hypothetical method to add the card back
            self.card_deck.shuffle()  # Shuffle the deck

        # Check if the deck is empty; if so, end the game
        if self.card_deck.is_empty():
            self.end()
        else:
            self.current_card = self.card_deck.draw_card()  # Draw the next card

    def end(self):
        """Handle game over logic."""
        print("Game over! Thanks for playing!")  # Replace with proper UI handling
