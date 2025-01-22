"""
Extra Hard Starting Project

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
"""
import datetime as dt
import os

import pandas as pd
import random


def directory_check(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist or is invalid.")
    else:
        print(f"Directory {directory} is valid")
        subdirectory = os.listdir(directory)

        print(subdirectory)


def get_letter(directory_path, name="Unknown"):
    txt_files = [
        filename for filename in os.listdir(directory_path)
        if filename.endswith(".txt")
    ]
    if not txt_files:
        return "No text files found in the directory"
    else:
        chosen_letter = random.choice(txt_files)

        # Build the full file path
        letter_path = os.path.join(directory_path, chosen_letter)

        # read the file
        # change [Name] part
        with open(letter_path, 'r') as letter_file:
            content = letter_file.read()

        named_content = content.replace("[NAME]", name)
        print(named_content)
        return named_content


def check_whos_birthday(birthday_dir, letter_dir):
    with open(birthday_dir, 'r') as file:
        df = pd.read_csv(file)

    for month, day, name, email in zip(df["month"], df["day"], df["name"], df["email"]):
        if month == today["month"] and day == today["day"]:
            print(f"it's {name}'s birthday! \n Email:{email}")
            get_letter(letter_dir, name)
            print("***send to email***")



today = {"month": dt.datetime.now().month, "day": dt.datetime.now().day}
# Pick a random letter txt
birthday_directory_path = "birthdays.csv"
letter_directory_path = "letter_templates"

directory_check(letter_directory_path)
check_whos_birthday(birthday_directory_path,letter_directory_path)
