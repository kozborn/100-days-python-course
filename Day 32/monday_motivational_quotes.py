import datetime as dt
import smtplib
import random
from passwd import app_password, my_email

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    try:
        with open('./Birthday Wisher (Day 32) start/quotes.txt', 'r') as file:
            all_quotes = file.readlines()

    except FileNotFoundError:
        print("File not found.")

    else:
        quote = all_quotes[random.randint(0, len(all_quotes) - 1)]
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="budget4you.cc@gmail.com",
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )



