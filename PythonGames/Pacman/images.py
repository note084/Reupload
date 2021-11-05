import pygame
import sys, os


def load_image(name):
    fullname = os.path.join('images')
    fullname = os.path.join(fullname, name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (24, 24))
    return image

class TestSprite(pygame.sprite.Sprite):

    def __init__(self):
        super(TestSprite, self).__init__()
        self.blinky = []
        self.blinky.append(load_image('up1_1.png'))
        self.blinky.append(load_image('up1_2.png'))

        self.index = 0
        self.blink = self.blinky[self.index]
        self.rect = pygame.Rect(5, 5, 24, 24)

    def update(self):
        self.index += 1
        if self.index >= len(self.blinky):
            self.index = 0
        self.blink = self.blinky[self.index]

