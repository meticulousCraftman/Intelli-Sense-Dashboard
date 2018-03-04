import pygame
import math

class IncreaseButton(pygame.sprite.Sprite):
	
	def __init__(self,position=None):
		super().__init__()
		self.position = position
		self.image = pygame.image.load("./images/increase.png")
		self.rect = self.image.get_rect()
		if position is not None:
			self.rect.center = (position[0], position[1])

	def scale(self,times=1):
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))

	def clicked(self,mouse,click,action=None):
		self.image = pygame.image.load("./images/increase.png")
		self.action = action
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		w,h = self.image.get_size()
		if self.rect.x + w > mouse[0] > self.rect.x and self.rect.y + h > mouse[1] > self.rect.y:
			if click[0] == 1 and action != None:
				self.image = pygame.image.load("./images/increase-tap.png")
				self.action()


class DecreaseButton(pygame.sprite.Sprite):
	
	def __init__(self,position=None):
		super().__init__()
		self.position = position
		self.image = pygame.image.load("./images/decrease.png")
		self.rect = self.image.get_rect()
		if position is not None:
			self.rect.center = (position[0], position[1])

	def scale(self,times=1):
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))

	def clicked(self,mouse,click,action=None):
		self.image = pygame.image.load("./images/decrease.png")
		self.action = action
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		w,h = self.image.get_size()
		if self.rect.x + w > mouse[0] > self.rect.x and self.rect.y + h > mouse[1] > self.rect.y:
			if click[0] == 1 and action != None:
				self.image = pygame.image.load("./images/decrease-tap.png")
				self.action()


def GenericButton(buttonSurface, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	w,h = buttonSurface.image.get_size()
	if buttonSurface.rect.x + w > mouse[0] > buttonSurface.rect.x and buttonSurface.rect.y + h > mouse[1] > buttonSurface.rect.y:
		if click[0] == 1 and action != None:
			action()
