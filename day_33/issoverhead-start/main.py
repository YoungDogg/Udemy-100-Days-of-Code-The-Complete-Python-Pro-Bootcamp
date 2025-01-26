import math
import time

import requests
import os
import smtplib
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / "day_32" / ".env"
load_dotenv(env_path)
my_email = os.environ.get("MY_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("PASSWORD")

print((my_email, receiver_email, password))

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_near_by_me(my_pos, iss_pos):
    distance = math.sqrt(
        (my_pos["MY_LAT"] - iss_pos["iss_latitude"]) ** 2 + (my_pos["MY_LONG"] - iss_pos["iss_longitude"]) ** 2
    )
    print(f"distance: {distance}")
    if -5 <= distance <= 5:
        return True
    # return True # only for the test case
    return False


def is_it_dark_outside(cur_time, sunrise_hr, sunset_hr):
    print(f"current time: {cur_time}\n"
          f"sunset:{sunset_hr}\n"
          f"sunrise:{sunrise_hr}\n")
    if cur_time >= sunset_hr or cur_time <= sunrise_hr:
        return True
    return False


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


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

pos_mine = {"MY_LAT": MY_LAT, "MY_LONG": MY_LONG}
pos_iss = {"iss_latitude": iss_latitude, "iss_longitude": iss_longitude}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_now_hr = time_now.hour

while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    # If the ISS is close to my current position
    # and it is currently dark
    if is_near_by_me(pos_mine, pos_iss) and is_it_dark_outside(time_now_hr, sunrise, sunset):
        # Then email me to tell me to look up.
        print("email: look up")
        send_email(
            sender=my_email, sender_password=password,
            receiver=receiver_email,
            msg_head="look up",
            msg_body="ISS is up in the sky."
        )
