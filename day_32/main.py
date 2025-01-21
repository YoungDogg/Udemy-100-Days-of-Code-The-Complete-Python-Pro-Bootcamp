import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random


def get_quote(filepath):
    """
    Reads quotes (one per line) from a text file and returns a random quote.

    Args:
        filepath (str): Path to the text file.

    Returns:
        str: A randomly chosen quote from the file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return random.choice(lines)


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


if __name__ == "__main__":
    load_dotenv()
    my_email = os.environ.get("MY_EMAIL")
    receiver_email = os.environ.get("RECEIVER_EMAIL")
    password = os.environ.get("PASSWORD")

    # Basic check for missing env variables
    if not my_email or not receiver_email or not password:
        print("[DEBUG] Missing environment variables! Please set MY_EMAIL, RECEIVER_EMAIL, and PASSWORD.")
    else:
        current_weekday = dt.datetime.now().weekday()  # Monday=0, Tuesday=1, ...
        if current_weekday == 1:  # Example: Tuesday
            quote = get_quote(filepath="quotes.txt")
            send_email(
                sender=my_email,
                sender_password=password,
                receiver=receiver_email,
                msg_head="Happy Birthday!",
                msg_body=quote
            )
