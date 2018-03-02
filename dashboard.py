import pygame
from pygame.locals import *
import time

import components

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255,255,255)
TITLEBAR_STRING = "Intelli Sense Dashboard"

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(TITLEBAR_STRING)


x = (DISPLAY_WIDTH * 0.3)
y = (DISPLAY_HEIGHT * 0.2)


# Loading images
ringImg = pygame.image.load("./images/ring.tif")
a1 = pygame.image.load("./images/1.tif")
ringImg = pygame.transform.scale2x(ringImg)
a1 = pygame.transform.scale2x(a1)


background = pygame.image.load("./images/background.jpg")

speedometer = components.speedometer.Speedometer((x,y))

def bg():
	game_display.blit(background, (0,0))

def ring(x,y):
	game_display.blit(ringImg, (x,y))


all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(speedometer)



def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font("./fonts/OpenSans-Light.ttf", 115)
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
	

	x_change = 0

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			# print(event)
			if event.type == QUIT:
				pygame.quit()
				quit()


		# Componenets that needs to present on the screen
		game_display.fill(WHITE)
		bg()
		ring(x,y)
		all_sprites_list.update()
		
		game_display.blit(speedometer.image, (x,y))
		
		for u in range(1,36):
			speedometer.update(u)
			game_display.blit(speedometer.image, (x,y))
			pygame.display.update()
			time.sleep(0.5)

		pygame.display.update()
		clock.tick(60)



game_loop()
