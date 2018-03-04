import pygame

class SliderBar(pygame.sprite.Sprite):

	def __init__(self, position=(0,0)):
		
		super().__init__()

		self.image = pygame.image.load("./images/sliderBar.png")
		self.rect = self.image.get_rect()
		self.rect.center = position

	def scale(self,times=1):
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))


class SliderDot(pygame.sprite.Sprite):
	
	def __init__(self, position=(0,0)):
		
		super().__init__()

		self.image = pygame.image.load("./images/sliderDot.png")
		self.rect = self.image.get_rect()
		self.rect.center = position


	def scale(self,times=1):
		w,h = self.image.get_size()
		neww = math.floor(w*times)
		newh = math.floor(h*times)
		self.image = pygame.transform.scale(self.image, (neww, newh))
