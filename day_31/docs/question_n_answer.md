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