import requests
from bs4 import BeautifulSoup

urlString = 'https://amazon.com'
getH = requests.get(urlString)
h = getH.content
soup = BeautifulSoup(h,'html.parser')