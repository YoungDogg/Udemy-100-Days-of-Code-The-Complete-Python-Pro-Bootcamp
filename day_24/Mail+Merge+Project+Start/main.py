# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


def main():
    # get the name list
    with open('Input/Names/invited_names.txt', 'r') as f:
        name_list = []
        for name in f.readlines():
            stripped = name.strip()
            name_list.append(stripped)

    # change the receiver's name
    with open('Input/Letters/starting_letter.txt', 'r') as f:
        letter = f.read()
        for name in name_list:
            new_letter = letter.replace(PLACEHOLDER, name).strip()
            # Make the file's name
            # Save the letters
            with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as filled_letter:
                filled_letter.write(new_letter)


if __name__ == "__main__":
    main()
