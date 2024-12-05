# UI 
- Card
  - Different colors on the front and back  
- Buttons: ✅ and ❌
- "Game Over" label

# Card
- Card class
- CardDeck class
- CardCRUD class
- CardJsonManager class

# Flow
- Flow class
  - before_start_program()
    - Shuffle the deck
  - start_program()
    - Display the UI
  - main_flow_program()
    - Loop until all cards in the deck are checked.
    - If the card is clicked, flip it.
    - Determine if the card is ✅ or ❌.
      - If ✅, mark the card as checked and show the next card.
      - If ❌, shuffle the deck and show another one.
  - end_program()
    - If all cards in the deck are checked, display the "Game Over" label.