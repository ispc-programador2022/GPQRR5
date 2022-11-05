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
            articulos = Product.objects.filter(name__icontains=producto)
            return render(request,'resultSearch.html',{'articulos':articulos,'query':producto})
    else:
        mensaje = 'No has introducido nada'
    return HttpResponse(mensaje)
