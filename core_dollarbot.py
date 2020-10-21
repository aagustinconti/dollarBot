import schedule
from data_check import data_check
from time import sleep



def job1():
    try:
        print(data_check())
    except:
        print("Ocurrió un error, volviendo a intentar en 3 segundos...")
        sleep(3)
        print(data_check())



schedule.every(1).minute.do(job1)


while True:
    schedule.run_pending()
    sleep(1)