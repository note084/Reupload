import pygame


class Menu():

    def __init__(self, ai_settings, screen):

        self.ai_settings = ai_settings
        self.screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        self.screen.fill(ai_settings.bg_color)
        self.screen_rect = screen.get_rect()

        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.title1_font = pygame.font.SysFont(None, 120)
        self.title2_font = pygame.font.SysFont(None, 80)
        self.font = pygame.font.SysFont(None, 96)
        self.smaller_font = pygame.font.SysFont(None, 40)

        self.title1 = self.title1_font.render("SPACE", True, self.WHITE, self.ai_settings.bg_color)
        self.title1_rect = self.title1.get_rect()
        self.title1_rect.centerx = self.screen_rect.centerx
        self.title1_rect.top = 100

        self.title2 = self.title2_font.render("INVADERS", True, self.GREEN, self.ai_settings.bg_color)
        self.title2_rect = self.title1.get_rect()
        self.title2_rect.centerx = self.screen_rect.centerx
        self.title2_rect.top = 175

        self.monster1_text = self.smaller_font.render(" = 10 PTS", True, self.WHITE, self.ai_settings.bg_color)
        self.monster1_rect = self.monster1_text.get_rect()
        self.monster1_rect.centerx = self.screen_rect.centerx + 100
        self.monster1_rect.top = 300

        self.monster2_text = self.smaller_font.render(" = 20 PTS", True, self.WHITE, self.ai_settings.bg_color)
        self.monster2_rect = self.monster2_text.get_rect()
        self.monster2_rect.centerx = self.screen_rect.centerx + 100
        self.monster2_rect.top = 350

        self.monster3_text = self.smaller_font.render(" = 30 PTS", True, self.WHITE, self.ai_settings.bg_color)
        self.monster3_rect = self.monster3_text.get_rect()
        self.monster3_rect.centerx = self.screen_rect.centerx + 100
        self.monster3_rect.top = 400

        self.monster4_text = self.smaller_font.render(" = ??? PTS", True, self.WHITE, self.ai_settings.bg_color)
        self.monster4_rect = self.monster4_text.get_rect()
        self.monster4_rect.centerx = self.screen_rect.centerx + 100
        self.monster4_rect.top = 450

        self.monster1 = pygame.image.load('images/tentacle0.png')
        self.monster2 = pygame.image.load('images/crab0.png')
        self.monster3 = pygame.image.load('images/octopus0.png')
        self.monster4 = pygame.image.load('images/mothership.png')
        self.monster1_scaled = pygame.transform.scale(self.monster1, (64, 64))
        self.monster2_scaled = pygame.transform.scale(self.monster2, (64, 64))
        self.monster3_scaled = pygame.transform.scale(self.monster3, (64, 64))
        self.monster4_scaled = pygame.transform.scale(self.monster4, (64, 64))



    def create_menu(self):
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        self.screen.fill(self.ai_settings.bg_color)
        self.screen.blit(self.title1, self.title1_rect)
        self.screen.blit(self.title2, self.title2_rect)
        self.screen.blit(self.monster1_text, self.monster1_rect)
        self.screen.blit(self.monster2_text, self.monster2_rect)
        self.screen.blit(self.monster3_text, self.monster3_rect)
        self.screen.blit(self.monster4_text, self.monster4_rect)
        self.screen.blit(self.monster1_scaled, (550, 280))
        self.screen.blit(self.monster2_scaled, (550, 340))
        self.screen.blit(self.monster3_scaled, (550, 390))
        self.screen.blit(self.monster4_scaled, (550, 440))