from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}
i = 1
url = f"https://scrapingclub.com/exercise/list_infinite_scroll/?page={i}"

while i <= 6:
    if i == 1:
        url ="https://scrapingclub.com/exercise/list_infinite_scroll/"
    else:
        url = f"https://scrapingclub.com/exercise/list_infinite_scroll/?page={i}"
    i += 1
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text, 'lxml')
    cards = html.find_all("div", class_="p-4")
    for card in cards:
        try:
            name = card.find("h4").text
            print(name)
        except Exception as e:
            print(e)
            



