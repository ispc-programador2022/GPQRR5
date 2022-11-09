from django.shortcuts import render
from gestionScrapers.models import Product
from django.http import HttpResponse


# Create your views here.

def searchProducts(request):
    return render(request,"searchProducts.html")

def search(request):
    if request.GET['prd']:
        #mensaje = f"Articulo buscado:{request.GET['prd']}"
        producto = request.GET['prd']
        if len(producto) > 30:
            mensaje = 'Texto demasiado largo'
        else:
            articulos = Product.objects.filter()
            for prod in producto.split(' '):
                articulos = articulos.filter(title__icontains=prod)
            return render(request,'resultSearch.html',{'articulos':articulos,'query':producto})
    else:
        mensaje = 'No has introducido nada'
    return HttpResponse(mensaje)

def pruebas_script(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        from mainScraper import searcherCompGamer, searcherFullHard, searcherMeli, searcherVenex
        items = request.POST['prd']
        searcherVenex(items)
        searcherFullHard(items)
        searcherCompGamer(items)
        searcherMeli(items)
        return render(request,'gracias.html')
    else:
        return render(request,'pruebas.html')
