import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (360,110)


emptyRingDistComp = primitive.rings.EmptyRing(BASE_POSITION)
distComp = primitive.rings.ActiveRings(0,1500,BASE_POSITION)
componentName = primitive.text.Text("Distance",25, COLORS["WHITE"],(BASE_POSITION[0],BASE_POSITION[1]-90))
distMag = primitive.text.Text("10.6 km",25, COLORS["WHITE"],BASE_POSITION)

Odometer = pygame.sprite.Group()
Odometer.add(emptyRingDistComp)
Odometer.add(distComp)
Odometer.add(componentName)
Odometer.add(distMag)