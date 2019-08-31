lista = ['Erendira', 'Carlos', 'Rodrigo', 'Liz']
print(lista)
usuario = input('¿En que posición esta Liz?')
usuario = int(usuario)

if lista[usuario] == 'Liz':
	print("Correcto")
else:
	print("Incorrecto")