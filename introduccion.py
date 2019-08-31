uno = 1
usuario = input("Ingresa un valor mayor a uno: ")
usuario = int(usuario)
print("Has ingresado el valor: %d" %(usuario))
print(type(usuario))

if usuario > 1:
	print("Correcto")
elif usuario < 1:
	print("Es menor")
else:
	print("Es un cero")