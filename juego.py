import random
import os
aleatorio = random.randint(1,100)
usuario = 0
while usuario != aleatorio:
 	usuario = input('Adivina el numero del 1 al 100: ')
 	try:
 		usuario = int(usuario)
 	except ValueError:
 		print('Eso no es un numero')
 		usuario = 0
 		continue
 	if usuario < 1 or usuario > 100:
 		print('numero entre uno y cien')
 		usuario = 0
 		continue
 	if usuario < aleatorio:
 		print('El numero es mayor')
 	elif usuario > aleatorio: 
 		print('El numero es menor')
 	else
 		print('Numero correcto')
os.system("PAUSE")