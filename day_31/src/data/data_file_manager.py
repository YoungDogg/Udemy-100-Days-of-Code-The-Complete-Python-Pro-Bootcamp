import pandas as pd
from typing import List
from day_31.src.card.card import Card, Language

from enum import Enum


class Data(Enum):
    FILE_NAME = "data.json"


class DataFileManager:
    """
    Handles file-based operations for managing card data using Pandas.

    Attributes:
        _file_name (str): Name of the JSON file for storing card data.
    """

    def __init__(self, filename: str = Data.FILE_NAME.value):
        self._file_name = filename

    def create_file(self) -> None:
        """Creates the JSON file if it doesn't exist."""
        try:
            pd.DataFrame([], columns=["words", "is_checked"]).to_json(self._file_name, orient="records", indent=4)
        except FileExistsError:
            pass  # File already exists, no need to create it

    # deprecated, apply won't work
    # def check_duplicate(self, card: Card) -> bool:
    #     """Checks if a card already exists in the file."""
    #     data = self.read_file()
    #     if data.empty:  # No data in file
    #         return False
    #     return any(data["words"].apply(lambda x: dict(x) == card.word))

    def check_duplicate(self, card: Card) -> bool:
        """Checks if a card already exists in the file."""
        data = self.read_file()
        if data.empty:  # No data in file
            return False
        for existing_card in data["words"]:
            if self._normalize_keys(existing_card) == card.word:
                return True
        return False

    def save(self, card: Card) -> None:
        """Saves a card to the JSON file."""
        if self.check_duplicate(card):
            raise ValueError("Duplicate card data detected.")
        data = self.read_file()
        new_entry = {"words": card.word, "is_checked": card.is_checked}
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
        self._write_file(data)

    def update(self, cards: List[Card]) -> bool:
        """
        Updates one or more cards in the JSON file if they exist.
        Returns True if at least one card was updated, False otherwise.
        """
        is_updated_any = False
        data = self.read_file()
        if data.empty:  # No data to update
            return False

        # Loop over each card passed in
        for card in cards:
            for i, row in data.iterrows():
                if self._normalize_keys(row["words"]) == card.word:
                    data.at[i, "is_checked"] = card.is_checked
                    is_updated_any = True

        if is_updated_any:
            self._write_file(data)
            return True

        return False

    def remove(self, card: Card) -> bool:
        """Removes a card from the JSON file if it exists."""
        data = self.read_file()
        if data.empty:  # No data to remove
            return False

        for i, row in data.iterrows():
            if self._normalize_keys(row["words"]) == card.word:
                data.drop(index=i, inplace=True)
                self._write_file(data.reset_index(drop=True))  # Write back without the dropped row
                return True

        return False

    def read_file(self) -> pd.DataFrame:
        """Reads data from the JSON file."""
        try:
            return pd.read_json(self._file_name, orient="records")
        except ValueError:  # If the JSON file is empty or invalid
            return pd.DataFrame([], columns=["words", "is_checked"])

    def _write_file(self, data: pd.DataFrame) -> None:
        """Writes data to the JSON file."""
        data.to_json(self._file_name, orient="records", indent=4)

    def _normalize_keys(self, words: dict) -> dict:
        """Converts stringified keys in a dictionary to Language enums."""
        return {Language[key.split(".")[1]]: value for key, value in words.items()}


# Example usage
if __name__ == "__main__":
    from day_31.src.data.data_file_manager import DataFileManager
    import pandas as pd

    # Initialize the DataFileManager
    file_name = "data.json"
    data_manager = DataFileManager(file_name)

    # Check if the file can be read properly
    try:
        print("Reading data from the file...")
        df = data_manager.read_file()
        if df.empty:
            print(f"The file `{file_name}` is empty or could not be read.")
        else:
            print(f"Data read successfully from `{file_name}`:")
            print(df)  # Print the DataFrame to check its contents
    except Exception as e:
        print(f"An error occurred while reading `{file_name}`: {e}")
