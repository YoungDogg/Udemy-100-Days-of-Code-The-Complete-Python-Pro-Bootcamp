# Card class
- ```python
    def __eq__(self, other):
        if not isinstance(other, Card):  # Check if 'other' is an instance of Card
            return NotImplemented  # If not, return NotImplemented
        return self.word == other.word and self.is_checked == other.is_checked
  ```
  - What is other?
    - `__eq__` automatically arises when comparing using `==`. `other` is the right side of `==`. 
    - `NotImplemented` returns `False` gracefully avoiding errors 



# DataFileManager class
-   ```python
    pd.DataFrame([]).to_json(self._file_name, orient="records", indent=4)
    ```
    - explain this code. ([]) what is this?
      - It creates an empty dictionary –records– dataframe.

- ```python
    return any(data["words"].apply(lambda x: x == card.word))
    ```
    - what is any?
        - It returns boolean value. True if any of iterable elements true. False if not.

- ```python
  data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
  ```
  - what is concat in here? I know it appends those.
    - Existing data and the new row –new_entry– are merged. The new line appended to the data. 
    Concat is more efficient while append is deprecated.

- ```python
    for i, row in data.iterrows():
       if row["words"] == card.word:
           data.at[i, "is_checked"] = card.is_checked
           self._write_file(data)
           return True
    ``` 
  - Why data.at[i, "is_checked"]  has two argument? What is i and does it do?
    - data.at accesses data following row –i in here– and column –is_checked.

- ```python
   def remove(self, card: Card) -> bool:
       data = self._read_file()
       if data.empty:  # No data to remove
           return False
       original_length = len(data)
       data = data[~data["words"].apply(lambda x: x == card.word)]
       if len(data) == original_length:  # No card removed
   ```
  - question: what is ~? Is it just mispelled?
    - No it’s not. ~ this negates the condition, true to false; false to true. 
  - question: then how this method can remove it?
    - data = data[...] overwrites data. With ~, inside [] only card.word matched one will be false. And [...] only saves true values.



# TestCard
- ```python
  if __name__ == "__main__":
  ```
  - script guard vs unittest
    - script guard for execution of separated script
    - unittest for test only
- ```python
    def test_invalid_language_key(self):
        """Test creating a card with an invalid language key."""
        with self.assertRaises(ValueError):
            Card(SPANISH="Hola")  # SPANISH is not in Language enum
  ```
  - what is `with`?
    - it's like more Pythonic `try-catch`. Good when managing resources.


# Test Card Deck Class
- ```python
    def test_put_back(self):
        """Test putting a card back into the deck."""
        self.deck.add_to_deck(self.card1)
        self.deck.add_to_deck(self.card2)
        self.deck.add_to_deck(self.card3)
        drawn_card = self.deck.draw_card()
        self.deck.put_back(drawn_card)
        self.assertEqual(self.deck.get_card_count(), 3)
        self.assertIn(drawn_card, self.deck._card_deck)
  ```
  - What is `self.assertIn(drawn_card, self.deck._card_deck)`?
    - It checks if `drawn_card` is in `self.deck._card_deck`
- ```python
    @patch("day_31.src.card.card_deck.Card")
    @patch("day_31.src.data.data_file_manager.DataFileManager")
    def test_from_file(self, MockDataFileManager, MockCard):
  ```
  - the arguments order following patches?
    - it's bottom up.
- ```python
  mock_file_manager = MockDataFileManager.return_value
  ```
  - In this line, what is MockDataFileManager.return_value?
    - It represents the instance of class. If omit it, accessing its method's value will be blocked
    ``` python
    mock_file_manager = MockDataFileManager
    mock_file_manager.read_file.return_value = test_data  # This doesn't work as expected
    ```
- ```python
  MockCard.side_effect = [MagicMock(spec=Card), MagicMock(spec=Card)]
  ```
  - What does `side_effect` mean?
    - In this line, it creates those 2 instances. 
    - ```python
      @classmethod
      def from_file(cls, file_manager: DataFileManager):  # test method didn't catch the class importing error
          """ Creates a CardDeck instance by loading data from a file. """
          data = file_manager.read_file()
          deck = cls()
          for _, row in data.iterrows():
              card = Card(**row['words'])
              card.is_checked = row["is_checked"]
              deck.add_to_deck(card)
          return deck
      ```
      - This method from CardDeck class is called and inside of it, this line `card = Card(**row['words'])` automatically
      - creates Card object. And `side_effect` helps make it.
- ```python
  MockCard.assert_any_call(**test_data[0]["words"])
  ```
  - `assert_any_call`, What does it do?
    - It checks if `MockCard`is called with this `(**test_data[0]["words"])`  
  - `**test_data[0]["words"]`, why kwarg is here?
    - `**` is used to unpack dictionaries. It can be used not only defining, but calling method too.
- ```python
  self.assertTrue(all(isinstance(card, MagicMock) for card in deck._card_deck))
  ```
  - `isinstance`, what is this?
    - `(isinstance(card, MagicMock)` this method checks if card is an instance of `MagicMock`. If not, it returns `False`.      


# Game Controller Class
- ```python
  """from this code to"""
  self.game_controller = GameController()
  self.game_controller.card_deck = self.mock_deck
  
  """to this"""
  self.game_controller = GameController(card_deck=self.mock_deck)  # Inject mock deck into GameController
  ```
  - What are benefit of the latter code?
    - The explicit argument implies the object needs attribute.
    - Keep from forgetting to set card_deck later
    - More close to encapsulation. If card_deck attribute became private or something, it will occur errors.
- ```python
        # Add cards to the mocked deck using add_to_deck
        self.mock_deck.add_to_deck.side_effect = lambda card: card  # Mock the behavior of adding cards
        self.mock_deck.draw_card.side_effect = [self.card1, self.card2, self.card3]  # Mock draw behavior
        self.mock_deck.is_empty.side_effect = [False, False, True]  # Deck becomes empty after three cards
  ```
  - Why not use `add_to_deck` in `self.mock_deck` directly?
    - To check its interaction (ensuring the method was called)
    - It's not using real _card_deck attribute. So verifying its internal behavior is not necessary.