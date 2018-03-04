import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (450,110)


emptyRingTimeComp = primitive.rings.EmptyRing(BASE_POSITION)
timeComp = primitive.rings.ActiveRings(BASE_POSITION)
componentName = primitive.text.Text("Timer",25, COLORS["WHITE"],(BASE_POSITION[0],BASE_POSITION[1]-90))
time = primitive.text.Text("12:54",25, COLORS["WHITE"],BASE_POSITION)

Timer = pygame.sprite.Group()
Timer.add(emptyRingTimeComp)
Timer.add(timeComp)
Timer.add(componentName)
Timer.add(time)