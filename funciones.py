def hola_mundo(nombre, saludos='Hola', punto='.'):
	return "%s, %s%s" % (saludo, nombre, punto)
hola = hola_mundo('Mundo',saludo='Hello',punto='!')
print(hola)

def hola_nombres(*nombres):
	for nombre in nombres:		
		print('Hola %s' % nombre)
hola_nombres('Pedro', 'Maria', 'Juan')

class animal():
	patas = 0
	pelo = True
	def __init__(self,pelo,patas):
		self.pelo = pelo
		self.patas = patas
	def numero_patas(self):
		print("este animal tiene %d patas" % (patas))
		print("mmm... patas")
	def tiene_pelo(sefl):
		if self.pelo:
			print("Tiene pelo")
		else
			print("Tiene alopecia")
class Perro(animal):
	def __init__(self,pelo=True,patas=4):
		super().__init__(self,pelo,patas)

perro.numero_patas()
perro.tiene_pelo()
