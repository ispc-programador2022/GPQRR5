from django.shortcuts import render
from gestionScrapers.models import Product

# Create your views here.

def searchProducts(request):
    try:
        if request.GET['prd']:
            producto = request.GET['prd']
            select = request.GET['select']
            price = request.GET['pricer']
            pages = {
                'full_hard':{'rangos':[],'productos':[]},
                'venex':{'rangos':[],'productos':[]}}    
            if len(producto) > 30:
                return render(request, "Texto demasiado largo")
            else:
                if price == 'asc':
                    articulos = Product.objects.all().order_by('-price')
                elif price == 'desc':
                    articulos = Product.objects.all().order_by('price')

                if select == 'page':
                    articulos = articulos.filter(page__icontains=producto)
                    pages = {f'{producto}':{'rangos':[],'productos':[]}}
                elif select == 'title':
                    for prod in producto.split(' '):
                        articulos = articulos.filter(title__icontains=prod)
                elif select == 'brand':
                    articulos = articulos.filter(brand__icontains=producto)

                for page in pages.keys():
                    pages[page]['productos'].append(articulos.filter(page__icontains = page.replace('_',' ')))

                for page in pages.keys():
                    if price == 'asc':
                        pages[page]['rangos'].append(pages[page]['productos'][0][0])
                        pages[page]['rangos'].append(pages[page]['productos'][0].reverse()[0])
                    else:
                        pages[page]['rangos'].append(pages[page]['productos'][0].reverse()[0])
                        pages[page]['rangos'].append(pages[page]['productos'][0][0])

                return render(request, 'resultSearch.html', {'articulos': articulos, 'query': producto,'paginas':pages})
        else:
            return render(request, '404.html')
    except:
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

