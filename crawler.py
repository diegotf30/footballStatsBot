#Football information crawler
from bs4 import BeautifulSoup
import requests
import lxml

site = requests.get('https://www.sofascore.com/es/equipo/futbol/tigres-uanl/1940')
htmlSite = BeautifulSoup(site.text, 'lxml')
print(htmlSite)

