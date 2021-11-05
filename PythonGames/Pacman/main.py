
import level001
from player import *
from monster import Monster
from images import *

BLOCK_SIZE = 16

class main:

    def __init__(self, width=900, height=1200):

        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def gameLoop(self):
        self.LoadSprites()
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.block_sprites.draw(self.screen)
        self.block_sprites.draw(self.background)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.KeyDown(event.key)
                elif event.type == KEYUP:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.KeyUp(event.key)
                elif event.type == SUPER_STATE_OVER:
                    self.player.superState = False
                    pygame.time.set_timer(SUPER_STATE_OVER, 0)
                    for monster in self.monster_sprites.sprites():
                        monster.SetScared(False)
                elif event.type == SUPER_STATE_START:
                    for monster in self.monster_sprites.sprites():
                        monster.SetScared(True)
                elif event.type == PLAYER_EATEN:
                    sys.exit()

            self.player_sprites.update(self.block_sprites, self.pellet_sprites, self.super_pellet_sprites, self.monster_sprites,)
            self.monster_sprites.update(self.block_sprites)


            textpos = 0
            self.screen.blit(self.background, (0, 0))

            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Pellets %s" % self.player.pellets, 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width() / 2)
                self.screen.blit(text,textpos)

            reclist = [textpos]
            reclist += self.pellet_sprites.draw(self.screen)
            reclist += self.super_pellet_sprites.draw(self.screen)
            reclist += self.player_sprites.draw(self.screen)
            reclist += self.monster_sprites.draw(self.screen)

            pygame.display.update(reclist)

    def LoadSprites(self):
        x_offset = (BLOCK_SIZE / 2)
        y_offset = (BLOCK_SIZE / 2)
        level1 = level001.level()
        layout = level1.getLayout()
        img_list = level1.getSprites()

        self.pellet_sprites = pygame.sprite.RenderUpdates()
        self.block_sprites = pygame.sprite.RenderUpdates()
        self.monster_sprites = pygame.sprite.RenderUpdates()
        self.super_pellet_sprites = pygame.sprite.RenderUpdates()

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                centerPoint = [(x * BLOCK_SIZE) + x_offset, (y * BLOCK_SIZE + y_offset)]
                if layout[y][x] == level1.BLOCK:
                    block = centerSprite.Sprite(centerPoint, img_list[level1.BLOCK])
                    self.block_sprites.add(block)
                elif layout[y][x] == level1.PLAYER:
                    self.player = Player(centerPoint, img_list[level1.PLAYER])
                elif layout[y][x] == level1.PELLET:
                    pellet = centerSprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet)
                elif layout[y][x] == level1.BLINKY:
                    blinky = Monster(centerPoint, img_list[level1.BLINKY], img_list[level1.SCARED_MONSTER])
                    self.monster_sprites.add(blinky)
                    pellet = centerSprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet)
                elif layout[y][x] == level1.SUPER_PELLET:
                    super_pellet = centerSprite.Sprite(centerPoint, img_list[level1.SUPER_PELLET])
                    self.super_pellet_sprites.add(super_pellet)

        self.player_sprites = pygame.sprite.RenderUpdates(self.player)


if __name__ == "__main__":
    MainWindow = main()
    MainWindow.gameLoop()