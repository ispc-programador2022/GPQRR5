import django
django.setup()
import json
import requests
from bs4 import BeautifulSoup
from gestionScrapers.models import Product

def soup_def(url):
    getH = requests.get(url)
    html = getH.content
    soup = BeautifulSoup(html,'html.parser')
    return soup

def searcherVenex(busqueda: str):
    _temp = 1
    _search = True
    while _search:
        print('Buscando resultados >>>>>', _temp)
        soup = soup_def(f'https://www.venex.com.ar/resultado-busqueda.htm?keywords={busqueda.replace(" ", "%20")}&page={_temp}')
        products = soup.findAll('div', class_="item")
        for prod in products:
            if 'item item-no-stock' in str(prod):
                _search = False
                break
            prod = json.loads(
                prod.a['onclick'].split('(')[1].replace(')', ''))
            productDB = Product(
                            name=prod['name'].lower(), 
                            price=int(prod['price']))
            if Product.objects.filter(name__contains=productDB.name).exists():
                _search=False
            else:
                productDB.save()
        _temp += 1

def searcherFullHard(busqueda: str):
    print('Cargando..')
    soup = soup_def(f'https://www.fullh4rd.com.ar/cat/search/{busqueda.replace(" ", "%20")}')
    products = soup.findAll('div', class_='item product-list')
    for prod in products:
        productDB = Product(
                        name=prod.find('h3').get_text().lower(), 
                        price=int(prod.find('div',class_='price').get_text().strip().split(' ')[0].replace('$','').replace('.','').split(',')[0]))
        if Product.objects.filter(name__contains=productDB.name).exists():
            break
        else:
            productDB.save()


def searcherCompGamer(busqueda: str):
    print('Cargando..')
    dicc_categorias = {
        'microprocesador': 27,
        'placa de video': 62,
        'notebook': 58,
        'teclado': 39,
    }

    soup = soup_def(f'https://compragamer.com/?gclid=&seccion=3&cate={dicc_categorias.get(busqueda)}&listado_prod=')
    products = soup.findAll('div', class_='contenidoPrincipal')
    for prod in products:
        productDB = Product(
                        name=prod.find('span', class_='_ngcontent-rhy-c234').get_text().lower(), 
                        price=int(prod.find('span',class_='theme_precio ng-star-inserted').get_text().strip().split(' ')[0].replace('$','').replace('.','').split(',')[0]))
        if Product.objects.filter(name__contains=productDB.name).exists():
            break
        else:
            productDB.save()


def searcherMeli(busqueda: str):
    print('Cargando..')

    busq = 'placa-de-video' if busqueda =='placa de video' else busqueda
    srch = f'placa%20de%20video' if busqueda =='placa de video' else busqueda
    soup = soup_def(f'https://listado.mercadolibre.com.ar/{busq}#D[A:{srch}]')

    products = soup.findAll('div', class_='ui-search-result__content-wrapper shops__result-content-wrapper')
    for prod in products:
        prod = Product(
                        name=prod.find('h2', class_='ui-search-item__title shops__item-title').get_text().lower(), 
                        price=int(prod.find('span',class_='price-tag-text-sr-only').get_text().split(' ')[0].replace('pesos','').replace('.','').split(',')[0]))
        if Product.objects.filter(name__contains=productDB.name).exists():
            break
        else:
            productDB.save()


if __name__ == '__main__':
    items = ['microprocesador','placa de video','notebook','teclado']
    for item in items:
        searcherVenex(item)
        searcherFullHard(item)
        searcherCompGamer(item)
        searcherMeli(item)
        