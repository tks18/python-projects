from bs4 import BeautifulSoup
import requests

# with open("./website.html", mode="r") as html_page:
#     content = html_page.read()

# soup = BeautifulSoup(content, "html.parser")

# for tags in soup.find_all("a"):
#     print(tags.getText())

# compa_url = soup.select_one("p a").get("href")
# print(compa_url)

request = requests.get("https://news.ycombinator.com/")
response = request.text

soup = BeautifulSoup(response, "html.parser")
titles = soup.select(".storylink")
for title in titles:
    print(title.getText())
    print(title.get("href"))

upvotes = soup.select(".score")
for votes in upvotes:
    print(votes.getText())