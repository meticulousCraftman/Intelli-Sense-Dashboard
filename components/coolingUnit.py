import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (660,110)

emptyRingcoolingComp = primitive.rings.EmptyRing(BASE_POSITION)
coolingUnitComp = primitive.rings.ActiveRings(BASE_POSITION)
rpmIncButton = primitive.buttons.IncreaseButton((BASE_POSITION[0]+65, BASE_POSITION[1]+80))
rpmDecButton = primitive.buttons.DecreaseButton((BASE_POSITION[0]-65,BASE_POSITION[1]+80))
componentName = primitive.text.Text("Cooling Unit",25, COLORS["WHITE"],(BASE_POSITION[0],BASE_POSITION[1]-90))
coolingPercentage = primitive.text.Text("10 %",30, COLORS["WHITE"],(BASE_POSITION[0],BASE_POSITION[1]))

CoolingUnit = pygame.sprite.Group()
CoolingUnit.add(emptyRingcoolingComp)
CoolingUnit.add(coolingUnitComp)
CoolingUnit.add(rpmDecButton)
CoolingUnit.add(rpmIncButton)
CoolingUnit.add(componentName)
CoolingUnit.add(coolingPercentage)