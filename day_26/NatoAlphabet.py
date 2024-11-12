# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd


class NatoAlphabet:
    def __init__(self):
        self.data = None
        self.phonetic_dict = {}

    def setup(self):
        try:
            self.data = pd.read_csv('../day_26/nato_phonetic_alphabet.csv')
        except FileNotFoundError as missing_file:
            print(f"{missing_file} is not found")
        else:
            for idx, row in self.data.iterrows():
                self.phonetic_dict[row.letter] = row.code

    def result(self, word):
        input_list = [letter for letter in word]
        result = [self.phonetic_dict[cha] for cha in input_list]
        return result


if __name__ == "__main__":
    n = NatoAlphabet()
    n.setup()
