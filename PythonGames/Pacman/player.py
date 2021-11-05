import pygame
import centerSprite
from helpers import *

SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START + 1
PLAYER_EATEN = SUPER_STATE_OVER + 1

class Player(centerSprite.Sprite):
    def __init__(self, centerPoint, image):

        centerSprite.Sprite.__init__(self, centerPoint, image)

        self.pellets = 0
        self.speed = 4
        self.y_dist = self.speed
        self.x_dist = self.speed

        self.yMove = 0
        self.xMove = 0
        self.superState = False

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.dead = False

    def init_player(self):
        self.images = [pygame.image.load('images/p0.png'),
                       pygame.image.load('images/p1.png'),
                       pygame.image.load('images/p2.png'),
                       pygame.image.load('images/p3.png'),
                       pygame.image.load('images/p4.png'),
                       pygame.image.load('images/p5.png'),
                       pygame.image.load('images/p6.png'),
                       pygame.image.load('images/p7.png'),
                       pygame.image.load('images/p8.png'),
                       pygame.image.load('images/p9.png'),
                       pygame.image.load('images/p10.png'),
                       pygame.image.load('images/p11.png'),
                       pygame.image.load('images/p12.png'),
                       pygame.image.load('images/p13.png')]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rcenter = self.rect.center
        self.last_frame = pygame.time.get_ticks()
        return self.images

    def KeyDown(self, key):

        if (key == K_RIGHT):
            self.xMove += self.x_dist
        elif (key == K_LEFT):
            self.xMove += -self.x_dist
        elif (key == K_UP):
            self.yMove += -self.y_dist
        elif (key == K_DOWN):
            self.yMove += self.y_dist

    def KeyUp(self, key):

        if (key == K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == K_LEFT):
            self.xMove += self.x_dist
        elif (key == K_UP):
            self.yMove += self.y_dist
        elif (key == K_DOWN):
            self.yMove += -self.y_dist

    def MonsterCollide(self, monsters):
        if (len(monsters) <= 0):
            return
        for monster in monsters:
            if (monster.scared):
                monster.Eaten()
            else:
                pygame.event.post(pygame.event.Event(PLAYER_EATEN, {}))



    def update(self, block_group, pellet_group, super_pellet_group, monster_group):
        #if not self.dead:
        #    if self.moving_right:
        #        self.xMove += self.x_dist
        #    if self.moving_left:
        #        self.xMove += -self.x_dist
        #    if self.moving_up:
        #        self.yMove += -self.y_dist
        #    if self.moving_down:
        #        self.yMove += self.y_dist
        if (self.xMove == 0) and (self.yMove == 0):
            return
        self.rect.move_ip(self.xMove, self.yMove)


        #time = pygame.time.get_ticks()
        #if abs(self.last_frame - time) > 1000:
        #    self.last_frame = time
        #    self.image_index = (self.image_index + 1) % len(self.images)
        #    self.image = self.images[self.image_index]


        if pygame.sprite.spritecollideany(self, block_group):
            self.rect.move_ip(-self.xMove, -self.yMove)

        first_monsters = pygame.sprite.spritecollide(self, monster_group, False)
        if (len(first_monsters) > 0):
            self.MonsterCollide(first_monsters)
        else:
            pelletCollision = pygame.sprite.spritecollide(self, pellet_group, True)
            if (len(pelletCollision) > 0):
                self.pellets += len(pelletCollision)
            elif (len(pygame.sprite.spritecollide(self, super_pellet_group, True)) > 0):
                self.superState = True
                pygame.event.post(pygame.event.Event(SUPER_STATE_START,{}))
                pygame.time.set_timer(SUPER_STATE_OVER, 0)
                pygame.time.set_timer(SUPER_STATE_OVER, 3000)



