import pygame
import primitive

pygame.init()

x = (800 * 0.5)
y = (480 * 0.5)

COLORS = {
	"WHITE":(255,255,255)
}

speedometerComp = primitive.rings.ActiveRings(0, 48, (x-300,y-100))
speedometerComp.scale(1.75)
speedometerComp.desc = "Active Rings"

emptyRingSpeedometerComp = primitive.rings.EmptyRing((x-300,y-100))
emptyRingSpeedometerComp.scale(1.75)

speedText = primitive.text.Text("22.34",50, COLORS["WHITE"],(x-250,y-70))
speedText.desc = "Magnitude"

speedUnitText = primitive.text.Text("kmph",40, COLORS["WHITE"],(x-250,y-30))

class SpeedometerClass(pygame.sprite.Group):

	def __init__(self):
		super().__init__()

	def update(self, value=0):
		self.value = value
		listOfSprites = self.sprites()
		for x in listOfSprites:
			if hasattr(x, "desc"):
				if x.desc=="Magnitude":
					x.changeText(str(self.value))
				elif x.desc=="Active Rings":
					x.setValue(self.value)

		super().update()

Speedometer = SpeedometerClass()
Speedometer.add(emptyRingSpeedometerComp)
Speedometer.add(speedometerComp)
Speedometer.add(speedText)
Speedometer.add(speedUnitText)
