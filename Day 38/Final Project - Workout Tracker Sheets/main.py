import requests
import datetime
from env import APP_ID, APP_KEY, SHEETY_TOKEN

NLP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POINT = "https://api.sheety.co/20e59a28ba4db6552fe1d9924c6c800e/test/workouts"


def process_NL(text):
    headers = {
        "x-app-id": str(APP_ID),
        "x-app-key": str(APP_KEY),
    }

    data = {"query": text}

    nl_request = requests.post(NLP_ENDPOINT, headers=headers, json=data)
    response = nl_request.json()
    return response


def track_sheet(nl_response):
    for exercise in nl_response["exercises"]:
        today = datetime.datetime.today()
        formatted_date = today.strftime("%d/%m/%Y")
        formatted_time = today.strftime("%H:%M:%S")

        headers = {"Authentication": f"Bearer {SHEETY_TOKEN}"}

        data = {
            "workout": {
                "date": formatted_date,
                "time": formatted_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

        sheety_request = requests.post(url=SHEETY_POINT, json=data)
        response = sheety_request.json()
        print(response)


text = input("\nEnter the workout in Natural Language ? ")
nl_response = process_NL(text=text)
track_sheet(nl_response=nl_response)