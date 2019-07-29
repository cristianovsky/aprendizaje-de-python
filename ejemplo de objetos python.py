import time as t

#objeto
#Intanciar

class Carro():
	

	#Proiedades
	marca = "Ford"
	color = "Rojo"
	modelo = "2010"
	__clave = ""
	#Metodos

	def arrancar(self):
		
		print("arrancando")
		for i in range(10):
			print(".")
			t.sleep(0.1)

		print("arrancó el carro", self.marca)


	def abrirPuertas(self, llave):
		if llave == self.__clave:
			print("puertas abiertas")
		else:
			print("puertas Ceradas intente nuevamente")


	def __asignarClave(self, llave):
		self.__clave = llave




#Declarar  el Obejo
CarroCristian=Carro()
clave = input("digite su clave : ")
CarroCristian.__asignarClave(clave)


CarroProfesor = Carro()
clave = input("digite su clave : ")
CarroProfesor.asignarClave(clave)

while True:
	clave = input("vamos a abrir las puertas digite su clave : ")
	CarroCristian.abrirPuertas(clave)
	CarroCristian.__clave = "9999"






