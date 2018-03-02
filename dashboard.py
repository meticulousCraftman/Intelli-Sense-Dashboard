import pygame
from pygame.locals import *
import time

import components


# Global settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255,255,255)
TITLEBAR_STRING = "Intelli Sense Dashboard"


# Application related settings
pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(TITLEBAR_STRING)
x = (DISPLAY_WIDTH * 0.3)
y = (DISPLAY_HEIGHT * 0.2)



background = pygame.image.load("./images/background.jpg")


speedometerComp = components.speedometer.Speedometer((x,y))
emptyRingComp = components.speedometer.EmptyRing((x,y))
speedometerComp.set_speed(26)


# This will ke a list of all the sprites present on the screen
all_sprites_list = pygame.sprite.Group()


# Adding speedometer to the group of sprites
all_sprites_list.add(emptyRingComp)
all_sprites_list.add(speedometerComp)	


# For displaying the background
def bg():
	game_display.blit(background, (0,0))


# The main game loop
def game_loop():
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
		all_sprites_list.update()
		all_sprites_list.draw(game_display)

		pygame.display.update()
		clock.tick(60)



game_loop()
