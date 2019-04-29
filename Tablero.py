import pygame
import random
from Reinas import *


ANCHO = 500
ALTO = 500

n = 4

reinas = Reinas(n)
print('Amigo amigo:',soluciones)

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

pygame.init()
dimensiones = [ANCHO, ALTO]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Tablero")

reina = pygame.image.load('src/reina.png')

juego_terminado = False
reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / n)
alto = int(dimensiones[1] / n)

while juego_terminado is False:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juego_terminado = True
				
	pantalla.fill(BLANCO)
	color = 0
	for i in range(0, dimensiones[0], ancho):
		for j in range(0, dimensiones[1], alto):
			if color % 2  == 0:
				pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
			color += 1
		if n % 2 == 0:
			color += 1
		
	for x, y in soluciones:
		pantalla.blit(reina, (((x * ancho) + ((ancho - 96) / 2)), (y * alto) + ((ancho - 96) / 2)))
		
	pygame.display.flip()
	reloj.tick(2)
	
pygame.quit()
