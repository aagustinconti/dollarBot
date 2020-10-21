import urllib.request
from bs4 import BeautifulSoup



def data_scraping():

    data = urllib.request.urlopen('https://www.cronista.com/MercadosOnline/dolar.html').read().decode()
    
    soup = BeautifulSoup(data ,'html.parser')

    values=[]

    div_0 = soup.find('div', {'id': 'cotizaciones-dolar-actual'})    
    
    for div_1 in div_0.find_all('div', {'class': 'cotizacion col-lg-4 col-md-4 col-sm-12 col-xs-12'}):

        table = div_1.find('table', {'class': 'tabla-datos dolar-cotizacion'})

        for td in table.find_all('td', {'align': 'center'}):
            for div_value in td.find('div', {'class': 'numDolar'}):
                values.append(div_value)
        
    return values


