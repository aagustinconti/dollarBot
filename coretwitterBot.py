#This is the core of the bot, here we call all of the modules for let bot to work
import extracciondatos
import twittearConPython
import schedule
import time
from time import perf_counter


#We define function to repeat ('the job')
def job1():
    tiempoInicio = time.perf_counter() #init time
    valorDolar = extracciondatos.extraccionValor() #we call this module to extract the data
    irATwittear = twittearConPython.twitt(valorDolar) #we call this module to twitt the data
    tiempoFinal = time.perf_counter() #end time
    tiempoEjec = tiempoFinal - tiempoInicio #delta time
    print('Se twitteo el precio del dolar con exito. En ' + str(tiempoEjec) + '[s].') #This message will be shown on the console, in this particular case in the bash of the Heroku server then we will be alert if everything are going well

    return 1




#Here it's important to know what the timezone of the server, which it's different to te timezone of my client (my computer, your computer)
#So i found the solution of this mistake finding the relation of the time and changing  it for my convenience.
#Also i read in some fonts what the time of the best interaction with the hashtags in my Country (Argentina) wich occurs in the time zone of 21hs to 03hs.

# Twitts of 21hs to 03hs of Argentina
schedule.every().day.at("00:00").do(job1) #21
schedule.every().day.at("01:00").do(job1) #22
schedule.every().day.at("02:00").do(job1) #23
schedule.every().day.at("03:00").do(job1) #00
schedule.every().day.at("04:00").do(job1) #01
schedule.every().day.at("05:00").do(job1) #02
schedule.every().day.at("06:00").do(job1) #03


# Twitts of 08hs to 10hs of Argentina (the oppening of te exchange market it's at 08hs)
 
schedule.every().day.at("11:00").do(job1) #8
schedule.every().day.at("12:00").do(job1) #9
schedule.every().day.at("13:00").do(job1) #10

# Twitts of 12hs to 13hs of Argentina

schedule.every().day.at("15:00").do(job1) #12
schedule.every().day.at("16:00").do(job1) #13

# Twitts of 15hs to 17hs of Argentina the close of te exchange market it's at 17hs)
schedule.every().day.at("18:00").do(job1) #15
schedule.every().day.at("19:00").do(job1) #16
schedule.every().day.at("20:00").do(job1) #17




#this loop hold the bot alive!

while True:
    schedule.run_pending()
    time.sleep(1)
