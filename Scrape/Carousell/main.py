import bs4
from bs4 import BeautifulSoup
import requests

url =  'https://id.carousell.com/'

contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')

data = response.findAll('div','D_HM D_QX')

for datas in data:
    print (datas.text)

