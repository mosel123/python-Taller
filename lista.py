import os
import random
lista = ['Erendira', 'Carlos', 'Rodrigo', 'Liz', 'Mosel', 'Tony']
print(lista)
nombre_index = random.randint(0, len(lista) - 1)
nombre = lista[nombre_index]
usuario = input('En que posicion esta %s' % (nombre))
usuario = int(usuario)
if usuario < len(lista) or usuario >= 0
	if lista[usuario] == nombre:
		print("Correcto")
	else:
		print("Incorrecto")
else:
	print("Vuelve a intentar")
os.system("PAUSE")