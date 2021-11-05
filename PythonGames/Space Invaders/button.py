import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 75, 50
        self.button_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (600, 650)

        #highscore rect
        self.rectHS = pygame.Rect(0,0, self.width, self.height)
        self.rectHS.center =(600, 725)

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.msg_imageHS = self.font.render(msg, True, (211,211,211), (0,0,0))
        self.msg_image_rectHS = self.msg_image.get_rect()
        self.msg_image_rectHS.center = self.rectHS.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_highscore(self):
        self.screen.fill((0, 0, 0), self.rectHS)
        self.screen.blit(self.msg_imageHS, self.msg_image_rectHS)