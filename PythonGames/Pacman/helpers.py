#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('images')
    fullname = os.path.join(fullname, name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (16, 16))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_pics(name):
    fullname = os.path.join('images')
    fullname = os.path.join(fullname, name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (24, 24))
    return image