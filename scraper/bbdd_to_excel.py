import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
import django
django.setup()
from gestionScrapers.models import Product
import pandas as pd

productos = Product.objects.all()
df = {
    'Página':[producto.page for producto in productos],
    'Titulo':[producto.title for producto in productos],
    'Precio':[producto.price for producto in productos],
    'Marcas':[producto.brand for producto in productos],
    'Links':[producto.link for producto in productos]
    }
df = pd.DataFrame(df)
df.to_excel('data.xlsx')