import random

soluciones = []

class Reinas:
	
	def __init__(self, n = 4, pos = 0):
		self.n = n
		self.ubicarReinas(pos)

	def ubicarReinas(self, i):
		if(i >= self.n):
			print("Termina")
			return 0
		print("Ingresa a nodo:", i)
		f, c = (i, random.randint(0, self.n - 1))
		print("Fila:", f, "Columna:", c)
		if(self.esValido((f, c), 0)):
			soluciones.append((f, c))
			self.ubicarReinas(i + 1)
		else:
			print("Vuelve a nodo anterior:", i - 1)
			soluciones.pop()
			self.ubicarReinas(i - 1)
	
	def esValido(self, posicion, i):
		f, c = posicion
		valido = True
		if(i < len(soluciones)):
			f_r, c_r = soluciones[i]
			print("Entra >","Posicion Reina:", (f_r, c_r), "Posicion nueva:", (f, c))
			if(f_r != f and c_r != c and abs(f_r - f) != abs(c_r - c)):
				print("Cumple >>", "Posicion Reina:", (f_r, c_r), "Posicion Nueva:", (f, c))
				valido = self.esValido(posicion, i + 1)
			else:
				print("NO Cumple >>>", "Posicion Reina:", (f_r, c_r), "Posicion nueva:", (f, c))
				valido = False
		return valido
