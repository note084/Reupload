import pygame
import random
import centerSprite
from imagerect import ImageRect

class Monster(centerSprite.Sprite):

    def __init__(self, centerPoint, image, scared_image=None):
        centerSprite.Sprite.__init__(self, centerPoint, image)
        self.original_rect = pygame.Rect(self.rect)
        self.normal_image = image
        if scared_image != None:
            self.scared_image = scared_image
        else:
            self.scared_image = image
        self.screen = (900, 1200)
        self.scared = False
        self.direction = random.randint(1, 4)
        self.dist = 3
        self.moves = random.randint(100, 200)
        self.moveCount = 0;

        self.blinkyup = [ImageRect(self.screen, 'up1_1', 32, 32),
                         ImageRect(self.screen, 'up1_2', 32, 32)]
        self.blinkyleft = [ImageRect(self.screen, 'left1_1', 32, 32),
                           ImageRect(self.screen, 'left1_2', 32, 32)]
        self.blinkyright = [ImageRect(self.screen, 'right1_1', 32, 32),
                            ImageRect(self.screen, 'right1_2', 32, 32)]
        self.blinkydown = [ImageRect(self.screen, 'down1_1', 32, 32),
                           ImageRect(self.screen, 'down1_2', 32, 32)]
        self.blinkyup_frames = None
        self.blinkyleft_frames = None
        self.blinkyright_frames = None
        self.blinkydown_frames = None


    def blinkyup(self):
        self.up = True
        self.blinkyup_frames = 0
        self.image = self.blinkyup[self.blinkyup_frames]
        self.last_frame = pygame.time.get_ticks()



    def SetScared(self, scared):
        if self.scared != scared:
            self.scared = scared
            if scared:
                self.image = self.scared_image
            else:
                self.image = self.normal_image

    def Eaten(self):
        self.rect = self.original_rect
        self.scared = False
        self.image = self.normal_image

    def update(self, block_group):
        xMove, yMove = 0, 0
        if self.direction == 1:
            xMove = -self.dist
        elif self.direction == 2:
            yMove = -self.dist
        elif self.direction == 3:
            xMove = self.dist
        elif self.direction == 4:
            yMove = self.dist
        self.rect.move_ip(xMove, yMove)
        self.moveCount += 1

        if pygame.sprite.spritecollideany(self, block_group):
            self.rect.move_ip(-xMove, -yMove)
            self.direction = random.randint(1, 4)
        elif self.moves == self.moveCount:
            self.direction = random.randint(1,4)
            self.moves = random.randint(100, 200)
            self.moveCount = 0