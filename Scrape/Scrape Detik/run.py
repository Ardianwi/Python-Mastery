import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def home():
    return render_template('index.html')


@app.route ('/detik-populer')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})

    artikel = soup.findAll(attrs={'class': 'list-content__item'})

    images = soup.findAll(attrs={'class': 'media__image'})

    titles = soup.findAll(attrs={'class': 'media__title'})

    text = soup.findAll(attrs={'class': 'media__text'})

    return render_template('index.html', images = images)






if __name__ == '__main__':
    app.run(debug=True)