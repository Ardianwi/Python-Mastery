import requests
from bs4 import BeautifulSoup

html_doc =requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class':'nhl indeks mgb-24'})

titles = populer_area.findAll(attrs={'class':'media__title'})

image = populer_area.findAll(attrs={'class':'media__image'})

for images in image:
    print(images.find('a').find('img')['title'])

#print (titles)
