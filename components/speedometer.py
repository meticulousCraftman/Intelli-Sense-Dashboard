import pygame
import primitive

pygame.init()

x = (800 * 0.5)
y = (480 * 0.5)

COLORS = {
	"WHITE":(255,255,255)
}

speedometerComp = primitive.rings.ActiveRings((x-300,y-100))
speedometerComp.scale(1.75)
speedometerComp.set_speed(12)
emptyRingSpeedometerComp = primitive.rings.EmptyRing((x-300,y-100))
emptyRingSpeedometerComp.scale(1.75)
speedText = primitive.text.Text("22.34",50, COLORS["WHITE"],(x-250,y-70))
speedUnitText = primitive.text.Text("kmph",40, COLORS["WHITE"],(x-250,y-30))

Speedometer = pygame.sprite.Group()
Speedometer.add(emptyRingSpeedometerComp)
Speedometer.add(speedometerComp)
Speedometer.add(speedText)
Speedometer.add(speedUnitText)