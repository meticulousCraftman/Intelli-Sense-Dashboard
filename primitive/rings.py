import pygame
import math


class EmptyRing(pygame.sprite.Sprite):
	
	def __init__(self,position=None):
		super().__init__()

		self.image = pygame.image.load("./images/ring.tif")
		self.rect = self.image.get_rect()
		if position is not None:
			self.rect.center = (position[0], position[1])

	def scale(self,times=1):
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))



class ActiveRings(pygame.sprite.Sprite):
	"""
	This class represents the speedomter present on the screen
	"""

	def __init__(self,minimum=0,maximum=1,position=(0,0)):
		super().__init__()
		self.scale_times = 1
		self.speed = 1
		self.min = minimum
		self.max = maximum
		self.image = pygame.image.load("./images/1.tif")
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.setValue()


	def setValue(self, value=1):
		self.value = value
		ratio = self.value/(self.max - self.min)
		print("The ratio is : "+str(ratio))
		self.active_count = math.floor(36*ratio)


	def update(self):
		if self.active_count!=0:
			image_url = "./images/%s.tif" % str(self.active_count)
			self.image = pygame.image.load(image_url)
			self.scale(self.scale_times)
	

	def scale(self,times=1):
		self.scale_times = times
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))