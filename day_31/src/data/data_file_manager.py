import pandas as pd
from typing import List
from day_31.src.card.card import Card, Language


class DataFileManager:
    """
    Handles file-based operations for managing card data using Pandas.

    Attributes:
        _file_name (str): Name of the JSON file for storing card data.
    """

    def __init__(self, file_name: str = "data.json"):
        self._file_name = file_name

    def create_file(self) -> None:
        """Creates the JSON file if it doesn't exist."""
        try:
            pd.DataFrame([]).to_json(self._file_name, orient="records", indent=4)
        except FileExistsError:
            pass  # File already exists, no need to create it

    def check_duplicate(self, card: Card) -> bool:
        """Checks if a card already exists in the file."""
        data = self._read_file()
        if data.empty:  # No data in file
            return False
        return any(data["words"].apply(lambda x: x == card.word))

    def save(self, card: Card) -> None:
        """Saves a card to the JSON file."""
        if self.check_duplicate(card):
            raise ValueError("Duplicate card data detected.")
        data = self._read_file()
        new_entry = {"words": card.word, "is_checked": card.is_checked}
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
        self._write_file(data)

    def update(self, card: Card) -> bool:
        """Updates a card in the JSON file if it exists."""
        data = self._read_file()
        if data.empty:  # No data to update
            return False
        for i, row in data.iterrows():
            if row["words"] == card.word:
                data.at[i, "is_checked"] = card.is_checked
                self._write_file(data)
                return True
        return False

    def remove(self, card: Card) -> bool:
        """Removes a card from the JSON file."""
        data = self._read_file()
        if data.empty:  # No data to remove
            return False
        original_length = len(data)
        data = data[~data["words"].apply(lambda x: x == card.word)]
        if len(data) == original_length:  # No card removed
            return False
        self._write_file(data)
        return True

    def _read_file(self) -> pd.DataFrame:
        """Reads data from the JSON file."""
        try:
            return pd.read_json(self._file_name, orient="records")
        except ValueError:  # If the JSON file is empty or invalid
            return pd.DataFrame([])

    def _write_file(self, data: pd.DataFrame) -> None:
        """Writes data to the JSON file."""
        data.to_json(self._file_name, orient="records", indent=4)
