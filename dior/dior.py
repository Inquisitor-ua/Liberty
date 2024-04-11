from bs4 import BeautifulSoup
import requests
from jopa import ins

def pars(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, "lxml")
    tovars = html.find_all('div', class_='product-tile-wrapper')
    for tovar in tovars:
        name = tovar.find_all("div", class_="product-tile__name u-text-bodycopy u-margin-bottom--xs")
        opis = ...
        ins(name, opis)

def main():
    pars(r"https://www.dior.com/ru_ru/beauty/%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B0%D0%BA%D0%B8%D1%8F%D0%B6%D0%B0/%D0%B3%D1%83%D0%B1%D1%8B/%D0%B3%D1%83%D0%B1%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BC%D0%B0%D0%B4%D1%8B")
    
if __name__ == "__main__":
    main()