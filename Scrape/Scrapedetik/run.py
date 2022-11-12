import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/detikpopuler')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'nhl indeks mgb-24'})

    titles = populer_area.findAll(attrs={'class': 'media__title'})

    image = populer_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images = image)





if __name__=='__main__':
    app.run(debug=True)