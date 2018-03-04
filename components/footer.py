import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (400,460)

footerText = primitive.text.Text("Atharva 2.0 Intelli Sense Dashboard",18, COLORS["WHITE"],BASE_POSITION)

Footer = pygame.sprite.Group()
Footer.add(footerText)