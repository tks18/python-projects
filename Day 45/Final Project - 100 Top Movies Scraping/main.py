from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = request.text

soup = BeautifulSoup(content, "html.parser")

movies_list_elem = soup.find_all(name="h3", class_="jsx-4245974604")
print(movies_list_elem)