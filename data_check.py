
from data_extraction import data_scraping
from data_management import convert_data, save_data,recover_data, dollar_value
from twitt_data import twitt

from time import perf_counter, sleep
import os
import numpy as np



file_name='temporal_store'


def data_check():

    init_time_function = perf_counter()

    new_values= convert_data(data_scraping())
    old_values= convert_data(recover_data(file_name))

    new_venta_oficial = new_values[1]
    old_venta_oficial = old_values[1]

    new_venta_blue = new_values[3]
    old_venta_blue= old_values[3]
    peso_vs_dolar= np.round(1/new_venta_blue,5)

    #Old values vs new values
    if old_values != new_values:
        
        #Remove file because Heroku crash modified files
        os.system('rm '+str(file_name)+'.csv')


        #Dolar oficial check
        init_time_oficial = perf_counter()

        if old_venta_oficial != new_venta_oficial:

            if old_venta_oficial > new_venta_oficial:

                out_text = dollar_value("BAJÓ el Dólar Oficial",False,0,new_values)

            elif old_venta_oficial < new_venta_oficial:

                out_text= dollar_value("SUBIÓ el Dólar Oficial",False,0,new_values)
        
            
            twitt(out_text)
            
            print("Valor viejo Oficial ", old_venta_oficial)
            print("Valor nuevo Oficial ", new_venta_oficial)
            
            final_time_oficial = perf_counter()
            execution_time = final_time_oficial - init_time_oficial
            
            print('Se twitteo el precio del dolar OFICIAL con exito. En ' + str(execution_time) + '[s].')

        
        
            
        sleep(3)



        #Dolar Blue check
        init_time_blue = perf_counter()

        if old_venta_blue != new_venta_blue:

            if old_venta_blue > new_venta_blue:

                out_text = dollar_value("BAJÓ el Dólar Libre",True, peso_vs_dolar,new_values)

            elif old_venta_blue < new_venta_blue:

                out_text = dollar_value("SUBIÓ el Dólar Libre",True, peso_vs_dolar,new_values)
    
        
            twitt(out_text)
            
            print("Valor viejo Libre", old_venta_blue)
            print("Valor nuevo Libre", new_venta_blue)
            
            final_time_blue = perf_counter()
            execution_time = final_time_blue - init_time_blue

            print('Se twitteo el precio del dolar LIBRE con exito. En ' + str(execution_time) + '[s].')

    
        save_data(file_name,[new_values])    
    
    final_time_function = perf_counter() 
    execution_time = final_time_function - init_time_function

    return 'Checkeo realizado en ' + str(execution_time) + '[s].'