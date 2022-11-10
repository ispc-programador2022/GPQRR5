from django.shortcuts import render
from gestionScrapers.models import Product

# Create your views here.

def searchProducts(request):
    try:
        if request.GET['prd']:
            producto = request.GET['prd']
            if len(producto) > 30:
                return render(request, "Texto demasiado largo")
            else:
                articulos = Product.objects.filter()
                for prod in producto.split(' '):
                    articulos = articulos.filter(title__icontains=prod)
                return render(request, 'resultSearch.html', {'articulos': articulos, 'query': producto})
    except:
        return render(request, "resultSearch.html")


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
