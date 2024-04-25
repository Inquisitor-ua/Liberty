from requests import Session
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}

url = 'https://quotes.toscrape.com'

work = Session()

response = work.get(url, headers=headers)
html = BeautifulSoup(response.text, 'lxml')
token = html.find('a', href='/login')

data = {"name": '123', 'password': '098', 'csrfmiddlewaretoken': token}

response = work.post(url, headers=headers, data=data, allow_redirects=True)