import pygame
from pygame.locals import *
import time

import primitive
import components

# Global settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
WHITE = (255,255,255)
TITLEBAR_STRING = "Intelli Sense Dashboard"
COLORS = {
	"WHITE":(255,255,255)
}

# Application related settings
pygame.init()
clock = pygame.time.Clock()
# game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.FULLSCREEN)
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) # For fast development purpose
pygame.display.set_caption(TITLEBAR_STRING)
x = (DISPLAY_WIDTH * 0.5)
y = (DISPLAY_HEIGHT * 0.5)



background = pygame.image.load("./images/background.jpg")



# Time Left Ring
emptyRingTimeComp = primitive.rings.EmptyRing((x+50,y-130))
timeComp = primitive.rings.ActiveRings((x+50,y-130))


# Exit Button
exitButton = primitive.buttons.DecreaseButton((770,20))
exitButton.scale(1)



# This will ke a list of all the sprites present on the screen
all_sprites_list = pygame.sprite.Group()



all_sprites_list.add(exitButton)
all_sprites_list.add(emptyRingTimeComp)
all_sprites_list.add(timeComp)



# For displaying the background
def bg():
	game_display.blit(background, (0,0))


def action():
	primitive.text.message_display(game_display,"Exit",(x,y-25-100),100)
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
			
			# Updating all the components on the screen
			components.speedometer.Speedometer.update()
			components.coolingUnit.CoolingUnit.update()

			# Drawing all the components on the screen
			components.speedometer.Speedometer.draw(game_display)
			components.coolingUnit.CoolingUnit.draw(game_display)

			mouse = pygame.mouse.get_pos()

			# For Speedometer
			all_sprites_list.draw(game_display)

			# Exit Button
			primitive.buttons.GenericButton(exitButton, action)


			pygame.display.update()
			clock.tick(60)
	except KeyboardInterrupt:
		pygame.quit()
		quit()
	pygame.quit()
	quit()



game_loop()
