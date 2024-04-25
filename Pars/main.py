from requests import Session
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}

url = 'https://quotes.toscrape.com/login'

work = Session()

work.get('https://quotes.toscrape.com', headers=headers)

response = work.get(url, headers=headers)
html = BeautifulSoup(response.text, 'lxml')
token = html.find('div', class_='container').find('input').get('value')

data = {"username": '123', 'password': '098', 'csrf_token': token}

response = work.post(url, headers=headers, data=data, allow_redirects=True)
print(response.text)