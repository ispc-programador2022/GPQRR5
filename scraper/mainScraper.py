import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
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
        try:
            if products[0] == soup_def(f'https://www.venex.com.ar/resultado-busqueda.htm?keywords={busqueda.replace(" ", "%20")}&page={_temp-1}').findAll('div',class_='item')[0] and _temp != 1:
                _search = False
        except IndexError:
            return 'No se encontraron resultados'
        for prod in products:
            if 'item item-no-stock' in str(prod):
                _search = False
                break
            _link = prod.a['href']
            prod = json.loads(
                prod.a['onclick'].split('(')[1].replace(')', ''))
            productDB = Product(
                            page = 'Venex',
                            title=prod['name'].lower(), 
                            price=int(prod['price']),
                            link=_link
                            )
            if Product.objects.filter(title__contains = productDB.title).exists() and productDB.price == Product.objects.filter(title__contains=productDB.title)[0].price:
                continue
            elif Product.objects.filter(title__contains=productDB.title).exists() and productDB.price != Product.objects.filter(title__contains=productDB.title)[0].price:
                update_id = Product.objects.filter(title__contains = productDB.title)[0].id
                Product.objects.filter(pk = update_id).update(price = productDB.price)
            else:
                productDB.save()
        _temp += 1

def searcherFullHard(busqueda: str):
    print('Cargando resultados de Full Hard..')
    soup = soup_def(f'https://www.fullh4rd.com.ar/cat/search/{busqueda.replace(" ", "%20")}')
    products = soup.findAll('div', class_='item product-list')
    if soup.findAll('div',class_='products')[0].find('h2'):
        return 'No se encontraron resultados'
    for prod in products:
        productDB = Product(
                        page = 'Full Hard',
                        title=prod.find('h3').get_text().lower(), 
                        price=int(prod.find('div',class_='price').get_text().strip().split(' ')[0].replace('$','').replace('.','').split(',')[0]),
                        link = f"https://www.fullh4rd.com.ar{prod.a['href']}")
        if Product.objects.filter(title__contains=productDB.title).exists() and productDB.price == Product.objects.filter(title__contains=productDB.title)[0].price:
            continue
        elif Product.objects.filter(title__contains=productDB.title).exists() and productDB.price != Product.objects.filter(title__contains=productDB.title)[0].price:
            update_id = Product.objects.filter(title__contains = productDB.title)[0].id
            Product.objects.filter(pk = update_id).update(price = productDB.price)
        else:
            productDB.save()

def searcherMexx(busqueda: str):
    print('Cargando resultados de Mexx..')
    soup = soup_def(f"https://www.mexx.com.ar/buscar/?p={busqueda.replace(' ','+')}")
    products = soup.findAll('div', class_='card-body px-3 pb-0 pt-0')
    for prod in products:
        try:
            productDB = Product(
                            page = 'Mexx',
                            title = prod.h4.get_text().replace('\n',''), 
                            price = int(prod.b.get_text().replace('$','').replace('.','')),
                            link = prod.a['href'])
        except:
            continue
        if Product.objects.filter(title__contains=productDB.title).exists() and productDB.price == Product.objects.filter(title__contains=productDB.title)[0].price:
            continue
        elif Product.objects.filter(title__contains=productDB.title).exists() and productDB.price != Product.objects.filter(title__contains=productDB.title)[0].price:
            update_id = Product.objects.filter(title__contains = productDB.title)[0].id
            Product.objects.filter(pk = update_id).update(price = productDB.price)
        else:
            productDB.save()

def searcherMeli(busqueda: str):
    print('Cargando  resultados de Mercado Libre..')
    soup = soup_def(f"https://listado.mercadolibre.com.ar/{busqueda.replace(' ','-')}#D[A:{busqueda.replace(' ','%20')}]")
    products = soup.findAll('div', class_='ui-search-result__wrapper shops__result-wrapper')
    for loop in range(1,4):
        if loop > 1:
            next_page = soup.find('a',{'title':'Siguiente'})['href']
            soup = soup_def(next_page)
            products = soup.findAll('div', class_='ui-search-result__wrapper shops__result-wrapper')
        for prod in products:
            try:
                productDB = Product(
                                page = 'Mercado Libre',
                                title = prod.find('h2').get_text().lower(),
                                price = int(prod.find('span',class_='price-tag-fraction').get_text().replace('.','')),
                                link = prod.a['href'])
            except:
                continue
            if Product.objects.filter(title__contains=productDB.title).exists() and productDB.price == Product.objects.filter(title__contains=productDB.title)[0].price:
                continue
            elif Product.objects.filter(title__contains=productDB.title).exists() and productDB.price != Product.objects.filter(title__contains=productDB.title)[0].price:
                update_id = Product.objects.filter(title__contains = productDB.title)[0].id
                Product.objects.filter(pk = update_id).update(price = productDB.price)
            else:
                productDB.save()

if __name__ == '__main__':
    items = ['microprocesador','placa de video','notebook','teclado']
    for item in items:
        searcherFullHard(item)
        searcherVenex(item)
        searcherMexx(item)
        searcherMeli(item)
        print(f'Termine de buscar: {item}\n\n\n')
        