import pygame
from pygame.locals import *
import time

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


# Componenets of speedometer
speedometerComp = components.rings.ActiveRings((x-300,y-100))
speedometerComp.scale(1.75)
speedometerComp.set_speed(12)
emptyRingSpeedometerComp = components.rings.EmptyRing((x-300,y-100))
emptyRingSpeedometerComp.scale(1.75)


# Components of Cooling Unit
emptyRingcoolingComp = components.rings.EmptyRing((x+260,y-160))
coolingUnitComp = components.rings.ActiveRings((x+260,y-160))
rpmIncButton = components.buttons.IncreaseButton((715,160))
rpmDecButton = components.buttons.DecreaseButton((615,160))


# Time Left Ring
emptyRingTimeComp = components.rings.EmptyRing((x+260,y+30))
timeComp = components.rings.ActiveRings((x+260,y+30))


# Exit Button
exitButton = components.buttons.DecreaseButton((770,20))
exitButton.scale(1)



# This will ke a list of all the sprites present on the screen
all_sprites_list = pygame.sprite.Group()


# Adding speedometer to the group of sprites
all_sprites_list.add(emptyRingSpeedometerComp)
all_sprites_list.add(speedometerComp)
all_sprites_list.add(emptyRingcoolingComp)
all_sprites_list.add(coolingUnitComp)
all_sprites_list.add(exitButton)
all_sprites_list.add(rpmIncButton)
all_sprites_list.add(rpmDecButton)
all_sprites_list.add(emptyRingTimeComp)
all_sprites_list.add(timeComp)


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
			components.text.message_display(game_display,"22.34",(x-250,y-70),50)
			components.text.message_display(game_display,"kmph",(x-250,y-30),35)

			# Odometer
			components.text.message_display(game_display,"3.68 km",(x-250,y+90),30)

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
