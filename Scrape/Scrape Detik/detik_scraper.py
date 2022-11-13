import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})

artikel = soup.findAll(attrs={'class':'list-content__item'})

images = soup.findAll(attrs={'class':'media__image'})

titles = soup.findAll(attrs={'class':'media__title'})

text = soup.findAll(attrs={'class':'media__text'})

for image in images:
    print(image.find ('a').find('img')['title'])



#print(images)