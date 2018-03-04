import pygame
import primitive

pygame.init()

COLORS = {
	"WHITE":(255,255,255)
}

BASE_POSITION = (400,400)

sliderBar = primitive.slider.SliderBar((BASE_POSITION[0], BASE_POSITION[1]))
sliderDot = primitive.slider.SliderDot((BASE_POSITION[0]-200, BASE_POSITION[1]-3))

LapTracker = pygame.sprite.Group()
LapTracker.add(sliderBar)
LapTracker.add(sliderDot)