from bs4 import BeautifulSoup
from dotenv import load_dotenv
from os import getenv, system
import requests 
import json
system("clear")
load_dotenv()


# b-content__inline_items
URL = getenv("URL")
DOMEN = getenv("DOMEN")
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"
}


def get_html(url=URL, headers=HEADERS):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"Ошибка с кодом: {response.status_code}"


def get_content(html):
    soup = BeautifulSoup(html, "lxml").find("div", {"class": "b-content__inline_items"}).find_all("div", {"class": "b-content__inline_item"})
    
    film_information = {
        "url": ""
    }

    for item in soup:
        film_photo = item.find("img").get("src")
        film_title = item.find("div", {"class": "b-content__inline_item-link"}).find("a").text
        film_url = item.find("div", {"class": "b-content__inline_item-link"}).find("a").get("href")
        film_url = item.find("div", {"class": "b-content__inline_item-link"}).find("div").text

        film_information.update({
            film_title : {
            "photo": film_url,
            }
        })
    return film_information

def parse():
    html = get_html()
    content = get_content(html)  # добавляем скобки для вызова функции
    with open("core/json/content.json", "w") as file:
        json.dump(content, file, indent=4, ensure_ascii=False)
    return "Все готово!"
    
print(parse())
