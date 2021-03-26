import smtplib
import datetime as dt
import random

# my_email = "tksudharshan@infozy.tk"
# my_pass = "abcd1234"

# with smtplib.SMTP(host="smtp.yandex.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_pass)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="tksudharshan@gmail.com",
#         msg="subject:This is Test Email\n\nThis is a Body",
#     )

quotes = []

with open("quotes.txt", mode="r") as quotesFile:
    unfilteredQuotes = quotesFile.readlines()
    quotes = [quote.replace("\n", "") for quote in unfilteredQuotes]


def checktoday():
    today = dt.datetime.now()
    if today.weekday() == 5:
        return True
    else:
        return False


random_quote = random.choice(quotes)
if checktoday():
    print(random_quote)