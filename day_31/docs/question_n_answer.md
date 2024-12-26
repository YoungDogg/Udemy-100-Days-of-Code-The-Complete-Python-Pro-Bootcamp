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
```python
    def test_invalid_language_key(self):
        """Test creating a card with an invalid language key."""
        with self.assertRaises(ValueError):
            Card(SPANISH="Hola")  # SPANISH is not in Language enum
```
- what is `with`?
  - it's like more Pythonic `try-catch`. Good when managing resources.

# Test Card Deck Class
```python
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