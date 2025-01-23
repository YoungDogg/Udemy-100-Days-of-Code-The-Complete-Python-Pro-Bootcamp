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
import smtplib
from dotenv import load_dotenv
import pandas as pd
import random

load_dotenv()
my_email = os.environ.get("MY_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("PASSWORD")

today = {"month": dt.datetime.now().month, "day": dt.datetime.now().day}
# Pick a random letter txt
birthday_directory_path = "birthdays.csv"
letter_directory_path = "letter_templates"


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

def send_email(sender, sender_password, receiver, msg_head, msg_body):
    """
    Sends an email using SMTP with TLS encryption (commonly for Gmail).

    Args:
        sender (str): Sender email address.
        sender_password (str): Sender email password or app password.
        receiver (str): Receiver email address.
        msg_head (str): Email subject line.
        msg_body (str): Email body text.
    """
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender, password=sender_password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=receiver,
                msg=f"Subject:{msg_head}\n\n{msg_body}"
            )
        print("[DEBUG] Email sent successfully!")
    except Exception as e:
        print(f"[DEBUG] Email failed to send. Error: {e}")


def check_whos_birthday(birthday_dir, letter_dir):
    with open(birthday_dir, 'r') as file:
        df = pd.read_csv(file)

    for month, day, name, email in zip(df["month"], df["day"], df["name"], df["email"]):
        if month == today["month"] and day == today["day"]:
            print(f"it's {name}'s birthday! \n Email:{email}")
            birthday_letter = get_letter(letter_dir, name)
            send_email(
                sender=my_email,sender_password=password,
                receiver=receiver_email,
                msg_head="happy birthday",
                msg_body=birthday_letter
            )


if __name__ == "__main__":

    directory_check(letter_directory_path)
    check_whos_birthday(birthday_directory_path, letter_directory_path)

