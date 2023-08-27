import pygame
import random
pygame.init()

screenSize = 600
snakeColor = (0, 0, 0)
bgColor = (200, 200, 200)
foodColor = (200, 0, 0)
win = pygame.display.set_mode((screenSize, screenSize))
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30, True)
speed = 10
score = 0

pygame.display.set_caption("Snake Game")

class Snake(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.size = 10
		self.direction = '_'

	def draw(self, win):
		pygame.draw.rect(win, snakeColor, (self.x, self.y, self.size, self.size))

class Background(object):

	def draw(self, win):
		pygame.draw.rect(win, bgColor, (0, 0, screenSize, screenSize))
		pygame.draw.rect(win, snakeColor, (0, 0, screenSize, 80))
		pygame.draw.rect(win, bgColor, (10, 10, screenSize - 20, 60))

class Food(object):

	def __init__(self):
		self.x = round(random.randrange(130, screenSize - 50) / 10) * 10
		self.y = round(random.randrange(130, screenSize - 50) / 10) * 10
		self.size = 8

	def draw(self, win):
		pygame.draw.rect(win, foodColor, (self.x + 1, self.y +1, self.size, self.size))

def redraw():
	bg.draw(win)
	for snake in body:
		snake.draw(win)
	food.draw(win)
	textScore = font.render('Score: ' + str(score), 1, snakeColor)
	textSpeed = font.render('Speed: ' + str(speed), 1, snakeColor)
	win.blit(textScore, (20, 20))
	win.blit(textSpeed, (320, 20))
	pygame.display.update()

head = Snake(200, 200)
body = [head]
bg = Background()
food = Food()
run = True
while run:
	clock.tick(speed)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for i in range(1, len(body), 1):
		if body[i].x == head.x and body[i].y == head.y and i > 1:
			run = False

	if head.x < 0 or head.x >= screenSize or head.y < 80 or head.y >= screenSize:
		run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and not head.direction == 'r':
		head.direction = 'l'
	if keys[pygame.K_RIGHT] and not head.direction == 'l':
		head.direction = 'r'
	if keys[pygame.K_UP] and not head.direction == 'd':
		head.direction = 'u'
	if keys[pygame.K_DOWN] and not head.direction == 'u':
		head.direction = 'd'

	for i in range(len(body)-1, 0, -1):
		body[i].x = body[i-1].x
		body[i].y = body[i-1].y

	if head.direction == 'l':
		head.x -= body[len(body)-1].size
	elif head.direction == 'r':
		head.x += body[len(body)-1].size
	elif head.direction == 'u':
		head.y -= body[len(body)-1].size
	elif head.direction == 'd':
		head.y += body[len(body)-1].size

	if head.x == food.x and head.y == food.y:
		food = Food()
		score += 1
		if score % 3 == 0:
			speed += 1
		body.append(Snake(body[len(body)-1].x, body[len(body)-1].y))

	redraw()

pygame.quit
