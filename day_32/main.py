import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("MY_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("PASSWORD")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg="email test hahaha")
#     connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day = now.day
# print(day)
#
# date_of_birth = dt.datetime(year=1999,month=1,day=3)
# print(date_of_birth)

"""
1. get the current day. 
2. If it matches some specific day, send a quote from a file 
"""