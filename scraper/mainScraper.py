import django
django.setup()
import json
import requests
from bs4 import BeautifulSoup
from gestionScrapers.models import Venex, FullHard

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
            productDB = Venex(
                            name=product['name'].lower(), 
                            price=int(product['price']))
            if Venex.objects.filter(name__contains=productDB.name).exists():
                _search=False
            else:
                productDB.save()
        _temp += 1

def searcherFullHard(busqueda: str):
    print('Cargando..')
    urlString = f'https://www.fullh4rd.com.ar/cat/search/{busqueda.replace(" ", "%20")}'
    getURL = requests.get(urlString)
    html = getURL.content
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.findAll('div', class_='item product-list')
    for product in products:
        productDB = FullHard(
                        name=product.find('h3').get_text().lower(), 
                        price=int(product.find('div',class_='price').get_text().split(' ')[0].replace('$','').replace('.','').split(',')[0]))
        if FullHard.objects.filter(name__contains=productDB.name).exists():
            break
        else:
            productDB.save()

if __name__ == '__main__':
    items = ['microprocesador','placa de video','notebook','teclado']
    for item in items:
        searcherVenex(item)
        searcherFullHard(item)
        