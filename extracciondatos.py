#scrapping es extraer informacion de la web de manera automatica
#Esto no dependen de ninguna api, ni de el tiempo de extraccion ni del contenido que puedo extraer
#La desventaja es que dependo de la estructura del contenido


import urllib.request
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pytz
import numpy as np



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

    return [compraNacion, ventaNacion, compraLibre, ventaLibre]

extraccionPagina = extraccionValor()

compraNacion= extraccionPagina[0]
ventaNacion= extraccionPagina[1]
compraLibre= extraccionPagina[2]
ventaLibre= extraccionPagina[3]




def valorDolar(subeOBaja, nacionOLibre, pesoVsDolar, valoresNuevos):
    
    compraOficialNuevo, ventaOficialNuevo, compraLibreNuevo, ventaLibreNuevo = valoresNuevos
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

    if nacionOLibre:

        valorDeSalida = str(subeOBaja) + " a $ " + str(compraLibreNuevo) + " | $ " + str(ventaLibreNuevo) + " y UN (1) Peso Argentino equivale a "+str(pesoVsDolar)+"U$D. A las " + str(horas) + " horas y " + str(minutos) + " minutos del " + str(dia) + "/" + str(mes) + "/" + str(anio) +". " +  "#DolarLibre #DolarBlue"
    
    else:

        valorDeSalida = str(subeOBaja) + " a $ " + str(compraOficialNuevo) + " | $ " + str(ventaOficialNuevo) + ". A las " + str(horas) + " horas y " + str(minutos) + " minutos del " + str(dia) + "/" + str(mes) + "/" + str(anio) +". " +  "#DolarOficial"

    
    return valorDeSalida



