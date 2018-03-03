import pygame
import primitive

pygame.init()

x = (800 * 0.5)
y = (480 * 0.5)

COLORS = {
	"WHITE":(255,255,255)
}

exitButton = primitive.buttons.DecreaseButton((770,20))
exitButton.scale(1)

ExitButton = pygame.sprite.Group()
ExitButton.add(exitButton)