import sys
sys.path.insert(1, 'C:/Users/mikae/Desktop/PROYECTOS/Python/ISPC-proyecto-integrador/scraper')
from gestionScrapers.models import Venex
from bs4 import BeautifulSoup
import requests
import json

def searcherVenex(busqueda: str):
    _temp = 1
    _search = True
    while _search:
        print('Buscando resultados >>>>>', _temp)
        urlString = f'https://www.venex.com.ar/resultado-busqueda.htm?keywords={busqueda.replace(" ", "%20")}&page={_temp}'
        getURL = requests.get(urlString)
        html = getURL.content
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.findAll('div', class_="item")
        for product in products:
            if 'item item-no-stock' in str(product):
                _search = False
                break
            product = json.loads(
                product.a['onclick'].split('(')[1].replace(')', ''))
            productDB = Venex(name=product['name'], category=product['category'],
                              brand=product['brand'], price=int(product['price']))
        _temp += 1
    productDB.save()

lala = searcherVenex('placa de video')