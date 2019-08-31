#Cliclos en python
numero = 1
while numero < 10:
	print(numero)
	if numero == 5:
		break
	numero += 1
print('fin')

for i in ['a','b','c','z','d']:
	if i == 'z':
		continue
	print(i)
	if i == 'b':
		break
else:
	print('Nadie me rompio')
print('fin')