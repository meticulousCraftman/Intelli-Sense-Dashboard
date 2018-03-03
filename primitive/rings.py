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

	def __init__(self,position=None):
		super().__init__()
		self.scale_times = 1
		self.speed = 1
		self.image = pygame.image.load("./images/1.tif")
		self.rect = self.image.get_rect()
		if position is not None:
			self.rect.center = (position[0], position[1])


	def set_speed(self, speed):
		self.speed = speed


	def update(self):
		"""
		This reads the value from the sensor and updates
		the board accordingly.
		"""
		self.active_count = self.speed
		image_url = "./images/%s.tif" % str(self.speed)
		self.image = pygame.image.load(image_url)
		self.scale(self.scale_times)
		# self.image = pygame.transform.scale2x(self.image)
	

	def scale(self,times=1):
		self.scale_times = times
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))