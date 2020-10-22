
import csv

import time
from datetime import datetime
import pytz



def dollar_value(up_or_down, oficial_or_blue, peso_vs_dolar, new_values):
    
    new_compra_oficial, new_venta_oficial, new_compra_blue, new_venta_blue = new_values

    #time zone    
    tz = tz = pytz.timezone('America/Argentina/Cordoba')

    #actual time 
    now= datetime.now(tz)
    horas = now.hour
    minutos = now.minute
    dia = now.day
    mes = now.month
    anio = now.year

    #the final message

    if oficial_or_blue:

        out_text = str(up_or_down) + " a $ " + str(new_compra_blue) + " | $ " + str(new_venta_blue) + " y UN (1) Peso Argentino equivale a "+str(peso_vs_dolar)+"U$D. A las " + str(horas) + " horas y " + str(minutos) + " minutos del " + str(dia) + "/" + str(mes) + "/" + str(anio) +". " +  "#Dolar #DolarLibre #DolarBlue"
    
    else:

        out_text = str(up_or_down) + " a $ " + str(new_compra_oficial) + " | $ " + str(new_venta_oficial) + ". A las " + str(horas) + " horas y " + str(minutos) + " minutos del " + str(dia) + "/" + str(mes) + "/" + str(anio) +". " +  "#Dolar #DolarOficial #DolarBN"

    
    return out_text



def convert_data(list_to_convert):

    tuple_of_numbers=[]    
    for string in list_to_convert:
        tuple_of_numbers.append(float(string.strip('$').replace(',','.').replace(' ','')))

    tuple_of_numbers = tuple(tuple_of_numbers)

    return tuple_of_numbers


def save_data(file_name, values):
    with open(str(file_name)+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(values)
    csvfile.close()
    
    return "Data saved."


def recover_data(file_name):
    values = []
    with open(str(file_name)+'.csv') as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            values.append(row)
    csvfile.close()
    
    
    values = values[0]

    return values


