import pygame
import primitive

pygame.init()

x = (800 * 0.5)
y = (480 * 0.5)

COLORS = {
	"WHITE":(255,255,255)
}

emptyRingcoolingComp = primitive.rings.EmptyRing((x+260,y-130))
coolingUnitComp = primitive.rings.ActiveRings((x+260,y-130))
rpmIncButton = primitive.buttons.IncreaseButton((715,190))
rpmDecButton = primitive.buttons.DecreaseButton((615,190))

CoolingUnit = pygame.sprite.Group()
CoolingUnit.add(emptyRingcoolingComp)
CoolingUnit.add(coolingUnitComp)
CoolingUnit.add(rpmDecButton)
CoolingUnit.add(rpmIncButton)
