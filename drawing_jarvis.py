
import Jarvis as jar
import pygame
from pygame.color import *
from pygame.locals import *




pygame.init()

caption = 'Convex Hull by Grahams Scan'
resolution = (500,500)
text = ['Klikkaa hiirella ruutua piirtaaksesi pisteita',
			'Valilyonti puhdistaa nayton',
			'Paina <esc> sulkeaksesi ikkunan']

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption(caption)
font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()

coords = []
segs = []	
run = True

while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			run = False
		elif event.type == MOUSEBUTTONDOWN:
			coords.append(event.pos)
			if len(coords) >= 3:
				segs = jar.jarvis_march(coords)
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				segs = []
				coords = []
			elif event.key == K_ESCAPE:
				pygame.quit()
	try:
		screen.fill(Color('white'))
	except:
		pygame.error
		print('Quit')

	#piirretaan teksti
	y = 10
	for line in text:
		img = font.render(line, 1, Color('black'))
		screen.blit(img, (5, y))
		y += 15
	

	#pisteiden piirtaminen
	for coord in coords:
		pygame.draw.circle(screen, Color('black'), coord, 2, 0)

	#convexin piirto
	if len(coords) >= 3:
		pygame.draw.lines(screen, Color('black'), True, segs, 2)

		
	pygame.display.update()
	clock.tick(50)
