import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
import django
django.setup()
from gestionScrapers.models import Product
import pandas as pd
import matplotlib.pyplot as plt

def bbdd_to_excel(excel = True):
    productos = Product.objects.all()
    df = {
        'Pagina':[producto.page for producto in productos],
        'Titulo':[producto.title for producto in productos],
        'Precio':[producto.price for producto in productos],
        'Links':[producto.link for producto in productos]
        }
    df = pd.DataFrame(df)
    if excel:
        df.to_excel('data.xlsx')
    else:
        return df

def ploter(pages):
    pages = pages 

    ax = plt.gca()
    if len(pages.keys()) == 1:
        for page in pages:
            df = pd.DataFrame(columns=[page])
            df[page] = pages[page]['precios']
            df.plot.line(ax=ax,color='red')
    else:
        df1 = pd.DataFrame(columns=['Full Hard'])
        df1['Full Hard'] = pages['Full Hard']['precios']
        df1.plot.line(ax=ax,color='red')

        df2 = pd.DataFrame(columns=['Venex'])
        df2['Venex'] = pages['Venex']['precios']
        df2.plot.line(ax=ax,color='green')

        df3 = pd.DataFrame(columns=['Mexx'])
        df3['Mexx'] = pages['Mexx']['precios']
        df3.plot.line(ax=ax,color='blue')

        df4 = pd.DataFrame(columns=['Mercado Libre'])
        df4['Mercado Libre'] = pages['Mercado Libre']['precios']
        df4.plot.line(ax=ax,color='yellow')

    try:
        os.remove('/home/agustin/Desktop/Proyectos_linux/ispc/web_scraper/scraper/gestionScrapers/templates/static/grafico.png')
        plt.savefig('gestionScrapers/templates/static/grafico.png') 
        plt.close()
    except:
        plt.savefig('gestionScrapers/templates/static/grafico.png') 
        plt.close()

if __name__ == '__main__':
    bbdd_to_excel()

