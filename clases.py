class Humano:
	nombre = 'Luis'
	edad = 26
	altura = 1.75
	aux_edad = None

	def __init__(self, nombre='Luis'):
		print('Acabo de nacer')
		self.nombre = nombre
		self.aux_edad = self.edad

	def hablar(self):
		print('Hola, me llamo {}'.format(self.nombre))

	def cumpleanos(self):
		self.edad += 1

	def preguntar_edad(self):
		return self.edad

	def rejuvenecer(self):
		self.edad = self.aux_edad


humano = Humano()
humano.hablar()
aux = humano.edad
print(humano.preguntar_edad())
for _ in range(30):
	humano.cumpleanos()
print(humano.preguntar_edad())
humano.rejuvenecer()
print(humano.preguntar_edad())
print('==================')
humano2 = Humano(nombre='Pepito')
humano2.hablar()

class Araña:
	def trepar_paredes(self):
		print('Estoy trepando paredes!')

class HombreAraña(Humano, Araña):
	edad = 16
	enemigos = ['King Ping', 'Venom', 'Duende Verde']

	def preguntar_enemigos(self):
		return self.enemigos

	@classmethod
	def get_copyright(cls):
		print('Sony')

	@staticmethod
	def get_copyright2():
		print('Sony')

print('==================')
hombre_araña = HombreAraña(nombre='Peter Parker')
hombre_araña.hablar()
print(hombre_araña.preguntar_edad())
hombre_araña.cumpleanos()
print(hombre_araña.preguntar_edad())
hombre_araña.trepar_paredes()
print(hombre_araña.preguntar_enemigos())

hombre_araña.get_copyright()
HombreAraña.get_copyright2()