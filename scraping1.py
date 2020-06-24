import requests                        #  pip install beautifulsoup4
from bs4 import BeautifulSoup as bs    #  pip install requests

URL = 'https://www.amazon.it/Sony-Fotocamera-Mirrorless-Intercambiabile-Stabilizzazione/dp/B00Q2KEUFI/ref=sr_1_3?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1592925788&sr=8-3'
#URL = 'https://www.amazon.it/'
r = requests.get(URL)
contenuto = bs(r.text, features="html.parser")


#print(contenuto.prettify())
#print(contenuto.title)
#print(contenuto.title.string)

ti = contenuto.find("span", {"id": "productTitle"})
print('OGGETTO: ',ti.text)

price = contenuto.find("span", {"class": "priceBlockStrikePriceString"})
#print(price)
print('PREZZO INTERO: ',price.text)
salesPrice = contenuto.find("span", {"class": "a-size-medium"})
#print(salesPrice)
print('PREZZO SCONTATO: ',salesPrice.text)

