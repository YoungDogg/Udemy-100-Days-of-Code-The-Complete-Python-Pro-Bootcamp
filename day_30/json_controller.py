import pandas as pd
import os


class JSONData:
    def __init__(self, file):
        if not isinstance(file, str) or not file.endswith(".json"):
            raise ValueError("File must be a valid JSON file path.")

        self.file = file

    def create(self, data):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary to create a JSON file.")

        try:
            pd.DataFrame(data).to_json(self.file)
        except Exception as e:
            print(f"Error creating JSON file: {e}")

    def read(self):
        try:
            if not os.path.exists(self.file):
                raise FileNotFoundError(f"{self.file} does not exist.")
            data = pd.read_json(self.file)
            if data.empty:
                print("Warning: JSON file is empty.")
            return data
        except ValueError:
            print("Invalid JSON format.")
            return pd.DataFrame()
        except FileNotFoundError as e:
            print(e)
            return pd.DataFrame()

    def update(self, condition_col, condition_val, update_col, update_val):
        data_file = self.read()
        if condition_col not in data_file.columns or update_col not in data_file.columns:
            raise KeyError(f"Column '{condition_col}' or '{update_col}' does not exist in the JSON file.")
        # e.g.  df.loc[df['name'] == 'Alice', 'age'] = 26
        data_file.loc[data_file[condition_col] == condition_val, update_col] = update_val
        data_file.to_json(self.file, orient="records")

    def delete(self, condition_col, condition_val):
        data_file = self.read()
        if condition_col not in data_file.columns:
            raise KeyError(f"Column '{condition_col}' does not exist in the JSON file.")
        data_file = data_file[data_file[condition_col] != condition_val]
        data_file.to_json(self.file, orient="records")
