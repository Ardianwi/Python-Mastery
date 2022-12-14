import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def home():
    return render_template('base.html')


@app.route ('/detik-scraper')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})

    artikel = soup.findAll(attrs={'class': 'list-content__item'})

    images = soup.findAll(attrs={'class': 'media__image'})

    titles = soup.findAll(attrs={'class': 'media__title'})

    text = soup.findAll(attrs={'class': 'media__text'})

    return render_template('detik-scraper.html', images = images)


@app.route ('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html' , datas = json_data.values())



if __name__ == '__main__':
    app.run(debug=True)