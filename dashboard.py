import pygame
from pygame.locals import *
import time

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
TITLEBAR_STRING = "Intelli Sense Dashboard"

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(TITLEBAR_STRING)
white = (255,255,255)
black = (0,0,0)
car_width = 73

# Loading images
carImg = pygame.image.load("racecar.png")

def car(x,y):
	game_display.blit(carImg, (x,y))


def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font("freesansbold.ttf", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
	game_display.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display("You Crashed")

# The main game loop
def game_loop():
	x = (DISPLAY_WIDTH * 0.45)
	y = (DISPLAY_HEIGHT * 0.8)

	x_change = 0

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			print(event)
			if event.type == QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		x += x_change

		game_display.fill(white)
		car(x,y)

		if x > (DISPLAY_WIDTH - car_width) or x < 0:
			crash()

		pygame.display.update()
		clock.tick(60)



game_loop()
