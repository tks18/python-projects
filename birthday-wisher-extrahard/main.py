import datetime as dt, smtplib, glob, pandas, random
from pathlib import Path


birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")


def check_birthday(birthdays):
    today = dt.datetime.now()
    today_birthdays = []
    for person in birthdays:
        person_birthday = dt.datetime(
            year=person["year"], month=person["month"], day=person["day"]
        )
        if person_birthday.date() == today.date():
            today_birthdays.append(person)

    return today_birthdays


def get_letters():
    letters = [letter for letter in glob.glob("letter_templates/*.txt")]
    return letters


def format_letter(todays_birthday, letter):
    formatted_birthday_dict = []
    for person in todays_birthday:
        letter_to_send = ""
        with open(Path(letter), mode="r") as birthday_letter:
            letter_contents = birthday_letter.read()
            formatted_letter = letter_contents.replace("[NAME]", person["name"])
            letter_to_send = formatted_letter
        formatted_birthday_dict.append(
            {
                "name": person["name"],
                "email": person["email"],
                "message": letter_to_send,
            }
        )
    return formatted_birthday_dict


def sendemail(letters_to_send):
    for letter in letters_to_send:
        my_email = "tksudharshan@infozy.tk"
        my_pass = "abcd1234"

        with smtplib.SMTP(host="smtp.yandex.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            message = letter["message"]
            connection.sendmail(
                from_addr=my_email,
                to_addrs=letter["email"],
                msg=f"subject:Happy Birthday\n\n{message}",
            )


todays_birthdays = check_birthday(birthdays=birthdays)
letters_avbl = get_letters()
random_letter = random.choice(letters_avbl)
letters_to_send = format_letter(todays_birthday=todays_birthdays, letter=random_letter)
sendemail(letters_to_send=letters_to_send)