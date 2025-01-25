##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from passwd import my_email, app_password
# 1. Update the birthdays.csv

contacts = pd.read_csv("birthdays.csv", index_col=0)
now = dt.datetime.now()

month = now.month
day = now.day

contacts = contacts[(contacts['month'] == month) & (contacts['day'] == day)]

# 2. Check if today matches a birthday in the birthdays.csv

if contacts.empty:
    print("No contacts with todays birthday found")
    exit(0)

try:
    connect = smtplib.SMTP('smtp.gmail.com', 587)
    connect.starttls()
    connect.login(my_email, app_password)
except Exception as e:
    print(e)
    exit(1)
else:
    for index, row in contacts.iterrows():
        random_letter_num = random.randint(1, 3)
        try:
            with open(f"./letter_templates/letter_{random_letter_num}.txt") as f:
                content = f.read().replace('[NAME]', row.name)
                connect.sendmail(
                    from_addr=my_email,
                    to_addrs=row.email,
                    msg=f"Subject: Happy Birthday\n\n{content}"
                )
        except FileNotFoundError:
            print("Template file not found")
            exit(2)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv



# 4. Send the letter generated in step 3 to that person's email address.
