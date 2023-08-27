import pygame
from subprocess import Popen
pygame.init()

screenSize = 600

win = pygame.display.set_mode((screenSize, screenSize))

pygame.display.set_caption("Snake Game Title Screen")

bg = pygame.image.load('images/title.png')
start = pygame.image.load('images/titleStart.png')

run = True
inRange = False
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN and inRange:
			Popen('python3 Snake.py', shell = True)

	mx, my = pygame.mouse.get_pos()
	if mx > 170 and mx < 407 and my > 361 and my < 419:
		win.blit(start, (0,0))
		inRange = True
	else:
		win.blit(bg, (0,0))
		inRange = False
	pygame.display.update()

pygame.quit