from django.shortcuts import render
from gestionScrapers.models import Product

# Create your views here.

def searchProducts(request):
    try:
        if request.GET['prd']:
            producto = request.GET['prd']
            select = request.GET['select']
            #price = request.GET['price_toogle']
            if len(producto) > 30:
                return render(request, "Texto demasiado largo")
            else:
                articulos = Product.objects.all()
                if select == 'page':
                    articulos = articulos.filter(page__icontains=producto)
                elif select == 'title':
                    for prod in producto.split(' '):
                        articulos = articulos.filter(title__icontains=prod)
                elif select == 'brand':
                    articulos = articulos.filter(brand__icontains=producto)
                return render(request, 'resultSearch.html', {'articulos': articulos, 'query': producto})
        else:
            return render(request, '404.html')
    except:
        return render(request, "resultSearch.html", {'primera_busqueda': True})


def pruebas_script(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        from mainScraper import searcherCompGamer, searcherFullHard, searcherMeli, searcherVenex
        items = request.POST['prd']
        searcherVenex(items)
        searcherFullHard(items)
        searcherCompGamer(items)
        searcherMeli(items)
        return render(request, 'gracias.html')
    else:
        return render(request, 'pruebas.html')
