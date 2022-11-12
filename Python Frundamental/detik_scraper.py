import requests
from bs4 import BeautifulSoup

url =   'https://www.detik.com/terpopuler'



res = requests.get(url)
print(res.status_code)