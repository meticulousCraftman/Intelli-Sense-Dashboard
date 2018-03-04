import pygame
import primitive
import time

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (700,110)

emptyRingcoolingComp = primitive.rings.EmptyRing(BASE_POSITION)

coolingUnitComp = primitive.rings.ActiveRings(0,100,BASE_POSITION)
coolingUnitComp.desc = "Active Rings"

rpmIncButton = primitive.buttons.IncreaseButton((BASE_POSITION[0]+65, BASE_POSITION[1]+80))
rpmIncButton.desc = "Increase"

rpmDecButton = primitive.buttons.DecreaseButton((BASE_POSITION[0]-65,BASE_POSITION[1]+80))
rpmDecButton.desc = "Decrease"

componentName = primitive.text.Text("Cooling Unit",25, COLORS["WHITE"],(BASE_POSITION[0],BASE_POSITION[1]-90))

coolingPercentage = primitive.text.Text("0 %",30, COLORS["WHITE"],BASE_POSITION)
coolingPercentage.desc = "Magnitude"



class CoolingUnitClass(pygame.sprite.Group):

	def __init__(self):
		self.value = 0
		super().__init__()

	def update(self):
		listOfSprites = self.sprites()
		for x in listOfSprites:
			if hasattr(x, "desc"):
				if x.desc=="Magnitude":
					x.changeText(str(self.value)+" %")
				elif x.desc=="Active Rings":
					x.setValue(self.value)
				elif x.desc=="Increase":
					x.clicked(self.rpmInc)
				elif x.desc=="Decrease":
					x.clicked(self.rpmDec)
		super().update()

	def rpmInc(self):
		if self.value < 100:
			self.value += 10

	def rpmDec(self):
		if self.value > 0:
			self.value -= 10



CoolingUnit = CoolingUnitClass()
CoolingUnit.add(emptyRingcoolingComp)
CoolingUnit.add(coolingUnitComp)
CoolingUnit.add(rpmDecButton)
CoolingUnit.add(rpmIncButton)
CoolingUnit.add(componentName)
CoolingUnit.add(coolingPercentage)