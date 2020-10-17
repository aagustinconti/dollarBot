
import extracciondatos
import twittearConPython
import schedule
import time
from time import perf_counter
import csv
import numpy as np

nombre_archivo='prueba_archivo'

#buscar una vez por minuto el precio

def convertData(toFloat):

    listOfNumbers=[]
    
    for string in toFloat:
        listOfNumbers.append(float(string.strip('$').replace(',','.')))

    tupleOfNumbers = tuple(listOfNumbers)
    return tupleOfNumbers


#CSV Functions (Read & Write)

def saveData(nombre_archivo, valores):

    with open(str(nombre_archivo)+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(valores)
    csvfile.close()
    return 0

def recoverData(nombre_archivo):
    valores = []
    with open(str(nombre_archivo)+'.csv') as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            valores.append(row)

        valores.pop()

    csvfile.close()
    return valores

def checkData():

    tiempoInicio = time.perf_counter()

    valoresNuevos= convertData(extracciondatos.extraccionValor())
    valoresViejos= convertData(recoverData(nombre_archivo)[0])

    ventaNacionNuevo = valoresNuevos[1]
    ventaNacionViejo = valoresViejos[1]

    ventaLibreNuevo = valoresNuevos[3]
    ventaLibreViejo= valoresViejos[3]
    pesoVsDolar= np.round(1/ventaLibreNuevo,5)

    #DolarOficial Check
    if ventaNacionViejo != ventaNacionNuevo:

        if ventaNacionViejo > ventaNacionNuevo:

            valorDolar = extracciondatos.valorDolar("BAJÓ el Dólar Oficial",False,0)

        elif ventaNacionViejo < ventaNacionNuevo:

            valorDolar= extracciondatos.valorDolar("SUBIÓ el Dólar Oficial",False,0)
    
        
        saveData(nombre_archivo, [valoresNuevos])

        irATwittear = twittearConPython.twitt(valorDolar) #we call this module to twitt the data
        tiempoFinal = time.perf_counter() #end time
        tiempoEjec = tiempoFinal - tiempoInicio #delta time
        print("Valor viejo Oficial", ventaNacionViejo)
        print("Valor nuevo Oficial", ventaNacionNuevo)
        print('Se twitteo el precio del dolar OFICIAL con exito. En ' + str(tiempoEjec) + '[s].')

    
    
    #Descanso por si se dan ambos casos a la vez
    time.sleep(10)



    #DolarLibre check
    if ventaLibreViejo != ventaLibreNuevo:

        if ventaLibreViejo > ventaLibreNuevo:

            valorDolar = extracciondatos.valorDolar("BAJÓ el Dólar Libre",True, pesoVsDolar)

        elif ventaNacionViejo < ventaNacionNuevo:

            valorDolar = extracciondatos.valorDolar("SUBIÓ el Dólar Libre",True, pesoVsDolar)
    
        
        
        saveData(nombre_archivo, [valoresNuevos])

        irATwittear = twittearConPython.twitt(valorDolar) #we call this module to twitt the data
        tiempoFinal = time.perf_counter() #end time
        tiempoEjec = tiempoFinal - tiempoInicio #delta time
        print("Valor viejo Libre", ventaLibreViejo)
        print("Valor nuevo Libre", ventaLibreNuevo)
        print('Se twitteo el precio del dolar LIBRE con exito. En ' + str(tiempoEjec) + '[s].')

    tiempoFinal = time.perf_counter() #end time
    tiempoEjec = tiempoFinal - tiempoInicio #delta time

    return 'Checkeo realizado en ' + str(tiempoEjec) + '[s].'

def job1():
    try:
        print(checkData())
    except:
        print("Hubo un error FATAL.")


schedule.every(1).minute.do(job1)


while True:
    schedule.run_pending()
    time.sleep(1)


