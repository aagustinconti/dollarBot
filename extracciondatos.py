#scrapping es extraer informacion de la web de manera automatica
#Esto no dependen de ninguna api, ni de el tiempo de extraccion ni del contenido que puedo extraer
#La desventaja es que dependo de la estructura del contenido


import urllib.request
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pytz



def extraccionValor():

    #get the data

    data = urllib.request.urlopen('http://www.dolarhoy.com/').read().decode()
    
    #load data into a bs4

    soup = BeautifulSoup(data ,'html.parser')

    #we need to split the table of data of the rest of page data

    divTabla = soup.find('div', {'class': 'table-responsive'})
    tablaValores = divTabla.find('table')
    cuerpoTabla = tablaValores.find('tbody')

    listaTd = [] #to store the values

    for tr in cuerpoTabla.find_all('tr'):
        
        #for each td of tr choose the 1st 
        valores = tr.find_all('td',{'class':'number'})[0].text.strip()
        listaTd.append(valores)

        #for each td of tr choose the 2nd
        valores = tr.find_all('td',{'class':'number'})[1].text.strip()
        listaTd.append(valores)



    compraNacion = listaTd[0]
    ventaNacion = listaTd[1]
    compraLibre = listaTd[2]
    ventaLibre = listaTd[3]

 

    #time zone

    
    tz = pytz.timezone('America/Argentina/Buenos_Aires')

    #actual time 
    now= datetime.now(tz)
    horas = now.hour
    minutos = now.minute
    dia = now.day
    mes = now.month
    anio = now.year


    #the final message

    valorDeSalida = "Dólar BN: " + compraNacion + " | " + ventaNacion + ". Dólar Libre: " + compraLibre + " | " + ventaLibre + ". A las " + str(horas) + " horas y " + str(minutos) + " minutos del " + str(dia) + "/" + str(mes) + "/" + str(anio) +". " + "Fuente: dolarhoy.com" + " | #educational #programming #bot #python #economia #argentina"

    return valorDeSalida


