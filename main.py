import datetime as dt
from smtplib import *
import random

my_email = "jahshuabr@yahoo.com"
password = "vzuqewqyngfleati"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:

    with open("quotes.txt", "r") as quotes:
        data = quotes.readlines()
        quote = random.choice(data)

    # Opening connection
    with SMTP("smtp.mail.yahoo.com") as connection:
        # Securing Connection
        connection.starttls()
        # Login in to email
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jahshuabr@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )