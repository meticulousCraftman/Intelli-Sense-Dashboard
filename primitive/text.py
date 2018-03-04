import pygame

COLORS = {
    "WHITE":(255,255,255)
}



def text_objects(text, font):
    textSurface = font.render(text, True, COLORS["WHITE"])
    return textSurface, textSurface.get_rect()

def message_display(display,text,position,size=40):
    largeText = pygame.font.Font('./fonts/OpenSans-Light.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (position[0], position[1])
    display.blit(TextSurf, TextRect)


class Text(pygame.sprite.Sprite):

    def __init__(self, text, size, color, position=(0, 0)):

        super().__init__()

        self.text = text
        self.size = size
        self.color = color
        self.position = position

        self.OpenSans = pygame.font.Font("./fonts/OpenSans-Light.ttf", size)
        self.textSurf = self.OpenSans.render(text, True, color)
        self.image = self.textSurf
        self.rect = self.image.get_rect()

        self.rect.center = self.position


    def changeText(self,text=""):
        self.text = text
        self.textSurf = self.OpenSans.render(self.text, True, self.color)
        self.image = self.textSurf
        self.rect = self.image.get_rect()

        self.rect.center = self.position