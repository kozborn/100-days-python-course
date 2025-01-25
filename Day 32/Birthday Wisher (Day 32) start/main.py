import smtplib
from passwd import app_password, my_email

my_password = app_password

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    try:
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="budget4you.cc@gmail.com",
            msg="Subject:Hello\n\nTest message",
        )
    except smtplib.SMTPAuthenticationError:
        print("Login failed")
    else:
        print("Login successful")
