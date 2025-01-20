import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("MY_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("PASSWORD")

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg="email test hahaha")
connection.close()
