from requests import Session
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}

url = 'https://scrapingclub.com/exercise/basic_login/'

work = Session()

response = work.get(url, headers=headers)
html = BeautifulSoup(response.text, 'lxml')
token = html.find('div', class_='my-4 mt-4').find('input').get('value')

data = {"name": '123', 'password': '098', 'csrfmiddlewaretoken': token}

response = work.post(url, headers=headers, data=data, allow_redirects=True)