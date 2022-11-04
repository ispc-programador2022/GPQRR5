import requests
from bs4 import BeautifulSoup

urlString = 'https://mercadolibre.com.ar'
getH = requests.get(urlString)
h = getH.content
soup = BeautifulSoup(h,'html.parser')