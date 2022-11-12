from django.shortcuts import render
from gestionScrapers.models import Product
import numpy as np

# Create your views here.

def searchProducts(request):
    try:
        if request.GET['prd']:
            producto = request.GET['prd']
            select = request.GET['select']
            price = request.GET['pricer']
            pages = {
                'Full Hard':{'rangos':[],'productos':[],'precios':[]},
                'Venex':{'rangos':[],'productos':[],'precios':[]},
                'Mexx':{'rangos':[],'productos':[],'precios':[]},
                'Mercado Libre':{'rangos':[],'productos':[],'precios':[]}}    
            if len(producto) > 30:
                return render(request, "Texto demasiado largo")
            else:
                if price == 'asc':
                    articulos = Product.objects.all().order_by('-price')
                elif price == 'desc':
                    articulos = Product.objects.all().order_by('price')

                if select == 'page':
                    articulos = articulos.filter(page__icontains=producto)
                    pages = {f'{producto}':{'rangos':[],'productos':[],'precios':[]}}
                elif select == 'title':
                    for prod in producto.split(' '):
                        articulos = articulos.filter(title__icontains=prod)

                for page in pages.keys():
                    pages[page]['productos'].append(articulos.filter(page__icontains = page))
                    for prod in pages[page]['productos'][0]:
                        pages[page]['precios'].append(prod.price)

                for page in pages.keys():
                    pages[page]['varianza'] = round(np.var(pages[page]['precios'])**0.5)

                for page in pages.keys():
                    if price == 'asc':
                        pages[page]['rangos'].append(pages[page]['productos'][0][0])
                        pages[page]['rangos'].append(pages[page]['productos'][0].reverse()[0])
                    elif price == 'desc':
                        pages[page]['rangos'].append(pages[page]['productos'][0].reverse()[0])
                        pages[page]['rangos'].append(pages[page]['productos'][0][0])
                    else:
                        continue

                return render(request, 'resultSearch.html', {'articulos': articulos, 'query': producto,'paginas':pages})
        else:
            return render(request, '404.html')
    except Exception as e:
        return render(request, "resultSearch.html", {'primera_busqueda': True})


def pruebas_script(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        from mainScraper import searcherCompGamer, searcherFullHard, searcherMeli, searcherVenex
        items = request.POST['prd']
        venex = searcherVenex(items)
        full_hard = searcherFullHard(items)
        #searcherCompGamer(items)
        #searcherMeli(items)
        return render(request, 'gracias.html',{'venex':venex,'full_hard':full_hard})
    else:
        return render(request, 'pruebas.html')

