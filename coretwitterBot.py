import extracciondatos
import twittearConPython
import schedule
import time
from time import perf_counter


#Definimos funcion a repetir
def job1():
    tiempoInicio = time.perf_counter()
    valorDolar = extracciondatos.extraccionValor()
    irATwittear = twittearConPython.twitt(valorDolar)
    tiempoFinal = time.perf_counter()
    tiempoEjec = tiempoFinal - tiempoInicio
    print('Se twitteo el precio del dolar con exito. En ' + str(tiempoEjec) + '.')

    return 1






#De 21 a 03 va a twittear la variacion
schedule.every().day.at("00:00").do(job1) #21
schedule.every().day.at("01:00").do(job1) #22
schedule.every().day.at("02:00").do(job1) #23
schedule.every().day.at("03:00").do(job1) #00
schedule.every().day.at("04:00").do(job1) #01
schedule.every().day.at("05:00").do(job1) #02
schedule.every().day.at("06:00").do(job1) #03


#twitts dolar normales de 8 a 17
 
schedule.every().day.at("11:00").do(job1) #8
schedule.every().day.at("12:00").do(job1) #9
schedule.every().day.at("13:00").do(job1) #10

schedule.every().day.at("15:00").do(job1) #12
schedule.every().day.at("16:00").do(job1) #13

schedule.every().day.at("18:00").do(job1) #15
schedule.every().day.at("19:00").do(job1) #16
schedule.every().day.at("20:00").do(job1) #17






while True:
    schedule.run_pending()
    time.sleep(1)