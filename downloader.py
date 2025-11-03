from bs4 import BeautifulSoup as bs
import requests
import wget

url='https://www.fcuc.cl/eventos-posters/'

b=bs(requests.get(url).text)
for link in b.find_all('a'):
    if link['href'].endswith('.pdf'):
        wget.download(link.get('href'))
