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

def main():
    # 1. Create a dictionary in this format:
    # {"A": "Alfa", "B": "Bravo"}
    data = pd.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {}
    for idx, row in data.iterrows():
        phonetic_dict[row.letter] = row.code

    def check_input_error():
        while True:
            user_input = input("Enter a word: ").upper()

            if len(user_input) < 1:
                print("Error: You didn't type anything. Type a word")
                continue

            if not user_input.isalpha():
                print("Error: it must be a word.")
                continue

            return user_input

    # 2. Create a list of the phonetic code words from a word that the user inputs.
    word = check_input_error()
    input_list = [letter for letter in word]
    result = [phonetic_dict[cha] for cha in input_list]
    print(result)



if __name__ == "__main__":
    main()
