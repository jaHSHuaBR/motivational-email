import datetime as dt
from smtplib import *
import random

# Enter your login info here
my_email = "YOUR EMAIL HERE"    
password = "YOUR PASSWORD HERE"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:

    with open("quotes.txt", "r") as quotes:
        data = quotes.readlines()
        quote = random.choice(data)

    # Opening connection - Replace "smtp.mail.yahoo.com" with your emails smtp address. Gmail: smtp.gmail.com 
    with SMTP("smtp.mail.yahoo.com") as connection:
        # Securing Connection
        connection.starttls()
        # Login in to email
        connection.login(user=my_email, password=password)
        connection.sendmail(
            # INSERT YOUR "FROM EMAIL" AND "TO EMAIL" HERE:
            from_addr=my_email,
            to_addrs="jahshuabr@gmail.com",
            # The content of email (Here is the random quote)
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )
