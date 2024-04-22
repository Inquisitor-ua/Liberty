from bs4 import BeautifulSoup
import requests
from jopa import ins

def download(url):
    response = requests.get(url)
    for value in response.iter_content(1024*1024):
        with open('dior/images/'+url.split('/')[-1].strip('?sw=800'), 'wb') as file:
            file.write(value)

def pars(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, "lxml")
    tovars = html.find_all('div', class_='product-tile-wrapper')
    for tovar in tovars:
        name = tovar.find("div", class_="product-tile__name u-text-bodycopy u-margin-bottom--xs").text.strip('\n')
        opis = tovar.find("div", class_="product-tile__short-description u-margin-bottom--xs").text.strip('\n')
        try:
            ottenki = tovar.find("div", class_="tile-body-content js-tile-body").find("div", class_="swatchable-colors__count").text
            img_url = tovar.find("div", class_='product-tile__base-media').find('img').get('src')
        except:
            ottenki = 'Empty'
            img_url = tovar.find('div', class_='product-tile__base-media').find('img').get('src')
            print('нет')
        #image = tovar.find("div", class_="image-container position-relative js-image-container") 
        # download(img_url)
        ins(name, opis, ottenki, img_url) 

def main():
    pars(r"https://www.dior.com/ru_ru/beauty/%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B0%D0%BA%D0%B8%D1%8F%D0%B6%D0%B0/%D0%B3%D1%83%D0%B1%D1%8B/%D0%B3%D1%83%D0%B1%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BC%D0%B0%D0%B4%D1%8B")
    
if __name__ == "__main__":
    main()