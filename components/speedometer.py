import pygame


class Speedometer(pygame.sprite.Sprite):
	"""
	This class represents the speedomter present on the screen
	"""

	def __init__(self,position=None):
		super().__init__()

		self.image = pygame.image.load("./images/1.tif")
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect()
		if position is not None:
			self.rect.x = position[0]
			self.rect.y = position[1]



	def update(self, speed):
		"""
		This reads the value from the sensor and updates
		the board accordingly.
		"""
		self.active_count = speed
		image_url = "./images/%s.tif" % str(speed)
		self.image = pygame.image.load(image_url)
		self.image = pygame.transform.scale2x(self.image)
