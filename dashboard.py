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
			
			# Updating all the components on the screen
			components.speedometer.Speedometer.update()
			components.coolingUnit.CoolingUnit.update()
			components.timer.Timer.update()
			components.exitButton.ExitButton.update()
			components.otherStats.Stats.update()
			components.lapsTracker.LapTracker.update()
			components.footer.Footer.update()

			# Drawing all the components on the screena
			components.speedometer.Speedometer.draw(game_display)
			components.coolingUnit.CoolingUnit.draw(game_display)
			components.timer.Timer.draw(game_display)
			components.exitButton.ExitButton.draw(game_display)
			components.otherStats.Stats.draw(game_display)
			components.lapsTracker.LapTracker.draw(game_display)
			components.footer.Footer.draw(game_display)

			mouse = pygame.mouse.get_pos()
			

			# Exit Button
			# primitive.buttons.GenericButton(exitButton, action)


			pygame.display.update()
			clock.tick(60)
	except KeyboardInterrupt:
		pygame.quit()
		quit()
	pygame.quit()
	quit()



game_loop()
