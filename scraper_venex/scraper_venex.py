import requests
from bs4 import BeautifulSoup

urlString = 'https://www.venex.com.ar/'
getH = requests.get(urlString)
h = getH.content
soup = BeautifulSoup(h,'html.parser')