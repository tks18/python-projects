import requests
import html

api_url = (
    "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"
)
response = requests.get(api_url)
jsonifed_resp = response.json()


def clean_data(results):
    modified_results = []
    for question in results:
        new_ques = question
        ques = html.unescape(new_ques["question"])
        new_ques["question"] = ques
        modified_results.append(new_ques)
    return modified_results


cleaned_data = clean_data(jsonifed_resp["results"])
question_data = cleaned_data
