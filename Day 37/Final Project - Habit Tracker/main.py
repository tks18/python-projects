import requests
import datetime
from env import TOKEN

USERNAME = "tks18"
GRAPH_ID = "coding"

api = {
    "creation": "https://pixe.la/v1/users",
    "graph": f"https://pixe.la/v1/users/{USERNAME}/graphs",
    "value": f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",
}

HEADERS = {"X-USER-TOKEN": TOKEN}


def create_user_account(username):
    details = {
        "token": TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    account_request = requests.post(url=api["creation"], json=details)
    response = account_request.json()
    return response["isSuccess"]


def create_graph_definition(id, graph_name):
    details = {
        "id": id,
        "name": graph_name,
        "unit": "commit",
        "type": "int",
        "color": "ajisai",
        "timezone": "Asia/Kolkata",
    }
    graph_request = requests.post(url=api["graph"], headers=HEADERS, json=details)
    response = graph_request.json()
    print(response)


def post_value_to_graph():
    today = datetime.datetime.today()
    formatted_date = today.strftime("%Y%m%d")

    details = {"date": formatted_date, "quantity": "2"}
    graph_request = requests.post(url=api["value"], headers=HEADERS, json=details)
    response = graph_request.json()
    print(response)


post_value_to_graph()