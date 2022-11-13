import bs4
import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/photography-6/?searchId=RAgIoW')

soup = BeautifulSoup(html_doc.text, 'html.parser')

kamera_terpopuler = soup.find(attrs={'class':'D_aCu'})

title = kamera_terpopuler.find_all(attrs={'class':'D_Rf M_acQ'})

for data in title:
    print(data.find('p',attrs= {'class':'D_in M_gZ D_gt M_fn D_io M_ha D_ir M_he D_iu M_hh D_ix M_hk D_iz M_hm D_iv M_hi D_ik'}))