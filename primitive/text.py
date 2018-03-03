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

        OpenSans = pygame.font.Font("./fonts/OpenSans-Light.ttf", size)
        self.textSurf = OpenSans.render(text, True, color)
        self.image = self.textSurf
        self.rect = self.image.get_rect()

        self.rect.center = (position[0], position[1])