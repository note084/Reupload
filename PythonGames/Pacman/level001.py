import pygame
import levelbase
from imagerect import ImageRect
from helpers import load_image
from helpers import load_pics


class level(levelbase.Level):
    
    def __init__(self):
        self.BLOCK = 1
        self.PLAYER = 2
        self.PELLET = 0
        self.BLINKY = 3
        self.SCARED_MONSTER = 4
        self.SUPER_PELLET = 5
        self.SHIELD = 6


    
    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 2, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9],\
                [9, 1, 9, 5, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 5, 9, 1, 9],\
                [9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 9],\
                [9, 1, 9, 0, 9, 9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 9, 0, 9, 0, 9, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 9],\
                [9, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 9, 1, 1, 9, 0, 9, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 0, 9, 9, 0, 9, 1, 1, 9, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 0, 9, 0, 9, 9, 0, 9, 3, 9, 9, 0, 9, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 0, 9, 0, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 0, 9, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 9, 0, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 5, 9, 9, 0, 9, 1, 1, 9, 9, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 9, 1, 1, 9, 0, 9, 9, 5, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 1, 1, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 1, 1, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 9, 0, 9, 0, 9, 1, 1, 9, 0, 9, 0, 9, 9, 0, 9, 1, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 1, 9, 0, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 9],\
                [9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]
                
        
    def getSprites(self):
        block, rect = load_image('block.png')
        pellet, rect = load_image('pellet.png',-1)
        pellet = pygame.transform.scale(pellet, (4, 4))
        pellet.get_rect()
        blinky, rect = load_image('up1_1.png', -1)
        player, rect = load_image('p0.png')
        player = pygame.transform.scale(player, (34, 34))
        monster_scared_01, rect = load_image('ghost1_1.png', -1)
        super_pellet, rect = load_image('super_pellet.png', -1)
        return [pellet, block, player, blinky, monster_scared_01, super_pellet]

    def blinkyup(self):
        self.up = True
        self.blinkyup_frames = 0
        self.image = self.blinkyup[self.blinkyup_frames]
        self.last_frame = pygame.time.get_ticks()
