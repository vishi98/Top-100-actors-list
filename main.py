import requests
from bs4 import BeautifulSoup

URL = "https://m.imdb.com/list/ls050274118/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_actors = soup.find_all(name="h4")

actor_titles = [actor.getText() for actor in all_actors]
actors = actor_titles[::-1]
with open("actors.txt", mode="w") as file:
    for actor in actors:
        file.write(f"{actor}\n")







