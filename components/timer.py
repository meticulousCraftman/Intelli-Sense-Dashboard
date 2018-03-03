import pygame
import primitive

pygame.init()

x = (800 * 0.5)
y = (480 * 0.5)

COLORS = {
	"WHITE":(255,255,255)
}

emptyRingTimeComp = primitive.rings.EmptyRing((x+50,y-130))
timeComp = primitive.rings.ActiveRings((x+50,y-130))

Timer = pygame.sprite.Group()
Timer.add(emptyRingTimeComp)
Timer.add(timeComp)