from time import sleep
from datetime import datetime
data_hora = datetime.now()
print('vamos iniciar a contagem regressiva:')
for c in range(10,-1,-1):
    print (c) 
    sleep (1) #pausa de 1segundo
print (f'FELIZ {data_hora.year}!!!')
       