import pygame
from pygame.locals import *
import time

import components


# Global settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255,255,255)
TITLEBAR_STRING = "Intelli Sense Dashboard"
COLORS = {
	"WHITE":(255,255,255)
}

# Application related settings
pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(TITLEBAR_STRING)
x = (DISPLAY_WIDTH * 0.5)
y = (DISPLAY_HEIGHT * 0.5)



background = pygame.image.load("./images/background.jpg")


speedometerComp = components.speedometer.Speedometer((x,y-100))
emptyRingComp = components.speedometer.EmptyRing((x,y-100))
exitButton = components.buttons.DecreaseButton((770,20))
exitButton.scale(0.75)
speedometerComp.set_speed(26)


# This will ke a list of all the sprites present on the screen
all_sprites_list = pygame.sprite.Group()


# Adding speedometer to the group of sprites
all_sprites_list.add(emptyRingComp)
all_sprites_list.add(speedometerComp)
all_sprites_list.add(exitButton)


# For displaying the background
def bg():
	game_display.blit(background, (0,0))


def action():
	components.text.message_display(game_display,"Exit",(x,y-25-100),100)
	gameExit = True
	pygame.quit()


# The main game loop
def game_loop():

	try:
		gameExit = False

		while not gameExit:
			for event in pygame.event.get():
				if event.type == QUIT:
					gameExit = True
					break


			# Componenets that needs to present on the screen
			game_display.fill(WHITE)
			bg()
			all_sprites_list.update()

			mouse = pygame.mouse.get_pos()

			# For Speedometer
			all_sprites_list.draw(game_display)
			components.text.message_display(game_display,"22.34",(x,y-25-100),50)
			components.text.message_display(game_display,"KMPH",(x,y+25-100),35)

			# Odometer
			components.text.message_display(game_display,"24 KM",(x,y+60),35)

			# Exit Button
			components.buttons.GenericButton(exitButton, action)


			pygame.display.update()
			clock.tick(60)
	except KeyboardInterrupt:
		pygame.quit()
		quit()
	pygame.quit()
	quit()



game_loop()
