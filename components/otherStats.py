import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (520,260)

averageSpeed = primitive.text.Text("Average Speed : 13.68 kmph",25, COLORS["WHITE"],(BASE_POSITION[0]+50,BASE_POSITION[1]+10))
temperature = primitive.text.Text("Teperature : 43 degree",25, COLORS["WHITE"],(BASE_POSITION[0]+63, BASE_POSITION[1]+40))

Stats = pygame.sprite.Group()
Stats.add(averageSpeed)
Stats.add(temperature)