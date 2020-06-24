import requests                        #  pip install beautifulsoup4
from bs4 import BeautifulSoup as bs    #  pip install requests

URLs = [
    'https://www.amazon.it/Sony-Fotocamera-Mirrorless-Intercambiabile-Stabilizzazione/dp/B00Q2KEUFI/ref=sr_1_3?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1592925788&sr=8-3',
    'https://www.amazon.it/Aigostar-Forest-Mist-33JTU-ION/dp/B077F8S348?smid=A2N1516CEJ317P&pf_rd_r=ADQ6HCSAQMV4798GKBF8&pf_rd_p=652b8325-ce6e-4a91-82f2-db00045ee373'
]

for URL in URLs:
    r = requests.get(URL)
    contenuto = bs(r.text, features="html.parser")
    ti = contenuto.find("span", {"id": "productTitle"})
    price = contenuto.find("span", {"class": "priceBlockStrikePriceString"})
    salesPrice = contenuto.find("span", {"class": "a-size-medium"})
    print('LINK: ', URL + '\n\nOGGETTO:',ti.text + 'PREZZO INTERO: \n',price.text + '\nPREZZO SCONTATO: ',salesPrice.text)


print('-------------------------------------------------------------------------------------------------------------------------------------')






